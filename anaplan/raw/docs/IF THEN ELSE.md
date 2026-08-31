---
title: "IF THEN ELSE"
source: "https://help.anaplan.com/if-then-else-9fb6586e-0219-4771-a660-4ebcc317efc0"
author:
published:
created: 2026-05-02
description: "Tests a Boolean argument and returns one of two results based on whether it is true or false."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Tests a Boolean argument and returns one of two results based on whether it is true or false.

For example, you can use the IF THEN ELSE function to ensure that calculations only apply to values that meet certain criteria.

`IF Boolean argument THEN Result 1 ELSE Result 2`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Boolean argument* | Boolean | The Boolean argument that determines whether the function returns *Result 1* or *Result 2*.  If TRUE, the function returns *Result 1*. If FALSE, the function returns *Result 2*. |
| *Result 1* | Number, Boolean, date, time period, list, text | The value to return if the *Boolean argument* resolves to TRUE.  Must be the same data type as *Result 2*. |
| *Result 2* | Number, Boolean, date, time period, list, text | The value to return if the *Boolean argument* resolves to FALSE.  Must be the same data type as *Result 1*. |

The IF THEN ELSE function returns a result of the same data type as the *Result 1* and *Result 2* arguments.

`IF Time Settings.'Current Version' THEN Revenue ELSE 0`

You can also use the syntax used for some other spreadsheet applications. For example:

`IF(a > b, x, y)`

This formula is equivalent to the formula below:

`IF a > b THEN x ELSE y`

If you use the IF THEN ELSE function in the [new modeling experience](https://help.anaplan.com/595248aa-2ecc-4b4d-9466-d65a9ff52498), each argument of the function is indented within the expanded [formula editor](https://help.anaplan.com/293fd5d3-7ad6-4c83-84f6-efd85981f265).

If you need to return a Boolean result based on certain criteria, it's not always necessary to use the IF THEN ELSE function. Instead you can use operators to create a statement and Anaplan returns a value of TRUE or FALSE based on the cell value. For example, you could use:

`a > b`

This formula is equivalent to the formula below:

`IF a > b THEN TRUE ELSE FALSE`

You can use IF THEN ELSE multiple times in a formula. However, try to avoid this where possible as such formulas can be difficult to maintain. If your formula requires 10 or more instances of IF THEN ELSE, consider using the LOOKUP function.

Both the Result 1 and Result 2 arguments must have the same data type. The target line item must also have the same data type.

[IF](https://support.office.com/en-gb/article/IF-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)

This example uses two modules. The first module, *Values module*, contains several line items that contain two values of each data type:

| Number 1 | 100 |
| --- | --- |
| Number 2 | 200 |
| Boolean 1 |  |
| Boolean 2 |  |
| Date 1 | 1/1/2021 |
| Date 2 | 2/2/2021 |
| Time period 1 | Jan 21 |
| Time period 2 | Feb 21 |
| List 1 | London |
| List 2 | Paris |
| Text 1 | Good |
| Text 2 | Bad |

The *Result 1* and *Result 2* arguments use the values above in the formulas in the second module below. The second module also contains a line item used for the *Boolean argument* of the IF THEN ELSE function.

|  | **Scenario 1** | **Scenario 2** |
| --- | --- | --- |
| Boolean argument |  |  |
| Number example  `IF Boolean argument THEN Values module.'Number 1' ELSE Values module.'Number 2'` | 100 | 200 |
| Boolean example  `IF Boolean argument THEN Values module.'Boolean 1' ELSE Values module.'Boolean 2'` |  |  |
| Date example  `IF Boolean argument THEN Values module.'Date 1' ELSE Values module.'Date 2'` | 1/1/2021 | 2/2/2021 |
| Time period example  `IF Boolean argument THEN Values module.'Time period 1' ELSE Values module.'Time period 2'` | Jan 21 | Feb 21 |
| List example  `IF Boolean argument THEN Values module.'List 1' ELSE Values module.'List 2'` | London | Paris |
| Text example  `IF Boolean argument THEN Values module.'Text 1' ELSE Values module.'Text 2'` | Good | Bad |

You can use [operators](https://help.anaplan.com/f1c2ec15-34af-4ebe-8114-530cf7c9f3bc) such as AND, NOT, or OR in the *Boolean argument* to create more detailed conditions for the IF THEN ELSE function.

|  | **Region A** | **Region B** | **Region C** |
| --- | --- | --- | --- |
| Value 1 | 1 | 10 | 10 |
| Value 2 | 10 | 1 | 10 |
| `IF 'Value 1' >= 10 AND 'Value 2' >= 10 THEN "A" ELSE "B"` | B | B | A |
| `IF 'Value 1' >= 10 OR 'Value 2' >= 10 THEN "A" ELSE "B"` | A | A | A |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fif-then-else-9fb6586e-0219-4771-a660-4ebcc317efc0&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>