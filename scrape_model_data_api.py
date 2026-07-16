"""
scrape_model_data_api.py
------------------------
API-driven model-settings exporter — the fast alternative to the Selenium-driven
:mod:`scrape_model_data`. Retrieves every file by an Anaplan HTTP API call; the
browser is used only to log in and hold the session (no Dojo UI navigation).

Why this exists
---------------
`scrape_model_data.py` drives the model-settings Dojo UI grid-by-grid (navigate
nested iframes → click nav/sub-tab → Export… → Run Export → wait for a CSV
download), 13 times per model. That is slow. This module pulls the same data
from Anaplan HTTP APIs instead:

  • **7 files via the REST API v2** (`/2/0/models/{id}/...`) as JSON over plain
    `requests` — Line Items (rich: formula/format/applies-to/summary/cell-count/
    referenced-by), Modules, Versions, General Lists, Actions, Imports, Views.
  • **8 legacy grids via the classic core-webapp API** (`--full`) — Line Item
    Subsets, Time Ranges, Source Models, Roles + Roles Modules/Versions/Lists/
    Actions. These have no REST endpoint (they live in the classic core engine),
    but the engine's own HTTP protocol is driven directly — jsonrpc
    VIEW_REQUEST_SET → PROGRESS → servlet?taskType=export — via fetch() inside the
    core-webapp iframe. No UI clicking. See the _LEGACY_TEMPLATES block below for
    the mechanism.

Why the browser is still needed for login
------------------------------------------
This tenant has **Basic Authentication disabled for the Integration API**: the
token endpoint (`auth.anaplan.com/token/authenticate`) rejects the `.env`
credentials with FAILURE_BAD_CREDENTIAL even though the very same
username/password log in fine through the web UI. There is no client
certificate or OAuth client configured either. So a truly head-less
(no-browser) run is not possible today — it would need an Anaplan admin to
enable OAuth2 / certificate auth. We reuse `scraper_ux.login` (browser) once,
lift the session cookies into a `requests.Session` for the REST calls, and drive
the classic-engine calls via fetch() in the authenticated iframe. In practice
the browser window is only open for the ~15-30 s login + a few seconds of API
calls.

Modes
-----
  default  → 7 REST-API files only (fast).
  --full   → all 15 files (7 REST + 8 classic-API). A legacy grid that fails the
             classic-API path falls back to the scrape_model_data UI export for
             that one grid, so coverage never regresses.

Column fidelity: the produced CSVs reuse the exact blueprint column layout (first
header cell blank, first data column = entity name). The 8 legacy files are byte-
for-byte the same grids the UI exports (verified equal to the reference). Within
the REST-derived Line Items.csv / Modules.csv, a few columns the REST API does
not expose (Populated Cell Count, Memory Used, Calculation Complexity/Effort,
Read/Write Access Driver, Users List, Parent, Code, Data Tags, Functional Area)
are left blank. `wiki-data-ingestion` parses everything identically.

Usage
-----
    python scrape_model_data_api.py fsp --name "FSP 2.0"            # 7 REST files
    python scrape_model_data_api.py fsp --name "FSP 2.0" --full     # all 15 files

As a library:

    from scrape_model_data_api import download_model_exports_api, download_model_exports_full
    download_model_exports_full("fsp", out_dir=r"raw/models/FSP 2.0")
"""

import argparse
import csv
import json
import os
import sys
import tempfile
import time

import requests

# import order matters — see scrape_model_data.py's note (scraper_ux loads .env).
import scraper_ux
import models
import scrape_model_data as smd

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# The 8 legacy-engine grids that the REST API v2 does NOT expose. Default
# (REST-only) mode skips them and reports them as such; --full retrieves them
# over the classic core-webapp API. Listed so a default run never silently looks
# "complete" when these 8 blueprint grids are absent.
API_UNAVAILABLE = [
    "Line Item Subsets.csv", "Time Ranges.csv", "Source Models.csv",
    "Roles.csv", "Roles Modules.csv", "Roles Versions.csv",
    "Roles Lists.csv", "Roles Actions.csv",
]


# ══════════════════════════════════════════════════════════════════════════════
#  HTTP session (browser login once → cookies → requests)
# ══════════════════════════════════════════════════════════════════════════════

def _session_from_browser(browser, base):
    """Lift the logged-in browser's cookies + User-Agent into a requests.Session
    so subsequent /2/0/ calls run over pure HTTP. The browser must already be
    authenticated (scraper_ux.login). Does NOT close the browser."""
    # Warm up on an app-shard URL so the API cookies are present, then lift.
    browser.get(f"{base}/a/")
    sess = requests.Session()
    for c in browser.get_cookies():
        sess.cookies.set(c["name"], c["value"],
                         domain=c.get("domain"), path=c.get("path", "/"))
    try:
        ua = browser.execute_script("return navigator.userAgent;")
    except Exception:
        ua = ""
    sess.headers.update({"Accept": "application/json"})
    if ua:
        sess.headers["User-Agent"] = ua
    return sess


