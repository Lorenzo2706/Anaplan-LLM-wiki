# `scrape_model_data_api.py` — API-driven model exporter

Retrieves the model-settings export **entirely through Anaplan HTTP APIs** — no
Dojo UI navigation. The browser is used only to log in and hold the session;
every file comes from an API call. This is the fast replacement for the
UI-driven `scrape_model_data.py`.

Two modes:

- **default** → the 7 files Anaplan's REST API v2 exposes (`/2/0/models/{id}/...`),
  pulled as JSON over plain `requests`.
- **`--full`** → all 15 files: the 7 REST files **plus** the 8 legacy-engine
  grids, retrieved over the **classic core-webapp API** (not the UI). A complete
  15-file export in one browser login.

```powershell
python scrape_model_data_api.py fsp --name "FSP 2.0"           # 7 REST files
python scrape_model_data_api.py fsp --name "FSP 2.0" --full    # all 15 files
python scrape_model_data_api.py fsp --out "C:/temp/fsp_api"    # explicit folder
```

## Why login still needs a browser

This tenant has **Basic Authentication disabled for the Integration API**: the
token endpoint (`auth.anaplan.com/token/authenticate`) rejects the `.env`
credentials with `FAILURE_BAD_CREDENTIAL`, even though the *same*
username/password log in fine through the web UI (verified live, 2026-07-15).
No client certificate or OAuth client is configured either. So a truly
head-less run is **not possible today** — it would need an Anaplan admin to
enable OAuth2 or certificate auth. The tool reuses `scraper_ux.login` once, then
lifts the browser session cookies for the REST calls and drives the classic-
engine calls via `fetch()` in the authenticated iframe. The browser is open only
for the ~15-30 s login plus a few seconds of API calls.

## How the two API paths work

**REST API v2 (7 files).** Standard `GET /2/0/models/{id}/{modules|lineItems|
versions|lists|actions|imports|views}` with the browser's session cookies lifted
into a `requests.Session`. `Line Items.csv` is the rich one (formula, format,
applies-to, summary, time scale/range, versions, style, cell count, is-summary,
formula scope, use switchover, breakback, start of section, referenced-by,
module name). A few columns the REST API doesn't expose are left blank
(Populated Cell Count, Memory Used, Calculation Complexity/Effort, Read/Write
Access Driver, Users List, Parent, Code, Data Tags, Functional Area).

**Classic core-webapp API (8 legacy files, `--full`).** The legacy blueprint
grids (Line Item Subsets, Time Ranges, Source Models, Roles + Roles Modules/
Versions/Lists/Actions) live in the classic core engine (`core-webapp-<ws>` on
the `eu4` shard) and have no REST endpoint — but the engine's own HTTP protocol
is driven directly, no UI clicking:

1. `POST .../anaplan/jsonrpc` `{requestType:"VIEW_REQUEST_SET", viewRequests:[{viewIndex:-1, viewGuid:<new>, viewDefinition:<grid template>}], activeViewIndices:[], modelDefinitionSerialNumber, clientSessionId}` → returns the opened view's `viewIndex`.
2. `POST .../anaplan/jsonrpc` `{requestType:"PROGRESS", activeViewIndices:[viewIndex]}` → returns a `taskId`.
3. `POST .../anaplan/servlet?taskType=export` (multipart: `taskId`, `entityId`=grid name, `viewDefinition`, `fileType=CSV`) → streams the grid CSV.

A **minimal** `VIEW_REQUEST_SET` (empty carried view-state, single new view) is
sufficient — proven live against all 8 grids, byte-for-byte equal to the
reference exports. `entityId` (= the grid name, i.e. the filename minus `.csv`)
is the primary driver; the `viewDefinition` is a **model-independent template**
(system identifiers `_SYSTEM_AXIS_IDENTIFIER.*` / `_2000000xxx_` / `_4000xxxxx_`
only) baked into `_LEGACY_TEMPLATES`. Only `modelDefinitionSerialNumber` and
`clientSessionId` are per-session, and they're scraped from the client's own
first jsonrpc call at run time. Any legacy grid that fails the classic-API path
falls back to the `scrape_model_data` UI export for that one grid, so coverage
never regresses.

## Output

All CSVs reuse the **exact blueprint column layout** (first header cell blank,
first data column = entity name), so `wiki-data-ingestion` parses them
identically to the pure-Selenium exports. The 8 legacy files are byte-for-byte
the same grids the UI produces (validated: identical headers + row sets vs.
`raw/models/FSP 2.0`). `Line Items.csv` omits the module-separator pseudo-rows
the UI export interleaves (~1 fewer row per module) but is otherwise cleaner —
every line item still carries its `Module Name`.

Full FSP 2.0 `--full` run: 15/15 files, all via API (7 `[API]` REST + 8 `[CLS]`
classic core-webapp), zero UI fallback.

## When to use which tool

- **Quick formula/structure refresh** → default mode (7 REST files, seconds).
- **Complete model export** → `--full` (all 15, API-driven, one login). Recommended
  default for onboarding/refresh.
- **Pure UI export / debugging the legacy grids in isolation** →
  `scrape_model_data.py` (see `SCRAPE_MODEL_DATA.md`). Still useful as the
  fallback path `--full` invokes automatically.

Prerequisites: `.env` filled in, a `models.py` shortcut, Edge installed, and
`pip install requests selenium openpyxl webdriver-manager python-dotenv`.
