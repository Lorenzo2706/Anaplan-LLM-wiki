---
title: "COUPDAYBS | Anapedia"
source: "https://help.anaplan.com/coupdaybs-ecaa8437-e5c7-42ff-9ce2-99644b0d4d45"
author:
published:
created: 2026-05-02
description: "Use the COUPDAYBS (coupon days before settlement) function to calculate the number of days from the beginning of the coupon period until its settlement date. The number returned includes both the first day of the period and the settlement date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use the COUPDAYBS (coupon days before settlement) function to calculate the number of days from the beginning of the coupon period until its settlement date. The number returned includes both the first day of the period and the settlement date.

`COUPDAYBS(Settlement, Maturity, Frequency[, Basis])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date: The date the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date: The date when the bond expires. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly |
| *Basis* | Number | The basis determines how many days exist in a year.  A full year has:  - 360 days when basis US (NASD) 30/360, Actual/360, and EUR 30/360 are used - 365 days when basis Actual/365 is used - 365 or 366 days when Actual/Actual is used  US 30/360 is the default basis for COUPDAYS. It can also be specified by entering 0.  To use a different type of day count basis, enter:  - 1 for Actual/Actual - 2 for Actual/360 - 3 for Actual/365 - 4 for European 30/360  Learn about the [conventions used to calculate the day count for basis](https://help.anaplan.com/44c45685-1873-4051-b0dc-160f21210fe7). |

The COUPDAYBS function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

- The settlement and maturity dates must be valid dates between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.
- The frequency must be either 1 (annual), 2 (semi-annual), or 4 (quarterly).
- The basis, when specified, must be either 0 (US (NASD) 30/360), 1 (Actual/Actual), 2 (Actual/360), 3 (Actual/365), or 4 (EUR 30/360).

[COUPDAYBS](https://support.office.com/en-us/article/COUPDAYBS-function-EB9A8DFB-2FB2-4C61-8E5D-690B320CF872)

This example shows how the number of days before the settlement date can be calculated when a basis is specified.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `COUPDAYBS(DATE(2015, 1, 15), DATE(2018, 1, 31), 1, 1)` | This formula uses:  - a settlement date of 01/15/2015 - a maturity date of 01/31/2018 - a frequency of 1 (annual) - a basis of 1 (Actual/Actual) | 349 |

In this example, the number of days in the coupon period that contains the settlement date is calculated without specifying a basis. As a result, the basis defaults to US 30/360.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `COUPDAYBS(DATE(2015, 1, 15), DATE(2018, 1, 31), 4)` | This formula uses:  - a settlement date of 01/15/2015 - a maturity date of 01/31/2018 - a frequency of 4 (quarterly) | 75 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcoupdaybs-ecaa8437-e5c7-42ff-9ce2-99644b0d4d45&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>