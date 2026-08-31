---
title: "CUMULATE | Anapedia"
source: "https://help.anaplan.com/cumulate-1173a903-81bb-4838-a4d0-1c9f9c739aa3"
author:
published:
created: 2026-05-02
description: "The CUMULATE function calculates the sum of a given set of values either over a time period or across a specified list. By default, it calculates the sum over a time dimension. You can also include a Boolean line item to determine which values should be included in the accumulation."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The CUMULATE function calculates the sum of a given set of values either over a time period or across a specified list. By default, it calculates the sum over a time dimension. You can also include a Boolean line item to determine which values should be included in the accumulation.

Use the CUMULATE function to track progressive totals, such as cumulative sales across categories.

`CUMULATE (Values to add [, Boolean] [, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Values to add* (required) | Number | A numeric line item to cumulatively add the values of. |
| *Boolean* | Boolean | A Boolean line item that resets the cumulative total when `TRUE`. |
| *List* | List | *See* **Calculation engine functionality differences**. |

The CUMULATE function returns a number.

- In Polaris, you can't use CUMULATE in formulas of line items with a formula summary method. In the Classic Engine, you can.
- In Polaris, the *List* argument can be any list related to a dimension of the line item the formula is used on. In the Classic Engine, for example, if you specify a subset as the *List* argument, it runs over the entire list. However, in Polaris, the function applies only within the subset. If a different level of hierarchy is used, the argument aligns and matches with the corresponding level in the target's dimensional hierarchy.
- In Polaris, the order of a *List* argument follows the correct hierarchical ordering instead of the order of the list in **General lists**.

In Classic, if you provide the *List* argument, the order in which values are added follows the original order of the list in **General lists**, even if the list is reordered.

The time range used for the *Values to add* argument must match the time range for the result line item.

In the example below, CUMULATE is used to cumulate the numeric values of the *Sales* line item over Time in months.

|  | **Jan 12** | **Feb 12** | **Mar 12** | **Apr12** |
| --- | --- | --- | --- | --- |
| *Sales* | 88,753 | 87,450 | 88,945 | 86,523 |
| `CUMULATE(Sales)` | 88,753 | 176,203 | 265,148 | 351,671 |

The second example below uses a Boolean, *Reset Sales*, to reset the cumulative total for a specific month.

|  | **Jan 12** | **Feb 12** | **Mar 12** | **Apr 12** |
| --- | --- | --- | --- | --- |
| *Sales* | 88,753 | 87,450 | 88,945 | 86,523 |
| `CUMULATE(Sales, Reset Sales)` | 88,753 | 176,203 | 88,945 | 175,468 |
| *Reset Sales* |  |  |  |  |

The third example below uses the CUMULATE function to cumulate *Sales* over a list, *Sales Reps*. Boolean is set to FALSE as no reset condition is applied.

|  | **Edgar Harrington** | **Joe Tipple** | **Harry Boyde** | **Nicky Spinks** |
| --- | --- | --- | --- | --- |
| *Sales* | 88,753 | 87,450 | 88,945 | 86,523 |
| `CUMULATE(Sales, FALSE, Sales Reps)` | 88,753 | 176,203 | 265,148 | 351,671 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcumulate-1173a903-81bb-4838-a4d0-1c9f9c739aa3&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>