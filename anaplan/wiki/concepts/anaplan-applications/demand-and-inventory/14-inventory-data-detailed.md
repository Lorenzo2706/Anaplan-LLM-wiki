# Exercise 14 — Importing and Managing the Inventory Data

**Series:** Anaplan Demand & Supply Chain Reference App
**Chapter:** 14 of 17
**Lessons:** 14-01 through 14-05

---

## Overview

Exercise 14 continues the initialization of the **inventory planning model**. The previous exercise (13) completed the import of the demand plan. This exercise adds the remaining transactional data sets needed to build a complete inventory picture: **on-hand DC inventory** and **open supplier purchase orders (POs)**.

By the end of the exercise, the planner can see all three key inputs — demand, on-hand inventory, and incoming POs — combined into a single projected inventory calculation on page 240.

The exercise follows four logical stages:

1. Import the transactional data into the **Data Hub**
2. Transfer it to the **Supply Planning / Inventory Planning model**
3. Review and configure the data inside the Inventory Planning app
4. Confirm the **forecast consumption** setup

---

## Lesson 14-01 — Overview

### Context and scope

The demand plan has already been imported (Exercise 13). The remaining data sets needed for inventory planning are on the transactional, supply side. In practice, several supply data sets could be relevant:

- On-hand DC inventory
- Open supplier purchase orders
- In-transit inventory between DCs
- Open intercompany orders (transfers placed on another DC, not yet processed)

For this exercise, only the two most fundamental are in scope: **DC inventory** and **open supplier POs**. The others follow the same pattern and are left as optional extensions.

### Steps at a glance

| # | Action | Location |
|---|--------|----------|
| 1 | Import DC inventory and PO data | Data Hub — page 108 |
| 2 | Push data to Supply Planning model | Data Hub — section 240 |
| 3 | Review available inventory (status codes) | Inventory Planning — page 204 |
| 4 | Review and configure open POs | Inventory Planning — page 202 |
| 5 | Validate the combined inventory picture | Inventory Planning — page 240 |
| 6 | Configure forecast consumption | Inventory Planning — page 900 |

---

## Lesson 14-02 — Import Inventory and PO Data into the Data Hub

### Where to work

Navigate to the **Data Hub application**, page **108 — Update Transactional Data**. This is the standard entry point for all supply-side transactional imports.

### Step 1 — Import DC inventory

1. On page 108, locate the **DC inventory** data set in the list of available supply data sets.
2. Navigate to the **Exercise 14** source folder and select the DC inventory file.
3. Run the import process.

### Step 2 — Import open supplier POs

1. On the same page 108, locate the **open supplier purchase orders** data set.
2. Select the corresponding file from the Exercise 14 folder.
3. Run the import process.

### What the imported data looks like

Once imported, the inventory data is visible in the Data Hub for a quick review. The key characteristics to note:

- **Lot-level granularity:** the inventory table contains multiple rows for the same product at the same location. What distinguishes each row is a lot-specific attribute — in this example, the **expiry date**. Other distinguishing attributes might be batch number, status code, or production date.
- **Fields visible per record:** quantity, location, product, expiry date, status code, and any other lot attributes loaded from the source system.

This lot-level structure is intentional: it allows the Inventory Planning app to report and plan against specific lot characteristics, most importantly expiry dates, which are needed for the shelf-life and aging reports in Exercise 17.

---

## Lesson 14-03 — Move Data to the Supply Planning Model

### Where to work

Remain in the **Data Hub application**, section **240 — Update Data**.

### Step 3 — Push open supplier POs

1. Scroll down in section 240 to find the **open supplier purchase orders** push process.
2. Run it. The process transfers PO data from the Data Hub into the Inventory Planning app.

### Step 4 — Push on-hand inventory

1. Still in section 240, find the **update inventory** process.
2. Run it. This transfers the on-hand DC inventory data.

Once both processes have completed, all work in the Data Hub is done. The data is now available in the Inventory Planning application for review and configuration.

