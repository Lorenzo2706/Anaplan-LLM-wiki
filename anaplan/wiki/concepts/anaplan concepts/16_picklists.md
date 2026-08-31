---
title: Picklists
type: concept
tags: [anaplan, picklists, list-formatted-line-items, filtered-picklists, one-to-many, many-to-many, selective-access, dimensions]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Picklists  Anapedia.md
  - raw/docs/Set picklists on line items.md
  - raw/docs/Create one-to-many filtered picklists.md
  - raw/docs/Create many-to-many filtered picklists.md
  - raw/docs/Actions and filtered picklists.md
  - raw/docs/Selective access and picklists.md
---

# Picklists

## What a Picklist Is

A picklist is a **list-formatted line item** — a line item whose data type is a reference to a list item rather than a numeric, text, or Boolean value. When a user clicks the cell, a dropdown appears showing valid list items to choose from.

The cell stores a **list item reference** (a pointer to a member of a list), not a calculated value. This makes picklists fundamentally different from formula-driven line items — the value is user-selected, not computed.

Key constraint: **a list-formatted line item cannot contain a formula**. If you add a formula to a list-formatted line item, the picklist behavior is disabled.

## Why Picklists Matter for Model Design

Picklists are the mechanism for **linking entities across modules**. They enable:

- Mapping employees to departments, products to categories, cost centers to legal entities.
- Driving lookups and hierarchical aggregations via list references.
- Implementing user-guided data entry where the valid values are controlled.

A line item formatted on a list is also used in [[17_selective-access|Selective Access]] filtering, [[08_dynamic-cell-access|DCA]] user mapping, and filtered picklist chaining.

## Types of Picklists

### Simple Picklist

A line item formatted on a list, list subset, or line item subset. The dropdown shows all items in the referenced list (subject to SA filtering).

Use case: Assign an employee to a department; select a cost center for a transaction.

### Filtered Picklist

A filtered picklist restricts the dropdown items based on context — specifically, based on the value selected in a **driver** line item in the same row. Two sub-types:

| Type | Relationship | Structure needed |
|---|---|---|
| One-to-many | One driver item → multiple filter items | Driver property added directly to the filter list |
| Many-to-many | Multiple driver items ↔ multiple filter items | Separate valid combinations (junction) list required |

## One-to-Many Filtered Picklists

### Concept

Each item in the filter list is linked to exactly one driver item via a list property. The dropdown shows only filter list items whose driver property matches the current driver selection.

Example:
- Driver list: **Role** (Executive, Senior Director, Team Leader)
- Filter list: **Compensation Plan** (Plan A, Plan B, Plan C, Plan D)
- Each Compensation Plan item has a **Role (driver)** property pointing to its eligible role
- When a user selects "Senior Director" in the Role line item, only Plan B and Plan C appear in the Compensation Plan dropdown

### Structure

- Add a list property to the filter list, formatted on the driver list.
- Map each filter list item to its corresponding driver item in Grid View.
- In the module's filter line item Format dialog, select **Dependent** and specify the driver list.

### Constraint

One-to-many means each filter item maps to **one** driver item. If a compensation plan is valid for multiple roles, you need many-to-many instead.

## Many-to-Many Filtered Picklists

### Concept

Multiple driver items can map to multiple filter items. This requires a **valid combinations list** (a junction list) that explicitly maps every valid driver-filter pair.

Example:
- Driver: **Role** (Executive, Senior Director, Senior Manager)
- Filter: **Compensation Plan** (Plan A, Plan B, Plan C)
- Valid combinations list: **Compensation Plan Lookup** with items like "Role Compensation 1" (Executive → Plan A), "Role Compensation 2" (Senior Director → Plan A), "Role Compensation 3" (Senior Director → Plan B), etc.

### Structure

The valid combinations list has two list properties:
- A property formatted on the **driver list**
- A property formatted on the **filter list**

