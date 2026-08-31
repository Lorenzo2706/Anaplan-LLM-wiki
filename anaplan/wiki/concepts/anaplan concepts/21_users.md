---
title: Users List
type: concept
tags: [anaplan, users, users-list, workspace-administrator, subsets, dimension, picklist, access]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Users list.md
  - raw/docs/Add a top-level item to the Users list.md
  - raw/docs/Create Users list subsets.md
  - raw/docs/Add users to a workspace from a model.md
  - raw/docs/Remove users from a workspace in a model.md
  - raw/docs/Designate workspace administrators.md
  - raw/docs/Control user access within models.md
  - raw/docs/Levels of model access.md
---

# Users List

## What the Users List Is

The Users list is Anaplan's built-in list of every user who has access to a model. It is automatically maintained by Anaplan — when a user is granted access to a model (any role other than No Access), they appear in the Users list. When assigned No Access, they disappear.

Key constraints:
- You **cannot delete or rename** the Users list.
- You **cannot reorder, add, edit, or delete** individual users from the Users list directly — user membership is governed by the Users pane and workspace access provisioning.
- The Users list is always treated as **production data**: you cannot reference individual users by name in formulas using `Users.username` syntax.
- The Users list appears at the top of General Lists in the model settings bar.

## Users List vs. Users Pane

| Object | What it contains | Who sees what |
|---|---|---|
| Users Pane (model settings) | All users with workspace access, including No Access model role users | Workspace admins only |
| Users List (General Lists) | Only users with a non-No Access model role for this model | All users; but non-admins see only themselves |

## Using the Users List as a Dimension

The Users list can be added as a dimension to modules, enabling per-user data storage (e.g., user preferences, personal targets, data entry ownership).

### Visibility Rules in a Users-Dimensioned Module

| User type | What they see |
|---|---|
| Workspace administrator | All users in the list + any top-level item |
| Non-admin user in the list/subset | Only their own row; cannot see the top-level item |
| Non-admin user NOT in the list/subset | Cannot see themselves or anyone else |

This means a Users-dimensioned module acts as a natural per-user sandbox — users cannot see each other's data by default without any additional DCA configuration.

### Show All Users Toggle

In the Modules pane or Blueprint, each module has a **Show All Users** setting:

- **On**: Workspace administrators see all users in the Users dimension.
- **Off**: Workspace administrators see only their own user name (same view as non-admins).

This toggle affects only what displays in the dimension, not what displays in list-formatted line items.

### Current User Filter

When Users is a dimension, a view filter by **Current User** restricts the visible rows to the current user's own data — even if the user is a workspace administrator and Users is on Pages (selecting another user in the Pages dropdown is ignored when this filter is active).

## Top-Level Item

Workspace administrators can add a single top-level item (a summary row) to the Users list. This enables aggregate views across all users, based on the module's line item summary methods.

Rules:
- Only workspace administrators see the top-level item in modules; non-admin users cannot see it.
- If the Users list subset is used as a dimension, the top-level item represents only the subset members.
- The top-level item can be set as the default page for a module (Configure tab).
- Non-admins cannot see the top-level item and would never land on it as a default page.

## Users List Subsets

Workspace administrators can create named subsets of the Users list — smaller lists that contain only selected users. These function like regular list subsets.

Use cases:
- `Planners` subset: only users who submit plans; use as dimension in planning input modules.
- `Approvers` subset: only users who approve; use as dimension in approval tracking modules.
- `Finance Team` subset: dimension in finance-only modules.

Subset membership is maintained manually via the Grid View of the list (checkboxes). Membership can also be imported.

Subsets can also **control access** — if a module uses a Users subset as its dimension, only users in that subset can see data in that module (non-members see no rows). This is a lightweight form of access control without DCA or SA.

> [!note] Subset vs. SA for access control
> Using a Users subset as a dimension is an elegant implicit access control: only subset members see any rows. It does not require SA on the Users list (SA for the Users list works differently — see below). However, it is coarser than DCA; all subset members see all rows within the subset-dimensioned module.

