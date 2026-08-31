---
title: "TEXTLIST (Aggregation function)"
source: "https://help.anaplan.com/textlist-aggregation-function-2da1f1a6-6f7d-42fb-b9dd-54dd057c2440"
author:
published:
created: 2026-05-02
description: "The TEXTLIST aggregation function returns a collection of text values as a comma-separated value. The values returned are based on mapping from a source module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The TEXTLIST aggregation function returns a collection of text values as a comma-separated value. The values returned are based on mapping from a source module.

For example, you can use the TEXTLIST function to return a list of customers for each region.

`Values to list[TEXTLIST: Mapping, TEXTLIST: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Values to list* | Text | The values to return as comma-separated text values based on the *Mapping* argument. |
| *Mapping* | List, date, time period | The mapping that determines which values to return as comma-separated text values.  Each instance of this argument must be a dimension present in the *Values to sum* argument.  This argument can be repeated to provide multiple mappings. |

The TEXTLIST function returns a text result. The result line item must share all dimensions used for the *Mapping* argument.

You cannot use the TEXTLIST aggregation function in Polaris.

In the Classic engine, you can.

`Customer Sales.Product Text[TEXTLIST: Customer Sales.Customers, TEXTLIST: Customer Sales.Sales Period]`

In this example, each text value from the *Product Text* line item is returned as a comma separated value for each unique combination of *Customer* and *Sales Period*.

You can reference the Users list with the TEXTLIST function. However, you cannot reference specific users within the Users list as this is [production data](https://help.anaplan.com/d129b0e3-34f7-4135-b27e-5956ed56e8d2), which can change and make your formula invalid.

The dimensions of the *Mapping* argument must also be dimensions of the *Values to list* argument.

The TEXTLIST aggregation function can only be used with values of the text data type. If you need to list values with the list data type, you can use the [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d) function to convert list values to text.

The TEXTLIST aggregation function returns duplicates if a text value occurs more than once in the cells chosen through the *Mapping* argument. The [TEXTLIST](https://help.anaplan.com/c1e24970-400f-43af-95e7-b34a43253cdb) calculation function enables you to only return each text value once, or to change the separator between text values.

The TEXTLIST aggregation function has a built in limit of 10,000 characters to prevent enormous text strings being created. At 10,000 characters, TEXTLIST stops appending to the list and adds an ellipsis that indicates more items. The ellipsis is after the 10,000 character limit, not included within it. The TEXTLIST function may truncate the final word listed if it exceeds 10,000 characters.

[CONCATENATE](https://support.office.com/en-gb/article/CONCATENATE-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d)

The module below is the *Transactions* module, which contains the data that the other examples aggregate. In this module, the *Transactions* list is on rows. Several line items are on columns, which contain:

- A text value of the product sold
- A list value for the customer sold to
- A time period value for when the transaction occurred

|  | **Product Text** | **Customer** | **Date** |
| --- | --- | --- | --- |
| Transaction 01 | Apples | Customer A | Jan 21 |
| Transaction 02 | Bananas | Customer B | Jan 21 |
| Transaction 03 | Grapefruit | Customer A | Jan 21 |
| Transaction 04 | Oranges | Customer C | Feb 21 |
| Transaction 05 | Apples | Customer D | Mar 21 |
| Transaction 06 | Grapefruit | Customer B | Mar 21 |
| Transaction 07 | Oranges | Customer B | Apr 21 |
| Transaction 08 | Bananas | Customer C | Apr 21 |
| Transaction 09 | Grapefruit | Customer A | May 21 |
| Transaction 10 | Oranges | Customer B | Jul 21 |
| Transaction 11 | Bananas | Customer A | Jul 21 |
| Transaction 12 | Oranges | Customer A | Aug 21 |
| Transaction 13 | Bananas | Customer D | Sep 21 |
| Transaction 14 | Apples | Customer B | Sep 21 |
| Transaction 15 | Grapefruit | Customer D | Oct 21 |
| Transaction 16 | Apples | Customer D | Oct 21 |
| Transaction 17 | Oranges | Customer C | Nov 21 |
| Transaction 18 | Grapefruit | Customer C | Nov 21 |
| Transaction 19 | Apples | Customer C | Dec 21 |
| Transaction 20 | Bananas | Customer D | Dec 21 |

In this example, the *Customer* list is on columns. On rows, a line item contains a formula that uses TEXTLIST to list each product sold to each customer.

|  | **Customer A** | **Customer B** | **Customer C** | **Customer D** |
| --- | --- | --- | --- | --- |
| Products sold by customer  `Transactions.Product Text[TEXTLIST: Transactions.Customer]` | Apples, Grapefruit, Grapefruit, Bananas, Oranges | Bananas, Grapefruit, Oranges, Oranges, Apples | Oranges, Bananas, Oranges, Grapefruit, Apples | Apples, Bananas, Grapefruit, Apples, Bananas |

In this example, the *Time* is on columns. On rows, a line item contains a formula that uses TEXTLIST to list each product sold in each time period.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** | **May 21** | **Jul 21** | **Aug 21** | **Sep 21** | **Oct 21** | **Nov 21** | **Dec 21** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Products sold in period  `Transactions. Product Text[TEXTLIST: Transactions.Date]` | Apples, Bananas, Grapefruit | Oranges | Apples, Grapefruit | Oranges, Bananas | Grapefruit | Oranges, Bananas | Oranges | Bananas, Apples | Grapefruit, Apples | Oranges, Grapefruit | Apples, Bananas |

In this example, the *Customer* list is on columns, and *Time* on rows.

Line items are on pages, and the selected line item contains this formula:

`Transactions.Product Text[TEXTLIST:Transactions.Customer, TEXTLIST: Transactions.Date]`

The formula lists the products sold for each combination of customer and time period.

|  | **Customer A** | **Customer B** | **Customer C** | **Customer D** |
| --- | --- | --- | --- | --- |
| Jan 21 | Apples, Grapefruit | Bananas |  |  |
| Feb 21 |  |  | Oranges |  |
| Mar 21 |  | Grapefruit |  | Apples |
| Apr 21 |  | Oranges | Bananas |  |
| May 21 | Grapefruit |  |  |  |
| Jul 21 | Bananas | Oranges |  |  |
| Aug 21 | Oranges |  |  |  |
| Sep 21 |  | Apples |  | Bananas |
| Oct 21 |  |  |  | Grapefruit, Apples |
| Nov 21 |  |  | Oranges, Grapefruit |  |
| Dec 21 |  |  | Apples | Bananas |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftextlist-aggregation-function-2da1f1a6-6f7d-42fb-b9dd-54dd057c2440&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>