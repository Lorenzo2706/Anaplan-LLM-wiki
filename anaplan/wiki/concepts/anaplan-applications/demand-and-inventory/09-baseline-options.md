---
title: "09 - Exploring Other Baseline Options"
type: concept
tags: [anaplan, demand-supply-chain-app, demand-planning]
created: 2026-05-12
updated: 2026-07-08
sources:
  - raw/docs/09-01 Exploring Other Baseline Options - Overview.md
  - raw/docs/09-02 Exploring Other Baseline Options - Collaborative Planning.md
  - raw/docs/09-03 Exploring Other Baseline Options - Rate of Sale.md
  - raw/docs/09-04 Exploring Other Baseline Options - 2nd Tier Planning.md
---

# 09 - Exploring Other Baseline Options

## Purpose

Up to this point the Demand & Supply Chain training has built the demand-plan baseline almost exclusively from the statistical forecast. Exercise 09 broadens that view by walking through **three alternative baseline-generation techniques** that can sit alongside (or replace) the stat forecast for a given product/customer:

1. **Collaborative Planning** — building-block driver entry (foundation + growth + seasonality).
2. **Rate of Sale Planning** — store-count × average sales-per-store.
3. **2nd Tier Planning** — sell-in / sell-thru with retailer inventory targets.

The exercise has a dual focus: what each technique *does* from an end-user perspective, **and** — more importantly for model builders — the **configuration and implementation implications** of supporting each one. The end state is a demand planning page (page 350) where the user can pick any of these baselines as the working baseline, alongside the stat forecast and PlanIQ outputs.

## Steps covered per sub-video

### 09-02 Collaborative Planning (page 130)

Collaborative planning composes a plan from three independent building blocks the user enters in sequence:

| Building block | What it represents | Input |
|---|---|---|
| **Foundation** | Underlying average weekly sales / demand | e.g. 2,500 units/week from start of July |
| **Organic growth** | Anticipated % growth on top of foundation | Growth rate + effective date |
| **Seasonal curve** | Overlay of a seasonality profile | Pick from the seasonality library built earlier in training |

Steps:

1. On page 130, add a planning input row, pick **input type = Foundation**, set an effective date, enter the value, tick *Effective*.
2. Refresh; a new empty input row appears. Repeat for **Organic growth**.
3. Refresh again; add a **Seasonal curve** row and pick a curve (e.g. *Organic Juice Grocery*) from the seasonality library.
4. Optionally add further rows — e.g. an **inorganic step change** to the foundation at a future date (e.g. early 2026) — to model step changes in baseline.
5. Go to **page 350 (Demand Planning)** and select *Collaborative Plan* as the alternative baseline; the composed plan flows through.

**Configuration implication:** the planning input rows are driven by **empty placeholder list items** (see empty placeholders pattern from an earlier exercise). The implementation must ensure these placeholders are seeded and continually replenished as users consume them.

### 09-03 Rate of Sale Planning (page 120)

A simple two-driver multiplicative model aimed at consumer-goods companies selling into retail:

```
Planned demand = Store count × Rate of sale (avg weekly sales per store)
```

Steps:

1. On page 120, enter **rate of sale** (e.g. 25 units/store/week) and **store count** (e.g. 100 stores). Inputs persist and can be edited going forward (e.g. when retailer expands listings).
2. Go to page 350 to select *Rate of Sale Plan* as a baseline.

**Optional/advanced configuration — statistically forecasted rate of sale:**

Instead of pure direct entry, rate of sale itself can be the output of statistical forecasting, with the direct-entry inputs acting as **overrides** on top. To enable this, two pieces must be in place:

1. **Capture historic store count** — the page exposes a table to enter store count history (e.g. 80 stores from week 17 FY24, 90 stores a few weeks later). Historic rate of sale is then derived as `historic demand / historic store count`.
2. **Signal the stat forecast engine to use rate-of-sale data**, not total volumes. This is configured in the **Demand Analysis** application on the page that selects, per product/customer combination, the input data series fed into stat forecasting. Defaults are *Collected History* (output of product training + history collection); the user can switch to a **rate-of-sale data series** so the forecast returns a rate-of-sale figure rather than a volume.

### 09-04 2nd Tier Planning (pages 910 and 124)

The "sell-in / sell-thru" approach. Planning happens at a level **more granular than the standard customer leaf** — at "second tier" sub-customers (e.g. store formats) hanging off a parent customer.

Steps:

1. **Page 910 — Manage Second Tier**: pick a parent customer, then name new second-tier customers against empty placeholder children (e.g. *Supermarket format*, *Convenience format*). Refresh between entries.
2. **Page 124 — Commercial Planning, Second Tier**: with the granular customer selected, capture three inputs over time:
   - **Sell-thru forecast** — what the retailer is expected to sell to its consumers.
   - **Opening inventory** — inventory the retailer currently holds of the product.
   - **Target inventory level** — mutually agreed inventory the retailer should carry.
3. The app back-calculates the **sell-in forecast** = what must be sold *into* the retailer to satisfy sell-thru while moving inventory toward target.
4. On page 350, select the resulting sell-in series as the baseline. A comparison view shows all baselines side-by-side (collaborative, rate-of-sale, sell-in/sell-thru, stat forecast, prior year, PlanIQ variants).

**Configuration implications:**

- **Empty placeholders** again — second-tier customers are placeholder children of the standard customer hierarchy and must be seeded/replenished.
- **Data import is hand-crafted.** Unlike most areas of the app, there is **no pre-built import template/action** for sell-thru and opening-inventory data. The rationale: this data comes from retailer collaboration and arrives in whatever format the retailer provides, so import actions must be built ad hoc per implementation.

Final housekeeping note: reset the baseline / clear any ad-hoc adjustments before moving on.

## Key takeaways

- The demand baseline is not just "the stat forecast" — Demand & Supply Chain ships **four+ alternative baseline sources** (collaborative, rate-of-sale, sell-in/sell-thru, stat forecast, prior year, PlanIQ outputs), all selectable on page 350.
- **Empty placeholder list items** are the recurring configuration pattern enabling user-defined planning rows (collaborative blocks, second-tier customers). Seeding *and* ongoing replenishment of these placeholders is a must-have implementation task.
- **Collaborative planning** decomposes a plan into foundation + organic growth + seasonality + (optional) step changes, each effective-dated and independently editable.
- **Rate-of-sale planning** can be pure direct-entry (store count × rate) *or* upgraded to a stat-forecasted rate of sale; the upgrade requires historic store-count capture and rerouting the stat-forecast input series in the Demand Analysis app.
- **2nd tier planning** operates one level below the standard customer leaf and uses retailer sell-thru, opening inventory, and target inventory to back-derive sell-in. It is the one area where **import actions must be custom-built** per implementation because of retailer-format variability.
- A side-by-side baseline comparison view exists on page 350 to evaluate techniques against each other before committing to one.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary]]
- Related exercises:
  - Statistical forecasting (precedes this exercise)
  - Seasonality library exercise (provides the curves consumed by Collaborative Planning)
  - Product training & history collection (feeds *Collected History* used by Demand Analysis input-selection)
- Concepts touched:
  - Empty placeholder list items
  - DISCO (these are predominantly **Input** modules feeding **Calculation** modules that emit candidate baselines to **Output**/planning pages)
  - Customer hierarchy and sub-leaf granularity (2nd tier)
