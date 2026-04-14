import pandas as pd
import numpy as np
import os

# ======================
# 設定
# ======================
file_path = "ALL_SUMMARY_OP.xlsx"
h_target = 20
H_FQ_lit = 9.25  # GPa

# ======================
# 読み込み
# ======================
df = pd.read_excel(file_path, sheet_name="Summary")

df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=["H(OP)", "hmax"])
df = df[(df["H(OP)"] > 0) & (df["H(OP)"] < 1)]

# ======================
# 出力
# ======================
output_path = "SUMMARY_trend_exp.xlsx"

results = []

with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:

    workbook = writer.book

    # ======================
    # フォルダごと処理
    # ======================
    for folder in df["Folder"].unique():

        df_sub = df[df["Folder"] == folder].copy()

        x = df_sub["hmax"].values
        y = df_sub["H(OP)"].values

        if len(x) < 5:
            continue

        # ======================
        # expフィット
        # ======================
        logy = np.log(y)

        coef = np.polyfit(x, logy, 1)
        B, logA = coef
        A = np.exp(logA)

        # フィット線
        x_fit = np.linspace(min(x), max(x), 100)
        y_fit = A * np.exp(B * x_fit)

        # 20nm値
        H20 = A * np.exp(B * h_target)

        results.append({
            "Folder": folder,
            "A": A,
            "B": B,
            "H_20nm (raw)": H20,
            "N": len(x)
        })

        # ======================
        # Excel書き出し
        # ======================
        sheet_name = folder[:30]

        df_out = pd.DataFrame({
            "hmax": x,
            "H(OP)": y
        })

        df_out.to_excel(writer, sheet_name=sheet_name, index=False)

        ws = writer.sheets[sheet_name]

        # フィットデータ
        ws.write_column(0, 3, x_fit)
        ws.write_column(0, 4, y_fit)

        # ======================
        # グラフ
        # ======================
        chart = workbook.add_chart({"type": "scatter"})

        # データ点
        chart.add_series({
            "name": "Data",
            "categories": [sheet_name, 1, 0, len(x), 0],
            "values":     [sheet_name, 1, 1, len(x), 1],
            "marker": {"type": "circle", "size": 5},
            "line": {"none": True}
        })

        # フィット線
        chart.add_series({
            "name": "Fit",
            "categories": [sheet_name, 1, 3, len(x_fit), 3],
            "values":     [sheet_name, 1, 4, len(x_fit), 4],
            "line": {"color": "black", "width": 2}
        })

        # 軸
        chart.set_x_axis({"name": "hmax (nm)"})
        chart.set_y_axis({
            "name": "Hardness (OP)",
            "log_base": 10
        })

        # 式表示（これ重要）
        eq_text = f"y = {A:.3e} * exp({B:.3e} x)"
        chart.set_title({"name": eq_text})

        ws.insert_chart("H2", chart)

    # ======================
    # Summary作成
    # ======================
    summary = pd.DataFrame(results)

    # FQ補正
    fq_row = summary[summary["Folder"].str.contains("FQ", case=False)]

    if len(fq_row) == 0:
        raise ValueError("FQ not found")

    H_FQ_measured = fq_row["H_20nm (raw)"].values[0]
    k = H_FQ_lit / H_FQ_measured

    summary["H_20nm (GPa)"] = summary["H_20nm (raw)"] * k

    summary.to_excel(writer, sheet_name="Summary", index=False)

    # ======================
    # Summaryグラフ
    # ======================
    ws_sum = writer.sheets["Summary"]

    chart2 = workbook.add_chart({"type": "column"})

    chart2.add_series({
        "name": "H @20nm",
        "categories": ["Summary", 1, 0, len(summary), 0],
        "values":     ["Summary", 1, 5, len(summary), 5],
        "data_labels": {"value": True}
    })

    chart2.set_title({"name": "Hardness @20nm (Corrected)"})
    chart2.set_y_axis({"name": "Hardness (GPa)"})

    ws_sum.insert_chart("H2", chart2)

print("\n🔥 完成:", output_path)
