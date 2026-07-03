---
title: "MAX | Anapedia"
source: "https://help.anaplan.com/max-a8aca856-8681-44d4-bae8-776f4842bae3"
author:
published:
created: 2026-05-02
description: "The MAX function returns the maximum from a set of values. For a number, it returns the maximum value. For a date, it returns the latest date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The MAX function returns the maximum from a set of values. For a number, it returns the maximum value. For a date, it returns the latest date.

For example, you can use the MAX function to force negative numbers to be zero without affecting positive numbers.

`MAX(Value to compare, Value to compare 2, [etc.])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to compare* (required) | Number, date | The values to search for the maximum value. Returns the highest number or most recent date.  All values must be of the same data type.  This argument can be repeated to provide multiple values for comparison. It must be provided a minimum of two times. |

The MAX function returns a result of the same data type as the *Value to compare* arguments.

`MAX(P1, 100, P2 / 2)`

This example returns the highest value out of:

- The P1 line item
- The number 100
- The P2 line item divided by two

[MAX](https://support.microsoft.com/en-us/office/max-function-e0012414-9ac8-4b34-9a47-73e662c08098)

In this example, the MAX function is used to return only positive values from the *Adjustment values* line item. This is done by using the number 0 and the *Adjustment values* line item with the MAX function.

The module also uses the MIN function to return only negative values.

|  | **Jan 22** | **Feb 22** | **Mar 22** | **Apr 22** | **May 22** | **Jun 22** |
| --- | --- | --- | --- | --- | --- | --- |
| Adjustment values | \-1,230 | 2,637 | 1,829 | \-3,109 | 2,019 | 320 |
| Positive Adjustment values only  `MAX(Adjustment values, 0)` | 0 | 2,637 | 1,829 | 0 | 2,019 | 320 |
| Negative Adjustment values only  `MIN(Adjustment values, 0)` | \-1,230 | 0 | 0 | \-3,109 | 0 | 0 |

In this example, a module is dimensioned by *Time* and line items. The first five line items contain the monthly salary costs for different departments. The final line item contains a formula that determines which department incurs the highest salary cost each month.

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Sales | 124,254 | 112,469 | 132,525 |
| Production | 64,631 | 66,298 | 72,049 |
| Executive | 175,302 | 169,030 | 190,298 |
| Finance | 97,210 | 97,210 | 102,051 |
| HR | 71,035 | 71,035 | 71,035 |
| Highest monthly departmental salary costs  `MAX(Sales, Production, Executive, Finance, HR)` | 175,302 | 169,030 | 190,298 |

In this example, a module is dimensioned by the *Products* list and line items. The first four line items contain product release dates for different regions, which have the date data type. The final line item contains a formula that determines the most recent product release for each product among each region.

|  | **Monet dress** | **Renoir dress** | **Picasso top** | **Cezanne sweatpants** | **Matisse pumps** |
| --- | --- | --- | --- | --- | --- |
| N America | 01/04/2021 | 01/04/2021 | 12/07/2021 | 12/07/2021 | 21/07/2021 |
| S America | 07/05/2021 | 23/05/2021 | 19/07/2021 | 19/07/2021 | 21/07/2021 |
| Europe | 27/03/2021 | 27/03/2021 | 12/03/2021 | 12/07/2021 | 28/07/2021 |
| Asia Pacific | 12/06/2021 | 12/06/2021 | 12/06/2021 | 12/07/2021 | 28/07/2021 |
| Most recent global release date  `MAX(N America, S America, Europe, ASia Pacific)` | 12/06/2021 | 12/06/2021 | 19/07/2021 | 19/07/2021 | 28/07/2021 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmax-a8aca856-8681-44d4-bae8-776f4842bae3&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>