---
title: "Sum up line items into a parent"
source: "https://help.anaplan.com/sum-up-line-items-into-a-parent-2090dd50-7e08-402a-99f9-2324fea369d7"
author:
published:
created: 2026-05-13
description: "Model builders can sum up line items into a parent."
tags:
  - "clippings"
---
[Line items](https://help.anaplan.com/line-items-52d76cdd-2571-4400-8f34-b15dd5651b9f "Line items")

When you select a parent for a line item, a formula is entered into the **Formula** column, and the **Is Summary** option is selected.

For example, the *Total Expenses* line item is the parent of the *General Expenses* and *Employee Expenses* line items.

| **Line item** | **Formula** | **Parent** | **Is Summary** |
| --- | --- | --- | --- |
| General Expenses |  | Total Expenses |  |
| Employee Expenses |  | Total Expenses |  |
| Total Expenses | `General Expenses + Employee Expenses` |  |  |

To change the parent of a line item:

1. Select **Modules** in the model settings bar.
2. Select the module that contains the line items you want to manage, then select **Open**.
3. Select **Blueprint**.
4. Deselect **Is Summary** for the current line item that is set as the parent.
5. Select **Is Summary** for the new parent line item.

The example below demonstrates how to change the parent of the *General Expenses* and *Employee Expenses* line items, without affecting the formula for *Total Expenses*.

The table below reflects the line items before changes are made:

| **Line item** | **Formula** | **Parent** | **Is Summary** |
| --- | --- | --- | --- |
| General Expenses |  | Total Expenses |  |
| Employee Expenses |  | Total Expenses |  |
| Total Expenses | `General Expenses + Employee Expenses` |  |  |
| Mailing Expenses |  | Other Expenses |  |
| Other Expenses |  |  |  |

The table shows the result of the change:

| **Line items** | **Formula** | **Parent** | **Is Summary** |
| --- | --- | --- | --- |
| General Expenses |  | Other Expenses |  |
| Employee Expenses |  | Other Expenses |  |
| Total Expenses | `General Expenses + Employee Expenses` |  |  |
| Mailing Expenses |  | Other Expenses |  |
| Other Expenses | `General Expenses + Employee Expenses` |  |  |

Follow the procedures below to recreate the table above:

1. Type the sum `General Expenses + Employee Expenses` in the **Formula** column for the *Other Expenses* line item. You can copy this from *Total Expenses*.
2. Deselect **Is Summary** for *Total Expenses.* This removes the parent from *General Expenses* and *Employee Expenses*.
3. Select **Is Summary** for the new parent, *Other Expenses*. The parent for *General Expenses* and *Employee Expenses* automatically changes to *Other Expenses.*

Line items can be part of multiple hierarchies with more than one parent.

For example, the *Vehicle Maintenance* line item can have *Total Vehicle Costs* and *Total Maintenance Costs* as parents. The **Parent** column enables you to choose a parent for the item in a particular context.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fsum-up-line-items-into-a-parent-2090dd50-7e08-402a-99f9-2324fea369d7&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>