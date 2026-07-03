---
title: "ISFIRSTOCCURRENCE | Anapedia"
source: "https://help.anaplan.com/isfirstoccurrence-f3a4e998-fda4-42e5-aa48-05bcf6afd852"
author:
published:
created: 2026-05-02
description: "The ISFIRSTOCCURRENCE function returns a Boolean value of TRUE for the first occurrence of a value in a list dimension."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ISFIRSTOCCURRENCE function returns a Boolean value of TRUE for the first occurrence of a value in a list dimension.

For example, you can use ISFIRSTOCCURRENCE to prevent duplicates when creating lists from data.

`ISFIRSTOCCURRENCE(Values to compare, List dimension to search)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Values to compare* | Number, Boolean, date, time period, list, or text | The values to search for the first occurrences of. |
| *List dimension to search* | List | The list to search along for the first occurrences of the *Values to compare* argument.  Must be a dimension of the target line item. |

The ISFIRSTOCCURRENCE function returns a Boolean result.

In Polaris, you can use the ISFIRSTOCCURRENCE function with the Time list. In the Classic Engine, you can't.

Additionally, in Polaris, the ISFIRSTOCCURRENCE function doesn't have a 50 million cell limit as it does in the Classic Engine.

In Polaris, the dimension argument must match one of the dimensions of the target line item. For example, you cannot use a subset of a list as a dimension argument. In the Classic Engine, this is not the case.

**Note:** Performance of ISFIRSTOCCURRENCE is known to be poor in Polaris for models with high dimensionality. We strongly advise you to avoid ISFIRSTOCCURRENCE in Polaris.

`ISFIRSTOCCURRENCE(Product, Contracts)`

You can reference the **Users** list with the ISFIRSTOCCURRENCE function. However, you can't reference specific users within the **Users** list as this is [production data](https://help.anaplan.com/d129b0e3-34f7-4135-b27e-5956ed56e8d2). This data can change and make your formula invalid.

The ISFIRSTOCCURRENCE function references the order of the leaf list as seen in **General Lists**, not the parent list. This means that the first occurrence of an item may not be the first that displays in a list within a module. You can change the order of lists with the [**Order List**](https://help.anaplan.com/22a2640b-8e60-4732-9d7b-10660c463023) action.

An artificial limit is imposed to prevent the searching of large data sets that would slow down the server. This limit is set at 50 million cells. If more than 50 million cells are used with the ISFIRSTOCCURRENCE function, the model rolls back and a notification displays.

The 50 million cell limit doesn't account for [summarized values](https://help.anaplan.com/anapedia/Content/Modeling/Build%20Models/Summary_Methods.html) or the **Time** and **Versions** lists. This means you can use the ISFIRSTOCCURRENCE function with a line item with a **Cell Count** of greater than 50 million cells if there are less than 50 million nonsummarized cells.

As the number of cells you use with the ISFIRSTOCCURRENCE function increases, so does the duration of the calculation.

This example has a list *Shipments* on rows, and the following line items on columns:

- *Product*, a **List** data type on the *Products* list
- *Shipment date*, a **Date** date type
- *Is first shipment?*, a **Boolean** data type

The line item, *Is first shipment?* contains the `ISFIRSTOCCURRENCE()` formula, which checks each shipment's product and flags the first shipment for that product as TRUE. All later shipments of the same product are FALSE.

|  | **Product** | **Shipment date** | **Is first shipment?   **`ISFIRSTOCCURRENCE(Product, Shipments)` |
| --- | --- | --- | --- |
| **S1** | Apple | 01/06/2025 |  |
| **S2** | Banana | 01/05/2025 |  |
| **S3** | Apple | 08/06/2025 |  |
| **S4** | Apple | 19/06/2025 |  |
| **S5** | Orange | 22/05/2025 |  |
| **S6** | Banana | 12/06/2025 |  |

In this example, a *Contracts* list displays on rows, and line items on columns. The line items contain information about each contract, and the *Is first occurrence?* line item uses the ISFIRSTOCCURRENCE function to identify the first contract for each product.

|  | **Product** | **Transaction amount** | **Is first occurrence?   **`ISFIRSTOCCURRENCE(Product, Contracts)` |
| --- | --- | --- | --- |
| Contract 1 | Peaches | 1,216.40 |  |
| Contract 2 | Peaches | 864.20 |  |
| Contract 3 | Peaches | 2.165.60 |  |
| Contract 4 | Bananas | 3,485.00 |  |
| Contract 5 | Bananas | 1.692.10 |  |
| Contract 6 | Peaches | 1,451.20 |  |

The *Values to compare* argument can be any valid expression. In this example, a Transactions list displays on rows, and line items on columns.

Each transaction has a fee subtracted from it. The ISFIRSTOCCURRENCE function is used to identify the first occurrence of each value after subtraction.

|  | **Transaction value** | **Transaction fee** | **First occurrence of transaction value   **`ISFIRSTOCCURRENCE(('Transaction value' - 'Transaction fee'), Transactions)` |
| --- | --- | --- | --- |
| Transaction 1 | 1,000 | 25 |  |
| Transaction 2 | 1,100 | 125 |  |
| Transaction 3 | 500 | 10 |  |
| Transaction 4 | 550 | 60 |  |
| Transaction 5 | 1,050 | 75 |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fisfirstoccurrence-f3a4e998-fda4-42e5-aa48-05bcf6afd852&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>