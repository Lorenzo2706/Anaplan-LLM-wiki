---
title: Line Item
type: concept
tags: [anaplan, fundamentals, module, blueprint, formula, format]
created: 2026-05-02
updated: 2026-07-08
sources:
  - wiki/sources/2026-05-02-anapedia-line-items-intro.md
  - raw/docs/Line items.md
  - raw/docs/Configure line items.md
  - raw/docs/Format line items.md
  - raw/docs/Apply styles to line items.md
  - raw/docs/Sum up line items into a parent.md
  - raw/docs/Cell count limit on line item blocks.md
  - raw/docs/Manage model size.md
  - raw/docs/Example Create EMP03 Employee Expenses by Country module.md
---

# Line Item

A **line item** is the atomic unit of calculation in an Anaplan module. Each line item holds values across the dimensions of its parent module.

## Core attributes

| Attribute | Purpose | Examples |
|---|---|---|
| **Format** | Data type of the cell values | Number, Boolean, Date, Time Period, List, Text, No Data |
| **Formula** | Optional expression deriving values from other line items | `Price * Volume` |
| **Summary** | How values aggregate at parent levels of a hierarchy | Sum, Average, Min, Max, None, Formula, Ratio |

## Classification by purpose

Line items are typically classified by what they do, which informs which kind of module they belong in (see [[wiki/patterns/disco|DISCO]]):

- **Input** — user-entered or imported. No formula.
- **Calculation** — derived. Has a formula referencing other line items.
- **Output** — surfaced to dashboards or downstream consumers.

## Data types

The **Format** of a line item determines what kind of data its cells hold and which functions and summary methods are valid.

| Format | Description |
|---|---|
| **Number** | Numeric values (integers or decimals). Default format. Supports all arithmetic, aggregation, and most functions. |
| **Boolean** | TRUE / FALSE. Used for flags, switches, access drivers, and conditional logic. |
| **Date** | A calendar date (day/month/year). Supports date arithmetic. Summary methods: Min, Max, First non-blank, Last non-blank. |
| **Time Period** | A reference to a time period in the model calendar (e.g. Jan 24, Q1 FY24). |
| **List** | A reference to a list item — used as a picklist to select a member of a specific list. Enables mapping and lookup patterns. Cannot contain a formula. |
| **Text** | Free-form string. Cells store characters; heavy use of text can increase model size. |
| **No Data** | Structural/heading line items that hold no cell data. Zero bytes per cell. Used as visual separators and section headers in Blueprint. |

> [!warning]
> Changing a line item's data type can cause data loss. For example, converting **Number** to **Text** may discard numeric values.

## Format options: numbers and dates

Number-formatted line items have additional sub-options configurable in Blueprint:

- **Decimal places** — fixed decimal display
- **Thousands separator** — for readability
- **Percentage display** — renders value ×100 with a % symbol
- **Currency symbol** — prefix a currency sign

Date-formatted line items can display in various regional date formats (DD/MM/YYYY, MM/DD/YYYY, etc.).

## Styles

Styles apply visual formatting to line items displayed **on rows** only (exception: **Summary1** can also apply to columns). Set in the **Style** column in Blueprint.

| Style | Key formatting changes |
|---|---|
| **Normal** | Default. Standard indentation, row height. |
| **Heading1** | Bold header, no indentation, double row height. |
| **Heading2** | Half-indented header, 1.5× row height. |
| **Heading3** | Italic header, 1.5× row height. |
| **Summary1** | Bold header, no indentation, double-lines top and bottom (or left/right for columns). |
| **Summary2** | Bold header, half-indented, thicker darker bottom border. |
| **Summary3** | Bold header, thicker darker bottom border. |

Styles are purely cosmetic — they do not affect calculation or data type.

## Summary method

