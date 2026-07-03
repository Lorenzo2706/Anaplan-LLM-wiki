---
title: "SELECT | Anapedia"
source: "https://help.anaplan.com/select-2ca3148d-466e-44bd-830e-7e5cf3ac8d08"
author:
published:
created: 2026-05-02
description: "Use the SELECT function to return values from a given list item or time period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the SELECT function to compare values between different [versions](https://help.anaplan.com/19b4391f-5257-40ee-8dfb-36f0ab426c8f).

Never combine SUM and SELECT in the same formula. Create two separate line items. One performing the SUM, and other using the SELECT to reference it.

`Source[SELECT: Target item]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source* | Number, Boolean, date, time period, list, or text | The source module and line item to select a value from. This must be a module line item `module.lineitem`. |
| *Target item* | Time period, list | The item for the SELECT function to return the value from. This should be a `List name.'list item'` or `Time.'time period'`. |

The SELECT function returns a value of the same data type as the *Source* argument.

In Polaris, the reference in SELECT must be literal, rather than an expression, except you can use a literal offset from the current time period, `Time.'Feb 23' + 1`.

In the Classic Engine, SELECT can use expressions. The Classic Engine allows `Time.'Current Period'` in the expression for SELECT, but you can't use any other named Time period in expressions.

`Income Statement.Sales[SELECT: Versions.Actual]`

We don't recommend the use of the SELECT function in conjunction with non-generic time periods. This use of SELECT goes against the sustainable nature of model building, where hard-coded elements can cause issues when updating the timescales of the model.

Use SUM or LOOKUP on modules with Time-formatted items, instead.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fselect-2ca3148d-466e-44bd-830e-7e5cf3ac8d08&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>