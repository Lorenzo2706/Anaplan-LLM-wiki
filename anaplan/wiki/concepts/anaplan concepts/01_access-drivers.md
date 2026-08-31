---
title: Access Drivers
type: concept
tags: [anaplan, access-drivers, DCA, dynamic-cell-access, boolean, blueprint, SYS-module, patterns]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Access drivers.md
  - raw/docs/Access driver recommendations.md
  - raw/docs/Create an access driver module.md
  - raw/docs/Example Control access to sales by customer.md
  - raw/docs/Example Control access to time periods.md
---

# Access Drivers

## What an Access Driver Is

An access driver is a **Boolean-formatted line item** whose value (true/false) tells Anaplan whether a user has read, write, or no access to a specific cell in a target module. Access drivers are the implementation vehicle for [[08_dynamic-cell-access|Dynamic Cell Access]] (DCA).

Two driver slots exist per line item in Blueprint:

| Blueprint Column | Governs |
|---|---|
| **Read Access Driver** | Whether the cell is visible (true = visible; false = hidden) |
| **Write Access Driver** | Whether the cell is editable (true = editable; false = read-only or hidden) |

Setting a Write driver on a line item but not a Read driver: write implies read, so the cell becomes fully editable. The Read driver is primarily used when you want read-only visibility without write capability.

## Dimension Compatibility

An access driver line item can only be assigned to a target if the dimensions are compatible. Compatibility requires:

1. **At least one shared dimension** between the driver module and the target module/line item, OR
2. The driver is dimensioned against **Users** (special case — applies to all targets regardless of other dimensions), OR
3. The driver is dimensioned against a **parent hierarchy** and the target is dimensioned against the corresponding **child hierarchy**.

AND in all cases:

4. The driver line item must be **Boolean** format with summary method **All**, **Any**, **None**, or **Formula**.

For dimensions in the target that are absent in the driver, the driver's access setting applies uniformly to all items of those absent dimensions. For flat lists in the target not present in the driver, set a **Top Level Item** on those lists (Configure tab of the list).

### Global Drivers

A driver module with **no dimensions** is a global driver — it applies a single true/false to every cell in any target module it is assigned to, regardless of the target's dimensionality. Use for model-wide lock/unlock scenarios.

## Access Driver Module Pattern

### Why a Dedicated Module

Mixing access drivers with calculation line items or input data creates several problems:
- Access settings become hard to find and audit.
- Users with write access to a calculation module could inadvertently affect their own access.
- Selective Access cannot easily be applied to a mixed-purpose module.

The [[DISCO — Module Classification|DISCO]] convention places access driver modules in the **System (SYS)** category. Treat them as infrastructure, not content.

> [!tip] Protect the driver module with SA
> Apply [[17_selective-access|Selective Access]] to the access driver module itself so that only workspace administrators can view or edit the access driver values. End users should never be able to modify their own DCA settings.

### Recommended Naming Convention

Anapedia recommends naming access driver modules to reflect their dimensions:

| Example Module Name | Dimensions |
|---|---|
| `SYS01 Access Drivers - Time` | Time only |
| `SYS02 Access Drivers - Cities, Time` | Cities list + Time |
| `SYS03 Access Drivers - Users, Products` | Users list + Products list |
| `SYS04 Access Drivers - Global` | No dimensions (global) |

Number prefixes allow ordering within the SYS functional area.

### Typical Module Structure

```
Module: SYS01 Access Drivers - Time
Dimensions: Time (on columns)
Line items:
  - Read  [Boolean, summary: None, formula: optional]
  - Write [Boolean, summary: None, formula: optional]
```

If you need different access rules for different target line items, add additional line item pairs:

```
  - Read - Actuals     [Boolean]
  - Write - Actuals    [Boolean]
  - Read - Budget      [Boolean]
  - Write - Budget     [Boolean]
```

### User-Dimensioned Drivers

To control access per user, add the **Users** list to the driver module and enable **Show All Users: On** in the module configuration. This allows workspace administrators to set different access flags for each user × dimension combination.

