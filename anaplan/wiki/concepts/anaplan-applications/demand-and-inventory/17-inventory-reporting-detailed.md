# Exercise 17 — Inventory Reporting

**Series:** Anaplan Demand & Supply Chain Reference App
**Chapter:** 17 of 17
**Lessons:** 17-01 through 17-05

---

## Overview

Exercise 17 is the final chapter of the Demand & Supply Chain reference app walkthrough. It covers the **reporting and exception management capabilities** that are built on top of the inventory planning process configured in the preceding exercises.

Unlike earlier exercises, this one is delivered primarily as a **demonstration** rather than a hands-on activity. The trainee's copy of the application does not contain sufficient data to reproduce the reports meaningfully, so a separate, fully populated copy is used for the demo. The focus is therefore less on executing steps and more on understanding what each report does, what configuration it requires, and what data must be available for it to work.

The lesson makes a deliberate point at the outset: reporting configuration is frequently treated as an afterthought during implementations, addressed only after the core inventory planning logic is working. This exercise argues that it should be planned and configured in parallel with the planning layer — not bolted on afterwards — because the reports depend on both correct configuration and the right data being loaded from source systems.

Three reporting areas are covered:

1. **Alerting and exception report** — a KPI-based prioritisation tool for planners
2. **Inventory aging report** — groups on-hand inventory by how old it is
3. **Remaining shelf life report** — groups on-hand inventory by how long it has until it expires
4. **Auto expiry** — a planning calculation (not a report) that uses expiry data to remove at-risk inventory from the available pool

### Steps at a glance

| # | Report / Feature | Output page | Configuration page |
|---|---|---|---|
| 1 | Alerting / exception report | Page 052 | Page 950 — Manage KPIs |
| 2 | Inventory aging report | Page 522 | Manage Age Categories + Global Parameters |
| 3 | Remaining shelf life report | Page 526 | Shelf life buckets + RSL parameter |
| 4 | Auto expiry | Page 240 (inventory plan) | Auto expiry toggle + true expiry vs. stop sell |

---

## Lesson 17-01 — Overview

### Why this exercise matters

Inventory reporting is often the last thing configured in a project — and consequently the thing most likely to be under-specified or misconfigured at go-live. The reports in the Inventory Planning app have a small number of configuration objects each, but those objects must be tailored to the implementing organisation. Default settings will rarely be correct out of the box.

There is also a hard dependency on **data availability**: each report can only function if the source data needed to power it has been loaded into the application. The aging report needs a date to measure age from; the shelf life report needs expiry dates. If the source systems cannot provide those fields, the corresponding reports cannot be used. This relationship between data availability and reporting capability is a key theme of the exercise.

### Scope

The exercise covers three reports (alerting, aging, remaining shelf life) and one related planning feature (auto expiry). All are demonstrated on a separate, data-rich copy of the application. The trainee's task is to understand the configuration requirements so they can apply them during an implementation project.

---

## Lesson 17-02 — Alerting and Exception Report (Page 052)

### What the report does

The alerting report on **page 052** is a standardised exception management view that exists across all applications in the Demand & Supply Chain suite. Its purpose is to help planners with limited time quickly identify **which product/location combinations need attention**, rather than reviewing every combination manually.

For each product × location combination, the report presents:

- **Contextual metrics** — summary information such as current inventory quantity and expected incoming receipts, giving the planner a sense of scale.
- **Three KPIs**, each with a good / neutral / bad status indicator:
  1. **Days until stock-out** — how long the current inventory projection can satisfy demand before running out.
  2. **Inventory vs. target** — whether current inventory is significantly above or below the policy target level.
  3. **Inventory aging profile** — how old the on-hand stock is.
- **Combined prioritisation score** — the three KPI statuses are aggregated into a single score that ranks combinations from highest to lowest priority. Planners can filter to "high priority" and drill into the inventory plan for those combinations directly.

**Example from the lesson:** filtering to high priority surfaces "Smartphones — New York DC" as a combination with too much inventory relative to demand. The planner can drill into the inventory plan for that combination to investigate.

### Configuration: page 950 — Manage KPIs

There are two main configuration inputs:

**1. Weighting approach**

The relative weight assigned to each KPI determines how much influence it has on the combined prioritisation score. For example, if days-until-stock-out is given a weight of 30 and the other two KPIs lower weights, a looming stock-out will dominate the prioritisation score more than an aging or over-stocking signal.

