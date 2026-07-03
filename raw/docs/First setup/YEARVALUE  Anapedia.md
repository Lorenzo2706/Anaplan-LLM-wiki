---
title: "YEARVALUE | Anapedia"
source: "https://help.anaplan.com/yearvalue-5df8cf5a-6609-4e14-832f-ddff9b29326b"
author:
published:
created: 2026-05-02
description: "The YEARVALUE function references another line item and returns the yearly time summary value for each time period within that year. The function replaces the period's individual value with the corresponding yearly summary."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The YEARVALUE function references another line item and returns the yearly time summary value for each time period within that year. The function replaces the period's individual value with the corresponding yearly summary.

For example, you can use the YEARVALUE function to identify sales across a year that are above average.

`YEARVALUE(Line item)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Line item* | Number, Boolean, date, time period, list, text | The line item to reference the yearly time summary value for. |

The YEARVALUE function returns a result of the same data type as the line item you reference.

In Polaris, you can't use the YEARVALUE function in a result line item with a time scale greater than the function.

The Classic Engine returns a value of 0 in this case.

You can't use the YEARVALUE function in a model that has the **Calendar Type** set to **Weeks: General**.

In this example, an *Income statement* module has line items on rows and Time on columns:

- The *Monthly sales* and the *Yearly sales* line items have **Number** data types
- The *Month above average for year* line item has a **Boolean** data type

In **Blueprint** view, in the [**Summary**](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) column for *Monthly sales*, **Time Summary** is set to **Average**. The formula for the *Yearly sales* returns the yearly summary average for every month of the year. The formula for the *Month above average for year* returns a TRUE result for values that are above the average value for each month of the year.

|  | **Jan 25** | **Feb 25** | **Mar 25** | **Apr 25** | **May 25** | **Jun 25** |
| --- | --- | --- | --- | --- | --- | --- |
| **Monthly sales** | 660,338 | 123,665 | 988,541 | 200,456 | 200,456 | 200,336 |
| **Yearly sales**   `YEARVALUE(Monthly sales)` | 236,444 | 236,444 | 236,444 | 236,444 | 236,444 | 236,444 |
| **Month above average for year**   `Monthly sales > YEARVALUE(Monthly sales)` |  |  |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fyearvalue-5df8cf5a-6609-4e14-832f-ddff9b29326b&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>