import pandas as pd
import numpy as np
import os

base_folder = os.path.dirname(os.path.abspath(__file__))

# ======================
# ⚙️ パラメータ（ここ調整）
# ======================
OFFSET_MIN = 1.5
OFFSET_MAX = 2.5

CONTACT_START = 2.0   # preload除外
SMOOTH_WINDOW = 5

THRESHOLD_LOAD = 0.3
THRESHOLD_SLOPE = 0.05
MIN_POINTS = 5


# ======================
# 接触検出（ロバスト版）
# ======================
def detect_contact(time, load_corr):

    mask = time > CONTACT_START

    if np.sum(mask) < 10:
        return None

    t_sub = time[mask]
    l_sub = load_corr[mask]

    # 平滑化
    l_smooth = pd.Series(l_sub).rolling(SMOOTH_WINDOW, center=True).mean().values

    # NaN除去（端）
    valid = np.isfinite(l_smooth)
    t_sub = t_sub[valid]
    l_smooth = l_smooth[valid]

    if len(l_smooth) < 10:
        return None

    # 勾配
    dl = np.gradient(l_smooth, t_sub)

    # 条件
    candidates = np.where(
        (l_smooth > THRESHOLD_LOAD) &
        (dl > THRESHOLD_SLOPE)
    )[0]

    # 連続領域検出
    for i in range(len(candidates) - MIN_POINTS):
        window = candidates[i:i+MIN_POINTS]
        if np.all(np.diff(window) == 1):
            idx_local = window[0]
            break
    else:
        return None

    # 元indexに戻す
    idx_contact = np.where(mask)[0][valid][idx_local]

    return idx_contact


# ======================
# 処理関数
# ======================
def process_curve(time, load, disp):

    # --- Load補正 ---
    mask_offset = (time > OFFSET_MIN) & (time < OFFSET_MAX)
    if np.sum(mask_offset) < 5:
        return None, None

    load_offset = np.mean(load[mask_offset])
    load_corr = load - load_offset

    # --- 接触検出 ---
    idx_contact = detect_contact(time, load_corr)

    if idx_contact is None:
        return None, None

    # --- Disp補正 ---
    disp_contact = disp[idx_contact]
    disp_corr = disp - disp_contact

    return load_corr, disp_corr


# ======================
# フォルダ処理
# ======================
for root, dirs, files in os.walk(base_folder):

    txt_files = [f for f in files if f.endswith(".txt") and f.startswith("Method")]

    if len(txt_files) == 0:
        continue

    folder_name = os.path.basename(root)
    print("📂 Processing:", folder_name)

    raw_cols = {}
    proc_cols = {}
    disp_load_cols = {}

    for file in txt_files:

        filepath = os.path.join(root, file)
        name = os.path.splitext(file)[0]

        try:
            with open(filepath, "r", encoding="latin-1") as f:
                lines = f.readlines()

            header_idx = next(i for i, l in enumerate(lines) if "Depth (nm)" in l)

            df = pd.read_csv(
                filepath,
                sep="\t",
                skiprows=header_idx,
                encoding="latin-1"
            )

            df.columns = df.columns.str.strip()

            if not all(col in df.columns for col in ["Depth (nm)", "Load (µN)", "Time (s)"]):
                continue

            time = df["Time (s)"].values
            load = df["Load (µN)"].values
            disp = df["Depth (nm)"].values

            # ======================
            # Raw
            # ======================
            raw_cols[f"{name}_Time"] = pd.Series(time)
            raw_cols[f"{name}_Load"] = pd.Series(load)
            raw_cols[f"{name}_Disp"] = pd.Series(disp)

            # ======================
            # Process
            # ======================
            load_corr, disp_corr = process_curve(time, load, disp)

            if load_corr is None:
                continue

            mask = np.isfinite(load_corr) & np.isfinite(disp_corr)

            load_corr = load_corr[mask]
            disp_corr = disp_corr[mask]
            time_corr = time[mask]

            proc_cols[f"{name}_Time"] = pd.Series(time_corr)
            proc_cols[f"{name}_Load"] = pd.Series(load_corr)
            proc_cols[f"{name}_Disp"] = pd.Series(disp_corr)

            disp_load_cols[f"{name}_Disp"] = pd.Series(disp_corr)
            disp_load_cols[f"{name}_Load"] = pd.Series(load_corr)

        except Exception as e:
            print("skip:", file, e)

    if len(proc_cols) == 0:
        continue

    df_raw = pd.DataFrame(raw_cols)
    df_proc = pd.DataFrame(proc_cols)
    df_dl = pd.DataFrame(disp_load_cols)

    # ======================
    # 出力（フォルダ名付き）
    # ======================
    output_name = f"{folder_name}_processed.xlsx"
    output_path = os.path.join(root, output_name)

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:

        df_raw.to_excel(writer, sheet_name="Raw", index=False)
        df_proc.to_excel(writer, sheet_name="Process", index=False)
        df_dl.to_excel(writer, sheet_name="Disp_Load", index=False)

        workbook = writer.book

        # ======================
        # Processグラフ
        # ======================
        ws_proc = writer.sheets["Process"]

        chart1 = workbook.add_chart({"type": "scatter", "subtype": "straight"})

        for i in range(0, len(df_proc.columns), 3):

            time_col = i
            load_col = i + 1

            chart1.add_series({
                "name": df_proc.columns[load_col],
                "categories": ["Process", 1, time_col, len(df_proc), time_col],
                "values":     ["Process", 1, load_col, len(df_proc), load_col],
            })

        chart1.set_x_axis({"name": "Time (s)"})
        chart1.set_y_axis({"name": "Load (µN)"})
        chart1.set_title({"name": "Processed Time Curves"})

        ws_proc.insert_chart("E2", chart1)

        # ======================
        # Disp vs Load
        # ======================
        ws_dl = writer.sheets["Disp_Load"]

        chart2 = workbook.add_chart({"type": "scatter", "subtype": "straight"})

        for i in range(0, len(df_dl.columns), 2):

            disp_col = i
            load_col = i + 1

            chart2.add_series({
                "name": df_dl.columns[load_col],
                "categories": ["Disp_Load", 1, disp_col, len(df_dl), disp_col],
                "values":     ["Disp_Load", 1, load_col, len(df_dl), load_col],
            })

        chart2.set_x_axis({"name": "Disp (nm)"})
        chart2.set_y_axis({"name": "Load (µN)"})
        chart2.set_title({"name": "Disp vs Load"})

        ws_dl.insert_chart("E2", chart2)

    print("✅ saved:", output_path)

print("\n🔥 完了")
