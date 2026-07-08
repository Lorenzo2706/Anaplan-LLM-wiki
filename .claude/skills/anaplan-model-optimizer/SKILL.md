---
name: anaplan-model-optimizer
description: >
  Analyze a production Anaplan model end-to-end to find modules that are safe to
  delete. Runs scraper_ux.py to pull a fresh new-UX (NUX) usage export for the
  chosen model, then cross-references it against the model's raw CSV export
  (cross-module formula references, import/export targets, classic dashboard
  usage) so it never flags Data/Load/Calculation modules that are intentionally
  invisible in the UX but still feed other modules. Reports genuine dead-module
  candidates in chat. Use this skill whenever the user asks to optimize, clean
  up, shrink, or reduce the size/complexity of an Anaplan model, asks which
  modules are unused/orphaned/dead/safe to delete, mentions running the NUX/UX
  scraper or scraper_ux.py, or wants a "model health check" or "model
  housekeeping" pass. Always prefer this skill over eyeballing the Excel
  output manually - the cross-referencing against Modules.csv and Imports.csv
  is what prevents false positives on load-bearing backend modules.
---

# Anaplan Model Optimizer

Finds modules in a production Anaplan model that can likely be deleted, by
combining two signals that neither one alone can safely provide:

1. **New-UX (NUX) exposure** - is the module shown on any app page/board? Comes
   from `scraper_ux.py`, which is the only source for this (it isn't in the
   static CSV export).
2. **Internal load-bearing-ness** - does the module feed other modules via
   formula, get written to by an import, or appear on a classic dashboard?
   Comes from the model's raw CSV export (`raw/models/<Model>/Modules.csv` and
   `Imports.csv`), which the NUX scrape cannot see.

A module with zero NUX exposure is **not** automatically dead - Data, Load, and
Calculation modules in the DISCO pattern are *designed* to be invisible in the
UX; their only consumers are other modules' formulas. Only flag a module when
**both** signals come back empty. Getting this cross-check wrong means telling
the user to delete something that quietly breaks half the model.

## Step 1 - Identify the target model

Ask which model to analyze if it isn't already clear from context. The
cross-reference in Step 4 needs `raw/models/<Model Name>/Modules.csv` (and
ideally `Imports.csv`) to already exist - these are the CSVs the
`wiki-data-ingestion` skill produces from a model's own CSV export. Per the
project's `CLAUDE.md`, the three currently-ingested models are:

- `FSP 2.0` - Polaris
- `AAC` - Polaris
- `MJP` - Classic (~440 modules)

If the requested model has no `raw/models/<Model Name>/` folder yet, tell the
user Step 4's safety cross-check needs at least a `Modules.csv` export dropped
there first (via the `wiki-data-ingestion` skill) - offer to proceed
Excel-only in the meantime, but flag every result as unverified against
internal formula dependencies if they choose that path.

## Step 2 - Make sure the model has a scraper shortcut

`scraper_ux.py` prompts interactively for everything, including a numbered
pick from a live list of every model in the tenant. To automate it safely,
the target model must be a pre-configured shortcut in `models.py` (see the
`fsp` entry there) - that turns "pick from a live list" into "type a known
number," which is the only part of the wizard that can't otherwise be
scripted blind.

1. Read `models.py`. `MODELS` is a dict; a model counts as a usable shortcut
   only if `customer_id`, `workspace_id`, and `model_id` are all truthy.
   Compute the 1-based position of the target model among the usable
   shortcuts, in dict order - that number is exactly what the wizard's
   "MODEL SELECTION" menu will show.
2. If the target model has no shortcut yet, you need its Anaplan model GUID.
   Ask the user for it - they can copy it out of the browser address bar while
   the model is open in Anaplan (`.../models/<GUID>/...`). Then:
   - Append `<PREFIX>_MODEL_ID=<guid>` to `.env` (pick a short prefix from the
     model name, e.g. `AAC`, `MJP`).
   - Add a matching entry to the `MODELS` dict in `models.py`, mirroring the
     `"fsp"` entry exactly (same `customer_id`/`workspace_id` variables, new
     `model_id` env var).
   - Re-read the file to recompute the shortcut's numeric position.
3. Preflight-check `.env` has what non-interactive login needs, **without
   printing or reading any secret values** - only check presence, e.g.:
   ```
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('ANAPLAN_USERNAME' in os.environ and bool(os.getenv('ANAPLAN_USERNAME')), bool(os.getenv('ANAPLAN_PASSWORD')), bool(os.getenv('CUSTOMER_ID')), bool(os.getenv('DEV_POLARIS')))"
   ```
   `ANAPLAN_PASSWORD` in particular is non-negotiable for automation: if it's
   missing, `scraper_ux.py` falls back to `getpass.getpass()`, which cannot be
   fed through a piped stdin sequence and will hang the run. If any of these
   come back `False`, stop and ask the user to fill in `.env` (never ask them
   to paste the value into chat - just tell them which key is missing).

