---
title: "DECUMULATE | Anapedia"
source: "https://help.anaplan.com/decumulate-eab1f7ce-5c1d-46b6-8361-69086d4876e7"
author:
published:
created: 2026-08-31
description: "The DECUMULATE function subtracts the value of the previous item from the current over any dimension."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The DECUMULATE function subtracts the value of the previous item from the current over any dimension.

For example, you can use DECUMULATE to create a rolling comparison of the current month's performance relative to the previous month.

`DECUMULATE(Value to subtract[, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to subtract* | Number | The data from which the function subtracts the previous value. |
| *List* (Polaris-only) | List | The list over which the function should operate.  See ***Calculation engine functionality differences****.* |

The DECUMULATE function returns a number.

- In Polaris, you can't use the DECUMULATE function for line items that have the **Formula** summary method. In the Classic Engine, you can.
- In Polaris, you can use the DECUMULATE function over any dimension, by including an additional argument. In the Classic Engine, you can't. Where, if the additional argument isn't included, the function defaults to Time as the dimension.

In this example, the DECUMULATE function is used to calculate the profit each month. Note that in Jan 21, there's no previous month, so DECUMULATE returns the input value. From **February** onward, the DECUMULATE function subtracts the previous month's value from the current month's value.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** | **May 21** | **Jun 21** | **Jul 21** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Profit** | $59,730 | $59,124 | $59,993 | $59,494 | $58,817 | $59,833 | $58,945 |
| `DECUMULATE(Profit)` | 59,730 | \-606 | 869 | \-499 | \-677 | 1,016 | \-888 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fdecumulate-eab1f7ce-5c1d-46b6-8361-69086d4876e7&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>