# Anaplan LLM Wiki

A **Claude Code-powered knowledge vault** for Anaplan model builders. Drop in Anapedia docs, articles, and model CSV exports; Claude ingests them into a structured, interlinked Obsidian-style wiki that becomes durable context for future model-building work (formulas, debugging, design reviews, deltas across re-uploads).

The wiki is the agent's **external memory** — not the product. The point is that every subsequent question Claude answers ("write me a formula for X", "what changed in this re-upload", "is this Polaris-safe?") is grounded in your actual model context, accumulated over time.

---

## What you get

- **Claude Code as an Anaplan model-builder agent** with a project-specific system prompt (`CLAUDE.md`) that defines a vault schema, ingest/query/lint workflows, and Anaplan-aware conventions (DISCO, PLANS, engine-aware reasoning).
- **A vault layout** that separates immutable sources (`raw/`) from generated, queryable wiki pages (`wiki/`).
- **Two project skills** that auto-activate from context: `anaplan-formula-agent` (formula writing/debugging, Step-0 context-loading + Classic-vs-Polaris reasoning) and `anaplan-module-mapping` (cross-module wiring — delivers dual financial-logic + Anaplan-mechanics explanations for every formula).
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
├── CLAUDE.md                   # project system prompt (see step 2)
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
```

Only `CLAUDE.md`, both `.claude/skills/` folders, and the empty top-level directories are needed to start — Claude will create the wiki pages, `index.md`, and `log.md` as you ingest content.

### 2. Drop in `CLAUDE.md`

Remove the .example extension from the `CLAUDE.md`and copy it from this repo into your vault root. It defines:

- The vault layout and naming conventions
- The **Ingest / Query / Lint** workflows
- The **incremental re-upload diff protocol** for model CSVs (so re-exports apply as deltas instead of overwriting)
- Anaplan-specific guidance (DISCO categorization, function naming, engine defaults)
- Which models default to which engine (fill in your own model names and engine assignments)

Edit the engine-default block and any team-specific naming conventions to fit your context.

### 3. Install the project skills

Copy both `.claude/skills/` subfolders into your vault:

**`anaplan-formula-agent`** — auto-activates when you ask Claude to write, fix, refactor, or explain a formula; mention a module/line item/list by name; ask about Classic vs Polaris differences; or have model CSVs ingested. Includes a Step-0 context-loading protocol, Planual checklist, and `references/classic-vs-polaris.md`.

**`anaplan-module-mapping`** — auto-activates whenever you wire one module into another: cross-module formulas (`SUM:`, `LOOKUP:`, `SELECT:`, dot-notation), data-flow questions, or "why is this formula written this way?" questions. Always delivers two separate explanations per formula — financial/functional logic first, then Anaplan mechanics — plus a dimension-alignment checklist and sign-convention reference.

### 4. Start Claude Code in the vault root

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

Claude will summarize the source, confirm the angle of emphasis, create a `wiki/sources/YYYY-MM-DD-<slug>.md` summary page, touch every relevant concept/function/pattern page, update `index.md`, and append to `log.md`.

### Re-upload a model CSV

Drop the new CSV into `raw/models/<Model>/` (overwrite the existing file — prior versions are not kept), then:

> "Ingest the new `<Model>` CSVs as a delta."

Claude diffs against the previous version, applies only added/removed/renamed/modified items to the wiki, preserves your annotations, and writes a new dated source page summarizing **what changed**.

### Ask model-building questions

> "Write a formula on `<Module Name>.<Line Item>` that …"
> "Why is `<Module Name>.<Line Item>` returning blank?"
> "What changed in `<Model Name>` between this upload and the last?"

Claude reads the master `index.md`, descends into sub-indexes, follows `[[wiki links]]`, and answers with citations to wiki pages and raw sources.

### Health-check the vault

> "Run a vault health check" (or "lint the vault")

Claude scans for broken `[[wiki links]]`, orphan pages, index drift, stale paths, frontmatter issues, and missing cross-references, and reports a prioritized list of fixes.

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
- `.claude/skills/anaplan-formula-agent/` — formula-writing skill
- `.claude/skills/anaplan-module-mapping/` — cross-module wiring skill
- `CLAUDE.md.example` — copy this to `CLAUDE.md` and fill in your vault root path, model names, and engine assignments
- `.claude/skills/anaplan-formula-agent/` — formula-writing skill
- `.claude/skills/anaplan-module-mapping/` — cross-module wiring skill
- `raw/docs/` — sample ingested sources (Anapedia clippings, methodology docs)
- `wiki/`, `index.md`, `log.md`, and `analyses/` are local-only and not checked in — Claude generates them as you ingest content. Start by copying `CLAUDE.md.example` to `CLAUDE.md`, customizing it, and ingesting your first source.
