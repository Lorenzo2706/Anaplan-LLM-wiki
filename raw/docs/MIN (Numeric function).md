---
title: "MIN (Numeric function)"
source: "https://help.anaplan.com/min-numeric-function-7a6b8a74-1de5-4e58-a33b-5b35420fec9b"
author:
published:
created: 2026-05-02
description: "The MIN function returns the minimum from a set of values. For a number, it returns the minimum value. For a date, it returns the earliest date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The MIN function returns the minimum from a set of values. For a number, it returns the minimum value. For a date, it returns the earliest date.

For example, you could enter a numerical constant in the MIN function to apply a cap to a set of values.

`MIN(Value to compare, Value to compare 2, [etc.])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to compare* (required) | Number, date | The values to search for the minimum value. Returns the lowest number or earliest date.  All values must be of the same data type.  This argument can be repeated to provide multiple values for comparison. It must be provided a minimum of two times. |

The MIN function returns a result of the same data type as the *Value to compare* arguments. When there are no values to compare, the function returns 0 for numbers and BLANK for other data types.

In Polaris, when comparing a blank date value to a non-blank date value, the MIN function returns the non-blank value.

In the Classic Engine, when comparing a blank date value to a non-blank date value, the MIN function returns the blank value.

`MIN(P1, 100, P2 / 2)`

This formula would return the lowest value from between:

- The value of P1
- 100
- The value of P2 divided by two.

[MIN](https://support.microsoft.com/en-gb/office/min-function-61635d12-920f-4ce2-a70f-96f202dcc152)

In this example, a module has an *Employees* list on columns, and line items on rows. The first line item is *Sales*, which shows the amount of sales each employee generated. The next line item, S *ales bonus,* calculates each employee's bonus, which is 20% of sales, with a limit of $5,000.

|  | **Ludwig VB** | **Amadeus M** | **Clara S** | **Felix M** |
| --- | --- | --- | --- | --- |
| Sales | 60,000 | 22,500 | 73,000 | 17,500 |
| Sales bonus  `MIN((Sales * 0.2), 5000)` | 5,000 | 4,500 | 5,000 | 3,500 |

In this example, a module is dimensioned by *Time* and line items. The first five line items contain the monthly salary costs for different departments. The final line item contains a formula that determines which department incurs the lowest salary cost each month.

|  | **Jan 21** | **Feb 21** | **March 21** |
| --- | --- | --- | --- |
| Sales | 124,254 | 112,469 | 132,525 |
| Production | 64,631 | 66,298 | 72,049 |
| Executive | 175,302 | 169,030 | 190,298 |
| Finance | 97,210 | 97,210 | 102,051 |
| HR | 71,035 | 71,035 | 71,035 |
| Lowest departmental salary costs  `MIN(Sales, Production, Executive, Finance, HR)` | 64,631 | 66,298 | 71,035 |

In this example, a module is dimensioned by the *Products* list and line items. The first four line items contain product release dates for different regions, which have the date data type. The final line item contains a formula that determines the earliest product release for each product among each region.

|  | **Monet dress** | **Renoir dress** | **Picasso top** | **Cezanne sweatpants** | **Matisse pumps** |
| --- | --- | --- | --- | --- | --- |
| N America | 01/04/2021 | 01/04/2021 | 12/07/2021 |  | 21/07/2021 |
| S America | 07/05/2021 | 23/05/2021 | 19/07/2021 | 19/07/2021 | 21/07/2021 |
| Europe |  | 27/03/2021 | 12/03/2021 | 12/07/2021 | 28/07/2021 |
| Asia Pacific | 12/06/2021 | 12/06/2021 | 12/06/2021 | 12/07/2021 | 28/07/2021 |
| Earliest global release date  `MIN(N America, S America, Europe, ASia Pacific)` | 01/04/2021 | 27/03/2021 | 12/03/2021 | 12/07/2021 | 21/07/2021 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmin-numeric-function-7a6b8a74-1de5-4e58-a33b-5b35420fec9b&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>