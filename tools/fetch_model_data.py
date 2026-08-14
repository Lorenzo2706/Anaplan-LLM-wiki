"""
fetch_model_data.py
-------------------
Read real cell values out of a live Anaplan model, one module or list per call.

Read-only. Token-bounded: prints a compact digest and writes the full grid to a
caller-supplied --out-dir (never a default location).

NEVER write fetched cell values into wiki/, analyses/, or log.md. See CLAUDE.md.
"""
import os
from dataclasses import dataclass, field


@dataclass
class Grid:
    """Engine-agnostic normalized grid. Everything downstream operates on this,
    never on the raw Anaplan payload, so wire-format changes are confined to
    parse_view_data(). Revision 1's wire-format guesses were all wrong and this
    boundary is why only one function had to change."""
    row_dim_names: list[str] = field(default_factory=list)
    row_labels: list[tuple[str, ...]] = field(default_factory=list)
    col_labels: list[str] = field(default_factory=list)
    cells: list[list[str | None]] = field(default_factory=list)
    page_selection: dict[str, str] = field(default_factory=dict)
    available_page_dims: list[str] = field(default_factory=list)
    page_dim_ids: dict[str, str] = field(default_factory=dict)

    @property
    def n_rows(self) -> int:
        return len(self.row_labels)

    @property
    def n_cols(self) -> int:
        return len(self.col_labels)


def _cell(raw):
    """Every probed cell came back as a non-empty string; how Anaplan represents
    a genuinely BLANK cell is UNVERIFIED against the live API (never observed).
    Assuming "" is the likely candidate, this defensively treats None, "", and
    whitespace-only strings as blank -> None, so downstream code has ONE blank
    sentinel and can still tell a blank from a "0"."""
    if raw is None:
        return None
    text = str(raw)
    return None if text.strip() == "" else text


def parse_view_data(data_payload: dict, meta_payload: dict) -> Grid:
    """Convert an Anaplan view-data response into a Grid.

    THE ONLY function in this codebase that knows Anaplan's wire format.

    Takes TWO payloads because one is not enough:
      data_payload = GET /2/0/models/{m}/views/{v}/data?format=v1
        -> {"pages": [selected values], "columnCoordinates": [[...]],
            "rows": [{"rowCoordinates": [...], "cells": [...]}]}
      meta_payload = GET /2/0/models/{m}/views/{v}
        -> {"viewName", "columns": [{name,id}], "rows": [{name,id}],
            "pages": [{name,id}]}

    `pages` in the data payload is a bare list of SELECTED VALUES with no
    dimension names; the names live in the metadata payload and are matched by
    POSITION. Verified 2026-08-14.
    """
    rows = data_payload.get("rows") or []
    col_coords = data_payload.get("columnCoordinates") or []
    page_values = data_payload.get("pages") or []
    page_dims = meta_payload.get("pages") or []

    # Zip page dimension names to their selected values by position.
    page_selection, page_dim_ids = {}, {}
    for i, dim in enumerate(page_dims):
        name = dim.get("name")
        if not name:
            continue
        page_selection[name] = (page_values[i] if i < len(page_values) else "")
        page_dim_ids[name] = str(dim.get("id") or "")

    return Grid(
        row_dim_names=[d.get("name", "") for d in (meta_payload.get("rows") or [])],
        row_labels=[tuple(r.get("rowCoordinates") or []) for r in rows],
        col_labels=[" / ".join(c) for c in col_coords],
        cells=[[_cell(c) for c in (r.get("cells") or [])] for r in rows],
        page_selection=page_selection,
        available_page_dims=[d["name"] for d in page_dims if d.get("name")],
        page_dim_ids=page_dim_ids,
    )


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def resolve_raw_dir(shortcut, models_map, repo_root=REPO_ROOT):
    """Map a models.py shortcut to its raw/models/<folder> path.

    A dedicated `raw_dir` key is required because the shortcut names do NOT
    match the folder names: `fsp` -> "FSP 2.0", and `umd` -> "AAC" because UMD
    is a cost-category acronym (Uren / Materiaal / Diensten Derden), not a
    model name. See wiki/models/AAC/index.md.
    """
    if shortcut not in models_map:
        raise ValueError(
            f"'{shortcut}' is not a configured shortcut. Available: "
            f"{sorted(models_map)}"
        )
    entry = models_map[shortcut]
    raw_dir = entry.get("raw_dir")
    if not raw_dir:
        raise ValueError(
            f"models.MODELS['{shortcut}'] has no 'raw_dir' key. Add the "
            f"raw/models/ folder name for this model, e.g. "
            f"\"raw_dir\": \"FSP 2.0\"."
        )
    path = os.path.join(repo_root, "raw", "models", raw_dir)
    if not os.path.isdir(path):
        raise ValueError(
            f"raw_dir '{raw_dir}' for shortcut '{shortcut}' does not exist at "
            f"{path}. Check the folder name in models.py."
        )
    return path