Each item in the combinations list represents one valid pairing. Multiple pairings per driver item are allowed (that's the "many-to-many").

The combinations list is typically a **numbered list** with the driver list as its parent hierarchy. This allows the Assign action to manage it.

In the module, the filter line item Format dialog: select **Dependent**, filter based on the driver list (via the combinations list's parent hierarchy).

### Assign Action for Many-to-Many Management

The **Assign** action simplifies maintaining a many-to-many valid combinations list:

1. Set the combinations list as a numbered list with the driver list as parent hierarchy.
2. Create the Assign action using the filter list property of the combinations list.
3. A user selects a driver item, runs Assign, and moves filter items between "unassigned" and "assigned" columns.
4. The combinations list is automatically populated with the correct rows.

This avoids manually maintaining the junction list and is the recommended pattern for many-to-many relationships at scale.

## Allow Access to Unfiltered Items

Both one-to-many and many-to-many filtered picklists support an **Allow access to unfiltered items** checkbox in the Format dialog. When checked:

- A "Show All" option appears at the bottom of the filtered picklist dropdown.
- Users can click "Show All" to see the complete filter list, bypassing the dependency filter.

Use carefully — this partially defeats the purpose of filtering and can lead to invalid data combinations.

## Interaction with Selective Access

SA interacts with picklists at the dropdown level:

- If SA is enabled on the list used as a picklist, the dropdown **shows only items the user has SA access to** (both Read and Write items appear; the Read/Write distinction is ignored for dropdown content).
- Items the user has no SA access to are hidden from the dropdown entirely.
- The user cannot select or view items outside their SA assignment.
- For filtered picklists, SA is applied **on top of** the dependency filter — the dropdown is the intersection of (dependency-valid items) ∩ (SA-accessible items).

To apply SA filtering explicitly in a filtered picklist, select **Selective Access** in the Format dialog's Filter options.

> [!note] SA on picklists ignores Read/Write distinction
> For picklists specifically, Anaplan uses SA purely as a visibility filter. Whether an item is in the Read column or Write column makes no difference — both are shown. SA's Read/Write distinction only matters for module data access, not for picklist dropdown content.

### Users List as Picklist

A line item formatted on the Users list creates a picklist showing all workspace users. By default, all users are shown — even to non-admin users. To restrict:

- Enable **Selective Access** in the picklist Format dialog → non-admins see only their own name.
- Add **Allow access to unfiltered items** → non-admins can optionally click "Show All" to see everyone.
- Workspace admins always see the full Users list.

## Actions and Filtered Picklists

The **Assign** action is tightly integrated with many-to-many filtered picklists:

- It requires a numbered list with at least one list-formatted property and a parent hierarchy (the driver list as parent).
- Running the Assign action on a combinations list lets a user graphically map driver items to valid filter items.
- Results populate the valid combinations list in Grid View.
- This list then drives the filtered picklist in the target module.

The Assign action is the recommended operational pattern for maintaining many-to-many relationships over time, as it requires no Blueprint access and can be surfaced on a dashboard for authorized users.

## Gotchas

- **Deleted list item → blank picklist cell.** If a list item that was previously selected in a picklist cell is deleted from the list, the picklist cell goes blank. There is no error — the reference silently becomes empty. This can cause downstream LOOKUPs to return blank/zero values.
- **Picklist ≠ formula reference.** A list-formatted line item holds a user-selected reference, not a calculated value. You cannot write a formula in a list-formatted line item.
- **Cannot import a formula into a list-formatted line item.** If you add a formula, the picklist stops working.
- **Filtered picklist context is row-specific.** The filter is based on the driver value in the same row. If the driver line item is blank, the filter list may show all items (no valid filter context) — validate this behavior for your use case.
- **SA + filtered picklist stacking.** If SA is enabled on the filter list AND a dependency filter is active, the user sees the intersection. An item must satisfy both the SA assignment and the dependency rule to appear. This can produce an empty dropdown if no items satisfy both constraints.
- **Many-to-many valid combinations list is production data.** Like all numbered lists used for data, the combinations list holds real data. Changes to the Assign action results persist. Build a workflow for ongoing maintenance.
- **Allow access to unfiltered items weakens data integrity.** If users bypass the filter with "Show All", they can create invalid combinations. Consider whether this is acceptable before enabling.

## Picklist vs. Dimension

| | Picklist (list-formatted line item) | Dimension |
|---|---|---|
| What it is | A cell that stores one list item reference | A list used to structure the module's axes |
| Multiple items per row? | No — one reference per cell | Yes — every item in the list is a row/column |
| Used for | Mapping/linking (Employee→Department) | Slicing data (data by Department) |
| Formula possible? | No | N/A (dimensions are structural) |
| SA filters? | Yes (dropdown content) | Yes (row visibility) |

## Related Pages

- [[11_lists]] — list structure, properties, subsets, hierarchies
- [[17_selective-access]] — how SA filters picklist dropdown items
- [[10_line-item]] — line item concepts including format types
- [[07_dimensions]] — how lists function as module dimensions vs. picklist references
