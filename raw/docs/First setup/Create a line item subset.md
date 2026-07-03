---
title: "Create a line item subset"
source: "https://help.anaplan.com/create-a-line-item-subset-30e5ac9c-0348-4bd4-8dd2-76855b8b8684"
author:
published:
created: 2026-05-13
description: "Model builders create line items subsets to narrow down large lists of line items, and to collect line items from different modules in one place. For example, you can group calculations from different modules into one list."
tags:
  - "clippings"
---
Model builders create line items subsets to narrow down large lists of line items, and to collect line items from different modules in one place. For example, you can group calculations from different modules into one list.

Create any [line items](https://help.anaplan.com/52d76cdd-2571-4400-8f34-b15dd5651b9f) you need in **Modules** in the model settings bar. You can add line items when you [create a module](https://help.anaplan.com/686ff444-5356-48d1-9a9c-7cb2544e31d8), or add them later.

Before you create a line item subset, consider the following:

- Even though line items can contain formulas, the items in a line item subset can only aggregate to a simple subtotal. Only formulas that are simple subtotals are included in a line item subset.
- Any line item styles do not transfer over to the line item subset.
- While line item subsets from different modules have different dimensions, not sharing at least one common dimension may impact functions such as [COLLECT](https://help.anaplan.com/887a0bce-034b-4a0b-9e5f-262ec2f47e35).
- Line item subsets can only contain line items with numeric data types.
- You can only use one line item subset as a dimension in a module.

To create a line item subset:

1. Select **Line item subsets** in the model settings bar.
2. Select **Insert**, then [type a name for the line item subset](https://help.anaplan.com/aeb0b95e-f7a3-4fe5-81c7-aec9a12f80be). Create extra line item subsets by typing each line item subset on a new line.
3. Select **Before** or **After** to add the line item subset before or after an existing line item subset in the list. Select **Start** or **End** to add the line item subset to the start or end of the list.
4. Select **OK**.
5. Double-click or select the ellipsis () in the **Modules** column, then select the modules that contain the line items that you want to include in the line item subset.
6. Select **OK**.
7. Select the new line item subset, then select **Open**.
8. Select the line items you want to include in the line item subset. Your selections save automatically.

You can use the line item subset in a module as a [dimension](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a), or as a [picklist](https://help.anaplan.com/ddeaf549-4699-4e56-be9a-185205c49823). You can also use the [COLLECT()](https://help.anaplan.com/887a0bce-034b-4a0b-9e5f-262ec2f47e35) function in a module that includes a line item subset to pull the line item values into the module.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcreate-a-line-item-subset-30e5ac9c-0348-4bd4-8dd2-76855b8b8684&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>