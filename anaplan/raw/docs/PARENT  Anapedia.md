---
title: "PARENT | Anapedia"
source: "https://help.anaplan.com/parent-1cdc486d-c4d7-42db-8b1a-d9e12c060999"
author:
published:
created: 2026-05-02
description: "The PARENT function returns the parent item of list items and time periods."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use PARENT to see which quarter a month belongs to.

`PARENT(Child value)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Child value | List, time period | The list or time period to return the parent of.  If the item has no parent, the function returns a blank value. |

The PARENT function returns a value of the same data type as the *Child value* argument. However, the level within the list hierarchy is different.

In Polaris, the parent of **Years** within the Time list is **All Periods**.

In the Classic Engine, **All Periods** has a time scale of **Years**, which means **Years** is the parent of **Years**.

In Polaris, the results of formulas are not coerced into different timescales. For example, if a formula returns a result with a **Months** timescale in a line item with the **Years** timescale, the formula is invalid.

In the Classic Engine, the results of formulas are coerced into different timescales. For example, if a formula returns a result with a **Months** timescale in a line item with the **Years** timescale, the **Months** value automatically converts to display in the **Years** line item.

`PARENT(Time.'Jan 21')`

In this example, there are two lists, *Outlets* and its parent list *Territories*. The relationship of these lists is shown in the table below as they display in **General Lists**.

|  | **Parent** | **Code** |
| --- | --- | --- |
| Outlet A1 | Territory A |  |
| Outlet A2 | Territory A |  |
| **Territory A** | Total |  |
| Outlet B1 | Territory B |  |
| Outlet B2 | Territory B |  |
| **Territory B** | Total |  |
| **Total** |  |  |
| New Outlet 1 |  |  |
| New Outlet 2 |  |  |

In the table below, three columns are line items and the rows are items from the *Outlets* list.

The *Parent Territory* line item has the list data type, and the *Territories* list is selected. The line item uses a formula that contains the PARENT and ITEM functions with the *Outlets* list. The ITEM function returns the list item for the *Outlets* list, and the PARENT function returns the parent of that list item, which is the territory.

The formula returns a blank result for the *New Outlet 1* and *New Outlet 2* list items as they do not have a parent.

|  | **Allocation %** | **Forecast** | **Parent Territory**  `PARENT(ITEM(Outlets))` |
| --- | --- | --- | --- |
| Outlet A1 | 60.0% | 120,000 | Territory A |
| Outlet A2 | 40.0% | 80,000 | Territory A |
| **Territory A** | 100.0% | 200,000 |  |
| Outlet B1 | 75.0% | 150,000 | Territory B |
| Outlet B2 | 25.0% | 50,000 | Territory B |
| **Territory B** | 100.0% | 200,000 |  |
| New Outlet 1 | 30.0% | 60,000 |  |
| New Outlet 2 | 70.0% | 140,000 |  |

In the table below, the rows are line items and the columns are items from the *Project Dates* list.

The formula used in the *Parent Quarter* line item uses the PARENT function to return the parent of each month in the *Month Period* line item. For time periods, quarters are the parent of months, so the formula returns the quarter that the month belongs to.

|  | **Start date** | **Expiry date** |
| --- | --- | --- |
| Month period | Feb 21 | Apr 21 |
| Parent Quarter  `PARENT(Month period)` | Q1 FY21 | Q2 FY21 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fparent-1cdc486d-c4d7-42db-8b1a-d9e12c060999&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>