---
title: Line Item Subsets (LIS)
type: concept
tags: [anaplan, line-item-subsets, LIS, collect, dimensions, aggregation]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Line item subsets.md
  - raw/docs/Create a line item subset.md
  - raw/docs/Line item subset example.md
  - raw/docs/Example Create line item subset LIS Multi-variance reporting.md
---

# Line Item Subsets (LIS)

A **line item subset (LIS)** is a named, ordered list of [[Line Item|line items]] drawn from one or more modules in the same model. It behaves like a [[Dimensions|dimension]] — it can be applied to a module's "Applies To" setting — and is the primary mechanism for cross-module aggregation via [[Aggregation Functions|COLLECT()]].

LIS have **no list properties** (unlike regular lists). They are a workspace administrator-only construct defined in Model Settings > Line Item Subsets.

---

## Use Cases

| Use Case | How LIS Enables It |
|---|---|
| Narrow a large set of line items | Pick a subset of items from one module so downstream views are smaller |
| Cross-module aggregation | Pull numeric line items from several modules into one staging module via `COLLECT()` |
| Variance / multi-metric reporting | Feed a reporting module with hand-picked KPIs from different calculation modules |
| Picklist on a line item | Use LIS as the list source for a line item with List data type pointing to a LIS |
| Currency conversion | Group income-statement line items so a single conversion block can iterate over them |
| Cash-flow forecasting | Collect invoiced-amount line items to convert to cash timing |

---

## Constraints

> [!warning] These constraints are absolute — violations cause build errors or silent data issues.

- **Numeric data types only.** A LIS cannot include line items with Boolean, Text, Date, List, or No Data types.
- **Only simple subtotal formulas transfer.** If a parent line item has a formula (e.g. `Salary + Bonus + Car Costs + Phone Costs + Medical Costs`), only the children actually present in the LIS contribute to the parent's value inside modules dimensioned by that LIS. If *none* of a parent's summed children are in the LIS, the parent appears as a leaf item (its formula is dropped).
- **Styles do not transfer.** Cell formatting, number formats, and custom styles on the source line items are not carried over to the LIS.
- **One LIS per module.** You can only use one line item subset as a dimension in any given module (set in the "Applies To" column in Modules settings).
- **Common dimension required for COLLECT().** When the LIS spans line items from multiple modules, those modules must share at least one common [[Dimensions|dimension]] for `COLLECT()` to work correctly. Lacking a common dimension won't always throw an error but will produce incorrect or missing values.
- **No list properties.** LIS items cannot carry properties the way regular list items can.

---

## How to Create a LIS

Requires workspace administrator role. Steps performed in **Model Settings > Line Item Subsets**:

1. Select **Line Item Subsets** in the model settings bar.
2. Select **Insert**, then type a name (e.g. `LIS: Multi-variance reporting`). Add multiple LIS by entering each on a new line.
3. Choose **Before / After** an existing LIS, or **Start / End** of the list. Select **OK**.
4. In the **Modules** column of the new LIS row, double-click (or select the ellipsis) and select the source modules containing the line items you want. Select **OK**.
5. Select the LIS row, then select **Open**.
6. Check the line items to include. Selections save automatically.

The LIS is now available to use as a dimension ("Applies To") in any module, as a picklist source, or as the target list for a `COLLECT()` formula.

---

## LIS as a Module Dimension

When a LIS is assigned to a module's **Applies To** column, the module gains an extra dimension whose members are the selected line items. This transforms the module's grid: rows (or columns) now iterate over the LIS members rather than being static line items.

Key structural implication: the module's line items become the *measures* across each LIS member. This is how a single `COLLECT()` line item can pull values for Margin, Salary, Rent, etc. all in one module without separate line items per metric.

> [!note] Only one LIS may be applied per module. You cannot stack two LIS as dimensions.

---

## COLLECT() Pattern with LIS

`COLLECT()` is the natural partner function for LIS. When a module is dimensioned by a LIS, `COLLECT()` automatically routes each LIS member back to its source module and pulls the correct value.

