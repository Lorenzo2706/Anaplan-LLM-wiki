# Exercise 15 — Managing Inventory Policies

**Series:** Anaplan Demand & Supply Chain Reference App
**Chapter:** 15 of 17
**Lessons:** 15-01 through 15-05

---

## Overview

Exercise 15 introduces the **inventory policy** — the core control object of the inventory planning calculation. An inventory policy defines two things: *when* to trigger a replenishment order and *to what level* to replenish. Everything else in the inventory calculation (MOQs, order multiples, frozen horizons, back-order behaviour) modifies or constrains how those two policy decisions translate into an actual replenishment plan.

The exercise follows five stages:

1. Understand what an inventory policy is and create a new one
2. Perform ABC segmentation on the supply side, per DC
3. Perform XYZ segmentation on the supply side, per DC
4. Map policies to ABC×XYZ segments and activate the segmented plan
5. Explore the additional parameters that shape the replenishment calculation

---

## Lesson 15-01 — Overview

### Purpose of inventory policies

At the heart of the inventory planning calculation is the concept of an **inventory policy**. A policy answers two questions:

- **When do we reorder?** (the reorder point strategy)
- **How much do we target?** (the target level strategy)

These two settings together drive the simulated replenishment receipts visible on page 240. Different product-location combinations may warrant different policies — a high-volume, stable SKU at a major DC has different replenishment needs than a low-volume, volatile SKU at a regional one.

### Steps at a glance

| # | Action | Location |
|---|--------|----------|
| 1 | Create a new inventory policy | Inventory Planning — Manage Policies page |
| 2 | Apply it to a specific product/DC on page 240 | Inventory Planning — page 240 |
| 3 | Run ABC segmentation per DC | ABC×XYZ — Edit and Commit page |
| 4 | Run XYZ segmentation per DC | ABC×XYZ — page 158 |
| 5 | Map policies to ABC×XYZ segments | Inventory Planning — page 206 |
| 6 | Activate segment-based policies on page 240 | Inventory Planning — page 240 |
| 7 | Explore replenishment modifiers | Inventory Planning — policy and parameter pages |

---

## Lesson 15-02 — Create a Test Inventory Policy

### Where to work

Navigate to the **Inventory Planning application**, then to the main configuration area and open the **Manage Inventory Policies** page. The application ships with a pre-configured set of policies; this step adds a new one.

### What a policy defines

Every policy is built around two strategies:

**1. Reorder point strategy — when to trigger a replenishment order**

This defines the logic for deciding when to place a new order. The example used in the lesson is **Periodic Review**, where inventory planners operate on a routine review cadence and place orders at fixed intervals. In this case, the cadence is set to a **full weekly cycle** — the planner reviews and orders once per week.

Other reorder point strategies exist (documented in the process reference guide) but are not explored in this lesson.

**2. Target level strategy — what quantity to order up to**

This defines the target inventory level the replenishment order is trying to reach. There are three main approaches:

| Target style | How it works |
|---|---|
| **Fixed** | A hard-coded quantity is defined for a specific product/location combination. The planner inputs a number manually. |
| **Calculated — Periods of Supply** | The target is dynamic: it equals N forward periods of forecasted demand. If demand rises, the target rises with it. |
| **Calculated — Service Level** | The target is derived from a desired service level percentage (e.g. 99%). The model accounts for three independent sources of uncertainty: variability in future demand, quality of the forecast itself, and variability in supplier lead times. |

### Creating the test policy

Step through the following inputs on the Manage Inventory Policies page:

1. **Name** — give the policy a descriptive name that encodes its behaviour. Example: `Every 4 periods: 8 periods supply`.
2. **Reorder point strategy** — select *Periodic Review*, then set the review cycle to *Full weekly*.
3. **Target level strategy** — select *Calculated*, then choose *Periods of Supply* and set the value to **8**. This means the target inventory level at any point in time should be sufficient to cover 8 forward weeks of demand.

### Observing the policy on page 240

Once the policy is created, navigate to **page 240 — DC Inventory Planning** and apply the new policy to a specific product/DC combination by overriding the default. The effect is visible immediately on the chart:

