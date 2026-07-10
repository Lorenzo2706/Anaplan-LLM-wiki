"""
scrape_model_data.py
---------------------
Automated Anaplan model-settings CSV exporter.

This script reuses scraper_ux.py's authentication and download helpers
(_create_browser, login, _wait_for_download, _parse_downloaded_file,
_safe_filename) as a black box — scraper_ux.py itself is never modified.
All navigation/export logic (nested-iframe handling, left-nav + sub-tab
clicking, the Dojo "Export..." / "Run Export" flow, and the list of 13
export targets) lives entirely in this file.

Why the export flow is bespoke
-------------------------------
The model-settings UI is a legacy Dojo app rendered inside NESTED iframes:
an OUTER shell iframe (data-testid="shell-content") that holds the
left-nav, and an INNER grid iframe (its first nested iframe) that holds
the sub-tabs, grid toolbar, and export dialog. The toolbar "Export..."
control is a <span class="dijitButtonText">, not a <button>, so
scraper_ux._click_export_button / _confirm_export_dialog do NOT work here
— we click visible elements directly and press the dialog's "Run Export"
button instead. The export dialog defaults File Type to CSV, so we leave
it untouched.

Usage
-----
As a library:

    from scrape_model_data import download_model_exports
    results = download_model_exports("fsp")

From the command line:

    python scrape_model_data.py fsp
    python scrape_model_data.py fsp --name "FSP 2.0" --out "raw/models/FSP 2.0"

To find a model that has no models.py shortcut yet (no export possible until
one is registered):

    python scrape_model_data.py --list-models

Configuration (username, password, environment, SSO flag) is sourced
from .env exactly like scraper_ux.py — importing scraper_ux triggers its
load_dotenv() call, so no separate .env loading is needed here.

Note: importing this module never launches a browser or touches the
network — the browser is only created inside download_model_exports() /
list_available_models().
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
import time
from glob import glob

from selenium.webdriver.common.by import By

# NOTE: import scraper_ux BEFORE models. scraper_ux calls load_dotenv() at import
# time and then imports models; models.py reads its env vars (CUSTOMER_ID,
# DEV_POLARIS, *_MODEL_ID) at import time. Importing models first would evaluate
# those getenv() calls before .env is loaded, yielding all-None shortcut values.
import scraper_ux
import models

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# ══════════════════════════════════════════════════════════════════════════════
#  The 13 export targets: (left-nav label, sub-tab label or None, output filename)
# ══════════════════════════════════════════════════════════════════════════════

EXPORT_TARGETS = [
    ("Modules", "Modules", "Modules.csv"),
    ("Modules", "Line Items", "Line Items.csv"),
    ("Line item subsets", None, "Line Item Subsets.csv"),
    ("General lists", None, "General Lists.csv"),
    ("Versions", None, "Versions.csv"),
    ("Time", "Time Ranges", "Time Ranges.csv"),
    ("Actions", "Actions", "Actions.csv"),
    ("Source models", None, "Source Models.csv"),
    ("Users", "Roles", "Roles.csv"),
    ("Users", "Roles → Modules", "Roles Modules.csv"),
    ("Users", "Roles → Versions", "Roles Versions.csv"),
    ("Users", "Roles → Lists", "Roles Lists.csv"),
    ("Users", "Roles → Actions", "Roles Actions.csv"),
]


# ══════════════════════════════════════════════════════════════════════════════
#  Iframe / navigation helpers (verified against the live Dojo UI)
# ══════════════════════════════════════════════════════════════════════════════

def enter_shell(browser, timeout=25):
    """default_content -> outer shell iframe. Left-nav lives here."""
    end = time.time() + timeout
    while time.time() < end:
        try:
            browser.switch_to.default_content()
            outer = (browser.find_elements(By.CSS_SELECTOR, 'iframe[data-testid="shell-content"]')
                     or browser.find_elements(By.TAG_NAME, "iframe"))
            if not outer:
                time.sleep(0.5); continue
            browser.switch_to.frame(outer[0])
            body = browser.execute_script("return document.body ? document.body.innerText : ''") or ""
            if any(k in body for k in ("Modules", "General lists", "Versions")):
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def enter_grid(browser, timeout=25):
    """default -> outer shell iframe -> inner grid iframe. Toolbar/tabs/dialog live here."""
    end = time.time() + timeout
    while time.time() < end:
        try:
            browser.switch_to.default_content()
            outer = (browser.find_elements(By.CSS_SELECTOR, 'iframe[data-testid="shell-content"]')
                     or browser.find_elements(By.TAG_NAME, "iframe"))
            if not outer:
                time.sleep(0.5); continue
            browser.switch_to.frame(outer[0])
            inner = browser.find_elements(By.TAG_NAME, "iframe")
            if not inner:
                time.sleep(0.5); continue
            browser.switch_to.frame(inner[0])
            if browser.execute_script("return !!document.querySelector('.dijitButtonText');"):
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def click_visible(browser, text, timeout=8, contains_all=None):
    """Click the first VISIBLE element whose normalized text == text.
    If contains_all is a list, instead match a visible element whose text contains
    every string in it (used for 'Roles → Modules' style tabs)."""
    end = time.time() + timeout
    if contains_all:
        xp = "//*[self::span or self::div or self::button or @role='tab' or @role='button' or self::a]"
    else:
        xp = (f"//span[normalize-space()='{text}'] | //*[@role='button'][normalize-space()='{text}'] "
              f"| //button[normalize-space()='{text}'] | //div[normalize-space()='{text}'] "
              f"| //*[@role='tab'][normalize-space()='{text}']")
    while time.time() < end:
        for el in browser.find_elements(By.XPATH, xp):
            try:
                if not el.is_displayed():
                    continue
                t = " ".join((el.text or "").split())
                if contains_all:
                    if not all(p in t for p in contains_all):
                        continue
                browser.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                time.sleep(0.1)
                try:
                    el.click()
                except Exception:
                    browser.execute_script("arguments[0].click();", el)
                return True
            except Exception:
                continue
        time.sleep(0.3)
    return False


def _alnum(s):
    return "".join(ch for ch in (s or "").lower() if ch.isalnum())


def click_tab(browser, label, timeout=10):
    """Click a Dojo grid sub-tab by label.

    Sub-tab labels render as <span role="tab" class="tabLabel"> with the text
    CONCATENATED and no separator — e.g. the "Roles → Modules" tab (the arrow is
    a CSS icon) has innerText "RolesModules". So we match on alphanumeric-only
    text: "Roles → Modules" -> "rolesmodules" == element "RolesModules".
    Restricting to role='tab'/tab-class elements avoids matching a wrapping
    container that happens to contain the same words.
    """
    want = _alnum(label)
    xp = ("//*[@role='tab'] | //*[contains(@class,'tabLabel')] "
          "| //*[contains(@class,'dijitTab')]")
    end = time.time() + timeout
    while time.time() < end:
        for el in browser.find_elements(By.XPATH, xp):
            try:
                if not el.is_displayed():
                    continue
                if _alnum(el.text) == want:
                    browser.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                    time.sleep(0.1)
                    try:
                        el.click()
                    except Exception:
                        browser.execute_script("arguments[0].click();", el)
                    return True
            except Exception:
                continue
        time.sleep(0.3)
    return False


# ══════════════════════════════════════════════════════════════════════════════
#  Per-grid orchestration
# ══════════════════════════════════════════════════════════════════════════════

def _export_one_target(browser, download_dir, nav_label, subtab_label, out_filename):
    """
    Navigate to one (nav_label, subtab_label) grid and export it to CSV.
    Returns {"ok": bool, "saved_path": str|None, "raw_name": str|None,
             "error": str|None}. Never raises.
    """
    result = {"ok": False, "saved_path": None, "raw_name": None, "error": None}
    tag = f"[{nav_label}" + (f" > {subtab_label}]" if subtab_label else "]")

    def fail(msg):
        result["error"] = msg
        print(f"  {tag} ✗ {msg}")
        return result

    try:
        # 1. Left-nav lives in the OUTER shell frame.
        if not enter_shell(browser):
            return fail("no shell")
        if not click_visible(browser, nav_label, 10):
            return fail("nav not found")
        time.sleep(2)

        # 2. Sub-tabs, toolbar and dialog live in the INNER grid frame.
        if not enter_grid(browser):
            return fail("no grid iframe")

        if subtab_label:
            if not click_tab(browser, subtab_label, 10):
                return fail("subtab not found")
            time.sleep(2)
            enter_grid(browser, 10)  # re-acquire after tab click

        # 3. Export via the Dojo toolbar + dialog.
        before = set(glob(os.path.join(download_dir, "*")))
        if not click_visible(browser, "Export...", 10):
            return fail("Export button not found")
        time.sleep(3)
        enter_grid(browser, 10)  # dialog is in the inner grid frame
        if not click_visible(browser, "Run Export", 10):
            return fail("Run Export not found")

        downloaded = scraper_ux._wait_for_download(download_dir, before, timeout=90)
        if not downloaded:
            return fail("no download")

        result["raw_name"] = os.path.basename(downloaded)
        result["saved_path"] = downloaded
        result["ok"] = True

        try:
            size = os.path.getsize(downloaded)
            print(f"  {tag} ✅ downloaded '{result['raw_name']}' ({size} bytes)")
        except OSError:
            print(f"  {tag} ✅ downloaded '{result['raw_name']}'")

        return result

    except Exception as e:
        return fail(f"unexpected error: {e}")


# ══════════════════════════════════════════════════════════════════════════════
#  Public API
# ══════════════════════════════════════════════════════════════════════════════

def _resolve_model(model, name=None):
    """
    Resolve `model` (a models.MODELS shortcut key, or a raw model_id GUID)
    into (model_id, model_name, workspace_id, customer_id).
    """
    configured = getattr(models, "MODELS", {})

    if model in configured:
        m = configured[model]
        model_id = m.get("model_id")
        workspace_id = m.get("workspace_id")
        customer_id = m.get("customer_id")
        model_name = name or m.get("name", model)
        missing = [k for k, v in (
            ("model_id", model_id), ("workspace_id", workspace_id),
            ("customer_id", customer_id),
        ) if not v]
        if missing:
            raise ValueError(
                f"models.MODELS['{model}'] is missing {missing} — check your .env "
                f"entries for this shortcut."
            )
        return model_id, model_name, workspace_id, customer_id

    # Treat `model` as a raw model_id GUID. A raw ID has no reliable way to
    # infer its workspace (only CUSTOMER_ID is shared tenant-wide), so require
    # it be registered in models.py instead of guessing.
    raise ValueError(
        f"'{model}' is not a configured shortcut in models.MODELS "
        f"({list(configured.keys())}). Raw model_id lookups need a workspace "
        f"ID that cannot be safely inferred — please add a shortcut entry to "
        f"models.py (mirroring the 'fsp' entry) with customer_id, "
        f"workspace_id, and model_id, then pass its key here."
    )


def _build_config():
    environment = os.getenv("ANAPLAN_ENVIRONMENT", "eu2a")
    main_url = scraper_ux.ANAPLAN_URLS.get(environment, scraper_ux.ANAPLAN_URLS["eu2a"])
    use_sso = os.getenv("ANAPLAN_USE_SSO", "false").strip().lower() in ("1", "true", "yes")
    return {
        "main_url": main_url,
        "username": os.getenv("ANAPLAN_USERNAME", ""),
        "password": os.getenv("ANAPLAN_PASSWORD", ""),
        "use_basic_auth": not use_sso,
        "output_folder": tempfile.gettempdir(),  # only used by scraper_ux.login() logging path
    }


def list_available_models():
    """
    Log in and fetch every model visible to this account via the live Anaplan
    API (springboard-platform-gateway-service), independent of models.MODELS
    shortcuts. For use when a model hasn't been registered as a shortcut yet
    and its workspace/customer IDs are unknown.

    Returns a list of dicts: model_name, model_id, workspace_name,
    workspace_id, customer_id — one per model, sorted by workspace then name.
    """
    config = _build_config()
    download_dir = tempfile.mkdtemp(prefix="anaplan_list_models_")
    browser = None
    try:
        browser = scraper_ux._create_browser(download_dir)
        scraper_ux.login(browser, config)

        main_url = config["main_url"]
        data = scraper_ux.api_get(
            browser,
            f"{main_url}/a/springboard-platform-gateway-service/models?limit=50000&offset=0",
        )
        items = data.get("items", []) or []

        out = []
        for m in items:
            ws_guid = m.get("CurrentWorkspaceGuid") or m.get("WorkspaceGuid", "")
            customer = m.get("CustomerGuid") or m.get("TenantGuid", "")
            if not customer and ws_guid:
                try:
                    ws_resp = scraper_ux.api_get(browser, f"{main_url}/1/3/workspaces/{ws_guid}")
                    customer = ws_resp.get("workspace", {}).get("customerId", "")
                except Exception:
                    pass
            out.append({
                "model_name": m.get("ModelName"),
                "model_id": m.get("ModelGuid"),
                "workspace_name": m.get("CurrentWorkspaceName") or m.get("WorkspaceName") or "Unknown workspace",
                "workspace_id": ws_guid,
                "customer_id": customer,
            })
        out.sort(key=lambda m: (m["workspace_name"] or "", m["model_name"] or ""))
        return out
    finally:
        if browser is not None:
            try:
                browser.quit()
            except Exception:
                pass
        shutil.rmtree(download_dir, ignore_errors=True)


def download_model_exports(model, out_dir=None, headless_download_dir=None, name=None):
    """
    Log into Anaplan, open the given model's model-settings shell, and
    export all 13 grids (see EXPORT_TARGETS) as CSV files.

    Args:
        model: a key in models.MODELS (e.g. "fsp") OR a raw model_id GUID
               (raw IDs must still resolve via models.MODELS today — see
               _resolve_model for why).
        out_dir: destination folder for the CSVs. Defaults to
                 raw/models/<model name>/ under the repo root.
        headless_download_dir: temp folder Selenium downloads into before
                 files are moved into out_dir. Defaults to a fresh
                 tempfile.mkdtemp().
        name: override the resolved model's display name.

    Returns:
        dict keyed by output filename -> {"ok": bool, "saved_path": str|None,
        "raw_name": str|None, "error": str|None}.
    """
    model_id, model_name, workspace_id, customer_id = _resolve_model(model, name=name)

    if out_dir is None:
        out_dir = os.path.join(REPO_ROOT, "raw", "models", model_name)
    os.makedirs(out_dir, exist_ok=True)

    download_dir = headless_download_dir or tempfile.mkdtemp(prefix="anaplan_scrape_")
    own_download_dir = headless_download_dir is None

    config = _build_config()
    base = config["main_url"].rstrip("/")  # double slash -> "can't find this page" 404
    settings_url = (
        f"{base}/a/modeling/customers/{customer_id}/workspaces/{workspace_id}"
        f"/models/{model_id}/model-settings"
    )

    results = {}
    browser = None

    try:
        print(f"\n{'=' * 70}")
        print(f"  Anaplan model export scraper — {model_name}")
        print(f"{'=' * 70}")
        print(f"  Settings URL : {settings_url}")
        print(f"  Output dir   : {out_dir}\n")

        browser = scraper_ux._create_browser(download_dir)
        browser.set_script_timeout(120)

        scraper_ux.login(browser, config)

        print(f"  → Opening model-settings shell...")
        browser.get(settings_url)

        if not enter_shell(browser, timeout=30):
            raise RuntimeError(
                "Could not enter the model-settings iframe after navigating "
                "to the settings URL — check the URL/credentials/model IDs."
            )

        for nav_label, subtab_label, out_filename in EXPORT_TARGETS:
            grid_result = _export_one_target(
                browser, download_dir, nav_label, subtab_label, out_filename
            )

            if grid_result["ok"]:
                dest_path = os.path.join(out_dir, out_filename)
                try:
                    if os.path.exists(dest_path):
                        os.remove(dest_path)
                    shutil.move(grid_result["saved_path"], dest_path)
                    grid_result["saved_path"] = dest_path
                except Exception as e:
                    grid_result["ok"] = False
                    grid_result["error"] = f"downloaded but failed to move file: {e}"
                    print(f"    ✗ could not move to {dest_path}: {e}")

            results[out_filename] = grid_result

    finally:
        if browser is not None:
            try:
                browser.quit()
            except Exception:
                pass
        if own_download_dir:
            shutil.rmtree(download_dir, ignore_errors=True)

    ok_count = sum(1 for r in results.values() if r["ok"])
    print(f"\n{'=' * 70}")
    print(f"  {ok_count}/{len(EXPORT_TARGETS)} exported")
    for out_filename, r in results.items():
        marker = "✅" if r["ok"] else "✗"
        detail = r["saved_path"] if r["ok"] else r["error"]
        print(f"    {marker} {out_filename:<22} {detail}")
    print(f"{'=' * 70}\n")

    return results


# ══════════════════════════════════════════════════════════════════════════════
#  CLI
# ══════════════════════════════════════════════════════════════════════════════

def _main():
    parser = argparse.ArgumentParser(
        description="Automated Anaplan model-settings CSV exporter "
                    "(reuses scraper_ux.py's login/download helpers).",
    )
    parser.add_argument(
        "model",
        nargs="?",
        default=None,
        help="Shortcut key from models.MODELS (e.g. 'fsp') or a raw model_id GUID "
             "(raw IDs currently still require a matching models.py shortcut). "
             "Omit when using --list-models.",
    )
    parser.add_argument("--name", default=None, help="Override the model's display name.")
    parser.add_argument("--out", default=None, help="Output directory for the CSV files.")
    parser.add_argument(
        "--list-models", action="store_true",
        help="Log in, fetch every model visible to this account via the live Anaplan "
             "API, print it as JSON to stdout, and exit — no export, no models.py "
             "shortcut required. Use this to find the model_id/workspace_id/customer_id "
             "for a model that isn't registered in models.py yet.",
    )
    args = parser.parse_args()

    if args.list_models:
        print(json.dumps(list_available_models(), indent=2))
        sys.exit(0)

    if not args.model:
        parser.error("model is required unless --list-models is passed")

    results = download_model_exports(args.model, out_dir=args.out, name=args.name)

    ok_count = sum(1 for r in results.values() if r["ok"])
    sys.exit(0 if ok_count == len(EXPORT_TARGETS) else 1)


if __name__ == "__main__":
    _main()
