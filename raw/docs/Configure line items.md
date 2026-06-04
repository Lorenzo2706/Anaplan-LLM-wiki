---
title: "Configure line items"
source: "https://help.anaplan.com/configure-line-items-e7de33be-6345-4ecc-a517-c3265ff6d04a"
author:
published:
created: 2026-05-13
description: "Model builders can configure different settings for line items in a module, such as formulas and time scales."
tags:
  - "clippings"
---
[Line items](https://help.anaplan.com/line-items-52d76cdd-2571-4400-8f34-b15dd5651b9f "Line items")

Model builders can configure different settings for line items in a module, such as formulas and time scales.

Before you configure line items, create any line items you need in **Modules** in the model settings bar. You can add line items when you create a module, or add them later.

To configure a line item:

1. Select **Modules** in the model settings bar.
2. Select the module that contains the line item you want to configure, then select **Open**.
3. Select **Blueprint**.

Refer to the table below for a description of each available setting.

| **Setting** | **Description** |
| --- | --- |
| **Format** | Set the line item's format. Choose from **Number**, **Boolean**, **Date**, **Time Period**, **List**, **Text**, and **No Data**. **Number** is the default format. |
| **Formula** | Enter a formula that calculates the line item. For example, the *Margin %* line might contain the `Margin / Revenue` formula. |
| **Summary** | Set the summary method for calculating line item totals. The default summary method is None**.**  If you want to calculate totals for a line item, select Sum. |
| **Applies To** | Choose the [list](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075) that the line item applies to.  If you select a list, it automatically creates a subsidiary view. |
| **Time Scale** | Set the line item's time scale.  You can select a different granularity for a line item in the [time scale](https://help.anaplan.com/c4045bfd-934c-4816-8e44-e4ff3fa1a429) column. For example, if the default dimension is measured by Year, you can create a line item that has a time scale of Month.  If you change the time scale for a line item, a subsidiary view is created. |
| **Time Range** | Set the line item's time range.  If your model includes time ranges, you can set a specific time range for the line item. Manage time ranges in **Time**.  If different line items use different time ranges in a module, subsidiary views are created. |
| **Versions** | Assign [versions](https://help.anaplan.com/19b4391f-5257-40ee-8dfb-36f0ab426c8f) to the line item. |
| **Style** | Apply styles to a line item to change its appearance. Styles only apply to line items that display on rows, except for **Summary**. |
| **Cell Count** | Displays the number of cells in the line item. |
| **Populated Cell Count** | Only displays in [Polaris](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).  Displays the number of cells that contain data in the line item. |
| **Memory Used** | Only displays in [Polaris](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).  Displays the amount of memory that a line item uses. |
| **Calculation Complexity** | Only displays in [Polaris](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).  Contains one of three values: **One-to-One**, **One-to-Many**, or **All cells**. These explain the effect of a line item formula upon model sparsity. [Learn more](https://help.anaplan.com/b6f91ac9-aa99-4eec-91f2-35355b2d566c). |
| **Calculation Effort** | Displays a percentage that represents the calculation effort of the line item.  In Classic, when you open a model, all formulas are calculated and measured for effort across the entire model, right away.  This tells you which line items in the model require the most computation, and may require optimization.  Subsequent changes to a line item's formula trigger a recalculation of effort for that line item.  In Polaris, the calculation effort shows as a percentage against the total effort of all line items over the last 10 minutes. |
| **Notes** | Displays any notes associated with the module. |
| **Read Access Driver** | Control [read access](https://help.anaplan.com/55ae93e6-5139-4bbf-93f9-c8cb06f68f75) to cell data with access drivers. Access drivers are line items with a Boolean data type. |
| **Write Access Driver** | Control [write access](https://help.anaplan.com/55ae93e6-5139-4bbf-93f9-c8cb06f68f75) to cell data with access drivers. Access drivers are line items with a Boolean data type. |
| **Users List** | If the module contains the [*Users* list](https://help.anaplan.com/56391e35-2831-4642-b6de-2dddb6c68cfa), specify if the full contents of the list are visible to workspace administrators. |
| **Parent** | Set a parent for the line item. When you set a parent for a line item, an additional formula is entered into the **Formula** column, and the **Is Summary** option is selected. |
| **Is Summary** | Marks a line item as a parent. |
| **Formula Scope** | Set the version that a line item formula applies to. |
| **Code** | Assign a code to the line item. Each line item name and code combination is unique, so when you import module data, you can match specifically on codes. You can [import line items](https://help.anaplan.com/796a5324-b043-46da-b6cb-ce04125cbcb2) and codes into a module. |
| **Use Switchover** | Apply the **Switchover** date to a line item that uses versions. [Switchover](https://help.anaplan.com/f164c070-19bf-4f47-88af-301f69edc0e5) combines actual data with forecast data on a switchover date to create a rolling forecast. |
| **Breakback** | Set the default [Breakback](https://help.anaplan.com/1b7aa87d-aa13-49f6-8f7d-d893fb8bccbe) setting for new line items in the module. |
| **Brought-Forward** | Create a new opening balance by carrying a balance forward.  An extra time period is added before the start of the time scale for this line item. If you apply **Brought-Forward** to a line item with a formula, you can't edit the cell for this additional time period.  **Note**: This functionality isn't available in [Polaris](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5). |
| **Start of Section** | Change the dimensionality of all line items that follow a specific line item without creating a subsidiary view.  Use **Start of Section** where a change in dimensionality reflects a subset of the default dimension. When you select this option, don't reorder line items as this affects the dimensionality of the module. |
| **Data Tags** | Assign data tags to group information that relates to the line item. A hyphen indicates that the data tag is set at module level. |
| **Referenced By** | Displays whether the line item is referenced by another line item.  If a line item originates from another module, the format of the reference is *module name*.*line item name*. |
| **Module Name** | Displays the name of the module that contains the line item. |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fconfigure-line-items-e7de33be-6345-4ecc-a517-c3265ff6d04a&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>