Weights should be set to reflect the business's risk priorities — a business with low tolerance for stock-outs will weight that KPI heavily; one with strict shelf-life constraints might weight the aging KPI more.

**2. KPI thresholds**

For each KPI, the planner defines the start and end points that separate good, neutral, and bad performance. For example:

- Days until stock-out: what number of days constitutes "good" buffer vs. an unacceptable risk?
- Inventory vs. target: what percentage above or below target triggers a "bad" flag?
- Aging profile: at what age does inventory become a concern?

These thresholds must be calibrated to the organisation. They are also sensitive to the **planning bucket**: thresholds set for a weekly planning model will be wrong if the model is later changed to monthly buckets, because the same number of periods represents a very different absolute time window.

**Implementation note:** unless new KPIs are being added to the application (a more advanced configuration task), many of the basic KPI definition fields will not need to be changed during a project. The weighting approach and thresholds are the two inputs that almost always require organisation-specific calibration.

---

## Lesson 17-03 — Inventory Aging Report (Page 522)

### What the report does

The inventory aging report on **page 522** shows all on-hand inventory across the network grouped into **age buckets** — ranges of days that classify how old the stock is. The view can be shown in aggregate across the network or drilled down to a specific DC and then to individual products.

**Example from the lesson (California DC):**

| Age bucket | Quantity |
|---|---|
| > 61 days | 60,000 units |
| 46–60 days | Additional tranche |
| 31–45 days | — |
| 16–30 days | Majority of network inventory |
| 0–15 days | — |

The report gives planners visibility into the age profile of their stock, which is relevant for identifying inventory that may be at risk of expiring, becoming obsolete, or failing customer shelf-life requirements before it can be consumed.

### Configuration 1: age bucket definitions (Manage Age Categories)

The age buckets displayed on page 522 are not fixed — they are defined in the **Manage Age Categories** configuration page. For each bucket, the planner provides:

- A **name** (e.g. "0–15 days", "16–30 days", "> 61 days").
- An **upper boundary** (days).
- A **lower boundary** (days).

The correct bucket definitions depend entirely on the organisation. A business with products that have a 90-day shelf life will need finer granularity in the 0–90 day range than one dealing with products that last years.

### Configuration 2: estimated production date (Global Parameters page)

To calculate the age of a piece of inventory, the model needs a **reference start date** — the "birth date" of the stock. This is set via the **Estimated Production Date** parameter on the Global Parameters page. There are three options, listed in order of accuracy:

| Option | Description | When to use |
|---|---|---|
| **Production date** | The exact date the batch was manufactured, loaded per lot from the source system. | Preferred — most accurate. Use when production/batch dates are available in the ERP or WMS. |
| **Receipt date** | The date the inventory was received into the DC. | Use when production date is not available but receipt date is. Age is measured from DC receipt, not manufacture — slightly less accurate. |
| **Receipt date − lead time** | An approximation of production date, calculated by subtracting the known lead time from the receipt date. | Use when neither production date nor a meaningful receipt date is available. A rough approximation only. |

**Implementation note:** the choice of date basis is the single biggest data-quality lever for this report. Pushing source systems to provide production dates — rather than accepting receipt dates or approximations — significantly improves the accuracy and usefulness of the aging analysis. This should be a data requirements conversation during the implementation project, not a post-go-live fix.

---

## Lesson 17-04 — Remaining Shelf Life Report (Page 526)

### What the report does

The remaining shelf life report on **page 526** is the **forward-looking counterpart to the aging report**. Where the aging report looks backward (how old is this inventory?), the shelf life report looks forward (how long does this inventory have left before it expires?).

Inventory is grouped into **shelf life buckets** — ranges of days representing how much remaining life each tranche of stock has. This gives planners a clear picture of how much inventory is at risk of expiring in the near term versus how much has ample remaining life.

**Example from the lesson (California DC):**

| Remaining shelf life bucket | Quantity |
|---|---|
| 14–27 days | 60,000 units |
| Up to 100 days | Additional tranche |
| > 100 days | Majority of inventory |

The report allows planners to prioritise consumption or redistribution of short-life stock and to flag at-risk inventory before it becomes unsellable.

