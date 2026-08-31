---
title: "YEAR | Anapedia"
source: "https://help.anaplan.com/year-d5b458d3-b0f7-4b70-a28a-342ea85f8416"
author:
published:
created: 2026-05-02
description: "The function YEAR converts a date or time period to a year in number format."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

This function is useful if you want to easily compare years to see if they're the same.

`YEAR(Value to convert, [Time period method]) `

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to convert* | Date, Time period | The date or time period to convert to a year, as a number. |
| *Time period method* (optional) | Keyword | Determines whether to extract the year from the start, middle, or end of a time period. |

The keywords for the *time period method* argument are:

- START, the default method, returns the year for the first date in the time period
- MID, which returns the year for the date in the middle of the time period
- END,whichreturns the year for the last date in the time period

The YEAR function returns a number.

- [YEAR](https://support.office.com/en-gb/article/YEAR-function-c64f017a-1354-490d-981f-578e8ec8d3b9)

In this example, the line item *Date* is in **Date** format. The line item *Number* returns the **Number** format of the year using the formula `YEAR(Date)`.

|  | **Jan 25** | **Feb 25** | **Mar 25** | **Apr 25** | **May 25** |
| --- | --- | --- | --- | --- | --- |
| Date | 01/01/2025 | 02/02/2025 | 03/03/2025 | 04/04/2025 | 05/05/2025 |
| Number   `YEAR(Date)` | 2,025 | 2,025 | 2,025 | 2,025 | 2,025 |

In this example, the target module is dimensioned by a list with a property called *Months*. This is the *List* as viewed in **Grid View**.

|  | **Parent** | **Code** | **Months** |
| --- | --- | --- | --- |
| 1 |  |  | Dec 21 |
| 2 |  |  | Jan 21 |
| 3 |  |  | Sep 22 |
| 4 |  |  | Jul 24 |
| 5 |  |  | Dec 23 |

The line item *Input* is in **Time Period** format in **Month**, and it has the formula `List.Months` to return the *Months* list items from the list. The line item *Number* returns the **Number** format of the year using the formula `YEAR(Input)`.

|  | **1** | **2** | **3** | **4** | **5** |
| --- | --- | --- | --- | --- | --- |
| Input   `List.Months` | Dec 25 | Jan 21 | Sep 22 | Jul 24 | Dec 23 |
| Number   `YEAR(Input)` | 2,025 | 2,021 | 2,022 | 2,024 | 2,023 |

The example below shows `YEAR(Value to convert)`. The values to convert are taken from the *Product date* and *Year period* line items. These are date and time period formatted, respectively.

|  | **Key dates** | **Expiry dates** |
| --- | --- | --- |
| Product released | 16/02/2016 | 23/08/2017 |
| Year period | Feb 16 | Aug 17 |
| Product year  `YEAR(Product released)` | 2,016 | 2,017 |
| Year number  `YEAR(Year period)` | 2,016 | 2,017 |

The next example shows `YEAR(TIME. 'Period').` An explicit time reference is used instead of a line item.

|  | **Key dates** |
| --- | --- |
| Year Number  `YEAR(TIME. 'Apr 16')` | 2,016 |

The final example shows the effect of the *Time period method* argument. An explicit time reference is used with a keyword to determine which date in a time period to extract the year from.

|  | **Product: Plums** |
| --- | --- |
| Start of fiscal year | Week 1 FY2019 |
| Year Start  `YEAR(Start of fiscal year, START)` | 2,018 |
| Year Mid  `YEAR(TIME. 'FY19', MID)` | 2,019 |
| Year End  `YEAR(Start of fiscal year, END)` | 2,019 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fyear-d5b458d3-b0f7-4b70-a28a-342ea85f8416&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>