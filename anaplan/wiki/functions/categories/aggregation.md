---
title: Aggregation Functions
type: function-category
tags: [anaplan, functions, aggregation]
created: 2026-05-02
updated: 2026-05-02
---

# Aggregation Functions

Use the `Source[FUNC: Mapping, ...]` selector syntax to roll values up from a source [[wiki/concepts/anaplan concepts/10_line-item|line item]] into a target via mapping line items. The target's dimensionality determines the grain of the result.

## Members
**SUM, AVERAGE, MIN, MAX, ANY, ALL, FIRSTNONBLANK, LASTNONBLANK, TEXTLIST**

## When to use which
| Need | Function |
|---|---|
| Totalize numbers | `SUM` |
| Mean | `AVERAGE` |
| Extremes | `MIN`, `MAX` |
| Boolean rollups | `ANY` (OR-style), `ALL` (AND-style) |
| Pick a representative non-blank value | `FIRSTNONBLANK`, `LASTNONBLANK` |
| Concatenate text into one cell | `TEXTLIST` |

## Pattern
- A common dimension must connect source and mapping.
- Multiple mappings allowed: `Source[SUM: M1, SUM: M2]`.
- Aggregation functions produce results at the *target* module's grain.

## Pitfalls
- ⚠️ **Never combine SUM with LOOKUP in the same line item formula** — see [[wiki/functions/categories/mapping]].
- Mismatched timescales: if target is finer than source, results may be 0 or default.
- `MIN`/`MAX` exist in both this category and [[wiki/functions/categories/numeric|Numeric]] — different semantics. Aggregation versions use `[MIN: Mapping]` selector syntax.

## See also
- [[wiki/functions/categories/mapping]] — LOOKUP / SELECT
- [[wiki/functions/index]]