The **Summary** column in Blueprint sets the [[Summary Methods|summary method]] — how a line item aggregates its values when a parent level of a list hierarchy is shown in rows or columns (or when a time period higher than the line item's time scale is shown).

- Default for Number and Boolean: **None** (parent cell is blank).
- Best practice: leave **None** unless aggregation is explicitly needed; unnecessary summaries multiply cell counts.
- See [[Summary Methods]] for the full method table and gotchas.

## Blueprint view

Blueprint is the configuration grid for a module's line items. Key columns:

| Column | What it controls |
|---|---|
| **Format** | Data type (see table above) |
| **Formula** | Expression for calculated line items |
| **Summary** | Aggregation method for parent hierarchy levels |
| **Applies To** | Narrows the list dimension for this line item; triggers a [[Subsidiary Views\|subsidiary view]] |
| **Time Scale** | Override the module's default time granularity for this line item |
| **Time Range** | Assign a specific model time range |
| **Versions** | Restrict the line item to specific versions |
| **Style** | Visual style for row display |
| **Cell Count** | Total cells across all blocks for this line item |
| **Populated Cell Count** | *(Polaris only)* Non-empty cell count |
| **Memory Used** | *(Polaris only)* Memory footprint |
| **Calculation Complexity** | *(Polaris only)* One-to-One / One-to-Many / All cells — impact on sparsity |
| **Calculation Effort** | % of total model computation effort |
| **Read / Write Access Driver** | Boolean line item that gates cell-level access (see [[01_access-drivers]]) |
| **Parent / Is Summary** | Defines line item hierarchy for summing into a parent |
| **Use Switchover** | Apply Switchover date to combine actuals and forecast |
| **Start of Section** | Change dimensionality of following line items without a subsidiary view |
| **Data Tags** | Group line items by tag |
| **Referenced By** | Shows which other line items reference this one |

## Cross-module formulas

A line item can reference line items from other modules in the same model using the syntax:
`'<Module Name>'.<Line Item Name>`

Example from REV03 Margin Calculation:
```
'REV02 Volume Inputs'.Volumes * 'REV01 Price Book'.Unit Price * (1 + Unit Price Growth %)
```

Aggregating with a mapping dimension (SUM selector pattern), from EMP03 Employee Expenses by Country:
```
'EMP02 Employee Expenses'.Salary[SUM: 'SYS08 Employee Details'.Country]
```

Same-module reference (no module prefix needed):
```
Revenue - Cost of Sales
```

## Line item hierarchy (summing into a parent)

Line items within a module can be organized into parent-child hierarchies:

- Assign a **Parent** to a line item in Blueprint; a sum formula is auto-generated on the parent.
- Mark the parent with **Is Summary**.
- A line item can belong to **multiple hierarchies** (multiple parents in different contexts).

Example:

| Line item | Formula | Is Summary |
|---|---|---|
| General Expenses | *(input)* | |
| Employee Expenses | *(input)* | |
| Total Expenses | `General Expenses + Employee Expenses` | ✓ |

## Cell count limit on line item blocks

Module data is stored in **blocks** — one block per combination of time period, version, and list hierarchy level for a line item. Each block has a hard limit of **2,147,483,647 cells**.

Cell count for a block = (list items at that level) × (other list items) — Time and Versions each create separate blocks rather than multiplying within a block.

**Implications:**

- Very large lists, combined with many versions and time periods, can push a block over the limit.
- If a change would exceed the limit, Anaplan blocks it and notifies the model builder.
- If write access to a list is controlled by model role, Anaplan **pre-allocates** extra cells in blocks for efficient recalculation when items are added/removed. Pre-allocated cells do not count toward workspace allowance or the visible cell count, but do count toward the block limit.

## Model size considerations

| Cell format | Bytes per cell |
|---|---|
| No Data | 0 |
| Boolean | 1 |
| Date | 4 |
| Time Period | 4 |
| List | 4 |
| Number | 8 |
| Text | 8 |

Key size-management rules:
- Set Summary to **None** unless aggregation is required — unnecessary summaries add cells.
- Use **line item subsets** instead of duplicating line items across modules.
- Modules with more than **~5 dimensions** should be split.

## Line items vs. list items

| | Line items | List items |
|---|---|---|
| Can contain formulas | Yes | No |
| Can be referenced by formulas | Yes | Yes |
| Scope | One module only | Any module in the model |

## Related

- [[Dimensions]] — line items are themselves a dimension axis
- [[Summary Methods]] — all summary method options and gotchas
- [[Subsidiary Views]] — triggered by Applies To / Time Scale changes on a line item
- [[Lists]] — the list data type and list items
- [[Picklists]] — list-formatted line items
- [[01_access-drivers]] — Read/Write Access Driver Blueprint columns
- [[wiki/patterns/disco]] — module classification pattern that builds on line item purpose

## Sources

- [[wiki/sources/2026-05-02-anapedia-line-items-intro]]
