---
title: "ADDMONTHS | Anapedia"
source: "https://help.anaplan.com/addmonths-2d567a53-8b5d-413f-a0c6-53be2eb3984f"
author:
published:
created: 2026-05-02
description: "The ADDMONTHS function adds a number of months to a date."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the ADDMONTHS function to show a contractor's end date at a company.

`ADDMONTHS(Date, number)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Date* | Date | The date to add months to. |
| *Number* | Number | The number of months to add to the date. |

The ADDMONTHS function returns a date result.

In Polaris, if you use a value of *NaN* (Not a Number) for the *Number* argument, the ADDMONTHS function returns a blank value.

In the Classic Engine, a value of *NaN* used with ADDMONTHS is equivalent to 0.

If you want to subtract the number of months from a date, you can use negative numbers in a formula. For example, `ADDMONTHS(Amended contract date, -6)`.

[EDATE](https://support.microsoft.com/en-us/office/edate-function-3c920eb2-6e66-44e7-a1f5-753ae47ee4f5)

In this example, a *Contractor Details* module has line items on rows and the *Contractors* list on columns. Both line items have a date format.

The formula returns the date six months after the contractor's start date.

|  | **Shala Engle** | **Eric Jones** |
| --- | --- | --- |
| Contractor start date | 02/08/2021 | 06/09/2021 |
| Contractor end date  `ADDMONTHS(Contractor start date, 6)` | 02/02/2022 | 06/03/2022 |

If you want to add months and days to a date, you can use additional numbers in your formula. In this example, the formula returns the date six months and 14 days after the contractor's start date.

|  | **Shala Engle** | **Eric Jones** |
| --- | --- | --- |
| Contractor start date | 02/08/2021 | 06/09/2021 |
| Contractor end date  `ADDMONTHS(Contractor start date, 6) + 14` | 16/02/2022 | 20/03/2022 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Faddmonths-2d567a53-8b5d-413f-a0c6-53be2eb3984f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>