## Step 3 - Run scraper_ux.py

The wizard asks a fixed sequence of questions; with `.env` filled in, every
one of them has a usable default except the model-selection number and the
final "scrape another model?" loop (which defaults to "yes" and must be
stopped explicitly). In order:

1. Anaplan environment - accept default
2. Email - accept default (password is read from `.env` directly, no prompt)
3. SSO? - accept default
4. Output folder - accept default
5. "Everything correct?" - accept default (yes)
6. Model selection - **the shortcut number from Step 2**
7. "Ready to scrape '<model>'. Continue?" - accept default (yes)
8. "Would you like to scrape another model?" - must answer **no**, or the
   wizard loops back to model selection with no way to feed it a second
   pre-computed choice

That means the full stdin payload is five blank lines, the shortcut number,
one more blank line, then `n`:

```bash
printf '\n\n\n\n\n%s\n\nn\n' "<shortcut_number>" | python scraper_ux.py
```

Run this in the background - it opens a real (non-headless) Edge window and
can take several minutes on large models (MJP has ~440 modules). Tell the
user up front: *"A browser window is about to open. If your organization uses
SSO with MFA, please complete that step in the window when it appears - the
script only pauses briefly after login before it starts pulling data."*
Because the browser isn't headless, the user can freely interact with it on
their own screen even though the wizard's text answers are coming from the
piped stdin.

Wait for the background command to finish, then find the newest file matching
`Anaplan NUX Report - <model name>_*.xlsx` in the output folder (`.env`'s
`ANAPLAN_OUTPUT_FOLDER`, or the script's default
`~/Documents/Anaplan NUX Reports` if unset).

If the run fails or hangs (most commonly: an SSO/MFA challenge that took
longer than the script's fixed post-login wait, so the subsequent API calls
came back as an HTML login page instead of JSON), tell the user what
happened and offer to retry.

## Step 4 - Cross-reference the report

Run the bundled script:

```bash
python .claude/skills/anaplan-model-optimizer/scripts/analyze_module_usage.py \
  --excel "<path to the NUX report .xlsx>" \
  --model-dir "raw/models/<Model Name>" \
  --model-name "<Model Name>" \
  --out-json "analyses/<Model Name>-module-optimization-<YYYY-MM-DD>.json" \
  --out-markdown "analyses/<Model Name>-module-optimization-<YYYY-MM-DD>.md"
```

This does the actual cross-referencing in code rather than by reading the
spreadsheet by eye, because the safety logic (don't flag a module that's
referenced elsewhere) needs to be exact, not approximate. For each module it
checks, in order:

1. NUX usage count > 0 → **active**, definitely keep
2. Referenced by another module's formula (`Modules.csv` "Referenced By") →
   **keep**, it's an internal dependency
3. Used on a classic dashboard (`Modules.csv` "Used in Dashboards") → **keep**
4. Source or target of an import/export (`Imports.csv`, plus the report's own
   per-model actions sheet) → **keep**
5. None of the above → **candidate for review**

It also separately flags any module the CSV export knows about but the NUX
report doesn't mention at all (name mismatch, or the export predates a rename)
- treat those as a data-quality flag, not a deletion candidate, and ask the
user to double check the name.

Per the project's `raw/` conventions, never edit the CSVs or the xlsx - this
script only reads them.

## Step 5 - Report in chat

Present the results directly in the conversation, not just a pointer to the
saved file:

- Lead with the candidate-for-review table (module name + functional area).
  Frame it as *"these look safe to review for deletion"*, not *"delete these"*
  - text-based reference parsing can miss dynamic references (e.g. `SELECT`
    on a computed string), so recommend the user do a final native check in
    Anaplan (e.g. the module's dependency/blueprint view) before deleting
    anything.
  - Group by functional area if there are more than a handful, so the user can
    see whether a whole retired workstream can go at once.
- Briefly show the "kept despite zero NUX usage" table too, with the reason -
  this is what lets the user trust the candidate list instead of wondering
  whether the analysis just missed something.
- Mention the full report was saved under `analyses/` per this project's
  convention for non-wiki outputs.
- This skill only recommends. Never delete anything - the user removes
  modules from the model themselves in Anaplan.
