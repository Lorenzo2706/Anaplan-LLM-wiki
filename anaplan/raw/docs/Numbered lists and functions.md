---
title: "Numbered lists and functions"
source: "https://help.anaplan.com/numbered-lists-and-functions-b317dde6-4aa0-4be1-9b20-83168f7539ca"
author:
published:
created: 2026-05-13
description: "Model builders can use different functions when working with formulas and numbered lists."
tags:
  - "clippings"
---
[Numbered lists](https://help.anaplan.com/numbered-lists-371af0ef-1465-4c4f-9a73-4150f4a6ee95 "Numbered lists")

For example, you can use the [functions](https://help.anaplan.com/2701ca45-d892-429b-97a1-bf26a1c8180d) in the table below with numbered lists.

| **Function** | **Formula example** | **Description** |
| --- | --- | --- |
| SELECT | `Sales.Gross Sales[SELECT: #Products.'#20']` | In this example, the SELECT function identifies the value from the *Gross Sales* line item for a specific list item in the *#Products* numbered list.  **Note**: The SELECT function requires a list item's unique identifier that is automatically generated when each numbered list item is created.  Learn more in [SELECT](https://help.anaplan.com/8511de23-aafd-47c9-979d-57c4218fbc8c). |
| FINDITEM | `FINDITEM(#Employees, Employee Search)` | In this example, the FINDITEM function identifies list items in the *#Employees* numbered list that match the employee name you want to search for.  The *Employee Search* line item must be a text value. You can use the TEXT function to convert numbers in the numbered list to text.  **Note**: The FINDITEM function requires a list item's code, or the unique identifier that is automatically generated when each numbered list item is created.  Learn more in [FINDITEM](https://help.anaplan.com/1933a49b-40a1-4575-8dd8-0b859fd3a05b) and [TEXT](https://help.anaplan.com/7c779d7b-c753-43f0-bc10-43e78b9b8572). |
| NAME | `NAME(ITEM(#Transactions))` | The ITEM function identifies the list item in the *#Transactions* numbered list, and the NAME function converts the list item to text.  Learn more in [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d). |
| LOOKUP | `People Details.Days Available [LOOKUP:#Resources.Employees]` | In this example, the LOOKUP function identifies list items in the *#Resources* numbered list, then pulls data from the *Employees* list property.  This data is used to look up the days available for each employee.  **Note**: Use the LOOKUP function with list-formatted properties.  Learn more in [LOOKUP](https://help.anaplan.com/32c15f4e-62b7-4f7c-a63b-ee75b939f124). |
| SUM | `Project Days.Days Booked[SUM: #Resources.Employees]` | In this example, the SUM function identifies list items in the *#Resources* numbered list, then pulls data from the *Employees* list property.  This data is used to look up the days booked for each employee.  **Note**: Use the SUM function with list-formatted properties.  Learn more in [SUM](https://help.anaplan.com/27935be6-48ba-47a2-bdd6-117d225e1b02). |

Learn more in [Formulas](https://help.anaplan.com/e1cc95b4-915d-435b-98cc-d34fbf2ab032).

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fnumbered-lists-and-functions-b317dde6-4aa0-4be1-9b20-83168f7539ca&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>