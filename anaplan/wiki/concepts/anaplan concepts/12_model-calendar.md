---
title: Model Calendar
type: concept
tags: [anaplan, time, calendar, fiscal-year, weeks, model-settings]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Time  Anapedia.md
  - raw/docs/Set the model calendar.md
  - raw/docs/Set the Calendar MonthsQuartersYears calendar.md
  - raw/docs/Set the Weeks 13 4-week Periods calendar.md
  - raw/docs/Set the Weeks 4-4-5, 4-5-4, or 5-4-4 calendar.md
  - raw/docs/Set the Weeks General calendar.md
  - raw/docs/Changes to the Fiscal Year Label.md
  - raw/docs/Time period selection.md
---

# Model Calendar

The **model calendar** is the single global time configuration that governs how every module and line item in a model understands time. All time dimensions — months, quarters, fiscal years, weeks — derive from this one setting. It is not a module; it is a model-wide infrastructure decision.

See also: [[Time Ranges]], [[Planual Chapter 1 — Central Library]]

---

## Critical gotcha: calendar type is effectively permanent

> [!warning]
> The calendar type should be chosen **before importing any data** and treated as immutable in production. Changing the calendar type after a model is built can cause widespread data loss across all line items and modules that use the Time dimension. Always set the calendar type first; everything else follows from it.

---

## Calendar type comparison

| Type | Description | Native periods per year | Typical use case |
|------|-------------|------------------------|-----------------|
| **Calendar Months/Quarters/Years** | Standard Gregorian months | 12 months | Most FP&A, finance |
| **Weeks: General** | Arbitrary number of weeks from a start date; no fiscal year concept | No fiscal year | Short-horizon operational, rolling windows |
| **Weeks: 13 (4-week Periods)** | 13 equal 4-week periods; one quarter has 4 periods, others have 3 | 13 periods | Payroll cycles, banks, even-period comparison |
| **Weeks: 4-4-5** | Weeks grouped 4-4-5 per quarter | 12 "months" | Retail fiscal-week alignment |
| **Weeks: 4-5-4** | Weeks grouped 4-5-4 per quarter | 12 "months" | Retail / CPG |
| **Weeks: 5-4-4** | Weeks grouped 5-4-4 per quarter | 12 "months" | Retail / CPG |

### Key differences between week-based calendars

- **Weeks: General** has **no concept of fiscal years**, so YTD, YTG, and Year summary levels are unavailable. It also **does not support time ranges**. Suitable only for purely week-based rolling horizons.
- **Weeks: 13 4-week Periods** gives 13 equal-length periods, making period-over-period comparison statistically clean. ~Every 6 years, a 53rd week is added; the model calculates which year automatically.
- **Weeks: 4-4-5** (and variants) maps weeks to 12 named "months" per fiscal year. Fiscal months are not calendar months — a 4-4-5 month and a calendar month are different things. Approximately every 5–6 years, one quarter will have a 14-week quarter to compensate for the 52-week vs 365-day drift.

---

## Fiscal year start month

Setting a non-January fiscal year start has two effects:
1. All period labels shift — e.g., FY26 covers Apr 2025 – Mar 2026 if the fiscal year starts in April.
2. All time ranges realign to the new fiscal year start month.

When the fiscal year does not match the calendar year, you must also choose whether the **Fiscal Year Label** is aligned with the **end month** or the **start month** of the fiscal year. This affects how FY labels appear in column headers.

---

## Fiscal Year Label

The **Fiscal Year Label** is the 2-character prefix shown before year numbers in the Time dimension (default: `FY`). It can be changed to `CY` (calendar year) or any other 2-character string.

**Changing this label is low-risk for month-scale imports but high-risk for other time scales.** Specifically:

| Time scale on importing module | Impact of FY label change |
|-------------------------------|--------------------------|
| Months | No impact |
| Weeks, Periods, Quarters, Half-Year, Year | Import mapping breaks — module will error with "Invalid date or timescale identifier" if mapped by Name Only |

To fix broken imports after a label change: use the **Custom fixed-position pattern** import option when mapping the Time dimension, or update the label in the source data to match. Always test in a development model first.

Use the **same Fiscal Year Label across all related models** in a workspace to maintain consistency.

---

## Timescale format: 2-digit vs 4-digit

All calendar types support two display formats:

| Format | Example (FY 2026) | Example (Jan 2025) | Planning limit |
|--------|-------------------|--------------------|---------------|
| 2-digit | FY26 | Jan 25 | Up to 2078 |
| 4-digit | FY2026 | Jan 2025 | 100 years from start date |

Choose 4-digit format if your model will persist long enough that 2-digit labels could become ambiguous.

---

## Model calendar scale settings

### Past and future years
- Up to **20 years** into the past.
- Up to **50 years** into the future.
- Each additional year substantially increases model size. Use [[Time Ranges]] for time windows outside the active planning horizon.

### Current Period
A model-level setting (not a version) marking the most recent period with actual data. It:
- Drives the default version page selector context.
- Enables `YTD` and `YTG` summary columns (for the year containing Current Period).
- Can be referenced in formulas: `Revenue.Data[SELECT: TIME.'Current Period']`
- Can be updated via the **Update Current Period** action (automatable from a data hub).
- Functions: `CURRENTPERIODSTART`, `CURRENTPERIODEND`

If Current Period is not set, these functions return blank.

### Optional aggregation levels

| Option | Effect |
|--------|--------|
| **Quarter Totals** | Adds Q1/Q2/Q3/Q4 summary columns; unlocks Quarter time scale for line items |
| **Half-Year Totals** | Adds H1/H2 summary columns; unlocks Half-Year time scale for line items |
| **YTD** | Adds a YTD summary column for the year containing Current Period |
| **YTG** | Adds a YTG summary column for the year containing Current Period |
| **All Periods** | Adds a grand total column across all calendar periods |

> [!note]
> **Weeks: General** does not support Quarter, Half-Year, YTD, YTG, or All Periods aggregations.

---

## 53rd week (week-based calendars)

Both the 13 4-week Periods and the 4-4-5/4-5-4/5-4-4 calendars must handle the 52-week vs 365-day gap. Approximately every 6 years, a **53rd week** appears. Anaplan calculates which year gets the 53rd week automatically, based on the "End of Fiscal Year" setting. The model builder selects which period within that year absorbs the extra week.

---

## Effect of model calendar changes

| Change | Effect on model |
|--------|----------------|
| Calendar type | All Time-dimensioned data at risk; effectively a rebuild |
| Fiscal Year Start Month | All time ranges realign; potential data loss |
| Available Aggregations (remove) | Data loss for line items at that aggregation level |
| Fiscal Year Label | Breaks imports on non-month time scales |
| Current Fiscal Year | New year starts clean; prior data lost unless Past Years > 0 |
| Number of Past/Future Years | Adds or removes time periods; removal destroys data in removed periods |
| Week grouping (4-4-5 etc.) | Inherited by time ranges; no data effect |
