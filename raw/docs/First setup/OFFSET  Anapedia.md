---
title: "OFFSET | Anapedia"
source: "https://help.anaplan.com/offset-4f5a095c-0e7a-4f1a-b6ea-0ef8f88d6c3f"
author:
published:
created: 2026-05-02
description: "The OFFSET function returns a value from a selected dimension, either preceding or following the current value in that dimension."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The OFFSET function returns a value from a selected dimension, either preceding or following the current value in that dimension.

Use this function to compare salary data across hierarchical employee levels, analyze salary progression, simulate promotions/demotions, or benchmark pay gaps

`OFFSET(Value to offset, Offset amount, Substitute value [, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to offset* | Number, Boolean, date,   time period, list, or text | Reference value from which you want to offset or retrieve data, for example, current sales. |
| *Offset amount* | Number | Number of periods to move from the current reference value:  - Positive values move forward in time, to future periods. - Negative values move backward in time, to past periods. - Zero stays in the current period. |
| *Substitute value* | Same as *Value to offset* | Value to return if the *Offset amount* specifies a period outside or beyond the model's time range. |
| *List* (Polaris only) | List | The list over which the function should operate. The target line item must be dimensioned with any dimension compatible with this list.  See **Calculation engine functionality differences**. |

The OFFSET function returns a value of the same data type as the *Value to offset* argument.

This function allows for three arguments. If you have these functions with two arguments and don't declare a third one, this will default to Time. If you declare a third argument, then you can use any related dimension to the line item as an argument.

- In Polaris, a value of *NaN* (Not a Number) for the *Offset amount* argument returns the *Substitute value* argument. ‌In the Classic Engine, a value of *NaN* is equivalent to 0.
- In Polaris, you can use OFFSET with any dimension except Versions. In the Classic Engine, you can use this function only with a time dimension.

`OFFSET(Base salary, Offset amount, 0, Employee levels)`

OFFSET is the same as LEAD in the NONSTRICT mode.

[OFFSET](https://support.office.com/en-gb/article/OFFSET-function-c8de19ae-dd79-4b9b-a14e-b4d906d11b66)

|  | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** |
| --- | --- | --- | --- | --- | --- | --- |
| **Fruits** | Apple | Peach | Banana | Pear | Fig | Melon |
| **Veg** | Carrot | Tomato | Cucumber | Onion | Lettuce | Broccoli |
| `OFFSET(Fruits, -1, Veg)` | Carrot | Apple | Peach | Banana | Pear | Fig |
| `OFFSET(Fruits, 2, Veg)` | Banana | Pear | Fig | Melon | Lettuce | Broccoli |

|  | **FY16** | **FY17** | **FY18** | **FY19** | **FY20** |
| --- | --- | --- | --- | --- | --- |
| **Data** |  |  |  |  |  |
| `OFFSET(Data, 1, FALSE)` |  |  |  |  |  |

|  | **1** | **2** | **3** | **4** | **5** |
| --- | --- | --- | --- | --- | --- |
| **Base salary** | 30,000 | 45,000 | 65,000 | 85,000 | 110,000 |
| **Offset amount** | 1 | 1 | \-1 | \-2 | \-3 |
| **Result**  `OFFSET(Base salary, Offset amount, 0, Employee levels)` | 45,000 | 65,000 | 45,000 | 45,000 | 45,000 |

In this example, OFFSET uses the hierarchical level list to shift salary values. Positive *Offset amount* shifts forward while the negative shifts backward. If the offset goes out of ‌bounds, it returns 0, the *Substitute value.*

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Foffset-4f5a095c-0e7a-4f1a-b6ea-0ef8f88d6c3f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>