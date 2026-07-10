# `scrape_model_data.py` — model-settings CSV exporter

Automates the manual "export the 13 blueprint CSVs from the Anaplan UI" step so a
model can be onboarded into the wiki without clicking through model-settings by
hand. It **reuses `scraper_ux.py`'s login unchanged** (Selenium/Edge, basic auth
from `.env`) and drives the modeling-UI grid exports itself.

## What it produces

All 13 files land in the output folder, matching the naming used under
`raw/models/<Model>/`:

```
Modules.csv          Line Items.csv       Line Item Subsets.csv
General Lists.csv     Versions.csv         Time Ranges.csv
Actions.csv          Source Models.csv    Roles.csv
Roles Modules.csv    Roles Versions.csv   Roles Lists.csv
Roles Actions.csv
```

## Prerequisites

- `pip install selenium openpyxl webdriver-manager python-dotenv` (same as the
  existing scraper) and Microsoft Edge installed.
- `.env` filled in (`ANAPLAN_USERNAME`, `ANAPLAN_PASSWORD`, `ANAPLAN_ENVIRONMENT`,
  `ANAPLAN_USE_SSO`, shared `CUSTOMER_ID` + workspace id, and the model id).
- The model registered as a shortcut in `models.py` (see below).

## Usage

```powershell
# Export into raw/models/<Model Name>/ (the default)
python scrape_model_data.py fsp --name "FSP 2.0"

# Export into an explicit folder (e.g. a scratch dir for testing)
python scrape_model_data.py fsp --out "C:/temp/fsp_export"
```

As a library:

```python
from scrape_model_data import download_model_exports
results = download_model_exports("fsp", out_dir=r"raw/models/FSP 2.0")
# results: {filename: {"ok": bool, "saved_path": str|None, "error": str|None}}
```

`model` is a `models.MODELS` shortcut key (e.g. `fsp`). It opens a real (non-headless)
Edge window and logs in automatically via basic auth; no manual step is needed unless
SSO is enabled. It prints a per-grid ✅/✗ summary and an `N/13 exported` line, and exits
0 only when all 13 succeed.

> **Default output vs. your real folders:** the default `out_dir` is
> `raw/models/<--name>/`. Pass `--name "FSP 2.0"` (or `--out`) so it writes to the
> existing folder rather than a new `raw/models/FSP/`. Re-runs overwrite the 13
> files in place (matching the "no dated raw copies" convention).

## Adding a new model

1. Add `<PREFIX>_MODEL_ID=<guid>` to `.env` (workspace + `CUSTOMER_ID` are shared).
2. Mirror the `fsp` entry in `models.py` with `customer_id`, `workspace_id`,
   `model_id`, then call `python scrape_model_data.py <prefix> --name "<Model Name>"`.

(Raw model-id GUIDs are rejected on purpose — a bare id has no reliable way to infer
its workspace, so register a shortcut instead.)

## How it works (for future maintainers)

The model-settings UI is a legacy **Dojo** app inside **nested iframes**: an outer
shell iframe (`data-testid="shell-content"`) holds the left-nav; its first nested
iframe holds the grid, sub-tabs, toolbar and export dialog. Per grid the script:
navigates the left-nav (shell frame) → switches into the inner grid frame → clicks
the sub-tab if any → clicks the toolbar `Export...` (`<span class="dijitButtonText">`,
not a `<button>`) → presses **Run Export** in the dialog (File Type defaults to CSV) →
saves the download under the target filename.

Two non-obvious gotchas it handles:
- The modeling URL **must not** contain a double slash (`.../` + `/a/...`), or Anaplan
  serves a "We can't find this page" 404 — the script `rstrip("/")`s the base URL.
- Dojo keeps **hidden duplicate widgets** in the DOM, so every click is filtered to
  `is_displayed()`; sub-tabs are matched on alphanumeric-only text because the
  "Roles → Modules" arrow is a CSS icon (real text is `RolesModules`).
