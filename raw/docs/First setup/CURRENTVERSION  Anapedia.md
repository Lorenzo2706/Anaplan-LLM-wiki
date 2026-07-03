---
title: "CURRENTVERSION | Anapedia"
source: "https://help.anaplan.com/currentversion-feef413b-7c68-488b-b8a8-b8de0be21146"
author:
published:
created: 2026-05-02
description: "The CURRENTVERSION function returns the value from another line item for the version that is set as Current in a model."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The CURRENTVERSION function returns the value from another line item for the version that is set as **Current** in a model.

For example, you can use the CURRENTVERSION function to compare data between versions.

`CURRENTVERSION(Expression)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Expression* | Number, Boolean, date, time period, list, or text | The expression to return the value from the current version for. |

The CURRENTVERSION function returns a result of the same data type as the *Expression* argument.

`CURRENTVERSION(Net profit)`

In this example, the formula returns the value from the current version for the *Net profit* line item.

- You can only use the CURRENTVERSION function if a version is set as **Current** in [**Versions**](https://help.anaplan.com/19b4391f-5257-40ee-8dfb-36f0ab426c8f) in the model settings bar.

In this example, an income statement module has line items on rows, the *Products* list on columns, and versions on pages. The Budget version displays as a page selector.

The model that contains the module has three versions: Budget, Actual, and Forecast. The Actual version is set as **Current**.

The formula uses the CURRENTVERSION function to show the difference between budget and actual data for *Cost of Goods*.

|  | **Chocolates** | **Sours** | **Taffy** | **Fudge** |
| --- | --- | --- | --- | --- |
| Cost of Goods | 190,000 | 150,000 | 250,000 | 180,000 |
| Cost of Goods (Actual)  `CURRENTVERSION(Cost of Goods)` | 198,000 | 140,433 | 250,670 | 203,005 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcurrentversion-feef413b-7c68-488b-b8a8-b8de0be21146&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>