---
title: Dynamic Cell Access
type: concept
tags: [anaplan, dynamic-cell-access, DCA, access-drivers, security, boolean, blueprint, formula]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Dynamic cell access.md
  - raw/docs/Access drivers.md
  - raw/docs/Access driver recommendations.md
  - raw/docs/Create an access driver module.md
  - raw/docs/Example Control access to sales by customer.md
  - raw/docs/Example Control access to time periods.md
---

# Dynamic Cell Access

## What Dynamic Cell Access Is

Dynamic Cell Access (DCA) is Anaplan's cell-level access control mechanism. It allows a model builder to control whether individual cells in a module are:

- **Read/Write** (editable, shown in blue)
- **Read Only** (visible but not editable, shown in grey)
- **No Access** (hidden — cell appears blank even if it contains data)

DCA is configured using **Boolean line items called access drivers**, assigned to target line items in Blueprint. Because drivers are line items, their values can be set by formula — making DCA dynamic and responsive to model state (e.g., current period, version, user, or any calculated condition).

DCA is a model-builder concern, not an administrator-assignment concern. Unlike [[17_selective-access|Selective Access]], DCA requires no per-user configuration — the formula determines access for all users simultaneously (unless the Users list is also a dimension of the driver).

## How DCA Differs from Selective Access

| Dimension | Selective Access | Dynamic Cell Access |
|---|---|---|
| Granularity | List item (whole row in a module) | Individual cell (intersection of dimensions) |
| Who configures it | Workspace administrator, per user | Model builder, via formula |
| Mechanism | Read/Write columns on a list | Boolean line items assigned in Blueprint |
| Dynamic / formula-driven? | No — static per-user assignment | Yes — formula-driven |
| Per-user control possible? | Yes (core use case) | Yes, if Users list is a driver dimension |
| Workspace admin bypass? | Yes | Yes (admins bypass DCA on file imports) |

## The Three DCA States

| Read Driver | Write Driver | Resulting Access | Visual in Grid |
|---|---|---|---|
| false | false | No Access | Cell appears blank; data is hidden |
| true | false | Read Only | Cell shows value, greyed out; non-editable |
| true | true | Read/Write | Cell shows value in blue; editable |
| false | true | Read/Write | Write implies Read; cell is editable |

> [!important] Write implies Read
> Setting the Write driver to true gives the user read access regardless of the Read driver value. You do not need both Read=true and Write=true for read/write access — Write alone is sufficient for full access.

## Access Driver Implementation

An access driver is a Boolean line item. It is assigned to a target line item via the **Read Access Driver** and **Write Access Driver** columns in Blueprint.

### Dimension Compatibility Rules

An access driver can only be applied to a target line item if one of the following is true:

1. The access driver module and target module share **at least one matching dimension**, OR
2. The driver line item is dimensioned against **Users**, OR
3. The driver module is dimensioned against a **parent hierarchy** and the target is dimensioned against the **child hierarchy**.

AND:

4. The access driver is a **Boolean** formatted line item with summary method: **All**, **Any**, **None**, or **Formula**.

For target dimensions not present in the driver module (e.g., target has Products × Customers × Time, driver only has Time), the driver applies to all items in the missing dimensions — effectively saying "this time constraint applies regardless of product or customer."

For flat lists in the target that are not in the driver, set a **Top Level Item** on those lists (in the list Configure tab).

### Module-Level vs. Line-Item-Level Assignment

- Setting an access driver in the **first row** of Blueprint (the module row) applies it to all line items in the module (indicated by a hyphen in subordinate rows).
- Setting an access driver on an **individual line item** row gives that line item its own access rule, overriding the module-level assignment for that line item.
- Fine-grained control: different line items within the same module can have different access drivers.

### The Global Access Driver Pattern

An access driver module with **no dimensions** acts as a global access driver — it applies to any target module regardless of dimensionality. Use this for model-wide lockdowns (e.g., lock the entire model for all users during a period close).

## Building an Access Driver Module

Best practice is to place all access drivers in one or more dedicated SYS modules (see [[01_access-drivers]] for naming conventions). A typical module contains:

- A **Read** line item (Boolean)
- A **Write** line item (Boolean)
- Dimensions matching the access control need (e.g., Time only for period locks; Time × Users for user-period combinations)

The module has **Show All Users: On** enabled when the access needs to vary by user.

Formulas can be applied to Read and Write line items. Examples:

