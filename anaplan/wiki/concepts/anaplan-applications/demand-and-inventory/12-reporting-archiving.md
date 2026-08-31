---
title: "Chapter 12 — Initializing the Reporting Model and Archiving Plans"
type: concept
tags: [anaplan, demand-supply-chain-app, reporting, archiving]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/12-01 Initializing reporting model and archiving plans-overview.md
  - raw/docs/12-02 Initializing reporting model and archiving plans-model settings.md
  - raw/docs/12-03 Initializing reporting model and archiving plans-hierarchies and data.md
  - raw/docs/12-04 Initializing reporting model and archiving plans-creating an archive.md
  - raw/docs/12-05 Initializing reporting model and archiving plans-auto archiving.md
---

# Chapter 12 — Initializing the Reporting Model and Archiving Plans

## Purpose

Final exercise of the demand planning track. The **reporting model** is a dedicated model in the architecture that stores **archived snapshots** of the demand plan. These snapshots are the basis for downstream reporting such as **forecast accuracy** and **waterfall analysis**. This chapter covers:

1. Standing up the reporting model from scratch (source connections, time, ranges, hierarchies, history).
2. Creating an archive (snapshot) of the demand plan.
3. Deciding whether to automate archiving or run it as a manual step.

## Steps covered

### 12-01 Overview

High-level walkthrough of the exercise. Tasks, in order:

- Point the reporting model at the correct **source models** (Data Hub, Demand Analysis, Demand Planning, Supply Planning).
- Configure **time settings** and **time ranges**.
- Seed it with **product/customer hierarchies** and **demand history**.
- Synchronize with the Demand Planning model (current period, scenarios).
- Create the first archive and verify it.

### 12-02 Model settings

Performed inside the reporting model itself.

- **Source model connections** — set Data Hub, Demand Analysis, Demand Planning, plus the two Supply Planning connections.
- **Time settings** — current year **FY25**, **3 years history**, **1 year future**.
- **Time range "Future"** — start **FY25**, length **2 periods**.
  - Watchout: tick **"Retain the total of all periods"** boolean before saving, or the save fails.

### 12-03 Hierarchies and data

Performed from the **Data Hub** application, section **216 – Export to Reporting**.

- Run **Update All Hierarchies** process — pulls product and customer hierarchies into the reporting model. (A location-hierarchy error appears but is safe to ignore for this exercise.)
- Run **Update Selected History** process (top-right of same page) — pulls sales-order / demand history from Data Hub into the reporting model.

At this point the reporting model is fully seeded.

### 12-04 Creating an archive

Done from the **Demand Planning** application, page **990 – Manage Archiving**.

1. **Synchronize reporting model with demand planning:**
   - Update Current Period (e.g. Week 17, FY25).
   - Update Scenarios (aligns the scenario list).
2. **Define archive scope:**
   - **Name** — accept the pre-populated default or override.
   - **Time horizon** — archive the entire future, or a subset (e.g. next 52 weeks).
   - **Reporting subsets** — flag whether this archive is included in the **Waterfall** and **Forecast Accuracy** subsets. Useful when multiple archives are taken in a cycle and only one should drive reporting.
   - **Scenario selection** — pick which scenarios to include (may be a subset of all demand-planning scenarios).
3. **Create the archive** — runs the action.
4. **Verify** in the reports area (e.g. Waterfall Analysis page) — the new snapshot (e.g. `Week 17, FY25, v2`) should appear with data.
   - Note: default page filters may hide columns beyond the current week. Clear or extend the filter to see archived future data.

### 12-05 Auto archiving

Same Manage Archiving page, scroll to the bottom: configure the **scope of scheduled archives** and trigger them via a process that can be automated through **Cloud Workflow / Workflow**.

- **Manual** — appropriate when archiving should be a conscious admin step (e.g. after the consensus planning meeting concludes).
- **Automated** — appropriate when a periodic cadence (e.g. weekly weekend snapshot) is desired.

Choice is purely customer preference.

## Key takeaways

- The reporting model is a **separate model** dedicated to holding archived plan snapshots — not just a page or module inside Demand Planning.
- Initialization order matters: **source connections → time settings → time ranges → hierarchies → history**. Skipping or reordering breaks downstream imports.
- Time ranges in Anaplan require the **"Retain total of all periods"** flag if downstream formulas/exports rely on the total — common gotcha.
- **Synchronization** (current period + scenarios) is a prerequisite for every archive run; archives are otherwise misaligned with the live model.
- The **Waterfall / Forecast Accuracy reporting subsets** are how you control *which* of potentially many archives drives reporting. Treat them as a deliberate flag, not a default.
- Archives are scoped by **time horizon × scenarios × reporting-subset membership**. Plan the scope before clicking create.
- Automation via Cloud Workflow is available but optional — manual archiving is often the better choice for ceremony-driven processes (consensus meeting sign-off).

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Anaplan Demand & Supply Chain app]]
