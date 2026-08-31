---
title: Selective Access
type: concept
tags: [anaplan, selective-access, lists, security, row-level-security, hierarchy, picklists, import]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Selective access.md
  - raw/docs/Enable selective access for a list.md
  - raw/docs/Selective access and list hierarchies.md
  - raw/docs/Selective access and picklists.md
  - raw/docs/Selective access example.md
  - raw/docs/Assign selective access to lists and list items.md
  - raw/docs/Example Control access to sales by customer.md
  - raw/docs/Example Control access to time periods.md
---

# Selective Access

## What Selective Access Is

Selective Access (SA) is Anaplan's row-level security mechanism. It restricts which list items a user can see (Read) or edit (Write) in any module that uses the SA-enabled list as a dimension. Unlike [[13_model-roles|model roles]] — which control whether a user can access a module at all — SA controls which rows within a module are visible or editable on a per-user basis.

SA is configured and maintained by workspace administrators. End users receive access assignments; they cannot self-manage it.

## How It Works

1. **Enable** SA on a list (General Lists > Selective Access checkbox, or Configure tab).
2. Once enabled, two columns appear: **Read** and **Write**, visible in both:
   - The **Users pane** (assign list items per user), and
   - The **Grid View of the list** (assign users per list item).
3. A workspace administrator assigns one or more list items to a user under Read or Write.
4. The user can now see (Read) or edit (Write) module data for those list items only.

## Read vs. Write Semantics

| Assignment | Can see data? | Can edit data? |
|---|---|---|
| Neither Read nor Write | No | No |
| Read only | Yes | No |
| Write only | Yes (write implies read) | Yes |
| Both Read and Write | Yes | Yes (Write governs) |

> [!note] Write implies Read
> Assigning Write access does not require a separate Read assignment — write access inherently grants read access. If you set both Read and Write for the same item, the Write driver governs.

## The Lock-Out Risk on Enabling SA

> [!warning] Critical: Enabling SA locks out ALL non-admin users immediately
> The moment SA is enabled on a list, **no user has access** — not even users who had model role Write access before. Workspace administrators are always exempt. You must explicitly assign Read or Write for every non-admin user who needs access after enabling SA.

This means: plan your access assignment before enabling SA on a production model, or enable it during an off-hours window.

## Assigning Selective Access

Three methods are available:

| Method | Best for |
|---|---|
| Users pane → Read/Write column per user | Assigning multiple list items to a specific user |
| Grid View of the list → Read/Write column per item | Assigning multiple users to a specific list item |
| Import into the list or users list | Bulk assignment / automation |

### Import Behavior

- SA can be set via import by providing permission values in the import source.
- Importing a value of `"None"` for a list **removes** all current SA for that user on that list.
- Importing is the most scalable method for large user sets or automated provisioning workflows.

## Interaction with List Hierarchies

SA propagates through parent-child list relationships. The rules are non-trivial.

### When You Enable SA on a Child List

Enabling SA on a child list **automatically enables SA on all parent lists** of that child. You cannot have child SA without parent SA.

If the parent has child lists, child list items inherit their SA from the parent unless you also explicitly enable SA on the child.

### Access Propagation Rules

| Action | Effect on child | Effect on parent |
|---|---|---|
| Enable SA on child | SA automatically enabled on all parents | If parent has children, children inherit parent's SA unless independently enabled |
| Assign SA to child item | Parent does NOT automatically receive the same access | — |
| Assign SA to parent item | All child items of that parent receive the same level of access | — |
| Remove SA from parent | Child items where access was equal to or more restrictive than parent also lose access | — |
| Remove list item from parent (orphan) | Orphaned child loses parent's access settings | — |

### Write Overrides Read in a Hierarchy

If a user has Write on a child item (e.g., Kiran in France) but only Read on the parent (France), the Write on the child item is preserved and overrides the parent-level Read for that specific item.

### Multi-Level Hierarchy Example

Given: Regions → Countries → Employees

- Grant Read on EMEA region → user gets Read on all countries under EMEA, and all employees under those countries.
- Grant Write on France → user gets Write on all employees under France, plus Read on all other countries/employees under EMEA (if EMEA Read was also assigned).

