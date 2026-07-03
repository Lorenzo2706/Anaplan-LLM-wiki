---
title: "ROUND | Anapedia"
source: "https://help.anaplan.com/round-0d779b88-d366-4849-af05-f57367772598"
author:
published:
created: 2026-05-02
description: "The ROUND function rounds a value to a specified number of decimal places, an integer, or a power of 10."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ROUND function rounds a value to a specified number of decimal places, an integer, or a power of 10.

For example, you can use ROUND to calculate the number of products a certain number of parts can create.

`ROUND(Number to round [, Number of decimal places] [, Rounding direction] [, Rounding method])`

**Note**: Only the first argument is required. If you use the optional arguments, then all preceding arguments are required.

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number to round* (required) | Number | The number to round. |
| *Number of decimal places* | Number | The number of decimal places to round to.  If you omit this argument, the ROUND function rounds to the nearest whole integer. |
| *Rounding direction* | Keyword | The direction to round in.  The keywords are UP, DOWN, NEAREST, TOWARDSZERO, and AWAYFROMZERO. There's more information in the Rounding direction keywords section below.  If you provide the *Number of decimal places* argument, but omit this argument, the ROUND function uses the NEAREST keyword by default. |
| *Rounding method* | Keyword | The rounding method to use.  The keywords are NORMAL and EXACT.  If you omit the *Rounding method* argument, NORMAL is the default.  There's more information in the Rounding direction keywords section below. |

The ROUND function returns a number-formatted result.

| **Keyword** | **Description** |
| --- | --- |
| UP | Rounds the value of the *Number to round* argument up, toward positive infinity.  This behavior is different to the Excel function ROUNDUP, which rounds away from zero. |
| DOWN | Rounds the value of the *Number to round* argument down, toward negative infinity.  This behavior is different to the Excel function ROUNDDOWN, which rounds towards zero. |
| NEAREST | The default keyword if you omit the *Rounding direction* argument.  Rounds the value of the *Number to round* argument to the nearest number or decimal place. Halves are rounded up. |
| TOWARDSZERO | Rounds the value of the *Number to round* argument toward zero. |
| AWAYFROMZERO | Rounds the value of the *Number to round* argument away from zero. |

| **Keyword** | **Description** |
| --- | --- |
| NORMAL | The default keyword if you omit the *Rounding method* argument.  When you use the NORMAL keyword, for some rare input values, the ROUND function results in a small degree of floating point error for the least significant digits. |
| EXACT | When you use the EXACT keyword, the ROUND function performs additional processing to minimize the effect of floating point error. |

In Polaris, the ROUND function always uses the EXACT rounding method. As such, you cannot provide the *Rounding method* argument. In the Classic engine, the ROUND function uses the NORMAL rounding method unless you provide EXACT for the *Rounding method* argument.

In Polaris, if *Number to round* is 0 and *Number of decimal places* is *NaN* (Not a Number), then the ROUND function returns 0. In the Classic Engine, this returns *NaN*.

In Polaris, if *Number to round* is not 0 and *Number of decimal places* is *NaN* (Not a Number), then the ROUND function returns *NaN*. In the Classic Engine, this returns *NaN* for the NORMAL *Rounding method*, and the *Number to round* for the EXACT *Rounding method*.

In Polaris, if *Number of decimal places* is not a whole number, then Number of decimal places rounds to the nearest whole number. The Classic Engine does not support the NORMAL *Rounding method* in this case, and with the EXACT *Rounding method*, ROUND rounds towards zero.

In Polaris, if *Number of decimal places* is -Infinity or less than -308.5, then ROUND returns 0, -Infinity, or Infinity, as expected. If *Number of decimal places* is Infinity or greater than 308.5, then ROUND returns *Number to round*, -Infinity, or Infinity, as expected. In the Classic Engine, all these return *NaN* (Not a Number).

