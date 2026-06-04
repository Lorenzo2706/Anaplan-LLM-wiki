---
title: "Apply time scales to individual line items"
source: "https://help.anaplan.com/apply-time-scales-to-individual-line-items-c4045bfd-934c-4816-8e44-e4ff3fa1a429"
author:
published:
created: 2026-05-13
description: "If you want to create a subsidiary view, you can apply different time scales to line items in a module. Subsidiary views show subsets of data."
tags:
  - "clippings"
---
[Line items](https://help.anaplan.com/line-items-52d76cdd-2571-4400-8f34-b15dd5651b9f "Line items")

If you want to create a subsidiary view, you can apply different time scales to line items in a module. Subsidiary views show subsets of data.

You can [set the time scale for either your entire model](https://help.anaplan.com/10a0397f-16ea-4e8a-97c2-1fee9c540ec7) in **Time** in the model settings bar, or different time scales for [line items in a module](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a). For example, if the default dimension is measured by **Year**, you can create a line item that has a time scale of **Month**.

To apply a different time scale to an individual line item:

1. Select **Modules** in the model settings bar.
2. Select the module that contains the line item you want to edit, then select **Open**.
3. Select **Blueprint** .
4. Select an option for your chosen line item in the **Time Scale** column.

When you change the time scale for a line item, a [subsidiary view](https://help.anaplan.com/b208ed3b-c958-4a55-94db-c297bc7c95cb) is automatically created.

If two line items have a different time scale, and one refers to the other in a formula:

- Days sum into months.
- Months sum into quarters.
- Quarters sum into years.

If required, you can skip different time levels. For example, days can sum into years.

If line item `X` has a time scale of **Months**, and line item `Y` has a time scale of **Years**, then `Y=X` returns the year total. However, `X=Y` returns a blank value, as `Y` contains no corresponding value for each month (`X`).

You can create formulas with the following functions to return a result:

- [WEEKVALUE](https://help.anaplan.com/191e147b-dd3a-4af0-8198-548ab39c8493)
- [MONTHVALUE](https://help.anaplan.com/0f2e55c3-8808-4b37-9017-7ea57e6f0d37)
- [QUARTERVALUE](https://help.anaplan.com/496d28ac-cf36-43bf-bc0e-06d4cc52c40e)
- [HALFYEARVALUE](https://help.anaplan.com/d78dd47b-5f5c-4e06-9788-7b1de7446b29)
- [YEARVALUE](https://help.anaplan.com/5df8cf5a-6609-4e14-832f-ddff9b29326b)
- [SELECT](https://help.anaplan.com/2ca3148d-466e-44bd-830e-7e5cf3ac8d08)

In the table below, the `X` and `Y` line items have the same time scales as above.

| **Example formulas** | **Explanation** |
| --- | --- |
| `Y=X` | The formula returns the relevant time total from `X`, where `X` has a more detailed timescale than `Y`. |
| `X=Y` | The formula returns a blank result, unless the [**Summary** method](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) is set to **Formula**, in which case it will show the value `Y` in the year totals only. |
| `X=YEARVALUE(Y)` | The formula returns the value of `Y` in each month. |
| `X=YEARVALUE(Y)/12` | The formula evenly allocates the value of `Y` over months. |
| `X=YEARVALUE(Y) * Seasonality %` | The formula allocates `Y` according to a seasonality percentage. |
| `X=Y[SELECT:Time.FY11]` | The formula returns the value of `Y` for a specific year. |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fapply-time-scales-to-individual-line-items-c4045bfd-934c-4816-8e44-e4ff3fa1a429&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>