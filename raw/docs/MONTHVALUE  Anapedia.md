---
title: "MONTHVALUE | Anapedia"
source: "https://help.anaplan.com/monthvalue-0f2e55c3-8808-4b37-9017-7ea57e6f0d37"
author:
published:
created: 2026-05-02
description: "The MONTHVALUE function references another line item and returns the monthly time summary value for each time period within that month. The function replaces the period's individual value with the corresponding monthly summary."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The MONTHVALUE function references another line item and returns the monthly time summary value for each time period within that month. The function replaces the period's individual value with the corresponding monthly summary.

For example, you can use the MONTHVALUE function to identify what percentage a given week contributes to monthly sales.

`MONTHVALUE(Line item)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Line item* | Number, Boolean, date, time period, list, text | The line item to reference the monthly time summary value for. |

The MONTHVALUE function returns a result of the same data type as the line item you reference.

In Polaris, you can't use the MONTHVALUE function in a result line item with a time scale greater than the function.

The Classic Engine returns a value of 0 in this case.

- If the line item you reference has a time scale of **Quarter** or above, then the reference returns the line item's default value. For example, `0` for numeric line items.
- You can't use the MONTHVALUE function in a model that has the **Calendar Type** set to **Weeks: General**.

In this example, a *Product sales* module has line items on rows and Time on columns:

- The *Weekly sales* and the *Monthly sales* line items have **Number** data types
- The *Week above average for month* line item has a **Boolean** data type

In **Blueprint** view, in the [**Summary**](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) column for *Weekly sales*, **Time Summary** is set to **Average**. The formula for the *Monthly sales* returns the monthly summary average for every week of the month. The formula for the *Week above average for month* returns a TRUE result for values that are above the average value for each week of the month.

|  | **Week 1 FY21** | **Week 2 FY21** | **Week 3 FY21** | **Week 4 FY21** |
| --- | --- | --- | --- | --- |
| **Weekly sales** | 833 | 860 | 867 | 812 |
| **Monthly sales**   `MONTHVALUE(Weekly sales)` | 843 | 843 | 843 | 843 |
| **Week above average for month**   `Weekly sales > MONTHVALUE(Weekly sales)` |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmonthvalue-0f2e55c3-8808-4b37-9017-7ea57e6f0d37&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>