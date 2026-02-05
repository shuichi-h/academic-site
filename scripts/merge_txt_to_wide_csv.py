import pandas as pd
import glob
import os

# ===== 設定 =====
FOLDER = "txt_files"      # TXTファイルのフォルダ
X_COL = "Time(s)"            # 共通のX軸列名
Y_COL = "J(Pa-1)"           # プロットしたいY列名
OUTPUT = "merged_wide.csv"
# =================

wide_df = None

for filepath in sorted(glob.glob(os.path.join(FOLDER, "*.txt"))):
    sample = os.path.splitext(os.path.basename(filepath))[0]

    df = pd.read_csv(filepath, sep="\t")
    df = df[[X_COL, Y_COL]].copy()
    df = df.rename(columns={Y_COL: sample})

    if wide_df is None:
        wide_df = df
    else:
        wide_df = pd.merge(
            wide_df,
            df,
            on=X_COL,
            how="outer"
        )

# X軸で並び替え
wide_df = wide_df.sort_values(by=X_COL)

# CSV出力
wide_df.to_csv(OUTPUT, index=False)

print(f"Saved: {OUTPUT}")
