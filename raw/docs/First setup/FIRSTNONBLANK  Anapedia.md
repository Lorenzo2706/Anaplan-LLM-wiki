---
title: "FIRSTNONBLANK | Anapedia"
source: "https://help.anaplan.com/firstnonblank-125738aa-c067-4602-b5bb-da6f4dfe940c"
author:
published:
created: 2026-05-02
description: "The aggregation function FIRSTNONBLANK returns the first value of a line item found for a given list item or time period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The aggregation function FIRSTNONBLANK returns the first value of a line item found for a given list item or time period.

This function is useful if you want to show the first non-blank record in a list of products sold to each customer.

`Line item to search [FIRSTNONBLANK: Mapping, FIRSTNONBLANK: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Values to search* | Date, time period, list, text | The value to search for the first occurrence of. |
| *Mapping* | Date, time period, list | The mapping that determines which values to find the first non-blank value for.  Each instance of this argument must be a dimension present in the *Values to sum* argument.  This argument can be repeated to provide multiple mappings. |

The FIRSTNONBLANK function returns a value that matches the type of *Value to search* argument. The line item that contains the FIRSTNONBLANK function must be dimensioned by all dimensions used for the *Mapping* argument.

You cannot use the FIRSTNONBLANK aggregation function in Polaris.

In the Classic engine, you can.

**First non-blank** can also be used as a [summary method](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936). You can use the summary method on date-, time period-, list-, and text-formatted line items.

In **Blueprint**, scroll right to the **Summary** column and select the method as *First non-blank*.

The FIRSTNONBLANK function and the summary method checks for values in the order of list items as they occur in **General lists**. If you hide values in a module or if the list items have parent items that change the order they display in, the order of the list items will change and this might impact the outcome of FIRSTNONBLANK.

You can reference the Users list with the FIRSTNONBLANK function. However, you can't reference specific users within the Users list as this is production data, which can change and make your formula invalid.

The dimensions of the *Mapping* argument must also be dimensions of the *Values to search* argument.

In the *Source Customers* module below, *Product text* is text-formatted and *Customers* is list-formatted.

| **Source Customers** | **Product Text** | **Customers** | **Date** | **Value** |
| --- | --- | --- | --- | --- |
| 1 |  | Customer A | 01/04/2015 | 1000 |
| 2 | Bananas | Customer A |  | 900 |
| 3 | Grapefruit | Customer B | 15/05/2015 | 1200 |
| 4 | Oranges | Customer B | 19/05/2015 | 1000 |
| 5 | Apples | Customer A | 20/05/2015 | 1000 |
| 6 | Grapefruit | Customer B |  | 1200 |
| 7 | Oranges | Customer B | 26/05/2015 | 800 |
| 8 | Bananas | Customer B | 28/05/2015 | 900 |
| 9 |  | Customer A | 29/05/2015 | 900 |
| 10 | Oranges | Customer B | 30/05/2015 | 1000 |

The *Customer Summary* results module below, holds the results of FIRSTNONBLANK. The *FIRSTNONBLANK Product* result line item is text-formatted. The *FIRSTNONBLANK Date* result line item is date-formatted.

| **Customer Summary** | **Customer A** | **Customer B** |
| --- | --- | --- |
| FIRSTNONBLANK Product  `Source Customers.Product Text[FIRSTNONBLANK: Source Customers.Customers]` | Bananas | Grapefruit |
| FIRSTNONBLANK Date  `Source Customers.Date[FIRSTNONBLANK: Source Customers.Customers]` | 01/04/2015 | 15/05/2015 |

The **First non-blank** summary method behaves in a similar way to the FIRSTNONBLANK function. In the table below, the **First non-blank** [summary method](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) is applied to *Product Text, Customers,* and *Date.* The result displays in the *Total* row.

| **Source Customers** | **Product Text** | **Customers** | **Date** |
| --- | --- | --- | --- |
| 1 |  | Customer A | 01/04/2015 |
| 2 | Bananas | Customer A |  |
| 3 | Grapefruit | Customer B | 15/05/2015 |
| 4 | Oranges | Customer B | 19/05/2015 |
| 5 | Apples | Customer A | 20/05/2015 |
| 6 | Grapefruit | Customer B |  |
| 7 | Oranges | Customer B | 26/05/2015 |
| 8 | Bananas | Customer B | 28/05/2015 |
| 9 |  | Customer A | 29/05/2015 |
| 10 | Oranges | Customer B | 30/05/2015 |
| Total | Bananas | Customer A | 01/04/2015 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ffirstnonblank-125738aa-c067-4602-b5bb-da6f4dfe940c&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>