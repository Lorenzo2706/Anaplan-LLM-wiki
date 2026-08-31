---
title: Variance Reporting
type: pattern
tags: [anaplan, reporting, variance, versions, line-item-subset, LIS, DISCO, REP, SYS]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Variance reports with versions.md
  - raw/docs/Variance reports without versions.md
  - raw/docs/Example Create SYS11 Time Variance Reporting input module.md
  - raw/docs/Example Create REP05 Variance Report staging module.md
  - raw/docs/Example Create REP06 Variance Report module.md
---

# Variance Reporting

Variance reporting in Anaplan compares two scenarios (Actual vs Budget, Current Month vs Prior Month, etc.) and computes the absolute and percentage difference. There are two structural approaches depending on whether the model uses native Versions as a dimension.

See also: [[Versions]], [[Pattern — Version-as-list (custom-list scenarios)]], [[DISCO — Module Classification]], [[Line Item Subsets (LIS)]], [[Planual Chapter 2 — Engine]]

---

## Approach 1: Variance WITH native Versions

In models that use Anaplan's built-in Versions dimension, variance can be modeled **directly on the Versions list** using version formulas.

### Version formula setup

Create dedicated Variance and Variance % versions in the Versions pane and assign formulas in the Formula column:

| Version | Formula |
|---------|---------|
| Actual | *(no formula — source data)* |
| Budget | *(no formula — source data, switchover = Jan of plan year)* |
| Variance | `Actual - Budget` |
| Variance % | `IF Budget > 0 THEN 100 * (Actual - Budget) / Budget ELSE 100 * (Budget - Actual) / Budget` |

The variance columns update automatically when Current Period changes. Any module that has Versions on rows or columns will display the computed variance.

### Alternative: SELECT-based line items (no extra version member)

You can avoid adding Variance as a version member by pulling scenarios into separate line items using `SELECT`:

| Line Item | Formula |
|-----------|---------|
| Actual | `Module.LineItem[SELECT: VERSIONS.Actual]` |
| Budget | `Module.LineItem[SELECT: VERSIONS.Budget]` |
| Variance | `Budget - Actual` |
| Variance % | `Variance / Actual` |

> [!note]
> `SELECT` with a version works only on line items (not on module-level formulas or summary rows).

### Time-period variance with `ISACTUALVERSION`

When a formula spans the version switchover boundary (e.g., a calculation that should use actuals before a date and a forecast after), use `ISACTUALVERSION`:

```
IF ISACTUALVERSION() THEN Actuals.Revenue ELSE Forecast.Revenue
```

---

## Approach 2: Variance WITHOUT native Versions

For models that do not use the Versions dimension — including **version-as-list models** like FSP 2.0 and AAC — scenarios are stored in separate line items or accessed via list members. No Version dimension is involved.

### Line item per scenario

Each scenario is a line item. Variance is a simple arithmetic formula:

| Line Item | Formula |
|-----------|---------|
| Actual | *(source reference or import)* |
| Budget | *(source reference or import)* |
| Variance | `Budget - Actual` |
| Variance % | `Variance / Actual` |

This is simpler, avoids version overhead, and is **Polaris-optimal**.

### Using a Line Item Subset (LIS) for multi-variance reporting

When you need to compare multiple metrics across two time periods simultaneously (e.g., Revenue, Cost, Margin each compared between any two user-selected months), a **Line Item Subset (LIS)** provides a flexible, scalable structure.

The LIS `LIS: Multi-variance reporting` collects line items from one or more source modules. The `COLLECT()` function populates a staging module dimensioned by the LIS, making any metric in the subset available in the report without hardcoding individual line item references.

---

## Three-module chain: Anapedia example

This is the reference implementation pattern for flexible time-variance reporting using a LIS. It is dimension-agnostic with respect to versions — it works equally well whether scenarios are stored as Versions or as list members.

### Module 1: SYS11 Time Variance Reporting (System / Input)

**DISCO category**: System (SYS) — stores user selections

