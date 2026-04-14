---
title: "Nanoindentation Processing Toolkit: Processing, Oliver–Pharr Analysis, and Depth-Dependent Hardness Evaluation"
permalink: /tools/nanoindentation-processing-toolkit/
layout: single
---

A comprehensive Python-based toolkit for processing nanoindentation data, performing Oliver–Pharr analysis, and analyzing depth-dependent mechanical properties.

## Downloads

- [Download process_from_txt.py]({{site.baseurl}}/scripts/process_from_txt.py)
- [Download make_summary_OP_full.py]({{site.baseurl}}/scripts/make_summary_OP_full.py)
- [Download OP_trend.py]({{site.baseurl}}/scripts/OP_trend.py)

## Core Scripts

These scripts form the main workflow for nanoindentation data analysis.

---

### 1. `process_from_txt.py`

**Purpose:**  
Convert raw nanoindentation TXT files into structured and normalized Excel data.

**Main functions:**
- Detect contact point (robust method)
- Correct load offset
- Normalize displacement (Disp = 0 at contact)
- Generate processed datasets

**Input:**
- Raw `.txt` files (nanoindentation output)

**Output:**
- `<folder_name>_processed.xlsx`

**Sheets:**
- `Raw` – original data  
- `Process` – corrected time-based data  
- `Disp_Load` – displacement vs load curves  

---

### 2. `make_summary_OP_full.py`

**Purpose:**  
Perform Oliver–Pharr analysis and generate a full dataset with fitting validation.

**Main functions:**
- Extract unloading curves
- Linear fit of unloading region
- Calculate:
  - Stiffness (S)
  - Contact depth (hc)
  - Hardness (H)
- Generate fit-check plots for each curve
- Compile all results into a single summary

**Input:**
- `_processed.xlsx` (Disp_Load sheet)

**Output:**
- `<folder>_OP_check.xlsx` (per folder, with fit visualization)
- `ALL_SUMMARY_OP.xlsx` (combined dataset)

---

### 3. `OP_trend.py`

**Purpose:**  
Analyze depth dependence of hardness and estimate values at a fixed depth.

**Main functions:**
- Fit hardness vs depth using exponential model:

  $$H = A \cdot \exp(Bh)$$

- Extract hardness at target depth (e.g., 20 nm)
- Normalize results using fused quartz (FQ) reference

**Input:**
- `ALL_SUMMARY_OP.xlsx`

**Output:**
- `SUMMARY_trend_exp.xlsx`

**Includes:**
- Per-folder fitting plots  
- Fitting parameters (A, B)  
- Hardness at target depth  
- FQ-corrected hardness  

---

## Workflow

Run scripts in the following order:

1. **`process_from_txt.py`** – Preprocess raw data
2. **`make_summary_OP_full.py`** – Generate Oliver–Pharr results
3. **`OP_trend.py`** – Analyze depth trends and normalize
