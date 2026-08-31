---
title: "Line item subsets"
source: "https://help.anaplan.com/line-item-subsets-fd6bfccc-fd3b-4d55-b838-59cdda9c572c"
author:
published:
created: 2026-05-13
description: "A workspace administrator can create a line item subset to generate a list of line items. These can be from the same module or different modules in a model."
tags:
  - "clippings"
---
[Line items](https://help.anaplan.com/line-items-52d76cdd-2571-4400-8f34-b15dd5651b9f "Line items")

A workspace administrator can create a line item subset to generate a list of line items. These can be from the same module or different modules in a model.

You can use line item subsets to:

- Narrow down a large list of line items to a smaller group.
- Group calculations together from different modules.
- Group line items from different modules into one list.

Workspace administrators can set line item subsets as a [dimensions](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a) in any module in the same model. You can also use a line item subset as a [picklist](https://help.anaplan.com/ddeaf549-4699-4e56-be9a-185205c49823) or perform calculations on the line item subset.

If you use the [COLLECT](https://help.anaplan.com/887a0bce-034b-4a0b-9e5f-262ec2f47e35) function in a module that includes a line item subset, `COLLECT()` pulls the line item values into the target module from the source modules.

**Note:** Line item subsets do not have [list properties](https://help.anaplan.com/da73f852-e39f-4046-bf97-675274ce0947).

Some use cases for line item subsets are:

- Currency conversion.
- To apply a percentage growth to last year's income statement.
- To convert invoiced amounts to cash for cash-flow forecasting.

If you have a parent line item in a line item subset, but the subset only includes some of its children, the value of the parent is only calculated from the line items in the line item subset.

For example, the parent line item, *Total Expenses,* has the sum:

`Salary + Bonus + Car Costs + Phone Costs + Medical Costs`

However, the *Expenses* line item subset only contains the *Total Expenses, Salary, Bonus, and Car Costs* line items.

In modules where the line item subset *Expenses* is used as a dimension, *Total Expenses* is then calculated by:

`Salary + Bonus + Car Costs`

If none of the line items in the sum are included in the line item subset, *Total Expenses* appears as a leafitem in the line item subset.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fline-item-subsets-fd6bfccc-fd3b-4d55-b838-59cdda9c572c&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>