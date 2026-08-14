import json
from pathlib import Path

import pytest

from fetch_model_data import (
    Grid,
    NameMismatchError,
    build_pages_param,
    fetch_view_metadata,
    find_list_id_via_api,
    find_view_id_offline,
    find_view_id_via_api,
    narrow_cols,
    narrow_rows,
    parse_page_arg,
    parse_view_data,
    resolve_page_selection,
    resolve_raw_dir,
    verify_resolved_name,
)

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


# Row 2 is a SAVED view sharing the module's exact name with a different ID,
# listed BEFORE the default view. Without it, nothing would exercise the
# ID == Module ID preference and a naive first-match would pass.
VIEWS_CSV = """﻿,ID,Module ID,Code
⠀⠀⠀       ◼️ LOAD MODULES,102000000000,102000000000,
REV 01. Revenue Calc,102000000099,102000000025,
REV 01. Revenue Calc,102000000025,102000000025,
CA 02. Cost Allocation,102000000031,102000000031,
"""


def write_views_csv(tmp_path):
    p = tmp_path / "Views.csv"
    p.write_text(VIEWS_CSV, encoding="utf-8")
    return str(p)


def test_find_view_id_offline_prefers_default_view_over_same_named_saved_view(tmp_path):
    """A module's DEFAULT view has ID == Module ID. A saved view sharing the
    name must never win: its filtered/pivoted layout would silently return a
    different grid. The saved view is listed FIRST in the fixture so a naive
    first-match implementation fails this test."""
    assert find_view_id_offline(write_views_csv(tmp_path),
                                "REV 01. Revenue Calc") == "102000000025"


def test_find_view_id_offline_is_case_insensitive(tmp_path):
    assert find_view_id_offline(write_views_csv(tmp_path),
                                "rev 01. revenue calc") == "102000000025"


def test_find_view_id_offline_strips_section_header_padding(tmp_path):
    """Modules.csv/Views.csv contain section pseudo-rows padded with braille
    blanks and emoji. They must still be findable by their bare name."""
    assert find_view_id_offline(write_views_csv(tmp_path),
                                "LOAD MODULES") == "102000000000"


def test_find_view_id_offline_returns_none_when_absent(tmp_path):
    assert find_view_id_offline(write_views_csv(tmp_path), "Nope") is None


def test_find_view_id_offline_returns_none_when_file_missing(tmp_path):
    """AAC has no Views.csv at all - this must fall through, not crash."""
    assert find_view_id_offline(str(tmp_path / "Views.csv"), "Anything") is None


class FakeSession:
    def __init__(self, payload):
        self.payload = payload
        self.calls = []

    def get(self, url, timeout=180):
        self.calls.append(url)
        return self.payload


def test_find_view_id_via_api_prefers_default_view():
    sess = FakeSession(load_fixture("views_list_sample.json"))
    got = find_view_id_via_api(sess, "https://api.anaplan.com", "M1",
                               "REV 01. Revenue Calc")
    assert got == "102000000025"


def test_find_view_id_via_api_raises_when_absent():
    sess = FakeSession(load_fixture("views_list_sample.json"))
    with pytest.raises(ValueError) as exc:
        find_view_id_via_api(sess, "https://api.anaplan.com", "M1", "Ghost Module")
    assert "Ghost Module" in str(exc.value)


def test_find_list_id_via_api():
    sess = FakeSession(load_fixture("lists_sample.json"))
    got = find_list_id_via_api(sess, "https://api.anaplan.com", "M1", "Afdeling")
    assert got == "101000000013"


def test_fetch_view_metadata_returns_the_metadata_payload():
    sess = FakeSession(load_fixture("view_meta_sample.json"))
    meta = fetch_view_metadata(sess, "https://api.anaplan.com", "M1", "102000000025")
    assert meta["viewName"] == "REV 01. Revenue Calc"
    assert sess.calls == [
        "https://api.anaplan.com/2/0/models/M1/views/102000000025"]


def test_verify_resolved_name_accepts_match():
    assert verify_resolved_name("REV 01. Revenue Calc", "REV 01. Revenue Calc") is None


def test_verify_resolved_name_tolerates_whitespace_and_case():
    assert verify_resolved_name(" REV 01. Revenue Calc ", "rev 01. revenue calc") is None


def test_verify_resolved_name_rejects_mismatch():
    """The guard against silently validating a formula against the WRONG grid."""
    with pytest.raises(NameMismatchError) as exc:
        verify_resolved_name("REV 01. Revenue Calc", "CA 02. Cost Allocation")
    assert "REV 01. Revenue Calc" in str(exc.value)
    assert "CA 02. Cost Allocation" in str(exc.value)


def test_parse_page_arg_basic():
    assert parse_page_arg("Product:Widget A,Region:EMEA") == {
        "Product": "Widget A", "Region": "EMEA"}


def test_parse_page_arg_value_may_contain_colon_and_spaces():
    assert parse_page_arg("Account:1000: Revenue") == {"Account": "1000: Revenue"}


def test_parse_page_arg_empty_returns_empty_dict():
    assert parse_page_arg("") == {}
    assert parse_page_arg(None) == {}


def test_parse_page_arg_rejects_missing_colon():
    with pytest.raises(ValueError) as exc:
        parse_page_arg("Product")
    assert "Dimension:Item" in str(exc.value)


