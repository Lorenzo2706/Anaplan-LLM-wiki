---
title: "LOOKUP | Anapedia"
source: "https://help.anaplan.com/lookup-f8baa402-606d-4764-a349-d8003fa383be"
author:
published:
created: 2026-05-02
description: "Use the LOOKUP function to look up values in a source module or list and display the values in a target module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use the LOOKUP function to look up values in a source module or list and display the values in a target module.

For example, you can look up the salary for each employee in a module based on grade and region and display them in a results module.

`Values to lookup[LOOKUP: Mapping, LOOKUP: Mapping 2, etc.]`

Never use SUM and LOOKUP in the same formula. This can lead to extremely long calculation times. For more information, see [Formulas and their effects on model performance](https://community.anaplan.com/t5/Best-Practices/Formulas-and-their-effect-on-model-performance/ta-p/33556) .

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Values to lookup* | Number, Boolean, date, time period, list, or text line item. | The data source to retrieve a value from. This can be a module line item `module.lineitem` or a list property `list.property`, and can be in any data format. |
| *Mapping* | List, date, or time line item, or a property from the source. | The mapping is the cross-reference criteria. It can be a line item with a data type of list or time period. It can also be a property from the source or a date data type. The mapping matches the source line item or property with the target line item.  A common dimension must link the source and the mapping cross-reference.  You can enter multiple arguments as mappings. Arguments must be separated by a comma. For example:  `Pay Table.BasicPay[LOOKUP: Grade, LOOKUP: Region, LOOKUP: Period, etc.]` |

The LOOKUP function returns a result of the same data type as the *Values to lookup*.

**Note:** In Classic, LOOKUP returns the value of the aggregate item in a composite hierarchy, and the default value for the line item in a non-composite hierarchy.

You can use LOOKUP when the source line item is a finer timescale than the mapping line item data type. You can also use LOOKUP when the dimension of the target line item is a finer timescale than the dimension of the mapping line item.

However, if the time scale that you use in the results doesn't exist in the source, then LOOKUP returns 0. For example if you select **Half-year totals** in the results but it isn't selected in the source, LOOKUP returns 0.

To use LOOKUP:

1. In the target module, open the formula editor for the target line item.
2. Open the source module (if different from the target) and select the line item or list property heading.
3. In the target module, type `[LOOKUP:` in the editor.
4. Open the module that contains the mapping criteria, if different, and then select the line item to use for mapping. Either a:
	- List data type
		- Time period or date data type
		- List property  
		  
		You can also type the mapping criteria in the format `module.lineitem` or `list.property`.
5. If you have multiple mapping criteria, separate them with a comma, and end with a ` ]`. For example, `Pay Table.BasicPay[LOOKUP: Grade, LOOKUP: Region]`

In Polaris, the LOOKUP function returns the value of the aggregate item in [composite](https://help.anaplan.com/cabf4596-28b5-4849-a028-d2e610905b7d) and non-composite hierarchies. The Classic Engine returns the value of the aggregate item in a composite hierarchy, and the default value for the line item in a non-composite hierarchy.

In Polaris, you can't use the LOOKUP function in a result line item with a time scale greater than the values you look up. The Classic Engine returns a value of 0 in this case.

In Polaris, if the target line item can't reference the mapping line item, then the LOOKUP is invalid.

In Polaris, a LOOKUP will be invalid if the mapping line item has a dimension that is not related to a dimension in the target line item. This includes cases where the mapping line item is dimensioned by a line item subset.

`Pay table.Basic pay[LOOKUP: Grade, LOOKUP: Region]`

Where:

- `Pay table` is the source module
- `Basic pay` is a line item in the source module
- `Grade` and `Region` are the dimensions in the source module and also line items in the results module

For more information on when to use LOOKUP, see [Formula usage tips](https://help.anaplan.com/89bd50bd-dbbf-4465-b085-36163aa74450).

[LOOKUP](https://support.microsoft.com/en-gb/office/lookup-function-446d94af-663b-451d-8251-369d5e3864cb?ui=en-us&rs=en-gb&ad=gb)

Use the LOOKUP function to look up values in a source module or list and display the values in a target module using mapping criteria. These examples demonstrate how you can use LOOKUP in different scenarios in your models. Select each example to expand.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Flookup-f8baa402-606d-4764-a349-d8003fa383be&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>