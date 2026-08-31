---
title: Anapedia — Core Concepts & Security (full ingest)
type: source
tags: [anaplan, anapedia, concepts, access, security, lists, dimensions, time, versions]
created: 2026-05-13
updated: 2026-05-13
sources:
  - raw/docs/ (103 new files — see categories below)
---

# Anapedia — Core Concepts & Security (full ingest)

Ingest of 103 new Anapedia documentation files added to `raw/docs/` on 2026-05-13, covering foundational model structure, time/calendar, access/security, users, picklists, and data tags.

## Source categories

### Core model structure (13 files)
`Dimensions  Anapedia.md`, `Line items.md`, `Configure line items.md`, `Format line items.md`, `Apply styles to line items.md`, `Summary methods.md`, `Sum up line items into a parent.md`, `Subsidiary views.md`, `Create subsidiary views.md`, `Page selectors and nested dimensions.md`, `Cell count limit on line item blocks.md`, `Manage model size.md`, `Example Create EMP03 Employee Expenses by Country module.md`

### Lists & hierarchies (20 files)
`General lists.md`, `List types.md`, `List hierarchies.md`, `Configure lists.md`, `Create lists.md`, `Add and delete list items.md`, `Create list properties.md`, `Add formulas to list properties.md`, `Numbered lists.md`, `Numbered lists and functions.md`, `Convert lists to numbered lists.md`, `Create display names for numbered lists.md`, `Preserve list item names in numbered lists.md`, `Use numbered lists in composite hierarchies.md`, `Composite hierarchies.md`, `Reset the list index.md`, `List subsets.md`, `Create list subsets.md`, `Delete list subsets.md`, `Delete lists.md`

### Versions & Time (27 files)
`Versions  Anapedia.md`, `Create versions.md`, `Delete versions.md`, `Restrict version edits.md`, `Bulk copy versions.md`, `Variance reports with versions.md`, `Variance reports without versions.md`, `Time  Anapedia.md`, `Time ranges.md`, `Time range fundamentals.md`, `Work with time ranges.md`, `Create a new time range.md`, `Edit a time range.md`, `Delete a time range.md`, `Remove references to a time range.md`, `Mixed time scales in a model.md`, `Apply time scales to individual line items.md`, `Set the model calendar.md`, `Set the Calendar MonthsQuartersYears calendar.md`, `Set the Weeks 13 4-week Periods calendar.md`, `Set the Weeks 4-4-5, 4-5-4, or 5-4-4 calendar.md`, `Set the Weeks General calendar.md`, `Time period selection.md`, `Changes to the Fiscal Year Label.md`, `Example Create SYS11 Time Variance Reporting input module.md`, `Example Create REP05 Variance Report staging module.md`, `Example Create REP06 Variance Report module.md`

### Access & Security (23 files)
`Selective access.md`, `Enable selective access for a list.md`, `Selective access and list hierarchies.md`, `Selective access and picklists.md`, `Selective access example.md`, `Dynamic cell access.md`, `Access drivers.md`, `Access driver recommendations.md`, `Create an access driver module.md`, `Model roles.md`, `Add a model role.md`, `Levels of model access.md`, `Control user access within models.md`, `Assign action permissions to model roles.md`, `Assign list permissions to model roles.md`, `Assign module permissions to model roles.md`, `Assign version permissions to model roles.md`, `Assign a user to a model role.md`, `Assign selective access to lists and list items.md`, `Example Control access to sales by customer.md`, `Example Control access to time periods.md`, `Select the landing dashboard for a model role.md`, `Organize model Contents by model role.md`

### Users (6 files)
`Users list.md`, `Add a top-level item to the Users list.md`, `Create Users list subsets.md`, `Add users to a workspace from a model.md`, `Remove users from a workspace in a model.md`, `Designate workspace administrators.md`

### Picklists (5 files)
`Picklists  Anapedia.md`, `Set picklists on line items.md`, `Create many-to-many filtered picklists.md`, `Create one-to-many filtered picklists.md`, `Actions and filtered picklists.md`

### Other (1 file)
`Data tags.md`

## Wiki pages created/updated

### New concept pages (17)
- `wiki/concepts/dimensions.md` — six dimension types, cell context, pivoting, Applies To
- `wiki/concepts/lists.md` — list types, hierarchy, properties, subsets, rules
- `wiki/concepts/numbered-lists.md` — integer index, display names, conversion, key functions
- `wiki/concepts/composite-hierarchies.md` — multi-list rollup, Parent Hierarchy, PARENT/ISANCESTOR limits
- `wiki/concepts/summary-methods.md` — all methods, FORMULA vs Sum (Polaris warning), NONE default
- `wiki/concepts/subsidiary-views.md` — triggers, efficiency, Start of Section, dashboard constraints
- `wiki/concepts/versions.md` — native Versions, switchover, bulk copy, native vs version-as-list trade-offs
- `wiki/concepts/time-ranges.md` — fixed spans, mixed time scales, aggregation/disaggregation rules
- `wiki/concepts/model-calendar.md` — calendar types, fiscal year label, gotchas on changing calendar
- `wiki/concepts/access-security.md` — three-layer model, most-restrictive-wins, decision guide
- `wiki/concepts/model-roles.md` — four permission types, No Access data deletion, design patterns
- `wiki/concepts/selective-access.md` — lock-out risk, hierarchy propagation, picklist interaction, import None
- `wiki/concepts/dynamic-cell-access.md` — four DCA states, dimension compatibility, interaction with model roles
- `wiki/concepts/access-drivers.md` — SYS module pattern, naming, many-to-one sharing, suggested module set
- `wiki/concepts/users.md` — Users list as dimension, subsets, workspace admin capabilities table
- `wiki/concepts/picklists.md` — simple/filtered (1:M and M:M), SA interaction, Assign action pattern
- `wiki/concepts/data-tags.md` — taggable objects, search, taxonomy recommendations

### New pattern page (1)
- `wiki/patterns/variance-reporting.md` — with/without Versions approaches, SYS11/REP05/REP06 three-module chain, LIS + COLLECT pattern

### Updated concept page (1)
- `wiki/concepts/line-item.md` — added data types table, styles table, Blueprint column reference, cell count limits, cross-module formula examples, line item hierarchy mechanics
