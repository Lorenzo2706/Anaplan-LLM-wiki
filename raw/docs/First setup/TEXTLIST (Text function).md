---
title: "TEXTLIST (Text function)"
source: "https://help.anaplan.com/textlist-text-function-c1e24970-400f-43af-95e7-b34a43253cdb"
author:
published:
created: 2026-05-02
description: "The TEXTLIST function concatenates a series of text values into a single text value."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can produce a list of products sold in a given region.

`TEXTLIST(Text to concatenate, Separator, List to reference [, Duplicate behavior])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text to concatenate* (required) | Text line item | An expression that evaluates to a text line item. |
| *Separator* (required) | Text | The text value to use as a separator between each text value concatenated. |
| *List to reference* (required) | List | The list that determines the order in which to concatenate the values from the *Text to concatenate* argument. |
| Duplicate behavior | Keyword | Determines whether duplicated text values should be listed once or multiple times. |

The TEXTLIST function returns a text value.

| **Keyword** | **Description** |
| --- | --- |
| ALL | If the *Text to concatenate* argument contains multiple instances of the same text, each instance is listed in the result.  The default behavior if you omit the *Duplicate behavior* argument. |
| UNIQUE | If the *Text to concatenate* argument contains multiple instances of the same text, only the first instance is listed in the result. |

You cannot use the TEXTLIST calculation function in Polaris.

In the Classic engine, you can.

`TEXTLIST('Regional product sales.Products', ", ", Regions, UNIQUE)`

You can reference the Users list with the TEXTLIST function. However, you cannot reference specific users within the Users list as this is production data, which can change and make your formula invalid.

The TEXTLIST function has a limit of 10,000 characters. This is to prevent the creation of text values that are too large and affect model performance.

If the result of the text function would exceed 10,000 characters, the function stops appending characters and adds an ellipsis (…) to indicate there's more.

[CONCATENATE](https://support.office.com/en-gb/article/CONCATENATE-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d)

This example uses two modules. The first module, *Sales Transactions*, has two line items on columns that contain the customer name and the value of transactions. The *Transactions* list is on rows. The *Regions* list is a page dimension, and London is currently selected.

Region: London

|  | **Customer** | **Transaction Value** |
| --- | --- | --- |
| Transaction 01 |  | 0 |
| Transaction 02 | Fairgreen Furniture Ltd | 20,000 |
| Transaction 03 | Carpenter Oak Ltd | 15,000 |
| Transaction 04 | Carpenter Oak Ltd | 20,000 |
| Transaction 05 | Bluebottle Inc | 5,000 |
| Transaction 06 |  | 0 |
| Transaction 07 | Purple Haze & Co | 2,000 |
| Transaction 08 | Fairgreen Furniture Ltd | 1,000 |
| Transaction 09 | Brass Monkeys Inc | 1,000 |
| Transaction 10 | Purple Marine Stores | 1,000 |
| Transaction 11 |  | 0 |
| Transaction 12 | Purple Marine Stores | 5,000 |

The second module, *List of customers*, has three line items on columns. The *Regions* list is on rows. The London row corresponds to the example above.

The first two line items contain formulas that show a list of customers by region. The formula in the *List of all customers* line item uses the ALL keyword for the *Duplicate behavior* keyword, so it returns duplicated text values multiple times. The formula in the *List of all customers without duplicates* line item uses the UNIQUE keyword for the *Duplicate behavior* keyword, so it does not return duplicated text values.

|  | **List of all customers**  `TEXTLIST(Sales Transactions.Customer, ", ", Transactions, ALL)` | **List of all customers without duplicates**  `TEXTLIST(Sales Transactions.Customer, ", ", Transactions, UNIQUE)` | **Total Transactions Value**  `Sales Transactions.Transaction Value` |
| --- | --- | --- | --- |
| London | Fairgreen Furniture Ltd, Carpenter Oak Ltd, Carpenter Oak Ltd, Bluebottle Inc, Purple Haze & Co, Fairgreen Furniture Ltd, Brass Monkeys Inc, Purple Marine Stores, Purple Marine Stores | Fairgreen Furniture Ltd, Carpenter Oak Ltd, Bluebottle Inc, Purple Haze & Co, Brass Monkeys Inc, Purple Marine Stores | 66,000 |
| Birmingham | Fairgreen Furniture Ltd, Fairgreen Furniture Ltd, Brass Monkeys Inc, Purple Marine Stores | Fairgreen Furniture Ltd, Brass Monkeys Inc, Purple Marine Stores | 110,000 |
| **UK** |  |  | 176,000 |
| Paris | Électricité Berlioz S.A., Amiot S.A | Électricité Berlioz S.A., Amiot S.A | 75,000 |
| Lyon | Dufay S.A., Dufay S.A., Jean Françaix S.A, René Désiré S.A. | Dufay S.A., Jean Françaix S.A, René Désiré S.A. | 104,000 |
| **France** |  |  | 179,000 |
| Munich | Hans-Jürgen GmbH, Von Bose AG | Hans-Jürgen GmbH, Von Bose AG | 58,000 |
| Berlin | Klughardt GmbH, Offenbach AG, Offenbach AG, Telemann GmbH | Klughardt GmbH, Offenbach AG, Telemann GmbH | 202,000 |
| **Germany** |  |  | 260,000 |
| New York | Anderson International Inc., Cummings Industries Inc., Headley Inc., Headley Inc. | Anderson International Inc., Cummings Industries Inc., Headley Inc. | 200,000 |
| Los Angeles | Kennedy Inc, ABC Inc | Kennedy Inc, ABC Inc | 20,000 |
| **USA** |  |  | 220,000 |
| **Total Company** |  |  | 835,000 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftextlist-text-function-c1e24970-400f-43af-95e7-b34a43253cdb&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>