### Configuration 1: shelf life bucket definitions

As with the aging report, the buckets are fully configurable. Each bucket requires:

- A **name** (e.g. "1–2 days", "3–4 days", "5–6 days", etc.).
- An **upper boundary** (days of remaining shelf life).
- A **lower boundary** (days of remaining shelf life).

The right bucket definitions depend on the nature of the products and the business's commercial agreements with customers. A business selling fresh food will need very fine daily buckets; one selling electronics with 2-year warranties may only need broad monthly ranges.

### Configuration 2: basis for remaining shelf life (RSL parameter)

The most important configuration decision for this report is the **basis on which remaining shelf life is calculated**. This is set via the **RSL 526** parameter, visible directly on the report header. There are two options:

**True expiry**
The remaining shelf life is calculated as: *physical expiry date − today*. The physical expiry date is derived from the production date plus the product master shelf life. This represents the date at which the product literally degrades beyond use.

**Stop sell**
The remaining shelf life is calculated as: *physical expiry date − minimum remaining shelf life the customer will accept − today*. This represents the date at which the product becomes commercially unsellable — not because it has physically expired, but because no customer will accept it with so little life remaining.

**Example:** if a product has a physical expiry date of day 100, but a customer mandates a minimum of 28 days remaining shelf life on delivery, the stop sell date is day 72. The product is effectively unsellable from day 72 onwards, even though it won't physically expire until day 100.

**Which to use:** stop sell is almost always the more operationally relevant choice for commercial planning purposes. It reflects the actual point at which stock becomes a write-off risk, not the theoretical physical expiry. The lesson notes this explicitly as the more meaningful basis for business planning.

---

## Lesson 17-05 — Auto Expiry

### What it is — and what it is not

Auto expiry is technically **not a report** — it is a **planning calculation** that feeds back into the inventory availability figure used by the rest of the model. It is covered in this exercise because it uses the same expiry date configuration as the remaining shelf life report and has a direct impact on what the planning model treats as usable inventory.

### The problem it solves

The inventory planning engine consumes stock on a **FIFO (First In, First Out)** basis — it always uses the oldest inventory first to meet demand. In isolation, this is sensible. But FIFO does not, by default, account for inventory that will **expire before demand can consume it**.

**Example from the lesson:** a DC holds 40,000 units of a 128GB tablet. The shelf life report confirms that 40,000 units are due to expire within the next 5–6 days. The demand for that product is not high enough to consume all 40,000 units within those 5–6 days. Without auto expiry, the model treats all 40,000 units as available and plans as though they will be consumed — this is phantom availability. In reality, a portion of that stock will expire unused and become worthless.

### Behaviour: auto expiry OFF vs. ON

| Setting | Behaviour |
|---|---|
| **Auto expiry OFF** | Expiry risk is ignored. All on-hand inventory is treated as available regardless of how close it is to its expiry date. The model plans as if all stock will be consumed before it expires. This produces overly optimistic availability projections. |
| **Auto expiry ON** | Units that are projected to expire before demand can consume them are **removed from available inventory in the period they expire**. In the lesson example, 17,000 units are flagged to expire in week 35 and are dropped from the availability calculation from that week onwards. The model then recognises the resulting shortfall and adjusts the replenishment plan accordingly. |

### The true expiry vs. stop sell toggle

Auto expiry uses the same two-option basis as the remaining shelf life report:

