---
title: "Data Hub | Anaplan Support"
source: "https://support.anaplan.com/data-hub-0b79439d-d310-4af3-b912-cffb2f52d771"
author:
published:
created: 2026-05-04
description: "Planual rules regarding data hubs."
tags:
  - "clippings"
---
There should be no need for composite list hierarchies in the Hub. They can be built to "test" the actions, but after testing they should be deleted.

| 5.07-01a Validation purposes | Used if data needs to be consolidated to check against source systems, although the flat modules with attributes can be used to sum data. |
| --- | --- |
| 5.07-01b Combining source systems | Used if you want to combine multiple source systems into one feed from the Data Hub to the spoke model(s). |

[Data Hubs: Purpose and Peak Performance](https://community.anaplan.com/t5/Best-Practices/Data-Hubs-Purpose-and-Peak-Performance/ta-p/48866)

Keep Analytical modules (modules with multiple lists in the Applies To) out of the Data Hub.

Use the flat list structures to create modules and views for downstream targets.

Get the data from IT in the correct format as well as the correct granularity.

Use System modules for filtering data (current period, current FY year, etc.).

Avoid creating master data in the hub. This should really come from the source system(s).

Use another reporting model (FIN Trans Data) to keep detailed transactional data out of the main planning models.

Large amounts of historic transactional data can inflate the size of the planning model and lead to reduced performance.

It is more efficient to aggregate the data in the hub and then export it, rather than accumulate it through the import to the downstream models.

Don't create a transaction list with a top level. The calculations will sum for all items in the list even if only a single item is added.

If a sum of all transactions is needed, consider using a "dummy" list and summing the data within a module dimensionalized by the "dummy" list.

[Top Level Item and Parent Hierarchy](https://community.anaplan.com/t5/Best-Practices/Top-Level-Item-and-Parent-Hierarchy/ta-p/56249)

If you need the totals for validation purposes, create intermediate sub-totals within the transaction list. This will significantly reduce the calculation load.

Another alternative would be to create a "dummy" list and sum the data using a list formatted member within the "Dummy" list.

Create the Data Hub in its own workspace. This allows for the Data Hub to expand in size without disrupting inbound or outbound integrations.

It also allows for segregation of duties (users who manage the data are kept separate from the production models).

If you need to consolidate your exports from multiple models to one export, create an Export Hub model to keep the Data Hub (data coming from outside source systems) clean.

Back to top