---
title: "PREVIOUSVERSION | Anapedia"
source: "https://help.anaplan.com/previousversion-b0fd3276-e78e-4219-ae2e-22d00635afc0"
author:
published:
created: 2026-05-02
description: "The PREVIOUSVERSION function evaluates the given expression using the previous version."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the PREVIOUSVERSION function to make comparisons between data from different versions of a plan.

`PREVIOUSVERSION(Expression)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Expression* | Number, Boolean, date, time period, list, or text | The expression to return the value from the previous version for. |

The PREVIOUSVERSION function returns a result of the same format as the *Expression* argument.

`PREVIOUSVERSION(Bonus)`

In this example, the formula returns the value from the previous version of the *Bonus* line item.

The order of versions is from top to bottom in **Versions** in the model settings bar.

For example, if your model's versions are ordered Budget, Actual, and Forecast, the previous version of Actual is Budget.

The result cell that you use the PREVIOUSVERSION function in must use Versions as a dimension.

In this example, an income statement module has line items on rows, time on columns, and versions on pages. The model has three versions: Budget, Actual, and Forecast, in that order. The page selector is set to the Actual version.

The formula in the *Budget Cost of Goods* line item uses the PREVIOUSVERSION function to retrieve the value of *Cost of Goods* from the previous version.

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Cost of Goods | 198,734 | 236,761 | 200,459 |
| Goods Sold | 456,987 | 498,705 | 460,983 |
| Budget Cost of Goods  `PREVIOUSVERSION(Cost of Goods)` | 200,000 | 245,000 | 205,000 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpreviousversion-b0fd3276-e78e-4219-ae2e-22d00635afc0&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>