---
title: "ISANCESTOR | Anapedia"
source: "https://help.anaplan.com/isancestor-2c35cf1b-9392-4726-8ebb-4291d1b24225"
author:
published:
created: 2026-05-02
description: "The ISANCESTOR function takes two list or time period values. It returns TRUE if the first is an ancestor of the second. Ancestors are an item's parent, parent's parent, and so on."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ISANCESTOR function takes two list or time period values. It returns TRUE if the first is an ancestor of the second. Ancestors are an item's parent, parent's parent, and so on.

`ISANCESTOR(Ancestor, Descendant)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Ancestor* | List, time period | The value to test whether it is an ancestor of the *Descendant* argument. |
| *Descendant* | List, time period | The value to test whether it is a descendant of the *Ancestor* argument. |

The ISANCESTOR function returns a Boolean result.

In Polaris, the ISANCESTOR function returns FALSE when given a top-level item coupled with an orphan entity.

In the Classic Engine, this returns TRUE*.*

In this example, a module has the *Products* list on columns, and the following line items on rows:

- *Product*, a **List** data type on the *Products* list
- *Is Fruits parent?*, a **Boolean** data type
- *Is Vegetables parent?*, a **Boolean** data type
- *Is Fresh produce parent?*, a **Boolean** data type

The *Products* list is a hierarchical list. Within this list, *Fresh produce* are the parents of *Fruits* and *Vegetables*.

Following is the *Products* list as displayed under **Grid View**.

|  | **Parent** | **Code** |
| --- | --- | --- |
| Apple | Fruits |  |
| Orange | Fruits |  |
| Banana | Fruits |  |
| **Fruits** | Fresh produce |  |
| Carrot | Vegetables |  |
| Beetroot | Vegetables |  |
| Broccoli | Vegetables |  |
| **Vegetables** | Fresh produce |  |
| **Fresh produce** |  |  |

|  | **Apple** | **Orange** | **Banana** | **Fruits** | **Carrot** | **Beetroot** | **Broccoli** | **Vegetables** | **Fresh produce** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Product**  `ITEM(Products list)` | Apple | Orange | Banana |  | Carrot | Beetroot | Broccoli |  |  |
| **Is Fruits parent?**  `ISANCESTOR(Products list.Fruits, Product)` |  |  |  |  |  |  |  |  |  |
| **Is Vegetables parent?**  `ISANCESTOR(Products list.Vegetables, Product)` |  |  |  |  |  |  |  |  |  |
| **Is Fresh produce parent?**  `ISANCESTOR(Products list.Fresh produce, Product)` |  |  |  |  |  |  |  |  |  |

The first line item, *Product*, returns each product within the *Products* list. Three further line items use the `ISANCESTOR()` formula to check whether these products are part of *Fruits*, *Vegetables*, or *Fresh products*, respectively.

In this example, a module has the *Organization* list on columns and line items on rows.

The *Organization* list is a hierarchical list with a top level of company. Within this list, regions are the parents of countries, and countries are the parents of cities.

The first line item, *City*, uses the ITEM function to return each location within the *Organization* list. Three further line items use the ISANCESTOR function to check whether these cities are part of the UK, France, or the EMEA region, respectively.

|  | **London** | **Birmingham** | **Paris** | **Lyon** | **New York** | **Los Angeles** |
| --- | --- | --- | --- | --- | --- | --- |
| **City** | London | Birmingham | Paris | Lyon | New York | Los Angeles |
| **Part of UK?**  `ISANCESTOR(Organization.UK, City)` |  |  |  |  |  |  |
| **Part of France?**  `ISANCESTOR(Organization.France, City)` |  |  |  |  |  |  |
| **Part of EMEA?**  `ISANCESTOR(Organization.EMEA, City)` |  |  |  |  |  |  |

In this example, the *Dates* list is on columns, and line items on rows. The *Chosen Month* and *Chosen Quarter* line items have the time period data type. The *Quarter is Ancestor?* has the Boolean data type and uses the ISANCESTOR function. This returns a Boolean value of TRUE if the value of *Chosen Quarter* is an ancestor of *Chosen Month*.

The final line item, *Within Q3?*, uses a direct reference to the time period of Q3 FY22 and checks whether it's the ancestor of *Chosen Month*.

|  | **Key** **Dates** | **Expiry Dates** |
| --- | --- | --- |
| **Chosen Month** | Feb 2022 | Jul 2022 |
| **Chosen Quarter** | Q1 FY22 | Q1 FY22 |
| **Quarter is Ancestor?**  `ISANCESTOR(Chosen Quarter, Chosen Month)` |  |  |
| **Chosen Month Within Q3 FY22?**  `ISANCESTOR(Time.'Q3 FY22', Chosen Month)` |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fisancestor-2c35cf1b-9392-4726-8ebb-4291d1b24225&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>