| Setting | Value |
|---------|-------|
| Dimensions | Users on Pages; line items on Rows |
| Time | Not applicable (no time dimension) |

| Line Item | Format | Summary |
|-----------|--------|---------|
| Month 1 | Time period: Month | None |
| Month 2 | Time period: Month | None |

**Purpose**: Allows each user to independently select two time periods to compare. The selections drive LOOKUP formulas in REP06. No formula is needed — these are pure user inputs.

---

### Module 2: REP05 Variance Report Staging (Report / Calculation)

**DISCO category**: Report staging (REP) — intermediate calculation

| Setting | Value |
|---------|-------|
| Dimensions | G2 Country + LIS: Multi-variance reporting on Pages; Time on Columns |
| Rows | LIS: Multi-variance reporting |
| Time Scale | Month |

| Line Item | Format | Formula | Summary | Time Scale |
|-----------|--------|---------|---------|-----------|
| Data | Number | `COLLECT()` | None | Month |

**Purpose**: Uses `COLLECT()` to pull monthly data for every line item in the LIS across the Country dimension. This single line item acts as a universal data spine — any metric registered in the LIS is automatically available here without formula changes.

---

### Module 3: REP06 Variance Report (Report / Output)

**DISCO category**: Report output (REP) — dashboard-facing

| Setting | Value |
|---------|-------|
| Rows | LIS: Multi-variance reporting |
| Columns | Line items (Month 1, Month 2, Variance, % Variance) |
| Pages | G2 Country, Users |
| Time | Not applicable |

| Line Item | Format | Formula |
|-----------|--------|---------|
| Month 1 | Number | `'REP05 Variance Report Staging'.Data[LOOKUP: 'SYS11 Time Variance Reporting'.'Month 1']` |
| Month 2 | Number | `'REP05 Variance Report Staging'.Data[LOOKUP: 'SYS11 Time Variance Reporting'.'Month 2']` |
| Variance | Number | `'Month 2' - 'Month 1'` |
| % Variance | Number: Percentage | `Variance / 'Month 1'` |

**Purpose**: The output module shown on a UX dashboard card. Time is not a dimension here — instead, the two chosen months are resolved via LOOKUP against the user's SYS11 selections. Each user sees their own variance because SYS11 is per-user.

---

## Key formula patterns

### LOOKUP to resolve a user-selected time period
```
'REP05 Variance Report Staging'.Data[LOOKUP: 'SYS11 Time Variance Reporting'.'Month 1']
```
`SYS11.Month 1` has format `Time period: Month`. The LOOKUP maps from the user's selected month to the corresponding column in the staging module. This avoids hardcoding any specific time period.

### COLLECT() to aggregate a LIS
```
COLLECT()
```
Used in a line item dimensioned by a LIS. Pulls the value from whichever source line item each LIS member maps to. Enables a single staging line item to serve all metrics in the subset simultaneously.

### SELECT to pin a specific version or time period
```
Module.LineItem[SELECT: VERSIONS.Actual]
Module.LineItem[SELECT: TIME.'Current Period']
```
Used in the without-versions approach to extract a specific version's data into a line item.

---

## When to use each approach

| Criterion | Approach: native Versions | Approach: no Versions (LIS/line items) |
|-----------|--------------------------|----------------------------------------|
| Model uses native Versions dimension | Yes | Not applicable |
| Polaris model (FSP 2.0, AAC) | Avoid — version block overhead | Preferred |
| Classic engine model | Viable | Viable |
| Scenarios > ~10 | Not recommended | Preferred (version-as-list) |
| User-selectable time comparison (any two months) | Needs SYS module + LOOKUP | SYS module + LOOKUP (same regardless) |
| Simple Actual vs Budget on a module | Version formulas — fastest to implement | SELECT-based line items — equally simple |
| Reuse across many metrics | Version columns apply model-wide | LIS + COLLECT — explicit but flexible |

> [!note]
> FSP 2.0 and AAC are Polaris models using version-as-list. For those models, the without-versions LIS approach is the correct choice. Version formulas and `ISACTUALVERSION` are not available when Versions is not a model dimension.
