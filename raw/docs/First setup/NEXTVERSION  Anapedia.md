---
title: "NEXTVERSION | Anapedia"
source: "https://help.anaplan.com/nextversion-ba1aacd7-b7c4-4808-b94f-98b68152b2aa"
author:
published:
created: 2026-05-02
description: "The NEXTVERSION function evaluates the given expression using the next version."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the NEXTVERSION function to make comparisons between data from different versions of a plan.

`NEXTVERSION(Expression)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Expression | Number, Boolean, date, time period, list, or text | The expression to return the value from the next version for. |

The NEXTVERSION function returns a result of the same data type as the *Expression* argument.

`NEXTVERSION(Operating costs)`

In this example, the formula returns the value from the next version of the *Operating costs* line item.

The order of versions is from top to bottom in **Versions** in the model settings bar.

For example, if your model's versions are ordered Budget, Actual, and Forecast, the next version of Actual is Forecast. If there is no next version, the function returns a blank value or 0.

The result cell that you use the NEXTVERSION function in must use Versions as a dimension.

In this example, an income statement module has line items on rows, time on columns, and versions on pages. The model has three versions: Budget, Actual, and Forecast, in that order. The page selector is set to the Actual version.

The formula in the *Forecast Revenue Costs* line item uses the NEXTVERSION function to retrieve the value of *Revenue Costs* from the Forecast version, which is the next version.

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Revenue Costs | 12,457 | 13,987 | 13,483 |
| Salary Costs | 27,950 | 28,000 | 22,765 |
| Forecast Revenue Costs  `NEXTVERSION(Forecast Revenue Costs)` | 15,000 | 15,500 | 16,000 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fnextversion-ba1aacd7-b7c4-4808-b94f-98b68152b2aa&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>