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
