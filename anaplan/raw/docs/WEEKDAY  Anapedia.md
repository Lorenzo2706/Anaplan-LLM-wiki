---
title: "WEEKDAY | Anapedia"
source: "https://help.anaplan.com/weekday-a445eb44-98b7-4abc-8748-92435187e423"
author:
published:
created: 2026-05-02
description: "The WEEKDAY function converts a date to a number between one and seven, representing the day of the week."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The WEEKDAY function converts a date to a number between one and seven, representing the day of the week.

You could use WEEKDAY to check if a transaction occurs on a weekend.

`WEEKDAY(Date [, First day of the week])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Date* (required) | Date | The date to return the day of the week for as a number. Returns 1 for Monday, 2 for Tuesday, and so on. |
| *Day offset* | Number | This argument specifies which day of the week the WEEKDAY function should consider to be the first day of the week.  For example, a value of 2 means that WEEKDAY returns a 1 for Tuesday, a 2 for Wednesday, and so on.  If omitted, a value of one is used by default. |

The WEEKDAY function returns a number.

In Polaris, you can use a decimal value for the *Day offset* argument and it is rounded to the nearest whole number. If you use a value outside of 1 to 7, the function returns a value of 0.

In the Classic Engine, you must use a whole number for the *Day offset* argument.

`WEEKDAY(Scheduled payment date)`

[WEEKDAY](https://support.office.com/en-gb/article/WEEKDAY-function-60e44483-2ed1-439f-8bd0-e404c190949a)

In this example, a module is dimensioned by a *Transactions* list. The *Transaction date* line item has the date data type. The other line items contain formulas.

The *Day of the week* line item uses the WEEKDAY function with the *Transaction date* line item. As the *First day of the week* argument is omitted, 1 represents Monday, 2 represents Tuesday, and so on.

The *Day of the week two days later* line item also uses the WEEKDAY function. However, 3 is used for the *Starting day of the week* argument. This means that 1 represents Wednesday, 2 represents Thursday, and so on.

|  | Transaction date | Day of the week  `WEEKDAY(Transaction date)` | Day of the week two days later  `WEEKDAY(Transaction date, 3)` |
| --- | --- | --- | --- |
| **Transaction 001** | 01/03/2022 | 1 | 6 |
| **Transaction 002** | 01/04/2022 | 2 | 7 |
| **Transaction 003** | 01/05/2022 | 3 | 1 |
| **Transaction 004** | 01/06/2022 | 4 | 2 |
| **Transaction 005** | 01/07/2022 | 5 | 3 |
| **Transaction 006** | 01/08/2022 | 6 | 4 |
| **Transaction 007** | 01/09/2022 | 7 | 5 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fweekday-a445eb44-98b7-4abc-8748-92435187e423&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>