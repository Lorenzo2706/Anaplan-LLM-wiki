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

> **Not every model's raw folder has this exact set today.** `raw/models/AAC/` matches
> it exactly, but `raw/models/FSP 2.0/` has only 9 of the 13 (missing the 5 Roles/Source
> Models grids) plus two files the scraper doesn't produce at all (`Imports.csv`,
> `Import Data Sources.csv`), and `raw/models/MJP/` has only 6. Re-running the scraper
> only ever touches these 13 filenames — anything else already in the folder is left
> alone, and any of the 13 that fail to export leave the prior file for that name
> untouched rather than deleting it.

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

### Finding a model that isn't registered yet

`scrape_model_data.py` refuses to scrape a raw model_id GUID directly — it needs a
`models.py` shortcut with `customer_id`/`workspace_id`/`model_id`. If you don't have
those for a model yet, fetch the live list instead of hunting through the Anaplan UI:

```powershell
python scrape_model_data.py --list-models
```

Logs in, calls the same `springboard-platform-gateway-service/models` API the
interactive `scraper_ux.py` wizard uses for "Browse all models…", and prints every
model visible to this account as JSON (`model_name`, `model_id`, `workspace_name`,
`workspace_id`, `customer_id`) — no `models.py` shortcut required. Confirm the right
entry with the user, then add it to `.env`/`models.py` (see "Adding a new model" below)
before scraping.

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
