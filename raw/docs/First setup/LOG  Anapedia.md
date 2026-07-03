---
title: "LOG | Anapedia"
source: "https://help.anaplan.com/log-56014c50-310d-42ba-b724-c47bb417651a"
author:
published:
created: 2026-05-02
description: "The LOG function returns the logarithm of a number to the base you specify."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

This function is the inverse of the [POWER](https://help.anaplan.com/2327281c-743b-4f42-b6d7-c8592c4a8193) function.

For example, if the formula `POWER(a, b)` gives a result of c, the formula `LOG(c, a)` gives a result of b.

`LOG(Number, Base)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number* | Number | The number to return the logarithm of. |
| *Base* (optional) | Number | The base to apply when returning the logarithm.  If omitted, the LOG function uses a default base of 10. |

In Polaris, the LOG function returns a value of *NaN* (Not a Number) if you use positive infinity for the *Base* argument.

In the Classic Engine, the LOG function returns 0 if you use positive infinity for the *Base* argument.

[LOG](https://support.office.com/en-gb/article/LOG-function-4e82f196-1ca9-4747-8fb0-6c4a3abb3280)

In this example, the *Number* and *Base* line items each contain four numeric values to be used for the *Number* and *Base* arguments respectively. The other two line items contain formulas to calculate the logarithm for the numbers.

As the formula for the *Logarithm base 10* line item does not contain the *Base* argument, the function returns the base 10 logarithm by default.

The values in this example are rounded to eight significant digits. You can change the number of digits that display in Anaplan under **Format** in blueprint view.

|  | **Item 1** | **Item 2** | **Item 3** | **Item 4** |
| --- | --- | --- | --- | --- |
| Number | 14.25 | 234.56 | 35.00 | 456.78 |
| Base | 8 | 6 | 9 | 3 |
| Logarithm with various bases  `LOG(Number, Base)` | 1.2776300 | 3.0460067 | 1.6181086 | 5.5744888 |
| Logarithm base 10  `LOG(Number)` | 1.1538149 | 2.3702540 | 1.5440680 | 2.6597071 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Flog-56014c50-310d-42ba-b724-c47bb417651a&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>