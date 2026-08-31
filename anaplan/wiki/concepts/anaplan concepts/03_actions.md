---
title: Model Actions
type: concept
tags: [anaplan, actions, imports, exports, processes, automation]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Model actions.md
---

# Model Actions

Actions are **pre-configured, repeatable routines** that workspace administrators set up to automate common tasks in an Anaplan model — data imports, exports, list management, version copying, optimization runs, and more.

## What Actions Are

- An action encapsulates a single task (e.g., "import forecast data from S3", "delete stale list members", "update current period").
- Once saved, an action is stored in the **Actions pane** and can be re-run on demand without reconfiguring it each time.
- Actions can be **chained into a process** so that multiple steps execute sequentially in a single click.
- Scheduling is possible via integrations such as Anaplan Connect.

## Where Actions Run From

| Surface | Who can use it |
|---|---|
| **Actions pane** (model build area) | Workspace administrators only |
| **Dashboard button** (classic UI) | Any user with access to that dashboard |
| **UX page / action card** | Any user with access to that page |
| **Process** (triggered from dashboard or UX) | Any user — the process surfaces all wrapped actions |

> [!note]
> Some actions must be published to a dashboard or added to a process before non-admin users can run them. Actions that open a dashboard (Open dashboard, Create, etc.) cannot be wrapped in a process.

## Setup vs. Execution

- **Setup** (creating or editing an action) — workspace administrators only, via the Actions pane → New Action menu.
- Imports and exports are configured separately (through the import/export wizard) but are saved as actions in the Actions pane once created.
- **Execution** — admins can run most actions directly from the Actions pane; non-admins run only actions published to dashboards or UX pages.

## Action Types Reference

| Action | Can be added to a process | Admin-only to run |
|---|---|---|
| Imports and exports | Yes | Only if the default file is set to Admins Only |
| Delete from list using selection | Yes | No |
| Order list | Yes | No |
| Open dashboard | No | No |
| Create | No | No |
| Delete branch | No | No |
| Assign / Assign only | No | No |
| Update current period | Yes | Yes |
| Copy branch | No | No |
| Optimizer | Yes | No (requires Enterprise + Optimizer enabled) |
| Bulk copy | Yes | Yes, unless enabled for all users |

> [!warning] Polaris limitation
> **Optimizer** actions are not available in Polaris-engine models.

## Processes

A **process** is a container that groups individual actions into an ordered sequence. Processes can be:
- Published to a dashboard button (classic UI)
- Added to a UX action card
- Run from the Actions pane by admins

Page builders can add imports and exports directly to UX action cards without wrapping them in a process. All other non-import/export actions must be added to a process first before they can appear in the UX.

## Related

- [[Model Roles]] — determines which users can run published actions
- [[Contents Panel]] — actions/processes can be published to UX pages surfaced via Contents
- [[DISCO — Module Classification]] — imports typically feed Data/Input modules; exports typically source from Output modules
