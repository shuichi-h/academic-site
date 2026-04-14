import pandas as pd
import numpy as np
import os

base_folder = os.path.dirname(os.path.abspath(__file__))

epsilon = 0.75

all_results = []

# ======================
# フォルダ処理
# ======================
for root, dirs, files in os.walk(base_folder):

    xlsx_files = [f for f in files if f.endswith("_processed.xlsx")]

    if len(xlsx_files) == 0:
        continue

    filepath = os.path.join(root, xlsx_files[0])
    folder_name = os.path.basename(root)

    print("📂 Processing:", folder_name)

    try:
        df = pd.read_excel(filepath, sheet_name="Disp_Load")
    except:
        continue

    cols = df.columns

    # ======================
    # 各フォルダFitチェックExcel
    # ======================
    output_path = os.path.join(root, f"{folder_name}_OP_check.xlsx")

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:

        workbook = writer.book

        for i in range(0, len(cols), 2):

            disp = df.iloc[:, i].values
            load = df.iloc[:, i+1].values

            name = cols[i].replace("_Disp", "")

            mask = np.isfinite(disp) & np.isfinite(load)
            disp = disp[mask]
            load = load[mask]

            if len(disp) < 30:
                continue

            # ======================
            # 最大点
            # ======================
            idx_max = np.argmax(load)
            Pmax = load[idx_max]
            hmax = disp[idx_max]

            if hmax <= 0:
                continue

            # ======================
            # Unload抽出
            # ======================
            unload_disp = disp[idx_max:]
            unload_load = load[idx_max:]

            if len(unload_disp) < 15:
                continue

            # ======================
            # フィット範囲（改良版）
            # ======================
            n = max(10, int(len(unload_disp) * 0.4))

            h_fit = unload_disp[:n]
            P_fit = unload_load[:n]

            # ======================
            # フィット
            # ======================
            try:
                coef = np.polyfit(h_fit, P_fit, 1)
                S = coef[0]
                fit_line = np.polyval(coef, h_fit)
            except:
                continue

            if S <= 0:
                continue

            # ======================
            # OP計算
            # ======================
            hc = hmax - epsilon * (Pmax / S)
            if hc <= 0:
                continue

            A = 24.5 * (hc ** 2)
            H = Pmax / A

            all_results.append({
                "Sample": name,
                "Folder": folder_name,
                "Pmax": Pmax,
                "hmax": hmax,
                "S": S,
                "hc": hc,
                "H(OP)": H
            })

            # ======================
            # シート作成
            # ======================
            sheet_name = name[:30]

            df_out = pd.DataFrame({
                "Disp_all": disp,
                "Load_all": load
            })

            df_out.to_excel(writer, sheet_name=sheet_name, index=False)

            ws = writer.sheets[sheet_name]

            # fitデータ書き込み
            ws.write_column(0, 3, h_fit)
            ws.write_column(0, 4, P_fit)
            ws.write_column(0, 5, fit_line)

            # ======================
            # グラフ作成
            # ======================
            chart = workbook.add_chart({"type": "scatter"})

            # 全体
            chart.add_series({
                "name": "All",
                "categories": [sheet_name, 1, 0, len(disp), 0],
                "values":     [sheet_name, 1, 1, len(disp), 1],
                "marker": {"type": "circle", "size": 3, "fill": {"color": "gray"}},
                "line": {"none": True}
            })

            # フィット範囲
            chart.add_series({
                "name": "Fit region",
                "categories": [sheet_name, 1, 3, len(h_fit), 3],
                "values":     [sheet_name, 1, 4, len(h_fit), 4],
                "marker": {"type": "circle", "size": 5, "fill": {"color": "red"}},
                "line": {"none": True}
            })

            # フィット線
            chart.add_series({
                "name": "Fit",
                "categories": [sheet_name, 1, 3, len(h_fit), 3],
                "values":     [sheet_name, 1, 5, len(h_fit), 5],
                "line": {"color": "blue", "width": 2}
            })

            chart.set_x_axis({"name": "Disp (nm)"})
            chart.set_y_axis({"name": "Load (µN)"})
            chart.set_title({"name": name})

            ws.insert_chart("H2", chart)

    print("✅ FitCheck saved:", output_path)


# ======================
# ALL SUMMARY
# ======================
df_all = pd.DataFrame(all_results)

df_all = df_all.sort_values(by=["Folder", "Pmax"], ascending=[True, False])
df_all = df_all.reset_index(drop=True)

summary_path = os.path.join(base_folder, "ALL_SUMMARY_OP.xlsx")

with pd.ExcelWriter(summary_path, engine="xlsxwriter") as writer:

    df_all.to_excel(writer, sheet_name="Summary", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Summary"]

    chart = workbook.add_chart({"type": "scatter"})

    folders = df_all["Folder"].unique()
    colors = ["red","blue","green","orange","purple","black"]

    for i, folder in enumerate(folders):

        df_f = df_all[df_all["Folder"] == folder]
        rows = df_f.index.to_list()

        start = rows[0] + 1
        end = rows[-1] + 1

        chart.add_series({
            "name": folder,
            "categories": ["Summary", start, 3, end, 3],  # hmax
            "values":     ["Summary", start, 6, end, 6],  # H(OP)
            "marker": {"type": "circle", "size": 6, "fill": {"color": colors[i % len(colors)]}},
            "line": {"none": True}
        })

    chart.set_x_axis({"name": "hmax (nm)"})
    chart.set_y_axis({"name": "Hardness (OP)"})

    worksheet.insert_chart("H2", chart)

print("\n🔥 ALL SUMMARY 完成:", summary_path)
