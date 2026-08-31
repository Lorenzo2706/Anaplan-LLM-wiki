---
title: "COUPPCD | Anapedia"
source: "https://help.anaplan.com/couppcd-1df0eb5c-b905-4925-b77e-ee853c2ef13a"
author:
published:
created: 2026-05-02
description: "The COUPPCD function calculates the previous coupon date before a settlement date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the COUPPCD function to identify the most recent coupon date for a bond before it was traded to a buyer.

`COUPPCD(Settlement, Maturity, Frequency)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Settlement* (required) | Date | The bond settlement date, when the bond is traded to the buyer. |
| *Maturity* (required) | Date | The bond maturity date, when the bond expires. |
| *Frequency* (required) | Number | The number of coupon payments per year.  Enter:  - 1 for annual - 2 for semi-annual - 4 for quarterly  If you use any value other than 1, 2, or 4, the function returns a blank result. |

The COUPPCD returns a date.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

- The settlement and maturity dates must be between 01/01/1900 and 12/31/2399.
- The maturity date must be later than the settlement date.

[COUPPCD](https://support.microsoft.com/en-us/office/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3?ui=en-us&rs=en-us&ad=us)

For example, the formula below calculates the previous coupon date before the settlement date for a bond. In this example, as the coupon is paid annually, the previous coupon date was 01/31/2014.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `COUPPCD(DATE(2015, 1, 15), DATE(2018, 1, 31), 1)` | In this example, the previous coupon date is calculated for a bond with a frequency of 1 (annual).  The example uses a settlement date of 01/15/2015 and a maturity date of 01/31/2018. | 01/31/2014 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcouppcd-1df0eb5c-b905-4925-b77e-ee853c2ef13a&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>