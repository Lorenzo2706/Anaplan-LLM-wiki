---
title: "LAG | Anapedia"
source: "https://help.anaplan.com/lag-3064919f-964e-4b84-be56-15f0e127e371"
author:
published:
created: 2026-05-02
description: "LAG returns a value from a preceding position within the specified dimension."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

You could use LAG to calculate how this month's earnings compare to last year's monthly earnings.

`LAG(Value to offset, Offset amount, Substitute value [, Non-positive behavior, List])`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *Value to offset* | Number, Boolean, date,   time period, list, or text | Value to replace with a value from a different time period.  See the **Calculation engine functionality differences** section for the use of a non-numeric argument in the Classic engine. |
| *Offset amount* | Number | Number of periods in the past from which to retrieve a value.  Positive values refer to past periods, negative to future ones, and zero the current period. |
| *Substitute value* | Same as *Value to offset* | Value to apply if the *Offset amount* specifies a period outside of the model's time range.  Also used for non-positive offsets if you use the SEMISTRICT or STRICT keywords for the *Non-positive behavior* argument. |
| *Non-positive behavior* (optional) | Keyword | Determines how the LAG function uses the *Substitute value* argument. |
| *List* (Polaris only) | List | The list over which the function should operate. The target line item must be dimensioned with any dimension compatible with this list.  You must provide a *Non-positive behavior* keyword to use LAG on a list.  See **Calculation engine functionality differences**. |

The LAG function returns a result of the same data type as the *Value to offset* argument.

This function allows for three arguments. If you have these functions with two arguments and don't declare a third one, this will default to Time. If you declare a third argument, then you can use any related dimension to the line item as an argument.

| **Keyword** | **Description** |
| --- | --- |
| NONSTRICT | The default keyword if you omit the *Non-positive behavior* argument.  Returns the *Value to offset* if the *Offset amount* is positive, negative, or zero. |
| SEMISTRICT | Returns the *Value to offset* if the *Offset amount* is positive or zero. |
| STRICT | Returns the *Value to offset* if the *Offset amount* is positive. |

In Polaris:

- Any number used for the *Offset amount* argument is rounded to the nearest integer. A value of *NaN* (Not a Number) for the *Offset amount* argument returns the *Substitute value* argument.
- You can use LAG with any dimension except Versions. In the Classic Engine, you can use this function only with a time dimension.

In the Classic Engine:

- You can use non-numeric *Value to offset* arguments, but only when the *Offset amount* is a constant. Otherwise, an error message displays.
- Any number used for the *Offset amount* argument is rounded toward zero. A value of *NaN* is equivalent to 0.

`LAG(Value to offset, 2, 0)`

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 3,000 | 1,000 | 2,000 | 7,000 | 2,500 | 3,000 |
| **LAG 1** | 0 | 0 | 3,000 | 1,000 | 2,000 | 7,000 |

In this example, the *LAG 1* line item contains the formula above. This means it returns the value from two periods before.

Since for *Jan* and *Feb*, two periods before the cells are outside of the module’s time range, the formula returns the *Substitute value* of 0. The function does not contain the *Non-positive behavior* argument, so the default behavior is *NONSTRICT*.

If the period LAG specifies is outside of the module's time range, LAG returns the value of the *substitute value* argument.

In this example, the *Lag by two periods* line item contains a formula that returns the *Value to offset* from two periods prior.

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 3,000 | 1,000 | 2,000 | 7,000 | 2,500 | 3,000 |
| **Substitute value** | 10 | 1 | 6 | 1 | 2 | 5 |
| **Lag by two periods   **`LAG(Value to offset, 2, Substitute value)` | 10 | 1 | 3,000 | 1,000 | 2,000 | 7,000 |

When the *Offset amount* specifies a period thatfalls outside the time range, *LAG* returns the *Substitute value* amount, as shown in *Jan* and *Feb* columns.

The formula does not contain the *Non-positive behavior* argument, so it uses the default behavior, *NONSTRICT*.

In this example, the *LAG with constant offset* line item contains the formula above. This means it returns line item from two periods before each cell.

If the *Substitute value* amount falls outside the model time range, the value from the *Value to offset* row in the current period is used, as shown in **Jan** and **Feb** columns. The formula does not contain the *Non-positive behavior* argument, so it uses the default behavior, *NONSTRICT*.

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 3,000 | 1,000 | 2,000 | 7,000 | 2,500 | 3,000 |
| **Substitute value** | 10 | 1 | 6 | 1 | 2 | 5 |
| **LAG with constant offset   **`LAG(Value to offset, 2, Substitute value)` | 10 | 1 | 3,000 | 1,000 | 2,000 | 7,000 |

In this example, you can see how the different keywords for the *Non-positive behavior* argument change the results.

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 1 | 2 | 3 | 4 | 5 | 6 |
| **Offset amount** | 0 | \-1 | 0 | 1 | 0 | 1 |
| **Substitute value** | 100 | 200 | 300 | 400 | 500 | 600 |
| **Semistrict behavior   **`LAG(Value to offset, Offset amount, Substitute value, SEMISTRICT)` | 1 | 200 | 3 | 3 | 5 | 5 |
| **Strict behavior   **`LAG(Value to offset, Offset amount, Substitute value, STRICT)` | 100 | 200 | 300 | 3 | 500 | 5 |
| **Nonstrict behavior   **`LAG(Value to offset, Offset amount, Substitute value, NONSTRICT)` | 1 | 3 | 3 | 3 | 5 | 5 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Flag-3064919f-964e-4b84-be56-15f0e127e371&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>