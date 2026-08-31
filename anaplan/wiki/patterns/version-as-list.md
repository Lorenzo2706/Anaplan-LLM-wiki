---
title: Pattern — Version-as-list (custom-list scenarios)
type: pattern
tags: [anaplan, pattern, versions, scenarios]
created: 2026-05-05
updated: 2026-05-05
sources: []
---

# Version-as-list

A common Anaplan pattern: model scenarios/forecast cycles as items in a **custom list** instead of using the native Versions list. Adds metadata, parenting, properties, and tighter memory control at the cost of native breakback / switchover / `PREVIOUSVERSION()`.

This pattern has been used in production models with chained version dependencies across model layers, including a fully wired example with a dedicated version-control metadata module and per-grain period flags. A minimal variant has also been seen: a 1-item versions list backed by a system version module, with no scenarios populated yet but the wiring in place to add them.

## When to use

✅ Use version-as-list when you need:
- Properties on a version (start/end year, source version, owner, export flag)
- Hierarchy or chaining between versions ("this FSP is based on that MJP")
- Many scenarios with controlled memory (subset Applies To)
- Variance/roll-forward via formulas (`LOOKUP` to "Previous Version")

❌ Stick with native Versions when:
- Built-in **breakback** matters
- Built-in **switchover (actuals → plan)** is desired
- Users expect the standard version selector UX
- You only have 2-3 versions and no metadata

## Skeleton

1. List `<X> versions` — numbered, production data, Display Name property.
2. System module `<X> Version Control` (Applies To: `<X> versions`) — line items: `Name`, `Previous Version` (list-formatted, self-reference), `Source Version` (list to upstream version), `Start Year`, `End Year`, `Export?`, `Delete?`.
3. Time-grain settings module `<X> Version Settings per Year/Month` (Applies To: `<X> versions × Year/Month`) — booleans: `In Period?`, `Start Year?`, `Horizons (+5, +15)`.
4. Calc modules add `<X> versions` to Applies To and use `LOOKUP` against the control modules instead of `CURRENTVERSION/PREVIOUSVERSION`.

## See also
- [[wiki/patterns/planual/01-central-library|Planual Ch.1 — Versions]]
- [[wiki/functions/categories/misc|Misc functions — CURRENTVERSION/PREVIOUSVERSION]]
