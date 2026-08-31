---
title: Data Tags
type: concept
tags: [anaplan, data-tags, search, metadata, lists, modules, line-items]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/Data tags.md
  - raw/docs/Levels of model access.md
---

# Data Tags

## What Data Tags Are

Data tags are **keyword labels** that workspace administrators apply to model objects to group related information and make it searchable. They function as a metadata tagging system within a model — similar to tags in a content management system.

Data tags are managed in **Data Tags** in the model settings bar (workspace administrator access only — Data Tags is not visible to end users).

## What Can Be Tagged

Data tags can be applied to:

| Object type | Scope |
|---|---|
| Lists | Tag a whole list |
| List properties | Tag individual properties within a list |
| Modules | Tag a whole module |
| Line items | Tag individual line items within a module |

## How They Work

1. Workspace administrators create data tags in the Data Tags settings pane (create, delete, reorder).
2. Tags are then applied to lists, list properties, modules, or line items.
3. Any user with model access can **search** for a tag by keyword and find all model objects sharing that tag.

A search by tag keyword returns all tagged objects across the entire model that carry that tag — regardless of which module or list they belong to.

## Use Cases

- **Cross-list entity tracking.** If a concept like "Account" appears in multiple lists (e.g., a Customer Accounts list, a GL Accounts list, a Budget Accounts list), tagging all three with `account` allows a user to search for "account" and find all related lists at once.
- **Thematic grouping.** Tag all line items related to headcount with `headcount` to quickly find them across modules.
- **Audit and documentation.** Tags can serve as a lightweight documentation layer — tagging all line items that feed a specific KPI, regulatory report, or integration target.
- **Change management.** During a model refactor, tag affected objects to track scope.

## Constraints and Gotchas

- Data Tags management (create/delete/reorder) is **workspace administrator only**. End users can search for tagged objects but cannot create or modify tags.
- Tags are model-scoped — a tag in one model is not shared across models in the workspace.
- There is no hierarchical relationship between tags — they are flat labels.
- There is no validation that a tag is used consistently; two admins could create near-duplicate tags (`headcount` vs. `Head Count`) and fragment the tagging scheme. Establish naming conventions before tagging at scale.
- Deleting a tag in the Data Tags pane removes it from all objects it was applied to.
- Tags do not affect access control, security, or calculations — they are purely a discovery/metadata mechanism.

## Design Recommendations

- **Agree on a tag taxonomy before tagging at scale.** Establish a controlled vocabulary: lowercase, no spaces (use hyphens), singular nouns where possible (e.g., `headcount`, `revenue`, `cost-center`).
- **Tag at the right granularity.** Tagging entire modules is coarser but faster to apply; tagging individual line items is precise but labor-intensive. Match granularity to the search use case.
- **Use tags to bridge DISCO categories.** In a large model, a concept like "revenue" may appear in SYS lists, DAT input modules, CALC calculation modules, and OUT output modules. Tags let you locate all `revenue`-related objects without knowing which module they live in.
- **Document integration touchpoints.** Tag all line items that are source or target for external integrations — makes impact analysis faster when the integration changes.

## Relationship to Other Features

Data tags have no interaction with access control (model roles, SA, DCA). They are purely organizational/search metadata. Any user with access to the model can search by tag; the search results respect the user's model role (they will not see objects in modules they have no access to).

Data Tags is one of the model settings features accessible only to workspace administrators (alongside Time, Versions, General Lists, Modules, Line Item Subsets, Users, Actions, Source Models, History, Contents, Dashboards).

## Related Pages

- [[02_access-security]] — model settings access restricted to workspace administrators
- [[13_model-roles]] — controls which modules/objects a user can see (affects tag search results)
- [[11_lists]] — lists and list properties are taggable objects
- [[10_line-item]] — line items are taggable objects
