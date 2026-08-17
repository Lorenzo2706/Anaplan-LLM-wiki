# `fetch_model_data.py` — live cell-data reader

> Read-only. Reads real cell values out of a live Anaplan model so the
> `anaplan-formula-agent` skill can validate a formula against data examples.

## Verified endpoint contract

Established by live probe on 2026-08-14 against **FSP 2.0** (`fsp`, DEV_POLARIS
workspace, Polaris engine). Observed, not inferred.

### Authentication — token, not cookies

```
POST https://auth.anaplan.com/token/authenticate   (Authorization: Basic <b64 user:pass>)
  -> HTTP 201  {"tokenInfo": {"tokenValue": "..."}, "statusMessage": "Login successful"}

GET  https://api.anaplan.com/2/0/...               (Authorization: AnaplanAuthToken <token>)
  -> HTTP 200
```

- **No browser is involved.** The token exchange takes about a second.
- The **host is `https://api.anaplan.com`**, the global Integration API endpoint.
  It is **not** the regional app shard. `eu2a.app.anaplan.com/2/0/...` redirects to
  the global endpoint, which rejects web-session cookies with
  `401 {"status":{"code":401,"message":"Not Authenticated."}}`. Cookie auth against
  `/2/0/` began failing around 2026-08-07 and is confirmed dead from every transport.
- A prior note claiming Basic auth was disabled on this tenant
  (`FAILURE_BAD_CREDENTIAL`, observed 2026-07-15) is **not true** as of 2026-08-14.
- `tools/scrape_model_data.py` already implements this as `_anaplan_token()` and
  `_api_session()`, with `API_BASE` and `AUTH_TOKEN_URL` module constants
  (committed in `0479278`). **Reuse them — do not reimplement the token exchange.**
- Token lifetime is roughly 30 minutes, which comfortably exceeds a single CLI run.
  **There is deliberately no token cache on disk.**

### Endpoints

| Endpoint | Status | Notes |
|---|---|---|
| `GET /2/0/models/{modelId}/views` | 200 | `{"meta","status","views"}`; entry keys `code, id, name, moduleId`. FSP returned **142** views vs 125 rows in `Views.csv` on 2026-08-14 — the offline CSV is genuinely incomplete. (The exact live count will drift as the model changes; the gap between it and the static CSV is the point, not the specific integer.) |
| `GET /2/0/models/{modelId}/views/{viewId}` | 200 | Metadata. Returns `viewName`, `viewId`, `columns:[{name,id}]`, `rows:[{name,id}]`, `pages:[{name,id}]`. |
| `GET /2/0/models/{modelId}/views/{viewId}/data` | **400** | `{"status":{"code":400,"message":"Mandatory query parameter 'format' is missing"}}` |
| `GET /2/0/models/{modelId}/views/{viewId}/data?format=v1` | 200 | The cell data. **`format` is mandatory.** |
| `GET /2/0/models/{modelId}/lists` | 200 | `{"meta","status","lists"}`; entry keys `id, name` only. |
| `GET /2/0/models/{modelId}/lists/{listId}/items` | 200 | Key is **`listItems`**, *not* `items`. Entry keys `id, name, code, parent, parentId`. |

### `…/data?format=v1` response shape

```json
{
  "pages": ["OPEX", "Activering", "MJP - 2026 - 2030", "Plan exclusief inflatie"],
  "columnCoordinates": [["Jan 26"], ["Feb 26"], ["Mar 26"]],
  "rows": [
    {"rowCoordinates": ["IT"],         "cells": ["<value>", "<value>", "<value>"]},
    {"rowCoordinates": ["Financiën"],  "cells": ["<value>", "<value>", "<value>"]}
  ]
}
```

Three top-level keys only: `pages`, `columnCoordinates`, `rows`.

- **`pages` is a flat list of *selected item names*.** It carries **no dimension
  names**. To build the `{dimension: selected}` mapping the digest needs, you must
  also call `GET /views/{viewId}` and zip its `pages:[{name,id}]` against this list
  **by position**.
- **`columnCoordinates` is a list of coordinate *tuples***, one per column, each a
  list of strings. In the probed view each tuple had length 1 (only Time on
  columns); with two or more column dimensions the tuples are longer. Do not assume
  length 1.
- **`rows[].rowCoordinates`** is the same shape for rows.
- **`cells` are always strings — including blanks.** No `null` was observed in
  any probed view. A direct probe of the raw payload on 2026-08-14 found all
  2,688 cells were JSON strings, of which 1,288 were `""`. **Anaplan represents
  a blank cell as an empty string, never `null`.** Verified, not inferred —
  the parser's `""` → `None` normalization is confirmed correct.
