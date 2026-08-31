---
title: Access & Security — Overview
type: concept
tags: [anaplan, access, security, model-roles, selective-access, dynamic-cell-access, workspace]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Control user access within models.md
  - raw/docs/Levels of model access.md
  - raw/docs/Model roles.md
  - raw/docs/Selective access.md
  - raw/docs/Dynamic cell access.md
  - raw/docs/Access drivers.md
---

# Access & Security — Overview

Anaplan's access control system is layered. Three distinct mechanisms operate at different granularities and must be understood both independently and in combination. Getting the design wrong means either over-exposure of data or users being locked out of modules they need.

## The Three Layers

| Layer | Mechanism | Granularity | Who configures it | Default when not configured |
|---|---|---|---|---|
| 1. Workspace / Tenant | Workspace role (Administrator vs. user) | Entire workspace | Tenant / User Administrator | User added to workspace gets Full Access to all models if added by workspace admin; No Access if provisioned from Administration |
| 2. Model-level | [[13_model-roles\|Model Roles]] | Module, Version, List, Action | Workspace Administrator | Full Access (default role) or No Access; depends on how user was added |
| 3. Data-level | [[17_selective-access\|Selective Access]] (list rows) and [[08_dynamic-cell-access\|Dynamic Cell Access]] (individual cells) | List item (row-level) or individual cell | Workspace Administrator (SA); Model Builder via formula (DCA) | SA: no user has access once enabled. DCA: no restriction until a driver is assigned |

## What Each Mechanism Controls

| Question | Mechanism to use |
|---|---|
| Can this user open this model at all? | Workspace role + model role (No Access) |
| Can this user see/edit this module? | Model role → Module permissions (None / Read / Write) |
| Can this user see/edit this version? | Model role → Version permissions (None / Read / Write) |
| Can this user insert/delete list items? | Model role → List permissions (checkbox) |
| Can this user run an action or process? | Model role → Action permissions (checkbox) |
| Can this user see data for only certain list items (row-level security)? | [[17_selective-access\|Selective Access]] |
| Can this user edit only certain cells, time periods, or intersections? | [[08_dynamic-cell-access\|Dynamic Cell Access]] via [[01_access-drivers\|Access Drivers]] |
| Should only the user's own data appear when Users is a dimension? | Users list `Show All Users` setting + DCA with Users dimension |

## Interaction Rules — Most Restrictive Wins

When multiple mechanisms apply simultaneously, the **most restrictive level always wins**:

- A user with Write on a module (model role) but a Read-only access driver on a cell can only read that cell.
- A user with Write at the model-role level but no Selective Access assignment on an SA-enabled list cannot see that list at all.
- DCA and Selective Access can be combined: SA restricts which rows the user sees; DCA further restricts which cells within those rows are editable.
- Workspace administrators bypass both SA and DCA — they can always read and write everything, including importing into DCA-protected cells from a file.

## Decision Guide: Which Mechanism to Use

```
Start: What needs to be restricted?
│
├─ "Some users should not see this module at all"
│   └─ Model Role → Module permission = None
│
├─ "Some users can view but not edit a version (e.g., Actuals)"
│   └─ Model Role → Version permission = Read
│
├─ "Different users own different rows in a list (e.g., each sales rep sees only their customers)"
│   └─ Selective Access on the Customers list
│
├─ "Some cells should be locked based on time (e.g., past periods read-only)"
│   └─ Dynamic Cell Access — time-dimensioned access driver
│
├─ "Access depends on a formula / business rule"
│   └─ Dynamic Cell Access with a formula-driven Boolean driver
│
└─ "A user should only see their own row in a Users-dimensioned module"
    └─ Users list + Show All Users: Off  OR  DCA with Users dimension
```

## Workspace Administrator: the Override Role

Workspace administrators sit above all three layers:

- They always have access to all lists, modules, and cells regardless of SA or DCA settings.
- They can access model settings (Time, Versions, General Lists, Modules, Line Item Subsets, Users, Actions, Source Models, History, Contents, Dashboards, Data Tags) that are invisible to regular users.
- Within a module, only workspace admins can save/edit/publish views; insert, delete, or move versions; insert, delete, or move line items.
- They can import from a file into DCA-write-protected cells (DCA write-access is bypassed on file import for admins).
- They always see the full Users list, even when SA or "Show All Users: Off" is active.

> [!note] Design implication
> Never rely on model roles, SA, or DCA to hide data from workspace administrators. If a user must not see data under any circumstance, they must not be a workspace administrator.

## Layer-by-Layer Setup Sequence (Recommended)

1. Create model roles aligned to business personas (e.g., Planner, Reviewer, Finance Manager).
2. Assign module, version, list, and action permissions to each role.
3. Set a landing dashboard and curate Contents per role.
4. Enable Selective Access on lists that require row-level security; assign per user.
5. Build access driver modules for cell-level rules; assign drivers in Blueprint.

## Related Pages

- [[13_model-roles]] — detailed reference for model roles and permission types
- [[17_selective-access]] — row-level security on lists
- [[08_dynamic-cell-access]] — formula-driven cell-level access
- [[01_access-drivers]] — how to build and assign access driver modules
- [[21_users]] — the Users list as dimension and its interaction with access
- [[16_picklists]] — how SA filters picklist dropdown content
