---
title: "Line items"
source: "https://help.anaplan.com/line-items-52d76cdd-2571-4400-8f34-b15dd5651b9f"
author:
published:
created: 2026-05-13
description: "Model builders create line items to measure data in a module. Use line items to input data, hold formulas, and run calculations. Line items can have different data types, such as number, date, Boolean, and list."
tags:
  - "clippings"
---
Model builders create line items to measure data in a module. Use line items to input data, hold formulas, and run calculations. Line items can have different data types, such as number, date, Boolean, and list.

For example, the *Employee expenses* module includes the *Start date, Leave date, Salary, Bonus, and Headcount* line items. The *Margin calculation* module includes the *Revenue, Cost of sales, Margin %, and Unit price growth %* line items.

You typically use line items to:

You can also use line items as [picklists](https://help.anaplan.com/ddeaf549-4699-4e56-be9a-185205c49823), and as headings in a module, so you can organize large numbers of line items.

Line items are different to list items in [lists](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075). Line items:

- Can contain formulas, and can be referenced by a formula. List items can only be referenced by a formula.
- Belong to only one module. List items can be used in any module.

To view and manage your line items, select **Modules** in the model settings bar, then select **Line Items**. If you want to [configure line items](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) in a module, open the module in Blueprint. Each line item displays in the column on the left.

You can reference line items in a formula in either the same module, or in other modules, within the same model. Not all line items contain formulas.

For example, the *REV03 Margin Calculation* module contains the *Revenue*, *Cost of Sales*, *Margin*, *Margin %*, *Unit Price Growth %,* and *Unit Cost Growth %* line items. Each line item has a number data type, and contains a formula that calculates the value of the cells.

You can calculate data in the *Revenue* line item by referencing *Volumes* from the *REV02 Volume Inputs* module, and *Unit Price* from the *REV01 Price Book* module in a formula. For example:  
  
`'REV02 Volume Inputs'.Volumes * 'REV01 Price Book'.Unit Price * (1 + Unit Price Growth %)`

You can also calculate data in the *Margin* line item by referencing other line items in the same module in a formula. For example:

`Revenue - Cost of Sales`

You can also create [line item subsets](https://help.anaplan.com/fd6bfccc-fd3b-4d55-b838-59cdda9c572c). Line item subsets are collections of line items from the same or different modules in the same model.

Use line item subsets to narrow down a large list of line items to a smaller group, or to group calculations from different modules. You can use a line item subset as a [dimension](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a) in a module.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fline-items-52d76cdd-2571-4400-8f34-b15dd5651b9f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>