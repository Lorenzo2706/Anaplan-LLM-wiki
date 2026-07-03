---
title: "COUPNCD | Anapedia"
source: "https://help.anaplan.com/coupncd-f489d668-7f00-4000-bdcc-9761e79f45fe"
author:
published:
created: 2026-05-02
description: "The COUPNCD function calculates the next coupon date after a settlement date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the COUPNCD function to identify the next coupon date after you purchase a bond.

`COUPNCD(Settlement, Maturity, Frequency)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date, when the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date, when the bond expires. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly  If you use any value other than 1, 2, or 4, the function returns a blank result. |

The COUPNCD function returns a date.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

- The settlement and maturity dates must be between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.

[COUPNCD](https://support.office.com/en-us/article/coupncd-function-fd962fef-506b-4d9d-8590-16df5393691f)

In this example, two formulas calculate the next coupon date. The first formula uses 1 for the *Frequency* argument, so the coupon is paid annually. The second formula uses 4 for the *Frequency* argument, so the coupon is paid quarterly.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `COUPNCD(DATE(2021, 1, 15), DATE(2024, 1, 15), 1)` | This example calculates the next coupon date for a bond with a frequency of 1 (annual).  The settlement date is 01/15/2021 and the maturity date is 01/15/2024. | 01/15/2022 |
| `COUPNCD(DATE(2021, 1, 15), DATE(2024, 1, 15), 4)` | In this example, the next coupon date is calculated for a bond with a frequency of 4 (quarterly).  The example uses a settlement date of 01/15/2021 and a maturity date of 01/15/2024. | 04/15/2021 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcoupncd-f489d668-7f00-4000-bdcc-9761e79f45fe&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>