## Selective Access and the Users List

The Users list has a special SA behavior, different from general lists:

- Standard SA (workspace admin assigns list items per user in the Users pane) does **not** apply to the Users list — you cannot restrict a user to seeing only certain other users via SA.
- The only SA-like restriction for the Users list in picklists is the **"Selective Access" filter in the Format dialog** for a line item formatted on the Users list (picklist). This causes:
  - Non-admin users see only their own name in the dropdown.
  - Workspace admins always see the full list.
  - If **Allow access to unfiltered items** is also checked, users can optionally click "Show All" to see everyone.

## Workspace Administrators

### What Workspace Administrators Can Do (That Regular Users Cannot)

| Capability | Admin | Non-admin |
|---|---|---|
| Access model settings (Time, Versions, General Lists, Modules, etc.) | Yes | No |
| Save, edit, publish module views | Yes | No |
| Insert, delete, move versions | Yes | No |
| Insert, delete, move line items | Yes | No |
| Manage the Users pane | Yes | No |
| See all users in Users-dimensioned modules | Yes | No (own row only) |
| Bypass Selective Access | Yes (always exempt) | No |
| Import into DCA-protected cells from file | Yes | No |
| Access modules/dashboards not in Contents | Yes (via Modules pane) | No |
| Change another user's model role | Yes | No |
| Designate other workspace administrators | Yes | No |
| Control SSO exceptions per user | Yes | No |

### Designating Workspace Administrators

Any existing workspace administrator can designate another user as a workspace administrator via **Model Settings > Users > Workspace Administrator checkbox**. Self-removal is blocked (you cannot remove your own admin status).

### Workspace Admin and Model Roles Interaction

Workspace administrators have Full Access to all models in the workspace by default when they are added to the workspace. Their admin status sits above the model role system — a workspace admin effectively has full access regardless of the model role assigned to them.

## Adding Users to a Workspace from a Model

When a workspace administrator adds a user from within a model:

- The user is added to the **entire workspace** (all models), not just the current model.
- The user gets the assigned role for the current model.
- The user gets **No Access** to all other models in the workspace (unless they are being added as a workspace admin, in which case they get Full Access to all models).
- An email notification is sent to the new user.

> [!warning] Adding from a model affects the whole workspace
> There is no way to add a user to a single model only. If you add from within a model, they enter the workspace and land at No Access on all other models. Remember to explicitly set roles on other models where appropriate.

### Conflict Resolution: Admin vs. User Administrator Changes

If a user administrator (from the Administration console) and a workspace administrator make conflicting changes to the same user simultaneously, the **most recent transaction wins**. Best practice: use the User Administrator role for adding/removing users and reserve workspace admin for model-role refinement.

### User Management Lock

If a tenant administrator enables the user management switch in Administration:
- Only user administrators can add or remove users (from Administration console only).
- Workspace administrators can no longer add/remove users from within models.
- Workspace administrators can still run imports to **update user attributes** (not add/remove).

## Removing Users from a Workspace

Removing a user from any model in the workspace removes them from **all models** in the workspace. To restrict a user to fewer models without removing them from the workspace, change their model role to No Access in the relevant models instead.

Batch deletion: up to 250 users can be deleted at once.

> [!warning] Remove vs. change to No Access
> Removing a user from the workspace deletes them everywhere. Assigning No Access in a single model keeps them in the workspace but removes their data from that specific model (including Users-dimensioned data deletion). Choose carefully based on the intended outcome.

## Related Pages

- [[02_access-security]] — overview of all access layers
- [[13_model-roles]] — per-model role permissions; No Access data deletion behavior
- [[17_selective-access]] — row-level SA (distinct from Users list SA picklist behavior)
- [[11_lists]] — general list concepts, subsets, hierarchies
- [[08_dynamic-cell-access]] — using Users list as dimension in access driver modules
