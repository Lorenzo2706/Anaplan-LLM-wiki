---
name: wiki-data-ingestion
description: >
  Ingest one or more new sources into the Anaplan LLM wiki — including raw docs, articles,
  PDFs, web clippings, and model CSV exports. Trigger whenever the user mentions ingesting a
  file, dropping something into raw/, adding a new source to the wiki, or updating the wiki
  with new content. Also trigger when the user says things like "I added a new doc", "process
  this CSV", "update the wiki with this file", "I dropped something in raw/", or any variant
  of "ingest". Handles both general sources and model CSV re-uploads (with automatic delta
  detection). Always use this skill instead of doing ad-hoc ingest work — it ensures indexes,
  log, and cross-references are consistently updated.
---

# Wiki Data Ingestion

This skill drives a consistent, structured ingest of new sources into the wiki. It handles
two source families — general docs (articles, PDFs, web clippings) and model CSVs — and
branches automatically based on what it finds. The goal is to make every ingest predictable:
you always know what got created, what got updated, and what the wiki state is afterward.

---

## Phase 0 — Acquire file paths

Before any reading or writing, you need to know exactly which files to ingest.

### If the user already provided file path(s)

Trust the input completely. Do not scan `raw/` or look for other new files. Proceed directly
to Phase 1 with the provided paths.

### If no paths were provided

**Stop immediately** and ask:

> "Which file(s) should I ingest? You can paste the path(s) or drag them in. If you'd prefer
> I discover them automatically, just say so."

- If the user provides path(s) → proceed to Phase 1 with those paths only.
- If the user explicitly declines to provide paths ("discover them", "check yourself", etc.):
  1. Read `wiki/sources/` index to build a set of already-ingested source slugs/filenames.
  2. Scan `raw/docs/`, `raw/models/`, and `raw/logs/` for files whose basenames do NOT
     appear in any existing `wiki/sources/` page (match on filename stem, case-insensitive).
  3. Present the candidate list to the user:
     > "I found these files that don't appear to be ingested yet: [list]. Should I proceed
     > with all of them, or only some?"
  4. Wait for confirmation before proceeding.

---

## Phase 1 — Grouping (multiple files only)

When more than one file is in scope, ask before diving in:

> "Are these files related to the same topic, or are they independent sources?"

Use the answer to build **batches** — groups that will be processed together in a single
ingest pass. Rules:
- Related files → one batch (they share a source page and cross-reference each other).
- Unrelated files → separate batches processed sequentially.
- Mixed answer (e.g., "A and B are related, C is separate") → two batches: {A, B} then {C}.

If there is only one file, skip this phase.

---

## Phase 2 — Classify each batch

For each batch, classify the source type and (for CSVs) determine first-time vs re-upload.

### Classification rules

**Model CSV batch** — all files match the pattern of Anaplan model exports: filenames like
`Modules.csv`, `Line Items.csv`, `General Lists.csv`, `Actions.csv`, `Model Calendar.csv`,
or any file inside a `raw/models/<Model>/` subfolder.

**General source batch** — anything else: articles, PDFs, web clippings, plain text docs,
diagnostic logs under `raw/logs/`.

### Delta detection for model CSVs

Check `wiki/sources/` for any prior ingest of the same model (match on model name in the
source page title or frontmatter slug). Also check `wiki/models/<Model>/` for existing pages.

- If prior pages exist → **incremental delta** mode (see Phase 3C).
- If no prior pages exist → **first-time ingest** mode (see Phase 3B).

When unsure (e.g., model name is ambiguous), ask the user: "Is this a re-upload of an
existing model, or a first-time ingest?"

---

## Phase 3A — Ingest: general source

For each batch of general sources:

1. **Read the source(s).** For CSVs outside the model export pattern, read structure first
   (headers, sample rows) before reading all content. For PDFs and long docs, read in
   sections.

2. **Create `wiki/sources/YYYY-MM-DD-<slug>.md`** with YAML frontmatter:
   ```yaml
   ---
   title: <Descriptive title>
   type: source
   tags: [anaplan, ...]
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   sources: [raw/docs/<filename>]
   ---
   ```
   Include: a summary of the source, key takeaways, and links to every wiki page created
   or updated as a result of this ingest.

3. **Touch relevant wiki pages:**
   - Create new pages for concepts, functions, or patterns introduced by the source (follow
     the function pages policy: only create individual function pages when the function is
     non-obvious, is used in a model being built, or the user asks).
   - Update existing pages with new facts, corrections, or examples. Preserve any
     user-added commentary.
   - Add cross-references both directions (new page → source, source → new page).

4. **Update indexes:**
   - Update the sub-index for every section touched (`wiki/concepts/index.md`,
     `wiki/functions/index.md`, `wiki/patterns/index.md`, `wiki/sources/index.md`).
   - Update the master `index.md` only if a new top-level section or sub-index was created.

