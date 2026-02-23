#!/usr/bin/env python3
"""
CSV-only TGA/STA parser

- Input : STARe-exported txt (drag & drop or CLI)
- Output: CSV per Sample ID (same folder)

Features:
- SampleID based CSV naming
- Curve number ($]1[, $]2[, ...) aware reconstruction
- Reconstruct split curves into one continuous curve

# NOTE:
# Curve numbers represent physical step order (1 = first, 4 = last),
# but STARe exports Curve Name blocks in reverse file order.
# Therefore, curves are reconstructed in descending key order
# to restore the correct physical sequence.
for curve_no in sorted(curves_by_no.keys(), key=int, reverse=True):

# Tested on STARe v7.x exports with split curves and reversed Curve Name blocks

"""

from pathlib import Path
import sys
import re
import csv
from typing import Optional, Any
from datetime import datetime

# ---------------------------------------------------------
# Regex
# ---------------------------------------------------------
NUM_RE = re.compile(r"[-+]?\d+[.,]?\d*(?:[eE][-+]?\d+)?")
CURVE_NO_RE = re.compile(r"\$\](\d+)\[")

# ---------------------------------------------------------
# Sample ID normalizer
# ---------------------------------------------------------
def normalize_sample_id(stem: str) -> str:
    if not stem:
        return "sample"

    stem = re.sub(r"[,\s]*\d+[\d.,]*\s*mg\b", "", stem, flags=re.IGNORECASE)
    cleaned = re.sub(r"[^\w\-]+", "_", stem)
    cleaned = re.sub(r"_+", "_", cleaned)

    if not re.match(r"[A-Za-z0-9]", cleaned):
        cleaned = "ID_" + cleaned

    return cleaned.strip("_")

# ---------------------------------------------------------
# Extract scalar from Sample entry
# ---------------------------------------------------------
def extract_scalar_from_sample_entry(sv: Any) -> Optional[str]:
    if sv is None:
        return None
    if isinstance(sv, str):
        return sv.strip()
    if isinstance(sv, dict):
        if "_lines" in sv and sv["_lines"]:
            return sv["_lines"][0].strip()
        if "_value" in sv and sv["_value"]:
            return sv["_value"].strip()
        for k, v in sv.items():
            if not k.startswith("_") and isinstance(v, str) and v.strip():
                return v.strip()
    return None

# ---------------------------------------------------------
# Minimal Results block extractor (STARe v7.x)
# ---------------------------------------------------------
def extract_results_block_v72(lines, start, end):
    result = {}
    i = start

    while i < end:
        ln = lines[i].rstrip()
        if ln.strip().lower().startswith("curve name"):
            break

        m = re.match(r"^\s*([^:]+)\s*:\s*(.*)$", ln)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()

            if key.lower() == "sample":
                values = []
                j = i + 1
                while j < end and (lines[j].startswith(" ") or not lines[j].strip()):
                    if lines[j].strip():
                        values.append(lines[j].strip())
                    j += 1
                result["Sample"] = {"_lines": values} if values else val
                i = j
                continue
        i += 1

    return result

# ---------------------------------------------------------
# Detect device type
# ---------------------------------------------------------
def detect_device(preview: str, first_value: Optional[float]) -> str:
    s = preview.lower()
    if "heat flow" in s or "heatflow" in s:
        return "STA-DSC"
    if "weight" in s:
        return "TGA"
    if first_value is not None:
        if abs(first_value - 100.0) < 0.1 or first_value > 50:
            return "TGA"
        return "STA-DSC"
    return "TGA"

# ---------------------------------------------------------
# Parse curve numeric values
# ---------------------------------------------------------
def parse_curve_values(lines, start, end):
    rows = []
    i = start

    if i < end and re.match(r"\s*[Ii]ndex\b", lines[i]):
        i += 1

    while i < end:
        ln = lines[i].rstrip()
        stripped = ln.strip()

        if not stripped:
            i += 1
            continue
        if stripped.lower().startswith(("results", "curve")):
            break
        if not re.match(r"^\s*\d+(\s|[.,])", ln):
            i += 1
            continue

        ln = ln.replace(",", ".")
        nums = [float(m.group(0)) for m in NUM_RE.finditer(ln)]

        if len(nums) >= 5:
            idx, t, Ts, Tr, val = nums[:5]
        elif len(nums) == 4:
            idx, t, Ts, val = nums
            Tr = None
        elif len(nums) == 3:
            idx, t, val = nums
            Ts = Tr = None
        else:
            i += 1
            continue

        rows.append({
            "Index": idx,
            "Time_s": t,
            "Temp_sample_C": Ts,
            "Temp_reference_C": Tr,
            "Value": val
        })
        i += 1

    return rows

# ---------------------------------------------------------
# Detect percent curve
# ---------------------------------------------------------
def detect_percent_curve(rows):
    vals = [r["Value"] for r in rows if r["Value"] is not None]
    if not vals:
        return False
    avg = sum(vals[:50]) / min(50, len(vals))
    return 95 <= avg <= 105

