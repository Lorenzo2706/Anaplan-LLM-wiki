---
title: "TEXT | Anapedia"
source: "https://help.anaplan.com/text-7c779d7b-c753-43f0-bc10-43e78b9b8572"
author:
published:
created: 2026-05-02
description: "The TEXT() function converts numeric values to text."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the TEXT function to convert numeric values to text values for use in other functions that require text-based arguments.

`TEXT(Number to convert)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number to convert* | Number | The value to convert to text. |

The TEXT function returns a text result.

In Polaris, the TEXT function returns a text value of *NaN* when used with the numerical value *NaN*.

In the Classic Engine, the TEXT function returns a blank value when you use it with the numerical value value *NaN* (Not a Number).

Results for numbers less than 0.001 display in computerized scientific notations. For example, `TEXT(0.0001)` = ' `1.0E-4` '.

[TEXT](https://support.microsoft.com/en-gb/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c?ui=en-us&rs=en-gb&ad=gb)

In this example, the line item *Number* with a **Number** data type is converted to a **Text** data type using the formula `TEXT(Number)`. As a result, the line item contains numbers as text and is available for use in text functions such as `LEFT` and `RIGHT`.

|  | **Jan 25** | **Feb 25** | **Mar 25** | **Apr 25** | **May 25** |
| --- | --- | --- | --- | --- | --- |
| Number | 1 | 2 | 3 | 4 | 5 |
| Text   `TEXT(Number)` | 1 | 2 | 3 | 4 | 5 |

In this example, the line item *Date* with a **Date** data type is converted to a **Text** data type using the formula `TEXT(DAY(Date)) & "/" & TEXT(MONTH(Date)) & "/" & TEXT(YEAR(Date))`.

|  | **Jan 25** | **Feb 25** | **Mar 25** | **Apr 25** | **May 25** |
| --- | --- | --- | --- | --- | --- |
| Date | 01/01/2025 | 01/02/2025 | 01/03/2025 | 01/04/2025 | 01/05/2025 |
| Text   `TEXT(DAY(Date)) & "/" & TEXT(MONTH(Date)) & "/" & TEXT(YEAR(Date))` | 1/1/2025 | 1/2/2025 | 1/3/2025 | 1/4/2025 | 1/5/2025 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftext-7c779d7b-c753-43f0-bc10-43e78b9b8572&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>