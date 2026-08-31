---
title: Lists
type: concept
tags: [anaplan, lists, dimensions, hierarchy, properties, subsets]
created: 2026-05-13
updated: 2026-08-05
sources:
  - raw/docs/General lists.md
  - raw/docs/List types.md
  - raw/docs/List hierarchies.md
  - raw/docs/Configure lists.md
  - raw/docs/Create lists.md
  - raw/docs/Add and delete list items.md
  - raw/docs/Create list properties.md
  - raw/docs/Add formulas to list properties.md
  - raw/docs/List subsets.md
  - raw/docs/Create list subsets.md
  - raw/docs/Delete list subsets.md
  - raw/docs/Delete lists.md
  - raw/docs/Model actions.md
---

# Lists

A **list** is a named, ordered collection of items used as a [[07_dimensions|dimension]] in Anaplan modules. Lists group related business entities — employees, products, geographic regions, cost centers — and give module data its context. Workspace administrators create and manage general lists in the **General Lists** pane under Model Settings.

## What Lists Do

- Provide dimensions for modules: a list applied to a module becomes rows, columns, or a page selector.
- Supply picklist values: any line item or list property formatted as a list turns into a dropdown picker in the UX.
- Define hierarchy and rollup structure used by aggregation formulas (SUM, LOOKUP, etc.).

## List Items vs. Line Items

| Characteristic | List item | Line item |
|---|---|---|
| Belongs to | A list (shared across model) | One module only |
| Can contain a formula | No — list items are data, not calculations | Yes |
| Can be referenced by a formula | Yes | Yes |
| Used as a dimension | Yes | No (but a [[Line Item Subsets (LIS)|line item subset]] can act as one) |

> [!important]
> **Deleting a list item removes its data from every module that uses the list as a dimension.** There is no undo short of restoring a model history snapshot.

## List Types

| Type | Description | Key use case |
|---|---|---|
| Flat list | No hierarchy; all items at the same level | Transactional data, simple look-up tables |
| Simple list | Parent/child hierarchy within one list; drag-and-drop ordering | Org charts, product groups |
| Composite hierarchy | Multiple lists each rolling up to a parent list | Multi-level geographic/org structures (see [[04_composite-hierarchies]]) |
| Numbered list | Items identified by auto-incremented integer index, not name | Duplicate names, large datasets, external key integration (see [[15_numbered-lists]]) |
| List subset | Named subset of items from a parent list; used as a scoped dimension | Targeted calculations, filtering modules |

### Default Lists (system-provided)

Anaplan provides built-in lists that cannot be deleted:
- **Time** — periods driven by the model calendar
- **Versions** — Actual, Budget, Forecast, etc.
- **Users** — all workspace users; appears at the top of General Lists
- **Organization** — the org hierarchy list (marked *Is Organization*)

---

## List Item Order

A list's item order is a persisted property of the list itself — independent of item name or code — and it drives the default order everywhere the list is used as a dimension (module rows, page selectors, dropdowns) unless a view explicitly overrides it. It does **not** auto-sort, so a logical non-alphabetical sequence (e.g. amortization terms running "Geen afschrijvingen" → "5 jaar" → ... → "50 jaar") has to be set explicitly.

Two ways to set it:

- **Manual reorder** — open the list in General Lists (grid view), drag an item's row handle into position, or select item(s) and use Move Up / Down / To Top / To Bottom. Fine for small lists; item IDs and all references are untouched.
- **Order List action** — Actions → New Action → **Order list** (see [[Model Actions]]). Pick the list, a line item to sort by (numeric, text, or date), and Ascending/Descending; running the action re-sequences the list's native item order to match that line item's current values. This is the better option for larger lists, or whenever the order needs to be re-derived after the driving data changes — e.g. keep a numeric "sort code" line item in a properties module and re-run the action after updating it, instead of hand-dragging rows or renaming items with numeric prefixes.

> [!note]
> `Order list` sorts by the values of a chosen **line item**, not by item name/code — that's what makes a non-alphabetical logical order possible without renaming list items.

---

## List Hierarchy

