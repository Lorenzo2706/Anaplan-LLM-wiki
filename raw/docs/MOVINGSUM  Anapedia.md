---
title: "MOVINGSUM | Anapedia"
source: "https://help.anaplan.com/movingsum-37394929-ea62-4e55-9655-b8c8c2732679"
author:
published:
created: 2026-05-02
description: "The MOVINGSUM function returns the sum of values over a changing time range. As the time range moves through the data, it aggregates the values for the updated time range."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The `MOVINGSUM` function returns the sum of values over a changing time range. As the time range moves through the data, it aggregates the values for the updated time range.

Use this function to create rolling summaries or forecasts based on a series of data, such as weekly sales or performance results.

`MOVINGSUM(Line item to aggregate [, Start offset] [, End offset] [, Aggregation method] [, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Line item to aggregate* (required) | Number, boolean, date, list, or text | The line item containing the values that you want to aggregate over a period of time.  This argument must be a line item. |
| *Start offset* | Number | The starting value for the aggregation.  When you omit *Start offset*, the aggregation is performed over the entire time range. |
| *End offset* | Number | The ending value for the aggregation. |
| *Aggregation method* | Keyword | The aggregation method to use.  The available keywords are `SUM`, `AVERAGE`, `MIN`, `MAX`, `ANY`, `ALL`, `FIRSTNONBLANK`, `LASTNONBLANK`, and `TEXTLIST`.  There's more information in the **Aggregation method** section below. |
| *List* | List | The list over which the function should operate.  When you omit *List*, the aggregation is performed over the time dimension.  See ***Calculation engine functionality differences****.* |

The `MOVINGSUM` function returns a value that matches the data type of the *Line item to aggregate*.

| **Keyword** | **Data type** | **Purpose** |
| --- | --- | --- |
| `SUM` | Number | Adds the input values |
| `AVERAGE` | Number | Calculates the average of the input values |
| `MIN` | Number, date, time period | Identifies the minimum input value |
| `MAX` | Number, date, time period | Identifies the maximum input value |
| `ANY` | Boolean | Checks and returns `TRUE` if any input value is `TRUE` |
| `ALL` | Boolean | Checks and returns `TRUE` if all input values are `TRUE` |
| `FIRSTNONBLANK` | Date, list, text, time period | Returns the first non-blank input value |
| `LASTNONBLANK` | Date, list, text, time period | Returns the last non-blank input value |
| `TEXTLIST` | Text | Concatenates the input values with a ", " separator to create a single text value |

When you omit the *Aggregation method*, the default behavior depends on the data type of the *Line item to aggregate*:

- If the data type of the *Line item to aggregate* is a number, the default method is `SUM`.
- If the data type of the *Line item to aggregate* is boolean, the default method is `ANY`.
- If the data type of the *Line item to aggregate* is a date, list, or text, the default method is `FIRSTNONBLANK`.

| **Behavior** | **Polaris** | **Classic** |
| --- | --- | --- |
| Two-argument variant | `MOVINGSUM(source, start)` aggregates the *source* values from the point corresponding to the *Start* *offset* to the end of the time dimension. | `MOVINGSUM` returns the value of the *source* at the point corresponding to the *Start* *offset*. |
| Blank values in *End offset* | Aggregates the *source* values from the point corresponding to the *Start offset* to the end of the time range, for example, 12 if the source is dimensioned by months. | *End offset* defaults to the value as the *Start offset*, for example, `MOVINSUM(source, 4)` is considered as `MOVINGSUM(source, 4, 4)`. |
| Reference across time ranges | Can reference different time ranges. For example, `MOVINGSUM` can reference a *Line item to aggregate* with a time dimension based on a different time range than the time dimension of the target line item. | Can't reference different time ranges. |
| Reference across timescales | Can't refer to a source line item with a time dimension at a coarser timescale than the time dimension of the target. | Always possible to refer to a source line item with a coarser time dimension. |
| NaN handling in arguments | When either the *Start offset* or *End* *offset* argument is NaN, `MOVINGSUM` returns the default value for the type of *Line item to aggregate*. | ‌NaN in either argument is treated as the offset corresponding to the earliest period in the time dimension. |
| Empty aggregation behavior | When there are no values to aggregate, that is when the *Start offset* is greater than the *End offset*, `MOVINGSUM` returns the default value for the type of *Line item to aggregate*.   The default values include 0 for numbers, False for Boolean, and blank for other data types. | Returns value depending on the combination of the aggregation method used and its data type. |
| Blank handling in MIN aggregation method on dates | When comparing a blank with a non-blank date value, `MIN` ignores the blank and returns the non-blank value. When all values are blank, it returns blank. | When blank is compared with a non-blank date value, it returns blank. |
| Unavailable aggregation methods | Among the aggregation methods listed in the **Aggregation method** section, `FIRSTNONBLANK`, `LASTNONBLANK`, and `TEXTLIST` aren't available in Polaris. | All aggregation methods listed in the **Aggregation method** section are available. |
| Operation over hierarchies | Can use the `MOVINGSUM` function over any dimension, by including the additional argument, *List*. | Can't use the *List* argument. Where, if the additional argument isn't included, the function defaults to Time as the dimension. |

`MOVINGSUM(Bonus, -2, 0)`

|  | **Jan 22** | **Feb 22** | **Mar 22** | **Apr 22** | **May 22** | **Jun 22** | **Jul 22** | **Aug 22** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bonus | 6,150 | 5,850 | 5,900 | 6,025 | 4,850 | 4,950 | 5,600 | 6,250 |
| `MOVINGSUM(Bonus, -2, 0)` | 6,150 | 12,000 | 17,900 | 17,775 | 16,775 | 15,825 | 15,400 | 16,800 |

In `MOVINGSUM(source, -1, 0)`, for example, if the *Start offset* (-1) or *End offset* (0) leads to values outside the time range of the *Line item to aggregate*, values outside the range are ignored in the aggregation.

If you use a decimal number for the *Start offset* or *End offset*, `MOVINGSUM` rounds it to the nearest value.

|  | **Jan 23** | **Feb 23** | **Mar 23** | **Apr 23** | **May 23** | **Jun 23** | **Jul 23** | **Aug 23** | **Sep 23** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number | 200 | 250 | 300 | 500 | 400 | 450 | 200 | 400 | 350 |
| `MOVINGSUM(Number, -2, 0, AVERAGE)` | 200 | 225 | 250 | 350 | 400 | 450 | 350 | 350 | 316.7 |
| `MOVINGSUM(Number, 1, 3, MAX)` | 500 | 500 | 500 | 450 | 450 | 400 | 400 | 350 | 0 |
| `MOVINGSUM(Number, -4, 2, SUM)` | 750 | 1,250 | 1,650 | 2,100 | 2,300 | 2,500 | 2,600 | 2,300 | 1,800 |
| Boolean |  |  |  |  |  |  |  |  |  |
| `MOVINGSUM(Boolean, -1, 0, ANY)` |  |  |  |  |  |  |  |  |  |
| `IF MOVINGSUM(Boolean, -1, 0, ALL) THEN 1 ELSE 0` | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| Date | 02/01/2023 | 06/02/2023 | 16/03/2023 | 20/04/2023 | 19/05/2023 | 23/06/2023 | 21/07/2023 | 30/08/2023 | 14/09/2023 |
| `MOVINGSUM(Date, -1, 0, MAX)` | 06/02/2023 | 16/03/2023 | 20/04/2023 | 19/05/2023 | 23/06/2023 | 21/07/2023 | 30/08/2023 | 14/09/2023 | 14/09/2023 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmovingsum-37394929-ea62-4e55-9655-b8c8c2732679&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>