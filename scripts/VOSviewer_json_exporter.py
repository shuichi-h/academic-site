import json
import pandas as pd

# JSONファイルを正しく指定
with open("VOSviewer-network.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["network"]["items"]

df = pd.DataFrame([
    {
        "label": item["label"],
        "occurrences": item["weights"]["Occurrences"],
        "cluster": item["cluster"],
        "x": item["x"],
        "y": item["y"],
        "avg_pub_year": item["scores"].get("Avg. pub. year"),
        "avg_citations": item["scores"].get("Avg. citations"),
        "avg_norm_citations": item["scores"].get("Avg. norm. citations"),
    }
    for item in items
])

df["rank"] = df["occurrences"].rank(method="dense", ascending=False).astype(int)
df = df.sort_values("rank")

print(df.head())
print(f"Total keywords: {len(df)}")

df.to_csv("keyword_ranking_full.csv", index=False)