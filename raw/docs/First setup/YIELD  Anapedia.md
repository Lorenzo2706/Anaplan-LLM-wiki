---
title: "YIELD | Anapedia"
source: "https://help.anaplan.com/yield-e5b84f11-aecb-40f9-931a-9c07cf7859e5"
author:
published:
created: 2026-05-02
description: "Use this function to calculate the yield to maturity (YTM) of a bond."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The YTM is the overall rate of interest that, when used to discount the bond's future cashflows, produces the given price.

When interest rates rise, bond prices fall, so it is important to know the yield when calculating the price of a bond.

As yield is used in the formula for calculating price, you can determine the value of the yield using an iterative solution.

This is the formula for price:

$Price =
                  \sum_{t}^{T-1}
                    \frac
                      {CashFlows_{t}}
                      {(1+Yield)^t}$

Where *T* is the total number of coupon periods.

`YIELD(Settlement, Maturity, Rate, Price, Redemption, Frequency [, Basis])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date: The date the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date: The date when the bond expires. |
| *Rate* (required) | Number | The bond annual coupon date. |
| *Price* (required) | Number | The bond price per 100 monetary units, face value. |
| *Redemption* (required) | Number | The payment received when the bond reaches maturity. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly |
| *Basis* | Number | The basis determines how many days exist in a year.  A full year has:  - 360 days when basis US (NASD) 30/360, Actual/360, and EUR 30/360 are used - 365 days when basis Actual/365 is used - 365 or 366 days when Actual/Actual is used  US 30/360 is the default basis for COUPDAYS. It can also be specified by entering 0.  To use a different type of day count basis, enter:  - 1 for Actual/Actual - 2 for Actual/360 - 3 for Actual/365 - 4 for European 30/360  Learn about the [conventions used to calculate the day count for basis](https://help.anaplan.com/44c45685-1873-4051-b0dc-160f21210fe7). |

The YIELD function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

If the price and redemption parameters are very far apart, the iterative method of calculation might never converge on a result. In this case, NaN (not a number) is returned.

- The settlement and maturity dates must be valid dates between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.
- The price must be greater than zero.
- The redemption must be greater than zero.
- The basis, when specified, must be either 0 (US 30/360), 1 (Actual/Actual), 2 (Actual/360), 3 (Actual/365), or 4 (EUR 30/360).

[YIELD](https://support.office.com/en-ie/article/YIELD-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe)

This example shows a YIELD calculation that specifies a basis.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `YIELD(DATE(2018, 1, 15), DATE(2021, 1, 15), 0.12, 90, 100, 1, 4)` | The example has a:  - settlement date of 01/15/2018 - maturity date of 01/15/2021 - rate of 0.12 (12%) - price of 90 monetary units - redemption of 100 monetary units - frequency of 1 (annual) - basis of 4 (European 30/360) | 0.1648 or 16.5%. |

In this example the yield is calculated without specifying a basis. As a result, the basis defaults to US 30/360.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `YIELD(DATE(2018, 1, 15), DATE(2021, 1, 15), 0.12, 90, 100, 4)` | Here:  - the settlement date is 01/15/2018 - the maturity date is 01/15/2021 - the rate is 0.12 (12%) - the price is 90 monetary units - the redemption is 100 monetary units - the frequency is 4 (quarterly) | 0.1627 or 16.3% |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fyield-e5b84f11-aecb-40f9-931a-9c07cf7859e5&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>