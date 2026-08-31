---
title: Numeric Functions
type: function-category
tags: [anaplan, functions, numeric]
created: 2026-05-02
updated: 2026-05-02
---

# Numeric Functions

Scalar math operating on individual values (not aggregations).

## Members
**ABS, DIVIDE, EXP, FIRSTNONZERO, LN, LOG, MAX, MIN, MOD, MROUND, POWER, ROUND, SIGN, SQRT**

## Highlights
- `DIVIDE(a, b)` — preferred over `a / b` because it handles divisor=0 gracefully (returns 0).
- `FIRSTNONZERO(v1, v2, ...)` — coalesce-style helper.
- `ROUND` vs `MROUND` — round to N decimals vs round to nearest multiple.
- `MAX`/`MIN` here are scalar comparisons across arguments. The same names exist as [[wiki/functions/categories/aggregation|aggregation]] functions with different selector syntax.
- `POWER(x, n)` and `EXP(x)` for exponentials; `LN`, `LOG` for logs.

## See also
- [[wiki/functions/index]]
- [[wiki/functions/categories/aggregation]] for `[MAX:]`, `[MIN:]` selectors
