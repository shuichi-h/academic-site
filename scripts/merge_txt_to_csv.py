import pandas as pd
import glob
import os
"""
============================================================
使い方メモ（merge_txt_to_csv.py）
============================================================

【目的】
複数のタブ区切り・ヘッダ付き TXT ファイルから
指定した列だけを抜き出し、1つの CSV ファイルにまとめる。

------------------------------------------------------------
【前提条件】
- TXT はタブ区切り（\t）
- 1行目にヘッダ（列名）がある
- 抽出したい列名は、すべての TXT で共通
- TXT ファイルは同一フォルダに入っている

------------------------------------------------------------
【フォルダ構成】
project/
├─ merge_txt_to_csv.py   ← このスクリプト
└─ txt_files/            ← TXTファイルを入れる
   ├─ sample1.txt
   ├─ sample2.txt

------------------------------------------------------------
【設定（ここだけ編集すればよい）】

1) FOLDER
   TXTファイルを入れたフォルダ名
   通常は変更不要

2) COLUMNS（最重要）
   抽出したい列名をリストで指定する
   列名は TXT のヘッダと完全一致させること
   並び順は出力CSVの列順になる

   例：
   COLUMNS = ["Time", "Stress", "Strain"]

3) OUTPUT
   出力される CSV ファイル名
   条件名や日付を入れてもよい

------------------------------------------------------------
【実行方法】
VS Code で project フォルダを開き、Terminal で以下を実行：

    python merge_txt_to_csv.py

------------------------------------------------------------
【出力】
- merged.csv が project フォルダ直下に作成される
- 列構成：
    [指定した列] + sample

  sample 列には、TXTファイル名（拡張子なし）が入る
  → 作図時のグループ分けに使用可能

------------------------------------------------------------
【よくあるエラー】
- COLUMNS に指定した列名が TXT に存在しない
- タブ区切りではない TXT を使っている
- txt_files フォルダの場所が違う

------------------------------------------------------------
【補足】
この CSV は以下にそのまま使用できる：
- Excel / LibreOffice
- Origin
- Python (pandas, seaborn)
- Dash / データベース用中間データ

============================================================
"""

# ===== 設定 =====
FOLDER = "txt_files"              # TXTファイルのフォルダ
COLUMNS = ["Time(s)", "J(Pa-1)"]       # 抜き出す列名
OUTPUT = "merged.csv"             # 出力CSV
# =================

dfs = []

for filepath in glob.glob(os.path.join(FOLDER, "*.txt")):
    df = pd.read_csv(filepath, sep="\t")

    out = df[COLUMNS].copy()
    out["sample"] = os.path.splitext(os.path.basename(filepath))[0]

    dfs.append(out)

result = pd.concat(dfs, ignore_index=True)

result.to_csv(OUTPUT, index=False)

print(f"Saved: {OUTPUT}")



