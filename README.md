# Anaplan LLM Wiki

A **Claude Code-powered knowledge vault** for Anaplan model builders. Drop in Anapedia docs, articles, and model CSV exports; Claude ingests them into a structured, interlinked Obsidian-style wiki that becomes durable context for future model-building work (formulas, debugging, design reviews, deltas across re-uploads).

The wiki is the agent's **external memory** — not the product. The point is that every subsequent question Claude answers ("write me a formula for X", "what changed in this re-upload", "is this Polaris-safe?") is grounded in your actual model context, accumulated over time.

---

## What you get

- **Claude Code as an Anaplan model-builder agent** with a project-specific system prompt (`CLAUDE.md`) that defines a vault schema, ingest/query/lint workflows, and Anaplan-aware conventions (DISCO, PLANS, engine-aware reasoning).
- **A vault layout** that separates immutable sources (`raw/`) from generated, queryable wiki pages (`wiki/`).
- **Seven skills** that auto-activate from context, all shipped as project skills in `.claude/skills/`: `first-setup` (one-time bootstrap of a freshly cloned vault — builds the empty folder skeleton, flattens the sample docs, adopts `CLAUDE.md`, verifies skills are in place), `anaplan-formula-agent` (formula writing/debugging, Step-0 context-loading + Classic-vs-Polaris reasoning), `anaplan-module-mapping` (cross-module wiring — delivers dual financial-logic + Anaplan-mechanics explanations for every formula), `anaplan-model-optimizer` (runs the NUX/UX scraper for a model and cross-references usage against the raw CSV export to flag genuinely dead modules, never the ones invisible-by-design), `anaplan-model-documentation` (fans out parallel research agents to assemble a full Word documentation deliverable for a model), `wiki-lint` (generic wiki sanity-check — orphans, broken links, stale stats, contradictions, auto-fix pass), and `wiki-data-ingestion` (structured ingest of docs and model CSVs — path acquisition, grouping, delta detection, index/log updates, post-ingest summary).
- **Obsidian compatibility** — open the vault in Obsidian to browse `[[wiki links]]` visually while Claude maintains it.

---

## Prerequisites

