---
title: Anaplan Demand & Inventory Reference App — Configuration Curriculum
type: concept
tags: [anaplan, demand-supply-chain-app, index]
created: 2026-05-12
updated: 2026-07-08
sources: [wiki/sources/2026-05-12-anaplan-demand-supply-chain-app.md]
---

# Anaplan Demand & Inventory Reference App — Configuration Curriculum

Walkthrough of how the Anaplan-built Demand Planning + Supply/Inventory reference applications are initialized and configured end-to-end. Not tied to any current build — kept as durable reference for future S&OP / demand / inventory work.

Source: [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|2026-05-12 Demand & SC App video transcripts]]

## Chapters

### Foundations
- [[01-data-hub]] — Initializing the Data Hub (mass delete, time, hierarchies, currency, properties)

### Demand Analysis
- [[03-demand-analysis-init]] — Source models, time, hierarchy clear, demand-history imports
- [[04-demand-analysis-config]] — ABC/XYZ segmentation + seasonal-profile library

### Statistical Forecasting
- [[05-statistical-forecasting-init]] — Source-model wiring, time alignment, structural config
- [[06-statistical-forecasting-config]] — Coefficients, back-testing (RMSE best-fit), method utilization

### Demand Planning
- [[07-demand-planning-init]] — Source models, hierarchies, data imports
- [[08-demand-planning-pt2]] — List management, time/product filters, baseline plan, manual adjustments
- [[09-baseline-options]] — Collaborative planning, rate-of-sale, 2nd-tier planning
- [[10-financialization]] — Bringing price into the DP, line-item formatting
- [[11-events]] — Temporary products, NPI, cannibalization, replacements

### Reporting
- [[12-reporting-archiving]] — Reporting model init + plan archiving (manual + auto)

### Inventory / Supply
- [[14-inventory-data]] — Inventory + PO import, transfer to Supply Planning, forecast consumption
- [[15-inventory-policies]] — ABC×XYZ per-DC segmentation → policy mapping
- [[16-network]] — Sites, lanes, lead times, tiered plan review
- [[17-inventory-reporting]] — Alerting, aging, remaining shelf life, auto-expiry

> [!note] Extended chapters
> Chapters 14–17 each have a companion `-detailed` page with deeper formula/config notes generated during the original ingest. Chapter 02 (video skipped) and chapter 13 (not transcribed) are absent by design.
>
> Detailed companion pages: [[14-inventory-data-detailed]], [[15-inventory-policies-detailed]], [[16-network-detailed]], [[17-inventory-reporting-detailed]]
