---
title: 04 - Exploring and Configuring Demand Analysis
type: concept
tags: [anaplan, demand-supply-chain-app, demand-analysis]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/04.1 Exploring and Configuring Demand Analysis Captions.md
  - raw/docs/04.2 Exploring and Configuring Demand Analysis Captions.md
---

# 04 — Exploring and Configuring Demand Analysis

## Purpose

This chapter walks through the initial configuration of the **Demand Analysis** application after it has been initialized, connected to the Data Hub, and loaded with customer hierarchy, product hierarchy, and sales order history (covered in the prior chapter). The goal is to validate that the demand-analysis process is working end-to-end and to produce the cleansed baseline and derived metrics that downstream applications — **Statistical Forecasting** and **Demand Planning** — depend on.

Two functional areas are configured as representative examples:

1. **ABC / XYZ analysis** — segmentation of product and customer portfolios by importance (ABC, Pareto) and demand variability (XYZ).
2. **Seasonal profiles** — building a reusable library of seasonal indices.

By the end of the exercise the user should have validated demand analysis, committed the ABC/XYZ outputs as master data, and seeded the seasonal-profile library for use downstream.

## Steps covered

### Sub-video 04.1 — ABC/XYZ Segmentation

- **Page 320 — Product portfolio segmentation**
  - Initial state: chart not populated until the `Data for ABC` parameter is set.
  - Set parameter to `Selected History (U)` — `(U)` denotes **units / volumes** as the scoring basis.
  - After refresh, the Pareto chart and ABC/XYZ scoring populate (e.g. *Orange Juice Smooth 12-count 625ml* identified as largest product by volume).
  - Each product receives an **ABC** classification (importance) and an **XYZ** classification (demand volatility — X stable, Z volatile).
- **Page 900 — Global configuration**
  - Central location where the same parameters (including `Data for ABC`) can be reviewed and managed for the entire application.
- **Page 326 — Edit & Commit ABC** (product)
  - Distinguishes the **dynamically calculated** ABC value from the **saved** (committed) value used downstream.
  - Saved value can be manually overridden, then refreshed by running the commit **process**.
  - Process kicked off manually to persist the values as product master data.
- **Edit & Commit XYZ** (product)
  - Same pattern as ABC: review calculation, optionally override, run process to save.
- **Discussion — Automation vs governance**
  - Commit processes can be automated (e.g. nightly via **CloudWorks**).
  - However, ABC/XYZ scores feed **inventory policy** in Inventory Planning (an AX policy differs from a BX, etc.). Refreshing nightly can silently shift target inventory levels.
  - Therefore many implementations deliberately keep the commit step as a **governed, periodic review** rather than automating it.
- **Customer portfolio segmentation** (page 300 / page 340 area)
  - Same flow: confirm parameter is set to `Selected History (U)`, validate chart (e.g. Tesco identified as largest customer), run process to commit ABC.

### Sub-video 04.2 — Seasonal Profiles

- **Page 220 — Manage Seasonal Profiles**
  - Clear out leftover demo profiles first.
  - Purpose: maintain a **library of seasonal profiles** derived from history, available for downstream use (notably **new product launches** that have no history of their own).
- **Defining a profile**
  - Give the profile a name (e.g. `OJ Retail`).
  - Select the hierarchy levels at which to calculate the seasonality:
    - Customer level — e.g. Customer Level 2 = Grocery channel.
    - Product level — e.g. Product Level 3 = Orange Juice.
  - The application computes the seasonal index at the chosen hierarchy intersection and stores it in the library.
- The output (seasonal indices) is now available to downstream models.

### Optional exploration

Areas of Demand Analysis worth exploring after the core configuration:

- **Manage History — History Correction (page 132)** — outlier and anomaly identification / cleansing.
- **Product Chaining** — supersession relationships, so phasing out an old SKU and introducing a replacement still yields a consistent baseline.
- **Demand Classification** — alternative portfolio categorization based on demand behavior.

## Key takeaways

- Demand Analysis sits **upstream** of Statistical Forecasting and Demand Planning; its cleansed baseline and derived metrics (ABC/XYZ, seasonality) are the contract handed to those apps.
- Pages typically expose **functional parameters** locally; the same parameters are also centralized on the **global configuration page (900)**.
- The **calculated vs committed** pattern is pervasive: a dynamic calculation is visible on the page, but a deliberate **process run** is required to persist it as master data consumed downstream. This applies to both ABC and XYZ on products and customers.
- **Do not blindly automate commit processes.** Because ABC/XYZ feed inventory policy, governance over when scores change is often more valuable than freshness.
- **Seasonal profiles** are a *library*, not a single computation — define one profile per (customer-level × product-level) combination of interest. Particularly important for new-product-launch modelling downstream.
- The exercise also serves as a **validation checkpoint**: if data is flowing through from Data Hub and the pages calculate correctly, demand analysis is ready to hand off downstream.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Anaplan Demand & Supply Chain App]]
- See preceding chapter on initializing Demand Analysis and connecting the Data Hub.
- See downstream chapters on **Statistical Forecasting** and **Demand Planning**, which consume the cleansed baseline, ABC/XYZ master data, and seasonal-profile library produced here.
- Related concept: **CloudWorks** as the automation mechanism for nightly process runs (with the caveats above).