class FakeItemsSession:
    """Returns list items for /lists/{id}/items - note the `listItems` key."""

    def __init__(self):
        self.calls = []

    def get(self, url, timeout=180):
        self.calls.append(url)
        return {"listItems": [
            {"id": "214000000001", "name": "Widget A"},
            {"id": "214000000002", "name": "Widget B"},
        ]}


def test_resolve_page_selection_maps_names_to_ids():
    """The API rejects name-based pages= with 400 Malformed page parameters.
    Both sides must become numeric IDs."""
    meta = load_fixture("view_meta_sample.json")
    got = resolve_page_selection(FakeItemsSession(), "https://api.anaplan.com",
                                 "M1", meta, {"Product": "Widget B"})
    assert got == {"101000000007": "214000000002"}


def test_resolve_page_selection_unknown_dimension_lists_available():
    meta = load_fixture("view_meta_sample.json")
    with pytest.raises(ValueError) as exc:
        resolve_page_selection(FakeItemsSession(), "https://api.anaplan.com",
                               "M1", meta, {"Ghost": "X"})
    assert "Ghost" in str(exc.value) and "Product" in str(exc.value)


def test_resolve_page_selection_unknown_item_lists_available():
    meta = load_fixture("view_meta_sample.json")
    with pytest.raises(ValueError) as exc:
        resolve_page_selection(FakeItemsSession(), "https://api.anaplan.com",
                               "M1", meta, {"Product": "Nonexistent"})
    assert "Nonexistent" in str(exc.value) and "Widget A" in str(exc.value)


def test_build_pages_param_uses_ids_and_is_deterministic():
    """Sorted so identical requests produce byte-identical URLs, which keeps
    runs reproducible."""
    a = build_pages_param({"101000000019": "9", "101000000007": "1"})
    b = build_pages_param({"101000000007": "1", "101000000019": "9"})
    assert a == b == "101000000007:1,101000000019:9"


def test_build_pages_param_empty_is_empty_string():
    assert build_pages_param({}) == ""


def test_narrow_rows_selects_named_line_items():
    got = narrow_rows(sample_grid(), ["Volume", "Revenue"])
    assert got.row_labels == [("Volume",), ("Revenue",)]
    assert got.cells == [["100", "105", "110"], ["250", "262.5", "302.5"]]


def test_narrow_rows_is_case_insensitive():
    assert narrow_rows(sample_grid(), ["volume"]).row_labels == [("Volume",)]


def test_narrow_rows_preserves_source_order():
    """Output follows GRID order, not argument order, so the digest layout is
    stable regardless of how the caller listed the line items."""
    got = narrow_rows(sample_grid(), ["Revenue", "Volume"])
    assert got.row_labels == [("Volume",), ("Revenue",)]


def test_narrow_rows_empty_list_is_a_noop():
    assert narrow_rows(sample_grid(), []).n_rows == 4


def test_narrow_rows_unknown_name_raises_and_lists_available():
    with pytest.raises(ValueError) as exc:
        narrow_rows(sample_grid(), ["Ghost"])
    assert "Ghost" in str(exc.value)
    assert "Volume" in str(exc.value)


def test_narrow_cols_explicit_list():
    got = narrow_cols(sample_grid(), "Jan 26,Mar 26")
    assert got.col_labels == ["Jan 26", "Mar 26"]
    assert got.cells[0] == ["100", "110"]


def test_narrow_cols_range_is_inclusive():
    got = narrow_cols(sample_grid(), "Jan 26:Feb 26")
    assert got.col_labels == ["Jan 26", "Feb 26"]
    assert got.cells[2] == ["250", "262.5"]


def test_narrow_cols_range_rejects_reversed_bounds():
    with pytest.raises(ValueError) as exc:
        narrow_cols(sample_grid(), "Mar 26:Jan 26")
    assert "after" in str(exc.value).lower()


def test_narrow_cols_unknown_label_raises():
    with pytest.raises(ValueError) as exc:
        narrow_cols(sample_grid(), "Jun 99")
    assert "Jun 99" in str(exc.value)


def test_narrow_cols_empty_is_a_noop():
    assert narrow_cols(sample_grid(), "").n_cols == 3


def test_narrow_rows_does_not_alias_row_lists_with_source():
    """Later code holds a reference to the unnarrowed grid alongside the
    narrowed one. If narrow_rows's returned Grid shares its inner row lists
    with the source (e.g. `cells=[grid.cells[i] for i in keep]`, which copies
    the outer list but reuses each inner row object), mutating a cell in the
    narrowed grid silently corrupts the same cell in the original."""
    grid = sample_grid()
    original_value = grid.cells[0][1]
    narrowed = narrow_rows(grid, ["Volume"])
    narrowed.cells[0][1] = "MUTATED"
    assert grid.cells[0][1] == original_value


def test_narrow_cols_does_not_alias_row_lists_with_source():
    """Same aliasing guarantee as narrow_rows, pinned here too so it cannot
    silently regress in whichever of the two a future edit touches."""
    grid = sample_grid()
    original_value = grid.cells[0][0]
    narrowed = narrow_cols(grid, "Jan 26")
    narrowed.cells[0][0] = "MUTATED"
    assert grid.cells[0][0] == original_value
