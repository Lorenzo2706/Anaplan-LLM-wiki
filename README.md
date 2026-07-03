# Anaplan LLM Wiki

A **Claude Code-powered knowledge vault** for Anaplan model builders. Drop in Anapedia docs, articles, and model CSV exports; Claude ingests them into a structured, interlinked Obsidian-style wiki that becomes durable context for future model-building work (formulas, debugging, design reviews, deltas across re-uploads).

The wiki is the agent's **external memory** — not the product. The point is that every subsequent question Claude answers ("write me a formula for X", "what changed in this re-upload", "is this Polaris-safe?") is grounded in your actual model context, accumulated over time.

---

## What you get

- **Claude Code as an Anaplan model-builder agent** with a project-specific system prompt (`CLAUDE.md`) that defines a vault schema, ingest/query/lint workflows, and Anaplan-aware conventions (DISCO, PLANS, engine-aware reasoning).
- **A vault layout** that separates immutable sources (`raw/`) from generated, queryable wiki pages (`wiki/`).
- **Five skills** that auto-activate from context: `first-setup` (one-time bootstrap of a freshly cloned vault — flattens the sample docs, adopts `CLAUDE.md`, verifies skills are in place), `anaplan-formula-agent` (formula writing/debugging, Step-0 context-loading + Classic-vs-Polaris reasoning), `anaplan-module-mapping` (cross-module wiring — delivers dual financial-logic + Anaplan-mechanics explanations for every formula), `wiki-lint` (generic wiki sanity-check — orphans, broken links, stale stats, contradictions, auto-fix pass), and `wiki-data-ingestion` (structured ingest of docs and model CSVs — path acquisition, grouping, delta detection, index/log updates, post-ingest summary).
- **Obsidian compatibility** — open the vault in Obsidian to browse `[[wiki links]]` visually while Claude maintains it.

---

## Prerequisites

- [Claude Code](https://docs.claude.com/en/docs/claude-code) installed (CLI or IDE extension).
- A local folder you'll use as the vault root (this becomes Claude Code's working directory).
- [Obsidian](https://obsidian.md/) pointed at the same folder for browsing the wiki.

No databases, no servers, no API keys beyond what Claude Code itself needs. Everything is flat markdown + CSVs on disk.

---

## Setup

### 1. Create the vault

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
        ├── anaplan-formula-agent/
        │   ├── SKILL.md
        │   └── references/
        │       └── classic-vs-polaris.md
        └── anaplan-module-mapping/
            └── SKILL.md
# wiki-lint and wiki-data-ingestion are Cowork plugin skills — install via the skill store, not here
```

Only `CLAUDE.md`, both `.claude/skills/` folders, and the empty top-level directories are needed to start — Claude will create the wiki pages, `index.md`, and `log.md` as you ingest content.

> [!tip] Steps 2–3 below (flattening the sample docs and adopting `CLAUDE.md`) are automated by the `first-setup` skill, which ships in `.claude/skills/`. Once you've cloned the repo, just start Claude Code in the vault root and say **"run first-time setup"** — it'll do both steps, ask you for model names/engines to fill into `CLAUDE.md`, and report what's left to do manually (like installing the Cowork plugin skills). The steps below are the manual walkthrough if you'd rather do it by hand.

### 2. Flatten the sample docs

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

### 3. Drop in `CLAUDE.md`

Remove the .example extension from the `CLAUDE.md`and copy it from this repo into your vault root. It defines:

- The vault layout and naming conventions
- The **Ingest / Query / Lint** workflows
- The **incremental re-upload diff protocol** for model CSVs (so re-exports apply as deltas instead of overwriting)
- Anaplan-specific guidance (DISCO categorization, function naming, engine defaults)
- Which models default to which engine (fill in your own model names and engine assignments)

Edit the engine-default block and any team-specific naming conventions to fit your context.

### 4. Install the project skills

Copy both `.claude/skills/` subfolders into your vault:

**`anaplan-formula-agent`** — auto-activates when you ask Claude to write, fix, refactor, or explain a formula; mention a module/line item/list by name; ask about Classic vs Polaris differences; or have model CSVs ingested. Includes a Step-0 context-loading protocol, Planual checklist, and `references/classic-vs-polaris.md`.

**`anaplan-module-mapping`** — auto-activates whenever you wire one module into another: cross-module formulas (`SUM:`, `LOOKUP:`, `SELECT:`, dot-notation), data-flow questions, or "why is this formula written this way?" questions. Always delivers two separate explanations per formula — financial/functional logic first, then Anaplan mechanics — plus a dimension-alignment checklist and sign-convention reference.

**`wiki-lint`** (Cowork plugin skill — install separately via the Cowork skill store) — auto-activates on "lint the wiki", "health check", "check for orphan pages", "wiki cleanup", and similar phrasing. Runs five standard checks: orphan pages, broken internal links, stale counts/stats, contradictions across pages, undocumented companion files. Fixes what's safe automatically (registers orphans in indexes, corrects stale counts, notes undocumented files) and flags anything requiring judgment. Appends a dated entry to `log.md`. Generic — works on any markdown wiki, not specific to Anaplan.

**`wiki-data-ingestion`** (Cowork plugin skill — install separately via the Cowork skill store) — auto-activates whenever you say "ingest", "process this CSV", "I dropped something in raw/", or any variant. Handles the full ingest pipeline: asks for file paths if not provided (or auto-discovers by diffing `raw/` against `wiki/sources/`), groups multiple files into batches by topic, classifies each batch as general doc or model CSV, auto-detects first-time vs incremental delta for CSVs, applies only deltas on re-uploads (preserving your annotations), updates all indexes and `log.md`, and ends with a structured post-ingest summary in chat.

### 5. Start Claude Code in the vault root

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

Triggers the **`wiki-lint`** skill, which scans for orphan pages, broken `[[wiki links]]`, stale counts in index files, contradictions across pages, and undocumented companion files. It auto-fixes safe issues and reports anything requiring manual attention. Requires the `wiki-lint` Cowork plugin skill to be installed.

---

## Customizing for your team

- **Different engine defaults?** Edit the *Engine defaults* line near the end of `CLAUDE.md`.
- **Different naming convention?** Ingest your own naming doc into `raw/docs/` and Claude will create a `wiki/patterns/naming-convention-<yourteam>.md` page from it.
- **More models?** Just create `raw/models/<NewModel>/` and `wiki/models/<NewModel>/`. The per-model-subfolder convention means filenames can repeat across models — the directory name disambiguates.
- **More skills?** Add `.claude/skills/<skill-name>/SKILL.md`. Frontmatter `description:` controls when it auto-activates.

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
- `.claude/skills/first-setup/` — one-time bootstrap skill: flattens the sample docs, adopts `CLAUDE.md` from the example, verifies skills are in place (project skill)
- `.claude/skills/anaplan-formula-agent/` — formula-writing skill (project skill)
- `.claude/skills/anaplan-module-mapping/` — cross-module wiring skill (project skill)
- `wiki-lint` — generic wiki sanity-check skill (Cowork plugin skill, install via skill store)
- `wiki-data-ingestion` — structured ingest pipeline for docs and model CSVs (Cowork plugin skill, install via skill store)
- `raw/docs/First setup/` — sample ingested sources (Anapedia clippings, methodology docs), shipped nested under a wrapper folder for sharing — flatten into `raw/docs/` during setup (step 2 above)
- `wiki/`, `index.md`, `log.md`, and `analyses/` are local-only and not checked in — Claude generates them as you ingest content. Start by copying `CLAUDE.md.example` to `CLAUDE.md`, customizing it, and ingesting your first source.
