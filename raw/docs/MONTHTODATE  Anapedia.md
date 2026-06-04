---
title: "MONTHTODATE | Anapedia"
source: "https://help.anaplan.com/monthtodate-a5fb44d0-43cf-418b-ac60-295e09ae295a"
author:
published:
created: 2026-05-02
description: "MONTHTODATE cumulates values from a single numeric parameter, within a monthly time range."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

You could use MONTHTODATE to compare orders received this month with the orders from previous months, up to and including the same day. MONTHTODATE resets at each monthly start date, based on **Calendar Type**.

`MONTHTODATE(Line item to aggregate)`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *Line item to*   *aggregate* | Number | The line item to aggregate in a monthly timeframe. |

In Polaris, you can use the MONTHTODATE function with line items with a time scale of **Month**. In the Classic Engine, you cannot.

In Polaris, you cannot use MONTHTODATE in formulas of line items with a formula summary method. In the Classic Engine, you can.

`MONTHTODATE(Sales)`

In the example below, MONTHTODATE cumulates sales for each month.

At week five, the start of the next month, MONTHTODATE resets.

|  | **Week 1   FY21** | **Week 2**   **FY21** | **Week 3**   **FY21** | **Week 4**   **FY21** | **Week 5**   **FY21** | **Week 6**   **FY21** |
| --- | --- | --- | --- | --- | --- | --- |
| *Sales* | 38,621 | 42,609 | 46,458 | 43,779 | 35,211 | 40,943 |
| `MONTHTODATE`   `(Sales)` | 38,621 | 81,230 | 127,688 | 171,467 | 35,211 | 76,154 |

- The line item argument in the MONTHTODATE function must have a **Time Scale** of Day or Week.
- MONTHTODATE cannot be used if the model has a **Calendar Type** of **Weeks: General**.

`MONTHTODATE(Stock)`

|  | **Week 1**   **FY22** | **Week 2**   **FY22** | **Week 3**   **FY22** | **Week 4**   **FY22** | **Week 5**   **FY22** | **Week 6**   **FY22** | **Week 7**   **FY22** | **Week 8**   **FY22** | **Week 9**   **FY22** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *Stock* | 4,188 | 3,543 | 3,967 | 4,297 | 4,024 | 3,827 | 4,216 | 4,388 | 3,635 |
| `MONTHTODATE`   `(Stock)` | 4,188 | 7,731 | 11,698 | 15,995 | 4,024 | 7,851 | 12,067 | 16,455 | 3,635 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmonthtodate-a5fb44d0-43cf-418b-ac60-295e09ae295a&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>