- **True expiry** — removes inventory from the available pool when it reaches its physical expiry date.
- **Stop sell** — removes inventory from the available pool when it reaches the stop sell date (physical expiry minus the customer's minimum required remaining shelf life). This removes more inventory, and earlier, than true expiry — because stock becomes commercially unusable before it physically expires.

Using stop sell gives a more conservative and operationally accurate picture of available inventory, but it will also trigger more replenishment orders to cover the earlier inventory removal.

### Why this is an implementation decision, not a default

Turning auto expiry on materially changes the inventory availability calculation and therefore the replenishment plan. It should be a deliberate, explicit configuration decision made during the implementation project — not something left at its default. The business needs to understand the commercial implication: enabling auto expiry will increase simulated replenishment requirements (because fewer units are counted as available), which has cost and supplier relationship implications.

---

## The Data–Reporting Dependency

A recurring theme across all four reporting areas is the relationship between **what data is available** and **what reporting is possible**. The lesson closes by making this explicit:

| Report | Minimum data required | Preferred data |
|---|---|---|
| Alerting / exception | Inventory quantities, demand plan | — |
| Inventory aging | Receipt date per lot | Production date per lot |
| Remaining shelf life | Expiry date per lot | Expiry date + customer minimum shelf life requirement |
| Auto expiry | Expiry date per lot | Expiry date + stop sell parameters |

The aging report cannot function at all without at least a receipt date. The shelf life report and auto expiry cannot function without expiry dates. These are **data requirements that must be defined upfront** with source system owners — typically ERP, WMS, or quality management systems — and built into the data integration design. Discovering mid-project that expiry dates are not available in the source system will block the shelf life and auto expiry capabilities entirely.

---

## Exercise 17 — Summary

| Step | Page | What you do | Key decision |
|---|---|---|---|
| 1 | Page 052 | Review the alerting / exception report | — |
| 2 | Page 950 | Configure KPI weights | Relative emphasis of each KPI on the combined score |
| 3 | Page 950 | Configure KPI thresholds | Good / neutral / bad boundaries per KPI; revisit if planning bucket changes |
| 4 | Page 522 | Review the inventory aging report | — |
| 5 | Manage Age Categories | Define age bucket names and day ranges | Right buckets for this organisation's product life cycle |
| 6 | Global Parameters | Set estimated production date basis | Production date / receipt date / receipt date − lead time |
| 7 | Page 526 | Review the remaining shelf life report | — |
| 8 | Shelf life bucket config | Define shelf life bucket names and day ranges | Right buckets for this organisation |
| 9 | RSL 526 parameter | Set basis for remaining shelf life | True expiry vs. stop sell |
| 10 | Page 240 / auto expiry toggle | Enable or disable auto expiry | Off / on (true expiry) / on (stop sell) |

---

## Key concepts

**Alerting / exception report** — a KPI-based prioritisation view (page 052) that scores each product × location combination on days-to-stock-out, inventory vs. target, and aging profile, combining them into a single priority score so planners can focus on the most critical combinations first.

**KPI weighting** — the relative emphasis placed on each KPI when calculating the combined prioritisation score. Set on page 950. Should reflect the organisation's commercial risk priorities.

**KPI thresholds** — the boundaries that define good / neutral / bad performance for each KPI. Set on page 950. Must be revisited if the planning bucket changes (weekly ↔ monthly).

**Inventory aging report** — a report (page 522) that groups on-hand inventory by age into configurable day-range buckets, showing how much stock has been sitting in the DC for how long.

**Age buckets** — configurable day-range groupings used to classify inventory age. Defined in Manage Age Categories. Must be tailored to each organisation.

**Estimated production date** — the Global Parameters setting that determines the reference start date for age calculations. Options: production date (preferred), receipt date, or receipt date minus lead time.

**Remaining shelf life report** — a forward-looking report (page 526) that groups on-hand inventory by days remaining until expiry, showing how much stock is at risk of expiring in the near term.

**Shelf life buckets** — configurable day-range groupings used to classify remaining shelf life. Must be tailored to each organisation's product life cycle and commercial agreements.

**True expiry** — the physical expiry date of a product, derived from its production date plus its master shelf life. The literal date it degrades beyond use.

**Stop sell** — the date at which a product becomes commercially unsellable, calculated as the physical expiry date minus the minimum remaining shelf life the customer will accept on delivery. Always earlier than true expiry, and usually the more operationally relevant basis for planning.

**Auto expiry** — a planning calculation (not a report) that removes inventory from the available pool in the period it is projected to expire, preventing phantom availability. Toggleable between off, on (true expiry basis), and on (stop sell basis). Enabling it increases replenishment requirements.

**FIFO (First In, First Out)** — the inventory consumption method used by the planning engine: oldest stock is always consumed first. Auto expiry complements FIFO by ensuring that stock which will expire before demand can reach it is removed from the available pool.

**Data–reporting dependency** — the principle that reporting capabilities are gated by data availability. Aging requires at minimum a receipt date; shelf life and auto expiry require expiry dates. These data requirements must be confirmed with source system owners at the start of the implementation project.

---

*Sources: raw transcripts 17-01 through 17-05 (raw/docs/)*
*Wiki summary: [[17-inventory-reporting]]*