5. **Append to `log.md`:**
   ```markdown
   ## [YYYY-MM-DD] ingest | <source title>
   Created: [list of new pages]
   Updated: [list of updated pages]
   ```

---

## Phase 3B — Ingest: model CSV (first-time)

1. **Sample the CSV structure** — read headers and a few rows to infer schema before
   loading the full file. Understand what each CSV covers (modules, line items, lists,
   dimensions, formulas, etc.).

2. **Seed `wiki/models/<Model Name>/`** — create structured pages for each entity type
   present in the exports:
   - One overview page listing all modules with their DISCO category (Data, Input, System,
     Calculation, Output) if inferable.
   - Subpages or sections per module, capturing: name, dimensions, line items, formulas
     (verbatim), and any flags (summary method, format).
   - Note the model's engine (Classic or Polaris) if determinable from context; otherwise
     flag as unknown.

3. **Create `wiki/sources/YYYY-MM-DD-<model>-initial.md`** summarizing the export scope
   (N modules, N line items, N lists, etc.) and linking to the model overview page.

4. **Update indexes** — `wiki/models/index.md`, `wiki/sources/index.md`, master `index.md`.

5. **Append to `log.md`:**
   ```markdown
   ## [YYYY-MM-DD] ingest | <Model Name> — initial CSV export
   Seeded wiki/models/<Model Name>/. Pages: [list]. Modules: N, Line items: N.
   ```

---

## Phase 3C — Ingest: model CSV (incremental delta)

The export is mostly the same as a prior version (~80% unchanged). Don't re-ingest from
scratch — apply only what changed.

1. **Diff against prior state** — compare the new CSV(s) against:
   - The prior raw CSV in `raw/models/<Model>/` (look for the most recent versioned file).
   - If no prior raw CSV is available, diff against the wiki model pages as a proxy.

   Identify: **added**, **removed**, **renamed**, and **modified** items (modules, line items,
   formulas, dimensions, lists).

2. **Save the new raw file with a date suffix** so prior versions remain for future diffs:
   `<original-name>__YYYY-MM-DD.csv`. Never overwrite an existing raw file.

3. **Apply only the deltas to the wiki:**
   - Added items → create new pages or add sections.
   - Modified items → update the relevant page/section with the new value; note the change
     inline if significant.
   - Removed items → do not silently delete. Add a note: `> [!note] Removed YYYY-MM-DD —
     this item no longer appears in the export.` This guards against accidental deletions.
   - Renamed items → update the page title and all inbound `[[links]]`; add an alias note.
   - Preserve all user-added commentary and cross-references on existing pages.

4. **Create a new `wiki/sources/YYYY-MM-DD-<model>-delta.md`** summarizing what changed
   since the previous version. Link back to the prior source page. Do NOT overwrite the
   prior source page.

5. **Update indexes** as needed.

6. **Append to `log.md`:**
   ```markdown
   ## [YYYY-MM-DD] ingest-delta | <Model Name>
   +N modules, +N line items, N formula changes, N renames, N removals.
   Source: wiki/sources/YYYY-MM-DD-<model>-delta.md
   ```

---

## Phase 4 — Post-ingest summary

After every ingest (regardless of type), end with a structured summary in chat. This is
**always required** — do not skip it even for small ingests.

```
## Ingest complete — <source title or model name>

**Mode:** [General source | First-time model CSV | Incremental delta]
**Batch:** [file(s) processed]

**Created:**
- wiki/sources/... (source page)
- wiki/concepts/... (if any)
- wiki/models/... (if any)

**Updated:**
- wiki/.../... — [what changed]
- index.md — [what was added]
- log.md — appended

**Delta summary** (model CSVs only):
- Added: N modules, N line items
- Modified: N formulas
- Removed: N items (flagged, not deleted)
- Renamed: N items

**Notes / flags for review:**
- [Anything ambiguous, contradictory, or requiring manual judgment]
```

If nothing was flagged, say so explicitly: "No issues flagged — wiki is consistent."

---

## Constraints and guardrails

- **Never modify files under `raw/`** — they are immutable source documents.
- **Always include a `sources:` frontmatter field** in every wiki page pointing back to the
  originating raw file.
- **Never overwrite a prior raw CSV** — always append a date suffix to the new one.
- **One source page per ingest event**, not per file. If a batch of 3 related CSVs is
  ingested together, one source page covers all three.
- **Prefer updating an existing wiki page over creating a near-duplicate.** Search
  `wiki/` before creating a new page.
- **Use Obsidian-compatible syntax** throughout: `[[wiki links]]`, YAML frontmatter,
  callouts (`> [!note]`), relative paths.
