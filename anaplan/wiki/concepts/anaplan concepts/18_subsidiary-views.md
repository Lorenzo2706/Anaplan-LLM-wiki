---
title: Subsidiary Views
type: concept
tags: [anaplan, fundamentals, dimensions, blueprint, module, views]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Subsidiary views.md
  - raw/docs/Create subsidiary views.md
  - raw/docs/Page selectors and nested dimensions.md
  - raw/docs/Configure line items.md
---

# Subsidiary Views

A **subsidiary view** is a separate, automatically generated view of a module that is created whenever a [[Line Item|line item]] has different dimensionality from the module's default. It shows only the data for that line item under its reduced or altered dimension set.

> [!note]
> A subsidiary view is not a user-created saved view — it is a structural consequence of changing a line item's dimensionality in Blueprint. It exists to display data that cannot fit cleanly in the module's default grid layout.

## When a subsidiary view is created

Anaplan automatically creates a subsidiary view when you change any of the following columns in Blueprint for a line item:

| Blueprint column | What changes | Effect |
|---|---|---|
| **Applies To** | Narrows (or changes) which list applies to this line item | Line item operates on a subset of the module's default list |
| **Time Scale** | Sets a different time granularity than the module default | Line item lives on a different time axis |
| **Time Range** | Assigns a specific time range | Line item spans a different set of periods |
| **Versions** | Restricts to specific versions | Line item is not visible for all versions |

Each affected line item gets its own subsidiary view. A module can contain multiple subsidiary views, but each subsidiary view displays only **one line item**.

## Purpose and efficiency benefit

Subsidiary views increase model efficiency by **reducing cell counts**. If a line item has the same value across all items in a large list (e.g. an exchange rate that applies to every country), there is no need to store N copies of it. By narrowing Applies To, only the needed cells are allocated.

The subsidiary view makes this reduced-dimensionality line item accessible and visible without cluttering the main module grid.

## Relationship to page selectors

Page selectors and subsidiary views interact in an important way:

- If the module's default list is on rows/columns but a line item's **Applies To** uses a **list subset**, the subsidiary view uses that subset as its effective row/column axis.
- When a user selects a page item that **exists in the subset**, the subsidiary view's cells display data.
- When a user selects a page item that is **not in the subset**, the subsidiary view's cells are blank — the data simply does not exist at that level.
- If the list is on rows or columns (not pages) and a subset-dimensioned line item is shown, editing happens at the parent list item level, not the child.

## Start of Section — avoiding subsidiary views for blocks

The **Start of Section** option in Blueprint changes the dimensionality of all consecutive line items that follow a selected line item, *without* creating a separate subsidiary view for each one. This is useful when a contiguous block of line items shares a narrower dimension.

**Example:** An Income Statement module uses the *Organization* list by default. A block of profit-center line items should apply to *Profit Centers* (a subset of *Organization*). Using **Start of Section** on the first profit-center line item applies the subset to the entire block — one configuration instead of N subsidiary views.

> [!warning]
> Do **not** reorder line items when using Start of Section. The dimensionality change applies to everything after the marker — reordering can silently move line items in or out of the affected block.

## Constraints and gotchas

| Constraint | Detail |
|---|---|
| **One line item per subsidiary view** | Each subsidiary view shows exactly one line item. A module with many subsidiary views can become difficult to understand. |
| **Dashboard publishing limitations** | You cannot edit subsidiary views published via "publish selected line items" to a dashboard. |
| **Dashboard layout** | The space subsidiary views occupy on dashboards can cause alignment issues. |
| **Module name hiding** | When publishing a subsidiary view to a dashboard, you can only hide the module name if you also hide the line item. |
| **No duplicate-dimension subsidiary views** | You cannot publish multiple subsidiary views that have the same dimensions as another subsidiary view. |
| **Filter restriction** | Filters on a subsidiary view can only be based on that view's own data — you cannot filter based on a different line item. |
| **Default view risk** | If you save a subsidiary view as the module's default, line items not included in it become inaccessible until you reset the default view (View > Manage Views > Reset Default View). |

## Best practice: prefer separate modules over subsidiary views for dashboards

If end users need to view a line item on a dashboard and that line item has different dimensionality, the preferred pattern is to **create a dedicated output module** rather than publishing a subsidiary view.

Reasons:
- Subsidiary views have publishing and layout restrictions on dashboards.
- A dedicated output module (aligned with [[DISCO — Module Classification|DISCO]] Output pattern) is easier to manage, version, and document.
- Subsidiary views are best kept as a model-internal efficiency tool, not as the user-facing layer.

## Cross-references

- [[Dimensions]] — dimensionality that drives subsidiary view creation
- [[Line Item]] — Blueprint columns (Applies To, Time Scale, Time Range, Versions) that trigger subsidiary views
- [[Lists]] — list subsets often used in Applies To
- [[DISCO — Module Classification]] — Output module pattern preferred over subsidiary views for dashboards
