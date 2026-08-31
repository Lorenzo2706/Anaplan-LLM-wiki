---
title: Initializing Demand Planning Pt 2
type: concept
tags: [anaplan, demand-supply-chain-app, demand-planning]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/08-01 Initializing Demand Planning Pt2-overview.md
  - raw/docs/08-02 Initializing Demand Planning Pt2-List Management Options.md
  - raw/docs/08-03 Initializing Demand Planning Pt2-time and product filters.md
  - raw/docs/08-04 Initializing Demand Planning Pt2-baseline plan.md
  - raw/docs/08-05 Initializing Demand Planning Pt2-manually adjust DP.md
---

# Initializing Demand Planning Pt 2

## Purpose

Continues the initial configuration of the Anaplan Demand Planning application started in chapter 07. Focuses on the operational housekeeping and user-facing configuration that makes the app usable day-to-day: cleaning list data, pre-creating placeholders, building user filters, defining the baseline-plan logic per scenario and product classification, and configuring how manual demand adjustments behave.

At the end of this exercise the Demand Planning app should be ready for end-user use.

## Steps covered

### 08-01 Overview

Four configuration themes for this exercise:

1. **List management** — delete orphans, create empty list placeholders.
2. **User filters** — time filters and product filters used across charts, tables and page selectors.
3. **Baseline plan** — driven by scenarios and product classification.
4. **Manual adjustment behavior** — including the perpetuation parameter.

### 08-02 List management options

**Orphans.** Many lists in the app (e.g. promotions) roll up under the product or customer hierarchy. When a parent (e.g. a customer) is removed during a hierarchy refresh or sync, its children become orphans — list items that have lost their parent. They must be cleared out, both at initial setup and on an ongoing scheduled basis.

- Page **906 Delete Orphans** identifies orphaned items across multiple lists and runs the cleanup processes.
- Example: promotions whose parent customer was deleted appear as orphans in the underlying `promotion header` list; running the process removes them.

**Empty placeholders.** Users need pre-created empty list items to plan against (new product introductions, second-tier customers, opportunities, promotions, etc.).

- Page **904 Create Empty Placeholders** runs the processes that pre-create these slots.
- The number of placeholders per list is parameter-driven (e.g. 10 for one list, 5 for another).
- Separate processes for product-related lists, customer-related lists, and "other" lists.
- These processes should also be scheduled to top up placeholders as users consume them.

### 08-03 Time and product filters

**Time filters.** Reusable filter definitions controlling the time window shown in charts/tables.

- Fill in an empty placeholder filter with a name and parameters defining the range.
- Example: "2 years history / 1 year future" expressed as a **rolling year** relative to the current period.
- Filters are not automatically published — a separate selection step controls which pages each filter is available on (can be set to "all places").
- A finalization process publishes the selection. Some documented errors during this process are expected for the training-model structure.

**Product filters.** Quick filters used by product page selectors.

- Defined by product properties (e.g. ABC classification, XYZ classification).
- Properties combine via **AND** / **OR** operators.
- Example: "A or B" classification AND "X" classification — yields only products meeting all criteria.

Confirmation on page **350 Demand Planning**: the new time filter restricts the displayed horizon (2y back / 1y forward) and the new product filter narrows the page selector to matching SKUs.

### 08-04 Baseline plan

Baseline configuration lives on **page 9 — Manage Scenarios**.

- Each scenario has a **selected baseline plan**. Default for all scenarios in the exercise is `System Forecast`.
- Other baseline options include: same as last year, upper/lower quantile from Plan IQ, and other statistical techniques.
- The baseline can be further **refined by product classification** (Smooth / Intermittent / Lumpy / Erratic — assigned in the Demand Analysis app).
  - Example policy: use statistical forecast for Smooth, Intermittent, Lumpy; for Erratic use "same as last year" (or zero) because the statistical forecast is not trusted for that class.
- Configuration goal: every scenario × classification combination has a sensible default baseline before users start planning.

Results flow through to page **350 Demand Planning**.

### 08-05 Manually adjusting the demand plan — perpetuation

Users can override the baseline either by:

- Entering an **absolute volume** (e.g. change 2,070 to 2,500), or
- Applying a **percentage uplift** (e.g. +20%).

**Perpetuation** is the key configuration parameter:

| Perpetuation | Behavior |
|---|---|
| **Yes** | Adjustment entered in one week carries forward into all future weeks until another change is made. Applies to both volume and % inputs. |
| **No** | Adjustment affects only the single week of input; later weeks revert to baseline. |

Perpetuation is a recurring configuration concept used in multiple places across the Demand & Supply Chain application.

## Key takeaways

- **Housekeeping is configuration.** Orphan deletion and placeholder creation should be part of the go-live checklist *and* scheduled processes — not a one-off task.
- **Filters are reusable assets** with two steps: define the filter, then publish to specific pages. Don't expect a new filter to appear everywhere automatically.
- **Baselines are a matrix**, not a single setting: (scenario) × (product classification) → baseline method. Match the method to the forecastability of the class — statistical methods only where they're trustworthy.
- **Perpetuation** is the single parameter that determines whether a manual override is a point edit or a forward-carrying assumption. Verify its setting before training planners, as the mental model differs significantly between the two modes.
- Product classification (Smooth / Intermittent / Lumpy / Erratic) originates in the **Demand Analysis** app and is consumed here — a concrete example of cross-app data flow within the Demand & Supply Chain suite.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Anaplan Demand & Supply Chain App training]]
- Prior chapter: Initializing Demand Planning Pt 1 (chapter 07)
- Related: Demand Analysis (origin of product classification), Scenario management, Page-based filters pattern