- **Open supplier POs** already transacted in the ERP remain unchanged — these are committed, real-world receipts and are not affected by policy changes.
- **Beyond the open-PO horizon**, the application generates new *simulated receipts*. These are placed on a weekly cadence (matching the Periodic Review cycle) and are sized to bring the projected inventory level up to 8 weeks of forward demand.

This makes the policy effect tangible: the frequency and sizing of future receipts on the chart directly reflect the two strategy parameters defined in the policy.

### Implementation guidance

The lesson makes an important project-level point: the right time to define the **full catalog of inventory policies** is during the implementation project — not after go-live. The catalog should represent all the reorder/target combinations the business is likely to need. Super-users and administrators should also be trained to create and manage policies themselves as business needs evolve over time.

---

## Lesson 15-03 — ABC / XYZ Segmentation (Supply Side, Per DC)

### Purpose

Rather than manually assigning a policy to every product/location combination, the app uses **ABC×XYZ segmentation** to assign default policies in bulk. This is the same segmentation concept introduced in the demand analysis exercises, but applied here on the supply side with one critical difference: **segmentation is evaluated per DC**, not globally.

The reason for this is that a product's importance depends on where it is. A SKU that is the highest-volume product at the Central DC might be a low-volume, low-priority item at a regional DC. Assigning policies based on global rankings would lead to mismatched replenishment strategies.

### ABC segmentation — ranking by volume per DC

Navigate to the **ABC×XYZ → Edit and Commit** page.

1. The application calculates an ABC rank for each product **within the currently selected DC**, based on historical volumes. Rank 1 = highest volume at that DC.
2. Review the calculated ranks. These can be **manually overridden** where the calculation does not reflect business reality. Example: a new product introduction (NPI) with no sales history would rank near the bottom by volume, but strategically it may need to be treated as an **A** item. The planner can override it directly.
3. Once the ranks are reviewed and any overrides applied, **commit the settings via a process**. The committed values — not the dynamically calculated ones — are what drives the policy assignment.

**Why commit rather than use dynamic values?** Because ABC categorizations directly influence inventory levels. Allowing them to shift automatically with every data load would create uncontrolled changes to replenishment targets. The business prefers to review and approve tier changes periodically, on a deliberate cadence.

### XYZ segmentation — classifying demand variability per DC

Move to **page 158** and repeat the same process for XYZ.

1. The application calculates a demand variability classification for each product at the selected DC: **X** (low variability / stable demand), **Y** (moderate variability), **Z** (high variability / volatile demand).
2. As with ABC, overrides are allowed. In the lesson, the NPI product is manually set to **X** (stable) — since it has no demand history, its calculated variability is meaningless, and the business may know its demand profile from other sources.
3. Run the process to **commit the XYZ classifications**.

### Outcome

Every **product × location** combination in the model now carries a committed ABC×XYZ classification — for example, "A/X" for the highest-volume, most stable SKU at a given DC, or "C/Z" for a low-volume, volatile one. These classifications are the input to policy assignment in the next step.

---

## Lesson 15-04 — Map Policies to Segments

### Where to work

Navigate to **page 206 — Set Inventory Policies by Segment**.

### How the mapping works

Page 206 presents the ABC×XYZ classification matrix. For each cell in the matrix (e.g. A/X, A/Y, B/Z, etc.), the planner assigns a default inventory policy. The logic is intuitive: the magnitude of demand (ABC) and its volatility (XYZ) together inform how tightly inventory should be managed.

Example from the lesson: **X items** (stable demand) can be reviewed every four weeks with a periods-of-supply target, because their predictability makes it safe to place orders infrequently. A Z item (volatile demand) would warrant a shorter review cycle and possibly a service-level-driven target to buffer against uncertainty.

### Activating the new segmentation

The application may be pre-configured to use a default or generic policy for all items. To use the ABC×XYZ-based assignment just committed:

