---
title: "WEEKTODATE | Anapedia"
source: "https://help.anaplan.com/weektodate-d8130eef-376b-4325-976e-c4833a36a5d3"
author:
published:
created: 2026-05-02
description: "WEEKTODATE aggregates the daily values within a week from a single numeric parameter. WEEKTODATE resets after the last day of the week."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

WEEKTODATE aggregates the daily values within a week from a single numeric parameter. WEEKTODATE resets after the last day of the week.

You could use WEEKTODATE to compare orders received this week with the orders from previous weeks, up to and including the same day of the week. WEEKTODATE resets at each weekly interval.

`WEEKTODATE(Line item to aggregate)`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *Line item to*   *aggregate* | Number or numeric line item. | The line item to aggregate in a weekly timeframe. |

The WEEKTODATE function returns a number-formatted result.

In Polaris, you can use the WEEKTODATE function with line items with a time scale of **Week**. In the Classic Engine, you cannot.

In Polaris, you cannot use WEEKTODATE in formulas of line items with a formula summary method. In the Classic Engine, you can.

`WEEKTODATE(Sales)`

WEEKTODATE below is used to show cumulative sales.

|  | **02-Feb-21** | **03-Feb-21** | **04-Feb-21** | **05-Feb-21** | **06-Feb-21** | **07-Feb-21** | **08-Feb-21** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *Unit costs* | 130 | 155 | 125 | 142 | 137 | 151 | 122 |
| *Packaging* | 30 | 40 | 26 | 38 | 41 | 33 | 39 |
| *Sales* | 110 | 53 | 37 | 72 | 67 | 93 | 102 |
| `WEEKTODATE`   `(Sales)` | 110 | 163 | 200 | 272 | 339 | 432 | 534 |

- The source **Time Scale** must be *Day*.
- WEEKTODATE cannot be used if **Calendar Type** is *Months/Quarters/Years*.

In the following example, WEEKTODATE is used to aggregate revenue for each day of the week.

|  | **28 Mar 21** | **29 Mar 21** | **30 Mar 21** | **31 Mar 21** | **1 Apr 21** | **2 Apr 21** | **3 Apr 21** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *Revenue* | 32,500 | 30,800 | 29,050 | 27,500 | 31,250 | 33,400 | 32,750 |
| `WEEKTODATE(Revenue)` | 32,500 | 63,300 | 92,350 | 119,850 | 151,100 | 184,500 | 217,250 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fweektodate-d8130eef-376b-4325-976e-c4833a36a5d3&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>