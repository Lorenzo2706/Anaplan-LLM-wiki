---
title: "Anaplan Support"
source: "https://support.anaplan.com/lists-66ad1f4c-7c96-4faf-b69f-3c012ffa1e15"
author:
published:
created: 2026-05-04
description: "Planual Rules regarding Lists."
tags:
  - "clippings"
---
Hierarchies should be prefixed with a letter signifying the name of the hierarchy and a number indicating the level. For example, P1 Product Category, P2 Product Family, P3 Products. There's no need to add "L" as a prefix to lists.

[Good Practice Naming Conventions](https://help.anaplan.com/name-conventions-aeb0b95e-f7a3-4fe5-81c7-aec9a12f80be)

Using codes is more efficient for loading and using lists so strive to always have a code for lists. This is especially important for numbered lists.

| 1.05-02a Static non-hierarchy lists | For simple static lists (such as Yes/No), it's OK not to have a code, but even then, Y and N can be used as codes. |
| --- | --- |

List properties are the same as line items but have many limitations, so keep it simple and have one place for calculations, for example, Module.Line Item.

| 1.05-03a Reference module line items | Where the following exceptions are used, reference module line items through a formula where possible to keep the audit trail valid. |
| --- | --- |
| 1.05-03b Numbered lists (and related actions) | Assign actions and associated filters require list properties. |
| 1.05-03c Exports | List properties can be used as export labels. |
| 1.05-03d Conditional Page navigation | List properties are needed to facilitate navigation to different dashboards based on the selection in the list. |
| 1.05-03e Dependent drop-downs | List properties are needed to create driver and dependent lists. |

[Data Hubs and Peak Performance](https://community.anaplan.com/t5/Best-Practices/Data-Hubs-Purpose-and-Peak-Performance/ta-p/48866)

If you're using Create or Assign actions for Numbered lists, try and incorporate a "code creation" action, as part of another process.

| 1.05-04a Combination of properties | If there's no code in the source, you'll have to use a combination of properties. Try and avoid if possible, as this is slower to import and more difficult to use without a code. |
| --- | --- |

Format the Display Name property for Numbered lists as List Formatted, not text. This is more efficient, saves a line item, minimizes text fields, and simplifies mappings. However, it's not recommended to create a separate list purely for this purpose. Use an existing list if possible.

Only use Top level for lists that will need sums so not Currency codes, or True/False (Indicators), or children in composite lists.

[Top Level Item and Parent Hierarchy](https://community.anaplan.com/t5/Best-Practices/Top-Level-Item-and-Parent-Hierarchy/ta-p/56249)

The calculation for a top level on a large list cannot be split, so as the list grows, the calculation becomes increasingly inefficient. Consider if you really need the total. If you do need to have the totals, look to add intermediate parent “totals” to make the calculations more efficient or use SUM to aggregate for validations.

[Top Level Item and Parent Hierarchy](https://community.anaplan.com/t5/Best-Practices/Top-Level-Item-and-Parent-Hierarchy/ta-p/56249)

Composite lists are more flexible and calculate more efficiently so try and "balance" the hierarchies whenever possible.

| 1.05-08a Chart of Accounts or financial reporting hierarchies | Chart of Accounts or financial reporting hierarchies are valid uses of non-composite lists. |
| --- | --- |

[Balanced ‌v unbalanced hierarchies](https://community.anaplan.com/discussion/95084/balanced-vs-unbalanced-hierarchies)

Add placeholders to organize General Lists and add Subsets and Line Item Subsets at the bottom of the General Lists. This will ensure that Subsets and Line Item Subsets can be easily identified when referring to them in the 'Applies To'. It's OK to use emojis for the placeholder lists.

Clearing and reloading a list increases the structural changes within a model and will increase the likelihood of a model save. This will increase the import time. It also removes pre-allocated memory blocks designed to increase efficiency. Use a unique key to update to values rather than delete and re-load. Also consider adding a TRUE field to the data source that will allow you to know which records have been imported.

Dates and values are "data" and should not be part of a code. Adding these elements to the code will usually vastly increase the size of the list and consequently increase the model size and reduce performance.

Based off the code of the list, it should be possible to derive the attributes. Calculating the values is more efficient than storing text fields.

Avoid having hierarchies in Data Hub. These should only apply to the main planning models.

Back to top