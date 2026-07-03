---
title: "CODE | Anapedia"
source: "https://help.anaplan.com/code-0e20099c-af47-4343-9ad9-3a20b580d2de"
author:
published:
created: 2026-05-02
description: "The CODE function returns a list item's code."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the CODE function to ensure that a formula only applies to a specific employee in a list.

`CODE(Item)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Item* | List or time period | The list item or time period to return the code of. |

The CODE function returns a text value. If a list item does not have a code, the CODE function returns a blank value.

In Polaris, if you use a time period value for the *Item* argument, the CODE function returns a blank text result. In the Classic Engine, it returns the time period value as text.

In Polaris, you can't use this function for line items that have the **Formula** or **Ratio** summary methods. In the Classic Engine, you can.

When adding codes to list items, you can manually add or [import](https://help.anaplan.com/4ebabad1-072e-4850-8720-ea94cd3b1f75) codes from the **Grid View** of thecorresponding list.

[LOOKUP](https://support.microsoft.com/en-gb/office/lookup-function-446d94af-663b-451d-8251-369d5e3864cb?ui=en-us&rs=en-gb&ad=gb)

This example uses a list *Sales personnel*, which is shown below as displayed in the **Grid View**.

|  | **Parent** | **Code** |
| --- | --- | --- |
| John Johnson |  | SP001 |
| Barbara Jones |  | SP002 |
| Hannah Smith |  | SP003 |

In this example, a *Sales commission rates* module has line items on rows and the *Sales personnel* list on columns. The *Personnel code* line item has a **Text** data type.

The formula uses the [ITEM](https://help.anaplan.com/41298b7a-e877-40e8-8cfa-8d7009d8686f) function to identify the list item in the *Sales personnel* list, and the CODE function to return the code of that list item.

|  | **John Johnson** | **Barbara Jones** | **Hannah Smith** |
| --- | --- | --- | --- |
| Length of service (years) | 6 | 8 | 2 |
| Commission rate % | 3.25% | 3.5% | 2% |
| Personnel code   `CODE(ITEM(Sales personnel))` | SP001 | SP002 | SP003 |

In this example, an *Income statement* module has line items on rows and time on columns.

- The *Personnel code* line item has a **Text** data type
- The *Sales staff* line item has a **List** data type on the *Sales personnel* list

The formula uses the CODE function to return the code of the corresponding list item in *Sales staff*.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** | **May 21** | **Jun 21** |
| --- | --- | --- | --- | --- | --- | --- |
| Sales staff | John Johnson | Barbara Jones | John Johnson | Hannah Smith | Barbara Jones | Hannah Smith |
| Sales commission | 20,366 | 10,300 | 13,422 | 20,002 | 1,999 | 15,698 |
| Personnel code   `CODE(Sales staff)` | SP001 | SP002 | SP001 | SP003 | SP002 | SP003 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcode-0e20099c-af47-4343-9ad9-3a20b580d2de&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>