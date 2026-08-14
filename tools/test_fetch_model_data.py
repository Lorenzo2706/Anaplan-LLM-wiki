import json
from pathlib import Path

import pytest

from fetch_model_data import Grid, parse_view_data, resolve_raw_dir

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def sample_grid():
    return parse_view_data(load_fixture("view_data_sample.json"),
                           load_fixture("view_meta_sample.json"))


def test_parse_view_data_shape():
    grid = sample_grid()
    assert isinstance(grid, Grid)
    assert grid.col_labels == ["Jan 26", "Feb 26", "Mar 26"]
    assert grid.row_labels == [("Volume",), ("Price",), ("Revenue",), ("Discount",)]
    assert grid.cells[0] == ["100", "105", "110"]


def test_parse_view_data_row_dim_names_come_from_metadata():
    """The data payload has no row dimension names - they only exist in
    GET /views/{id}. A Grid built from the data payload alone would be
    unlabelled."""
    assert sample_grid().row_dim_names == ["Line Item"]


def test_parse_view_data_page_selection_zips_names_to_values():
    """`pages` in the data payload is a bare list of selected VALUES; the
    dimension NAMES come from the metadata payload, matched by position."""
    grid = sample_grid()
    assert grid.page_selection == {"Product": "Widget A", "Region": "EMEA"}
    assert grid.available_page_dims == ["Product", "Region"]
    assert grid.page_dim_ids == {"Product": "101000000007", "Region": "101000000019"}


def test_parse_view_data_normalizes_empty_string_to_none():
    """A blank cell and a zero cell are DIFFERENT facts when validating a
    formula. Anaplan sends blanks as "" and zeros as "0"; collapsing them would
    hide a real class of bug."""
    assert sample_grid().cells[3] == [None, "0", None]


def test_parse_view_data_handles_multi_coordinate_axes():
    """Coordinate tuples are length 1 only when a single dimension is on the
    axis. Two dimensions on rows produce 2-element tuples."""
    data = {
        "pages": [],
        "columnCoordinates": [["Jan 26", "Actual"], ["Jan 26", "Budget"]],
        "rows": [{"rowCoordinates": ["EMEA", "Volume"], "cells": ["1", "2"]}],
    }
    meta = {"viewName": "V", "viewId": "1",
            "columns": [{"name": "Time", "id": "a"}, {"name": "Version", "id": "b"}],
            "rows": [{"name": "Region", "id": "c"}, {"name": "Line Item", "id": "d"}],
            "pages": []}
    grid = parse_view_data(data, meta)
    assert grid.row_labels == [("EMEA", "Volume")]
    assert grid.col_labels == ["Jan 26 / Actual", "Jan 26 / Budget"]
    assert grid.row_dim_names == ["Region", "Line Item"]


def test_parse_view_data_normalizes_null_cell_to_none_too():
    """How Anaplan represents a genuinely blank cell is UNVERIFIED against the
    live API - every probed cell was a non-empty string, so "" is only an
    assumption, not an observation. This test builds an inline payload where a
    blank cell arrives as JSON null (the other plausible sentinel) instead of
    "", and proves parse_view_data normalizes it to None exactly like the ""
    case, while still keeping a real "0" distinct from either blank form."""
    data = {
        "pages": [],
        "columnCoordinates": [["Jan 26"], ["Feb 26"]],
        "rows": [{"rowCoordinates": ["Discount"], "cells": [None, "0"]}],
    }
    meta = {"viewName": "V", "viewId": "1",
            "columns": [{"name": "Time", "id": "a"}],
            "rows": [{"name": "Line Item", "id": "b"}],
            "pages": []}
    grid = parse_view_data(data, meta)
    assert grid.cells[0] == [None, "0"]


FAKE_MODELS = {
    "fsp": {"name": "FSP", "raw_dir": "FSP 2.0", "model_id": "M1"},
    "umd": {"name": "UMD", "raw_dir": "AAC", "model_id": "M2"},
    "broken": {"name": "Broken", "model_id": "M3"},
}


def test_resolve_raw_dir_uses_raw_dir_not_name(tmp_path):
    (tmp_path / "raw" / "models" / "FSP 2.0").mkdir(parents=True)
    got = resolve_raw_dir("fsp", FAKE_MODELS, str(tmp_path))
    assert Path(got).name == "FSP 2.0"


def test_resolve_raw_dir_handles_umd_to_aac(tmp_path):
    """umd is a cost-category acronym (Uren/Materiaal/Diensten Derden), not a
    model name - it points at AAC. No fuzzy match could find this."""
    (tmp_path / "raw" / "models" / "AAC").mkdir(parents=True)
    got = resolve_raw_dir("umd", FAKE_MODELS, str(tmp_path))
    assert Path(got).name == "AAC"


def test_resolve_raw_dir_unknown_shortcut_lists_valid_ones(tmp_path):
    with pytest.raises(ValueError) as exc:
        resolve_raw_dir("nope", FAKE_MODELS, str(tmp_path))
    assert "fsp" in str(exc.value) and "umd" in str(exc.value)


def test_resolve_raw_dir_missing_key_names_it(tmp_path):
    with pytest.raises(ValueError) as exc:
        resolve_raw_dir("broken", FAKE_MODELS, str(tmp_path))
    assert "raw_dir" in str(exc.value)


def test_resolve_raw_dir_missing_folder_errors(tmp_path):
    (tmp_path / "raw" / "models").mkdir(parents=True)
    with pytest.raises(ValueError) as exc:
        resolve_raw_dir("fsp", FAKE_MODELS, str(tmp_path))
    assert "FSP 2.0" in str(exc.value)
