---
title: Mapping Functions
type: function-category
tags: [anaplan, functions, mapping, performance]
created: 2026-05-02
updated: 2026-05-02
---

# Mapping Functions

Pull individual values from a source module into a target module by following mapping line items. Where [[wiki/functions/categories/aggregation|Aggregation]] rolls many → one, Mapping retrieves one → one (or one per target cell).

## Members
**LOOKUP, SELECT**

## When to use which
| Need | Function |
|---|---|
| Match by a list/time/property mapping → fetch source value | `LOOKUP` |
| Hardcode retrieval for a specific list item or time period | `SELECT` |

`LOOKUP` is the workhorse; `SELECT` is for fixed selectors.

## Performance warning
> ⚠️ **Never use SUM and LOOKUP in the same formula.** This combination causes extremely long calculation times. If you need both, split into two line items: one for the LOOKUP, one for the SUM that consumes it.

(Source: every LOOKUP/SUM Anapedia page repeats this; see *Formulas and their effects on model performance* in Anaplan Community.)

## Polaris vs Classic
- **LOOKUP in non-composite hierarchy:** Polaris returns the aggregate value; Classic returns the line item's default.
- **LOOKUP with target timescale > source:** Polaris invalidates the formula; Classic returns 0.
- **Mapping line item with unrelated dimension (incl. line item subset):** Polaris invalidates; Classic may evaluate.

Always check engine target if a LOOKUP behaves unexpectedly.

## Pattern
```
Pay Table.Basic Pay[LOOKUP: Grade, LOOKUP: Region]
```
- Source line item must be reachable from target via the mapping line items.
- Mapping line items must resolve to a list, time, or date type that aligns with the source dimension.

## See also
- [[wiki/functions/categories/aggregation]]
- [[wiki/functions/index]]