**Formula pattern (in a module dimensioned by the LIS):**

```
COLLECT()
```

No arguments are needed — Anaplan resolves the source module and line item for each LIS member automatically, as long as all source modules share a common dimension with the target module.

See [[Aggregation Functions]] for full `COLLECT()` syntax and engine-specific behavior (Classic vs Polaris).

---

## Variance Reporting Example (SYS11 / REP05 / REP06)

This is the canonical Anapedia worked example for LIS. The goal: a UX board where a user picks two months and sees variance per country for a mix of P&L metrics.

### LIS: Multi-variance reporting

Three source modules, all sharing the **G2 Country** list as a common dimension:

| Source Module | Line Items Included |
|---|---|
| **REV03 Margin Calculation** | Revenue, Cost of Sales, Margin, Margin % |
| **EMP03 Employee Expenses by Country** | Headcount, Salary, Bonus, Car costs, Phone costs, Medical costs, Total Employee Expenses |
| **OTH01 Non Employee Expenses** | Shipping costs, Rent, Utilities, Shared costs, Total |

### Module chain

```
SYS11 Time Variance Reporting   ← input module (user selects Month 1, Month 2)
         ↓
REP05 Variance Report Staging   ← uses COLLECT() + LIS dimension, pulls multi-module data
         ↓
REP06 Variance Report           ← final output; calculates variance between the two months
         ↓
UX Board: Variance Report       ← two cards: month selector + variance grid
```

- **SYS11** holds two line items (Month 1, Month 2) with Time-period data type, driven by user selection.
- **REP05** is dimensioned by the LIS and by G2 Country. Its `COLLECT()` line item pulls from REV03, EMP03, OTH01 in a single formula.
- **REP06** references REP05 for Month 1 and Month 2 values and calculates the delta.

This pattern is a strong example of [[Variance Reporting]] and demonstrates why LIS + COLLECT() is preferred over duplicating line items across reporting modules.

---

## Partial Parent Recalculation

When a parent line item is in the LIS but only some of its children are:

- The parent's value recalculates using **only the children present in the LIS**.
- Example: `Total Expenses = Salary + Bonus + Car Costs + Phone Costs + Medical Costs` in the source. If the LIS includes `Total Expenses`, `Salary`, `Bonus`, `Car Costs` but not `Phone Costs` or `Medical Costs`, then inside the LIS-dimensioned module: `Total Expenses = Salary + Bonus + Car Costs`.
- If **none** of a parent's summed children appear in the LIS, the parent becomes a leaf item (shows its stored value, formula dropped).

---

## Gotchas and Tips

> [!warning] LIS + COLLECT() requires a shared dimension. If source modules diverge on dimensions (e.g. one has Employees, another doesn't), COLLECT() results will be blank or incorrect for those members. Always confirm common dimensions before building the LIS.

- **Naming convention:** Prefix with `LIS:` (e.g. `LIS: Income Statement KPIs`) to make LIS immediately recognizable in the Applies To dropdown.
- **One LIS per module limit:** Design reporting modules to need only one LIS. If you need to group metrics from two different LIS, flatten them into a single LIS or use a different aggregation pattern.
- **Style loss:** If source line items have custom formatting that matters for user-facing display, reapply styles in the target module's blueprint.
- **Numeric-only restriction:** Boolean flags, text labels, and date fields cannot be in a LIS. If you need them alongside numeric data, keep them as separate line items in the reporting module.
- **Re-check LIS membership after model changes:** Adding or renaming source line items does not automatically update LIS membership. Manually verify after structural changes to source modules.
- **Picklist use:** A line item with a LIS as its list type lets users select a specific LIS member as a value — useful for "select a metric" type UX interactions (e.g. driving a chart series).

---

## Related

- [[Line Item]] — individual line items that make up a LIS
- [[Dimensions]] — LIS functions as a dimension type
- [[Modules]] — Applies To column where LIS is assigned
- [[Aggregation Functions]] — COLLECT() function
- [[Variance Reporting]] — canonical LIS use case
