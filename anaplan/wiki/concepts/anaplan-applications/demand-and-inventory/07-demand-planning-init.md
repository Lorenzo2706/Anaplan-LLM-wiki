---
title: "Chapter 07 — Initializing Demand Planning"
type: concept
tags: [anaplan, demand-supply-chain-app, demand-planning]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/07-01 Initializing Demand Planning-Overview.md
  - raw/docs/07-02 Initializing Demand Planning-Set Source Models and Time Settings.md
  - raw/docs/07-03 Initializing Demand Planning-Import Hierarchies.md
  - raw/docs/07-04 Initializing Demand Planning-Import Data.md
---

# Chapter 07 — Initializing Demand Planning

## Purpose

Stand up the **Demand Planning** model so it is ready for use as the central planning workspace in the Demand & Supply Chain application suite. Demand Planning is downstream of three feeder models — the **Data Hub**, **Demand Analysis**, and **Statistical Forecasting** — and consolidates their outputs into a single plannable view.

The initialization mirrors the setup performed earlier for Demand Analysis and Statistical Forecasting: configure source-model connections, align time settings, import hierarchies, and finally pull in transactional and derived data. Most steps are performed via the **UX**; only source models and time settings require touching the underlying model.

See [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary]] for the broader course context.

## Steps covered per sub-video

### 07-01 — Overview

- Demand Planning reuses the same setup pattern as the upstream models: time settings, hierarchy levels, source-model connections.
- After the basics are in place, hierarchies and data are pulled in from the Data Hub, Demand Analysis, and Statistical Forecasting.
- Introduces the concept of **hierarchy reconciliation** — keeping hierarchies in sync between source and downstream models without full delete/reload processes.
- End state: Demand Planning is operational and verifiable from its initial UX pages.

### 07-02 — Set Source Models and Time Settings

Performed inside the **underlying Demand Planning model** (the only non-UX work in the chapter).

**Source model connections** to configure:

| Connection | Target model |
|---|---|
| Data Hub | Training exercise Data Hub |
| Statistical Forecasting | Stat Forecast |
| Stat Combination | *(skipped — not used in this exercise)* |
| Demand Analysis | Demand Analysis |
| Reporting | Reporting Model (referenced by some processes) |

**Time settings:**

- Current year: **FY25**
- History: **3 years**
- Future: **1 year**
- No **time ranges** are used in the Demand Planning application, so none need to be defined.

### 07-03 — Import Hierarchies

**Hierarchy reconciliation parameter** — controls how downstream hierarchies stay in sync when the Data Hub refreshes:

- **Update only** — always applied (renames flow through).
- **Insert only** — always applied (new members added).
- **Delete** — *optional*; this is the only behavior the parameter actually toggles.

| Option | Behavior on members missing from the source |
|---|---|
| Update + Insert + Delete | Removed in downstream model (mirror of source). Typical choice when the source is a full refresh. |
| Update + Insert | Retained in downstream model. Use when the source feed is incremental and not a full snapshot. |

Most implementations use **Update + Insert + Delete**, assuming the source system delivers a full hierarchy refresh.

**Execution:**

1. Set the reconciliation parameter on the **Global Parameters** page if not already configured.
2. From the **Update Data** page in Demand Planning, run the combined hierarchy import process (handles Product, Customer, and Location together — Locations not yet present in the exercise).
3. Verify by inspecting the **Product** and **Customer** lists in the underlying model — the juices/smoothies products and the retail/other-channel customers from the Data Hub should now be present, replacing any earlier demo data.

> [!note]
> The hierarchy refresh process for Demand Planning is **owned by the Data Hub**, same pattern used to refresh Demand Analysis and Stat Forecast.

### 07-04 — Import Data

Data sets pulled into Demand Planning by source:

**From the Data Hub:**
- Demand history (the pure, original history)
- Current period flag
- Open orders (if present in sales history)
- Optional: budget (for comparison), marketing plan (top-down seeding), contracted customer demand, constrained supply

**From Demand Analysis:**
- **Corrected and chained history** (output of history collection / training)
- **Seasonal profiles** (e.g. for NPI use cases)
- Product/customer metrics: **ABC/XYZ scoring**, product classification, etc.

**From Statistical Forecasting:**
- The **statistical forecast** itself
- Forecast accuracy / **back-test scores**
- History window used by Stat Forecast
- **Best-fit method** selected per series

**Execution sequence (from the UX):**

1. **Data Hub → Demand Planning** — run *Update All Demand Transactions* on the Data Hub application.
2. **Demand Analysis → Demand Planning** — page **236DP**, run the import process.
3. **Statistical Forecasting → Demand Planning** — page **238**, run *Update System Forecasting*.

**Verification:** open page **350 Demand Planning** — the heart of the application. Confirm:

- Hierarchies populated (products, customers).
- **Corrected History** column populated (Demand Analysis connection working).
- **Baseline Plan** populated, sourced from the system forecast (Stat Forecast connection working).

## Key takeaways

- Demand Planning is a **consumer model**: its initialization is mostly about wiring it correctly to three upstream models, not building new logic.
- Only **source model connections** and **time settings** require working in the underlying model — everything else is run from the UX.
- **Hierarchy reconciliation** abstracts away delete/reload cycles. The choice of *Update+Insert* vs *Update+Insert+Delete* hinges on whether the source feed is a full refresh or an incremental update.
- The hierarchy refresh processes live in and are **owned by the Data Hub**, even though they target downstream models.
- The three data-import processes (Data Hub, Demand Analysis, Stat Forecast) must be run **after** hierarchies are in place, otherwise transactions would have no members to attach to.
- Page **350 Demand Planning** is the canonical smoke test for a healthy initialization — if Corrected History and Baseline Plan both populate, all three source connections are working.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Demand & Supply Chain App course]]
- Previous chapters in the demand-and-inventory series (Demand Analysis, Statistical Forecasting initializations) follow the same pattern.
- Related concepts: hierarchy reconciliation, source model connections, time settings, Data Hub spoke pattern.
