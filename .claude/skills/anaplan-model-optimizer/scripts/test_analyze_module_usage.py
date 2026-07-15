import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from analyze_module_usage import detect_manual_marker


def test_detect_manual_marker_no_signal():
    result = detect_manual_marker("Some normal note about formatting.", "CALCULATION MODULES")
    assert result == {"flagged": False, "reasons": []}


def test_detect_manual_marker_notes_keyword():
    result = detect_manual_marker("To be deleted after Q4 close.", "")
    assert result["flagged"] is True
    assert any("delete" in r.lower() for r in result["reasons"])


def test_detect_manual_marker_notes_keyword_obsolete():
    result = detect_manual_marker("This module is obsolete, replaced by CA26.", "")
    assert result["flagged"] is True
    assert any("obsolete" in r.lower() for r in result["reasons"])


def test_detect_manual_marker_functional_area():
    result = detect_manual_marker("", "DELETE")
    assert result["flagged"] is True
    assert any("Functional Area" in r for r in result["reasons"])


def test_detect_manual_marker_both_sources():
    result = detect_manual_marker("Deprecated - remove in next cleanup.", "DELETE")
    assert result["flagged"] is True
    assert len(result["reasons"]) == 2


def test_detect_manual_marker_case_insensitive():
    result = detect_manual_marker("DELETE THIS", "delete")
    assert result["flagged"] is True


def test_detect_manual_marker_empty_inputs():
    result = detect_manual_marker(None, None)
    assert result == {"flagged": False, "reasons": []}


import csv as csv_module

from analyze_module_usage import load_modules_csv, analyze, to_markdown_modules


def _write_csv(path: Path, header: str, rows: list, delimiter: str = ","):
    path.write_text(header + "\n" + "\n".join(rows), encoding="utf-8-sig")


def _write_modules_csv(tmp_path: Path) -> Path:
    model_dir = tmp_path / "TestModel"
    model_dir.mkdir()
    header = ",Functional Area,Applies To,Time Scale,Time Range,Versions,Breakback,Users List,Cell Count,Populated Cell Count,Memory Used,Notes,Read Access Driver,Write Access Driver,Data Tags,Managed By,Referenced By,Used in Dashboards,Line Items"
    rows = [
        "CA01 Candidate,CALCULATION MODULES,,,,,,,,,,,,,,,,,",
        "CA02 Marked Candidate,CALCULATION MODULES,,,,,,,,,,To be deleted next release,,,,,,,",
        "IN01 Kept Referenced,INPUT MODULES,,,,,,,,,,Deprecated - kept for now,,,,,'CA03 Kept'.some line,,",
        "OU01 Active,OUTPUT MODULES,,,,,,,,,,,,,,,,,",
    ]
    _write_csv(model_dir / "Modules.csv", header, rows)
    (model_dir / "Imports.csv").write_text(";Source Label;Source Object;Source Type;Target Object;Target Type;Production Data\n", encoding="utf-8-sig")
    return model_dir


def _write_workbook(path: Path, modules_usage_rows: list, extra_sheets: dict = None):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Modules Usage Count"
    ws.append(["Module", "Module ID", "Usage Count"])
    for row in modules_usage_rows:
        ws.append(row)
    for name, rows in (extra_sheets or {}).items():
        sheet = wb.create_sheet(name)
        for row in rows:
            sheet.append(row)
    wb.save(path)


def test_load_modules_csv_captures_notes_and_marker(tmp_path):
    model_dir = _write_modules_csv(tmp_path)
    modules = load_modules_csv(model_dir)
    assert modules["CA02 Marked Candidate"]["notes"] == "To be deleted next release"
    assert modules["CA02 Marked Candidate"]["manual_marker"]["flagged"] is True
    assert modules["CA01 Candidate"]["manual_marker"]["flagged"] is False


def test_analyze_attaches_marker_and_flagged_but_kept(tmp_path):
    model_dir = _write_modules_csv(tmp_path)
    excel_path = tmp_path / "report.xlsx"
    _write_workbook(excel_path, [
        ["CA01 Candidate", "1", 0],
        ["CA02 Marked Candidate", "2", 0],
        ["IN01 Kept Referenced", "3", 0],
        ["OU01 Active", "4", 5],
    ])

    report, _line_item_exposure = analyze(excel_path, model_dir)
    by_name = {e["name"]: e for e in report["modules"]}

    assert by_name["OU01 Active"]["verdict"].startswith("ACTIVE")
    assert by_name["IN01 Kept Referenced"]["verdict"].startswith("KEEP")
    assert by_name["CA01 Candidate"]["verdict"].startswith("CANDIDATE")
    assert by_name["CA02 Marked Candidate"]["verdict"].startswith("CANDIDATE")

    # Marked candidate should sort before the unmarked candidate.
    candidate_names = [e["name"] for e in report["modules"] if e["verdict"].startswith("CANDIDATE")]
    assert candidate_names.index("CA02 Marked Candidate") < candidate_names.index("CA01 Candidate")

    # IN01 has a marker (Notes says "Deprecated") but was computed KEEP - contradiction case.
    assert by_name["IN01 Kept Referenced"]["flagged_but_kept"] is True
    assert by_name["CA02 Marked Candidate"]["flagged_but_kept"] is False  # it's a candidate, not a contradiction
    assert report["summary"]["flagged_but_kept"] == 1


