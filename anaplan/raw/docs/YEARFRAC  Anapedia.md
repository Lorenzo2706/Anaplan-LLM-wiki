---
title: "YEARFRAC | Anapedia"
source: "https://help.anaplan.com/yearfrac-1daf8419-1de9-483d-a9db-aa2d4e4affa2"
author:
published:
created: 2026-05-02
description: "Use the YEARFRAC function to calculate the fraction of a year between two dates (inclusive of the start date, exclusive of the end date).The function uses a basis (day-count convention) to count the number of days between these dates, and then divide that number by the basis."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use the YEARFRAC function to calculate the fraction of a year between two dates (inclusive of the start date, exclusive of the end date).

The function uses a basis (day-count convention) to count the number of days between these dates, and then divide that number by the basis.

`YEARFRAC(Start, End[, Basis])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Start* (required) | Date | The bond settlement date: The date the bond is traded to the buyer. |
| *End* (required) | Date | The bond maturity date: The date when the bond expires. |
| *Basis* | Number | The basis determines how many days exist in a year.  A full year has:  - 360 days when basis US (NASD) 30/360, Actual/360, and EUR 30/360 are used - 365 days when basis Actual/365 is used - 365 or 366 days when Actual/Actual is used  US 30/360 is the default basis for COUPDAYS. It can also be specified by entering 0.  To use a different type of day count basis, enter:  - 1 for Actual/Actual - 2 for Actual/360 - 3 for Actual/365 - 4 for European 30/360  Learn about the [conventions used to calculate the day count for basis](https://help.anaplan.com/44c45685-1873-4051-b0dc-160f21210fe7). |

The YEARFRAC function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

- The start and end dates must be valid dates between 01/01/1900 and 12/31/2399.
- The basis, when specified, must be either 0 (US (NASD) 30/360), 1 (Actual/Actual), 2 (Actual/360), 3 (Actual/365), or 4 (EUR 30/360).

[YEARFRAC](https://support.microsoft.com/en-us/office/yearfrac-function-3844141e-c76d-4143-82b6-208454ddc6a8?ui=en-us&rs=en-us&ad=us)

This example shows a YEARFRAC calculation that includes a basis.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `YEARFRAC(DATE(2015, 1, 15), DATE(2018, 4, 30), 1)` | This formula uses:  - a start date of as 01/15/2015 - an end date of 04/30/2018 - a basis of 1 (Actual/Actual) | 3.28767123 |

This example shows a YEARFRAC calculation does not use a basis. As a result, the basis defaults to US 30/360.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| YEARFRAC(DATE(2015, 1, 15), DATE(2018, 4, 30)) | This formula uses:  - a start date of 01/15/2015 - an end date of 04/30/2018 | 3.29166666 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fyearfrac-1daf8419-1de9-483d-a9db-aa2d4e4affa2&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>