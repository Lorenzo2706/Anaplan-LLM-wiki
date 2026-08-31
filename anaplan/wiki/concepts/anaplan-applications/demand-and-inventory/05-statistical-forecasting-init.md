---
title: Chapter 05 — Initializing Statistical Forecasting
type: concept
tags: [anaplan, demand-supply-chain-app, statistical-forecasting]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/05-01-Initializing Statistical Forecasting-Overview.md
  - raw/docs/05-02-Initializing Statistical Forecasting-Source Models.md
  - raw/docs/05-03-Initializing Statistical Forecasting-Time Settings and Ranges.md
  - raw/docs/05-04-Initializing Statistical Forecasting-Import Hierarchies and Data.md
  - raw/docs/05-05-Initializing Statistical Forecasting-Structural Configuration.md
---

# Chapter 05 — Initializing Statistical Forecasting

## Purpose

Stand up the **Statistical Forecasting** model/application so it can produce a usable baseline forecast for downstream demand planning. This mirrors the pattern used to initialize Demand Analysis (see [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary]]): wire up source models, align time, pull master data and transactional data from upstream models, then perform one structural configuration step that requires actual model edits (rather than parameter changes).

By the end of the exercise:

- Statistical Forecasting is connected to **Demand Analysis** and the **Data Hub**.
- Time settings and time ranges match Demand Analysis exactly.
- Product and customer hierarchies plus transactional data are loaded.
- A baseline forecast is being calculated (visible on the *Best Fit Analysis* page).
- Aggregate-level forecasting + disaggregation is configured at the chosen hierarchy level.

## Steps covered per sub-video

### 05-01 Overview

Sets the agenda. The Statistical Forecasting app follows the same initialization recipe as Demand Analysis:

1. Set source models.
2. Align time settings and time ranges.
3. Import hierarchies and data from the Data Hub / Demand Analysis.
4. Sense-check that a forecast is being produced.
5. Apply one structural configuration change related to **aggregate-level planning and disaggregation**.

### 05-02 Source Models

In the Statistical Forecasting model, edit the source-model mappings to point to:

- **Demand Analysis** model (via the *Demand Planning* connection / data management mapping).
- **Data Hub** model (the training-exercise data hub workspace).

After this, the Stat Forecasting model is "talking to the right models" and can receive imports.

### 05-03 Time Settings and Ranges

> [!important]
> Time settings and time ranges in Statistical Forecasting **must match Demand Analysis exactly**. Mismatches can silently prevent the forecast from being produced.

Settings used in the training exercise (FY25 current year):

| Setting | Value |
| --- | --- |
| Current year | FY25 |
| History | 3 years |
| Future | 1 year |

Time ranges:

| Range | Start | Length |
| --- | --- | --- |
| History range | FY22 | 4 years |
| Current-year-minus-one range | FY24 | 2 years |
| Future range | FY25 | 2 years |

Training-provisioned models may already have these set — confirm rather than re-enter blindly. Each range save triggers a recalc wait.

### 05-04 Import Hierarchies and Data

The import processes live on **Data Hub** application pages (same pattern as Demand Analysis initialization).

1. **Master data** — run the *product hierarchy update* and *customer hierarchy update* processes. These push hierarchies into Stat Forecasting.
2. **Transactional data** — on Data Hub page **212 — Update Transactional Data**, run the process. Note: this transactional data does **not** come from the Data Hub directly; it comes from **Demand Analysis**, because by that point it may have already been treated (training-period suppressions, outlier correction, etc.).

Once both finish, the Stat Forecasting model has hierarchies + cleaned demand data and should be calculating.

**Sense check:** open the *Best Fit Analysis* page in the Stat Forecasting application, pick a product/customer, and click through the available forecast methods (linear regression, seasonal models, etc.). Traditional time-series methods should show forecasts. **PlanIQ-backed methods will be empty** at this stage — that requires a later PlanIQ configuration step not covered here.

### 05-05 Structural Configuration (aggregate-level forecasting + disaggregation)

Context: the Stat Forecast independently produces a forecast at **every level** of the hierarchy. The high-level forecast is currently just the sum of leaf-level forecasts. Often a higher-level forecast is more accurate, and we want to **forecast at an aggregate level then disaggregate down**.

> [!note]
> This is one of the rare places where configuring the application requires **actual model changes** (formulas, Applies To), not just parameter edits. Configuration-guide documentation accompanies any such step. Skipping this step does not block later exercises.

Steps performed in the model:

1. **Module `FCT400`** — locate the two line items representing *level to disaggregate from* (one for customer, one for product). Set them to the desired aggregate level (training example: **product level 3** and **customer level 3**, i.e. one level up from leaf).
2. Replace their formulas with `PARENT ITEM(...)` against the leaf-hierarchy lists, e.g. `PARENT ITEM(hlp080 product leaf hierarchy)` and the customer-leaf equivalent. This derives the chosen parent from the leaf.
3. Clear formulas from three other related line items in `FCT400` — but **save them first** into the line item Notes field, they'll be re-introduced shortly.
4. On modules **`FCT200`** and **`FCT202`**, change *Applies To* to the new aggregate level (product L3, customer L3).
5. Back in `FCT400`, restore the saved formulas, adding `LOOKUP` calls onto the disaggregation-parent line items so the formula resolves correctly at the new Applies To.

Verification page: **Edit Final Forecast** in the app. For a chosen product/customer (e.g. *Orange Juice Smooth* in Tesco) the best-fit method is shown (e.g. linear regression). Toggling **Use Disaggregated Forecast** swaps the final forecast to the aggregate-then-disaggregate version.

**Automation:** the *Global Parameters* page exposes an option to **automatically** use the aggregate forecast when leaf-level demand variability is too high — i.e. when the leaf signal is too noisy to trust, fall back to a higher-level forecast pushed down.

## Key takeaways

- **Initialization recipe is consistent across apps**: source models → time → hierarchies → data → sense check. Same pattern as Demand Analysis.
- **Time alignment with Demand Analysis is non-negotiable** — mismatched current year / history / future settings can silently break the forecast.
- **Transactional data flows from Demand Analysis, not the Data Hub**, so that outlier correction and training-period suppressions are preserved.
- **Best Fit Analysis** is the go-to sense-check page after initialization. Empty PlanIQ methods are expected at this stage.
- **Configuration via parameters first, model edits only when necessary.** The aggregate-level disaggregation step is an intentional exception, fully documented in the configuration guide.
- **Aggregate-then-disaggregate forecasting** (`FCT400` + `FCT200`/`FCT202` Applies To + `PARENT ITEM` + `LOOKUP`) lets planners forecast at a more stable level and push results down — and the global parameter can switch to this automatically when leaf-level variability is high.
- **Stat Combination Model** exists as an alternative deployment for large/sparse hierarchies — product and customer are merged into a single combinations list instead of staying as independent dimensions. Watch for references to it in Data Hub pages.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Demand & Supply Chain App walkthrough]]
- Prior chapter: Demand Analysis initialization (same initialization pattern)
- Related concepts: `PARENT ITEM`, `LOOKUP`, Applies To, time ranges, hierarchies
- Downstream: Demand Planning consumes the baseline forecast produced here
