---
title: Time Ranges
type: concept
tags: [anaplan, time, dimensions, time-ranges, mixed-time-scales]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Time ranges.md
  - raw/docs/Time range fundamentals.md
  - raw/docs/Work with time ranges.md
  - raw/docs/Create a new time range.md
  - raw/docs/Edit a time range.md
  - raw/docs/Delete a time range.md
  - raw/docs/Remove references to a time range.md
  - raw/docs/Mixed time scales in a model.md
  - raw/docs/Apply time scales to individual line items.md
  - raw/docs/Time period selection.md
---

# Time Ranges

A **time range** is a named subset of time periods, defined in units of whole fiscal years, that can be assigned to modules or individual line items. Time ranges allow different parts of a model to span different time windows without expanding the global model calendar.

See also: [[Model Calendar]], [[Planual Chapter 1 — Central Library]]

---

## What a time range is

Each time range is an independent entity with:
- **Start Period** — first fiscal year (tied to the model's Fiscal Year Start Month)
- **Number of Periods** — length in whole fiscal years
- **Available Aggregations** — which summary levels (month, quarter, half-year, year) the range exposes

Time ranges are independent of Current Period and do not roll forward automatically. They have a **fixed span**.

The start point of every time range anchors to the **Fiscal Year Start Month** of the model calendar. If that setting changes, all time ranges realign accordingly.

---

## Default time range vs custom ranges

| Scenario | Use |
|----------|-----|
| All data fits within the current fiscal window | Model calendar only — no custom time ranges needed |
| Actuals history spanning multiple past years | Add a "History" time range covering e.g. FY2015–FY2024 |
| Long-range planning (10+ years) | Add a "Long Range" time range; avoids bloating the model calendar |
| Short-horizon operational modules | Assign a narrow time range to those modules to reduce sparsity |

> [!note]
> Best practice: keep the model calendar as small as possible (use the minimum number of past/future years), and use time ranges for anything that falls outside the operational planning window. Each additional calendar year substantially increases model size.

---

## Relationship to the model calendar

A time range can:
- Exist entirely **within** the model calendar
- **Extend before** the calendar start
- **Extend after** the calendar end
- Exist entirely **outside** the model calendar

They do not react to changes to the model calendar's fiscal year count or Current Period setting — but they **do** realign if the Fiscal Year Start Month changes.

---

## Per-line-item time scale

Beyond the module-level time range, individual line items can be set to a different **time scale** (granularity) within the Blueprint. Available scales depend on the model's calendar type:

| Calendar type | Available time scales |
|---------------|-----------------------|
| Calendar Months/Quarters/Years | Not Applicable, Day, Month, Quarter*, Half-Year*, Year |
| Weeks: 13 4-week Periods | Not Applicable, Day, Week, Month, Quarter*, Year |
| Weeks: 4-4-5 / 4-5-4 / 5-4-4 | Not Applicable, Day, Week, Month, Quarter*, Half-Year*, Year |
| Weeks: General | Not Applicable, Day, Week |

*Quarter and Half-Year require those aggregations to be enabled in the model calendar.

When you set a different time scale on a line item, Anaplan automatically creates a **subsidiary view** for that module.

---

## Mixed time scales: aggregation and disaggregation rules

When two line items in the same module (or in a formula cross-reference) have different time scales:

- **Finer → coarser (aggregation)**: Works automatically. Days sum into months, months sum into quarters, quarters sum into years. You can skip levels (e.g., days directly to years).
- **Coarser → finer (disaggregation)**: Does NOT work by default. If `Y` is in Years and `X` is in Months, `X = Y` returns a blank, because `Y` has no monthly value to distribute.

| Formula | Behavior |
|---------|----------|
| `Y = X` (X=months, Y=years) | Y receives the year total aggregated from X |
| `X = Y` (X=months, Y=years) | Returns blank (no monthly disaggregation) |
| `X = YEARVALUE(Y)` | Returns the year value of Y in every month of X |
| `X = YEARVALUE(Y) / 12` | Evenly distributes Y over 12 months |
| `X = YEARVALUE(Y) * Seasonality %` | Distributes Y by a seasonality curve |
| `X = Y[SELECT: Time.FY26]` | Returns Y's value for a specific year in every month |

> [!warning]
> `X = Y` where X is at a finer granularity than Y produces a **blank**, not an error. This is a common silent mistake. Use `YEARVALUE`, `MONTHVALUE`, `QUARTERVALUE`, or `SELECT` to explicitly disaggregate.

Functions used for cross-scale references: `WEEKVALUE`, `MONTHVALUE`, `QUARTERVALUE`, `HALFYEARVALUE`, `YEARVALUE`, `SELECT`.

---

## Time period selection and the superset

The **time period superset** is the union of all periods across all time ranges and the model calendar. It determines which periods are available in context-sensitive selectors (e.g., version switchover dates, import selected-year settings).

| Model element | Time options governed by |
|---------------|--------------------------|
| Line item time scale | That line item's assigned time range |
| Time period format | Superset |
| Version switchover / Edit From / Edit To / Bulk Copy | Superset |
| Module filter / compare / import | Module's time range |
| Import > Selected Year | Superset |
| Current Period | Model calendar settings |

Adding or removing a time range modifies the superset, which can affect selectors across the model.

---

## Limitations

- Can only use units of **whole years** — no fractional years.
- Do **not** support the **Weeks: General** calendar type.
- Do not vary by version or any other list dimension.
- Cannot be marked as production data (ALM).
- Fixed span — do not roll with Current Period.
- System date constraint: start period must be between FY1981 and FY2078.

---

## Advantages

| Benefit | Detail |
|---------|--------|
| Less sparsity | Engine can ignore empty cells outside the range; no unnecessary aggregations |
| Avoids custom time lists | Eliminates brittle workarounds for non-standard time windows |
| Independent aggregation | Each range can have its own summary levels |
| Greater range | 2-digit format: up to FY2078; 4-digit: up to 100 years from start |
| ALM support | Time ranges synchronize across environments via ALM |

---

## Editing and deleting a time range

**Editing**: Any change to a time range's span or aggregations may cause **data loss** for line items using that range. Anaplan warns before saving. Modules and line items linked to the edited range continue using it automatically.

**Deleting**: A time range must be **inactive** (no line item references it) before it can be deleted.

Cleanup steps before deletion:
1. In the Line Items tab (Modules), find all line items where the Time Range column references your range.
2. Reassign each to a different time range (data loss warning will appear).
3. Once no references remain, delete the range from the Time Ranges tab.

For models with many line items, export the line items list first and filter in a spreadsheet tool to identify references efficiently.
