---
title: "ISBLANK | Anapedia"
source: "https://help.anaplan.com/isblank-709bc8d0-f645-4a83-b7d9-7cd2476cee12"
author:
published:
created: 2026-05-02
description: "The ISBLANK function returns true for values that are blank."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the ISBLANKfunction to determine if an employee has an active health plan.

`ISBLANK(Value to test)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to test* | Date, time period, text, or list | The value to test for blankness. |

The ISBLANK function returns a Boolean result.

In Polaris, the ISBLANK function considers a text value that consists exclusively of carriage return characters to be a blank value.

In the Classic Engine, the ISBLANK function considers a carriage return to be a non-blank value.

`ISBLANK(Health Plan Start Date)`

In this example, *Health Plan Start Date* is a line item with a date format. This function returns true if a value from the line item is empty, which means there is no Health Plan Start Date on record.

[ISBLANK](https://support.microsoft.com/en-gb/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665)

In this example, *Health Plan Start Date* source is period-formatted, using `ISBLANK (Health Plan Start Date)` will return a boolean value of true if *Health Plan Start Date* is blank, and false if the value is anything else.

|  | **Jan 2021** | **Feb 2021** | **Mar 2021** | **Q1 FY21** |
| --- | --- | --- | --- | --- |
| Health Coverage Points | 75 | 98 | 115 | 288 |
| Health Plan |  |  | Single |  |
| Employee Deduction (%Salary) | 0 | 0 | 3.5 |  |
| Health Plan Start Date |  |  | Mar 2021 |  |
| `ISBLANK (Health Plan Start Date)` |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fisblank-709bc8d0-f645-4a83-b7d9-7cd2476cee12&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>