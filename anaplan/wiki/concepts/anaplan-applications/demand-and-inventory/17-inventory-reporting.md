---
title: "Chapter 17 — Inventory Reporting"
type: concept
tags: [anaplan, demand-supply-chain-app, inventory, reporting]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/17-01 Inventory reporting-overview.md
  - raw/docs/17-02 Inventory reporting-alerting report.md
  - raw/docs/17-03 Inventory reporting-inventory aging report.md
  - raw/docs/17-04 Inventory reporting-remaining shelflife report.md
  - raw/docs/17-05 Inventory reporting-auto expiry.md
---

# Chapter 17 — Inventory Reporting

## Purpose

The final exercise of the Demand & Supply Chain app walkthrough covers the **reporting capabilities derived from the inventory planning process**. The chapter is delivered as a demonstration rather than a hands-on task — the trainee's app copy lacks sufficient data to reproduce the visuals, so a separate populated copy is used.

Two themes run through the chapter:

1. **Configuration matters.** End-user reporting is often treated as an afterthought once the core planning logic works. Each report has a small number of parameters (thresholds, buckets, date basis) that must be tailored to the implementing organization.
2. **Data availability gates reporting capability.** Aging requires production or receipt dates; shelf-life reporting requires expiry dates. What can be reported is a direct function of what can be loaded.

> [!note] 17-04 ingested 2026-05-12
> The `17-04` transcript (**Remaining Shelf Life report**) was added in a follow-up ingest. The Remaining Shelf Life section below now reflects that primary source; the earlier inference from the `17-02` overflow is consistent with it.

## Steps covered

### 17-02 — Alerting / exception report

- **What it is:** a standardized alerts-and-exceptions page across the suite (demoed on page **052**) that surfaces KPIs per product × location, plus a combined prioritization score so planners with limited time know where to drill in.
- **KPIs shown** for each combination:
  - Days until stock-out
  - Current inventory vs. target (over/under)
  - Inventory age profile
- **Prioritization:** the three KPI statuses are combined (via configurable weights) into a single priority score; planners filter to "high priority" combinations and drill into the underlying detail page.
- **Configuration (page 950 — Manage KPIs):**
  - **Weighting approach** — relative emphasis of each KPI on the combined score (e.g. setting one to 30 makes it dominate).
  - **Thresholds** — start/end points for good / neutral / bad status per KPI. Must be revisited if the planning bucket changes (e.g. weekly ↔ monthly) or for businesses with different tolerance for stock-out.

### 17-03 — Inventory aging report & 17-04 — Remaining shelf life

#### Inventory aging (page 522)

- Groups all network inventory into **age buckets** (e.g. 0–15, 16–30, 31–45, 46–60, 61+ days) by DC, with drill-down to product.
- **Configuration:**
  - **Manage Age Categories** — define bucket names and upper/lower day thresholds. Right buckets vary per organization.
  - **Estimated production date** parameter (global parameters page) — sets the *start point* used to compute age. Options, in order of preference:
    1. **Production date** — exact, when each batch's production date is loaded.
    2. **Receipt date** — when production date isn't available; age measured from DC receipt.
    3. **Receipt date − lead time** — approximates production date by back-dating receipt by the lead time.

#### Remaining shelf life (page 526) — from `17-04`

- Forward-looking counterpart to aging: groups inventory by **days until expiry** into shelf-life buckets, so planners see how much stock is at risk of expiring soon vs. has long remaining life.
- Demo example: in California, 60,000 units expire within 14–27 days; another tranche has up to 100 days; the bulk has >100 days remaining.
- **Configuration (two parameters, mirroring the aging report):**
  - **Shelf-life buckets** — name + upper/lower day boundaries (e.g. 1–2, 3–4, 5–6 …). Must be tailored to the implementation's product life-cycle.
  - **Basis for remaining shelf life** (parameter `RSL 526`, surfaced on the report header):
    - **True expiry** — physical expiry date derived from production date + product master shelf life.
    - **Stop sell** — true expiry offset by the **minimum remaining shelf life the customer will accept** (e.g. customer mandates ≥28 days on delivery). Operationally more relevant than true expiry because stop-sell is when the product effectively becomes unsellable, not when it physically expires.

### 17-05 — Auto expiry

- **Not a report** but a planning calculation that feeds back into inventory availability — included here because it shares the expiry-date configuration of the shelf-life report.
- **Problem it solves:** the engine consumes inventory FIFO against demand, but by default it does **not** recognize that some old stock will expire before demand can consume it. Result: phantom availability.
- **Behavior:**
  - **Auto expiry OFF** → expiry risk ignored, all on-hand inventory treated as usable.
  - **Auto expiry ON** → units that would expire before being consumed are removed from available inventory in the period they expire (demoed: 17,000 units flagged to expire in week 35 and dropped from availability).
- **Basis toggle:** same true-expiry vs. stop-sell choice as the shelf-life report. Using stop-sell removes more inventory, and earlier in the horizon, than using true expiry.

## Key takeaways

- Reporting in the Inventory app is **driven by a small set of configuration objects**: KPI definitions/weights/thresholds (alerts), age and shelf-life bucket definitions, and the date-basis parameters that anchor "age" and "remaining life" to the right reference date.
- **Date basis is the single biggest data-quality lever:** production date > receipt date > receipt − lead time. The implementation team should push for the most accurate date the source systems can provide.
- **Stop-sell vs. true expiry** is a recurring choice — affects both the shelf-life report and the auto-expiry calculation. Stop-sell is usually closer to commercial reality.
- **Auto expiry** bridges reporting and planning: turning it on materially changes projected availability and downstream replenishment recommendations, so it should be a deliberate implementation decision, not a default.
- Plan the reporting layer **alongside** the planning logic, not after — late configuration of thresholds and buckets is a common implementation gap.

## Cross-references

- Source summary: [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Anaplan Demand & Supply Chain App — source summary]]
- Related chapters: chapter 16 (inventory planning core) feeds the data these reports consume.
