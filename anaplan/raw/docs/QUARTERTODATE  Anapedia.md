---
title: "QUARTERTODATE | Anapedia"
source: "https://help.anaplan.com/quartertodate-156ac565-ac4a-48a0-980b-6c0c04781a95"
author:
published:
created: 2026-05-02
description: "QUARTERTODATE accumulates values from a single numeric parameter, within a quarterly time range."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

You could use QUARTERTODATE to compare orders received this quarter with the orders from previous quarters, up to and including the same day. QUARTERTODATE resets at each quarterly interval.

`QUARTERTODATE(Line item to aggregate)`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *Line item to*   *aggregate* | Number | The line item to aggregate in a quarterly timeframe. |

The QUARTERTODATE function returns a number.

In Polaris, you can use the QUARTERTODATE function with line items with a time scale of **Quarter**. In the Classic Engine, you cannot.

In Polaris, you cannot use QUARTERTODATE in formulas of line items with a formula summary method. In the Classic Engine, you can.

`QUARTERTODATE(Sales)`

In the example below QUARTERTODATE cumulatessales for each quarter.

|  | **Jan   2021** | **Feb   2021** | **Mar   2021** | **Apr   2021** | **May   2021** | **Jun   2021** |
| --- | --- | --- | --- | --- | --- | --- |
| Sales | 88,425 | 92,680 | 91,368 | 86,328 | 97,763 | 94328 |
| `QUARTERTODATE`   `(Sales)` | 88,425 | 181,105 | 272,473 | 86,328 | 184,091 | 278,419 |

The line item that contains the QUARTERTODATE function must have a Time Scale of Day, Week, or Month.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fquartertodate-156ac565-ac4a-48a0-980b-6c0c04781a95&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>