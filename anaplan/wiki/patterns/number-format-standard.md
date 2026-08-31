---
title: Number Format Standard
type: pattern
tags: [anaplan, pattern, formatting, number-format]
created: 2026-07-27
updated: 2026-07-27
sources: []
---

# Number Format Standard

**Convention (user-specified, applies across all models in this vault):** for NUMBER-formatted
line items, **comma (`,`) is the decimal separator** and **dot (`.`) is the thousands/grouping
separator** — i.e. EU/NL locale (`1.234,56`). In Anaplan's Line Items export this maps to:

```json
"decimalSeparator": "COMMA",
"groupingSeparator": "FULL_STOP"
```

The inverse (`decimalSeparator: FULL_STOP`, `groupingSeparator: COMMA` — US/UK locale,
`1,234.56`) is **non-standard** and should be flagged wherever found. Other grouping values
(`SPACE`, `NONE`) are also non-standard outliers.

## Why this matters

Some models in this vault are Dutch-language and dashboarded for
Dutch-speaking business users — inconsistent decimal/grouping conventions between line items
on the same board are confusing and error-prone (e.g. `1.234` reading as one-thousand-two-
hundred-thirty-four vs one-point-two-three-four depending on which convention the line item
happens to use).

## Audits performed against this standard

A full-model audit against this standard has been run on one production model in this vault:
an initial pass flagged just over a thousand non-standard NUMBER line items, narrowed down to
the subset actually visible in the New UX (grids/combined grids/charts/fields/KPIs); a
follow-up delta re-check found the non-standard count dropping meaningfully, and a later status
update confirmed a large share of the previously-flagged NUX-visible items had since been fixed,
with the remainder still outstanding. This shows the audit-then-remediate cycle working as
intended — flag drift, track it over successive deltas, confirm fixes land.

No other model in this vault has had this audit run yet.
