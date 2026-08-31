---
title: Polaris Formula Patterns — Functions & Replacements
type: concept
tags: [anaplan, polaris, formulas, functions, classic-vs-polaris]
created: 2026-06-09
updated: 2026-06-09
sources: []
---

# Polaris Formula Patterns

Critical function availability and replacement patterns for Polaris models (FSP 2.0, AAC). Complements [[wiki/patterns/planual/02-engine|Planual Ch.2 — Polaris]].

> [!warning] Financial functions are entirely unavailable in Polaris
> All 22 functions in Anaplan's Financial category fail silently with "formula is invalid" in Polaris — no descriptive error is shown. Replace with date arithmetic (see below).

---

## 1. Financial functions — all unavailable in Polaris

The entire Financial function category is **Classic-only**:

`YEARFRAC` · `COUPDAYBS` · `COUPDAYS` · `COUPDAYSNC` · `COUPNCD` · `COUPNUM` · `COUPPCD` · `CUMIPMT` · `CUMPRINC` · `DURATION` · `FV` · `IPMT` · `IRR` · `MDURATION` · `NPER` · `NPV` · `PMT` · `PPMT` · `PRICE` · `PV` · `RATE` · `YIELD`

### YEARFRAC replacement

```
-- Classic
YEARFRAC(START(ITEM(Time)), some_date)

-- Polaris
(some_date - START(ITEM(Time))) / DAYS(ITEM(Time))
```

`DAYS(ITEM(Time))` returns the exact number of days in the current period (365 or 366 — leap-year safe). Date subtraction returns an integer number of days.

For the fraction between two arbitrary dates:
```
(date2 - date1) / DAYS(ITEM(Time))
```

### NPV replacement

Use `OFFSET` or `CUMULATE` to discount cashflows manually:
```
-- Discount factor for period n
1 / POWER(1 + rate, n)
```

### IRR

Not directly replaceable in Anaplan. Export cashflows to Excel or use an iterative solver pattern in a separate module.

---

## 2. Time functions — key Polaris patterns

### START() requires an argument

`START()` without an argument is **invalid in Polaris**. Always pass a period:

```
-- Invalid in Polaris
START()

-- Correct
START(ITEM(Time))      -- start of current time period
END(ITEM(Time))        -- end of current time period
```

### INPERIOD — preferred date-in-period check

`INPERIOD(Date, Period)` returns TRUE if a date falls within a time period. Use instead of YEAR comparison patterns:

```
-- Avoid
YEAR(date_LI) = YEAR(START(ITEM(Time)))

-- Prefer
INPERIOD(date_LI, ITEM(Time))
```

### PREVIOUS / NEXT / POST — removed in Polaris

Use `OFFSET` instead:

| Classic | Polaris |
|---|---|
| `PREVIOUS(x)` | `OFFSET(x, -1, 0)` |
| `NEXT(x)` | `OFFSET(x, 1, 0)` |
| `POST(x, n)` | `OFFSET(x, n, 0)` |

---

## 3. Year-fraction pattern for debt/maturity schedules

Full pattern for computing the fraction of a year a date-bounded instrument is active (e.g., `CA 23. Current Liability Schedule`.`Maturity factor`):

**Helper line items (Technical group):**

| LI | Formula |
|---|---|
| `Starts this year?` | `INPERIOD('IP 14. Debt Items'.'Start Period', ITEM(Time))` |
| `Matures this year?` | `INPERIOD('IP 14. Debt Items'.'Original maturity Period', ITEM(Time))` |
| `Already matured?` | `'IP 14. Debt Items'.'Original maturity Period' < START(ITEM(Time))` |
| `Not yet started?` | `'IP 14. Debt Items'.'Start Period' > END(ITEM(Time))` |
| `Fraction to start` | `('IP 14. Debt Items'.'Start Period' - START(ITEM(Time))) / DAYS(ITEM(Time))` |
| `Fraction to maturity` | `('IP 14. Debt Items'.'Original maturity Period' - START(ITEM(Time))) / DAYS(ITEM(Time))` |

**Maturity factor:**
```
IF Already matured? OR Not yet started?
THEN 0
ELSE IF Starts this year? AND Matures this year?
THEN Fraction to maturity - Fraction to start
ELSE IF Starts this year?
THEN 1 - Fraction to start
ELSE IF Matures this year?
THEN Fraction to maturity
ELSE 1
```

---

## 4. Quick reference — Polaris availability

| Category | Available in Polaris? |
|---|---|
| Aggregation | ✅ |
| Mapping (LOOKUP, SELECT) | ✅ |
| Time & Date | ✅ (with caveats above) |
| Logical | ✅ |
| Numeric | ✅ |
| Text | ✅ |
| **Financial** | ❌ **None** |
| Trigonometry | ✅ |
| Call Center | ✅ |
| Misc (COLLECT, CUMULATE, DISTRIBUTE) | ✅ (Polaris-only) |