---

## Lesson 14-04 — Review the Data in Inventory Planning

Move to the **Inventory Planning application**. There are three pages to visit, each paired with a specific configuration decision.

---

### Page 204 — Manage Available Inventory

#### What it shows

A summarized view of all the on-hand inventory the application now knows about, aggregated across products and locations.

#### Configuration decision: inventory status codes

Not all physical inventory is usable for meeting customer demand. Some stock may be damaged, quarantined, on hold, or otherwise unavailable. The application allows you to control which inventory is treated as "available" by mapping **status codes** to an inclusion/exclusion flag.

**Example:** if the source system tags damaged inventory with a specific status code, that code should be excluded here. Including it would falsely inflate the available inventory figure and lead to stock-outs the system didn't anticipate.

**Action:** review the list of status codes present in the imported data and mark each one as either available or excluded, according to business rules.

---

### Page 202 — Open Purchase Orders

#### What it shows

- **PO headers:** a list of all open supplier POs, showing PO date, destination location (which DC the PO is directed to), and the number of lines on each PO.
- **PO lines (drill-down):** the individual products and quantities within each PO.

At the top of the page there is a **scenario selector**. For this configuration exercise, switch from the committed scenario to **Scenario 1** in order to explore the PO configuration options without affecting the baseline.

#### Configuration decision: how much PO data to include

This is the primary configuration choice on this page. It controls how open POs flow into the inventory calculation, and it is set per scenario. There are three options:

| Setting | Behavior |
|---------|----------|
| **No** | All open POs are excluded. Use for what-if simulations where you want to see the inventory position as if no POs will be honored. |
| **Yes — all** | Every open PO is included, regardless of its expected receipt date. This is the typical production setting. |
| **Yes — future receipts only** | Only POs whose expected receipt date falls in the current or a future period are included. POs that are already late (receipt date before the current period) are excluded. |

**The late PO edge case:** when "Yes — all" is selected, a PO whose expected receipt date has already passed is pulled into the **first forecasted period** (the current period), rather than being dropped. This is a pragmatic choice: the PO is still open, so it is assumed to arrive as soon as possible.

**Which to use:** the "future receipts only" option is useful when the business wants a conservative view that does not credit late deliveries. "Yes — all" is appropriate when late POs are still expected to arrive and should be counted toward the plan.

---

### Page 240 — DC Inventory Planning

#### What it shows

This is the main inventory planning view. With data now imported and configured, all three demand-and-supply inputs should be visible together for a selected DC:

- **Demand baseline** — the forecasted customer demand the DC must meet, period by period.
- **Open supply PO spikes** — the two upward spikes in the supply line correspond to the incoming supplier POs. These are also visible in the detail table below the chart.
- **Calculated new receipts** — replenishment orders the model calculates beyond the open-PO horizon (covered in a later exercise).
- **Inventory balance** — the projected on-hand position: it starts from the opening balance, depletes as demand consumes it, spikes up when new receipts arrive, and continues to deplete.

#### Success criterion

Reaching this view with a coherent demand + inventory + PO picture is the explicit success criterion for Exercise 14. If page 240 shows the combined projection for the selected DC, the data import phase is complete.

---

## Lesson 14-05 — Confirm Forecast Consumption

### Where to work

**Inventory Planning application**, page **900 — Global Parameters**, under the "Application Configuration" section. Scroll down to find the **Consumption Method** parameter.

### What forecast consumption does

Forecast consumption reconciles two parallel views of demand:

- **The demand plan** — a forecasted, planning-based view of what customers are expected to order.
- **Committed customer demand** — the actual open sales orders that customers have placed (transacted demand).

For any given period, the consumption process calculates:

> **Unconsumed forecast = Demand plan − Committed customer orders**

This tells the inventory planner how much of the planned demand has not yet been backed by actual orders. The breakdown is visible alongside the demand plan so the planner has clear sight of what is certain versus what is still a planning assumption.

