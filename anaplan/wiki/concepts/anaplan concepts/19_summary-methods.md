---
title: Summary Methods
type: concept
tags: [anaplan, fundamentals, aggregation, line-item, hierarchy, polaris, classic]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Summary methods.md
  - raw/docs/Configure line items.md
  - raw/docs/Manage model size.md
---

# Summary Methods

A **summary method** defines how a [[Line Item|line item]]'s values aggregate when a parent member of a list hierarchy (or a higher time period) is selected in rows or columns of a module grid. It is set per line item in the **Summary** column of Blueprint.

> [!note]
> Summary methods are about *automatic rollup* — what you see in the parent-level cell. They are distinct from aggregation **functions** (like `SUM(...)`) used in formulas, which aggregate across a dimension in a calculation.

## Summary method vs. aggregation function

| | Summary method | SUM / other aggregation function |
|---|---|---|
| **Where configured** | Blueprint — Summary column | Formula bar |
| **When it runs** | When a parent-level list member or higher time period is visible | Explicitly called in a formula |
| **Scope** | Controls the automatic rollup cell | Controls a calculated value in any cell |
| **Example** | Set to Sum → quarterly cell shows sum of its months | `SUM(Revenue, Product)` → single cell aggregating across Product members |

## Available summary methods

| Summary method | Valid data types | Description | When to use |
|---|---|---|---|
| **None** | Number, Boolean, Date, List, Time Period, Text | Parent cell is **blank** — no aggregation. Default for Number and Boolean. | Line items only meaningful at leaf level (e.g. exchange rate, %-input that should not be summed). |
| **Sum** | Number | Adds all child cell values. | Additive measures: headcount, revenue, cost, units. |
| **Average** | Number | Mean of child cells, including zeros and empty cells. | Rates, prices, scores where the average across children is meaningful. |
| **Ratio** | Number | Divides one line item by another; specify numerator and denominator. | Margins, ROI, any percentage that should be computed from totals rather than averaged from ratios. |
| **Formula** | Number, Boolean, Date, List, Time Period, Text | Evaluates the line item's formula at the parent level, picking references at the appropriate hierarchy level. | Any calculated line item whose formula already handles aggregation correctly — percentages, variances, rates. |
| **Min** | Number, Date, Time Period | Returns the smallest child value. | Earliest date, lowest price, minimum inventory. |
| **Max** | Number, Date, Time Period | Returns the largest child value. | Latest date, peak sales, maximum headcount. |
| **Opening Balance** | Number *(Time summary only)* | Returns the value of the first time period in the range. | Opening cash, opening inventory for a quarter/year. |
| **Closing Balance** | Number *(Time summary only)* | Returns the value of the last time period in the range. | Closing inventory, end-of-period subscriber count. |
| **Any** | Boolean | TRUE if at least one child is TRUE. | Risk flags, overdue flags — parent is flagged if any child is flagged. |
| **All** | Boolean | TRUE only if every child is TRUE. | Completion checks — parent is complete only if all sub-tasks are complete. |
| **First non-blank** | Date, List, Time Period, Text | Returns the first non-empty value over time. | Original assignment, initial status. |
| **Last non-blank** | Date, List, Time Period, Text | Returns the most recent non-empty value over time. | Current owner, latest status. |

> [!note]
> When no input values exist, methods return the data type's default: **0** for Number, **FALSE** for Boolean, **BLANK** for all other types.

## The FORMULA option — critical for Polaris

**Formula** is the most important and most misused summary method.

When set to **Formula**, the line item's formula is **re-evaluated at the parent level** using the members at that level as context — it does not sum up child results. This is correct behavior for any line item whose formula already produces the right aggregate naturally (e.g. a percentage, a variance, a lookup).

### Why this matters for Polaris

In Polaris, sparsity is pervasive. If a calculated line item has summary method **Sum** but its formula already produces correct totals by re-evaluation (because the referenced line items themselves roll up correctly), the parent cell will **double-count**:

1. The formula at the child level produces child values.
2. The Sum summary adds those child values for the parent.
3. But the formula *re-evaluated at the parent level* would already have been correct.

**Rule:** For any calculated line item (i.e. one with a formula), default to **Formula** as the summary method. Switch to **Sum** only when the formula is genuinely additive and you want the parent to be the sum of children (not a re-evaluation).

### Example

```
Margin % = Margin / Revenue
```

- Summary = **Sum** → parent Margin % would be the *sum* of all child Margin % values. Wrong.
- Summary = **Formula** → parent Margin % = (parent-level Margin) / (parent-level Revenue). Correct.

```
Units Sold = (input)
```

- Summary = **Sum** → parent shows total units. Correct.
- Summary = **Formula** → parent re-evaluates the formula (but there is no formula — it is an input). Use **Sum**.

## NONE — the safe default

The Anapedia recommendation and best practice:

> Set your line item's summary method to **None**, and only use another summary method when you need it.

Reasoning: summaries cause aggregated cells to be computed. In a large model with many dimensions and deep hierarchies, unnecessary summaries multiply cell counts and computation significantly.

## RATIO — when to prefer it over FORMULA

Use **Ratio** instead of **Formula** when:

- The summary is purely `A / B`.
- You want to declare the numerator and denominator explicitly rather than relying on the formula being evaluated correctly at the parent.
- Classic engine only (check Polaris compatibility).

Example: `Profit Margin = Profit / Revenue` — specifying Profit as numerator and Revenue as denominator means the summary is always computed from the *parent-level totals*, never a sum of child ratios.

## Time summary independence

You can set a **different summary method for the Time dimension** compared to other dimensions. For example:

- List hierarchy summary: **Sum** (aggregate headcount across departments)
- Time summary: **Closing Balance** (show end-of-period headcount, not a sum of months)

When using Time summary, **Formula**, **None**, and **Ratio** can be combined with each other.

## Common gotchas

| Gotcha | Description |
|---|---|
| **Sum on a calculated % line item** | Parent shows sum of percentages (e.g. 320%) instead of a re-evaluated percentage. Fix: set to **Formula** or **Ratio**. |
| **Formula on an input line item** | Input line items have no formula to re-evaluate — parent cell will be blank or zero. Fix: set to **Sum**, **Average**, etc. |
| **Average includes zeros and blanks** | Average counts empty cells as zero, which can skew results. Consider whether this is intended. |
| **Forgetting None causes cell bloat** | Every summary method other than None creates additional aggregated cells. In large models, this can double or triple cell counts. |
| **Changing summary method mid-project** | Can silently change dashboard values that users rely on — communicate changes and audit dependent outputs. |

## Cross-references

- [[Line Item]] — where summary methods are configured
- [[Lists]] — hierarchy levels that summary methods roll up through
- [[Dimensions]] — dimensions over which aggregation occurs