# ---------------------------------------------------------
# Curve reconstruction by curve number
# ---------------------------------------------------------
def reconstruct_curves_by_curve_no(curves_by_no):
    merged_rows = []
    new_index = 0
    new_time = 0.0
    dt = None

    for curve_no in sorted(curves_by_no.keys(), key=int, reverse=True):
        rows = curves_by_no[curve_no]
        if not rows:
            continue

        if dt is None and len(rows) >= 2:
            t0 = rows[0].get("Time_s")
            t1 = rows[1].get("Time_s")
            if t0 is not None and t1 is not None:
                dt = t1 - t0

        for r in rows:
            r2 = r.copy()
            r2["Index"] = new_index
            r2["Time_s"] = new_time

            merged_rows.append(r2)

            new_index += 1
            if dt is not None:
                new_time += dt

    return merged_rows

# ---------------------------------------------------------
# Merge TGA and DSC curves
# ---------------------------------------------------------
def merge_curves(tga_rows, dsc_rows):
    merged = []
    tga_map = {r["Index"]: r for r in tga_rows}
    dsc_map = {r["Index"]: r for r in dsc_rows}
    all_idx = sorted(tga_map.keys() | dsc_map.keys())

    is_percent = detect_percent_curve(tga_rows)
    init_mg = None
    if not is_percent:
        for r in tga_rows:
            if r["Value"] is not None:
                init_mg = r["Value"]
                break

    for idx in all_idx:
        t = tga_map.get(idx)
        d = dsc_map.get(idx)
        v = t["Value"] if t else None

        row = {
            "Index": idx,
            "Time_s": (t or d).get("Time_s"),
            "Temp_sample_C": (t or d).get("Temp_sample_C"),
            "Temp_reference_C": (t or d).get("Temp_reference_C"),
            "Weight_percent": None,
            "Weight_mg": None,
            "HeatFlow_mW": d["Value"] if d else None,
        }

        if v is not None:
            if is_percent:
                row["Weight_percent"] = v
            else:
                row["Weight_mg"] = v
                if init_mg:
                    row["Weight_percent"] = (v / init_mg) * 100

        merged.append(row)

    return merged

# ---------------------------------------------------------
# Parse file → samples
# ---------------------------------------------------------
def parse_file(path: Path):
    lines = path.read_text(errors="ignore").splitlines()
    n = len(lines)

    curve_idxs = [i for i, ln in enumerate(lines)
                  if ln.strip().lower().startswith("curve name")]

    samples = {}

    for ci_idx, ci in enumerate(curve_idxs):
        end = curve_idxs[ci_idx + 1] if ci_idx + 1 < len(curve_idxs) else n

        values_start = None
        for j in range(ci, end):
            if "curve values" in lines[j].lower():
                values_start = j + 1
                break
        if values_start is None:
            continue

        rows = parse_curve_values(lines, values_start, end)
        if not rows:
            continue

        preview = "".join(lines[ci:ci + 10])
        first_val = next((r["Value"] for r in rows if r["Value"] is not None), None)
        device = detect_device(preview, first_val)

        curve_meta = extract_results_block_v72(lines, values_start, end)
        sample_raw = extract_scalar_from_sample_entry(curve_meta.get("Sample"))
        sample_id = normalize_sample_id(sample_raw or f"sample_{ci_idx}")

        m = CURVE_NO_RE.search(lines[ci])
        curve_no = int(m.group(1)) if m else ci_idx

        samples \
            .setdefault(sample_id, {}) \
            .setdefault(device, {}) \
            .setdefault(curve_no, []) \
            .extend(rows)

    return samples

# ---------------------------------------------------------
# Write CSV
# ---------------------------------------------------------
def write_csv(sample_id: str, merged_rows, base_path: Path):
    out = base_path.parent / f"{sample_id}.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "Index", "Time_s", "Temp_sample_C", "Temp_reference_C",
            "Weight_percent", "Weight_mg", "HeatFlow_mW"
        ])
        for r in merged_rows:
            w.writerow([
                r.get("Index") or "",
                r.get("Time_s") or "",
                r.get("Temp_sample_C") or "",
                r.get("Temp_reference_C") or "",
                r.get("Weight_percent") or "",
                r.get("Weight_mg") or "",
                r.get("HeatFlow_mW") or "",
            ])

def log_usage():
    try:
        with open("usage_log.txt", "a", encoding="utf-8") as f:
            f.write(datetime.now().isoformat(timespec="minutes") + "\n")
    except:
        pass

# ---------------------------------------------------------
# main
# ---------------------------------------------------------
def main():
    log_usage()
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            continue

        samples = parse_file(path)

        for sid, data in samples.items():
            tga_rows = reconstruct_curves_by_curve_no(data.get("TGA", {}))
            dsc_rows = reconstruct_curves_by_curve_no(data.get("STA-DSC", {}))

            merged = merge_curves(tga_rows, dsc_rows)
            write_csv(sid, merged, path)

if __name__ == "__main__":
    main()
