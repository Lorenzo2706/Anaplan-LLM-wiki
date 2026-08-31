---
title: "SUM | Anapedia"
source: "https://help.anaplan.com/sum-fa7ab44f-c31c-4928-88b3-9fe28ca8a774"
author:
published:
created: 2026-05-02
description: "The SUM aggregation function sums values in a result module based on mapping from a source module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Never use SUM and LOOKUP in the same formula. This can lead to extremely long calculation times. For more information, see [Formulas and their effects on model performance](https://community.anaplan.com/t5/Best-Practices/Formulas-and-their-effect-on-model-performance/ta-p/33556) .

The SUM aggregation function sums values in a result module based on mapping from a source module.

For example, you can use the SUM function to sum revenue across several product categories.

`Values to sum[SUM: Mapping, SUM: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Values to sum* | Number | The values to sum based on the *Mapping* argument. |
| *Mapping* | List, date, time period | The mapping that determines which values to sum.  Each instance of this argument must be a dimension present in the *Values to sum* argument.  This argument can be repeated to provide multiple mappings. |

The SUM function returns a numeric result. The line item that contains the SUM function must be dimensioned by all dimensions used for the *Mapping* argument.

`'Employee Expenses'.Salary[SUM:'Employee Details'.Region, SUM: 'Employee Details'.Role]`

In this example, the values from the *Salary* line item are summed for each employee role and region.

SUM can also be used as a [summary method](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936). You can use the summary method on line items with the number data type.

You can use the SUM function to pull data from one module into another. However, the SUM function only works with number values. If you need to do this for other data types, such as Boolean or text, use a different aggregation function.

To determine whether to use SUM or [LOOKUP](https://help.anaplan.com/f8baa402-606d-4764-a349-d8003fa383be), see [Formula usage tips](https://help.anaplan.com/89bd50bd-dbbf-4465-b085-36163aa74450).

You can reference the Users list with the SUM function. However, you cannot reference specific users within the Users list as this is production data, which can change and make your formula invalid.

The dimensions of the *Mapping* argument must also be dimensions of the *Values to sum* argument.

[SUMIF](https://support.microsoft.com/en-gb/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b)

In these examples, there are several modules.

The first is a *Transactions Module*. In this module, the *Transactions* list displays on rows. Several line items that contain information about each transaction display on columns:

- *Product* line item, which has the list data type with the *Products* list. Displays the product that each transaction relates to.
- *Region*, which has the list data type with the *Organization* list. Displays the location of the sale for each transaction.
- *Sale value*, which contains the numeric value of each transaction.
- *Sale date*, which contains the date of each transaction.

|  | **Product** | **Region** | **Sale value** | **Sale date** |
| --- | --- | --- | --- | --- |
| Transaction 01 | Apples | London | $ 10,000.00 | 1/23/2020 |
| Transaction 02 | Bananas | Birmingham | $ 5,000.00 | 2/15/2020 |
| Transaction 03 | Pears | London | $ 6,000.00 | 4/1/2020 |
| Transaction 04 | Pears | Birmingham | $ 4,000.00 | 5/15/2020 |
| Transaction 05 | Apples | Paris | $ 4,500.00 | 5/19/2020 |
| Transaction 06 | Carrots | Munich | $ 7,000.00 | 5/20/2020 |
| Transaction 07 | Lettuce | Berlin | $ 11,000.00 | 5/26/2020 |
| Transaction 08 | Bananas | London | $ 12,000.00 | 5/28/2020 |
| Transaction 09 | Apples | London | $ 6,500.00 | 5/29/2020 |
| Transaction 10 | Cucumbers | Lyon | $ 2,000.00 | 5/30/2020 |
| Transaction 11 | Carrots | Paris | $ 1,000.00 | 3/4/2021 |
| Transaction 12 | Carrots | Berlin | $ 3,500.00 | 3/20/2021 |
| Transaction 13 | Bananas | Birmingham | $ 8,000.00 | 4/1/2021 |
| Transaction 14 | Apples | London | $ 9,500.00 | 6/15/2021 |
| Transaction 15 | Peaches | Munich | $ 5,000.00 | 6/28/2021 |
| Transaction 16 | Pears | Munich | $ 7,000.00 | 7/7/2021 |
| Transaction 17 | Lettuce | Berlin | $ 12,000.00 | 8/11/2021 |
| Transaction 18 | Cucumbers | Lyon | $ 3,000.00 | 9/22/2021 |
| Transaction 19 | Bananas | Paris | $ 1,500.00 | 9/30/2021 |
| Transaction 20 | Apples | London | $ 9,500.00 | 10/1/2021 |

The *Transactions Module* is used as the source for each of the examples below.

This example uses the SUM function to sum values from the *Transactions Module* for each region.

The formula used for the *Total Sales* line item is:

`Transactions Module.Sale value[SUM:Transactions Module.Region]`

|  | **London** | **Birmingham** | **UK** | **Paris** | **Lyon** | **France** | **Munich** | **Berlin** | **Germany** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total Sales | $ 53,500.00 | $ 17,000.00 | $ 70,500.00 | $ 7,000.00 | $ 5,000.00 | $ 12,000.00 | $ 19,000.00 | $ 26,500.00 | $ 45,500.00 | $ 128,000.00 |

This example uses the SUM function to sum values for each combination of product and region. The page dimension is line items, which displays the *Sales* line item. On rows, the *Products* list displays, and on columns, the *Region* list displays.

The formula used for the *Sales* line item is:

`Transactions Module.Sale value[SUM:Transactions Module.Product, SUM:Transactions Module.Region]`

|  | **London** | **Birmingham** | **UK** | **Paris** | **Lyon** | **France** | **Munich** | **Berlin** | **Germany** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Apples | $ 35,000.00 | 0 | $ 35,500.00 | $ 4,500.00 | 0 | $ 4,500.00 | 0 | 0 | 0 | $ 40,000.00 |
| Peaches | 0 | 0 | 0 | 0 | 0 | 0 | $ 12,000.00 | 0 | 0 | $ 12,000.00 |
| Bananas | $ 12,000.00 | $ 13,000.00 | $25,000.00 | $ 1,500.00 | 0 | $ 1,500.00 | 0 | 0 | 0 | $ 26,500.00 |
| Pears | $ 6,000.00 | $ 4,000.00 | $ 10,000.00 | 0 | 0 | 0 | 0 | 0 | 0 | $ 10,000.00 |
| **Fruits** | $ 53,500.00 | $ 17,000.00 | $ 70,500.00 | $ 6,000.00 | 0 | $ 6,000.00 | $ 12,000.00 | 0 | $ 12,000.00 | $ 88,500.00 |
| Carrots | 0 | 0 | 0 | $ 1,000.00 | 0 | $ 1,000.00 | $ 7,000.00 | $ 3,500.00 | $ 10,500.00 | $ 11,500.00 |
| Cucumbers | 0 | 0 | 0 | 0 | $ 5,000.00 | $ 5,000.00 | 0 | 0 | 0 | $ 5,000.00 |
| Lettuce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | $ 23,000.00 | $ 23,000.00 | $ 23,500.00 |
| **Vegetables** | 0 | 0 | 0 | $ 1,000.00 | $ 5,000.00 | $ 6,000.00 | $ 7,000.00 | $ 26,500.00 | $ 33,500.00 | $ 39,500.00 |
| **Total Products** | $ 53,500.00 | $17,000.00 | $ 70,500.00 | $ 7,000.00 | $ 5,000.00 | $ 12,000.00 | $ 19,000.00 | $ 26,500.00 | $ 45,500.00 | $ 128,000.00 |

This example uses the SUM function to sum values for each combination of product, region, and time. The page dimensions are line items and time. The *Sales* line item and *FY20* are selected in the context selectors. This means that only sales that took place in 2020 display in this table.

On rows, the *Products* list displays, and on columns, the *Region* list displays.

The formula used for the *Sales* line item is:

`Transactions Module.Sales[SUM:Transactions Module.Product, SUM:Transactions Module.Region, SUM: Transactions Module.Sale date]`

|  | **London** | **Birmingham** | **UK** | **Paris** | **Lyon** | **France** | **Munich** | **Berlin** | **Germany** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Apples | $ 16,500.00 | 0 | $ 16,500.00 | $ 4,500.00 | 0 | $ 4,500.00 | 0 | 0 | 0 | $ 21,000.00 |
| Peaches | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Bananas | $ 12,000.00 | $ 5,000.00 | $17,000.00 | 0 | 0 | 0 | 0 | 0 | 0 | $ 17,000.00 |
| Pears | $ 6,000.00 | $ 4,000.00 | $ 10,000.00 | 0 | 0 | 0 | 0 | 0 | 0 | $ 10,000.00 |
| **Fruits** | $ 34,500.00 | $ 9,000.00 | $ 43,500.00 | $ 4,500.00 | 0 | $ 4,500.00 | 0 | 0 | 0 | $ 48,000.00 |
| Carrots | 0 | 0 | 0 | 0 | 0 | 0 | $ 7,000.00 | 0 | $ 7,000.00 | $ 7,000.00 |
| Cucumbers | 0 | 0 | 0 | 0 | $ 2,000.00 | $ 2,000.00 | 0 | 0 | 0 | $ 2,000.00 |
| Lettuce | 0 | 0 | 0 | 0 | 0 | 0 | 0 | $ 11,000.00 | $ 11,000.00 | $ 11,000.00 |
| **Vegetables** | 0 | 0 | 0 | 0 | $ 2,000.00 | $ 2,000.00 | $ 7,000.00 | $ 11,000.00 | $ 18,000.00 | $ 20,000.00 |
| **Total Products** | $ 34,500.00 | $9,000.00 | $ 43,500.00 | $ 4,500.00 | $ 2,000.00 | $ 6,500.00 | $ 7,000.00 | $ 11,000.00 | $ 18,000.00 | $ 68,000.00 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fsum-fa7ab44f-c31c-4928-88b3-9fe28ca8a774&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>