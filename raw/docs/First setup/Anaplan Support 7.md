---
title: "Anaplan Support"
source: "https://support.anaplan.com/modules-b2d142a4-53fe-4809-9ace-3cd9e51547db"
author:
published:
created: 2026-05-04
description: "Planual rules regarding Modules."
tags:
  - "clippings"
---
[Classic](https://support.anaplan.com/classic-a182c8c4-2e69-437d-8871-78346dc8b1bf "Classic")

Keep names as short as is practical. Use alphanumeric to help identify modules from long names. There's no need to prefix modules in line with DISCO. It's better to align them with functional areas.

| 2.01-01a Space saving for user-facing modules | User-facing modules can be renamed to a more descriptive name if required to save on dashboard space, but be mindful of not cramming too much onto a dashboard as per the general design principles. |
| --- | --- |

[Good Naming Convention](https://help.anaplan.com/name-conventions-aeb0b95e-f7a3-4fe5-81c7-aec9a12f80be)

Use functional areas to categorize modules.

Use these to provide sections and ordering to the Modules list, but don't use emojis. These modules are regular modules without any line items.

Within functional areas, group "like" modules together. Design for the type of module and use the appropriate structures.

The DISCO convention is designed to categorize types of modules. Within a functional area you may have multiple types of modules.

Subsidiary views are difficult to work with and audit. Try and minimize their use especially for calculation modules. Create groups of calculation modules instead with like dimensionality.

| 2.01-06a Display on Dashboards for analysis or filtering | Sometimes, to enhance the end user experience, attributes are needed to be shown on pages. |
| --- | --- |
| 2.01-06b Ratio formulas | Numeric values for ratios need to be in the same module and are unlikely to need the full dimensionality. |
| 2.01-06c Synchronization for ‌pages | If you have pages that need to synchronize from a module, sometimes a specific line item is needed. |
| 2.01-06d Line items needed for sorting | Sometimes to facilitate a sort, the line items don't need the full module dimensionality. |
| 2.01-06e Reporting or Export modules | To use filtering in reports or to provide attributes for exports (model to model), you may need to have line items for the non-dimensional attributes. Make sure these are set as subsidiary views to minimize the calculations. |

Create all functions and filters relating only to time in separate modules. They will only re-calculate on model opening and when the time settings change.

It's best practice to use a separate module for each time granularity (‌week, month, quarter, year, etc.).

Create a System module to support all standing data and attributes about the hierarchy (all levels). At a minimum, have the code and parent as line items.

| 2.01-08a SYS Module isn't needed | If the hierarchy isn't referenced in a formula as a filter or a selector module on a dashboard then it isn't needed. |
| --- | --- |

[Best Practice for Module Design](https://community.anaplan.com/t5/Knowledge/Best-Practices-for-Module-Design/ta-p/35993)

Create a module with no dimensions to hold assumptions for Time and other "SELECT" values. These are useful for global assumptions and general setting that are used throughout the model. They're also useful within an Application Lifecycle Management (ALM) setup.

Keep summary options off, which is the default. It's better to use SUM for any downstream aggregation if all levels of the hierarchy aren't needed.

| 2.01-10a All aggregation levels are needed | If all aggregation levels are needed, then it's faster to use ‌native aggregation than to use the SUM formula. |
| --- | --- |

Make sure the dimension order is consistent among modules. Calculations are faster if the common dimensions are in the same order as the Applies To. The size of the list isn't as critical as the order.

[Dimension Order](https://community.anaplan.com/t5/Knowledge/Dimension-Order/ta-p/32934)

Create Calculation modules to house sets of line items using the same dimensionality. Avoid using Subsidiary views.

Keep the non-time-based data in a separate module from static attributes.

[Data Hubs Purpose and Peak Performance](https://community.anaplan.com/t5/Best-Practices/Data-Hubs-Purpose-and-Peak-Performance/ta-p/48866)

Don't use Select levels combined with filters on the same hierarchy. It's a double filter and is inefficient because both will be kicked off. Use one or the other. Setting a Boolean line item in a System module with 'none' as the summary option will achieve the same result.

Try and keep filters in separate System modules. They can then be reused for different modules. In the notes section, describe where and how this filter is used to prevent accidental deletion as the Reference By column won't list filters on views.

If not using for other reasons, use Data Tags to signify the DISCO category.

Create separate modules for Access Drivers for relevant combinations to be reused. This helps the overall maintenance and enablement of the model, and it can also help decrease repeated logic. Use different line items for different settings if needed.

Copying large modules, especially those with filters and many views, can take time and block the model while doing so. For large modules, it's likely to be quicker to re-create the module.

If you're using lists instead of native timescale or native versions, ensure these lists are placed as the first two lists in the dimension order. This mirrors the native time and version settings and will improve performance when mapping between native time/versions and standard lists.

[Dimension Order](https://community.anaplan.com/t5/Best-Practices/Dimension-Order/ta-p/32934)

When creating a module, consider the scope of the calculation and only include the dimensions that are needed. If the formula doesn't return the value required, or errors, don't keep adding dimensions until it renders the correct data. It's better to review the calculation itself. Check other modules, you may already have a calculation module with the relevant dimensions, so add the calculation in the existing module.

Back to top