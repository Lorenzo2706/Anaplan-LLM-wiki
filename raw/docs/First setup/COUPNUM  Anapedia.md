---
title: "COUPNUM | Anapedia"
source: "https://help.anaplan.com/coupnum-65da7647-8b2c-4b8c-82e5-32a2efb744da"
author:
published:
created: 2026-05-02
description: "The COUPNUM function returns the number of coupons payable between a settlement and maturity date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the COUPNUM function to calculate how many coupons remain to be paid for a bond.

`COUPNUM(Settlement, Maturity, Frequency)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date, when the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date, when the bond expires. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly  If you use any value other than 1, 2, or 4 for this argument, the function returns a blank result. |

The COUPNUM function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

- The settlement and maturity dates must be between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.

[COUPNUM](https://support.office.com/en-us/article/coupnum-function-a90af57b-de53-4969-9c99-dd6139db2522)

In this example, two formulas calculate how many coupons are payable between the settlement and maturity date. The first formula uses 1 for the *Frequency* argument, so coupons are paid annually. The second formula uses 4 for the *Frequency* argument, so coupons are paid quarterly.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `COUPNUM(DATE(2021, 1, 15), DATE(2024, 1, 15), 1)` | This example calculates how many coupons are payable given a coupon frequency of 1 per year.  The settlement date is 01/15/2021 and the maturity date is 01/15/2024. | 3 |
| `COUPNUM(DATE(2021, 1, 15), DATE(2024, 1, 15), 4)` | This example calculates how many coupons are payable given a coupon frequency of 4 per year.  The example uses a settlement date of 01/15/2021 and a maturity date of 01/15/2024. | 12 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcoupnum-65da7647-8b2c-4b8c-82e5-32a2efb744da&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>