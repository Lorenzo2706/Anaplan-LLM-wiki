---
title: Anapedia — All Functions (Master Index)
type: source
tags: [anaplan, functions, reference]
created: 2026-05-02
updated: 2026-05-02
raw: raw/docs/All functions.md
---

# Anapedia — All Functions (Master Index)

**Raw:** [[raw/docs/All functions]]
**Source URL:** https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3

## Summary
The complete Anapedia catalog of Anaplan formula functions — 145 functions in total, grouped into 10 categories. Each entry in the source includes syntax and a one-sentence description. Individual function pages were also clipped (one per function under `raw/docs/`), so the raw layer holds full reference content; the wiki adds categorization, comparison, and synthesis.

## Categories observed (with counts)
| Category | Count |
|---|---|
| Aggregation functions | 9 |
| Call center planning functions | 8 |
| Financial functions | 17 |
| Logical functions | 7 |
| Mapping functions | 2 |
| Miscellaneous functions | 11 |
| Numeric functions | 14 |
| Text functions | 11 |
| Time and date functions | 36 |
| Trigonometry and maths functions | 14 |

## Wiki pages produced
- [[wiki/functions/index|Functions — Master Index]]
- 10 category overview pages under [[wiki/functions/categories/index|wiki/functions/categories]]

## Key insights to mine later
- Aggregation, Mapping, and Time functions are the workhorses for typical planning models.
- Call-center planning and Financial groups are domain-specific (Erlang formulas, bond math).
- The single most repeated warning in source clippings: **never combine SUM and LOOKUP in the same formula** ([[wiki/functions/categories/mapping#performance-warning|see Mapping]]).
- Several functions have **Polaris vs Classic** behavior differences — flag these when they appear in user formulas.
