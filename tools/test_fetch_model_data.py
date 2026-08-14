import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from fetch_model_data import Grid, parse_view_data

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
