---
title: "YEARTODATE | Anapedia"
source: "https://help.anaplan.com/yeartodate-5b08fc8e-0fed-47e1-b5dc-f846a22e6431"
author:
published:
created: 2026-05-02
description: "YEARTODATE cumulates values from a single numeric parameter, within a yearly time range. YEARTODATE resets at each yearly start date, based on Calendar Type."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

YEARTODATE cumulatesvalues from a single numeric parameter, within a yearly time range. YEARTODATE resets at each yearly start date, based on **Calendar Type**.

You could use YEARTODATE to compare sales from the same period of another year.

`YEARTODATE(Line item)`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *Line item to*   *cumulate* | Number | The line item to cumulate in a yearly timeframe. |

The YEARTODATE function returns a number.

In Polaris, you can use the YEARTODATE function with line items with a time scale of **Year**. In the Classic Engine, you cannot.

In Polaris, you cannot use YEARTODATE in formulas of line items with a formula summary method. In the Classic Engine, you can.

`YEARTODATE(Sales)`

- The **Time Scale** of source must be Day, Week, Month, Quarter, or Half-Year.
- This function cannot be used if model **Calendar Type** is **Weeks: General**.

The example below shows YEARTODATE applied to sales, in half year increments.

|  | **H1   FY18** | **H2   FY18** | **H1   FY19** | **H2   FY19** | **H1 FY20** | **H2 FY20** | **H1   FY21** | **H2   FY21** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *Sales* | 78,545 | 63,239 | 67,883 | 72,045 | 84,671 | 69,229 | 76,532 | 67,807 |
| `YEARTODATE`   `(Sales)` | 78,545 | 141,784 | 67,883 | 139,928 | 84,671 | 153,900 | 76,532 | 144,339 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fyeartodate-5b08fc8e-0fed-47e1-b5dc-f846a22e6431&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>