- [Claude Code](https://docs.claude.com/en/docs/claude-code) installed (CLI or IDE extension).
- A local folder you'll use as the vault root (this becomes Claude Code's working directory).
- [Obsidian](https://obsidian.md/) pointed at the same folder for browsing the wiki.

No databases, no servers, no API keys beyond what Claude Code itself needs. Everything is flat markdown + CSVs on disk.

---

## Setup

### Quick start (recommended)

1. Clone the repo and start Claude Code inside it:
   ```powershell
   git clone <repo-url> <vault-root>
   cd <vault-root>
   claude
   ```
2. Tell Claude: **"Run first-time setup."** The `first-setup` skill (ships in `.claude/skills/`, so it's available immediately) takes it from there — it:
   - builds the empty `raw/models/`, `raw/logs/`, `raw/assets/`, `wiki/concepts/`, `wiki/functions/`, `wiki/models/`, `wiki/patterns/`, `wiki/sources/`, `analyses/`, and `Clippings/` folders (git doesn't track empty directories, so these don't exist yet on a fresh clone),
   - flattens the shipped `raw/docs/First setup/` sample bundle into `raw/docs/` and simplifies `.gitignore` to match,
   - copies `CLAUDE.md.example` to `CLAUDE.md`, strips the notes that only apply to the unflattened layout, and asks you for your vault root path and each model's name + engine (Classic/Polaris) to fill in,
   - reports which project skills are present under `.claude/skills/` (all seven ship with the repo, so normally all are).

That's it. Claude will create `wiki/` pages, `index.md`, and `log.md` as you start ingesting content. The skill is idempotent, so re-running "run first-time setup" later is a safe no-op if something didn't finish.

### Manual setup

Prefer to do it by hand, or want to see exactly what the skill automates? Here's the same process step by step.

#### 1. Create the vault

```
<vault-root>/
├── CLAUDE.md                   # project system prompt (see step 3)
├── README.md                   # this file
├── index.md                    # master index (Claude maintains)
├── log.md                      # append-only operation log (Claude maintains)
├── raw/
│   ├── docs/                   # Anapedia clippings, PDFs, articles
│   ├── models/<Model Name>/    # CSV exports per model
│   ├── logs/<Model Name>/      # error/diagnostic logs from imports/actions
│   └── assets/                 # images referenced from sources
├── wiki/
│   ├── concepts/               # Anaplan concepts (line items, dimensions, …)
│   ├── functions/              # categorized function index + category pages
│   ├── models/<Model Name>/    # per-model dossiers (mirrors raw/models/)
│   ├── patterns/               # DISCO, PLANS, Planual, Anaplan Way, naming, …
│   └── sources/                # one summary page per ingested source
└── .claude/
    ├── settings.local.json
    └── skills/
        ├── first-setup/
        │   └── SKILL.md
        ├── anaplan-formula-agent/
        │   ├── SKILL.md
        │   └── references/
        │       └── classic-vs-polaris.md
        ├── anaplan-module-mapping/
        │   └── SKILL.md
        ├── anaplan-model-optimizer/
        │   ├── SKILL.md
        │   └── scripts/
        │       └── analyze_module_usage.py
        ├── anaplan-model-documentation/
        │   └── SKILL.md
        ├── wiki-lint/
        │   └── SKILL.md
        └── wiki-data-ingestion/
            └── SKILL.md
```

Optional: `scraper_ux.py` and `models.py` at the vault root, plus a gitignored `.env` and `UI/` output folder — the toolchain `anaplan-model-optimizer` drives to pull live NUX usage data. See [Scraper toolchain](#scraper-toolchain-optional) below.

Only `CLAUDE.md.example`, all seven `.claude/skills/` folders, `scraper_ux.py`/`models.py`, and `raw/docs/First setup/` (the sample bundle) ship with the repo — the empty top-level directories (`raw/models/`, `raw/logs/`, `raw/assets/`, `wiki/concepts/`, `wiki/functions/`, `wiki/models/`, `wiki/patterns/`, `wiki/sources/`, `analyses/`, `Clippings/`) don't exist yet on a fresh clone, since git doesn't track empty folders. Create them yourself:

```powershell
New-Item -ItemType Directory -Force -Path raw/models, raw/logs, raw/assets, `
  wiki/concepts, wiki/functions, wiki/models, wiki/patterns, wiki/sources, `
  analyses, Clippings | Out-Null
```

Claude will create the wiki pages, `index.md`, and `log.md` as you ingest content — don't pre-create those.

#### 2. Flatten the sample docs

This repo ships its sample corpus nested under `raw/docs/First setup/` rather than directly under `raw/docs/` — that's just how the maintainer shared a curated subset of a larger personal `raw/docs/` folder, not the intended layout. Before your first ingest, un-nest it and drop the wrapper folder:

```powershell
Move-Item "raw/docs/First setup/*" "raw/docs/"
Remove-Item "raw/docs/First setup"
```

If you're keeping this as a git repo of your own, also drop the `First setup`-specific carve-out from `.gitignore` so it matches the standard convention described in `CLAUDE.md.example`:

```diff
 /raw/*
 !/raw/docs
-/raw/docs/*
-!/raw/docs/First setup
```

#### 3. Drop in `CLAUDE.md`

Remove the .example extension from the `CLAUDE.md`and copy it from this repo into your vault root. It defines:

- The vault layout and naming conventions
- The **Ingest / Query / Lint** workflows
- The **incremental re-upload diff protocol** for model CSVs (so re-exports apply as deltas instead of overwriting)
- Anaplan-specific guidance (DISCO categorization, function naming, engine defaults)
- Which models default to which engine (fill in your own model names and engine assignments)

Edit the engine-default block and any team-specific naming conventions to fit your context.

#### 4. Install the project skills

Copy all seven `.claude/skills/` subfolders into your vault:

**`anaplan-formula-agent`** — auto-activates when you ask Claude to write, fix, refactor, or explain a formula; mention a module/line item/list by name; ask about Classic vs Polaris differences; or have model CSVs ingested. Includes a Step-0 context-loading protocol, Planual checklist, and `references/classic-vs-polaris.md`.

**`anaplan-module-mapping`** — auto-activates whenever you wire one module into another: cross-module formulas (`SUM:`, `LOOKUP:`, `SELECT:`, dot-notation), data-flow questions, or "why is this formula written this way?" questions. Always delivers two separate explanations per formula — financial/functional logic first, then Anaplan mechanics — plus a dimension-alignment checklist and sign-convention reference.

**`anaplan-model-optimizer`** — auto-activates on "optimize this model", "which modules can I delete", "unused/orphaned/dead modules", or any mention of the NUX/UX scraper. Runs `scraper_ux.py` for the chosen model, then cross-references the resulting Excel against `raw/models/<Model>/Modules.csv` and `Imports.csv` (via the bundled `scripts/analyze_module_usage.py`) so it never flags Data/Load/Calculation modules that are intentionally invisible in the UX but still feed other modules by formula. Recommendation only — never deletes anything itself; saves the full report under `analyses/`. Needs the optional [scraper toolchain](#scraper-toolchain-optional) set up first.

**`anaplan-model-documentation`** — auto-activates on "document this model", "draft documentation for X", "write up the model", or a request to redraft an existing model doc to match a reference style. Dispatches six parallel background research agents against the model's wiki + raw CSVs (one per outline domain: Introduction, Data Flows, Technical Set-up, Appendices), then assembles a validated `.docx` with `[PLACEHOLDER: ...]` markers for anything the sources don't confirm. Saves to `analyses/<Model>-Model-Documentation.docx`.

**`wiki-lint`** — auto-activates on "lint the wiki", "health check", "check for orphan pages", "wiki cleanup", and similar phrasing. Runs five standard checks: orphan pages, broken internal links, stale counts/stats, contradictions across pages, undocumented companion files. Fixes what's safe automatically (registers orphans in indexes, corrects stale counts, notes undocumented files) and flags anything requiring judgment. Appends a dated entry to `log.md`. Generic — works on any markdown wiki, not specific to Anaplan.

**`wiki-data-ingestion`** — auto-activates whenever you say "ingest", "process this CSV", "I dropped something in raw/", or any variant. Handles the full ingest pipeline: asks for file paths if not provided (or auto-discovers by diffing `raw/` against `wiki/sources/`), groups multiple files into batches by topic, classifies each batch as general doc or model CSV, auto-detects first-time vs incremental delta for CSVs, applies only deltas on re-uploads (preserving your annotations), updates all indexes and `log.md`, and ends with a structured post-ingest summary in chat.

#### 5. Start Claude Code in the vault root

```powershell
cd <vault-root>
claude
```

Claude will read `CLAUDE.md` automatically.

---

## Daily workflow

### Ingest a new source

Drop a file into the right `raw/` subfolder, then tell Claude:

> "Ingest `raw/docs/<new-clipping>.md`."

The `wiki-data-ingestion` skill activates automatically. If you don't provide a path, it will ask; if you'd rather not specify one, it discovers new files by comparing `raw/` against `wiki/sources/`. It then creates a `wiki/sources/YYYY-MM-DD-<slug>.md` summary page, touches every relevant concept/function/pattern page, updates `index.md`, and appends to `log.md`. A structured summary is printed in chat when done.

### Re-upload a model CSV

Drop the new CSV(s) into `raw/models/<Model>/`, then:

> "Ingest the new `<Model>` CSVs."

The `wiki-data-ingestion` skill detects automatically whether this is a first-time ingest or a re-upload by checking `wiki/sources/` and `wiki/models/`. On a re-upload it diffs against the prior version, applies only added/removed/renamed/modified items, saves the new raw file with a date suffix (never overwriting the old one), preserves your annotations, and writes a new dated delta source page.

### Ask model-building questions

> "Write a formula on `<Module Name>.<Line Item>` that …"
> "Why is `<Module Name>.<Line Item>` returning blank?"
> "What changed in `<Model Name>` between this upload and the last?"

Claude reads the master `index.md`, descends into sub-indexes, follows `[[wiki links]]`, and answers with citations to wiki pages and raw sources.

### Health-check the vault

> "Run a vault health check" (or "lint the vault" / "wiki sanity check")

Triggers the **`wiki-lint`** skill, which scans for orphan pages, broken `[[wiki links]]`, stale counts in index files, contradictions across pages, and undocumented companion files. It auto-fixes safe issues and reports anything requiring manual attention.

### Find dead modules in a live model

> "Which modules in `<Model>` are safe to delete?" (or "optimize this model" / "model housekeeping")

Triggers the **`anaplan-model-optimizer`** skill. It runs `scraper_ux.py` against the live tenant to pull fresh NUX usage data for the model, then cross-references it against `raw/models/<Model>/Modules.csv` and `Imports.csv` so Data/Load/Calculation modules that are invisible-by-design in the UX aren't flagged as dead. Reports candidates in chat and saves the full report under `analyses/`. Requires the [scraper toolchain](#scraper-toolchain-optional).

### Generate a Word doc for a model

> "Document the `<Model>` model" (or "write up onboarding material for X")

Triggers the **`anaplan-model-documentation`** skill. Fans out six background research agents over the model's wiki pages and raw CSVs, then assembles a styled `.docx` under `analyses/<Model>-Model-Documentation.docx` with explicit placeholders for anything unconfirmed.

---

## Customizing for your team

- **Different engine defaults?** Edit the *Engine defaults* line near the end of `CLAUDE.md`.
- **Different naming convention?** Ingest your own naming doc into `raw/docs/` and Claude will create a `wiki/patterns/naming-convention-<yourteam>.md` page from it.
- **More models?** Just create `raw/models/<NewModel>/` and `wiki/models/<NewModel>/`. The per-model-subfolder convention means filenames can repeat across models — the directory name disambiguates.
- **More skills?** Add `.claude/skills/<skill-name>/SKILL.md`. Frontmatter `description:` controls when it auto-activates.
- **More models for the scraper?** Add a `<PREFIX>_MODEL_ID` to `.env` and mirror the `fsp` entry in `models.py` — `CUSTOMER_ID` and the workspace ID are shared across every model in the tenant, only `model_id` differs.

---

## Scraper toolchain (optional)

Only needed if you want the **`anaplan-model-optimizer`** skill's dead-module analysis, which relies on live NUX usage data that never appears in a CSV export.

- **`scraper_ux.py`** (vault root) — interactive wizard that logs into Anaplan via Selenium/Edge, lets you pick a model, and exports a 5-sheet Excel report (`All Views`, `Actions Usage Report`, `Views Usage Report`, `Modules Usage Count`, `Actions <model>`). Every default (username, environment, SSO, output folder) is sourced from `.env` — no hardcoded credentials.
- **`models.py`** (vault root) — a `MODELS` dict of quick-select shortcuts so the wizard's "pick from a live list" step can be scripted instead of browsed. An entry only counts as usable once its `customer_id`, `workspace_id`, and `model_id` are all present.
- **`.env`** (gitignored, create it yourself) — `ANAPLAN_USERNAME`, `ANAPLAN_PASSWORD`, `ANAPLAN_ENVIRONMENT`, `ANAPLAN_USE_SSO`, `ANAPLAN_OUTPUT_FOLDER`, the shared `CUSTOMER_ID`/workspace ID, and per-model `<PREFIX>_MODEL_ID` entries.
- **`UI/`** (gitignored) — default output folder for scraped Excel reports and per-run logs. May contain real model data — never commit it.

Install and run:

```powershell
pip install selenium openpyxl webdriver-manager python-dotenv
python scraper_ux.py
```

It opens a real (non-headless) Edge window — the driver is auto-downloaded via Selenium Manager. Every wizard prompt defaults from `.env`; only the model-selection number and the final "scrape another model?" question need real input.

---

## Tips

- **Confirm angle before big ingests.** A two-line "I'll emphasize X, Y, Z — OK?" exchange beats redoing 20 wiki pages.
- **Never edit `raw/`.** It's the source of truth and the diff baseline. Edit `wiki/` instead.
- **Keep page scope tight** — one concept, one function, one module per page. Split at ~400 lines.
- **Update sub-indexes, not the root.** The root `index.md` only changes when a new top-level section appears.
- **Use the log.** `log.md` is the chronological audit trail; Claude appends to it on every ingest. `grep '^## \[' log.md` for a quick history.

---

## Repo layout in this reference vault

What's checked in here as a working example:

- `CLAUDE.md` — the system prompt
- `CLAUDE.md.example` — copy this to `CLAUDE.md` and fill in your vault root path, model names, and engine assignments
- `.claude/skills/first-setup/` — one-time bootstrap skill: builds the empty folder skeleton, flattens the sample docs, adopts `CLAUDE.md` from the example, verifies skills are in place (project skill)
- `.claude/skills/anaplan-formula-agent/` — formula-writing skill (project skill)
- `.claude/skills/anaplan-module-mapping/` — cross-module wiring skill (project skill)
- `.claude/skills/anaplan-model-optimizer/` — dead-module analysis skill, cross-references a scraped NUX report against `Modules.csv`/`Imports.csv` (project skill)
- `.claude/skills/anaplan-model-documentation/` — generates a full Word documentation deliverable for a model via parallel research agents (project skill)
- `.claude/skills/wiki-lint/` — generic wiki sanity-check skill (project skill)
- `.claude/skills/wiki-data-ingestion/` — structured ingest pipeline for docs and model CSVs (project skill)
- `scraper_ux.py`, `models.py` — optional NUX usage-data scraper toolchain that `anaplan-model-optimizer` drives; see [Scraper toolchain](#scraper-toolchain-optional) above
- `raw/docs/First setup/` — sample ingested sources (Anapedia clippings, methodology docs), shipped nested under a wrapper folder for sharing — flatten into `raw/docs/` during setup (step 2 above)
- `wiki/`, `index.md`, `log.md`, and `analyses/` are local-only and not checked in — Claude generates them as you ingest content. Start by copying `CLAUDE.md.example` to `CLAUDE.md`, customizing it, and ingesting your first source.
