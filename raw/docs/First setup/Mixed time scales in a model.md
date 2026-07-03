---
title: "Mixed time scales in a model"
source: "https://help.anaplan.com/mixed-time-scales-in-a-model-5dd0aa9a-3f72-4bbb-8634-2712464e0bd0"
author:
published:
created: 2026-05-13
description: "Model builders can set a single calendar type for a model, but different timescales can also be set for modules and line items within the model."
tags:
  - "clippings"
---
Model builders can set a single calendar type for a model, but different timescales can also be set for modules and line items within the model.

Available time scales depend on the calendar type you select for a model.

| **Calendar type** | **Available time scales** |
| --- | --- |
| **Calendar Months/Quarters/Years** | Not Applicable, Day, Month, Quarter, Half-Year, Year.  **Note**: Quarter, and Half-Year options are available if the **Include: Quarter Totals**, or **Half-Year Totals** options are selected in the Model Calendar. |
| **Weeks: 13 4-week Periods** | Not Applicable, Day, Week, Month, Quarter\*, Year   **Note**: Quarter is available if the **Include: Quarter Totals** option is selected in the Model Calendar. |
| **Weeks: 4-4-5, 4-5-4 or 5-4-4** | Not Applicable, Day, Week, Month, Quarter\*, Half-Year\*, Year  **Note**: Quarter and Half-Year options are available if the **Include: Quarter Totals**, or **Half-Year Totals** options are selected in the Model Calendar. |
| **Weeks: General** | Not Applicable, Day, Week |

When line items in a module have different time scales, [subsidiary views](https://help.anaplan.com/b208ed3b-c958-4a55-94db-c297bc7c95cb) are created.

Where two line items each use a different timescale, and one refers to the other in a formula, then days aggregate into months, months aggregate into quarters, and quarters aggregate into years. You can also choose to skip levels. For example, days can aggregate into years.

If line item X has a time scale of months, and line item Y has a time scale of years, then Y=X returns the year total. However, X=Y returns nothing, because Y does not contain a corresponding value for each month.

You can set up formulas that use the [WEEKVALUE](https://help.anaplan.com/191e147b-dd3a-4af0-8198-548ab39c8493), [MONTHVALUE](https://help.anaplan.com/0f2e55c3-8808-4b37-9017-7ea57e6f0d37), [QUARTERVALUE](https://help.anaplan.com/496d28ac-cf36-43bf-bc0e-06d4cc52c40e), [YEARVALUE](https://help.anaplan.com/5df8cf5a-6609-4e14-832f-ddff9b29326b), or [SELECT](https://help.anaplan.com/2ca3148d-466e-44bd-830e-7e5cf3ac8d08) functions to return the results that you need. For example, if line item X is in months, and line item Y is in years:

| `Y = X` | Result takes the relevant time total from X, where X has a more detailed time scale than Y, such as X in months, Y in years. |
| --- | --- |
| `X = Y` | Shows a blank, unless the summary method is set to **Formula**, in which case it shows the value Y in the year totals only. |
| `X = YEARVALUE(Y) * Seasonality %` | Allocates Y according to a seasonality percentage. |
| `X = Y[SELECT:Time.FY11]` | Shows the value of Y for a specific year. |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmixed-time-scales-in-a-model-5dd0aa9a-3f72-4bbb-8634-2712464e0bd0&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>