- The payload alone cannot supply `row_dim_names`, page dimension names, or the
  view name. All three come from `GET /views/{viewId}`. This is why
  `parse_view_data` takes **two** payloads.

### `pages=` query parameter

Verified by probing three candidate syntaxes:

| Form | Result |
|---|---|
| `pages={dimensionId}:{itemId}` e.g. `pages=101000000007:214000000002` | **200** — `pages` echo changed from `"OPEX"` to `"CAPEX"` |
| `pages={itemId}` | 400 `Malformed pages parameter [214000000002]` |
| `pages={dimName}:{itemName}` | 400 `Malformed page parameters` |

**`pages=` requires numeric IDs, not names.** A user-facing `--page "Dim:Item"`
argument therefore needs a two-step resolution: dimension name → `id` from
`GET /views/{viewId}`'s `pages` array, and item name → `id` from
`GET /lists/{dimId}/items`.

### Non-JSON 200 responses are real

While scanning FSP's default views, one returned HTTP 200 with a body that
`response.json()` could not decode (`Expecting value: line 1 column 1 (char 0)`).
A `Content-Type`-only check does **not** catch this. `classify_response` must
also verify the body actually decodes, or the typed-error contract leaks a raw
`JSONDecodeError`.

### Non-ASCII data is present

Row coordinates include values such as `Financiën`. On Windows the default
console encoding is cp1252 and printing these raises `UnicodeEncodeError`,
crashing the digest after a successful fetch.

## What it is

Read-only reader for **live Anaplan cell values**, one module or list per call.
Everything else in `tools/` exports *blueprint metadata* (line items, formulas,
dimensions); this is the only tool that returns actual numbers.

Built so the `anaplan-formula-agent` skill can check a recommendation against
real data instead of reasoning purely from structure.

## Usage

    python tools/fetch_model_data.py module <shortcut> "<Module Name>" --out-dir DIR \
        [--page "Dim:Item,Dim2:Item2"] [--line-items "A,B"] \
        [--periods "Jan 26:Mar 26"] [--sample N]

    python tools/fetch_model_data.py list <shortcut> "<List Name>" --out-dir DIR [--sample N]

`--out-dir` is **required** and must be outside the repository. The tool refuses
a path inside the repo: this vault lives under OneDrive sync and must never hold
client cell data.

## Narrowing: what shrinks the fetch vs the digest

| Argument | Effect | Where it applies |
|---|---|---|
| `--page "Product:Widget A"` | Shrinks the **fetch** — sent to Anaplan as `pages=` | server-side |
| `--line-items "Volume,Price"` | Shrinks the **digest** — rows filtered after arrival | client-side |
| `--periods "Jan 26:Mar 26"` | Shrinks the **digest** — columns filtered after arrival | client-side |
| `--sample N` | Rows shown in the digest (default 10) | client-side |

`--page` takes **names**, but the API only accepts **numeric IDs**
(`pages={dimensionId}:{itemId}`; name-based selection returns
`400 Malformed page parameters`). The tool resolves names to IDs for you via the
view metadata and one `/lists/{dimId}/items` call per selected dimension.

`--periods` matches column labels **exactly as Anaplan returns them**, either as
a comma list or an inclusive `A:B` range. There is no calendar parsing, so it
works whatever period format a model uses.

Sampling is deterministic: evenly spaced rows, first and last always included.

## Number formatting — no locale risk

Verified 2026-08-14 against ~1,400 sampled cells: values come back as raw
machine numbers with a **period** decimal separator and full float precision
(e.g. `0.028999999999999915`, `-0.19417939074643778`, both illustrative
inflation-rate formats, not values to treat as meaningful in isolation). **Not
one comma appeared in any numeric value** — no thousands separators, no
locale-specific formatting of any kind.

This matters because `row_stats` strips commas before parsing a value as a
number (`str(raw).replace(",", "")`). Given the above, that strip is a **no-op
in practice** — there is no evidence Anaplan ever sends a European-style
`1.234,56` decimal through this endpoint that the stripping would mangle.

## Name resolution

Module → view ID tries the ingested `raw/models/<raw_dir>/Views.csv` first, then
falls back to the live API. The fallback is **not** an edge case:

- `raw/models/AAC/` has **no `Views.csv`** — AAC always uses the API.
- `FSP 2.0/Views.csv` covers 125 rows against **142 live views** (as of
  2026-08-14 — the exact count will drift; the offline CSV being materially
  incomplete is the durable fact).
- `General Lists.csv` has **no ID column**, so list resolution *always* uses the API.

Only a module's **default** view is used (`ID == Module ID`). Saved views are
skipped because their filtered/pivoted layout would return a different grid — and
a saved view can share the module's exact name, so matching by name alone is not
enough.

Whatever the path, `viewName` from `GET /views/{viewId}` is verified against the
name asked for. A mismatch **raises** instead of returning data.