```
// Lock all months before current period to Read Only
Write = CURRENTPERIODSTART() <= Time.Start

// Future periods hidden (no read or write)
Read = Time.Start <= TODAY()

// User can only write their own cost center's data
Write[Users, Cost Centers] = Users.CostCenter = ITEM(Cost Centers)
```

## Interaction with Model Roles

DCA and model roles are independent layers. The effective access is:

- If model role says None on the module → user cannot open the module; DCA is irrelevant.
- If model role says Read on the module → user can read; DCA cannot upgrade to Write.
- If model role says Write on the module + DCA Write driver is false → cell is read-only or hidden.
- If model role says Write on the module + DCA Read driver is false + DCA Write driver is false → cell is hidden.

**Most restrictive wins.** Model role sets the ceiling; DCA can only restrict further, never expand beyond the model role permission.

## Interaction with Selective Access

SA and DCA are orthogonal and composable:

- SA controls which rows (list items) are visible at all.
- DCA controls which cells within those visible rows are editable or hidden.
- A user may have SA Read on a customer → sees that customer's rows → but DCA may make certain time-period cells in those rows read-only or hidden.
- Use SA on the access driver module itself to prevent end users from editing their own access drivers.

## Performance Considerations

DCA adds calculation overhead because access drivers are computed for every cell in every affected module at render time:

- Keep driver formulas simple — avoid lookups, OFFSET, or recursive references.
- Do not reference the target protected line item in its own access driver formula (circular reasoning and potential circular dependency errors).
- Avoid unnecessarily large driver modules — if you only need to control by Time, do not add all other dimensions to the driver.
- Sparse driver modules (many false, few true) are faster than dense ones.
- Changes to access drivers are recorded in the model's change history as **Security Changes**.

## Workspace Administrator Bypass

Workspace administrators bypass DCA in one specific scenario: **importing from a file** into DCA write-protected cells. In all other scenarios (manual cell editing in the grid), workspace admins respect the DCA settings like any other user. However, workspace admins can manually edit their own access driver modules to change the driver values, which effectively gives them full control.

## Model-to-Model Imports and DCA

Whether DCA is preserved in model-to-model imports depends on:

- The running user's access rights in both the source and target model.
- The running user's workspace administrator status in each model.

If the running user is a workspace admin in the target, they can import into DCA-protected cells from a file.

## Example Patterns

### Lock Past Periods to Read-Only

Driver module: `SYS Access Drivers - Time` (dimensioned on Time only)

```
Write = NOT(ISANCESTOR(ITEM(Time), CURRENTPERIODSTART()))
```

Assign `SYS Access Drivers - Time.Write` to the Write Access Driver column of the actuals input module. Users can only edit the current period.

### Per-User, Per-Product Access

Driver module: `SYS Access Drivers - Users, Products` (dimensioned on Users and Products)
- `Write` line item: formula checking if the current user is the product owner.
- Enable **Show All Users: On** on this module.

This enables a product manager to edit only their product rows, even though the module is shared.

### Global Model Lock During Period Close

Driver module: `SYS Access Drivers - Global` (no dimensions — global)
- `Write` line item: Boolean, manually set to false during close; true during open period.

Assigning this to all input modules makes the entire model read-only when the period is being closed.

## Gotchas

- **No Access hides data silently.** A cell with No Access appears completely blank — users may think the cell is empty rather than restricted. Consider adding a visible indicator (a companion text/label line item) if users need to know data exists but is restricted.
- **DCA does not prevent API access for workspace admins.** An integration running as a workspace admin service account bypasses DCA write restrictions (on file import).
- **DCA is not a substitute for model roles.** If a user should not be able to open a module at all, use model role None. DCA is for nuanced within-module access, not module-level gate-keeping.
- **Circular reference risk.** If a DCA driver formula references the protected line item (directly or indirectly), Anaplan will report a circular dependency.
- **Summary methods matter.** Access driver Boolean line items must use summary methods of All, Any, None, or Formula. The default for Boolean is None — verify this is correct for your use case (All = access only if all child cells grant access; Any = access if any child cell grants access).

## Related Pages

- [[02_access-security]] — overview of all access layers and decision guide
- [[01_access-drivers]] — deep-dive on access driver module construction, naming, and patterns
- [[17_selective-access]] — row-level security (SA is complementary to DCA)
- [[13_model-roles]] — module/version/action permissions (ceiling that DCA cannot exceed)