1. On page 206, switch the configuration from the pre-set default to **use the product/location-specific ABC×XYZ values** calculated in Lesson 15-03.
2. The application immediately recalculates the inventory projection across all DCs, now applying the segment-mapped policy to each product/location combination.

### Result on page 240

Return to **page 240 — DC Inventory Planning**. The replenishment calculation now reflects the segment-assigned default policy for each product/location. The default policy is derived from its ABC×XYZ cell, but **per-line overrides remain available** — the planner can still manually assign a different policy to any specific product/location if business rules require it.

The chain is: **ABC×XYZ cell → default policy → reorder point + target level behaviour on page 240**.

---

## Lesson 15-05 — Additional Replenishment Parameters

Beyond the policy itself, several parameters shape how the replenishment plan is actually generated. These modifiers sit on top of the policy's intent and can significantly change the final output.

### Minimum Order Quantity (MOQ)

In its base state, the replenishment calculation identifies the exact quantity of inventory needed to reach the policy target — for example, 2,655 units. In reality, suppliers often impose a minimum order quantity that prevents ordering below a threshold.

**Example from the lesson:** setting an MOQ of 5,000 causes the system to immediately round every replenishment up to at least 5,000 units. The visible effect on page 240:

- Every simulated receipt now has a floor of 5,000 units.
- Because the order is larger than necessary, the DC ends up with more inventory than the policy target requires.
- This excess means the DC can skip the next reorder cycle — there is already enough inventory to last beyond the next expected review point. In the lesson, a policy that was generating receipts every two weeks now generates them every four weeks, because each receipt overshoots the target enough to last twice as long.

**Project implication:** MOQs can create structural over-stocking. Modeling them explicitly — and using scenarios to compare inventory levels with and without MOQs — is a useful way to quantify the cost of supplier ordering constraints.

### Order Multiple

Related to MOQ, the **order multiple** constrains the sizing of orders above the MOQ threshold. Rather than ordering the precise quantity the model calculates, the order is rounded up to the nearest multiple.

**Example:** with a MOQ of 1,000 and an order multiple of 5,000, any order above 1,000 is rounded to the nearest 5,000 (5,000 / 10,000 / 15,000 etc.). This further smooths the order quantities but introduces additional over-stocking at each replenishment event.

### Frozen Horizon

The **frozen horizon** defines a number of forward periods during which the replenishment plan is locked and cannot be changed. It reflects the operational reality that once orders have been communicated to suppliers or production, they cannot be withdrawn or amended within a certain lead window.

**Example from the lesson:** setting a frozen horizon of 12 weeks means the next 12 weeks of replenishment are fixed. No new simulated receipts can be inserted inside that window, even if the model detects a projected stock-out.

**The consequence of stock-outs within the frozen horizon:** if demand in the frozen period exceeds available inventory and no new receipts can be added, a stock-out accumulates. What happens to the unmet demand depends on the back-order strategy.

### Back-Order Strategy

The back-order strategy controls how the application handles situations where demand exceeds available inventory:

| Strategy | Behaviour |
|---|---|
| **Back order** | Unmet demand accumulates as a backlog. When inventory is eventually replenished after the frozen horizon, that replenishment is used to clear both the backlog and restore the policy target. Demand is fulfilled late, not lost. |
| **Fill or Kill** | Unmet demand is lost. If inventory is not available in the period the customer wants it, the sale is forfeit. When replenishment eventually arrives, it only needs to restore the policy target — not cover any backlog. Replenishment volumes are therefore lower than under back order. |

**Comparison in practice:** in the lesson, applying a 12-week frozen horizon triggers a projected stock-out. Under *Back order*, the shortfall accumulates week by week and is cleared when the first replenishment after week 12 arrives. Under *Fill or Kill*, the same stock-out occurs but the demand is written off — the future replenishment is smaller because there is no backlog to clear.

The choice between the two strategies should reflect commercial agreements with customers: if the business can ship late and customers will accept it, Back order is appropriate. If late shipments are commercially unacceptable and the sale is simply lost, Fill or Kill is the more accurate representation.

### Scenarios

