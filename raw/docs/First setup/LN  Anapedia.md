---
title: "LN | Anapedia"
source: "https://help.anaplan.com/ln-e72b1d5c-0076-490d-b6a8-216a5009dcf8"
author:
published:
created: 2026-05-02
description: "Use the natural logarithm (LN) to work out the length of time it takes to achieve a unit of growth.LN returns the natural logarithm of a number, based on the constant e. This function is the inverse of the EXP function, which raises e to the nth power."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use the natural logarithm (LN) to work out the length of time it takes to achieve a unit of growth.

LN returns the natural logarithm of a number, based on the constant *e*. This function is the inverse of the EXP function, which raises e to the nth power.

You can use the natural logarithm (LN) to work out the length of time it takes to achieve a unit of growth, such as with compound interest.

LN returns the natural logarithm of a number, based on the constant *e*. This function is the inverse of the EXP function, which raises e to the nth power.

In terms of measuring growth:

- EXP allows you to enter time in order to work out growth
- LN allows you to enter growth in order to work out the time it would take to achieve that growth

`LN(Number)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Number | Numeric line item, property or expression | Number you want to return the natural logarithm for |

Here's an example of how to use LN to find out how long it will take to achieve a specific amount of growth based on compound interest.

- If an investment grows at a rate of 10% per annum how long will it take for the investment to reach a specific amount?

To calculate this, use this syntax:

`LN(total amount after growth/current amount )/LN(1 + percentage growth rate represented as a multiplier e.g. 1.10 for 10% in this instance)= Time to hit the specific amount`

You can only use LN with positive numbers.

[LN](https://support.office.com/en-gb/article/LN-function-81fe1ed7-dac9-4acd-ba1d-07a142c6118f)

Using the example above, let's work out how long it will take for an initial investment of $25,000 to reach $65,000.

LN(total amount after growth/current amount )/LN(1 + interest rate represented as a multiplier)= Time in years to hit the specific amount

LN($65,000/$25,000)/LN(1 + 1.10)=10.0252821576 (approximately 10 years).

| Initial investment | $25,000 |
| --- | --- |
| Investment goal | $65,000 |
| Annual percentage rate (APR) | 10% |
| Time to hit goal (using LN)  `*LN(Investment goal/Initial investment)/LN(1 + 'Annual percentage rate(APR)')*` | 10 years |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fln-e72b1d5c-0076-490d-b6a8-216a5009dcf8&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>