## Assigning Drivers in Blueprint

In the target module's Blueprint view:

| Blueprint row | Meaning |
|---|---|
| Module-level row (top row) | Driver cascades to all line items (shown as `-` in subordinate rows) |
| Individual line item row | Driver applies only to that line item, overriding any module-level driver |

Steps:
1. Open target module in Blueprint.
2. Navigate to the **Read Access Driver** column.
3. Select the appropriate access driver line item from the picker (format: `ModuleName.LineItemName`).
4. Repeat for **Write Access Driver** column.
5. For module-level application: set the driver in the first (module) row.
6. For line-item-level granularity: set individually per row; leave others as `-` (inherits module level).

## Formula-Driven vs. Manually-Set Drivers

Access drivers can be either formula-driven or manually maintained:

| Approach | Best for |
|---|---|
| Formula-driven | Rules that follow model data: current period, version status, user-product mapping |
| Manually-set checkboxes | Rules that require human decision: period close, exceptional overrides |

Common formula patterns:

```
// Lock all months before current period to Read Only
Write = CURRENTPERIODSTART() <= ITEM(Months).Start

// Future periods hidden (no read or write)
Read = ITEM(Months).Start <= TODAY()

// User can only write their own cost center's data
Write[Users, Cost Centers] = Users.CostCenter = ITEM(Cost Centers)
```

> [!warning] Do not reference the protected line item in its driver
> If the access driver formula refers (directly or transitively) to the line item it is protecting, Anaplan will detect a circular dependency. Design driver formulas to reference independent system data only (time properties, list properties, other SYS modules).

## Many-to-One: One Driver Controls Multiple Targets

A single access driver line item can be assigned to many target line items across many modules. This is the recommended approach when the same access rule governs multiple line items:

- Assign `SYS01 Access Drivers - Time.Write` as the Write Access Driver for every input line item in every input module.
- Changing the driver formula or values immediately propagates to all controlled line items.

This is far preferable to creating separate driver line items per target, which creates maintenance overhead and risk of inconsistency.

## One-to-One vs. Shared Drivers: Trade-offs

| Approach | Pros | Cons |
|---|---|---|
| Shared driver (one driver → many targets) | Single point of change; consistent; simple audit | All targets behave identically — cannot differentiate per line item |
| Per-line-item drivers | Fine-grained control; different rules per line item | More drivers to manage; risk of divergence; harder to audit |

Use shared drivers as the default; introduce per-line-item drivers only when the access rules genuinely differ.

## Change Tracking

Changes to access driver values (whether manual or formula-recalculated on publish) are recorded in the model's **change history** as **Security Changes**. This provides an audit trail of when access changed.

## Integration with Selective Access

DCA and [[17_selective-access|Selective Access]] are complementary:

- Protect the access driver module itself with SA (workspace admins only) to prevent end users from self-granting access.
- SA restricts which list items a user sees (row-level); DCA restricts which cells within visible rows are editable (cell-level).
- Both mechanisms are independent; both can be active simultaneously; the most restrictive always wins.

## Suggested `SYS Access Drivers` Module Set

For a typical planning model, consider this set of driver modules:

| Module | Dimensions | Purpose |
|---|---|---|
| `SYS Access Drivers - Time` | Time | Lock closed periods |
| `SYS Access Drivers - Versions` | Versions | Lock locked versions |
| `SYS Access Drivers - Users` | Users | Per-user global restrictions |
| `SYS Access Drivers - Users, Time` | Users × Time | User-specific period locks |
| `SYS Access Drivers - Global` | None | Model-wide lock during close |

Not every model needs all of these — build only what the access requirements demand.

## Related Pages

- [[08_dynamic-cell-access]] — the DCA concept; how driver state translates to access states
- [[02_access-security]] — full overview of all access layers
- [[DISCO — Module Classification]] — DISCO module categorization; SYS module conventions
- [[17_selective-access]] — complementary row-level access mechanism
