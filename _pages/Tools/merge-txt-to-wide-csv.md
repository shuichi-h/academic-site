---
title: "Merge TXT to Wide CSV"
permalink: /tools/merge-txt-to-wide-csv/
layout: single
---

A script to merge multiple TXT inputs into a wide-format CSV (one row per record with many columns).

### Features
- Converts long-form TXT records into wide CSV layout
- Useful for reshaping data for analysis or spreadsheets

### Download
[Download merge_txt_to_wide_csv.py]({{site.baseurl}}/scripts/merge_txt_to_wide_csv.py)

### Usage
This script is configured via variables at the top of the file. Edit `FOLDER`, `X_COL`, `Y_COL`, and `OUTPUT` as needed, then run:

```bash
python merge_txt_to_wide_csv.py
```

- `FOLDER`: directory containing the TXT files (default: `txt_files`)
- `X_COL`: the common X-axis column name (e.g. `Time(s)`)
- `Y_COL`: the Y column to pivot into wide columns (e.g. `J(Pa-1)`)
- `OUTPUT`: output CSV filename (default: `merged_wide.csv`)

The script reads each `*.txt` in `FOLDER`, keeps only `[X_COL, Y_COL]`, renames the Y column to the sample name, merges on `X_COL` (outer join), sorts by `X_COL`, and writes `OUTPUT`.

### Result Example
- Produces a wide-format CSV aggregating fields across inputs.


