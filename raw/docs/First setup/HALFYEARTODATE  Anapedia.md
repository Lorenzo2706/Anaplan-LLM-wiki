---
title: "HALFYEARTODATE | Anapedia"
source: "https://help.anaplan.com/halfyeartodate-7e11523e-4d49-49c4-9bb7-e762e1722145"
author:
published:
created: 2026-05-02
description: "The HALFYEARTODATE function cumulates values from a single numeric parameter, over a half-year period. The HALFYEARTODATE cumulation starts at the Fiscal Year Start Month as selected in the Model Calendar, and resets every half-year."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The HALFYEARTODATE function cumulatesvalues from a single numeric parameter, over a half-year period. The HALFYEARTODATE cumulation starts at the **Fiscal Year Start Month** as selected in the **Model Calendar**, and resets every half-year.

You could use HALFYEARTODATE to track revenue over half-year periods.

`HALFYEARTODATE(Line item to cumulate)`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *Line item to*   *cumulate* | Number | The line item to cumulate over half-year periods. |

The HALFYEARTODATE function returns a number.

In Polaris, you can use the HALFYEARTODATE function with line items with a time scale of **Half-Year**. In the Classic Engine, you cannot.

In Polaris, you cannot use HALFYEARTODATE in formulas of line items with a formula summary method. In the Classic Engine, you can.

`HALFYEARTODATE(Sales)`

- The **Time Scale** of source must be Day, Week, Month, or Quarter.
- You cannot use this function if model **Calendar Type** is **Weeks: General**.

The example below shows HALFYEARTODATE applied to sales.

|  | **Q1**   **FY18** | **Q2**   **FY18** | **Q1**   **FY19** | **Q2**   **FY19** | **Q1 FY20** | **Q2 FY20** | **Q1**   **FY21** | **Q2**   **FY21** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *Sales* | 24,977 | 28,500 | 34,585 | 31,708 | 37,102 | 33,943 | 41,663 | 38,338 |
| `HALFYEARTODATE`   `(Sales)` | 24,977 | 53,477 | 34,585 | 66,293 | 37,102 | 71,045 | 41,663 | 80,001 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fhalfyeartodate-7e11523e-4d49-49c4-9bb7-e762e1722145&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>