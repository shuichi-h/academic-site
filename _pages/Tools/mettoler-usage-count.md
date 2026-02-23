---
title: "Mettoler Usage Count"
permalink: /tools/mettoler-usage-count/
layout: single
---

A Python script to count usage statistics from Mettoler output files.

### Features
- Can sort all users experimental information by curve name, date and user name.

### Download
[Download Mettoler_usage_count.py]({{site.baseurl}}/scripts/Mettoler_usage_count.py)

### Usage
Run the script with Python 3. Place the Mettoler `.txt` files in the same directory as the script and it will process every `*.txt` found.

For each input `*.txt` the script creates a CSV with the same basename (e.g. `sample.txt` → `sample.csv`). No interactive prompts are used.

Mettoler `.txt` files can be obtained from Mettoler software, and it needs to contain only user name and curve name.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-02-20-17-40-10.png)

