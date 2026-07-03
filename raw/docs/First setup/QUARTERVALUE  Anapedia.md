---
title: "QUARTERVALUE | Anapedia"
source: "https://help.anaplan.com/quartervalue-496d28ac-cf36-43bf-bc0e-06d4cc52c40e"
author:
published:
created: 2026-05-02
description: "The QUARTERVALUE function references another line item and returns the quarterly time summary in place of the detail value."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The QUARTERVALUE function references another line item and returns the quarterly time summary in place of the detail value.

For example, you can use the QUARTERVALUE function to identify monthly sales that fell below average in a quarter.

`QUARTERVALUE(Line item)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Line item* | Number, Boolean, date, time period, list, text | The line item to reference the quarterly time summary value for. |

The QUARTERVALUE function returns a result of the same data type as the line item you reference.

In Polaris, you cannot use the QUARTERVALUE function in a result line item with a **Time Scale** greater than the function.

The Classic engine returns a value of 0 in this case.

- If you do not select **Quarter Totals** in **Time** in the model settings bar, the QUARTERVALUE function returns the line item's default value. For example, `0` for numeric line items.
- You cannot use the QUARTERVALUE function in a model that has the **Calendar Type** set to Weeks: General.

In this example, an *Income Statement* module has line items on rows and Time on columns. The *Cost of Goods* line item has a numeric data type, and the *Month below average for quarter* line item has a Boolean data type.

In Blueprint,in the [**Summary**](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) column for *Cost of Goods*, **Time Summary** is set to **Average**. The formula returns a TRUE result for values that are below average for each month in the quarter.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Q1 FY21** |
| --- | --- | --- | --- | --- |
| Cost of Goods | 198,000 | 190,453 | 123,000 | 170,484 |
| Month below average for quarter  `Cost of Goods < QUARTERVALUE(Cost of Goods)` |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fquartervalue-496d28ac-cf36-43bf-bc0e-06d4cc52c40e&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>