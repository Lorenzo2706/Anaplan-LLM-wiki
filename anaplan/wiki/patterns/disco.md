---
title: DISCO — Module Classification
type: pattern
tags: [anaplan, best-practice, architecture]
created: 2026-05-02
updated: 2026-05-02
sources:
  - wiki/sources/2026-05-02-anapedia-line-items-intro.md
---

# DISCO

Anaplan best-practice pattern for organizing modules by purpose. Each module should belong to one of five categories — never mix.

| Letter | Category | Contains |
|---|---|---|
| **D** | Data | Imported / staged data hubs |
| **I** | Inputs | User-entered assumptions and drivers |
| **S** | System | System-wide constants, mappings, time settings |
| **C** | Calculations | Intermediate calculated [[wiki/concepts/anaplan concepts/10_line-item\|line items]] |
| **O** | Outputs | Reporting modules feeding dashboards |

## Why
- Predictable structure → easier handover and review.
- Calculation modules can be optimized independently of input/output ergonomics.
- Reduces accidental dependency tangles.

## Related
- [[wiki/concepts/anaplan concepts/10_line-item]] — purpose classification of line items maps onto DISCO

## Sources
- [[wiki/sources/2026-05-02-anapedia-line-items-intro]]