The lesson finishes with a brief look at **scenario configuration**, accessible from the scenario management page. Each scenario is configured with a set of flags and controls that govern its behaviour:

- **Committed plan (Boolean):** when ticked, this flag disables the calculation of future simulated replenishment. The scenario shows only what the current on-hand inventory plus committed inbound transactions (already transacted POs) can deliver — no new orders are simulated. This is useful as a baseline to see the plan without any model-generated replenishment.
- **Interface with constrained production plans:** additional controls for scenarios that need to respect production capacity constraints.
- **Quick-toggle overrides:** each scenario can include fast switches to temporarily override parameters such as MOQs. This is useful for quantifying inefficiency — for example, running a scenario with MOQs turned off shows how much additional inventory the business is holding purely because of the minimum order constraint. The difference between the two scenarios is the "cost" of the MOQ.

---

## Exercise 15 — Summary

| Step | Page | What you do | Key decision |
|------|------|-------------|--------------|
| 1 | Manage Policies | Create a new inventory policy | Reorder point strategy + target level strategy |
| 2 | Page 240 | Apply the new policy to a product/DC | Override default, observe simulated receipts |
| 3 | ABC×XYZ Edit & Commit | Run ABC segmentation per DC | Rank by volume; override NPIs/strategic items |
| 4 | Page 158 | Run XYZ segmentation per DC | Classify demand variability; override as needed |
| 5 | Page 206 | Map policies to ABC×XYZ segments | Assign a default policy per matrix cell |
| 6 | Page 206 | Switch to product/location-specific ABC×XYZ | Activate the new segmentation |
| 7 | Page 240 | Review the updated inventory projection | Validate segment-driven replenishment |
| 8 | Policy/parameter pages | Configure MOQ, order multiple, frozen horizon | Set according to supplier/operational constraints |
| 9 | Policy/parameter pages | Set back-order strategy | Back order vs. Fill or Kill |
| 10 | Scenario config page | Review and configure planning scenarios | Committed plan flag, quick-toggle overrides |

---

## Key concepts

**Inventory policy** — the core control object of the replenishment calculation. Combines a reorder point strategy (when to order) and a target level strategy (how much to hold). Everything else is a modifier on top of the policy.

**Periodic Review** — a reorder point strategy where orders are placed on a fixed routine cadence (e.g. weekly) rather than triggered by a real-time stock level crossing a threshold.

**Periods of Supply** — a target level strategy that sets the inventory target to N forward periods of forecasted demand. Dynamic: as demand changes, the target adjusts automatically.

**Service Level target** — a target level strategy that derives the required safety stock from a desired service percentage, accounting for demand variability, forecast error, and lead-time variability independently.

**ABC segmentation (supply side)** — ranking of products by historical volume *within a specific DC*. Evaluated per DC because importance varies by location.

**XYZ segmentation (supply side)** — classification of products by demand variability *within a specific DC*. X = stable, Z = volatile. Evaluated per DC.

**Commit via process** — the deliberate step of saving ABC×XYZ classifications as a fixed snapshot rather than letting them update dynamically. Protects inventory levels from shifting uncontrolled with every data load.

**MOQ (Minimum Order Quantity)** — a supplier-imposed floor on order sizes. Can cause structural over-stocking and extended reorder cycles.

**Order multiple** — a rounding rule applied to order quantities above the MOQ, snapping orders to the nearest defined multiple.

**Frozen horizon** — a lock on the near-term replenishment plan, reflecting that commitments already made to suppliers or production cannot be changed within a certain window.

**Back order** — a strategy where unmet demand accumulates as a backlog to be fulfilled once inventory is available. Contrast with Fill or Kill, where unmet demand is lost.

**Fill or Kill** — a strategy where demand that cannot be met in the requested period is forfeit. Future replenishment only restores the policy target, not any backlog.

**Committed plan scenario** — a scenario flag that disables simulated future replenishment, showing only what current on-hand inventory and already-transacted POs can deliver.

---

*Sources: raw transcripts 15-01 through 15-05 (raw/docs/)*
*Wiki summary: [[15-inventory-policies]]*
