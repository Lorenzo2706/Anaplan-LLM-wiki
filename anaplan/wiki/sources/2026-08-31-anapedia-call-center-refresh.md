---
title: Anapedia — Call Center Functions Refresh (AGENTS, AGENTSB, ERLANGB, ERLANGC)
type: source
tags: [anaplan, functions, call-center, clippings, refresh]
created: 2026-08-31
updated: 2026-08-31
sources: [raw/docs/AGENTS  Anapedia.md, raw/docs/AGENTSB  Anapedia.md, raw/docs/ERLANGB  Anapedia.md, raw/docs/ERLANGC  Anapedia.md]
---

# Anapedia — Call Center Functions Refresh (AGENTS, AGENTSB, ERLANGB, ERLANGC)

**Raw:** [[raw/docs/AGENTS  Anapedia]], [[raw/docs/AGENTSB  Anapedia]], [[raw/docs/ERLANGB  Anapedia]], [[raw/docs/ERLANGC  Anapedia]]

Re-clipped versions of four Erlang/queueing function pages first ingested via the [[wiki/sources/2026-05-02-anapedia-all-functions|2026-05-02 bulk functions ingest]]. Anaplan has since revised the underlying Anapedia help pages; the refreshed raw docs replace the originals in place (this vault's raw docs mirror the current published source, not a dated snapshot).

## What changed
- **AGENTS**: gained an explicit Classic vs. Polaris behavior table for edge cases (`SLA = 0`, `Average duration = 0`), a clarified dimensionless-offered-load explanation, and reworded argument descriptions ("achieve a desired Service Level" replacing "fulfil requests within a target time").
- **AGENTSB**: minor wording refinements; argument descriptions and example table unchanged in substance.
- **ERLANGB / ERLANGC**: both gained explicit Classic vs. Polaris rounding-behavior tables (integer rounding of *Number of servers*, and return values when *Arrival rate*/*Average duration* are 0) and the underlying Erlang formula definitions (LaTeX).
- **No syntax or semantic changes** to any of the four functions — existing formulas built with them remain valid. The [[wiki/functions/index|function index]] and [[wiki/functions/categories/call-center|Call Center category page]] syntax rows and pick-your-unknown table required no edits.

## Behavior notes worth flagging in future formula work
- Classic **truncates** the agent count toward 0; Polaris **rounds to nearest**, halves away from 0 — a source of small discrepancies when comparing the same formula across engines.
- When `Arrival rate = 0`: Classic returns `NaN` if `Number of servers` is negative, `0` otherwise; Polaris always returns `0`.
- When `Average duration = 0`: Classic always returns `NaN`; Polaris always returns `0`.

## Wiki pages touched
- No new pages — existing [[wiki/functions/index|Functions index]] and [[wiki/functions/categories/call-center|Call Center category]] already had accurate syntax rows; content addition lives in the raw docs themselves for future deep-dive reference.
