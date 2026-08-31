---
title: "Planual Chapter 5 — Integration"
type: pattern
tags: [anaplan, planual, integration, imports, exports, actions, processes, data-hub]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Support 15.md
  - raw/docs/Anaplan Support 16.md
  - raw/docs/Source models  Anaplan Support.md
  - raw/docs/Anaplan Support 17.md
  - raw/docs/Anaplan Support 18.md
  - raw/docs/Import data sources  Anaplan Support.md
  - raw/docs/Data Hub  Anaplan Support.md
---

# Chapter 5 — Integration

> Imports, exports, and the Data Hub pattern. How data enters and leaves Anaplan, and where the master copies live.

Sub-sections: [Actions](#actions) · [Processes](#processes) · [Source models](#source-models) · [Imports](#imports) · [Exports](#exports) · [Import data sources](#import-data-sources) · [Data Hub](#data-hub)

---

## Actions

- **Numeric prefixes for ordering** — `1.1 Import Products`, `1.2 Import Product details`. **Don't include the technical module name** in the description.
- **Imports/Exports vs Process actions** — Import/Export actions must be **republished** when modified or replaced; Process actions stay consistent with whatever they contain. Prefer Processes for manageability.
  - **`5.01-02a`** Numbered-list actions (Create, Assign, Copy branch, Delete branch) **cannot** be placed in a Process.
- **Critically review user-driven actions** — they impact concurrency. Prefer formulas where possible (extra modules may be needed, but UX often improves).
- **Delete one-off imports** (and their data sources) after use to keep the model clean.

## Processes

- **Friendly names for user-facing processes**; numeric prefixes for data-hub or admin processes (`5.01-01 Naming convention`).
- **Each action triggers a recalc** — minimize the number of actions in a process.

## Source models

- **Delete unused source models** — keep the source-model list tidy when a one-off import is done or the source is no longer needed.
- **Remap actions to the correct source** — when multiple Dev copies have been created, remapping back to the canonical Dev model cleans up Production *and* makes future source changes easier.

## Imports

### File preparation

- **Separate file for unique members** — don't reuse the transactional file for list loads. A unique-members file is much smaller.
  - **`5.04-01a`** Codes >60 characters → fall back to combination of properties.
- **Data files**: key + values per dimension. **Non-dimensional data goes in a different file.**
- **Key columns**: only what makes the row unique. **No data fields, no dates** in the key.
- **Use the Ignore field** for unwanted source columns — better performance, cleaner warnings log.
- **Aggregate at source** when possible — faster import, smaller engine footprint, smaller files.
- **Right granularity only** — no weekly transactional data when planning runs at month grain.

### Format and source

- **Use correct line-item formats** for imported data: List-formatted, Number, Date — **not Text** unless it really is text.
- **Import from a module view or a file**, never directly from a list (lists can't be filtered → always full-list).
- **Saved views for model-to-model imports** — only the data that changed flows through; modules/lists can't filter.
- **Generic date format `YYYYMMDD`** simplifies imports and avoids date-mismatch manipulation.

## Exports

- **Naming**: keep it simple — `Export`, `Load`, `Build`. **No module name in the view name.**
- **Only export needed line items.** Create multiple views if the same module feeds different imports — a process can't reference the same view twice.
- **Column count matters** — fewer columns = faster export *and* faster downstream import.
- **Two views in the source SYS module**:
  1. List load (name, code, parent)
  2. Member attributes
- **One filter criterion only.** Combine multiple conditions into a single line item.

## Import data sources

- **Rename import sources immediately**:
  - For saved views: `module.saved view`.
  - For model imports: `model_module.saved view` (use a shortened model name).
- **Delete one-off / unused sources** (`5.03-01 Remove unwanted sources`).

## Data Hub

The Data Hub is a separate model that holds master data and feeds spoke planning models.

### Structure

- **No composite hierarchies in the Hub.** Build them only to test actions, then delete.
  - **`5.07-01a`** Validation: OK if data needs consolidation against source systems (flat modules with attributes also work).
  - **`5.07-01b`** Combining source systems: OK if the Hub merges multiple sources into one feed downstream.
- **No Analytical modules** (multi-list `Applies To`) in the Hub — keep them in spoke models.
- **Use flat list structures** to build modules and views for downstream targets.
- **No master data created in the Hub** — master data should come from source systems.

### Data shape

- **Get data from IT in the right format and granularity** — push transformations upstream where possible.
- **System modules for filtering** (current period, current FY, etc.).
- **Detailed transactional data goes in a separate reporting model** (e.g. `FIN Trans Data`), not in the planning models. Large transactional histories inflate planning-model size and slow performance.
- **Aggregate in the Hub, then export** — more efficient than accumulating via repeated imports to spokes.

### Transaction lists

- **No top level on a transaction list** — totals would sum across the entire list even when only one item is added.
- **For all-transaction sums**: use a "dummy" list and sum within a module dimensioned by the dummy list.
- **Validation totals**: create intermediate sub-totals within the transaction list — significantly reduces calc load.

### Hub deployment

- **Hub in its own workspace** — lets it grow without disrupting integrations. Also enables segregation of duties (data managers separate from production-model users).
- **Export Hub model**: if you need to consolidate exports from multiple models into one feed, create an Export Hub to keep the Data Hub clean.

---

## See also

- [[wiki/patterns/planual/01-central-library|Chapter 1 § Lists]] — `1.05-12 Avoid hierarchies in Data Hub` lives there too
- [[wiki/patterns/planual/06-alm|Chapter 6 — ALM]] — Source models / Dev cleanup interact with ALM
- [[wiki/patterns/planual/08-data-orchestrator|Chapter 8 — ADO]] — modern alternative source-data path
