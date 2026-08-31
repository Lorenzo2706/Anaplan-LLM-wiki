---
title: "ITEM | Anapedia"
source: "https://help.anaplan.com/item-41298b7a-e877-40e8-8cfa-8d7009d8686f"
author:
published:
created: 2026-05-02
description: "When used with a list, ITEM() returns the list item that applies to each cell. When used with Time, it returns the time period that applies to each cell."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

When used with a list, `ITEM()` returns the list item that applies to each cell. When used with **Time**, it returns the time period that applies to each cell.

For example, you can use `ITEM()` to create conditional formulas where the output changes based on the list that applies to a cell in a module.

`ITEM(List)`

| **Argument** | **Data Type** | **Description** |
| --- | --- | --- |
| *List* | List or Time | The name of the list, or a reference to a time period, to return the item from. |

You can use two arguments separated by a comma for `ITEM()`. When you do this, your formula automatically updates to use [`FINDITEM()`](https://help.anaplan.com/0668e215-a0d2-4ad1-b93f-3c2a56a9f5c2) upon submission.

For example:

The formula `ITEM(Hardware, "Bolts")` updates to become `FINDITEM(Hardware, "Bolts")` to return the text match of *Bolts* from the list **Hardware**.

This is only applicable for List. You can't use this two-argument version for Time, such as `ITEM(Time, "Jan 22")`, as FINDITEM isn't supported on Time.

In Polaris, you can't use `ITEM()` for line items that have the **Ratio** summary method. In the Classic Engine, you can.

In Polaris, you can't use this function with a two-argument variant of Time, for example `ITEM(Time, "Feb 10")`. In the Classic Engine, you can.

`ITEM(Products)`

Here, `ITEM()` returns the applicable value for the *Products* list, which is a dimension in the module.

You can use the `ITEM()` function with the [**Formula** summary method](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) for non-composite lists.

- When using `ITEM(``*List*``)` with the **Formula** summary method, then the *List* must be a non-composite list. However, you can use `ITEM()` with the **Formula** summary method for line items that are dimensioned by composite lists.
- The list that you use the `ITEM()` with must be a dimension selected in [**Applies To**](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) in the module.
- You can't use the `ITEM(``*List*``)` with the **Formula** summary method on a composite *List*. This is because the parent list isn't selected in **Applies To**, only the child list.

**Note:** Time is always considered composite in Polaris.

In this example, *Time* is on columns and a *Products* list is on rows. The page dimension contains a line item, which contains the formula `ITEM(Products)`.

|  | **Jan 22** | **Feb 22** | **Mar 22** |
| --- | --- | --- | --- |
| Product 1 | Product 1 | Product 1 | Product 1 |
| Product 2 | Product 2 | Product 2 | Product 2 |
| Product 3 | Product 3 | Product 3 | Product 3 |
| Product 4 | Product 4 | Product 4 | Product 4 |

You can use `ITEM()` with the [IF THEN ELSE](https://help.anaplan.com/9fb6586e-0219-4771-a660-4ebcc317efc0) function to create conditional formulas that change depending upon the applicable list item.

Take for example a module dimensioned by two lists named *Products* and *Organization*. If you require a calculation for a specific product, or products, you can use the formulas as below:

`IF ITEM(Products) = Products.Product 1 THEN (``**Calculation for Product 1**``) ELSE (``**Calculations for other products**``)`

`IF ITEM(Products) = Products.Product 1 OR Products.Product 2 THEN (``**Calculation for Product 1 or Product 2**``) ELSE (``**Calculations for other products**``)`

Additionally, you can specify a calculation that only applies to a specific combination of the *Product* and *Organization* lists by using the [AND](https://help.anaplan.com/f1c2ec15-34af-4ebe-8114-530cf7c9f3bc) operator:

`IF ITEM(Products) = Products.Product 1 AND ITEM(Organization) = Organization.Company 1 THEN (``**Calculation for Product 1 and Company 1**``) ELSE (``**Calculations for other products and companies**``)`

In this example, the *Organization* list is on columns, and the *Class* line item on rows. The *Class* line item has the list data type, and references the *Company Class* list. The *Class* line item uses `ITEM()` to assign certain items in the *Organization* list a different value from the *Company Class* list. The formula used is:

`IF ITEM(Organization) = Organization.'Company 01' OR Organization.'Company 05' THEN Company Class.Class A ELSE IF ITEM(Organization) = Organization.'Company 08' THEN Company Class.Class C ELSE Company Class.Class B`

|  | **Company 01** | **Company 02** | **Company 03** | **Company 04** | **Company 05** | **Company 06** | **Company 07** | **Company 08** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Class | Class A | Class B | Class B | Class B | Class A | Class B | Class B | Class C |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fitem-41298b7a-e877-40e8-8cfa-8d7009d8686f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>