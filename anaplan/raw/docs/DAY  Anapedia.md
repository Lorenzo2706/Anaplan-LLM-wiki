---
title: "DAY | Anapedia"
source: "https://help.anaplan.com/day-2acab59d-aca5-4c8a-8a79-b98f5846c200"
author:
published:
created: 2026-05-02
description: "The DAY function returns the day from a date as a number between 1 and 31. If the day is blank, it returns 0."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The DAY function returns the day from a date as a number between 1 and 31. If the day is blank, it returns 0.

For example, you can use the DAY function to extract the day of an employee's start or end date.

`DAY(Date)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Date | Date | The date to extract the day from. |

The DAY function returns a numeric result.

`DAY(DATE(2018, 1, 4))`

In this example, the formula returns the number 4.

[DAY](https://support.microsoft.com/en-gb/office/day-function-8a7d1cbb-6c7d-4ba1-8aea-25c134d03101?ui=en-us&rs=en-gb&ad=gb)

In this example, the line item *Date* is in **Date** format. The line item *Number* returns the **Number** format of the day using the formula `DAY(Date)`.

|  | **Jan 25** | **Feb 25** | **Mar 25** | **Apr 25** | **May 25** |
| --- | --- | --- | --- | --- | --- |
| Date | 01/01/2025 | 02/02/2025 | 03/03/2025 | 04/04/2025 | 05/05/2025 |
| Number   `DAY(Date)` | 1 | 2 | 3 | 4 | 5 |

In this example, the date line items *Contractor start date* and *Contractor end date* contain start and end dates for different contractors.

The `DAY(Contractor end date)` formula returns the day of the date from *Contractor end date*.

|  | **James Smith** | **Simon Peters** |
| --- | --- | --- |
| Contractor start date | 08/31/2019 | 09/22/2019 |
| Contractor end date   `ADDMONTHS(Contractor start date, 6)` | 02/29/2020 | 03/20/2020 |
| Contractor end day   `DAY(Contractor end date)` | 29 | 20 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fday-2acab59d-aca5-4c8a-8a79-b98f5846c200&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>