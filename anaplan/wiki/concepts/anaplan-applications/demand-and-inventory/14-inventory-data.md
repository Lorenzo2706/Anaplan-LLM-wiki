---
title: Chapter 14 — Importing and Managing the Inventory Data
type: concept
tags: [anaplan, demand-supply-chain-app, inventory, supply-planning]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/14-01 Importing and managing the inventory data-overview.md
  - raw/docs/14-02 Importing and managing the inventory data-import inventory and po data.md
  - raw/docs/14-03 Importing and managing the inventory data-move data to supply planning model.md
  - raw/docs/14-04 Importing and managing the inventory data-review data.md
  - raw/docs/14-05 Importing and managing the inventory data-confirm forecast consumption.md
---

# Chapter 14 — Importing and Managing the Inventory Data

## Purpose

Continue initializing the **inventory planning model** by bringing in the remaining transactional data sets needed to complete the inventory picture. Chapter 13 imported the demand plan; chapter 14 imports **on-hand DC inventory** and **open supplier purchase orders (POs)** through the Data Hub, transfers them to the Supply Planning model, reviews configuration choices that govern how that data is used, and confirms the **forecast consumption** setup that reconciles planned demand with actual customer orders.

By the end of the chapter, the inventory planner can see a full projected inventory picture combining **demand, on-hand inventory, and incoming POs** in one place — the starting point for downstream supply planning calculations.

## Steps covered per sub-video

### 14-01 — Overview

- Recap: demand plan already imported (chapter 13). Now adding the remaining inventory-side data.
- Scope intentionally limited to two data sets: **on-hand DC inventory** and **open supplier POs** (other transactional sets exist — in-transit, intercompany — but are out of scope here).
- Workflow: import to Data Hub → push to Supply Planning model → review in Inventory Planning app → set forecast consumption.

### 14-02 — Import inventory and PO data into the Data Hub

- Use the standard **page 108 "Update Transactional Data"** in the Data Hub application.
- Wider menu shows many supply-side data sets (in-transit between DCs, intercompany orders, etc.); this exercise picks only DC inventory and open supplier POs.
- For each: locate the **Exercise 14** source folder, select the file, run the import process. Same pattern for both.
- Inventory data is at **lot level**: multiple rows can share product + location but differ on attributes such as **expiry date**. This granularity lets downstream modules report and plan against expiry, batch, or other lot-specific attributes.
- Inventory record fields seen: quantity, location, product, expiry date, status code, etc.

### 14-03 — Move data to the Supply Planning model

- Stay in Data Hub; use the **240 Update Data** section to push imported data outward.
- Run the **open supplier purchase orders** push process, then the **update inventory** process.
- After these run, the Data Hub side of chapter 14 is complete; data has landed in the Inventory Planning application.

### 14-04 — Review the data in Inventory Planning

Three review pages, each with a configuration lever:

**Page 204 — Manage Available Inventory**
- Summarized view of inventory the app now knows about.
- Key config: decide which **status codes** count as *available* inventory. Statuses flagged as e.g. *damaged* should be excluded so they do not falsely satisfy demand.

**Page 202 — Open Purchase Orders**
- Shows PO **headers** (PO date, destination location, line count) with drill-down into PO **lines** (per-product quantities).
- Scenario selector lets planner switch from the committed scenario to e.g. *Scenario 1* to test alternate configurations.
- Key config: **how much PO data to include** in the inventory calculation. Options:
  - **No** — simulate ignoring all open POs (what-if where placed POs are not honored).
  - **Yes (all)** — include every open PO (typical).
  - **Yes, future receipts only** — include only POs whose expected receipt date is in the current or future period; late POs (receipt date before current period) are excluded. If late POs are *included*, the app pulls them into the first forecasted period.

**Page 240 — DC Inventory Planning**
- Brings demand, on-hand inventory, and incoming supply together per location (e.g. Central DC).
- Visual: demand baseline, spikes from incoming POs, calculated new receipts (out in the future — covered in a later exercise), and the **inventory balance** trajectory (opening on-hand → consumed by demand → replenished by arrivals → consumed again).
- This page is the success criterion for the exercise: an inventory projection is now visible.

### 14-05 — Confirm forecast consumption

- Configured on **page 900 Global Parameters** in Inventory Planning.
- Parameter: **Consumption Method**. Must be set to *something* (not left off, unless consumption is being handled upstream — see below).
- What forecast consumption does: reconciles the **forecasted demand plan** against **committed customer demand** (open sales orders) so the planner sees:
  - Transacted (committed) portion of demand.
  - **Unconsumed forecast** = plan − committed (the portion of the plan not yet realized as orders).
- Example: plan 2,200, committed 1,960 → unconsumed = 240 (transcript rounds to ~277 illustratively).
- Consumption methods matter most when **committed > plan** for a period:
  - **Same period only** — the excess simply shows as a spike that period; no spillover; under-consumed forecast becomes zero for that bucket.
  - **Forwards** — excess committed demand consumes future periods' forecast as well (e.g. a 5,000–6,900 spike absorbs week 20 plus weeks 21 and part of 22).
- **Important interlock with demand planning**: forecast consumption can happen either at the **end of demand planning** or at the **start of inventory planning**, but **not both** (would double-consume). The Demand Planning model sends a **signal** to Inventory Planning. If demand planning already ran consumption, Inventory Planning cannot apply it again. Recall: chapter 13 explicitly switched consumption *off* on the demand side so it can run here.

## Key takeaways

- **Two transactional data sets** added in this chapter: on-hand DC inventory and open supplier POs. Other supply data sets exist but are not always required.
- Inventory is imported at **lot level**, preserving attributes like expiry date — necessary for expiry-aware planning.
- Three review-page configuration knobs gate how raw transactional data feeds the calculation:
  1. **Inventory status codes** (page 204) — what counts as *available*.
  2. **PO inclusion** (page 202) — none / all / future-only, scenario-scoped.
  3. **Forecast consumption method** (page 900) — same-period vs forwards.
- **Page 240 DC Inventory Planning** is where the full picture (demand + on-hand + incoming POs + calculated balance) becomes visible. Hitting this view is the explicit success criterion.
- **Forecast consumption must run in exactly one place** (Demand Planning *or* Inventory Planning). The Demand Planning model signals Inventory Planning so the latter can refuse to run it twice. This was prepared for in chapter 13 by turning consumption *off* in demand planning.
- All imports flow through the **Data Hub → Supply Planning model** pattern established earlier in the course — same architectural shape as the demand plan import in chapter 13.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Anaplan Demand & Supply Chain App course]]
- Previous chapter: importing the demand plan (chapter 13) — sets up the consumption-off flag this chapter depends on.
- Related concepts: Data Hub transactional import pattern, scenario-based planning, DISCO module categorization (the page 204/202/240 pages are Outputs/Calculations layered on imported Data).
