---
title: Anaplan Demand & Inventory Reference App — Video Transcripts
type: source
tags: [anaplan, demand-supply-chain-app, training]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/01-01 Initializing Data Hub - Overview.md
  - raw/docs/01-02 Initializing Data Hub - Run Mass Delete.md
  - raw/docs/01-03 Initializing Data Hub - Time Settings and Ranges.md
  - raw/docs/01-04 Initializing Data Hub - Import and Hierarchies.md
  - raw/docs/01-05 Initializing Data Hub - Import Currency List.md
  - raw/docs/01-06 Initializing Data Hub - Import Properties.md
  - raw/docs/03.1 Initializing Demand Analysis Captions.md
  - raw/docs/03.2 Initializing Demand Analysis.md
  - raw/docs/04.1 Exploring and Configuring Demand Analysis Captions.md
  - raw/docs/04.2 Exploring and Configuring Demand Analysis Captions.md
  - raw/docs/05-01-Initializing Statistical Forecasting-Overview.md
  - raw/docs/05-02-Initializing Statistical Forecasting-Source Models.md
  - raw/docs/05-03-Initializing Statistical Forecasting-Time Settings and Ranges.md
  - raw/docs/05-04-Initializing Statistical Forecasting-Import Hierarchies and Data.md
  - raw/docs/05-05-Initializing Statistical Forecasting-Structural Configuration.md
  - raw/docs/06-01 Configuring and Exploring Statistical Forecasting-Overview.md
  - raw/docs/06-02 Configuring and Exploring Statistical Forecasting-Coefficients.md
  - raw/docs/06-03 Configuring and Exploring Statistical Forecasting-Back-testing.md
  - raw/docs/06-04 Configuring and Exploring Statistical Forecasting-method utilization.md
  - raw/docs/07-01 Initializing Demand Planning-Overview.md
  - raw/docs/07-02 Initializing Demand Planning-Set Source Models and Time Settings.md
  - raw/docs/07-03 Initializing Demand Planning-Import Hierarchies.md
  - raw/docs/07-04 Initializing Demand Planning-Import Data.md
  - raw/docs/08-01 Initializing Demand Planning Pt2-overview.md
  - raw/docs/08-02 Initializing Demand Planning Pt2-List Management Options.md
  - raw/docs/08-03 Initializing Demand Planning Pt2-time and product filters.md
  - raw/docs/08-04 Initializing Demand Planning Pt2-baseline plan.md
  - raw/docs/08-05 Initializing Demand Planning Pt2-manually adjust DP.md
  - raw/docs/09-01 Exploring Other Baseline Options - Overview.md
  - raw/docs/09-02 Exploring Other Baseline Options - Collaborative Planning.md
  - raw/docs/09-03 Exploring Other Baseline Options - Rate of Sale.md
  - raw/docs/09-04 Exploring Other Baseline Options - 2nd Tier Planning.md
  - raw/docs/10-01 Financialization of the Demand Plan-overview.md
  - raw/docs/10-02 Financialization of the Demand Plan-data hub.md
  - raw/docs/10-03 Financialization of the Demand Plan-DP model plan.md
  - raw/docs/10-04 Financialization of the Demand Plan-price adjustments.md
  - raw/docs/10-05 Financialization of the Demand Plan-line item formatting.md
  - raw/docs/11-01 Overlaying Events onto the Demand Baseline-Overview.md
  - raw/docs/11-02 Overlaying Events onto the Demand Baseline-Create a Temporary Product.md
  - raw/docs/11-03 Overlaying Events onto the Demand Baseline-NPI.md
  - raw/docs/11-04 Overlaying Events onto the Demand Baseline-Caniballization.md
  - raw/docs/11-05 Overlaying Events onto the Demand Baseline-Temporary Product Replacements.md
  - raw/docs/12-01 Initializing reporting model and archiving plans-overview.md
  - raw/docs/12-02 Initializing reporting model and archiving plans-model settings.md
  - raw/docs/12-03 Initializing reporting model and archiving plans-hierarchies and data.md
  - raw/docs/12-04 Initializing reporting model and archiving plans-creating an archive.md
  - raw/docs/12-05 Initializing reporting model and archiving plans-auto archiving.md
  - raw/docs/14-01 Importing and managing the inventory data-overview.md
  - raw/docs/14-02 Importing and managing the inventory data-import inventory and po data.md
  - raw/docs/14-03 Importing and managing the inventory data-move data to supply planning model.md
  - raw/docs/14-04 Importing and managing the inventory data-review data.md
  - raw/docs/14-05 Importing and managing the inventory data-confirm forecast consumption.md
  - raw/docs/15-01 Managing inventory policies-Overview.md
  - raw/docs/15-02 Managing inventory policies-Create a test inventory policy.md
  - raw/docs/15-03 Managing inventory policies-ABCXYZ.md
  - raw/docs/15-04 Managing inventory policies-set policies.md
  - raw/docs/15-05 Managing inventory policies-inventory policies.md
  - raw/docs/16 Configuring a Network.md
  - raw/docs/17-01 Inventory reporting-overview.md
  - raw/docs/17-02 Inventory reporting-alerting report.md
  - raw/docs/17-03 Inventory reporting-inventory aging report.md
  - raw/docs/17-04 Inventory reporting-remaining shelflife report.md
  - raw/docs/17-05 Inventory reporting-auto expiry.md
---

# Anaplan Demand & Inventory Reference App — Video Transcripts

## What this is
Transcribed walkthrough videos showing the end-to-end configuration of Anaplan's reference applications for **Demand Planning** and **Inventory / Supply Planning**: Data Hub → Demand Analysis → Statistical Forecasting → Demand Planning (incl. financialization, events) → Reporting/Archiving → Inventory data → Inventory Policies → Network → Inventory Reporting.

## Why it's in the wiki
Not tied to any active model. Kept as durable reference for future S&OP, demand-planning, or inventory work — captures the structure, action IDs, page numbers, and configuration choices that the Anaplan reference apps assume.

## Scope notes
- Curriculum chapters present: 01, 03–12, 14–17 (all 17-xx sub-videos present after 2026-05-12 follow-up ingest of 17-04). Chapters 02 and 13 are not available as transcripts and will not be ingested.
- Raw filenames have inconsistent casing/separators (e.g. `01-01`, `03.1`, `05-01-...`, `16 Configuring a Network.md`).
- Engine: the reference apps target Anaplan Classic. No engine-specific call-outs given in the videos.

## Wiki output
All chapter pages live under [[wiki/concepts/anaplan-applications/demand-and-inventory/index|concepts/anaplan-applications/demand-and-inventory/]]. See that index for the per-chapter pages.

## Highlights worth remembering
- **Data Hub is the single point of truth** for hierarchies, time, currency, and properties — every downstream model imports from it (chapter 01).
- **ABC/XYZ segmentation** drives both demand-analysis governance (ch. 04) and inventory-policy selection (ch. 15) — same conceptual lever, applied in two places.
- **Best-fit forecasting** uses back-testing with RMSE across configurable alpha/beta coefficient grids, offsets, period sums, and number-of-tests (ch. 06). PlanIQ requires plan archives to function.
- **Events overlay** (ch. 11) is the standard pattern for NPI, cannibalization, and temporary products — uses placeholder/temporary product items.
- **Inventory policies** are mapped from ABC×XYZ segments per DC, with replenishment parameters layered on top (ch. 15).
- **Network** modeling uses sites + lanes + lead times, with multi-tier extension via versions (ch. 16).
