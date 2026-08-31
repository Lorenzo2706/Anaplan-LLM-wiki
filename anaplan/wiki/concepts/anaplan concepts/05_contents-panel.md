---
title: Contents Panel
type: concept
tags: [anaplan, contents, navigation, model-roles, visibility]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Select content to display in the Contents panel.md
  - raw/docs/Set new content to automatically show in Contents.md
  - raw/docs/Show hidden content in model Contents.md
---

# Contents Panel

The **Contents panel** is the navigation sidebar in a model. It lists the modules and dashboards a user can access. What appears there is **per model role** — each role sees only the items an admin has enabled for it.

## What It Is

- Every model has a Contents panel (left sidebar in the classic model UI).
- It is the primary navigation surface for non-admin users working inside a model.
- The list of items in Contents is **filtered by model role**: two users with different roles in the same model see different Contents.

## Admin Control: Selecting What Appears

Prerequisites before configuring Contents:

1. **Model roles must exist** — create them under Model Settings → Roles.
2. **Module access permissions must be assigned** to the role — a module cannot be shown in Contents for a role that has no access to it.

To configure:
- Go to **Model Settings → Contents**.
- The grid shows modules/dashboards on rows and model roles on columns.
- Check a cell to show that item for that role; uncheck to hide it.
- By default, all content a role can access is shown (all checkboxes enabled).

## Show New Content Toggle

When a new module or dashboard is added to the model, the **Show New Content** setting determines whether it automatically appears in Contents for a given role.

- Default: **On** — new items appear in Contents automatically.
- Can be toggled per Functional Area, per role from the Contents tab.
- Is automatically disabled (forced Off) when:
  - The role's access for a module is set to **None**.
  - The role lacks access to module data that drives a dashboard.

## Show Hidden Content Toggle

Admins can optionally allow any user to reveal hidden items from Contents at will, without needing to permanently re-enable them.

- When enabled, a **Show hidden content** toggle appears at the bottom of the Contents panel for all users in that model.
- Users can flip this toggle to see items the admin has deselected — but only items their role has access to.
- To enable: Model Settings → Contents → **View menu** → **Enable access to hidden content**.

> [!note]
> Enabling Show Hidden Content does not override role-based access. Users can only ever surface items their model role permits them to see. Contents visibility is a UX convenience layer, not a security boundary.

## Relationship to Model Roles

Contents is entirely role-scoped. The same module can be visible for one role and hidden for another:

- **Permissions** (model roles) govern whether a user can read or write data in a module.
- **Contents visibility** governs whether that module appears in the navigation at all.

A module hidden from Contents is still accessible if the user navigates directly to it (e.g. via a dashboard link).

## Related

- [[Model Roles]] — roles are the prerequisite for Contents configuration
- [[Access & Security — Overview]] — module access permissions sit beneath Contents visibility
- [[Model Actions]] — actions/processes can be published to UX pages surfaced via Contents
