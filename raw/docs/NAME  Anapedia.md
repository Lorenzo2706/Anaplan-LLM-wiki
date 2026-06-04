---
title: "NAME | Anapedia"
source: "https://help.anaplan.com/name-bb3d44df-6980-4266-b9f8-42b053e7826d"
author:
published:
created: 2026-05-02
description: "Use the NAME function to convert a list item to a text data type."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

`NAME(List item)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *List item* | List | The list item to convert to a text data type. |

The NAME function returns a text result.

`NAME(Month period)`

This formula converts the value in the *Month period* line item into text.

[T](https://support.microsoft.com/en-gb/office/t-function-fb83aeec-45e7-4924-af95-53e073541228?ui=en-us&rs=en-gb&ad=gb)

NAME function converts list items and time-formatted list items to text.

**Source list**

This example uses a list named *Employees*, shown below in the **Grid View**.

|  | **Parent** | **Code** | **Start month** | **Start year** |
| --- | --- | --- | --- | --- |
| Alice |  |  | Jan 21 | FY21 |
| Bob |  |  | Jul 25 | FY25 |
| Carol |  |  | Sep 22 | FY22 |
| Dan |  |  | Jan 24 | FY24 |
| Ellie |  |  | Apr 23 | FY23 |
| Felix |  |  | Aug 25 | FY25 |

Here, the properties *Start month* and *Start year* are in **Month** and **Year** format, respectively.

**Target module**

The target module *Employee details* is dimensioned over the above list, *Employees*. The module has the list *Employees* on the columns. It has five line items on the rows:

- *Name*, **Text** data type.
	- This line item has the formula `NAME(ITEM(Employees))`. Here, `ITEM(Employees)` returns the list items from the *Employees* list, and `NAME()` converts those items to **Text**.
- *Start month*, **Text** data type.
	- This line item has the formula `NAME(Employees.Start month)`. Here, `Employees.Start month` returns the list items from the *Start month* property of the *Employees* list, and `NAME()` converts those items to **Text**.
- *Start year*, **Text** data type.
	- This line item has the formula `NAME(Employees.Start year)`. Here, `Employees.Start year` returns the list items from the *Start year* property of the *Employees* list, and `NAME()` converts those items to **Text**.

|  | **Alice** | **Bob** | **Carol** | **Dan** | **Ellie** | **Felix** |
| --- | --- | --- | --- | --- | --- | --- |
| Name   `NAME(ITEM(Employees))` | Alice | Bob | Carol | Dan | Ellie | Felix |
| Start month   `NAME(Employees.Start month)` | Jan 21 | Jul 25 | Sep 22 | Jan 24 | Apr 23 | Aug 25 |
| Start year   `NAME(Employees.Start year)` | FY21 | FY25 | FY22 | FY24 | FY23 | FY25 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fname-bb3d44df-6980-4266-b9f8-42b053e7826d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>