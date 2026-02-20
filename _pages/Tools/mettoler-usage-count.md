---
title: "Mettoler Usage Count"
permalink: /tools/mettoler-usage-count/
layout: single
---

A Python script to count usage statistics from Mettoler output files.

### Features
- Parses Mettoler output
- Counts occurrences and usage metrics
- Exports summary to CSV for further analysis

### Download
[Download Mettoler_usage_count.py]({{site.baseurl}}/scripts/Mettoler_usage_count.py)

### Usage
Run the script with Python 3. Place the Mettoler `.txt` files in the same directory as the script and it will process every `*.txt` found.

```bash
python Mettoler_usage_count.py
```

For each input `*.txt` the script creates a CSV with the same basename (e.g. `sample.txt` → `sample.csv`). No interactive prompts are used.

### Result Example
- Produces a CSV summary with counts per item.