**Gotcha: `GET /lists` does not expose Anaplan system lists.** Verified
2026-08-14: FSP 2.0's `GET /lists` returns **38** lists. `Users` and `Versions`
appear in `General Lists.csv` but are **absent** from the API response. Asking
`fetch_model_data.py list fsp "Users"` therefore returns a correct-but-surprising
`No list named 'Users' exists` error — that is expected API behavior, not a bug
in the tool's list-resolution logic.

## Error taxonomy

Deliberately *not* modelled on the old `scrape_model_data._get()`, which returned
`{}` for every failure and so made an expired session indistinguishable from an
empty module. Each condition is distinct, and none produce an empty result:

| Exit | Condition | Meaning |
|---|---|---|
| 0 | success, or grid exists with zero rows | An empty grid is a **real model state** (common in sparse Polaris models), reported explicitly as `EMPTY:` — never as "the formula produces nothing" |
| 1 | generic API or lookup failure | message included |
| 2 | bad arguments, or `--out-dir` inside the repo | refused before any network call |
| 3 | grid too large | refuses rather than truncating; names the page dimensions to narrow by |
| 4 | resolved name mismatch | Anaplan returned a different grid than requested |
| 5 | auth failure after one token refresh | check `.env` |
| 6 | timeout | a timeout, **not** an empty grid |

A `200` response whose body will not decode as JSON is treated as an error, not as
an empty grid — that response was observed live on 2026-08-14.

## Authentication

Integration-API token auth. **No browser, no Selenium, no cookies.**

1. `POST auth.anaplan.com/token/authenticate` with Basic credentials from `.env`
   → `tokenInfo.tokenValue` (HTTP 201).
2. `GET api.anaplan.com/2/0/...` with `Authorization: AnaplanAuthToken <token>`.

Implemented once in `scrape_model_data._anaplan_token()` / `_api_session()` and
reused here. The exchange takes about a second, so **nothing is cached to disk** —
no credential-equivalent artifact is written anywhere. A 401 mid-run triggers
exactly one token refresh, then gives up.

> Do **not** call the regional app shard (`eu2a.app.anaplan.com`) for `/2/0/`
> endpoints. It redirects to the global endpoint, which rejects web-session
> cookies with 401. That transport died around 2026-08-07; the URL allowlist
> rejects app-shard URLs so the mistake fails loudly.

**`.env` must be loaded before `models` is imported.** `tools/models.py`
resolves every credential via `os.getenv(...)` **eagerly at import time**, but
`load_dotenv()` historically only ever ran as a side effect of importing
`scraper_ux`. `tools/fetch_model_data.py` calls `load_dotenv()` explicitly
*before* `import models` for exactly this reason — this ordering is a real bug
found and fixed during the 2026-08-14 live smoke test. If an import-sorting
tool (isort, ruff, etc.) ever reorders those two lines, every value in
`models.MODELS` silently reverts to `None` instead of raising, and a live
request goes to a URL like `.../models/None/...`. Keep `load_dotenv()` textually
above `import models` in this file.

## Read-only guarantee

`tools/anaplan_session.py` exposes exactly one HTTP verb, `get`. There is no
`post`/`put`/`patch`/`delete` wrapper, every URL is checked against an
allowlist pinned to `https://api.anaplan.com`, and
`test_session_has_no_write_methods` fails if one is added. Four of five
`models.py` shortcuts (`umd`, `mjp`, `old_fsp`, `datahub`) resolve to
**production** workspaces.

## Data handling rules

- Full grids go **only** to the caller-supplied `--out-dir`, never the repo.
- Fetched values may be quoted **in chat** as validation evidence.
- Fetched values must **never** be written into `wiki/`, `analyses/`, or `log.md`.
  Those may record that a validation ran, against which model and module, and
  the verdict — never the values.

## Tests

    python -m pytest tools/ -v

Unit tests cover the deterministic parts — allowlist, error classification,
JSON-decode guard, name resolution, mismatch guard, page-ID resolution,
narrowing, sampling, stats, digest — using **synthetic** fixtures. Fixtures are
hand-written with fake values on purpose: `tools/` is committed and
OneDrive-synced, so a captured real response must never be checked in. The live
path is verified against `fsp` (the only DEV-workspace model).

## Known gaps

- **Oversize behaviour is unverified.** No probed DEV view was large enough to
  trigger a server-side size refusal (largest observed: 12,350 cells against a
  `MAX_CELLS` of 50,000), so `_TOO_LARGE_MARKERS` is a guess.
  `check_grid_size` (client-side, `MAX_CELLS`) is the guard that is actually tested.
- **The AAC (no-`Views.csv`) API-fallback path is untested** — exercising it means
  reading a production workspace. Deliberately not run.
