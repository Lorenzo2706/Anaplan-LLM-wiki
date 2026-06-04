---
title: "PREVIOUS | Anapedia"
source: "https://help.anaplan.com/previous-e5806da3-1ae6-4b45-9e02-68ac764cb97d"
author:
published:
created: 2026-05-02
description: "The PREVIOUS function evaluates an expression based on the preceding value across the selected dimension."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use this function to compare the values of each period relative to the previous period.

`PREVIOUS(Expression [, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Expression* | Number, Boolean, date, time period, list, or text | The expression to return the value from the previous period for. |
| *List* (Polaris only) | List | The list over which the function should operate. The target line item must be dimensioned with any dimension compatible with this list.  See **Calculation engine functionality differences**. |

The PREVIOUS function returns a result of the same data type as the *Expression* argument.

- In Polaris, you can't use PREVIOUS for line items that have the **Formula** summary method.  
	In the Classic Engine, you can.
- In Polaris, you can use PREVIOUS with any dimension compatible with a dimension of the target, except Versions. For example you can use a list or its subset as the second argument when the target line item is dimensioned by a list. For versions, use PREVIOUSVERSION.  
	In the Classic Engine, you can use PREVIOUS only with a time dimension.
- In Polaris, for time outside the time range hierarchy, PREVIOUS returns zero or blank values.

`PREVIOUS(Revenue)`

This formula returns the preceding value of the *Revenue* line item.

`PREVIOUS(Lead count, Sales stage order)`

This formula looks up the lead count from the previous stage in the *Sales stage order* list.

If the PREVIOUS function returns a value from outside a line item's time range, it uses a default value. If the line item has a data type of:

- Number, PREVIOUS returns a value of 0.
- Boolean, PREVIOUS returns a value of FALSE.
- Text, date, or time period, PREVIOUS returns a value of BLANK.

When you apply **Brought-Forward** to a line item, the PREVIOUS function includes it as an additional period before the first time period in a module. However, as there is no value before the Brought-Forward period itself, the PREVIOUS function returns the default value for the Brought-Forward period.

In Polaris, the target line item can be of any dimension compatible with the second argument *List*. In the Classic Engine, the target line item must have Time as a dimension.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** |
| --- | --- | --- | --- | --- |
| **Net Profit** | 215,770 | 221,123 | 223,495 | 220,129 |
| **Month-on-month profit change**  `Net Profit - PREVIOUS(Net Profit)` | 215,770 | 5,353 | 2,372 | \-3,366 |

In this example, an income statement module has line items on rows and time on columns. The *Net Profit* line item shows the net profit for a business.

The formula in the *Month-on-month profit change* line item uses the PREVIOUS function to retrieve the value of *Net Profit* from the previous period. The *Net Profit* for the previous period is subtracted from the *Net Profit* for the current period to calculate the change in profit from one month to another. As the module's time range starts in 2021, the value for *Month-on-month profit change* in *Jan 21* is the same as the *Net Profit*.

|  | **1** | **2** | **3** | 4 |
| --- | --- | --- | --- | --- |
| **Lead count** | 1,000 | 600 | 300 | 150 |
| **Previous stage lead count**  `PREVIOUS(Lead count, Sales stage order)` | 0 | 1,000 | 600 | 300 |
| **Change**  `Lead count - PREVIOUS(Lead count, Sales stage order)` | 1,000 | \-400 | \-300 | \-150 |

In this example, the function is dimensioned over the *Sales stage order* list, which is on columns.

The formula in the *Previous stage lead count* line item retrieves the lead count from the item immediately before the current one in the *Sales stage order* list. The formula in the *Change* line item calculates the difference in lead count between the current stage and the previous one. It shows how many leads were lost or gained as you move from one stage to the next in the pipeline.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fprevious-e5806da3-1ae6-4b45-9e02-68ac764cb97d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>