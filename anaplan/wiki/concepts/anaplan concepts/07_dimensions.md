---
title: Dimensions
type: concept
tags: [anaplan, fundamentals, dimensions, module, lists]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Dimensions  Anapedia.md
  - raw/docs/Page selectors and nested dimensions.md
  - raw/docs/Subsidiary views.md
  - raw/docs/Configure line items.md
---

# Dimensions

**Dimensions** are the lists that give a module its row, column, and page structure. Every cell in a module has a unique context determined by exactly one member from each active dimension. Without dimensions, a module has no axes and cannot hold structured data.

> [!note]
> The data in a cell has meaning *because* of the context given by its dimensions. Remove a dimension and the model loses that axis of granularity entirely.

## Types of dimension

| Type | Description |
|---|---|
| **General lists** | User-created lists in the General Lists pane. The most common source of custom dimensions (e.g. Products, Countries, Cost Centers). List subsets can also be used as dimensions to narrow scope. |
| **Time** | A default dimension present in every model. Configured in its own pane with calendar type, granularity, and time ranges. |
| **Versions** | A default dimension present in every model. Configured in its own pane (e.g. Actual, Budget, Forecast). |
| **Users** | A default dimension present in every model. Enables per-user data scoping. |
| **Organization** | A default list, pre-configured with a **Total Company** top-level item. Behaves like a general list but ships with every model. |
| **Line items / line item subsets** | The line items of a module themselves act as one dimension (typically columns). A [[Line Item Subsets (LIS)\|line item subset]] — a curated collection of line items from one or more modules — can replace the full line-items dimension to narrow the visible set. |

### Default dimensions

Time, Versions, Users, and Organization exist in every model and **cannot be deleted**. They are always available as dimensions.

- **Organization** is configurable in General Lists. **Total Company** is automatically set as the top-level item.
- **Time**, **Versions**, and **Users** each have their own Model Settings pane with richer configuration than a plain general list.

## How dimensions define cell context

Each cell is the intersection of exactly one member per active dimension. Example — *Country Margin Report* module:

- **Pages:** Time (FY22), Countries (Germany)
- **Rows:** Products (Chocolates, Sours, Taffy, Fudge, All Products)
- **Columns:** Line items (Revenue, Cost of Sales, Margin, Margin %)

The cell at row **Chocolates** / column **Revenue** holds the value **2,675,773** — which is *Revenue from Chocolates sold in Germany in FY22*. Change any page selector and the entire grid re-renders to a new context slice.

## Pivoting

You can **pivot** dimensions to move them between rows, columns, and pages at any time:

- **Rows** and **Columns** — data renders as a grid.
- **Pages** — a dimension moved to pages becomes a **page selector** (dropdown above the grid); only one member's data is visible at a time.

Any user can pivot within their browser session. Workspace administrators can set the default layout for a module or saved view.

## Placing multiple dimensions: nested vs. page selectors

| Placement | Behaviour | Practical limit |
|---|---|---|
| **Nested on rows/columns** | Members of outer dimension group rows/columns; inner dimension expands within each outer member. | Classic: up to 3 dimensions per axis. Polaris: up to 8. |
| **Page selector** | Single-item dropdown; grid shows data for the selected member only. | One page selector per dimension; unlimited dimensions on pages. |

> [!tip]
> For large datasets, prefer page selectors over deep nesting — nested grids with many items are hard to read and slow to render.

## Applies To — controlling per-line-item dimensionality

The **Applies To** column in Blueprint lets you assign a *different* (usually narrower) list to an individual line item, instead of the module's default dimension. This automatically creates a [[Subsidiary Views|subsidiary view]] for that line item.

Use **Start of Section** in Blueprint to change the dimensionality of a *block* of consecutive line items without creating separate subsidiary views for each — useful when a subset of the module's logic operates on a list subset (e.g. Profit Centers inside an Organization hierarchy).

## Practical rules and constraints

- A module's dimensions are set when it is created; they can be changed in the **Applies To** field of the Modules pane or in Blueprint.
- Keep total dimension count low: **if a module has more than ~5 dimensions, consider splitting it**.
- Increasing dimensions multiplies cell count dramatically — always evaluate the cell count impact before adding a new dimension.
- List **subsets** as dimensions are a key tool to reduce cell counts: only the members in the subset occupy cells, not the full list.

## Cross-references

- [[Line Item]] — a line item is both a unit of data and a dimension axis
- [[Lists]] — the raw building block most dimensions are drawn from
- [[Line Item Subsets (LIS)]] — curated subsets of line items usable as a dimension
- [[Versions]] — the Versions default dimension and its role in scenario planning
- [[Subsidiary Views]] — what happens when a single line item has different dimensionality from its module
- [[Summary Methods]] — how aggregation works when a dimension has a parent-child hierarchy