In Polaris, if *Rounding direction* is UP, DOWN, AWAYFROMZERO, or TOWARDSZERO, and the result is too small to represent, then ROUND returns the smallest possible number. In the Classic Engine, these cases, with a *Rounding method* of EXACT, return 0.

In Polaris, if *Number to round* is negative, *Rounding direction* is NEAREST, and *Number of decimal places* is negative, then ROUND rounds away from zero. The Classic Engine rounds this towards zero.

`ROUND((Payment amount * Exchange rate), 2, UP, EXACT)`

This formula multiplies a payment amount by an exchange rate and rounds the result to two decimal places. The formula uses the UP keyword to round upwards toward positive infinity and uses the EXACT keyword to minimize any floating point error.

You can use a negative number for the *Number of decimal places* argument. If you do this, the ROUND function rounds the *Number to round* argument to a power of ten. You can also use the [MROUND](https://help.anaplan.com/a6f48277-3751-48da-bef8-587d08f088ca) function to do this, and that function can also round to numbers that are not a power of ten.

When you round a number that's very large or has a lot of decimal places, sometimes tiny precision differences can arise due to floating point math. Find out more about [Precision differences and large number calculations](https://help.anaplan.com/f8b2ba0a-1291-4424-9a06-06a601ccc269).

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `ROUND(12.344)` | Only the value to be rounded, 12.344, has been provided. The formula uses the default arguments of: 0 decimal places, the NEAREST direction, and NORMAL rounding method | 12.0 |
| `ROUND(12.399, 1, DOWN)` | This formula contains arguments of 1 decimal place and the DOWN direction. This means that 12.399 is rounded down to one decimal place. | 12.3 |
| `ROUND(-12.5)` | As this formula only contains ROUND and a value to be rounded, it uses the default arguments of: 0 decimal places, the NEAREST direction, and NORMAL rounding method. As -12.5 is a negative number, it rounds down. | \-13 |
| `ROUND(532.8399, 2, TOWARDSZERO)` | This formula contains arguments of 2 decimal places and the TOWARDSZERO direction. This means that 532.8399 is rounded down towards zero to 2 decimal places. This usage of ROUND can calculate the price of a product. Rounding towards zero maximizes profit margin. | 532.83 |
| `ROUND(28.135, 1, UP)` | This formula contains arguments of 1 decimal place and the UP direction. This means that 28.135 is rounded up to one decimal place. | 28.2 |
| `ROUND(2.509, 2, NEAREST, NORMAL)` | This is an example where the NORMAL rounding method results in a small degree of error. | 2.5100000000000002 |
| `ROUND(2.509, 2, NEAREST, EXACT)` | The additional processing performed by the EXACT rounding method corrects the small degree of error in the previous example. | 2.51 |

In foreign exchange, exchange rates often include up to 5 decimal places. However, some currencies such as Euros, U.S. Dollars, or Pound Sterling can only be paid in increments of two decimal places.

In this example, payments are made from a company in U.S. Dollars to an account that uses Euros. It contains a *Transaction* list on columns, and line items on rows. The line items include:

- The amount paid in U.S. dollars.
- The detailed exchange rate for U.S. Dollars to Euros, to five decimal places.
- A formula that applies the detailed exchange rate to the U.S. Dollar amount, then uses the ROUND function to round the final amount up to two decimal places for payment.

|  | **Transaction 1** | **Transaction 2** | **Transaction 3** | **Transaction 4** | **Transaction 5** |
| --- | --- | --- | --- | --- | --- |
| Amount to be paid (USD) | USD 500 | USD 750 | USD 100 | USD 125 | USD 375 |
| Exchange rate at time of payment | 0.84271 | 0.84037 | 0.82473 | 0.82829 | 0.85154 |
| Amount paid (EUR)  `ROUND(('Amount to be paid (USD)' * 'Exchange rate at time of payment'), 2, UP, EXACT)` | EUR 421.36 | EUR 630.28 | EUR 82.48 | EUR 103.54 | EUR 319.33 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fround-0d779b88-d366-4849-af05-f57367772598&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>