def test_to_markdown_modules_renders_flagged_but_kept_section(tmp_path):
    model_dir = _write_modules_csv(tmp_path)
    excel_path = tmp_path / "report.xlsx"
    _write_workbook(excel_path, [
        ["CA01 Candidate", "1", 0],
        ["CA02 Marked Candidate", "2", 0],
        ["IN01 Kept Referenced", "3", 0],
        ["OU01 Active", "4", 5],
    ])
    report, _line_item_exposure = analyze(excel_path, model_dir)
    md = to_markdown_modules(report, "TestModel")
    assert "## Modules flagged for deletion but still active or kept" in md
    assert "IN01 Kept Referenced" in md.split("## Modules flagged for deletion but still active or kept")[1]


from analyze_module_usage import (
    load_line_items_csv,
    _parse_dotted_reference,
    load_import_line_item_matches,
)


def _write_line_items_csv(tmp_path: Path) -> Path:
    model_dir = tmp_path / "LiModel"
    model_dir.mkdir()
    header = ",Format,Formula,Summary,Applies To,Time Scale,Time Range,Versions,Style,Cell Count,Populated Cell Count,Memory Used,Calculation Complexity,Calculation Effort,Notes,Read Access Driver,Write Access Driver,Users List,Parent,Is Summary,Formula Scope,Code,Use Switchover,Breakback,Start of Section,Data Tags,Referenced By,Module Name"
    rows = [
        "Line A,,,,,,,,,,,,,,,,,,,,,,,,,,,CA01 Candidate",
        "Line B,,,,,,,,,,,,,,Remove this line item,,,,,,,,,,,,,CA01 Candidate",
        "Line C,,,,,,,,,,,,,,,,,,,,,,,,,,'Line A',IN01 Kept Referenced",
    ]
    _write_csv(model_dir / "Line Items.csv", header, rows)
    return model_dir


def test_load_line_items_csv(tmp_path):
    model_dir = _write_line_items_csv(tmp_path)
    items = load_line_items_csv(model_dir)
    assert items[("CA01 Candidate", "Line A")]["referenced_by"] == []
    assert items[("CA01 Candidate", "Line B")]["notes"] == "Remove this line item"
    assert items[("IN01 Kept Referenced", "Line C")]["referenced_by"] == ["Line A"]


@pytest.mark.parametrize("obj,expected", [
    ("Data Hub 2.0 / 'SYS 05. Date of Today'.Date MBH Master Data", ("SYS 05. Date of Today", "Date MBH Master Data")),
    ("'CA01 Candidate'.Line A", ("CA01 Candidate", "Line A")),
    ("SM 02. General Settings", None),  # whole-module target, no line item
    ("", None),
])
def test_parse_dotted_reference(obj, expected):
    assert _parse_dotted_reference(obj) == expected


def test_load_import_line_item_matches(tmp_path):
    model_dir = tmp_path / "ImportModel"
    model_dir.mkdir()
    header = ";Source Label;Source Object;Source Type;Target Object;Target Type;Production Data"
    rows = [
        "Import A;Feed;'CA01 Candidate'.Line A;SAVED VIEW;SM 02. General Settings;MODULE;FALSE",
        "Import B;External File;FILE;IMPORT;'IN01 Kept Referenced'.Line C;MODULE;FALSE",
    ]
    (model_dir / "Imports.csv").write_text(header + "\n" + "\n".join(rows), encoding="utf-8-sig")

    known_pairs = {("CA01 Candidate", "Line A"), ("IN01 Kept Referenced", "Line C"), ("CA01 Candidate", "Line B")}
    matched = load_import_line_item_matches(model_dir, known_pairs)
    assert matched == {("CA01 Candidate", "Line A"), ("IN01 Kept Referenced", "Line C")}


from analyze_module_usage import load_excel, FIXED_SHEETS


def test_load_excel_reads_line_item_exposure_sheets(tmp_path):
    excel_path = tmp_path / "report.xlsx"
    _write_workbook(excel_path, [["OU01 Active", "1", 5]], extra_sheets={
        "Views Usage Report - Line Items": [
            ["Module/View name", "App name", "Page name", "View URL", "Page URL",
             "Module/View ID", "App ID", "Page ID", "UX Type", "Line Item"],
            ["OU01 Active", "App", "Page", "url", "url", "1", "a", "p", "GRID", "Revenue"],
            ["OU01 Active", "App", "Page", "url", "url", "1", "a", "p", "GRID", ""],
        ],
        "UI Filters": [
            ["Page", "Module", "Filter Column", "Value Filter Column", "Filter Rows", "Value Filter Rows"],
            ["Page", "OU01 Active", "Cost Center; Region", True, "", False],
        ],
        "Actions TestModel": [
            ["Source Label", "Source Object", "Source Type", "Target Object", "Target Type"],
        ],
    })

    ux_counts, action_usage, line_item_exposure = load_excel(excel_path)

    assert ("OU01 Active", "Revenue") in line_item_exposure
    assert ("OU01 Active", "Cost Center") in line_item_exposure
    assert ("OU01 Active", "Region") in line_item_exposure
    # Blank Line Item cell must not add a bogus ("OU01 Active", "") entry.
    assert ("OU01 Active", "") not in line_item_exposure


def test_fixed_sheets_includes_new_sheets():
    assert "Views Usage Report - Line Items" in FIXED_SHEETS
    assert "UI Filters" in FIXED_SHEETS
