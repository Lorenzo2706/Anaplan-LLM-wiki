---
title: Anapedia — VARP / VARS Aggregation Functions
type: source
tags: [anaplan, functions, aggregation, clippings]
created: 2026-08-31
updated: 2026-08-31
sources: [raw/docs/VARP aggregation function.md, raw/docs/VARS aggregation function.md]
---

# Anapedia — VARP / VARS Aggregation Functions

**Raw:** [[raw/docs/VARP aggregation function]], [[raw/docs/VARS aggregation function]]

First-time ingest of two aggregation functions not covered by the [[wiki/sources/2026-05-02-anapedia-all-functions|2026-05-02 bulk functions ingest]] (that ingest's "145 functions" count predates these).

## Summary
- **VARP** — `Source[VARP: Mapping, ...]` — returns the **population variance** of a line item, aggregated per the mapping(s) given. Polaris-only.
- **VARS** — `Source[VARS: Mapping, ...]` — returns the **unbiased sample variance** of a line item, aggregated per the mapping(s) given. Polaris-only.

Both:
- Return `NaN` if the source set includes a `NaN`.
- Return `0` for a single value or for unmapped points.
- Can't be combined with another number-typed aggregation function, used with the **Formula** summary method, or used in version formulas.
- Have a square-root counterpart: `√VARP = STDEVP`, `√VARS = STDEVS` (those two functions are not yet ingested into this vault).

## Wiki pages touched
- [[wiki/functions/index|Functions index]] — added VARP and VARS rows under **Aggregation functions**.
- [[wiki/functions/categories/aggregation|Aggregation category page]] — added VARP, VARS to the Members list and a "when to use" row (variance/spread of a rolled-up value).
