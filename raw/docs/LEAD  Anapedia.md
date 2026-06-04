---
title: "LEAD | Anapedia"
source: "https://help.anaplan.com/lead-e3f4969b-65b1-4726-b41c-d028c9c71c14"
author:
published:
created: 2026-05-02
description: "LEAD returns a subsequent position within the specified dimension."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

You could use LEAD to calculate how this month's earnings compare to next year's projected monthly earnings.

`LEAD(Value to offset, Offset amount, Substitute value [, Non-positive behavior, List])`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *Value to offset* | Number, Boolean, date,   time period, list, or text | The value to replace with a value from a different time period.  See the **Calculation engine functionality differences** section for the use of a non-numeric argument in the Classic engine. |
| *Offset amount* | Number | Number of periods forward from which to retrieve a value.  Positive values refer to future periods, negative to past periods, and zero to the current period. |
| *Substitute value* | Same as *Value to offset* | Value to return if the *Offset amount* specifies a period outside of the model's time range.  Also used for non-positive offsets if you use the SEMISTRICT or STRICT keywords for the *Non-positive behavior* argument. |
| *Non-positive behavior* (optional) | Keyword | Determines how the LEAD function uses the *Substitute value* argument.  The keywords are NONSTRICT, SEMISTRICT, and STRICT. There's more information in the **Non-positive behavior keywords** section below. |
| *List* (Polaris only) | List | The list over which the function should operate. The target line item must be dimensioned with any dimension compatible with this list.  You must provide a *Non-positive behavior* keyword to use LEAD on a list.  See **Calculation engine functionality differences**. |

You must provide the arguments in the given order. The LEAD function returns a result of the same data type as the *Value to offset* argument.

This function allows for three arguments. If you have these functions with two arguments and don't declare a third one, this will default to Time. If you declare a third argument, then you can use any related dimension to the line item as an argument.

| **Keyword** | **Description** |
| --- | --- |
| NONSTRICT | The default keyword if you omit the *Non-positive behavior* argument.  Returns the *Value to offset* if the *Offset amount* is positive, negative, or zero. |
| SEMISTRICT | Returns the *Value to offset* if the *Offset amount* is positive or zero. |
| STRICT | Returns the *Value to offset* if the *Offset amount* is positive.  In STRICT mode, LEAD applies to the future, and not to current periods. The fill value is returned if either shift < 0 or the future period is beyond model time range. |

In Polaris:

- Any number used for the *Offset amount* argument is rounded to the nearest integer. A value of *NaN* (Not a Number) for the *Offset amount* argument returns the *Substitute value* argument.
- You can use LEAD with any dimension except Versions. In the Classic Engine, you can use this function only with a time dimension.

In the Classic Engine:

- You can use non-numeric *Value to offset* arguments, but only when the *Offset amount* is a constant. Otherwise, an error message displays.
- Any number used for the *Offset amount* argument is rounded towards zero. A value of *NaN* is equivalent to 0.

`LEAD(Value to offset, 2, 0)`

In this example, the *LEAD 1* line item returns the value from two periods after each cell. If two periods after a cell is outside of the module’s time range, the formula returns the *Substitute value* of 0, as seen in the *June* column. The function does not contain the *Non-positive behavior* argument, so the default behavior is *NONSTRICT*.

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 1 | 2 | 3 | 4 | 5 | 6 |
| **LEAD 1** | 3 | 4 | 5 | 6 | 0 | 0 |

If the period LEAD specifies is outside of the module's timescale, LEAD returns the value of the S *ubstitute value* argument.

`LEAD(Value to offset, 2, Substitute value)`

In this example, the *LEAD 2* line item returns line item from two periods after each cell. If two periods after a cell is outside of the module’s time range, the formula returns the *Substitute value*. The formula returns the values of 500 and 600 contained in the *May* and *June* columns for the *Substitute value*. The function does not contain the *Non-positive behavior* argument, so the default behavior is *NONSTRICT*.

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 1 | 2 | 3 | 4 | 5 | 6 |
| **Substitute value** | 100 | 200 | 300 | 400 | 500 | 600 |
| **LEAD 2** | 3 | 4 | 5 | 6 | 500 | 600 |

`LEAD(Value to offset, Offset amount, Substitute value, [non-positive behavior])   ` In this example, the *LEAD 3* line item returns the *Substitute value* for the period the *Offset amount* specifies. If the *Substitute value* specifies a period outside of the module's time range, the formula returns the *Substitute value*. This means the formula returns the value of 600 contained in the *June* column for the *Substitute value*. The function doesn't contain the *Non-positive behavior* argument, so the default behavior is *NONSTRICT*.

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 1 | 2 | 3 | 4 | 5 | 6 |
| **Offset amount** | 0 | \-1 | 0 | 1 | 0 | 1 |
| **Substitute value** | 100 | 200 | 300 | 400 | 500 | 600 |
| **LEAD 3** | 1 | 1 | 3 | 5 | 5 | 600 |

`LEAD(Value to offset, Offset amount, Substitute value, [, Non-positive behavior])`

In this example, you can see how the different keywords for the *Non-positive behavior* change the results.

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to offset** | 1 | 2 | 3 | 4 | 5 | 6 |
| **Offset amount** | 0 | \-1 | 0 | 1 | 0 | 1 |
| **Substitute value** | 100 | 200 | 300 | 400 | 500 | 600 |
| **LEAD   **`SEMISTRICT` | 1 | 200 | 3 | 5 | 5 | 600 |
| **LEAD   **`STRICT` | 100 | 200 | 300 | 5 | 500 | 600 |
| **LEAD   **`NONSTRICT` | 1 | 1 | 3 | 5 | 5 | 600 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Flead-e3f4969b-65b1-4726-b41c-d028c9c71c14&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>