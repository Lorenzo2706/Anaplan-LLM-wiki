---
title: Chapter 10 - Financialization of the Demand Plan
type: concept
tags: [anaplan, demand-supply-chain-app, demand-planning, financialization]
created: 2026-05-12
updated: 2026-07-08
sources:
  - raw/docs/10-01 Financialization of the Demand Plan-overview.md
  - raw/docs/10-02 Financialization of the Demand Plan-data hub.md
  - raw/docs/10-03 Financialization of the Demand Plan-DP model plan.md
  - raw/docs/10-04 Financialization of the Demand Plan-price adjustments.md
  - raw/docs/10-05 Financialization of the Demand Plan-line item formatting.md
---

# Chapter 10 — Financialization of the Demand Plan

## Purpose

Up to this point the Demand Planning model has expressed demand purely in **units**. Chapter 10 converts that unit-based plan into **monetary terms** — revenue, cost of sales, and gross profit / contribution — so that the demand plan can be consumed by Finance and used for value-based decisions.

To achieve this the exercise:

- Brings **sales prices** and **standard unit costs** into the Data Hub.
- Transfers that pricing and costing reference data into the Demand Planning model.
- Multiplies prices and costs against the unit demand to produce revenue, total cost, and gross profit line items.
- Provides planners with the ability to **adjust prices** (permanent overrides and temporary uplifts) inside the planning process.
- Notes a small UX/formatting consideration around currency symbols on line item formats.

## Steps covered per sub-video

### 10-01 — Overview

- Goal: convert the demand plan from volumes into values (revenue, cost of sales, gross profit).
- High-level workflow:
  1. Import a **sales price** file into the Data Hub.
  2. Import a **unit (standard) cost** file into the Data Hub.
  3. Review the imported pricing/costing data in the Data Hub.
  4. Transfer pricing and costing across to the Demand Planning model.
  5. Confirm that unit volumes are now monetized in Demand Planning.
  6. Use planning pages to **override** or **uplift** prices/values.

### 10-02 — Data Hub imports

- Performed from Data Hub **page 108**, which centralizes the management of imports into the hub.
- Two key actions/processes are run:
  - **Update System Commercial Pricing** — imports `system commercial pricing.csv` from the Exercise 10 data folder.
  - **Product Standard Cost** process — imports the corresponding unit cost CSV.
- Data Hub **page 516** is used to review the loaded pricing and standard cost:
  - **Sales price** is held at the **Product × Customer** level (example: 14.50 GBP), with **effective dates** so price history and future price changes can both be captured.
  - An adjacent table for **product-level pricing** (without customer dimension) exists but was not loaded in this exercise. This is the alternative granularity used when prices are set per product only — a separate template and import action would be used.
  - **Standard cost** is held at the **Product** level (example: 16.20 GBP), also with effective dates supporting historical and forward-looking cost changes.

### 10-03 — Transfer to the DP model

- The hub-to-spoke transfer is managed from Data Hub **page 230**, which contains the actions controlling data flow into the Demand Planning model.
- A single process runs **both** the pricing and costing transfers at once.
- Validation is done on Demand Planning **page 350** (main DP page). Scrolling down reveals new sections:
  - **Sales price** and the resulting **Revenue** (price × volume).
  - **Standard cost**, the resulting **Total Cost**, and **Contribution / Gross Profit**.

### 10-04 — Price adjustments in planning

- Planners adjust pricing on Demand Planning **page 304**, within the **Financial Assumptions** section.
- Two adjustment mechanisms are provided:
  1. **Price change (override)** — a hard override that becomes the new enduring price from a given week onward (e.g. "from week 27 the price becomes 16.00" — perpetuating).
  2. **Temporary price uplift** — a **percentage** change applied for a **fixed number of periods**, after which price reverts to the latest permanent price.
- On DP page 350, after adjustments are entered, the planner can see, side by side:
  - Original imported price.
  - Permanent price change.
  - Temporary uplift (applied for the specified number of weeks — e.g. six — before dropping back to the new permanent price).
  - The final blended price that is multiplied against volumes.
- Recap: the full pattern is **standard templates → Data Hub → transfer to DP app → planner-driven adjustments**.

### 10-05 — Line item formatting (currency symbol)

- All financial line items default to a `$` prefix in their number format.
- There is no global toggle — the symbol comes from each line item's **format** setting.
- Recommended bulk approach:
  1. Open the model's full line item inventory (blueprint view of all line items).
  2. Select and copy the **Format** column into Excel.
  3. Perform a bulk **find & replace** to swap the dollar symbol for the desired currency.
  4. Paste the updated formats back into the blueprint.

## Key takeaways

- **Volume → Value conversion is the headline outcome** of Chapter 10. The plan is no longer just units — it now produces revenue, total cost, and gross profit.
- **Pricing structure matters**: this exercise loads Product × Customer prices, but the model supports a Product-only pricing structure via a different template/action. Choose the granularity that matches the business reality.
- **Effective dates** on both prices and costs are first-class — the same record set captures historical evolution and forward-looking changes, which is essential for time-phased revenue/cost calculations.
- **Data Hub is the single point of import** for commercial reference data; the DP model never imports the raw CSVs directly. This keeps the hub-and-spoke discipline intact (see Data Hub architecture if present).
- **Planner control is layered, not destructive**: imported price is preserved; permanent overrides and temporary % uplifts sit on top. The final applied price is computed downstream, so the audit trail back to the source price stays intact.
- **Temporary uplifts have an explicit duration** (number of periods) — they are not open-ended adjustments. After the window, the price drops back to the latest permanent price, not the original.
- **Currency formatting is a per-line-item concern**, not a model-level setting. The blueprint bulk edit via Excel is the practical workaround.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Demand & Supply Chain app walkthrough]]
- Previous chapter: demand plan in units (chapters 1–9 of the same walkthrough).
- Related concepts: effective-dated reference data, hub-and-spoke transfers, planner override patterns, [[wiki/concepts/anaplan concepts/10_line-item|Line items]] and their format property.
