---
title: "MROUND | Anapedia"
source: "https://help.anaplan.com/mround-a6f48277-3751-48da-bef8-587d08f088ca"
author:
published:
created: 2026-05-02
description: "The MROUND function rounds a value to the nearest multiple of a number."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, if you require a certain number of a part to make a single product, you can use MROUND to calculate the number of products that can be made.

`MROUND(Number to round [, Multiple to round to] [, Rounding direction])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number to round* (required) | Number | The number to round. |
| *Multiple to round to* | Number | The multiple to round to.  Using 0 returns a value of *NaN* (Not a Number). |
| *Rounding direction* | Keyword | The direction to round in.  The keywords are UP, DOWN, NEAREST, TOWARDSZERO, and AWAYFROMZERO. There's more information below. |

The MROUND function returns a numeric result.

| **Keyword** | **Description** |
| --- | --- |
| UP | Rounds the value of the *Number to round* argument up, towards positive infinity.  This behavior is different to the Excel function ROUNDUP, which rounds away from zero. |
| DOWN | Rounds the value of the *Number to round* argument down, towards negative infinity.  This behavior is different to the Excel function ROUNDDOWN, which rounds towards zero. |
| NEAREST | The default keyword if you omit the *Rounding direction* argument.  Rounds the value of the *Number to round* argument to the nearest number or decimal place. |
| TOWARDSZERO | Rounds the value of the *Number to round* argument towards zero. |
| AWAYFROMZERO | Rounds the value of the *Number to round* argument away from zero. |

In Polaris, if *Number of decimal places* resolves to *NaN* (Not a Number) or 0, then the MROUND function returns 0. In the Classic Engine, this returns *NaN*.

`MROUND(Product components, 4, Down) / 4`

In this example the total number of *Product components* rounds down to the nearest multiple of four, and then divides by four. In this hypothetical example, you need four components to create a single product. As such, this formula provides the total number of products you can make with the current number of product components.

[MROUND](https://support.office.com/en-gb/article/MROUND-function-c299c3b0-15a5-426d-aa4b-d2d5b3baf427)

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `MROUND(1234.56)` | Only the value to be rounded, 1234.56, has been provided. The formula uses the default arguments of 0 decimal places and the NEAREST direction. | 1,235 |
| `MROUND(1234.56, 10)` | Rounds 1234.56 to the nearest multiple of 10. The formula contains no rounding direction, so the default NEAREST direction is used. | 1,230 |
| `MROUND(1236.54, 10, TOWARDSZERO)` | Rounds 1236.54 to a multiple of 10. The formula uses the TOWARDSZERO rounding direction, so 1236.54, a positive number, was rounded down. | 1,230 |
| `MROUND(1234.56, 10, AWAYFROMZERO)` | Rounds 1234.56 to the nearest multiple of 10. The formula uses the AWAYFROMZERO rounding direction, so 1234.56, a positive number, was rounded up. | 1,240 |
| `MROUND(1234.56, 1000)` | Rounds 1234.56 to the nearest multiple of 1,000. The formula contains no rounding direction, so the default NEAREST direction is used. | 1,000 |
| `MROUND(-1234.56, 1000, UP)` | Rounds -1234.56 to a multiple of 1,000. The formula uses the UP rounding direction, so x rounds towards positive infinity. | \-1,000 |
| `MROUND(-1234.56, 1000, DOWN)` | Rounds -1234.56 to a multiple of 1,000. The formula uses the DOWN rounding direction, so x rounds towards negative infinity. | \-2,000 |
| `MROUND(15555, 10)` | Rounds 15555 to the nearest multiple of 10. The formula contains no rounding direction, so the default NEAREST direction is used. As 55 is a positive number halfway between 50 and 60, x rounds up, towards positive infinity. | 15,560 |
| `MROUND(-15555, 10)` | Rounds -15555 to the nearest multiple of 10. The formula contains no rounding direction, so the default NEAREST direction is used. As -55 is a negative number halfway between -50 and -60, x rounds down, towards negative infinity. | \-15,560 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmround-a6f48277-3751-48da-bef8-587d08f088ca&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>