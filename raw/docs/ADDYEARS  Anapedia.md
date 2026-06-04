---
title: "ADDYEARS | Anapedia"
source: "https://help.anaplan.com/addyears-2f37fddd-58a4-468b-be9b-40367e4ba7c3"
author:
published:
created: 2026-05-02
description: "The ADDYEARS function adds a number of years to a date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the ADDYEARS function to show a customer's contract end date.

`ADDYEARS(Date, number)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Date* | Date | The date to add years to. |
| *Number* | Number | The number of years to add to the date. |

The ADDYEARS function returns a date result.

In Polaris, if you use a value of *NaN* (Not a Number) for the *Number* argument, the ADDYEARS function returns a blank value.

In the Classic Engine, a value of *NaN* used with ADDYEARS is equivalent to 0.

If you want to subtract the number of years from a date in a formula, you can use negative numbers. For example, `ADDYEARS(Amended contract date, -2)`.

[EDATE](https://support.microsoft.com/en-us/office/edate-function-3c920eb2-6e66-44e7-a1f5-753ae47ee4f5)

In this example, a *Contract Details* module has line items on rows, and the *Customers* list on columns. Both line items have a date format.

The formula returns the date two years after the customer's contract start date.

|  | **Customer A** | **Customer B** |
| --- | --- | --- |
| Contract start date | 01/01/2021 | 01/06/2021 |
| Contract end date  `ADDYEARS(Contract start date, 2)` | 01/01/2023 | 01/06/2023 |

If you want to add years and days to a date, you can use additional numbers in your formula. In this example, the formula returns the date one year and seven days after the contract start date.

|  | **Customer A** | **Customer B** |
| --- | --- | --- |
| Contract start date | 01/01/2021 | 01/06/2021 |
| Contract end date  `ADDYEARS(Contract start date, 1) + 7` | 08/01/2022 | 08/06/2022 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Faddyears-2f37fddd-58a4-468b-be9b-40367e4ba7c3&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>