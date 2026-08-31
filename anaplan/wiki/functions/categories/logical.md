---
title: Logical Functions
type: function-category
tags: [anaplan, functions, logical]
created: 2026-05-02
updated: 2026-05-02
---

# Logical Functions

Boolean tests and the conditional construct.

## Members
**IF THEN ELSE, COMPARE, ISBLANK, ISNOTBLANK, ISANCESTOR, ISFIRSTOCCURRENCE, ISACTUALVERSION, ISCURRENTVERSION**

## When to use which
| Need | Function |
|---|---|
| Branch on a condition | `IF cond THEN a ELSE b` |
| Three-way text comparison (-1/0/1) | `COMPARE` |
| Detect blank / non-blank | `ISBLANK`, `ISNOTBLANK` |
| Test list/time hierarchy ancestry | `ISANCESTOR` |
| Mark first occurrence in a list | `ISFIRSTOCCURRENCE` |
| Conditional formulas tied to versions | `ISACTUALVERSION`, `ISCURRENTVERSION` |

## IF THEN ELSE patterns
```
IF Sales > 0 THEN Sales * Margin% ELSE 0
IF ISBLANK(Forecast) THEN Plan ELSE Forecast
IF ISACTUALVERSION() THEN Actuals ELSE Plan
```

Nested IFs are allowed but become unreadable fast — extract sub-expressions into intermediate calculation line items (see [[wiki/patterns/disco|DISCO]]).

## See also
- [[wiki/functions/index]]
