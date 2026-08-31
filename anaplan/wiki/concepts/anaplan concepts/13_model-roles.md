---
title: Model Roles
type: concept
tags: [anaplan, model-roles, permissions, access, workspace, modules, versions, actions, lists]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Model roles.md
  - raw/docs/Add a model role.md
  - raw/docs/Levels of model access.md
  - raw/docs/Control user access within models.md
  - raw/docs/Assign module permissions to model roles.md
  - raw/docs/Assign version permissions to model roles.md
  - raw/docs/Assign list permissions to model roles.md
  - raw/docs/Assign action permissions to model roles.md
  - raw/docs/Assign a user to a model role.md
  - raw/docs/Select the landing dashboard for a model role.md
  - raw/docs/Organize model Contents by model role.md
---

# Model Roles

## What Model Roles Are

A model role is a named permission profile assigned to users within a single model. Roles group users who share the same business function and data access needs, allowing a single configuration change to affect many users simultaneously.

Every model has two built-in, non-deletable roles:

| Role | Behavior |
|---|---|
| **Full Access** | Can see and edit all modules, versions, lists, and run all actions. Always displayed at the top of the Roles list; cannot be re-ordered below Full Access. Note: Full Access end users still have less capability than workspace administrators (cannot edit Blueprint structure, cannot save views, etc.) |
| **No Access** | User is added to the workspace but cannot see or interact with this model. User still appears in the Users pane but does NOT appear in the Users list dimension elsewhere in the model. Any line item data referencing a No Access user is deleted. |

Custom roles created by workspace administrators sit between these two extremes.

## Permission Types

Model role permissions cover four object types. Each is configured in a separate sub-tab under **Users > Roles**:

### Module Permissions

| Permission Value | Effect |
|---|---|
| **None** (default for new roles) | User cannot open or see the module or its data |
| **Read** | User can view data in the module; cannot edit |
| **Write** | User can view and amend data in the module |

- `Full Access` and `No Access` do not appear on the Roles → Modules tab — they are implicit.
- When a new module is created, default permission for all existing custom roles is **None**. The model builder must explicitly grant access.
- Write at module level does not override cell-level DCA restrictions.

### Version Permissions

| Permission Value | Effect |
|---|---|
| **None** | User cannot see data for that version |
| **Read** | User can view version data; cannot edit |
| **Write** | User can view and edit version data |

Version permissions layer with module permissions. A user needs Write on both the module and the version to edit a cell in that version.

### List Permissions

List permissions control structural editing of the list itself (inserting, deleting, renaming list items), not whether the user can see data dimensioned on the list.

- A user without list permission can still view and edit data in modules that use that list as a dimension.
- List permission = can modify the list membership (add/remove items). This is a checkbox permission (allowed or not; no read/write gradation).
- Only workspace administrators can use the **Order List** action — this is not grant-able to end users via model roles.

### Action Permissions

Action permissions control whether a role can execute specific actions (imports, exports, processes, etc.).

- Default is unchecked (no access) for each action.
- **Order List** and **Update Current Period** actions are reserved for workspace administrators only and cannot be assigned to custom roles.

## Default Access Behavior

| Scenario | Default role assigned |
|---|---|
| User added to workspace from within a model by workspace admin | Full Access to the model they are added from; No Access to all other models in workspace |
| Workspace administrator added to workspace | Full Access to ALL models in the workspace by default |
| User provisioned from Administration console | No Access to all models by default |

> [!warning] Default can surprise you
> If a workspace administrator adds a regular user to one model, that user silently gets No Access to every other model in the workspace. Always audit roles across all models when adding users.

## Effective Access = Most Restrictive Combination

A user's actual access is the intersection of:
1. Their workspace role (admin vs. user)
2. Their model role (module/version/list/action permissions)
3. Any Selective Access restrictions on list items
4. Any Dynamic Cell Access restrictions on individual cells

Workspace administrators override all of these. For non-admin users, the most restrictive layer governs.

## Contents Panel and Landing Dashboard per Role

### Landing Dashboard

- Each role can have a distinct landing dashboard — the view that appears when the user opens the model.
- Multiple roles can share the same landing dashboard.
- If no landing dashboard is set, users see the full Contents panel on open.
- Ensure the role has appropriate module permissions for all modules the landing dashboard references — otherwise panels will be blank or show errors.

### Contents Panel Organization

- By default, Contents shows all modules, dashboards, and views the user's role can access.
- Workspace administrators can curate Contents per role: select which items appear, in what order, grouped by Functional Area.
- Items excluded from Contents are still accessible to workspace admins via the Modules pane.
- If **Show hidden content** is enabled, users can opt-in to see Content items their role has access to but that have been hidden by the workspace admin.
- End users can only navigate to modules and dashboards via Contents. Workspace admins can use the Modules pane directly.

## Assigning Users to Roles

- Each user has exactly one role per model at any given time.
- A user can have different roles in different models within the same workspace.
- Role assignment is changed in **Users > Users tab > Model Role column**.
- A user cannot be assigned No Access to themselves by the currently logged-in user (you cannot lock yourself out).

> [!warning] No Access data deletion
> Assigning a user to No Access has permanent side effects:
> - The user disappears from picklist dropdowns formatted on the Users list.
> - Any list-formatted line items that had this user selected are cleared.
> - In modules where Users is a dimension, all data rows for that user are deleted.
> This is not reversible through role reassignment — the data must be re-entered.

## Design Patterns

### One Role per Business Persona

Design roles to match job functions, not individuals. Common patterns:

| Persona example | Typical permissions |
|---|---|
| Planner | Write on input modules for their area; Read on output/reporting modules; No access to system modules |
| Reviewer / Approver | Read on input + output modules; Write on approval flag modules only |
| Finance Manager | Write on finance consolidation modules; Read on operational detail modules |
| Read-Only / Auditor | Read on all modules; no action permissions |

### Avoid Role Proliferation

- Too many roles create maintenance overhead. When two roles have identical permissions, merge them.
- Do not create one role per user — use Selective Access for per-user row-level restrictions instead.
- Aim for 3–8 roles in typical planning models. Large complex models may justify more.

### Module Access Matrix as Design Artifact

Before building, create a matrix: Modules on rows, Roles on columns, with None/Read/Write in each cell. Maintain this as a design document alongside the model. It prevents gaps when new modules are added.

### New Module = No Access by Default

Remember: every new module added to a model is automatically None for all custom roles. Add module access to your model-building checklist.

## Gotchas

- Model roles are **per-model**. The same user can be a Planner in Model A and a Reviewer in Model B within the same workspace.
- The Full Access role for end users is less powerful than workspace administrator status — often mistakenly assumed equivalent.
- Removing a user's module access (setting to None) does not delete their data — but assigning No Access role does delete Users-dimensioned data.
- Actions assigned to a role can still fail if the action itself imports into a module the role has no write access to — role-level action permission and module permission must both be satisfied.
- You cannot currently export the role-permission matrix from the UI — screenshot or document it externally.

## Related Pages

- [[02_access-security]] — overview of all three access layers
- [[17_selective-access]] — row-level security layered on top of model roles
- [[08_dynamic-cell-access]] — cell-level security layered on top of model roles
- [[21_users]] — Users list, subsets, workspace administrator designation
