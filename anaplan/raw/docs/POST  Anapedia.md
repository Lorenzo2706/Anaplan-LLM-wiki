---
title: "POST | Anapedia"
source: "https://help.anaplan.com/post-082cb491-879c-4711-b5c6-9ed162391bb1"
author:
published:
created: 2026-05-02
description: "The POST function helps you shift or move a number, such as a sales amount or order quantity, forward or backward along a dimension. If multiple values are offset to the same target item in the dimension, the POST function adds them together."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The POST function helps you shift or move a number, such as a sales amount or order quantity, forward or backward along a dimension. If multiple values are offset to the same target item in the dimension, the POST function adds them together.

You could use POST to determine when stock arrives at a warehouse given a certain lead time.

`POST(Value to post, Offset amount [, List]) `

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to post* | Number | The value to post to the target item in the dimension. |
| *Offset amount* | Number | The number of line items to offset forward or backward within the dimension. This can be a positive or negative number, or zero.  - A positive number posts a value into a later item in the dimension. - A negative number posts a value into an early item in the dimension. - A zero value keeps the value in the same item. |
| *List* (Polaris-only) | List | The list over which the function should operate.  See ***Calculation engine functionality differences****.* |

The POST function returns a number.

- In Polaris, you can't use the POST function for line items that have the **Formula** summary method. In the Classic Engine, you can.
- In Polaris, you can use the POST function over any dimension, by including an additional argument. In the Classic Engine, you can't. Where, if the additional argument isn't included, the function defaults to Time as the dimension.

`POST(Orders, Lead time)`

The time range for any values used as arguments for the POST function must match the time range of the result line item.

This example uses the POST function to offset the *Orders* line item for each month based on the *Lead time* line item.

|  | **Jan 22** | **Feb 22** | **Mar 22** | **Apr 22** | **May 22** | **Jun 22** | **Jul 22** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Orders** | 50 | 10 | 20 | 70 | 35 | 75 | 50 |
| **Lead time** | 3 | \-1 | \-2 | 1 | \-3 | 0 | \-4 |
| `POST(Orders, Lead time)` | 30 | 35 | 50 | 50 | 70 | 75 | 0 |

You can use the POST function in combination with the [IF THEN ELSE](https://help.anaplan.com/9fb6586e-0219-4771-a660-4ebcc317efc0) function to create a conditional formula. However, when you do this, ensure you position the two functions appropriately within your formula.

In this example, separate line items contain the *Value to post*, the *Offset amount*, and the Boolean condition that determines if a value should be posted.

When using the POST function within the IF THEN ELSE, the value is only posted in items where the Boolean condition is TRUE. However, the posted value can come from any of the values in the *Value to post*, irrespective of its Boolean condition.

When using the IF THEN ELSE within the POST function, the formula can contain the IF THEN ELSE function as part of the *Value to post* argument. This makes sure that values are posted in all items. However, the posted value can only come from the *Value to post* where its Boolean condition is TRUE.

|  | **Jan 22** | **Feb 22** | **Mar 22** | **Apr 22** | **May 22** | **Jun 22** | **Jul 22** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Value to post** | 1 | 2 | 4 | 10 | 20 | 40 | 100 |
| **Offset amount** | 1 | 1 | \-1 | 2 | \-2 | 1 | \-2 |
| **Boolean condition** |  |  |  |  |  |  |  |
| `IF Boolean condition THEN POST(Value to post, Offset amount) ELSE 0` | 0 | 5 | 22 | 0 | 0 | 10 | 0 |
| `POST(IF Boolean condition THEN Value to post ELSE 0, Offset amount)` | 0 | 4 | 2 | 0 | 0 | 10 | 40 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpost-082cb491-879c-4711-b5c6-9ed162391bb1&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>