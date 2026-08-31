---
title: Versions
type: concept
tags: [anaplan, dimensions, versions, scenario-management, switchover]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Versions  Anapedia.md
  - raw/docs/Create versions.md
  - raw/docs/Delete versions.md
  - raw/docs/Restrict version edits.md
  - raw/docs/Bulk copy versions.md
  - raw/docs/Variance reports with versions.md
  - raw/docs/Variance reports without versions.md
---

# Versions

Versions is a **built-in Anaplan dimension** present in every model by default. It allows you to hold multiple scenarios side by side in the same module — Actuals, Budget, Forecast, Revised Forecast, Variance, etc. — and to compare them without duplicating modules.

See also: [[Dimensions]], [[Pattern — Version-as-list (custom-list scenarios)]], [[Planual Chapter 1 — Central Library]]

---

## Default versions

Every new model includes two versions:

| Version | Notes |
|---------|-------|
| **Actual** | Cannot be deleted. Always acts as the "Actual" reference for switchover logic. |
| **Forecast** | Includes a switchover date by default (adjustable). |

Additional versions can be created by workspace administrators.

> [!warning]
> Using more than ~10 versions can significantly increase model memory usage and slow model load times — potentially to the point of failure. Before creating many versions, consider whether a standard list (version-as-list pattern) is more appropriate.

---

## Version types

### Standard versions
A plain version with no switchover. All periods are either fully editable (Write access) or read-only (Read access), subject to any Edit From / Edit To date constraints.

### Switchover versions
A version with a **switchover date** set. The behavior is:

- **Before the switchover date**: data mirrors Actual and is **read-only** in this version.
- **On and after the switchover date**: data defaults to zero (or the data type's default) and is **editable**.

This makes switchover versions ideal for rolling forecasts: the past is locked to actuals, the future is open for planning.

The **Forecast** version is automatically created with a switchover date. You can advance the switchover date at the end of each period to roll the forecast forward.

---

## Current version

One version can be marked as the **Current** version (checkbox in the Versions pane). Only one version can be current at a time.

- Determines the default version selected in page selectors when a user opens a module.
- Required for the `CURRENTVERSION` and `ISCURRENTVERSION` functions to return meaningful results.
- If no current version is set, the version at the top of the list is selected by default.

---

## Key functions

| Function | Returns |
|----------|---------|
| `ISACTUALVERSION` | `TRUE` if the current cell's version is the Actual version |
| `ISCURRENTVERSION` | `TRUE` if the current cell's version is the version marked as Current |
| `CURRENTVERSION` | The value of a line item for the current version |
| `SELECT: VERSIONS.<name>` | Retrieves a specific version's data in a line item formula (e.g., `Module.LineItem[SELECT: VERSIONS.Budget]`) |

`ISACTUALVERSION` is commonly used in formulas that span the switchover boundary — e.g., to show actuals before the switchover date and a calculated forecast after it.

---

## Read/write control

Versions support fine-grained access control at the version level:

| Setting | Effect |
|---------|--------|
| **None** | Version hidden from this model role |
| **Read** | Version visible but not editable |
| **Write** | Version fully editable |

In addition, workspace administrators can set **Edit From** and **Edit To** date ranges per version. Data outside that range becomes read-only regardless of the access level. Date ranges available depend on the model's Calendar Type.

> [!note]
> The Actual version cannot be deleted, only renamed. Any version referenced by a `SELECT` formula also cannot be deleted until the formula is removed.

---

## Bulk copy

**Bulk Copy** copies all data from one version to another in a single action. The target version's data is completely overridden.

Common use cases:
- Seeding a Budget from Actuals at year-start.
- Copying a Forecast into a Revised Forecast for scenario comparison.
- Copying list items (not only versions — Bulk Copy works on any list).

Bulk Copy can be set up as a reusable **Bulk Copy action** to include in processes or schedules.

---

## Variance formulas on versions

Versions support **formula columns**: you can create a "Variance" version whose formula is `Actual - Budget`, so the variance is always computed across the dimension. Typical setup:

| Version | Formula |
|---------|---------|
| Actual | *(no formula — source data)* |
| Budget | *(no formula — source data)* |
| Variance | `Actual - Budget` |
| Variance % | `IF Budget > 0 THEN 100 * (Actual - Budget) / Budget ELSE 100 * (Budget - Actual) / Budget` |

When **Current Period** changes, variance reports referencing it update automatically.

For an alternative approach that avoids adding version members, see [[Variance Reporting]].

---

## Native Versions vs version-as-list: trade-offs

| Dimension | Native Versions | Version-as-list |
|-----------|----------------|-----------------|
| **Setup** | Built-in, zero config | Custom flat list, requires deliberate design |
| **Switchover logic** | Built-in (`ISACTUALVERSION`) | Must be replicated with Boolean line items and explicit formulas |
| **Workspace aggregation** | Supported natively | Not applicable |
| **UI support** | Native page selector, pivot integration | Acts as any other list dimension |
| **Performance (Classic)** | Adds block overhead per version | Lower overhead for few scenarios |
| **Polaris sparsity** | Can create unnecessary cell blocks at scale | Preferred for Polaris — sparse-friendly, avoids engine overhead |
| **Flexibility** | Limited to Anaplan version features | Full list behavior: subsets, hierarchies, properties, LOOKUP |
| **Max practical count** | ~10 before memory issues | Essentially unlimited |
| **Used in FSP 2.0 / AAC** | No | Yes — both are Polaris models |

> [!note]
> FSP 2.0 and AAC both use the version-as-list pattern. For Polaris models, version-as-list is generally preferred because it avoids the block-structure overhead that native Versions impose.

See [[Pattern — Version-as-list (custom-list scenarios)]] for the full design pattern.
