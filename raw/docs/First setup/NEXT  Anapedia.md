---
title: "NEXT | Anapedia"
source: "https://help.anaplan.com/next-ce38460d-e931-403a-837c-d650d0ddaf64"
author:
published:
created: 2026-05-02
description: "The NEXT function evaluates an expression based on the next value across the selected dimension."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use this function to compare the performance of the current period against the forecast value for the next period.

`NEXT(Expression[, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Expression* | Number, Boolean, date, time period, list, or text | The expression to return the value from the next period for. |
| *List* (Polaris only) | List | The list over which the function should operate. The target line item must be dimensioned with any dimension compatible with this list.  See **Calculation engine functionality differences**. |

The NEXT function returns a result of the same data type as the *Expression* argument.

- In Polaris, you can't use NEXT for line items that have the **Formula** summary method.  
	In the Classic Engine, you can.
- In Polaris, you can use NEXT with any dimension compatible with a dimension of the target, except Versions. For example you can use a list or its subset as the second argument when the target line item is dimensioned by a list. For versions, use NEXTVERSION.  
	In the Classic Engine, you can use NEXT only with a time dimension.
- In Polaris, for time outside the time range hierarchy, NEXT returns zero or blank values.

`NEXT(Revenue)`

This formula returns the next value of the *Revenue* line item.

If the NEXT function returns a value from outside of a line item’s range, it uses a default value. If the line item has a data type of:

- Number, NEXT returns a value of 0.
- Boolean, NEXT returns a value of FALSE.
- Text, date, or time period, NEXT returns a value of BLANK.

In Polaris, the target line item can be of any dimension compatible with the second argument *List*. In the Classic Engine, the target line item must have Time as a dimension.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** |
| --- | --- | --- | --- | --- |
| **Net Profit** | 215,770 | 221,123 | 223,495 | 220,129 |
| **Forecast Profit Change**  `NEXT(Net Profit) - Net Profit` | 5,353 | 2,372 | \-3,366 | 220,129 |

In this example, an income statement module has line items on rows and time on columns. The *Net Profit* line item shows the net profit for a business.

In this model, the *Actual* version changes to *Forecast* in *Apr 21*, as **Switchover** is enabled in **Model Settings > Versions**. The *Forecast* value for Apr 21 uses a formula to calculate a forecast based on an average of the values for the past three months. As the current period changes, this formula calculates a forecast profit for the next period.

The formula in the *Forecast Profit Change* line item uses the NEXT function to retrieve the value of *Net Profit* from the next period. The *Net Profit* for the current period is subtracted from the *Net Profit* for the next period to calculate the change in profit from one month to another. This includes the *Forecast* value for *Apr 21*, which can be used to plan ahead. As there's no value for *May 21* yet, the final value of the *Forecast Profit Change* line item is the value of the *Net Profit* line item for *Apr 21*.

|  | **1** | **2** | **3** | 4 |
| --- | --- | --- | --- | --- |
| **Lead count** | 1,000 | 600 | 300 | 150 |
| **Next stage lead count**  `NEXT(Lead count, Sales stage order)` | 600 | 300 | 150 | 0 |
| **Change**  `Lead count - NEXT(Lead count, Sales stage order)` | 400 | 300 | 150 | 150 |

In this example, the function is dimensioned over the *Sales stage order* list, which is on columns.

The formula in the *Next stage lead count* line item retrieves the lead count from the item immediately after the current one in the *Sales stage order* list. The formula in the *Change* line item calculates the difference in lead count between the current stage and the next one. It shows how many leads were lost or gained as you move from one stage to the next in the pipeline.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fnext-ce38460d-e931-403a-837c-d650d0ddaf64&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>