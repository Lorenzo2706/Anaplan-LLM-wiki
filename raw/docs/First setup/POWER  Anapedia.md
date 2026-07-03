---
title: "POWER | Anapedia"
source: "https://help.anaplan.com/power-2327281c-743b-4f42-b6d7-c8592c4a8193"
author:
published:
created: 2026-05-02
description: "The POWER function raises a number to the power you specify."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

This function is the inverse of the [LOG](https://help.anaplan.com/56014c50-310d-42ba-b724-c47bb417651a) function.

For example, if the formula `LOG(a, b)` gives a result of c, the formula `POWER(b, c)` gives a result of a.

`POWER(Number, Power)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number* | Number | The number to raise to a power. |
| *Power* | Number | The power, or exponent, to raise the number to. |

In Polaris, `POWER(0,0)` returns 0.

In the Classic Engine, `POWER(0,0)` returns 1.

The POWER function can be used to calculate the root of a positive number by using a fraction for the *Power* argument. For example using 1/2 or 1/3 for the *Power* argument returns the square root and cube root respectively. However, if you attempt to return the root of a negative number, the POWER function returns a result of NaN (Not a Number).

[POWER](https://support.office.com/en-us/article/power-function-d3f2908b-56f4-4c3f-895a-07fb519c362a)

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `POWER(2, 4)` | This formula raises two to the power of four. | 16 |
| `POWER(9, 9)` | This formula raises nine to the power of nine. | 387,420,489 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpower-2327281c-743b-4f42-b6d7-c8592c4a8193&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>