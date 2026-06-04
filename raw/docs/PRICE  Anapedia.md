---
title: "PRICE | Anapedia"
source: "https://help.anaplan.com/price-27e2da03-28c7-40cd-88c4-d6c4c4a63287"
author:
published:
created: 2026-05-02
description: "The PRICE function calculates the price per 100 monetary units invested for a bond that pays periodic interest."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The PRICE function calculates the price per 100 monetary units invested for a bond that pays periodic interest.

You can use PRICE to calculate how much you pay against the bond's final value, and therefore the return on your investment.

`PRICE(Settlement, Maturity, Rate, Yield, Redemption, Frequency[, Basis])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date: The date the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date: The date when the bond expires. |
| *Rate* (required) | Number | The bond annual coupon date. |
| *Yield* (required) | Number | The bond annual yield. |
| *Redemption* (required) | Number | The payment received when the bond reaches maturity. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly |
| *Basis* | Number | The basis determines how many days exist in a year.  A full year has:  - 360 days when basis US (NASD) 30/360, Actual/360, and EUR 30/360 are used - 365 days when basis Actual/365 is used - 365 or 366 days when Actual/Actual is used  US 30/360 is the default basis for COUPDAYS. It can also be specified by entering 0.  To use a different type of day count basis, enter:  - 1 for Actual/Actual - 2 for Actual/360 - 3 for Actual/365 - 4 for European 30/360  Learn about the [conventions used to calculate the day count for basis](https://help.anaplan.com/44c45685-1873-4051-b0dc-160f21210fe7). |

The PRICE function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

For bonds that pay two or more coupons between settlement and maturity, the price is calculated with this formula:

$Price =
                \left [ 
                  \frac
                    {redemption}
                    {\left ( 1+\frac{yld}{frequency} \right )^{N-1+\frac{DSC}{E}}}
                \right ] +
                \left [ 
                  \sum_{k=1}^{N}
                    \frac
                      {100 * \frac{rate}{frequency}}
                      {\left ( 1+\frac{yld}{frequency} \right )^{k-1+\frac{DSC}{E}}} \right ]
                - 100 * \frac{rate}{frequency} * \frac{A}{E}$

For a bond that pays one coupon between settlement and maturity, the price is calculated with this formula:

$DSR = E – A$

$Price=
                \frac
                  {100 * \frac{rate}{frequency} + redemption}
                  {\frac{yld}{frequency} * \frac{DSR}{E}+1}
<ul>
  <li>100 * \frac{rate}{frequency} * \frac{A}{E}</li>
</ul>$

Where bonds have a zero rate and do not pay a coupon, the price is calculated with this formula:

$Price = \frac{redemption}{(1 + yld)^{n}}$

In these formulas:

- E is the number of coupon days in the coupon period containing the settlement
- A is the number of coupon days before settlement
- DSC is the number of coupon days between the settlement and the next coupon
- DSR is the number of coupon days between the settlement and the maturity
- yld is the yield
- N is the total number of coupon periods between settlement and maturity
- n is the number of years to maturity as a fraction (calculated using a basis)

- The settlement and maturity dates must be valid dates between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.
- The rate must be greater than zero.
- The yield must be greater than negative one.
- The redemption must be greater than zero.
- The frequency must be either 1 (annual), 2 (semi-annual), or 4 (quarterly).
- The basis, when specified, must be either 0 (US 30/360), 1 (Actual/Actual), 2 (Actual/360), 3 (Actual/365), or 4 (EUR 30/360).

[PRICE](https://support.microsoft.com/en-us/office/price-function-3ea9deac-8dfa-436f-a7c8-17ea02c21b0a)

This example shows a PRICE calculation that specifies a basis.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `PRICE(DATE(2015, 1, 15), DATE(2018, 1, 15), 0.12, 0.10, 100, 1, 4)` | The example has a:  - settlement date of 01/15/2015 - maturity date of 01/15/2018 - rate of 0.12 (12%) - a yield of 0.10 (10%) - redemption of 100 monetary units - frequency of 1 (annual) - basis of 4 (European 30/360) | 104.97 |

This example shows a PRICE calculation that does not specify a basis. As a result, the basis defaults to US 30/360.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `PRICE(DATE(2015, 1, 15), DATE(2018, 1, 15), 0.12, 0.10, 100, 4)` | The example has a:  - settlement date of 01/15/2015 - maturity date of 01/15/2018 - rate of 0.12 (12%) - a yield of 0.10 (10%) - redemption of 100 monetary units - frequency of 1 (annual) | 105.13 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fprice-27e2da03-28c7-40cd-88c4-d6c4c4a63287&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>