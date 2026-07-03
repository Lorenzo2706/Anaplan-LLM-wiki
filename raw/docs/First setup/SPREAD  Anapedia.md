---
title: "SPREAD | Anapedia"
source: "https://help.anaplan.com/spread-f2db2f33-5ff8-46b1-aa64-e3fa20ad5169"
author:
published:
created: 2026-05-02
description: "The SPREAD function divides a value evenly over multiple entities."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

`SPREAD(Value to divide, Entity count [, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to divide* | Number | The value to be spread across the entity count. |
| *Entity count* | Number | The number of entities over which to spread the value. |
| *List* (Polaris-only) | List | The list over which the function should operate.  See **Calculation engine functionality differences**. |

The SPREAD function returns a number.

- In Polaris, you can't use the SPREAD function for line items that have the **Formula** summary method. In the Classic Engine, you can.
- In Polaris, you can use the SPREAD function over any dimension, by including an additional argument. In the Classic Engine, you can't. Where, if the additional argument isn't included, the function defaults to Time as the dimension.

If you are operating over time, the *Value to divide* and *Entity count* arguments must have the same time range.

[SLN](https://support.office.com/en-gb/article/SLN-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8)

|  | **Jan 19** | **Feb 19** | **Mar 19** | **Apr 19** | **May 19** | **Jun 19** |
| --- | --- | --- | --- | --- | --- | --- |
| **Value to spread** | 1000 | 0 | 400 | 0 | 0 | 0 |
| `SPREAD(Value to spread, 4)` | 250 | 250 | 350 | 350 | 100 | 100 |

From the example above, the value *1000* is entered into the *Value to spread* cell for **Jan 19** and is spread over the next 4 months.

When an additional value of *400* is added for **Mar 19**, the value is also spread over the next 4 months. The overlapping months are summed up to provide a final figure.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fspread-f2db2f33-5ff8-46b1-aa64-e3fa20ad5169&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>