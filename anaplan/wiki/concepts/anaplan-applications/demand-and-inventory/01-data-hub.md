---
title: "Chapter 01 — Initializing Data Hub"
type: concept
tags: [anaplan, demand-supply-chain-app, data-hub]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/01-01 Initializing Data Hub - Overview.md
  - raw/docs/01-02 Initializing Data Hub - Run Mass Delete.md
  - raw/docs/01-03 Initializing Data Hub - Time Settings and Ranges.md
  - raw/docs/01-04 Initializing Data Hub - Import and Hierarchies.md
  - raw/docs/01-05 Initializing Data Hub - Import Currency List.md
  - raw/docs/01-06 Initializing Data Hub - Import Properties.md
---

# Chapter 01 — Initializing Data Hub

## Purpose

Exercise 1 of the Anaplan Demand & Supply Chain application training. The goal is to bring the **Data Hub** from an empty (or demo-loaded) state to a working baseline that can feed the downstream demand-planning model: clean structural data, correct time settings, product/customer hierarchies, currency list, and item properties loaded.

Work is split between the **Data Hub UX application** (most imports) and the **underlying Data Hub model** (time settings + fixing broken action mappings).

## Steps covered

### 01-01 Overview

Sets context for the exercise. Key concepts introduced before hands-on work:

- **Mass delete is optional.** Most import processes already have parameters to delete items missing from the source, so blowing away the whole hub is convenient but not strictly necessary — and it removes more than needed (currencies, transport modes, UoMs, etc., which then have to be re-imported).
- **Hierarchy balancing parameter.** When the source file is a ragged (value) hierarchy with uneven parent depth, two options exist:
  - *As-is* — leaf items end up at different hierarchy levels (usually undesirable).
  - *Auto-balance* — the import inserts placeholder parents so all leaves sit at the bottom level. Global default lives in the application configuration area (page 900).
- **Parent code generation.** Leaf-level codes are mandatory; parent codes are not always supplied by source ERP. The Data Hub can generate parent codes so downstream models keep a consistent mapping key.
- **Transactional vs. process (leaf) level.** Planning typically occurs at the *process/leaf* level, which may be one level above the true transactional grain (e.g. plan at *sold-to* customer even though transactions are at *ship-to*; plan at SKU even though transactions are at variant/pack).
- **Property files** import many optional ERP attribute columns; only a small subset is commonly used by the application.

### 01-02 Run Mass Delete

- Action: **`P9999 Mass Delete Process`** (run from the Data Hub model's Actions list).
- Wipes virtually all structural items: hierarchies, lists, and associated data.
- Performed here to start from a clean slate. Gotcha: it also clears currencies / transport modes / UoMs that must then be reloaded (see 01-05).

### 01-03 Time Settings and Ranges

Done in the underlying model (Time settings, not via UX).

| Setting | Value |
|---|---|
| Current period | **FY25** |
| Past years | **3** |
| Future years | **1** |
| History time range | start **FY22**, **4** periods |
| Future time range | start **FY25**, **2** years |

- The "waterfall" time range is explicitly ignored in this exercise.
- Gotcha: depending on when the training environment was provisioned, the model may already be on FY25 and need no change. Verify before editing.

### 01-04 Import and Hierarchies

Done in the UX application: **Data Import → Update Master Hierarchies (page 106)**. Four hierarchies are exposed (Locations, Customers, Suppliers, Products); this exercise loads **Customers** and **Products** only.

Each hierarchy import is a **two-step pattern**:

1. Import source CSV into a **staging area** (for review/validation).
2. Run the **Update / Build Hierarchy** process to construct the actual list from staging.

CSVs come from the *Exercise 1* subfolder of the training data templates.

**Known gotcha — broken column mapping due to file encoding.** The training-data CSVs trigger a mapping loss on the *Level 1 Name* column in two import actions:

- `P020 002 Import Customer Hierarchy`
- `P010 002 Import Product Hierarchy`

Fix: open the action in the model, re-select the Level 1 Name source column (strange characters indicate the encoding issue), save, then re-run from the UX page. After staging validation clears, run the matching **Update Customer Hierarchy** / **Update Product Hierarchy** process to build the lists.

Validation options after build:
- UX **Master Hierarchies page 310** (Customer view), expand the tree.
- Or open the underlying general list (the **`leaf`**-labelled list at the bottom level) directly in the model.

### 01-05 Import Currency List

- Currencies were wiped by the mass delete (01-02) and must be restored because downstream steps depend on them.
- UX page **102 — Other Flat Lists** (same Data Imports section as hierarchies).
- Flat lists are **single-step** (no staging vs. build split).
- Select the currency process, pick the currency CSV from the Exercise 1 templates folder, run it.
- Verify on UX **page 400** (currency list view).

### 01-06 Import Properties

Loads master-data attributes alongside the hierarchies just created.

- Same UX page **106**, third step in each of the Customer and Product hierarchy/item-management sections.
- Run **Import Customer Properties** and **Import Product Properties**.
- Same encoding/mapping gotcha as 01-04: the first column (key onto the list of customers / products) loses its mapping. Fix actions:
  - `P022 001` — customer properties
  - `P012 001` — product properties
  - Edit each action in the model, remap column 1 onto the corresponding leaf list, re-run from UX.

After fixing and re-running, both property imports complete clean.

## Key takeaways

- **Two-step pattern for hierarchies** (stage → build) vs. **one-step for flat lists** (currencies, UoMs, transport modes, etc.).
- **Mass delete is a convenience, not a requirement.** Most imports support delete-on-missing, so a targeted refresh is often preferable; running mass delete forces you to also reload "incidental" structural lists like currencies.
- **Hierarchy balancing** (auto-balance vs. as-is) and **parent code generation** are the two parameters worth knowing for ragged source data. Global defaults live on UX **page 900** (application configuration).
- **Transactional ≠ planning grain.** The lowest level of the planning hierarchy may sit above the true transactional level (sold-to vs. ship-to, SKU vs. variant).
- **Encoding-driven action-mapping breakage** is a known training-data gotcha and affects all three Customer/Product import actions: `P020 002`, `P010 002`, `P022 001`, `P012 001`. Fix is always the same — re-map the affected column inside the underlying action.
- **Time settings live in the model**, not in the UX configuration area. Time ranges (history `FY22 × 4`, future `FY25 × 2`) are configured separately from the main current-period setting (`FY25`, -3/+1).
- End state of Exercise 1: empty hub repopulated with Customer + Product hierarchies (with properties), currency list restored, time correctly framed for downstream demand planning.

## Cross-references

- Source summary: [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Anaplan Demand & Supply Chain App — source summary]]
- Raw transcripts:
  - [[raw/docs/01-01 Initializing Data Hub - Overview]]
  - [[raw/docs/01-02 Initializing Data Hub - Run Mass Delete]]
  - [[raw/docs/01-03 Initializing Data Hub - Time Settings and Ranges]]
  - [[raw/docs/01-04 Initializing Data Hub - Import and Hierarchies]]
  - [[raw/docs/01-05 Initializing Data Hub - Import Currency List]]
  - [[raw/docs/01-06 Initializing Data Hub - Import Properties]]
