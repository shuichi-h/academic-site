---
title: "CV Markdown to JSON"
permalink: /tools/cv-markdown-to-json/
layout: single
---


A small utility to convert CV entries written in Markdown into a JSON structure compatible with the site CV format.

### Features
- Reads Markdown-formatted CV entries
- Converts front-matter and content into structured JSON
- Useful for programmatic CV updates and resume export

### Download
[Download cv_markdown_to_json.py]({{site.baseurl}}/scripts/cv_markdown_to_json.py)

### Usage
This script requires explicit input and output paths. Example:

```bash
python cv_markdown_to_json.py --input path/to/cv.md --output path/to/cv.json --config path/to/_config.yml
```

- `--input/-i`: path to the Markdown CV file to convert (required)
- `--output/-o`: path to write the JSON file (required)
- `--config/-c`: optional Jekyll `_config.yml` to enrich author info

The script infers the repository root as the parent directory of the input file's folder and writes the structured JSON to `--output`.

### Result Example
- Outputs `cv.json` that can be used by the site templates.



````
