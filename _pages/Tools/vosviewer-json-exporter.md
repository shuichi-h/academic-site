---
title: "VOSviewer JSON Exporter"
permalink: /tools/vosviewer-json-exporter/
layout: single
---

A Python script to process VOSviewer JSON output files and export keyword distances and cluster information to CSV for quantitative analysis.

### Features
- Parses VOSviewer JSON files
- Extracts keyword distances and cluster assignments
- Exports to CSV format for further analysis
- Useful for comparing field structures across different literature searches

### Download
[Download VOSviewer_json_exporter.py]({{site.baseurl}}/scripts/VOSviewer_json_exporter.py)

### Usage
Run the script with Python 3.

Place the VOSviewer JSON file named `VOSviewer-network.json` in the same folder as the script (or edit the filename inside the script), then run:

```bash
python VOSviewer_json_exporter.py
```

The script reads `VOSviewer-network.json`, prints a preview, and writes `keyword_ranking_full.csv` in the current directory.

### Result Example
![image](/academic-site/images/images_pages_posts/img_2026-01-17-23-21-01.png)


