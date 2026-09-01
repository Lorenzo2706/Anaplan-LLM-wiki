---
title: Anapedia — Financial Functions Refresh (CUMIPMT, MDURATION)
type: source
tags: [anaplan, functions, financial, clippings, refresh]
created: 2026-08-31
updated: 2026-08-31
sources: [raw/docs/CUMIPMT  Anapedia.md, raw/docs/MDURATION  Anapedia.md]
---

# Anapedia — Financial Functions Refresh (CUMIPMT, MDURATION)

**Raw:** [[raw/docs/CUMIPMT  Anapedia]], [[raw/docs/MDURATION  Anapedia]]

Re-clipped versions of two financial function pages first ingested via the [[wiki/sources/2026-05-02-anapedia-all-functions|2026-05-02 bulk functions ingest]]. The refreshed raw docs replace the originals in place.

## What changed
- **CUMIPMT**: argument table reworded for clarity (e.g. *Loan balance* description tightened); sign-convention note (positive = money received, negative = money paid) and the *Start period*/*End period* < *Number of periods* constraint carried over unchanged.
- **MDURATION**: added explicit validity constraints (settlement/maturity date range 01/01/1900–12/31/2399, maturity must be later than settlement, rate/yield must be non-negative, frequency must be 1/2/4, basis must be 0–4) and a second worked example showing the default-basis case.
- **No syntax or semantic changes** — both functions remain unavailable in Polaris (financial functions generally are). The [[wiki/functions/index|function index]] and [[wiki/functions/categories/financial|Financial category page]] required no edits.

## Wiki pages touched
- None — existing index/category rows already accurate.
