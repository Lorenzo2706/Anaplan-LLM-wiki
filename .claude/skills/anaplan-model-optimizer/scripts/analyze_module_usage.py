"""
Cross-reference a scraper_ux.py NUX report against a model's raw CSV export
to find modules that are genuinely unused, as opposed to modules that are
merely absent from the new-UX pages/boards by design (Data/Load/Calculation
modules in the DISCO pattern are normal to have zero NUX exposure - they feed
other modules via formulas instead).

A module is only reported as a deletion candidate when ALL of these are true:
  - zero NUX usage (Modules Usage Count sheet == 0)
  - not referenced by any other module's formula (Modules.csv "Referenced By")
  - not used in a classic dashboard (Modules.csv "Used in Dashboards")
  - not the source/target of an import or export (Imports.csv, and the
    Excel's per-model Actions detail sheet)

Usage:
    python analyze_module_usage.py --excel "<path to NUX report.xlsx>" \
        --model-dir "raw/models/<Model Name>" \
        [--out-json report.json] [--out-markdown report.md]

Always prints a markdown report to stdout.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

FIXED_SHEETS = {"All Views", "Actions Usage Report", "Views Usage Report", "Modules Usage Count"}
SECTION_HEADER_PREFIX = "◼"  # "◼️" - pseudo-header rows like "◼️ LOAD MODULES"


def _read_csv_rows(path: Path, delimiter_candidates=(",", ";")):
    if not path.is_file():
        return []
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    try:
        dialect = csv.Sniffer().sniff(raw.splitlines()[0], delimiters="".join(delimiter_candidates))
        delimiter = dialect.delimiter
    except Exception:
        delimiter = delimiter_candidates[0]
    reader = csv.DictReader(raw.splitlines(), delimiter=delimiter)
    return list(reader)


def _extract_names(field: str) -> list:
    if not field or not field.strip():
        return []
    quoted = re.findall(r"'([^']+)'", field)
    if quoted:
        return [q.strip() for q in quoted]
    return [p.strip() for p in field.split(",") if p.strip()]


def load_modules_csv(model_dir: Path) -> dict:
    rows = _read_csv_rows(model_dir / "Modules.csv")
    modules = {}
    for row in rows:
        name = (row.get("") or "").strip()
        # Anaplan pads section-header rows (e.g. "◼️ CALCULATION MODULES") with
        # leading U+2800 (braille pattern blank) characters, so a plain
        # startswith() on the glyph misses them - strip that padding first.
        stripped = name.lstrip("⠀ \t")
        if not stripped or stripped.startswith(SECTION_HEADER_PREFIX):
            continue
        modules[name] = {
            "functional_area": (row.get("Functional Area") or "").strip(),
            "referenced_by": _extract_names(row.get("Referenced By", "")),
            "used_in_dashboards_classic": bool((row.get("Used in Dashboards") or "").strip()),
        }
    return modules


def load_imports_csv(model_dir: Path) -> set:
    rows = _read_csv_rows(model_dir / "Imports.csv")
    used = set()
    for row in rows:
        if (row.get("Target Type") or "").strip().upper() == "MODULE":
            tgt = (row.get("Target Object") or "").strip()
            if tgt:
                used.add(tgt)
        if (row.get("Source Type") or "").strip().upper() == "MODULE":
            src = (row.get("Source Object") or "").strip()
            if src:
                used.add(src)
    return used


def load_excel(excel_path: Path):
    wb = load_workbook(excel_path, data_only=True, read_only=True)

    ux_counts = {}
    if "Modules Usage Count" in wb.sheetnames:
        ws = wb["Modules Usage Count"]
        rows = list(ws.iter_rows(values_only=True))
        for row in rows[1:]:
            if not row or row[0] is None:
                continue
            name, _id, count = (row + (None, None, None))[:3]
            ux_counts[str(name).strip()] = int(count) if count is not None else 0

    action_usage = set()
    action_sheet_names = [s for s in wb.sheetnames if s not in FIXED_SHEETS]
    if len(action_sheet_names) == 1:
        ws = wb[action_sheet_names[0]]
        rows = list(ws.iter_rows(values_only=True))
        if rows:
            header = [str(h) if h is not None else "" for h in rows[0]]
            idx = {h: i for i, h in enumerate(header)}
            for row in rows[1:]:
                if not row or not any(row):
                    continue
                if idx.get("Target Type") is not None and str(row[idx["Target Type"]] or "").strip().upper() == "MODULE":
                    tgt = str(row[idx["Target Object"]] or "").strip()
                    if tgt:
                        action_usage.add(tgt)
                if idx.get("Source Type") is not None and str(row[idx["Source Type"]] or "").strip().upper() == "MODULE":
                    src = str(row[idx["Source Object"]] or "").strip()
                    if src:
                        action_usage.add(src)
    elif len(action_sheet_names) > 1:
        print(
            f"WARNING: expected exactly one non-fixed sheet for the per-model actions "
            f"detail, found {action_sheet_names}. Skipping the Excel-based action-usage signal "
            f"(Imports.csv is still used).",
            file=sys.stderr,
        )

    wb.close()
    return ux_counts, action_usage


def analyze(excel_path: Path, model_dir: Path) -> dict:
    modules = load_modules_csv(model_dir)
    if not modules:
        raise SystemExit(f"No modules found in {model_dir / 'Modules.csv'} - check the path.")

    imports_usage = load_imports_csv(model_dir)
    ux_counts, excel_action_usage = load_excel(excel_path)
    used_in_actions_all = imports_usage | excel_action_usage

    results = []
    for name, meta in modules.items():
        ux_count = ux_counts.get(name)
        entry = {
            "name": name,
            "functional_area": meta["functional_area"],
            "ux_count": ux_count,
            "referenced_by": meta["referenced_by"],
            "used_in_dashboards_classic": meta["used_in_dashboards_classic"],
            "used_in_actions": name in used_in_actions_all,
        }

        if ux_count is None:
            entry["verdict"] = "DATA MISMATCH - not found in NUX report; verify the module name matches exactly"
        elif ux_count > 0:
            entry["verdict"] = "ACTIVE - used in NUX pages/boards"
        elif meta["referenced_by"]:
            entry["verdict"] = "KEEP - feeds other modules via formula"
        elif meta["used_in_dashboards_classic"]:
            entry["verdict"] = "KEEP - used in a classic dashboard"
        elif entry["used_in_actions"]:
            entry["verdict"] = "KEEP - used as an import/export source or target"
        else:
            entry["verdict"] = "CANDIDATE FOR REVIEW - no NUX usage, no formula reference, no dashboard usage, no action usage found"

        results.append(entry)

    results.sort(key=lambda e: (e["verdict"] != "CANDIDATE FOR REVIEW - no NUX usage, no formula reference, no dashboard usage, no action usage found", e["functional_area"], e["name"]))
    return {
        "modules": results,
        "summary": {
            "total_modules": len(results),
            "candidates_for_review": sum(1 for e in results if e["verdict"].startswith("CANDIDATE")),
            "active_in_ux": sum(1 for e in results if e["verdict"].startswith("ACTIVE")),
            "kept_internal_dependency": sum(1 for e in results if e["verdict"].startswith("KEEP")),
            "data_mismatches": sum(1 for e in results if e["verdict"].startswith("DATA MISMATCH")),
        },
    }


def to_markdown(report: dict, model_name: str) -> str:
    s = report["summary"]
    lines = [
        f"# Module optimization analysis - {model_name}",
        "",
        f"- Total modules: {s['total_modules']}",
        f"- Active in NUX: {s['active_in_ux']}",
        f"- Kept (internal dependency - formula/dashboard/action usage): {s['kept_internal_dependency']}",
        f"- **Candidates for review: {s['candidates_for_review']}**",
        f"- Data mismatches (name not found in NUX report): {s['data_mismatches']}",
        "",
    ]

    candidates = [e for e in report["modules"] if e["verdict"].startswith("CANDIDATE")]
    if candidates:
        lines += ["## Candidates for review", "", "| Module | Functional Area |", "|---|---|"]
        for e in candidates:
            lines.append(f"| {e['name']} | {e['functional_area']} |")
        lines.append("")

    mismatches = [e for e in report["modules"] if e["verdict"].startswith("DATA MISMATCH")]
    if mismatches:
        lines += ["## Data mismatches (need manual check)", "", "| Module | Functional Area |", "|---|---|"]
        for e in mismatches:
            lines.append(f"| {e['name']} | {e['functional_area']} |")
        lines.append("")

    kept = [e for e in report["modules"] if e["verdict"].startswith("KEEP")]
    if kept:
        lines += ["## Kept - internal dependency (zero NUX usage but still load-bearing)", "",
                   "| Module | Functional Area | Reason |", "|---|---|---|"]
        for e in kept:
            reason = e["verdict"].split(" - ", 1)[1]
            lines.append(f"| {e['name']} | {e['functional_area']} | {reason} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--excel", required=True, type=Path)
    parser.add_argument("--model-dir", required=True, type=Path)
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--out-json", type=Path, default=None)
    parser.add_argument("--out-markdown", type=Path, default=None)
    args = parser.parse_args()

    model_name = args.model_name or args.model_dir.name
    report = analyze(args.excel, args.model_dir)
    md = to_markdown(report, model_name)

    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.out_markdown:
        args.out_markdown.parent.mkdir(parents=True, exist_ok=True)
        args.out_markdown.write_text(md, encoding="utf-8")

    try:
        print(md)
    except UnicodeEncodeError:
        print(md.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


if __name__ == "__main__":
    main()
