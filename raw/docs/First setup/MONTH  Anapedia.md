---
title: "MONTH | Anapedia"
source: "https://help.anaplan.com/month-38d3ce37-2f9e-4a16-8324-f3ba10c11808"
author:
published:
created: 2026-05-02
description: "The function MONTH converts a date or time period to a month in number format."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

This function is useful if you want to easily compare months to see if they're the same.

`MONTH(Value to convert, [Time period method]) `

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Value to convert | Date, time period | The date or time period to convert to a month, as a number. |
| Time period method (optional) | Keyword | Determines whether to extract the month from the start, middle, or end of a time period. |

The keywords for the *time period method* argument are:

- START, the default method, returns the month for the first date in the time period
- MID, which returns the month for the date in the middle of the time period
- END,whichreturns the month for the last date in the time period

The MONTH function returns a number.

[MONTH](https://support.office.com/en-gb/article/MONTH-function-579a2881-199b-48b2-ab90-ddba0eba86e8)

In this example, the line item *Date* is in **Date** format. The line item *Number* returns the **Number** format of the month using the formula `MONTH(Date)`.

|  | **Jan 25** | **Feb 25** | **Mar 25** | **Apr 25** | **May 25** |
| --- | --- | --- | --- | --- | --- |
| Date | 01/01/2025 | 02/02/2025 | 03/03/2025 | 04/04/2025 | 05/05/2025 |
| Number   `MONTH(Date)` | 1 | 2 | 3 | 4 | 5 |

In this example, the target module is dimensioned by a list with a property called *Months*. This is the *List* as viewed in **Grid View**.

|  | **Parent** | **Code** | **Months** |
| --- | --- | --- | --- |
| 1 |  |  | Dec 21 |
| 2 |  |  | Jan 21 |
| 3 |  |  | Sep 22 |
| 4 |  |  | Jul 24 |
| 5 |  |  | Dec 23 |

The line item *Input* is in **Time Period** format in **Month**, and it has the formula `List.Months` to return the *Months* list items from the list. The line item *Number* returns the **Number** format of the month using the formula `MONTH(Input)`.

|  | **1** | **2** | **3** | **4** | **5** |
| --- | --- | --- | --- | --- | --- |
| Input   `List.Months` | Dec 25 | Jan 21 | Sep 22 | Jul 24 | Dec 23 |
| Number   `MONTH(Input)` | 12 | 1 | 9 | 7 | 12 |

The example below shows `MONTH(Value to convert)`. The values to convert are taken from the *Product date* and *Month period* line items. They're date and time period formatted, respectively. The MONTH function returns the same result.

|  | **Key dates** | **Expiry dates** |
| --- | --- | --- |
| Product released | 16/02/2016 | 23/08/2017 |
| Month period | Feb 16 | Aug 17 |
| Product month  `MONTH(Product released)` | 2 | 8 |
| Month number  `MONTH(Month period)` | 2 | 8 |

The next example shows `MONTH(TIME. 'Period').` An explicit time reference is used instead of a line item.

|  | **Key dates** |
| --- | --- |
| Year Number  `MONTH(TIME. 'Apr 16')` | 4 |

The final example shows the effect of the *Time period method* argument. An explicit time reference is used with a keyword to determine which date in a time period to extract the month from.

|  | **Product: Plums** |
| --- | --- |
| Start of fiscal year | Jan FY2019 |
| Month Start  `MONTH(Start of fiscal year, START)` | 1 |
| Month Mid  `MONTH(TIME. 'Q1 FY19', MID)` | 2 |
| Month End  `MONTH(TIME. 'Q1 FY19', END)` | 3 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmonth-38d3ce37-2f9e-4a16-8324-f3ba10c11808&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>