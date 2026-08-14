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
| `GET /2/0/models/{modelId}/views` | 200 | `{"meta","status","views"}`; entry keys `code, id, name, moduleId`. FSP returned **141** views vs 125 rows in `Views.csv` — the offline CSV is genuinely incomplete. |
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
- **`cells` are always strings.** No `null` was observed in any probed view.
  The representation of a genuinely blank cell is **UNVERIFIED**.
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