**Example from the lesson:** if the demand plan for a week is **2,200 units** and open customer sales orders total **1,960 units**, the unconsumed forecast is **240 units** (the transcript shows 277 due to rounding elsewhere in the model).

### Configuration: consumption method

The parameter must be set to one of the active methods — it should not be left off unless forecast consumption is being handled in the Demand Planning model upstream.

| Method | Behavior |
|--------|----------|
| **Same period only** | If committed demand exceeds the plan in a period, the excess is shown as a spike in that period only. The unconsumed forecast for that period goes to zero. Demand in surrounding periods is unaffected. |
| **Forwards** | If committed demand exceeds the plan in a period, the excess "consumes" forecast from future periods as well. The spike effectively absorbs multiple forward periods of planned demand. |

**When does the choice matter?** The difference between the two methods is most visible when committed demand is **larger than the plan** for a period. For example, if the plan is 2,200 but a large order arrives for 5,000 (a spike of 6,900 in the example, accounting for the base plan):

- With **Same period only**, the spike sits in that one period. Future weeks remain fully unconsumed.
- With **Forwards**, the 5,000+ is spread forward and consumes week 20, week 21, and part of week 22 — equivalent to roughly 2.5 weeks of demand absorbed into that single spike.

The right choice depends on the commercial dynamics of the business. A make-to-order business where large orders represent future-week demand pulled forward may need Forwards; a steady-rate replenishment business may prefer Same period only.

### Critical interlock: where consumption runs

Forecast consumption must run in **exactly one place** in the planning chain — either at the end of Demand Planning or at the start of Inventory Planning. Running it in both places would cause double consumption.

- If Demand Planning has already performed forecast consumption, the Inventory Planning model receives a **signal** from Demand Planning and will not allow it to be applied again here.
- In Exercise 13 (just prior), consumption was explicitly **switched off** in the Demand Planning model so that it can be applied here in Exercise 14. This is why the setting needs to be confirmed in this step.

**Action:** verify the Consumption Method is set to the appropriate active method (Same period only or Forwards). Do not leave it off unless it is confirmed that Demand Planning is handling consumption.

---

## Exercise 14 — Summary

| Step | Page | What you do | Key decision |
|------|------|-------------|--------------|
| 1 | Data Hub p.108 | Import DC inventory | — |
| 2 | Data Hub p.108 | Import open supplier POs | — |
| 3 | Data Hub s.240 | Push PO data to Supply Planning | — |
| 4 | Data Hub s.240 | Push inventory to Supply Planning | — |
| 5 | Inv. Planning p.204 | Review available inventory | Which status codes count as available |
| 6 | Inv. Planning p.202 | Review open POs | No / Yes all / Yes future only |
| 7 | Inv. Planning p.240 | Validate combined inventory picture | Success criterion: projection is visible |
| 8 | Inv. Planning p.900 | Set forecast consumption method | Same period only / Forwards / Off |

---

## Key concepts

**Lot-level inventory** — inventory stored at sub-SKU granularity, where multiple records share the same product and location but differ on attributes such as expiry date or batch number. Required to enable expiry-aware planning and reporting.

**Status codes** — tags on inventory records that classify stock condition (e.g. available, damaged, on hold). Used on page 204 to control which inventory is treated as usable.

**Forecast consumption** — the reconciliation process that compares the statistical/planning demand forecast against actual committed customer orders, producing an "unconsumed" residual that represents the still-uncertain portion of demand.

**Same period only vs. Forwards** — the two active consumption methods, differing in whether an oversized committed demand spike absorbs only its own period's forecast or spills forward into future periods.

**The consumption interlock** — a model-level signal that prevents forecast consumption from running in both Demand Planning and Inventory Planning simultaneously.

---

*Sources: raw transcripts 14-01 through 14-05 (raw/docs/)*
*Wiki summary: [[14-inventory-data]]*
