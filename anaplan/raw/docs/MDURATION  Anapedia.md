---
title: "MDURATION | Anapedia"
source: "https://help.anaplan.com/mduration-611e8dae-c597-4ce3-b0af-149391c39c50"
author:
published:
created: 2026-05-02
description: "You can use the MDURATION function to calculate the modified Macauley duration for an assumed parity value of 100 monetary units.The modified Macauley duration expresses the measurable change in the value of a bond in response to a change in interest rates. The result represents the effect that a 1% change in interest rates will have on the price of a bond."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

You can use the MDURATION function to calculate the modified Macauley duration for an assumed parity value of 100 monetary units.

The modified Macauley duration expresses the measurable change in the value of a bond in response to a change in interest rates. The result represents the effect that a 1% change in interest rates will have on the price of a bond.

`MDURATION(Settlement, Maturity, Rate, Yield, frequency [, basis])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date: The date the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date: The date when the bond expires. |
| *Rate* (required) | Number | The bond annual coupon date. |
| *Yield* (required) | Number | The bond annual yield. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly |
| *Basis* | Number | The basis determines how many days exist in a year.  A full year has:  - 360 days when basis US (NASD) 30/360, Actual/360, and EUR 30/360 are used - 365 days when basis Actual/365 is used - 365 or 366 days when Actual/Actual is used  US 30/360 is the default basis for COUPDAYS. It can also be specified by entering 0.  To use a different type of day count basis, enter:  - 1 for Actual/Actual - 2 for Actual/360 - 3 for Actual/365 - 4 for European 30/360  Learn about the [conventions used to calculate the day count for basis](https://help.anaplan.com/44c45685-1873-4051-b0dc-160f21210fe7). |

The DURATION function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The modified Macauley duration is calculated with the following formula:

$MDuration = \frac
                  {
                    Duration
                  }
                  {
                    \left( 1 + \frac{y}{f} \right )
                  }$

Where:

- y is yield
- f is frequency

- The settlement and maturity dates must be valid dates between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.
- The rate and yield must be positive or zero.
- The frequency must be either 1 (annual), 2 (semi-annual), or 4 (quarterly).
- The basis, when specified, must be either 0 (US 30/360), 1 (Actual/Actual), 2 (Actual/360), 3 (Actual/365), or 4 (EUR 30/360).

[MDURATION](https://support.microsoft.com/en-us/office/mduration-function-b3786a69-4f20-469a-94ad-33e5b90a763c?ui=en-us&rs=en-us&ad=us)

This example shows a modified Macauley duration calculation that specifies a basis.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `MDURATION(DATE(2018, 1, 15), DATE(2021, 1, 15), 0.12, 0.1, 1, 4)` | The example has a:  - settlement date of 01/15/2018 - maturity date of 01/15/2021 - rate of 0.12 (12%) - yield of 0.1 (10%) - frequency of 1 (annual) - basis of 4 (European 30/360) | 2.4524373 |

This example shows a modified Macauley duration calculation that does not specify a basis. As a result, the basis defaults to US 30/360.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `MDURATION(DATE(2018, 1, 15), DATE(2021, 1, 15), 0.12, 0.1, 4)` | The example has a:  - settlement date of 01/15/2018 - maturity date of 01/15/2021 - rate of 0.12 (12%) - yield of 0.1 (10%) - frequency of 4 (quarterly) | 2.5131792 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmduration-611e8dae-c597-4ce3-b0af-149391c39c50&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>