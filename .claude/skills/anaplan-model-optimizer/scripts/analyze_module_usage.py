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

# Manual deletion markers: model-owner intent captured in free-text Notes, or
# (at module level) a Functional Area that itself reads "DELETE". Detection
# here is purely additive - it must never suppress the reference/front-end
# safety check, only annotate the result (see analyze() / analyze_line_items()).
DELETE_MARKER_KEYWORDS = ["delete", "to be deleted", "obsolete", "deprecated", "remove"]


def detect_manual_marker(notes: str, functional_area: str = "") -> dict:
    """Scan Notes/Functional Area for a model-owner deletion marker.

    Returns {"flagged": bool, "reasons": [str, ...]}. Never returns more than
    one Notes-derived reason and one Functional-Area-derived reason, even if
    several keywords independently match the same Notes text.
    """
    notes_l = (notes or "").lower()
    matched_keywords = [kw for kw in DELETE_MARKER_KEYWORDS if kw in notes_l]
    reasons = []
    if matched_keywords:
        reasons.append("Notes: " + ", ".join(f"'{kw}'" for kw in matched_keywords))
    if "delete" in (functional_area or "").lower():
        reasons.append("Functional Area contains 'DELETE'")
    return {"flagged": bool(reasons), "reasons": reasons}


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
        functional_area = (row.get("Functional Area") or "").strip()
        notes = (row.get("Notes") or "").strip()
        modules[name] = {
            "functional_area": functional_area,
            "referenced_by": _extract_names(row.get("Referenced By", "")),
            "used_in_dashboards_classic": bool((row.get("Used in Dashboards") or "").strip()),
            "notes": notes,
            "manual_marker": detect_manual_marker(notes, functional_area),
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


def load_line_items_csv(model_dir: Path) -> dict:
    """Load Line Items.csv keyed by (module_name, line_item_name).

    Line Items.csv carries its own per-line-item "Referenced By" and "Notes"
    columns - unlike Modules.csv's aggregate signals, these are already at
    the exact grain Pass 2 needs, no extraction/aggregation required.
    """
    rows = _read_csv_rows(model_dir / "Line Items.csv")
    items = {}
    for row in rows:
        name = (row.get("") or "").strip()
        module_name = (row.get("Module Name") or "").strip()
        if not name or not module_name:
            continue
        items[(module_name, name)] = {
            "notes": (row.get("Notes") or "").strip(),
            "referenced_by": _extract_names(row.get("Referenced By", "")),
        }
    return items


_DOTTED_REFERENCE_RE = re.compile(r"'([^']+)'\.(.+)$")


def _parse_dotted_reference(obj: str):
    """Extract (module_name, line_item_name) from an Imports.csv Source/Target
    Object string's final path segment, e.g.
    "Data Hub 2.0 / 'SYS 05. Date of Today'.Date MBH Master Data" ->
    ("SYS 05. Date of Today", "Date MBH Master Data"). Module names routinely
    contain periods (e.g. "SYS 05."), which is why only the quoted-module
    pattern is trusted - a whole-module reference like "SM 02. General
    Settings" has no quotes and correctly returns None.
    """
    if not obj:
        return None
    last_segment = obj.split(" / ")[-1].strip()
    match = _DOTTED_REFERENCE_RE.search(last_segment)
    if not match:
        return None
    return match.group(1).strip(), match.group(2).strip()


def load_import_line_item_matches(model_dir: Path, known_pairs: set) -> set:
    """Best-effort: which (module, line item) pairs already known from
    Line Items.csv are named via dot-notation in Imports.csv Source/Target
    Object. Only ever returns a subset of known_pairs - never invents a pair
    that isn't already in this model's own Line Items.csv (which would
    happen if a dot-notation reference happened to resolve to a different
    model's module/line item of the same name).
    """
    rows = _read_csv_rows(model_dir / "Imports.csv")
    matched = set()
    for row in rows:
        for value in row.values():
            parsed = _parse_dotted_reference((value or "").strip())
            if parsed and parsed in known_pairs:
                matched.add(parsed)
    return matched


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
            "manual_marker": meta["manual_marker"],
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

        entry["flagged_but_kept"] = meta["manual_marker"]["flagged"] and not entry["verdict"].startswith("CANDIDATE") and not entry["verdict"].startswith("DATA MISMATCH")

        results.append(entry)

    results.sort(key=lambda e: (
        e["verdict"] != "CANDIDATE FOR REVIEW - no NUX usage, no formula reference, no dashboard usage, no action usage found",
        not e["manual_marker"]["flagged"],
        e["functional_area"],
        e["name"],
    ))
    return {
        "modules": results,
        "summary": {
            "total_modules": len(results),
            "candidates_for_review": sum(1 for e in results if e["verdict"].startswith("CANDIDATE")),
            "active_in_ux": sum(1 for e in results if e["verdict"].startswith("ACTIVE")),
            "kept_internal_dependency": sum(1 for e in results if e["verdict"].startswith("KEEP")),
            "data_mismatches": sum(1 for e in results if e["verdict"].startswith("DATA MISMATCH")),
            "flagged_but_kept": sum(1 for e in results if e["flagged_but_kept"]),
        },
    }


def to_markdown_modules(report: dict, model_name: str) -> str:
    s = report["summary"]
    lines = [
        f"# Module optimization analysis - {model_name}",
        "",
        f"- Total modules: {s['total_modules']}",
        f"- Active in NUX: {s['active_in_ux']}",
        f"- Kept (internal dependency - formula/dashboard/action usage): {s['kept_internal_dependency']}",
        f"- **Candidates for review: {s['candidates_for_review']}**",
        f"- Data mismatches (name not found in NUX report): {s['data_mismatches']}",
        f"- Flagged for deletion (Notes/Functional Area) but still active or kept: {s['flagged_but_kept']}",
        "",
    ]

    candidates = [e for e in report["modules"] if e["verdict"].startswith("CANDIDATE")]
    if candidates:
        lines += ["## Candidates for review", "", "| Module | Functional Area | Flagged for deletion |", "|---|---|---|"]
        for e in candidates:
            flag = ("Yes - " + "; ".join(e["manual_marker"]["reasons"])) if e["manual_marker"]["flagged"] else ""
            lines.append(f"| {e['name']} | {e['functional_area']} | {flag} |")
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

    flagged_but_kept = [e for e in report["modules"] if e["flagged_but_kept"]]
    if flagged_but_kept:
        lines += ["## Modules flagged for deletion but still active or kept", "",
                   "| Module | Functional Area | Verdict | Flag reason |", "|---|---|---|---|"]
        for e in flagged_but_kept:
            lines.append(f"| {e['name']} | {e['functional_area']} | {e['verdict']} | {'; '.join(e['manual_marker']['reasons'])} |")
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
