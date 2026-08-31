---
title: Time and Date Functions
type: function-category
tags: [anaplan, functions, time]
created: 2026-05-02
updated: 2026-05-02
---

# Time and Date Functions

The largest category (36 functions). Group these into mental sub-buckets — picking the right one is mostly about identifying which sub-bucket the question lives in.

## Sub-buckets

### 1. Date construction / arithmetic
`DATE`, `ADDMONTHS`, `ADDYEARS`

### 2. Date components
`DAY`, `MONTH`, `YEAR`, `WEEKDAY`, `DAYS`, `DAYSINMONTH`, `DAYSINYEAR`

### 3. Period boundaries
`START`, `END`, `PERIOD`, `INPERIOD`, `CURRENTPERIODSTART`, `CURRENTPERIODEND`

### 4. Cumulation (running totals within a calendar window)
`WEEKTODATE`, `MONTHTODATE`, `QUARTERTODATE`, `HALFYEARTODATE`, `YEARTODATE`, `CUMULATE`, `DECUMULATE`

### 5. Period summary value (broadcast a parent-period summary onto every child)
`WEEKVALUE`, `MONTHVALUE`, `QUARTERVALUE`, `HALFYEARVALUE`, `YEARVALUE`

### 6. Position offsets along a dimension
`LAG`, `LEAD`, `OFFSET`, `POST`, `NEXT`, `PREVIOUS`

### 7. Windowed aggregates
`TIMESUM` (range between two periods), `MOVINGSUM` (rolling window)

### 8. Allocation / shaping
`SPREAD` (even split), `PROFILE` (multiply by a profile series)

## Cumulation vs Value — easy to confuse
- `MONTHTODATE` (cumulation) → running sum *within* the month, resets at month start.
- `MONTHVALUE` (period value) → broadcasts the *month total* down to every period inside that month.

Same naming pattern for WEEK, QUARTER, HALFYEAR, YEAR.

## LAG vs PREVIOUS vs OFFSET
- `LAG(value, 1, default)` — value from N positions back, with explicit default.
- `PREVIOUS(expr)` — *evaluate* an expression at the previous position (recursive-friendly).
- `OFFSET` — bidirectional shift along a chosen dimension.

## See also
- [[wiki/functions/index]]
- [[wiki/concepts/anaplan concepts/10_line-item]]
