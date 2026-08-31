---
title: Anapedia — Missing Files Ingest (LIS, Modules, Actions, Contents)
type: source
tags: [anaplan, anapedia, line-item-subsets, modules, actions, contents]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Line item subsets.md
  - raw/docs/Create a line item subset.md
  - raw/docs/Line item subset example.md
  - raw/docs/Example Create line item subset LIS Multi-variance reporting.md
  - raw/docs/Configure modules.md
  - raw/docs/Model actions.md
  - raw/docs/Select content to display in the Contents panel.md
  - raw/docs/Set new content to automatically show in Contents.md
  - raw/docs/Show hidden content in model Contents.md
  - raw/docs/TEXTLIST (Text function).md
---

# Anapedia — Missing Files Ingest (LIS, Modules, Actions, Contents)

Ingest of 10 raw docs that existed in `raw/docs/` but had never been indexed or processed into wiki pages. Discovered during a file audit on 2026-05-13.

## Files ingested

### Line Item Subsets (4 files)
`Line item subsets.md`, `Create a line item subset.md`, `Line item subset example.md`, `Example Create line item subset LIS Multi-variance reporting.md`

### Module configuration (1 file)
`Configure modules.md`

### Actions (1 file)
`Model actions.md`

### Contents panel (3 files)
`Select content to display in the Contents panel.md`, `Set new content to automatically show in Contents.md`, `Show hidden content in model Contents.md`

### Function (1 file)
`TEXTLIST (Text function).md`

## Files skipped

| File | Reason |
|---|---|
| `_index.md` | Internal supply chain app TOC, not a raw doc |
| `Add a top-level item to the Users list 1.md` | Duplicate of already-ingested `Add a top-level item to the Users list.md` |
| `Create links from data in a module.md` | MAKELINK already covered in `functions/categories/text.md` |
| `Manage images in a central module.md` | Minor UX tip, no new concept |
| `Example Create a page called Variance report.md` | UX/dashboard how-to, covered by existing `patterns/variance-reporting.md` |
| `Saved Views  Anaplan Support.md` | Planual best-practice notes, no new concept |
| `17-05 Inventory reporting-auto expiry.md` | Already ingested — `17-inventory-reporting.md` had complete 17-05 content |

## Wiki pages created/updated

### New concept pages (4)
- `wiki/concepts/line-item-subsets.md` — LIS mechanics, COLLECT() pattern, variance reporting example, constraints, gotchas
- `wiki/concepts/modules.md` — module configuration columns, cell count, breakback, DISCO mapping
- `wiki/concepts/actions.md` — action types, process vs. direct run, admin vs. user execution
- `wiki/concepts/contents-panel.md` — per-role visibility, Show New Content, Show Hidden Content

### Updated function category page (1)
- `wiki/functions/categories/text.md` — added TEXTLIST (Text function) Classic-only warning