A hierarchy lets parent items roll up data from their children. There are two patterns:

### Simple (single-list) hierarchy

Parent/child relationships are set within one list. Items at the lowest level (leaf items) hold data; all higher levels aggregate upward. You can only add data to child (leaf) list items — the top level is read-only aggregation.

### Composite hierarchy (multi-list)

Multiple lists are chained via **Parent Hierarchy** assignments:

```
G1 Region  ←  G2 Country  ←  G3 Location
```

Each child list's **Parent Hierarchy** field points to the list one level above. The top-most list carries a **Top Level** item (e.g., *All Regions*, *Total Company*) that summarizes the entire structure.

See [[04_composite-hierarchies]] for detail on how this works and why numbered lists are required for certain composite patterns.

### Top Level Item

- Represents the highest point in a list's own hierarchy.
- Data cannot be entered at the Top Level — it is always an aggregate of the items below.
- Can be set as the **default page selector** in the UX (overridable per user or per saved view).

---

## List Properties

List properties store **additional attributes of list items** — metadata that travels with the item rather than living in a module cell.

### Property formats

| Format | Description |
|---|---|
| Text | Free text string (also used for display names) |
| Number | Numeric value per list item |
| Boolean | True/false flag per list item |
| List | References another list (creates a picklist / enables LOOKUP/SUM mapping) |
| Date | A date value per list item |

### Formula properties

A list property can hold a formula that **pulls data from a module or line item** into the list. This is the only way to give a list item a computed attribute.

Common patterns:
- `'SYS08 Employee Details'.Name` — pulls a name from a system module into a display name property.
- `NAME(ITEM(Listname))` — captures current item names before converting to a numbered list.

> [!note]
> Unlike module line items, list property formulas must be applied at the property level (not the item level). The formula runs for every item in the list.

### Display Name Property

A special property (Text or List format) designated in General Lists as the **Display Name Property** for a numbered list. When set, list items show their display name in the UX instead of their numeric identifier. See [[15_numbered-lists]] for the full pattern.

---

## List Subsets

A **list subset** is a named, maintained selection of items drawn from a parent list. Subsets do not duplicate the items — they reference them.

### Why use subsets

- Scope a module to a smaller, relevant set of members (e.g., only Sales team members from a full Employees list).
- Reduce calculation volume and memory in large models.
- Allow different modules to use different slices of the same list without creating redundant lists.

### Key rules

- A list subset **cannot be used in the same module as its parent list**. Use one or the other as a dimension in any given module.
- A single list item can belong to **multiple subsets**.
- Subsets stay live: add/remove items from the parent list and the subset reflects the change (membership within the subset is still manually or import-managed, but the item pool updates automatically).
- Subset membership can be driven by a Boolean list property or line item formula, but there is **no automatic sync** — membership must be refreshed (manually or via import) when conditions change.

### Naming convention

Prefix subset names with `ls`, `sub`, or `ss` to distinguish them from the parent list (e.g., `ls Sales Team`).

---

## Key Rules and Gotchas

- **List item names are unique within a list** (max 60 characters). Use [[15_numbered-lists]] to handle duplicates or long names.
- **Deleting a list deletes all data associated with it** across all modules — this is irreversible without a model history restore.
- **Deleting a list item** removes its data from every dimensioned module cell. The **Next item index** does not reset after a delete; gaps accumulate until a manual index reset.
- **You cannot add data to a top-level item** — it is always a rollup aggregate.
- **PARENT and ISANCESTOR only work within a single list**. Cross-list ancestry requires a composite hierarchy pattern.
- Tree View supports viewing up to **1,000 items**; larger lists require Grid View.

---

## See Also

- [[07_dimensions]] — how lists, time, and versions combine to define module structure
- [[15_numbered-lists]] — integer-indexed lists for duplicates, large datasets, and external key integration
- [[04_composite-hierarchies]] — multi-list rollup structures
- [[Line Item Subsets (LIS)]] — analogous scoping mechanism for line items
- [[Model Actions]] — includes the **Order list** action used to re-sequence list item order
