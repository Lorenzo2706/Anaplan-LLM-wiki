---
title: Numbered Lists
type: concept
tags: [anaplan, numbered-lists, lists, dimensions, CODE, NAME, FINDITEM, composite-hierarchies]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Numbered lists.md
  - raw/docs/Numbered lists and functions.md
  - raw/docs/Convert lists to numbered lists.md
  - raw/docs/Create display names for numbered lists.md
  - raw/docs/Preserve list item names in numbered lists.md
  - raw/docs/Use numbered lists in composite hierarchies.md
  - raw/docs/Reset the list index.md
---

# Numbered Lists

A **numbered list** is a list in which each item is identified by an **auto-incremented integer index** rather than a user-supplied name. The integer is the item's true identity; any human-readable label is stored separately as a **display name** list property.

Naming convention: prefix the list name with `#` (e.g., `#Employees`, `#Transactions`) to distinguish it from companion named lists.

---

## Why Use a Numbered List

| Scenario | Why numbered lists help |
|---|---|
| Duplicate display names needed | Multiple items can share the same display name; the integer index keeps them distinct |
| Item names exceed 60 characters | List item names are capped at 60 chars; display names have no such limit (e.g., long SKUs) |
| Integration with external systems | External systems often use numeric primary keys; the integer index maps cleanly to those keys |
| Large, frequently changing datasets | Append-only integer keys are stable; no name collision risk on import |
| Composite hierarchy leaf nodes | Numbered lists are required when multiple child lists roll up to one parent (see [[04_composite-hierarchies]]) |

---

## How the Index Works

- When a numbered list item is created, it receives the next available integer (the **Next item index** shown in General Lists).
- The index is **never reused** after a delete — gaps accumulate. Deleting items does not decrement the counter.
- The maximum index value is **999,999,999**. Anaplan sends a notification as this limit approaches.
- Items display in the model as `#1`, `#2`, `#3`, … unless a display name property is set.

> [!note]
> The auto-generated integer index is conceptually distinct from the **Code** field. The Code field may hold an external system identifier (e.g., staff number), while the index is Anaplan's internal identifier.

---

## Display Names

A display name is a **Text** or **List**-formatted list property designated as the list's display name in General Lists. When set, it replaces the numeric label (`#1`, `#2`, …) in the UX.

- More than one item can share the same display name (this is the primary use case).
- In **Tree View**, duplicate display names disambiguate with the index in brackets: `Rajesh Patel (#1)`, `Rajesh Patel (#3)`.
- Everywhere else (modules, dropdowns) duplicates show only the display name without disambiguation.

### Display name property formats

| Format | Use case |
|---|---|
| Text | Free-text display name typed directly or populated via formula |
| List | Display name sourced from another list (enables picklist selection and LOOKUP/SUM mapping) |

---

## Key Functions for Numbered Lists

| Function | Formula example | What it does |
|---|---|---|
| `NAME` | `NAME(ITEM(#Transactions))` | Converts the numbered item to its text representation (display name or index string) |
| `FINDITEM` | `FINDITEM(#Employees, Employee Search)` | Finds a numbered list item by its code or auto-generated identifier; the search line item must be Text |
| `SELECT` | `Sales.Gross Sales[SELECT: #Products.'#20']` | Selects a specific numbered item by its unique identifier |
| `LOOKUP` | `People Details.Days Available[LOOKUP: #Resources.Employees]` | Maps through a list-formatted property to look up values; use with list-format properties |
| `SUM` | `Project Days.Days Booked[SUM: #Resources.Employees]` | Aggregates through a list-formatted property; use with list-format properties |

> [!important]
> `FINDITEM` and `SELECT` require the item's **unique identifier** (the auto-generated integer code), not its display name.

---

## Converting a Named List to a Numbered List

Conversion is **one-way and irreversible** — there is no revert path once a list is numbered.

### What happens on conversion

- All existing item names become integers (`#1`, `#2`, …).
- If the list is part of a **composite hierarchy**, conversion removes any parent list items from the converted list (the top-level item is preserved).
- Any formulas referencing the old item names by string may break.

### Preserving names before conversion

Use this pattern to capture current names as display names before the conversion destroys them:

1. Create a Text-format list property on the list (e.g., `Display name`).
2. Enter the formula `NAME(ITEM(Listname))` in the property's Formula column — this populates the property with the current string name for each item.
3. Verify the names appear in Grid View's Display name column.
4. **Remove the formula** (the values are now static data, not driven by a formula).
5. Proceed with the conversion to numbered.
6. After conversion, set the property as the **Display Name Property** in General Lists.

Items added to the numbered list after conversion will not have a display name — they appear as raw numbers until one is manually assigned or imported.

---

## Resetting the List Index

The **Next item index** only ever increments — deletes leave gaps. If a list accumulates large gaps (e.g., after a bulk delete and re-import cycle) or approaches the 999,999,999 limit:

1. Remove **all items** from the entire list hierarchy.
2. Use **Configure > Reset** in the list's settings to reset the index to 1.
3. Re-import items; numbering restarts from 1.

> [!warning]
> Resetting the index after items have been exported or referenced by external systems can cause key mismatches. Only reset when the list is truly empty and external references are also cleared.

In deployed models, index reset is only available for **production lists**.

---

## Using Numbered Lists in Composite Hierarchies

A numbered list can participate in a composite hierarchy as a **child list**. Assign the parent list in the numbered list's **Parent Hierarchy** configuration:

```
Departments (named list)  ←  #Employees (numbered list)
```

Each numbered employee item rolls up to its assigned Department parent. PARENT and ISANCESTOR will resolve correctly within the composite structure because all hierarchy resolution operates on the shared item index.

See [[04_composite-hierarchies]] for the full multi-list rollup pattern.

---

## Gotchas

- **Cannot revert**: once a list is numbered, there is no UI path to make it non-numbered.
- **CODE vs. index**: the auto-generated integer index and the item's Code field are separate. `FINDITEM` uses the Code or the auto-generated identifier — confirm which your import populates.
- **Display names are cosmetic only**: formulas and LOOKUP/SUM mappings operate on the integer index (or list-formatted properties), never on display name text.
- **Duplicate display names are invisible outside Tree View**: end users cannot distinguish two items with the same display name in a module dropdown unless Tree View is used.
- **Items added post-conversion have no display name**: they appear as raw integers until manually or import-assigned.
- **Index gaps are permanent** until a full reset: deleting 500 items and re-adding 500 new ones leaves the counter at the prior high-water mark plus 500.

---

## See Also

- [[11_lists]] — list fundamentals, types, properties, and subsets
- [[04_composite-hierarchies]] — how numbered lists enable multi-list rollup structures
