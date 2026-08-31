---
title: "HALFYEARVALUE | Anapedia"
source: "https://help.anaplan.com/halfyearvalue-d78dd47b-5f5c-4e06-9788-7b1de7446b29"
author:
published:
created: 2026-05-02
description: "The HALFYEARVALUE function references another line item and returns the half-yearly time summary in place of the detail value."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The HALFYEARVALUE function references another line item and returns the half-yearly time summary in place of the detail value.

For example, you can use the HALFYEARVALUE function to identify monthly sales that fell below average in the first half of a year.

`HALFYEARVALUE(Line item)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Line item* | Number, Boolean, date, time period, list, text | The line item to reference the half-yearly time summary value for. |

The HALFYEARVALUE function returns a result of the same data type as the line item you reference.

In Polaris, you must enable **Half-year Totals** in the **Model Calendar** to use the HALFYEARVALUE function. In the Classic engine, you can use the HALFYEARVALUE function regardless of if **Half-year Totals** is enabled in the **Model Calendar**.

In Polaris, you cannot use the HALFYEARVALUE function in a result line item with a time scale greater than the function. The Classic Engine returns a value of 0 in this case.

- If you do not select **Half-Year Totals** in **Time** in the model settings bar, the HALFYEARVALUE function returns the line item's default value. For example, `0` for numeric line items.
- The line item that contains the HALFYEARVALUE function must have a time scale of Day, Month, Quarter, or Year.
- You cannot use the HALFYEARVALUE function in a model that has the **Calendar Type** set to Weeks: General.

In this example, an *Income Statement* module has line items on rows and Time on columns. The *Cost of Goods* line item has a numeric data type, and the *Month below average for half year* line item has a Boolean data type.

In this example, in the [**Summary**](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) column for *Cost of Goods,* **Time Summary** is set to **Average**. The formula returns a TRUE result for values that are below average for each month in the first half of the year.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** | **May 21** | **Jun 21** | **H1 FY21** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cost of Goods | 103,000 | 99,332 | 98,000 | 95,660 | 79,000 | 80,500 | 92,582 |
| Month below average for half year  `Cost of Goods < HALFYEARVALUE(Cost of Goods)` |  |  |  |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fhalfyearvalue-d78dd47b-5f5c-4e06-9788-7b1de7446b29&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>