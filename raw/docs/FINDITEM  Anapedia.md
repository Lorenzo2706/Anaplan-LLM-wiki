---
title: "FINDITEM | Anapedia"
source: "https://help.anaplan.com/finditem-0668e215-a0d2-4ad1-b93f-3c2a56a9f5c2"
author:
published:
created: 2026-05-02
description: "The FINDITEM function searches a list for a matching item using a text input. If a match is found, it returns the corresponding item from the list."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The FINDITEM function searches a list for a matching item using a text input. If a match is found, it returns the corresponding item from the list.

For example, you could use the FINDITEM function to determine whether an item available in one region exists in a list of items available in other regions.

`FINDITEM(List, Text)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *List* | List | The list to search within. This is where the function looks for a match with the text input. |
| *Text* | Text | The text to match against the name or code of an item in the list. |

The FINDITEM function returns a result of the list data type, based on the given *List* argument.

In Polaris, you can't use the FINDITEM function on Time dimension. In the Classic Engine, you can.

In Polaris, you can't use this function for line items that have the **Formula** or **Ratio** summary methods. In the Classic Engine, you can.

`FINDITEM(Country, Country text)`

You must set the data type of the result line item to **List**, configured with the same list.

[LOOKUP](https://support.office.com/en-gb/article/LOOKUP-function-446d94af-663b-451d-8251-369d5e3864cb)

This example converts a text to a list item.

Here, the FINDITEM function takes the values of the line item *Country* and searches for it in the *Countries* list. If there's a match, it returns the corresponding list item that matches with the text in the line item *Country*. If you have a text value as *US* and you want to find the corresponding item in the list, you can use `FINDITEM(Countries, "US")`. This returns the list item *US* if it exists in the *Countries* list. If no match is found, no list item is returned and the result will be **blank**.

**Source list**

This is the list named *Countries*, as viewed from the **Grid View** under **General lists**.

|  | **Parent** | **Code** |
| --- | --- | --- |
| US |  | US |
| Canada |  | CA |
| Mexico |  | MX |
| UK |  | GB |
| France |  | FR |
| Spain |  | ES |
| Australia |  | AU |
| India |  | IN |
| Japan |  | JP |

**Result module**

The result module uses *Country* and *Code* as input values to search within the *Countries* list:

- *Country* and *Code*, **Text** data type
- *Output 1* and *Output 2*, **List** data types on the *Countries* list

|  | **Item 1** | **Item 2** | **Item 3** | **Item 4** | **Item 5** | **Item 6** |
| --- | --- | --- | --- | --- | --- | --- |
| Country | US | Spain | New Zealand | Kubek | India | Alberta |
| Output 1 `   FINDITEM(Countries, Country)` | US | Spain |  |  | India |  |
| Code | FR | AP | IN | CA-AB | US | CA-IN |
| Output 2 `   FINDITEM(Countries, Code)` | France |  | India |  | US |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ffinditem-0668e215-a0d2-4ad1-b93f-3c2a56a9f5c2&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>