### Orphaned List Items

When a list item is removed from its parent (via import or manual edit), it becomes an orphan and loses the parent's SA settings. To restore access to orphans:
- Assign access directly to the orphan item, or
- Re-import a parent assignment and reapply access.

## Interaction with Picklists

SA interacts with picklists differently from regular module dimensions:

- When SA is enabled on a list used as a picklist, the picklist dropdown **only shows items the user has access to** (both Read and Write items appear; the distinction between Read/Write is ignored for the dropdown itself).
- The user cannot select items they have no SA assignment for.
- For filtered picklists (one-to-many or many-to-many), you can additionally enable "Selective Access" as the filter option in the Format dialog, which applies SA filtering on top of the dependency filter.
- **Allow access to unfiltered items**: if enabled, a "Show All" option appears at the bottom of the picklist, letting users see the unfiltered list.

### Special Case: Users List as Picklist

The Users list behaves differently from general lists regarding SA:

- Standard SA does not apply to the Users list in the same way.
- Enabling "Selective Access" in the picklist Format dialog for a Users-formatted line item causes the picklist to **show only the current user's own name** (non-admins) or the full list (workspace admins).
- This is not the same as list-level SA and is not configured in the Users pane.

## Model-to-Model Imports and SA

When running a model-to-model import, whether SA applies depends on:

- The **running user's access rights** in both source and target model.
- The running user's **workspace administrator status**.

If the running user is a workspace administrator, SA is bypassed for the import. If not, the running user's SA assignments in the source model filter which data is exported, and their assignments in the target model filter which data they can write.

## Example: Sales by Customer (Row-Level Security)

Classic use case — each sales rep should only see their own customer data:

1. Enable SA on the Customers list.
2. Assign each sales rep Read and/or Write access to only their assigned customers.
3. Modules dimensioned on Customers will automatically show each rep only their rows.

For reporting roll-ups (e.g., regional managers need to see all reps' customers), assign Read access at the parent Region level — this cascades down to all customers in that region.

## Example: Hierarchical Manager Access

A manager (Patrice) needs Write access to direct reports but Read-only on others:

1. Enable SA on L1 Employees. This auto-enables SA on L2 Countries.
2. Assign Write to Kiran Contributor (L1 Employees Write).
3. Assign Read to Sylvia Sales (L1 Employees Read).
4. Later, to simplify: assign Read to France and Canada (L2 Countries Read) — this covers all employees in those countries. Kiran's Write remains because explicit Write on a child overrides parent-level Read.

## When to Use SA vs. DCA vs. Model Roles

| Need | Use |
|---|---|
| User should not see a module at all | Model Role → None on module |
| User should see the module but only certain rows (list items) | Selective Access |
| User should see a row but only certain cells within it (e.g., not future periods) | Dynamic Cell Access |
| Access depends on a formula / business logic | Dynamic Cell Access |
| Access differs per individual user on the same list | Selective Access |
| Access rule is the same for all users of a role | Model Role permissions |

## Gotchas

- Enabling SA on a list instantly blocks all non-admin users. There is no soft-enable.
- Workspace administrators always bypass SA — they see and can edit everything.
- DCA and SA are independent; if you use both, the most restrictive wins.
- Orphaned list items lose parent SA. This can unexpectedly hide data from users after a data import that changes parent assignments.
- SA does not prevent API access — the API respects SA but only for the user's own session token. Integration service accounts with workspace admin privileges bypass SA.
- The Read/Write distinction in SA for picklists is **ignored** — the picklist just uses SA as a filter for visible items.
- Importing `"None"` as a permission value in a list import removes all SA for that user on that list — use carefully in bulk imports.

## Related Pages

- [[02_access-security]] — overview of all three access layers and decision guide
- [[13_model-roles]] — module/version/action permissions
- [[08_dynamic-cell-access]] — cell-level access control
- [[11_lists]] — list structure, hierarchies, and parent-child relationships
- [[16_picklists]] — how SA interacts with dropdown list items
