---
title: "WEEKVALUE | Anapedia"
source: "https://help.anaplan.com/weekvalue-191e147b-dd3a-4af0-8198-548ab39c8493"
author:
published:
created: 2026-05-02
description: "The WEEKVALUE function references another line item and returns the weekly time summary value for each time period within that week. The function replaces the period's individual value with the corresponding weekly summary."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The WEEKVALUE function references another line item and returns the weekly time summary value for each time period within that week. The function replaces the period's individual value with the corresponding weekly summary.

For example, you can use the WEEKVALUE function to identify daily sales that fell below average in a certain week.

`WEEKVALUE(Line item)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Line item* | Number, Boolean, date, time period, list, text | The line item to reference the weekly time summary value for. |

The WEEKVALUE function returns a result of the same data type as the line item you reference.

In Polaris, you can't use the WEEKVALUE function in a result line item with a time scale greater than the function.

The Classic Engine returns a value of 0 in this case.

- The line item that contains the WEEKVALUE function must have the **Time Scale** set to **Day** or **Week**.
- You can only use the WEEKVALUE function in models where the **Calendar Type** is based on weeks.

In this example, a *Product sales* module has line items on rows and Time on columns:

- The *Daily sales* and the *Weekly sales* line items have **Number** data types
- The *Day below average for week* line item has a **Boolean** data type

In **Blueprint** view, in the [**Summary**](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) column for *Daily sales*, **Time Summary** is set to **Average**. The formula for the *Weekly sales* returns the weekly summary average for every day of the week. The formula for the *Day below average for week* returns a TRUE result for values that are below the average value for each day of the week.

|  | **4 Jan 21** | **5 Jan 21** | **6 Jan 21** | **7 Jan 21** | **8 Jan 21** | **9 Jan 21** | **10 Jan 21** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Daily sales** | 200 | 254 | 122 | 543 | 233 | 350 | 431 |
| **Weekly sales**   `WEEKVALUE(Daily sales)` | 304.71 | 304.71 | 304.71 | 304.71 | 304.71 | 304.71 | 304.71 |
| **Day below average for week**   `Daily sales < WEEKVALUE(Daily sales)` |  |  |  |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fweekvalue-191e147b-dd3a-4af0-8198-548ab39c8493&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>