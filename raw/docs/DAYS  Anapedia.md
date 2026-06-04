---
title: "DAYS | Anapedia"
source: "https://help.anaplan.com/days-fc064281-7c00-456f-821f-a94aebc35144"
author:
published:
created: 2026-05-02
description: "The DAYS function returns the number of days in a given time period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, use the DAYS function to find out how many days are in a quarter.

`DAYS([Period])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Period* (Optional) | Time period | The period for which to return the number of days. |

The DAYS function returns a numeric result.

You can omit the *Period* argument if the line item you use the DAYS function in is dimensioned by Time. In this case, the DAYS function returns the number of days in each time period of the Time dimension.

If you use the DAYS function in a line item that is not dimensioned by Time, you must provide the *Period* argument or the function returns an error.

|  | Number of days in month  `DAYS()` |
| --- | --- |
| **Jan 21** | 31 |
| **Feb 21** | 28 |
| **Mar 21** | 31 |
| **Q1 FY21** | 90 |
| **Apr 21** | 30 |
| **May 21** | 31 |
| **Jun 21** | 30 |
| **Q2 FY21** | 91 |
| **H1 FY21** | 181 |
| **Jul 21** | 31 |
| **Aug 21** | 31 |
| **Sep 21** | 30 |
| **Q3 FY21** | 92 |
| **Oct 21** | 31 |
| **Nov 21** | 30 |
| **Dec 21** | 31 |
| **Q4 FY21** | 92 |
| **H2 FY21** | 184 |
| **FY21** | 365 |

In this example, the module contains both the Time dimension and a single line item. The line item contains the DAYS function without an argument, so it returns the number of days for each applicable time period of the Time dimension. As the DAYS function returns a numeric result, the **Sum** [summary method](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) aggregates the number of days within each parent time period.

|  | **Product A Launch** | **Product B Launch** |
| --- | --- | --- |
| Month period | Feb 19 | Feb 20 |
| Quarter period | Q1 FY19 | Q1 FY20 |
| Year period | FY19 | FY20 |
| Days in month  `DAYS(Month period)` | 28 | 29 |
| Days in quarter  `DAYS(Quarter period)` | 90 | 91 |
| Days in year  `DAYS(Year period)` | 365 | 366 |

In this example, the module does not have time as a dimension. As such, the *Period* argument must be given to use the DAYS function.

A list that describes two different product launches displays on columns. Line items display on rows. The top three line items are time period format. The bottom three line items are number format, and contain formulas to calculate the number of days in the corresponding time periods.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fdays-fc064281-7c00-456f-821f-a94aebc35144&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>