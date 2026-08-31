---
title: "Chapter 03 — Initializing Demand Analysis"
type: concept
tags: [anaplan, demand-supply-chain-app, demand-analysis]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/03.1 Initializing Demand Analysis Captions.md
  - raw/docs/03.2 Initializing Demand Analysis.md
---

# Chapter 03 — Initializing Demand Analysis

## Purpose

This is the first exercise where data flows **out of the Data Hub into a downstream consumption model** — the Demand Analysis model and its corresponding application. The goal is to:

- Stand up Demand Analysis so its functionality "comes to life".
- Connect it to the Data Hub via source-model mappings.
- Bring across product/customer hierarchies and demand history.
- Confirm the model is analyzing data and is ready to feed further downstream models (statistical forecasting, demand planning).

The exercise is split across two sub-videos: **03.1** covers underlying-model setup (source models + time), **03.2** covers clearing demo hierarchies, importing real hierarchies/data from the Data Hub, and final verification.

## Steps covered

### 03.1 — Underlying-model setup

1. **Open the underlying Demand Analysis model** (`Training Exercise - Demand Analysis`), not the application.
2. **Set source models** so that import actions targeting other models re-point to the correct instances:
   - Data Hub source → `Training Exercise - Data Hub` (in the `Product Management 2` workspace).
   - Statistical Forecasting source → the training stat-forecasting model.
   - Demand Planning source → `Training Exercise - Demand Planning`.
   - Stat-combinations / reporting mappings can be skipped.
3. **Time settings — model calendar**:
   - Current Fiscal Year: **FY25**.
   - History: **3 years**.
   - Future: **1 year**.
4. **Time ranges**:
   - *Future time range*: start **FY25**, **2 years** (two periods into the future).
   - *Forecast/long time range*: start **FY25**, **5 years**.
   - Caveat: editing an existing time range can silently un-tick the **Total of All Periods** aggregation — re-tick it after editing or downstream calculations break.
5. Copies of the training model may already have correct settings — check before editing.

### 03.2 — Clear demo data, import from Data Hub, verify

1. **Clear demo product & customer hierarchies** in the underlying model:
   - Run process **`P215 Master Link Process`** (a "Delete Process - All" wrapper).
   - Takes a couple of minutes; wipes the demo Hollyoaks-style content from product and customer lists.
   - Alternative approach (covered in a later exercise): use the Data Hub sync imports themselves to keep target lists in lock-step, instead of a hard delete.
2. **Switch to the Data Hub application** — the imports that *push* hierarchies and data into Demand Analysis live under the Data Hub app's **Export to Demand Analysis** section (page `202 DA`).
3. **Import hierarchies** (products + customers) via the single combined process.
   - Expected non-blocking error: a customer-properties import complains about the default-currency property because `P215` deleted the currency list inside Demand Analysis. Safe to ignore for this training — that property is not required downstream.
4. **Import demand transactions** (sales-order history that Chapter 02 loaded into the Data Hub). The same process also carries across the **Current Period** setting derived in the Data Hub, so Demand Analysis inherits the correct "today".
5. **Verify** on page **`212`** in the Demand Analysis application:
   - Product hierarchy populated (fruit-juice product tree).
   - Customer hierarchy populated (retailers / retail channels).
   - Chart shows demand data for a product/customer combination and at higher aggregations.
   - Some statistical measures already auto-calculate — confirms the model is live.

## Key takeaways

- **Source-model mappings are the wiring** that lets a target model's import actions reach the correct Data Hub / forecast / planning model in a given workspace. They must be set on every fresh copy of the model.
- **Two strategies for refreshing a list from the Data Hub**:
  - Hard delete via a `P215`-style master process, then re-import (used here).
  - Continuous sync via standard import actions (covered later) — keeps Data Hub and target perfectly aligned without nuking lists.
- **Editing a time range can drop the "Total of All Periods" aggregation** silently — always re-check this checkbox after edits.
- **The Current Period flows from Data Hub to Demand Analysis** as a side-effect of the demand-transactions import — no separate action needed.
- **The Data Hub application owns the export-to-spoke processes**, not the spoke model's application. Conceptually: Data Hub *pushes* to consumption models.
- A non-blocking import error on a deleted property (currency) is acceptable when the property isn't used downstream; not every red banner is a real problem.

## Sequence summary

| # | Where | Action |
|---|-------|--------|
| 1 | Demand Analysis (model) | Set source models (Data Hub, Stat Forecasting, Demand Planning) |
| 2 | Demand Analysis (model) | Set model calendar: FY25, 3y history, 1y future |
| 3 | Demand Analysis (model) | Set time ranges: future (FY25, 2y), long (FY25, 5y); re-tick Total of All Periods |
| 4 | Demand Analysis (model) | Run `P215 Master Link Process` to clear demo product/customer hierarchies |
| 5 | Data Hub (app, page `202 DA`) | Run combined products + customers hierarchy import |
| 6 | Data Hub (app, page `202 DA`) | Run demand-transactions import (also carries Current Period) |
| 7 | Demand Analysis (app, page `212`) | Visually confirm hierarchies, data, and stat measures |

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Demand & Supply Chain App training]]
- Related concepts to expand later: source-model mappings, model calendar vs time ranges, Data Hub spoke imports, `P215` master delete pattern.
