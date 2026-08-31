---
title: "DURATION | Anapedia"
source: "https://help.anaplan.com/duration-d32d366c-04b8-4047-a811-a13959f3dc4f"
author:
published:
created: 2026-05-02
description: "You can use the DURATION function to calculate the Macauley duration for an assumed parity value of 100 monetary units.The Macauley duration is the weighted average maturity of cash flows. That is, the weighted average distance to payment. It's used to measure a bond price's response to changes in yield. A higher Macauley duration value indicates a riskier investment."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

You can use the DURATION function to calculate the Macauley duration for an assumed parity value of 100 monetary units.

The Macauley duration is the weighted average maturity of cash flows. That is, the weighted average distance to payment. It's used to measure a bond price's response to changes in yield. A higher Macauley duration value indicates a riskier investment.

`DURATION(Settlement, Maturity, Rate, Yield, Frequency [, Basis])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date: The date the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date: The date when the bond expires. |
| *Rate* (required) | Number | The bond annual coupon date. |
| *Yield* (required) | Number | The bond annual yield. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly |
| *Basis* | Number | The basis determines how many days exist in a year.  A full year has:  - 360 days when basis US (NASD) 30/360, Actual/360, and EUR 30/360 are used - 365 days when basis Actual/365 is used - 365 or 366 days when Actual/Actual is used  US 30/360 is the default basis for COUPDAYS. It can also be specified by entering 0.  To use a different type of day count basis, enter:  - 1 for Actual/Actual - 2 for Actual/360 - 3 for Actual/365 - 4 for European 30/360  Learn about the [conventions used to calculate the day count for basis](https://help.anaplan.com/44c45685-1873-4051-b0dc-160f21210fe7). |

The DURATION function returns a number.

The Macauley duration is calculated with the following formula:

$Duration = \frac
                  {
                    \sum_{t=1}^{T} 
                       \frac
                         {tC}
                         {(1+y)^{t}}
                    + \frac{TF}{(1+t)^{T}}
                  }
                  {
                    P
                  }$

Where:

- C is coupon
- y is yield
- F is face value
- P is price, inclusive of accrued interest
- T is number of periods

- The settlement and maturity dates must be valid dates between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.
- The rate and yield must be positive or zero.
- The frequency must be either 1 (annual), 2 (semi-annual), or 4 (quarterly).
- The basis, when specified, must be either 0 (US 30/360), 1 (Actual/Actual), 2 (Actual/360), 3 (Actual/365), or 4 (EUR 30/360).

[DURATION](https://support.microsoft.com/en-us/office/duration-function-b254ea57-eadc-4602-a86a-c8e369334038?ui=en-us&rs=en-us&ad=us)

This example shows a Macauley duration calculation that specifies a basis.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `DURATION(DATE(2018, 1, 15), DATE(2021, 1, 15), 0.12, 0.1, 1, 4)` | The example has a:  - settlement date of 01/15/2015 - maturity date of 01/15/2018 - rate of 0.12 (12%) - yield of 0.1 (10%) - frequency of 1 (annual) - basis of 4 (European 30/360) | 2.6976811 |

This example shows a Macauley duration calculation that does not specify a basis. As a result, the basis defaults to US 30/360.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `DURATION(DATE(2018, 1, 15), DATE(2021, 1, 15), 0.12, 0.1, 4)` | The example has a:  - settlement date of 01/15/2018 - maturity date of 01/15/2021 - rate of 0.12 (12%) - yield of 0.1 (10%) - frequency of 4 (quarterly) | 2.5760086 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fduration-d32d366c-04b8-4047-a811-a13959f3dc4f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>