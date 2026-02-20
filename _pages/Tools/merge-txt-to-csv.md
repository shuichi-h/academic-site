---
title: "Merge TXT to CSV"
permalink: /tools/merge-txt-to-csv/
layout: single
---

A utility to merge multiple TXT files into a single CSV file.

### Features
- Reads multiple tab- or comma-delimited TXT files
- Merges rows into a single CSV
- Handles simple header alignment and missing values

### Download
[Download merge_txt_to_csv.py]({{site.baseurl}}/scripts/merge_txt_to_csv.py)

### Usage
This script is configured via variables at the top of the file. Edit `FOLDER`, `COLUMNS`, and `OUTPUT` as needed, then run:

```bash
python merge_txt_to_csv.py
```

- `FOLDER`: directory containing the TXT files (default: `txt_files`)
- `COLUMNS`: list of column names to extract (must match headers exactly)
- `OUTPUT`: output CSV filename

The script reads all `*.txt` in `FOLDER` (tab-separated, header on first line), extracts `COLUMNS`, adds a `sample` column with the source filename, and writes `OUTPUT`.

### Result Example
- Produces a consolidated CSV suitable for spreadsheet or analysis tools.



