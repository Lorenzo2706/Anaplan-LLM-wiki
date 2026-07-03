---
title: "DATE | Anapedia"
source: "https://help.anaplan.com/date-68d07b3e-cf86-48fc-9822-ead63c7be153"
author:
published:
created: 2026-05-02
description: "The DATE function forms a date from values that represent the year, month, and day."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

`DATE(Year, Month, Day)`

| **Argument** | **Data type** | **Descriptio** n |
| --- | --- | --- |
| Year | Number | A four-digit number that represents the year. |
| Month | Number | A number between 1 and 12 that represents the month. |
| Day | Number | A number between 1 and 31 that represents the day. |

The DATE function returns a date.

The format used to display the date depends on your OS/browser settings. For example, the U.S. date format displays the month before the day (mm/dd/yyyy).

- The month must be a number between 1 and 12, inclusive.
- The day must be a number between 1 and 31, inclusive.
- The values must represent a valid date (01/01/1900 —12/31/2399).

[DATE](https://support.microsoft.com/en-gb/office/date-function-e36c0c8c-4104-49da-ab83-82328b832349?ui=en-us&rs=en-gb&ad=gb)

You can enter values directly into the DATE formula, or reference line items or list properties that are number formatted.

| **Formula** | **Description** | **Result for U.S. date format** |
| --- | --- | --- |
| `DATE(2018, 12, 25)` | This example shows how you can enter values directly into your formula. | 12/25/2018 |
| `DATE(Previous Year, Start Month, 3)` | This example shows how you can reference line items or list properties in your formula. | 03/01/2017 |
| `DATE(2018.3, 2.65, 8.4)` | This example shows how the DATE function will round to the nearest whole number. | 03/08/2018 |

In this example, the line items *Day*, *Month*, and *Year* are in **Number** format. The line item *Date* returns the **Date** format of the numeric line items using the formula `DATE(Year, Month, Date)`.

|  | **a** | **b** | **c** | **d** | **e** |
| --- | --- | --- | --- | --- | --- |
| Day | 1 | 4 | 26 | 16 | 10 |
| Month | 6 | 4 | 5 | 8 | 9 |
| Year | 2,021 | 2,025 | 2,024 | 2,022 | 2,023 |
| Date   `DATE(Year, Month, Date)` | 01/06/2021 | 04/04/2025 | 26/05/2024 | 16/08/2022 | 10/09/2023 |

In this example, the line items *Day*, *Month*, and *Year* are in **Text** format. The date format requires numerical data, so you need to convert these text data to a number using `VALUE`, and then convert it to a date using `DATE`. The line item *Date* returns the **Date** format of the line items using the formula `DATE(VALUE(Year), VALUE(Month), VALUE(Day))`.

|  | **a** | **b** | **c** | **d** | **e** |
| --- | --- | --- | --- | --- | --- |
| Day | 20 | 6 | 16 | 3 | 10 |
| Month | 2 | 5 | 6 | 8 | 9 |
| Year | 2025 | 2023 | 2021 | 2022 | 2024 |
| Date   `DATE(VALUE(Year), VALUE(Month), VALUE(Day))` | 20/02/2025 | 06/05/2023 | 16/06/2021 | 03/08/2022 | 10/09/2024 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fdate-68d07b3e-cf86-48fc-9822-ead63c7be153&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>