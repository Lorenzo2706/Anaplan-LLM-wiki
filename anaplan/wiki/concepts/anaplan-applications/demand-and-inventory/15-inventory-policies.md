---
title: Chapter 15 — Managing Inventory Policies
type: concept
tags: [anaplan, demand-supply-chain-app, inventory, ABC-XYZ, policies]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/15-01 Managing inventory policies-Overview.md
  - raw/docs/15-02 Managing inventory policies-Create a test inventory policy.md
  - raw/docs/15-03 Managing inventory policies-ABCXYZ.md
  - raw/docs/15-04 Managing inventory policies-set policies.md
  - raw/docs/15-05 Managing inventory policies-inventory policies.md
---

# Chapter 15 — Managing Inventory Policies

## Purpose

An **inventory policy** is the core control object of inventory planning in the Anaplan Demand & Supply Chain app. Each policy defines two things:

1. **Reorder point strategy** — *when* to trigger replenishment (e.g. periodic review on a weekly cadence).
2. **Target level strategy** — *to what level* to replenish (fixed quantity, periods-of-supply, or service-level-driven).

Together, these two settings drive the replenishment calculation visible on the main inventory planning page (page 240). This chapter walks through creating a policy, performing **ABC / XYZ segmentation on the supply side**, mapping policies to segments, and reviewing the surrounding parameters (MOQ, order multiple, frozen horizon, back-order strategy, scenarios) that also shape the replenishment plan.

## Steps covered

### 15-01 Overview

The exercise sequence:

1. Create a new inventory policy.
2. Perform ABC and XYZ segmentation on the supply side (analogous to the demand-analysis version seen earlier, but evaluated **per DC**).
3. Use the resulting ABC×XYZ segments as the basis for assigning default policies.
4. Review the replenishment result on the main inventory planning page.
5. Explore other parameters that influence the calculation.

### 15-02 Create a test inventory policy

In the main configuration area, open the **Manage Inventory Policies** page and add a new policy by stepping through inputs:

- **Name** — free text, e.g. `Every 4 periods: 8 periods supply`.
- **Reorder point strategy** — chosen here as **Periodic Review** on a **full weekly cycle** (planners place orders on a routine cadence).
- **Target level strategy** — set to **Calculated → Periods of Supply = 8**, so target inventory always equals 8 forward periods of forecast demand.

Apply the policy to a specific DC/product on page 240 (override the default). The result:

- Existing open supply POs (ERP-transacted) remain untouched.
- Beyond the open-PO horizon, new **simulated receipts** appear at the weekly reorder cadence, each sized to bring stock to ~8 weeks of forward demand.

Target-level alternatives worth noting (full catalog in the process reference guide):

| Target style | Use |
|---|---|
| Fixed | Hard-coded quantity per product/location |
| Calculated — periods of supply | Cover N forward periods of demand |
| Calculated — service level | Target driven by % service level + uncertainty sources: demand variability, forecast quality, lead-time variability |

Project implication: define an appropriate **catalog of policies** at implementation and train super-users to extend it over time.

### 15-03 ABC / XYZ segmentation (supply side)

Open the **ABC×XYZ → Edit and Commit** page. The process mirrors demand analysis but is evaluated **per DC**, because a SKU's importance differs by location.

**ABC segmentation logic:**

- Rank products by historical volume **within the selected DC**.
- Rank 1 = highest-volume product **for that DC** (the same SKU may rank differently across DCs).
- The calculated rank is overridable — e.g. a new-product-introduction SKU with no history can be manually flagged **A** as a strategic product.
- Effective settings must be **committed via a process** (saved snapshot). Rationale: ABC tiers drive inventory levels, so the business prefers periodic review over dynamic recalculation on every data load.

**XYZ segmentation logic** (page 158):

- Analyse **variability of demand** for each product at the selected DC.
- X / Y / Z reflect low / medium / high demand volatility.
- Dynamically calculated, overridable (e.g. mark an NPI as stable), then committed via process.

Outcome: every **product × location** combination carries a committed ABC×XYZ classification — the input to policy assignment.

### 15-04 Map policies to segments

On page **206 — Set inventory policies by segment**, the ABC×XYZ matrix is used to assign a default policy per cell. Example logic: items in the **X (stable)** column can be reviewed every four weeks with a periods-of-supply target, since both magnitude (ABC) and volatility (XYZ) inform the appropriate target.

Steps:

1. Switch the application from a pre-configured default to **use the new product/location-specific ABC×XYZ values** just committed.
2. The inventory projection (volumes and value) is recalculated per DC against the segment-mapped policies.
3. On page 240, the **default policy for each product/location now derives from its ABC×XYZ cell**, while still allowing per-line overrides.

Mapping summary: **ABC×XYZ cell → default inventory policy → reorder-point + target-level behaviour on page 240**.

### 15-05 Other replenishment parameters

Beyond the policy itself, several parameters shape the actual replenishment plan:

- **Minimum Order Quantity (MOQ)** — replenishment is rounded up to the MOQ (e.g. 5000). Side effect: receipts can overshoot the target and cause skipped reorder cycles until stock drains.
- **Order multiple** — once above MOQ, orders are rounded to a multiple (e.g. 5000s) rather than the exact target gap.
- **Frozen horizon** — number of forward periods that are locked (already committed to suppliers/production). No new replenishment can be inserted inside the horizon, even if a stock-out is projected.
- **Back-order strategy** — controls behaviour when demand exceeds available inventory:
  - **Back order** — shortfall accumulates as backlog; later replenishment clears the backlog (demand fulfilled late).
  - **Fill or Kill** — unmet demand is lost; replenishment only restores the policy target, not the backlog. Net replenishment volume is therefore lower.
- **Scenarios** — managed via a dedicated config page. Each scenario has flags such as:
  - *Committed plan* (Boolean) — disables future simulated replenishment; shows only on-hand + committed inbound transactions.
  - Interface controls with constrained production plans.
  - Quick-toggle overrides (e.g. ignore MOQs) to quantify the inventory inefficiency caused by a given constraint.

## Key takeaways

- A policy = **reorder-point strategy + target-level strategy**; everything else (MOQ, multiples, frozen horizon, back-order) is a *modifier* on top of the policy's intent.
- **ABC×XYZ is evaluated per DC**, not globally — the same SKU can be A at one DC and C at another.
- **Commit-via-process** is deliberate: ABC×XYZ tiers shouldn't drift with every data refresh because they directly drive stock levels.
- Policies are assigned **by segment** as defaults, with per product/location overrides on page 240.
- Service-level targets are the lever to control three independent uncertainties: demand variability, forecast error, and lead-time variability.
- MOQ and order multiples can cause structural over-stocking and skipped reorder cycles — useful to model explicitly via scenarios.
- Frozen horizon can create unavoidable stock-outs; the **back-order vs fill-or-kill** flag determines whether that demand is recovered later or lost.

## Cross-references

- Source summary: [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary]]
- Related: ABC×XYZ segmentation on the demand side (earlier demand-analysis exercise)
- Related concepts: reorder point, target inventory, service level, MOQ, frozen horizon, back-order strategy, planning scenarios
