from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent

for txt in BASE_DIR.glob("*.txt"):
    print(f"Processing: {txt.name}")

    try:
        lines = txt.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        lines = txt.read_text(encoding="latin-1").splitlines()

    rows = []
    current = {}

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # --- 新しい測定ブロック ---
        if line.startswith("Curve Name"):
            if current:
                rows.append(current)
                current = {}

            # Curve Name は次の行
            if i + 1 < len(lines):
                current["Curve Name"] = lines[i + 1].strip()

            i += 2
            continue

        # --- Performed は同じ行 ---
        if line.startswith("Performed"):
            current["Performed"] = line.replace("Performed", "").strip()
            i += 1
            continue

        # --- User は次の行 ---
        if line.startswith("User"):
            if i + 1 < len(lines):
                current["User"] = lines[i + 1].strip()
            i += 2
            continue

        i += 1

    if current:
        rows.append(current)

    if not rows:
        print("  ⚠ データなし（スキップ）")
        continue

    df = pd.DataFrame(rows)
    out = txt.with_suffix(".csv")
    df.to_csv(out, index=False)

    print(f"  ✔ Created: {out.name}")

print("=== ALL DONE ===")