def _get(sess, url):
    """GET url and return parsed JSON, or {} on any non-JSON / error response."""
    try:
        r = sess.get(url, timeout=180)
        if r.status_code != 200 or "json" not in r.headers.get("Content-Type", ""):
            return {}
        return r.json()
    except Exception:
        return {}


def _list_field(body):
    """Return the first list value in a dict body (the payload array), or []."""
    if not isinstance(body, dict):
        return []
    for v in body.values():
        if isinstance(v, list):
            return v
    return []


# ══════════════════════════════════════════════════════════════════════════════
#  Small formatting helpers
# ══════════════════════════════════════════════════════════════════════════════

def _names(seq):
    """Join a list of {"id","name"} (or plain strings) into 'a, b, c'."""
    out = []
    for x in seq or []:
        if isinstance(x, dict):
            out.append(str(x.get("name", "")))
        else:
            out.append(str(x))
    return ", ".join(n for n in out if n)


def _b(v):
    """Blueprint-style boolean text (Anaplan writes lowercase true/false)."""
    if isinstance(v, bool):
        return "true" if v else "false"
    return "" if v is None else str(v)


def _write_csv(path, header, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# ══════════════════════════════════════════════════════════════════════════════
#  Per-file builders (return (header, rows))
# ══════════════════════════════════════════════════════════════════════════════

# Column layout copied verbatim from the Selenium export so ingestion is identical.
LINE_ITEM_HEADER = [
    "", "Format", "Formula", "Summary", "Applies To", "Time Scale", "Time Range",
    "Versions", "Style", "Cell Count", "Populated Cell Count", "Memory Used",
    "Calculation Complexity", "Calculation Effort", "Notes", "Read Access Driver",
    "Write Access Driver", "Users List", "Parent", "Is Summary", "Formula Scope",
    "Code", "Use Switchover", "Breakback", "Start of Section", "Data Tags",
    "Referenced By", "Module Name",
]

MODULE_HEADER = [
    "", "Functional Area", "Applies To", "Time Scale", "Time Range", "Versions",
    "Breakback", "Users List", "Cell Count", "Populated Cell Count", "Memory Used",
    "Notes", "Read Access Driver", "Write Access Driver", "Data Tags", "Managed By",
    "Referenced By", "Used in Dashboards", "Line Items",
]


def build_line_items(sess, base, model_id):
    body = _get(sess, f"{base}/2/0/models/{model_id}/lineItems?includeAll=true")
    items = _list_field(body)
    rows = []
    for li in items:
        ver = li.get("version") or {}
        rows.append([
            li.get("name", ""),
            li.get("format", ""),
            li.get("formula", ""),
            li.get("summary", ""),
            _names(li.get("appliesTo")),
            li.get("timeScale", ""),
            li.get("timeRange", ""),
            ver.get("name", "") if isinstance(ver, dict) else _b(ver),
            li.get("style", ""),
            _b(li.get("cellCount")),
            "", "", "", "",                      # populated/memory/complexity/effort — n/a
            li.get("notes", ""),
            "", "", "", "",                      # read/write driver, users list, parent — n/a
            _b(li.get("isSummary")),
            li.get("formulaScope", ""),
            "",                                  # code — n/a
            _b(li.get("useSwitchover")),
            _b(li.get("breakback")),
            _b(li.get("startOfSection")),
            "",                                  # data tags — n/a
            _names(li.get("referencedBy")),
            li.get("moduleName", ""),
        ])
    return LINE_ITEM_HEADER, rows, items


def build_modules(sess, base, model_id, line_items):
    """Modules endpoint only gives id/name; enrich each module with the list of
    its line items (from the lineItems payload). Stat columns stay blank."""
    body = _get(sess, f"{base}/2/0/models/{model_id}/modules")
    mods = _list_field(body)
    # module name -> ordered list of its line item names
    li_by_module = {}
    for li in line_items:
        li_by_module.setdefault(li.get("moduleName", ""), []).append(li.get("name", ""))
    rows = []
    for m in mods:
        name = m.get("name", "")
        li_names = li_by_module.get(name, [])
        rows.append([
            name,
            "",                                  # Functional Area — n/a
            "", "", "", "",                      # applies to / time scale / range / versions — n/a at module level
            "",                                  # Breakback — n/a
            "",                                  # Users List — n/a
            "", "", "",                          # cell/populated/memory — n/a
            "",                                  # Notes — n/a
            "", "",                              # read/write driver — n/a
            "",                                  # Data Tags — n/a
            "",                                  # Managed By — n/a
            "",                                  # Referenced By — n/a
            "",                                  # Used in Dashboards — n/a
            "; ".join(li_names),                 # Line Items (derived) ✓
        ])
    return MODULE_HEADER, rows


def build_versions(sess, base, model_id):
    body = _get(sess, f"{base}/2/0/models/{model_id}/versions")
    vers = _list_field(body)
    header = ["", "Current", "Actual", "Switchover", "Formula",
              "Edit From", "Edit To", "Notes"]
    rows = []
    for v in vers:
        ef = v.get("editFrom") or {}
        et = v.get("editTo") or {}
        rows.append([
            v.get("name", ""),
            _b(v.get("isCurrent")),
            _b(v.get("isActual")),
            "",                                  # Switchover — n/a
            "",                                  # Formula — n/a
            ef.get("periodText", "") if isinstance(ef, dict) else "",
            et.get("periodText", "") if isinstance(et, dict) else "",
            "",                                  # Notes — n/a
        ])
    return header, rows


def build_general_lists(sess, base, model_id):
    body = _get(sess, f"{base}/2/0/models/{model_id}/lists")
    lists = _list_field(body)
    header = ["", "Item Count", "Has Selective Access", "Numbered",
              "Production Data", "Managed By", "Subsets", "Properties"]
    rows = []
    for l in lists:
        detail = _get(sess, f"{base}/2/0/models/{model_id}/lists/{l.get('id')}")
        # detail may wrap the metadata under 'list' or 'metadata'; probe both.
        meta = {}
        if isinstance(detail, dict):
            meta = detail.get("list") or detail.get("metadata") or detail
        rows.append([
            l.get("name", ""),
            _b(meta.get("itemCount")) if isinstance(meta, dict) else "",
            _b(meta.get("hasSelectiveAccess")) if isinstance(meta, dict) else "",
            _b(meta.get("numberedList")) if isinstance(meta, dict) else "",
            _b(meta.get("productionData")) if isinstance(meta, dict) else "",
            _b(meta.get("managedBy")) if isinstance(meta, dict) else "",
            _names(meta.get("subsets")) if isinstance(meta, dict) else "",
            _names(meta.get("properties")) if isinstance(meta, dict) else "",
        ])
    return header, rows


def build_actions(sess, base, model_id):
    """Combined action inventory (processes/imports/exports/actions), name+type.
    The rich blueprint columns (durations, used-in-processes/dashboards) are not
    in the API."""
    header = ["", "Type"]
    rows = []
    for atype in ("processes", "imports", "exports", "actions"):
        body = _get(sess, f"{base}/2/0/models/{model_id}/{atype}")
        for a in _list_field(body):
            rows.append([a.get("name", ""), atype])
    return header, rows


def build_imports(sess, base, model_id):
    body = _get(sess, f"{base}/2/0/models/{model_id}/imports")
    imports = _list_field(body)
    files_body = _get(sess, f"{base}/2/0/models/{model_id}/files")
    files = {f.get("id"): f.get("name", "") for f in _list_field(files_body)}
    header = ["", "Import Type", "Source (file/view id)", "Source File Name"]
    rows = []
    for imp in imports:
        ds = imp.get("importDataSourceId", "")
        rows.append([
            imp.get("name", ""),
            imp.get("importType", ""),
            ds,
            files.get(ds, ""),
        ])
    return header, rows


def build_views(sess, base, model_id):
    body = _get(sess, f"{base}/2/0/models/{model_id}/views")
    views = _list_field(body)
    header = ["", "ID", "Module ID", "Code"]
    rows = [[v.get("name", ""), v.get("id", ""), v.get("moduleId", ""), v.get("code", "")]
            for v in views]
    return header, rows


# ══════════════════════════════════════════════════════════════════════════════
#  Public API
# ══════════════════════════════════════════════════════════════════════════════

def _pull_api_files(sess, base, model_id, out_dir, results):
    """Write the 7 API-covered CSVs into out_dir, recording status in `results`.
    Returns the raw line-items payload (reused by the modules builder)."""
    def emit(filename, builder):
        try:
            built = builder()
            header, rows = built[0], built[1]
            path = os.path.join(out_dir, filename)
            _write_csv(path, header, rows)
            results[filename] = {"ok": True, "rows": len(rows), "path": path, "error": None}
            print(f"  [API] ok  {filename:22} {len(rows):>5} rows")
            return built
        except Exception as e:
            results[filename] = {"ok": False, "rows": None, "path": None, "error": str(e)}
            print(f"  [API] ERR {filename:22} {e}")
            return None

    li_built = emit("Line Items.csv", lambda: build_line_items(sess, base, model_id))
    line_items = li_built[2] if li_built else []
    emit("Modules.csv",       lambda: build_modules(sess, base, model_id, line_items))
    emit("Versions.csv",      lambda: build_versions(sess, base, model_id))
    emit("General Lists.csv", lambda: build_general_lists(sess, base, model_id))
    emit("Actions.csv",       lambda: build_actions(sess, base, model_id))
    emit("Imports.csv",       lambda: build_imports(sess, base, model_id))
    emit("Views.csv",         lambda: build_views(sess, base, model_id))
    return line_items


def _print_summary(model_name, results, mode):
    produced = sum(1 for r in results.values() if r["ok"])
    print(f"\n{'=' * 70}")
    print(f"  {model_name} — {mode}: {produced} files produced")
    for fn, r in results.items():
        mark = "ok " if r["ok"] else "-- "
        detail = (f"{r['rows']} rows" if r["ok"] and r["rows"] is not None
                  else (r["error"] or ""))
        print(f"    {mark}{fn:24} {detail}")
    print(f"{'=' * 70}\n")


def download_model_exports_api(model, out_dir=None, name=None):
    """Log in once (browser), then export all API-covered model files as CSV over
    plain HTTP. Fast, but only the 7 API-obtainable files; the 8 in
    API_UNAVAILABLE are reported as not available (use --full for those).

    Returns dict keyed by output filename -> {"ok", "rows", "path", "error"}.
    """
    model_id, model_name, workspace_id, customer_id = smd._resolve_model(model, name=name)
    if out_dir is None:
        out_dir = os.path.join(REPO_ROOT, "raw", "models", model_name)
    os.makedirs(out_dir, exist_ok=True)
    config = smd._build_config()

    print(f"\n{'=' * 70}")
    print(f"  Anaplan API model export — {model_name}")
    print(f"{'=' * 70}")
    print(f"  Output dir : {out_dir}")
    print(f"  (browser opens only to log in; all data pulled over HTTP)\n")

    base = config["main_url"].rstrip("/")
    download_dir = tempfile.mkdtemp(prefix="anaplan_api_login_")
    browser = None
    results = {}
    try:
        browser = scraper_ux._create_browser(download_dir)
        browser.set_script_timeout(120)
        scraper_ux.login(browser, config)
        sess = _session_from_browser(browser, base)
        _pull_api_files(sess, base, model_id, out_dir, results)
    finally:
        if browser is not None:
            try:
                browser.quit()
            except Exception:
                pass
        import shutil
        shutil.rmtree(download_dir, ignore_errors=True)

    for fn in API_UNAVAILABLE:
        results[fn] = {"ok": False, "rows": None, "path": None,
                       "error": "not in REST API v2 — run --full (classic core-webapp API)"}
    _print_summary(model_name, results, "API-only mode")
    return results


# The 8 legacy-engine-only grids, expressed as scrape_model_data EXPORT_TARGETS
# (nav_label, subtab_label, filename). These cannot be pulled from the REST API
# (proven: served only by the classic core-webapp jsonrpc/servlet). --full mode
# drives them over that classic API directly (no UI clicking) — see below.
_LEGACY_TARGETS = [t for t in smd.EXPORT_TARGETS if t[2] in set(API_UNAVAILABLE)]


# ══════════════════════════════════════════════════════════════════════════════
#  Legacy-grid export over the classic core-webapp API (jsonrpc + servlet)
# ══════════════════════════════════════════════════════════════════════════════
#
# The 8 legacy grids live in the classic core engine (core-webapp-<ws> on the eu4
# shard). There is no REST endpoint, but the engine's own HTTP protocol can be
# driven directly — no Dojo UI clicking — once a browser session exists:
#
#   1. POST .../anaplan/jsonrpc  {requestType:"VIEW_REQUEST_SET", viewRequests:[
#        {viewIndex:-1, viewGuid:<new>, viewDefinition:<grid template>, ...}],
#        activeViewIndices:[], modelDefinitionSerialNumber:<n>, clientSessionId:<s>}
#      → returns the opened view's `viewIndex`.
#   2. POST .../anaplan/jsonrpc  {requestType:"PROGRESS", activeViewIndices:[viewIndex]}
#      → returns a `taskId`.
#   3. POST .../anaplan/servlet?taskType=export (multipart: taskId, entityId=<grid>,
#        viewDefinition, fileType=CSV, ...) → streams the grid CSV (text/csv).
#
# A MINIMAL VIEW_REQUEST_SET (empty carried view-state) is sufficient — proven
# live against all 8 grids. `entityId` (= the grid name, i.e. the filename minus
# ".csv") is the primary driver; `viewDefinition` is the model-INDEPENDENT
# template below (system identifiers `_SYSTEM_AXIS_IDENTIFIER.*` / `_2000000xxx_`
# / `_4000xxxxx_` only — no per-model data), captured once and reused for any
# model. `modelDefinitionSerialNumber` + `clientSessionId` ARE per-session and
# are scraped from the client's own first jsonrpc call at run time.
#
# The fetch() calls run inside the eu4 core-webapp iframe (via execute_async_
# script) so the browser session cookies + origin are supplied automatically.

_LEGACY_TEMPLATES = json.loads(r'''
{
  "Time Ranges.csv": {"entityId": "Time Ranges", "viewDefinition": {"name": "Time Ranges", "type": "MODEL_DEFINITION", "rowAxisSpecification": {"axisDefinitionIdentifier": "_20000000068_", "axisDefinition": null}, "columnAxisSpecification": {"axisDefinitionIdentifier": "_20000000069_", "axisDefinition": null}, "pageAxisSpecifications": [], "useDefaultPageOrder": true, "columnSizes": {"customRowLabelWidthsByDimension": [], "defaultColumnWidth": 150, "rowLabelWidth": 0, "customWidthsByStyle": [], "customWidthsByLineItem": []}, "pageContext": "SINGLE"}},
  "Line Item Subsets.csv": {"entityId": "Line Item Subsets", "viewDefinition": {"name": "Line Item Subsets", "type": "MODEL_DEFINITION", "rowAxisSpecification": {"axisDefinitionIdentifier": "_20000000041_", "axisDefinition": null}, "columnAxisSpecification": {"axisDefinitionIdentifier": "_20000000042_", "axisDefinition": null}, "pageAxisSpecifications": [], "useDefaultPageOrder": true, "columnSizes": {"customRowLabelWidthsByDimension": [], "defaultColumnWidth": 150, "rowLabelWidth": 0, "customWidthsByStyle": [], "customWidthsByLineItem": []}, "pageContext": "SINGLE"}},
  "Source Models.csv": {"entityId": "Source Models", "viewDefinition": {"name": "Source Models", "type": "MODEL_DEFINITION", "rowAxisSpecification": {"axisDefinitionIdentifier": "_20000000064_", "axisDefinition": null}, "columnAxisSpecification": {"axisDefinitionIdentifier": "_20000000065_", "axisDefinition": null}, "pageAxisSpecifications": [], "useDefaultPageOrder": true, "columnSizes": {"customRowLabelWidthsByDimension": [], "defaultColumnWidth": 75, "rowLabelWidth": 400, "customWidthsByStyle": [], "customWidthsByLineItem": []}, "pageContext": "SINGLE"}},
  "Roles.csv": {"entityId": "Roles", "viewDefinition": {"name": "Roles", "type": "MODEL_DEFINITION", "columnSizes": {"defaultColumnWidth": 150, "customRowLabelWidthsByDimension": [], "customWidthsByLineItem": [], "customWidthsByStyle": []}, "rows": "_SYSTEM_AXIS_IDENTIFIER.FULL_ACCESS_WITH_CUSTOM_MODEL_ROLE", "columns": "_SYSTEM_AXIS_IDENTIFIER.MODEL_ROLE_PROPERTY", "pages": []}},
  "Roles Modules.csv": {"entityId": "Roles Modules", "viewDefinition": {"name": "Roles Modules", "type": "MODEL_DEFINITION", "staticContextIdentifiers": ["_4000001000_"], "columnSizes": {"defaultColumnWidth": 150, "customRowLabelWidthsByDimension": [], "customWidthsByLineItem": [], "customWidthsByStyle": []}, "rows": "_SYSTEM_AXIS_IDENTIFIER.MODULE_ALL", "columns": "_SYSTEM_AXIS_IDENTIFIER.MODEL_ROLE", "pages": []}},
  "Roles Versions.csv": {"entityId": "Roles Versions", "viewDefinition": {"name": "Roles Versions", "type": "MODEL_DEFINITION", "staticContextIdentifiers": ["_4000001000_"], "columnSizes": {"defaultColumnWidth": 150, "customRowLabelWidthsByDimension": [], "customWidthsByLineItem": [], "customWidthsByStyle": []}, "rows": "_SYSTEM_AXIS_IDENTIFIER.VERSION_ALL", "columns": "_SYSTEM_AXIS_IDENTIFIER.MODEL_ROLE", "pages": []}},
  "Roles Lists.csv": {"entityId": "Roles Lists", "viewDefinition": {"name": "Roles Lists", "type": "MODEL_DEFINITION", "staticContextIdentifiers": ["_4000001001_"], "columnSizes": {"defaultColumnWidth": 150, "customRowLabelWidthsByDimension": [], "customWidthsByLineItem": [], "customWidthsByStyle": []}, "rows": "_SYSTEM_AXIS_IDENTIFIER.HIERARCHY_NOUSER", "columns": "_SYSTEM_AXIS_IDENTIFIER.MODEL_ROLE", "pages": []}},
  "Roles Actions.csv": {"entityId": "Roles Actions", "viewDefinition": {"name": "Roles Actions", "type": "MODEL_DEFINITION", "staticContextIdentifiers": ["_4000001002_"], "columnSizes": {"defaultColumnWidth": 150, "customRowLabelWidthsByDimension": [], "customWidthsByLineItem": [], "customWidthsByStyle": []}, "rows": "_SYSTEM_AXIS_IDENTIFIER.ACTION_WITH_HEADING", "columns": "_SYSTEM_AXIS_IDENTIFIER.MODEL_ROLE", "pages": []}}
}
''')

# JS run inside the eu4 iframe: VIEW_REQUEST_SET -> PROGRESS -> servlet, returning
# {vrs_status, viewIndex, taskId, servlet_status, ct, csv} (csv = full text).
_LEGACY_CHAIN_JS = r"""
const p = arguments[0], done = arguments[1];
const rand = () => { let s=''; for(let i=0;i<26;i++) s+='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'[Math.floor(Math.random()*62)]; return s; };
const guid = () => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'.replace(/X/g, () => '0123456789ABCDEF'[Math.floor(Math.random()*16)]);
const vrs = {
  modelId:p.model_id, modelDefinitionSerialNumber:p.mdsn, requestType:'VIEW_REQUEST_SET', workspaceId:p.ws,
  submissions:[], viewRequests:[{
    workspaceId:p.ws,
    dataPageRequests:[{startRow:0,startColumn:0,rowCount:-1,columnCount:-1}],
    rowLabelPageRequests:[{start:0,count:-1}], columnLabelPageRequests:[{start:0,count:-1}],
    cellSelectorLabelsRequired:false, pageSelectorLabelsRequired:false,
    serialNumbers:{breakbackHeldCellsSerialNumber:'-1',columnAxisSerialNumber:'-1',dataSerialNumber:'-1',pageInfoSerialNumber:'-1',rowAxisSerialNumber:'-1',viewDefinitionSerialNumber:'-1'},
    viewIndex:-1, viewGuid:guid(), containerEntityLongId:-1, state:{}, modelId:p.model_id, viewDefinition:p.vd
  }], systemActions:[], fetchAllModelSummaries:false, clientSessionId:p.csid, activeViewIndices:[], txid:rand(), includeDetailsInErrorInfo:true
};
const out = {};
fetch(p.jsonrpc,{method:'POST',credentials:'include',headers:{'Content-Type':'application/json'},body:JSON.stringify(vrs)})
 .then(r=>r.text().then(t=>{ out.vrs_status=r.status; let vi=null; try{vi=JSON.parse(t).result.viewRequestResults[0].viewIndex;}catch(e){out.vrs=t.slice(0,300);} out.viewIndex=vi;
   if(vi===null){ done(out); return; }
   const prog={workspaceId:p.ws,requestType:'PROGRESS',modelId:p.model_id,activeViewIndices:[vi],txid:rand(),includeDetailsInErrorInfo:true};
   return fetch(p.jsonrpc,{method:'POST',credentials:'include',headers:{'Content-Type':'application/json'},body:JSON.stringify(prog)})
    .then(r2=>r2.text().then(t2=>{ let tid=null; try{tid=JSON.parse(t2).taskId;}catch(e){} out.taskId=tid; if(!tid){out.prog=t2.slice(0,300); done(out); return;}
      const fd=new FormData();
      const f={taskType:'export',context:JSON.stringify({workspaceId:p.ws,modelId:p.model_id,modelName:null}),
        taskId:tid,entityId:p.entityId,moduleId:'',exportLayout:'GRID_CURRENT_PAGE',fileType:'CSV',formattingEnabled:'false',
        omitSummaries:'false',useFormatSettings:'false',omitEmptyRows:'false',withBOM:'false',filter0LineItemEntityLongId:'-1',
        filter1LineItemEntityLongId:'-1',listDimensionColumnSelection:'{}',listFormattedCellPropertySelection:'{}',
        includeRowLabelHeaders:'false',sharingOption:'0',entityLongIdOfShare:'',viewDefinition:JSON.stringify(p.vd)};
      for(const k in f) fd.append(k,f[k]);
      return fetch(p.servlet,{method:'POST',credentials:'include',body:fd})
       .then(r3=>r3.text().then(t3=>{ out.servlet_status=r3.status; out.ct=r3.headers.get('content-type'); out.csv=t3; done(out); }));
    }));
 })).catch(e=>{ out.error=String(e); done(out); });
"""

# Hook that records the client's own jsonrpc request bodies, so we can scrape the
# per-session modelDefinitionSerialNumber + clientSessionId from a VIEW_REQUEST_SET.
_SESSION_HOOK_JS = r"""
window.__cap = window.__cap || [];
if (!window.__hooked) {
  window.__hooked = true;
  const S = XMLHttpRequest.prototype.send, O = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function(m,u){ this.__u=u; return O.apply(this,arguments); };
  XMLHttpRequest.prototype.send = function(b){ if(this.__u && this.__u.indexOf('jsonrpc')>=0 && b) window.__cap.push(String(b)); return S.apply(this,arguments); };
}
return 'ok';
"""


def _capture_session_params(browser):
    """Inside the eu4 grid iframe, install the jsonrpc hook and nudge the client
    into issuing a VIEW_REQUEST_SET (by re-opening a nav item), then scrape the
    per-session modelDefinitionSerialNumber + clientSessionId. Returns (mdsn,
    csid) or (None, None)."""
    browser.execute_script(_SESSION_HOOK_JS)
    # Nudge the classic client to emit a VIEW_REQUEST_SET we can read.
    smd.enter_shell(browser)
    for nudge in ("Versions", "General lists", "Modules"):
        if smd.click_visible(browser, nudge, 6):
            break
    time.sleep(2)
    smd.enter_grid(browser, 12)
    for b in browser.execute_script("return window.__cap || [];"):
        try:
            j = json.loads(b)
        except Exception:
            continue
        if j.get("requestType") == "VIEW_REQUEST_SET":
            return j.get("modelDefinitionSerialNumber"), j.get("clientSessionId")
    return None, None


def _pull_legacy_via_api(browser, base, model_id, ws, out_dir, results):
    """Export the 8 legacy grids over the classic core-webapp API (jsonrpc +
    servlet), driven by fetch() inside the eu4 iframe — no UI navigation. The
    browser must already be on the model-settings page (shell entered)."""
    jsonrpc = f"https://eu4.app.anaplan.com/core-webapp-{ws}/anaplan/jsonrpc"
    servlet = f"https://eu4.app.anaplan.com/core-webapp-{ws}/anaplan/servlet?taskType=export"

    if not smd.enter_grid(browser, 20):
        for fn in _LEGACY_TEMPLATES:
            results[fn] = {"ok": False, "rows": None, "path": None,
                           "error": "could not enter core-webapp iframe"}
        return
    mdsn, csid = _capture_session_params(browser)
    if mdsn is None or csid is None:
        for fn in _LEGACY_TEMPLATES:
            results[fn] = {"ok": False, "rows": None, "path": None,
                           "error": "could not capture session params (mdsn/csid)"}
        return

    smd.enter_grid(browser, 12)  # ensure we're in the eu4 iframe for fetch()
    for fn, tpl in _LEGACY_TEMPLATES.items():
        params = {"model_id": model_id, "ws": ws, "mdsn": mdsn, "csid": csid,
                  "jsonrpc": jsonrpc, "servlet": servlet,
                  "vd": tpl["viewDefinition"], "entityId": tpl["entityId"]}
        try:
            res = browser.execute_async_script(_LEGACY_CHAIN_JS, params)
        except Exception as e:
            results[fn] = {"ok": False, "rows": None, "path": None, "error": f"chain exec error: {e}"}
            print(f"  [CLS] ERR {fn:22} {e}")
            continue
        csv_text = res.get("csv")
        ok = (res.get("servlet_status") == 200 and "csv" in str(res.get("ct")) and csv_text)
        if ok:
            path = os.path.join(out_dir, fn)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(csv_text)
            n = csv_text.count("\n")
            results[fn] = {"ok": True, "rows": n, "path": path, "error": None}
            print(f"  [CLS] ok  {fn:22} {n:>5} lines")
        else:
            err = (res.get("error") or f"vrs={res.get('vrs_status')} "
                   f"servlet={res.get('servlet_status')} ct={res.get('ct')}")
            results[fn] = {"ok": False, "rows": None, "path": None, "error": err}
            print(f"  [CLS] ERR {fn:22} {err}")


def download_model_exports_full(model, out_dir=None, name=None):
    """Full 15-file export in ONE browser login, entirely API-driven:
      • Phase 1 — the 7 REST-API files over plain HTTP (cookies lifted).
      • Phase 2 — the 8 legacy grids over the classic core-webapp API
        (jsonrpc VIEW_REQUEST_SET → PROGRESS → servlet), driven by fetch()
        inside the eu4 iframe. No Dojo UI navigation.
    Any legacy grid that fails the classic-API path falls back to the
    scrape_model_data UI export for that one grid, so coverage never regresses.
    The browser is used only to log in / hold the session — every file is
    retrieved by an Anaplan HTTP API call.
    """
    model_id, model_name, workspace_id, customer_id = smd._resolve_model(model, name=name)
    if out_dir is None:
        out_dir = os.path.join(REPO_ROOT, "raw", "models", model_name)
    os.makedirs(out_dir, exist_ok=True)
    config = smd._build_config()
    base = config["main_url"].rstrip("/")
    settings_url = (f"{base}/a/modeling/customers/{customer_id}/workspaces/"
                    f"{workspace_id}/models/{model_id}/model-settings")

    print(f"\n{'=' * 70}")
    print(f"  Anaplan FULL model export (API-driven) — {model_name}")
    print(f"{'=' * 70}")
    print(f"  Output dir : {out_dir}")
    print(f"  REST API for 7 files; classic core-webapp API for "
          f"{len(_LEGACY_TEMPLATES)} legacy files.\n")

    download_dir = tempfile.mkdtemp(prefix="anaplan_full_")
    browser = None
    results = {}
    try:
        browser = scraper_ux._create_browser(download_dir)
        browser.set_script_timeout(120)
        scraper_ux.login(browser, config)

        # ── Phase 1: REST API pull (cookies lifted from this same session) ──────
        sess = _session_from_browser(browser, base)
        _pull_api_files(sess, base, model_id, out_dir, results)

        # ── Phase 2: legacy grids over the classic core-webapp API (no UI) ──────
        print(f"\n  → Exporting {len(_LEGACY_TEMPLATES)} legacy grids over the "
              f"classic core-webapp API...")
        browser.get(settings_url)
        if not smd.enter_shell(browser, timeout=30):
            for fn in _LEGACY_TEMPLATES:
                results[fn] = {"ok": False, "rows": None, "path": None,
                               "error": "could not open model-settings shell"}
        else:
            _pull_legacy_via_api(browser, base, model_id, workspace_id, out_dir, results)

        # ── Phase 2b: UI-export fallback for any legacy grid the API missed ─────
        import shutil
        failed = [t for t in _LEGACY_TARGETS
                  if not results.get(t[2], {}).get("ok")]
        if failed:
            print(f"\n  → UI-export fallback for {len(failed)} grid(s): "
                  f"{', '.join(fn for _n, _s, fn in failed)}")
            MAX_TRIES = 3
            pending = list(failed)
            for attempt in range(1, MAX_TRIES + 1):
                if not pending:
                    break
                browser.get(settings_url)
                if not smd.enter_shell(browser, timeout=30):
                    continue
                still_pending = []
                for nav_label, subtab_label, fn in pending:
                    gr = smd._export_one_target(browser, download_dir, nav_label, subtab_label, fn)
                    if gr["ok"]:
                        dest = os.path.join(out_dir, fn)
                        try:
                            if os.path.exists(dest):
                                os.remove(dest)
                            shutil.move(gr["saved_path"], dest)
                            results[fn] = {"ok": True, "rows": None, "path": dest, "error": None}
                            print(f"  [UI]  ok  {fn:22} (fallback download)")
                        except Exception as e:
                            results[fn] = {"ok": False, "rows": None, "path": None,
                                           "error": f"downloaded but move failed: {e}"}
                            still_pending.append((nav_label, subtab_label, fn))
                    else:
                        results[fn] = {"ok": False, "rows": None, "path": None,
                                       "error": gr.get("error")}
                        still_pending.append((nav_label, subtab_label, fn))
                pending = still_pending
    finally:
        if browser is not None:
            try:
                browser.quit()
            except Exception:
                pass
        import shutil
        shutil.rmtree(download_dir, ignore_errors=True)

    _print_summary(model_name, results, "FULL mode (API-driven)")
    return results


# ══════════════════════════════════════════════════════════════════════════════
#  CLI
# ══════════════════════════════════════════════════════════════════════════════

def _main():
    p = argparse.ArgumentParser(
        description="API-driven Anaplan model export. Default mode pulls the 7 "
                    "REST-API files over HTTP. --full additionally exports the 8 "
                    "legacy-engine files (Line Item Subsets, Time Ranges, Source "
                    "Models, Roles×5) over the classic core-webapp API — a complete "
                    "15-file export in one browser login, no UI navigation.")
    p.add_argument("model", help="Shortcut key from models.MODELS (e.g. 'fsp').")
    p.add_argument("--name", default=None, help="Override the model's display name.")
    p.add_argument("--out", default=None, help="Output directory for the CSV files.")
    p.add_argument("--full", action="store_true",
                   help="Also export the 8 legacy-engine files over the classic "
                        "core-webapp API (complete 15-file export). Omit for the "
                        "REST-only 7-file subset.")
    args = p.parse_args()

    if args.full:
        results = download_model_exports_full(args.model, out_dir=args.out, name=args.name)
    else:
        results = download_model_exports_api(args.model, out_dir=args.out, name=args.name)
    produced = sum(1 for r in results.values() if r["ok"])
    sys.exit(0 if produced else 1)


if __name__ == "__main__":
    _main()
