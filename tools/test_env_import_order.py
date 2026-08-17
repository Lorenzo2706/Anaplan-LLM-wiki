"""
Regression test for the 2026-08-14 "models/None" incident.

`models.py` resolves every credential via `os.getenv(...)` at IMPORT TIME.
`fetch_model_data.py` must therefore call `load_dotenv()` BEFORE it imports
`models`, or every value in `models.MODELS` silently becomes `None` instead
of raising - which showed up live as a request to
`https://api.anaplan.com/2/0/models/None/views/...`.

This test proves the *mechanism* (import order), not the secret: it never
touches the developer's real `.env` or real Anaplan credentials. It launches
a subprocess in a fresh temp directory containing a synthetic `.env` with
fake values, imports `fetch_model_data` then `models` there, and asserts the
fake value made it into `models.MODELS`. If a future edit (e.g. an
import-sorter reordering the top-of-file imports) reintroduces the bug, this
test fails with `None` instead of the fake model id.

Why a subprocess instead of monkeypatching os.environ in-process: the bug is
specifically about *import order within a fresh interpreter* - `models.py`'s
`getenv(...)` calls only run once, at first import, and pytest's own
collection may have already imported `fetch_model_data`/`models` (directly or
via `tools/test_fetch_model_data.py`) by the time this test runs, with
whatever `.env` state happened to be live at that moment. Re-importing an
already-imported module is a no-op in Python, so asserting anything from
those cached modules in-process would not actually re-exercise the ordering
bug. A subprocess gets a clean, uncontaminated interpreter every time.

Why `python -c "..."` rather than a temp .py script file: python-dotenv's
`load_dotenv()` (with no explicit path) searches for `.env` starting from the
*calling frame's* file and walking up parent directories - EXCEPT when
`__main__` has no `__file__` attribute (as with `python -c`), in which case
it falls back to `os.getcwd()`. Using `-c` combined with `cwd=<temp dir>`
pins the search to the synthetic temp `.env` deterministically, regardless of
where `fetch_model_data.py` itself lives on disk (which could otherwise walk
up into a real, gitignored `tools/.env` on a developer's machine).
"""
import os
import subprocess
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).parent

# Real credential var names read by models.py (see tools/models.py), given
# obviously-fake values here. None of these are real secrets.
_FAKE_ENV_VARS = {
    "CUSTOMER_ID": "fake-customer-id",
    "DEV_POLARIS": "fake-workspace-id",
    "FSP_MODEL_ID": "fake-fsp-model-id-0123456789ab",
}

_PROBE_CODE = (
    "import fetch_model_data\n"
    "import models\n"
    "print(models.MODELS['fsp']['model_id'])\n"
)


def _run_probe(tmp_path):
    """Run _PROBE_CODE in a fresh interpreter, cwd'd into tmp_path (which
    holds the synthetic .env), with no real credential env vars inherited."""
    env = dict(os.environ)
    for key in _FAKE_ENV_VARS:
        env.pop(key, None)
    # `tools/` must be importable from the subprocess's cwd (tmp_path), which
    # is unrelated to the repo tree.
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        str(TOOLS_DIR) + (os.pathsep + existing_pythonpath if existing_pythonpath else "")
    )

    return subprocess.run(
        [sys.executable, "-c", _PROBE_CODE],
        cwd=str(tmp_path),
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_dotenv_loaded_before_models_import(tmp_path):
    """With the fix in place, a synthetic .env in the subprocess's cwd is
    picked up by fetch_model_data's load_dotenv() call before `models` is
    imported, so models.MODELS['fsp']['model_id'] reflects the fake value -
    not None."""
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(f"{k}={v}" for k, v in _FAKE_ENV_VARS.items()) + "\n",
        encoding="utf-8",
    )

    result = _run_probe(tmp_path)

    assert result.returncode == 0, (
        f"probe subprocess failed:\nstdout={result.stdout!r}\nstderr={result.stderr!r}"
    )
    assert result.stdout.strip() == _FAKE_ENV_VARS["FSP_MODEL_ID"]


def test_no_dotenv_no_env_no_traceback(tmp_path):
    """Sanity companion: with no .env file present at all (not even a
    synthetic one) and no relevant vars in the environment, importing
    fetch_model_data must not raise - models.MODELS['fsp']['model_id'] is
    simply None. This pins down that the fix's fallback path (no .env found)
    is not itself a source of crashes."""
    result = _run_probe(tmp_path)

    assert result.returncode == 0, (
        f"probe subprocess failed:\nstdout={result.stdout!r}\nstderr={result.stderr!r}"
    )
    assert result.stdout.strip() == "None"
