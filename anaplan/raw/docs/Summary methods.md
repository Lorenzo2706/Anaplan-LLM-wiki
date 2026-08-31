---
title: "Summary methods"
source: "https://help.anaplan.com/summary-methods-32821c05-3e6c-4b36-b04e-2fb840418936"
author:
published:
created: 2026-05-13
description: "Summary methods define how the total of child cells is calculated into one value."
tags:
  - "clippings"
---
[Line items](https://help.anaplan.com/line-items-52d76cdd-2571-4400-8f34-b15dd5651b9f "Line items")

For example, if you have a line item with values for each month, you can use a summary method to calculate the total for the quarter or the year. You can sum them, find their average, find the maximum value, or you can choose from other summary methods to control how your data aggregates.

Each data type has a default summary method. For example, **None** (no summary) is the default for the Booleandata type, and for the number data type.

When you [select a summary method](https://help.anaplan.com/55069a7f-fe25-4d22-a6fb-221a01a9e4fa), you may be calculating the totals of many cells. If a module contains many [dimensions](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a) or deep [hierarchies](https://help.anaplan.com/2fc52da8-b161-4d29-acfb-9aafde1b5bae), totals can cause a significant increase in the overall number of cells.

It's recommended practice to set your line item's summary method to **None**, and only use another summary method when you need it. This approach guarantees that aggregated cells are only calculated when you require them.

When you have chosen an appropriate summary method for your data, consider whether the summary is a strict sum of the data for all the members in the hierarchy.

For example, you might want to add up units sold by stores in each region. In this case, you would select **Sum**, the default method. If you want to calculate the price of the units over time, you might select **Average**.

You can select a different summary method for the Time dimension to the summary method that you select for other dimensions.

The table below describes the valid summary methods you can use with each data type in the Classic Engine. [The Polaris engine has some differences](https://help.anaplan.com/4c7a3bda-f406-49d5-a3ba-d54524fc0c22).

| **Summary method** | **Data type** | **Description** |
| --- | --- | --- |
| **Sum** | Number | Adds together all the values from the child cells. |
| **None** | Number, Date, List, Time Period, Text, Boolean | Turns off summaries. No aggregation is performed. The summary cell remains blank.  None is the default option for Number and Boolean.  When using **Time summary**, **None** can be combined with the **Formula** and **Ratio**. |
| **Formula** | Number, Date, List, Time Period, Text, Boolean | Uses a formula to calculate the summary value.  The formula is applied by picking values from the referenced line items at the appropriate levels.  When using **Time summary**, **Formula** can be combined with the **None** and **Ratio**. |
| **Average** | Number | Calculates the mean average of the child cells.  **Note:** Average also includes empty cells and cells containing zero. |
| **Ratio** | Number | Calculates the summary by dividing one line item by another.  When you select **Ratio**, you must specify the line items used in the ratio. For example:  `Profit Margin = Profit/Revenue`  When using **Time summary**, **Ratio** can be combined with the **Formula** and **None**. |
| **Min** | Number, Date, Time Period | Returns the smallest value from the child cells. |
| **Max** | Number, Date, Time Period | Returns the largest value from the child cells. |
| **Opening Balance** | Number (**Time Summary** only) | Returns the value of the first time period in the series. |
| **Closing Balance** | Number (**Time Summary** only) | Returns the value of the last time period in the series. |
| **Any** | Boolean | Returns TRUE when at least one of the child cells is TRUE. |
| **All** | Boolean | Returns TRUE when all the child cells are TRUE. |
| **First non-blank** | Date, List, Time Period, Text | Returns the first value of the time period that is not empty. |
| **Last non-blank** | Date, List, Time Period, Text | Returns the last value of the time period that is not empty. |

**Note:** When there are no input values, the methods return the default value of the data type associated with them:

- 0for numbers,
- FALSE for Boolean
- BLANK for other data types.

| **Summary method** | **Examples** |
| --- | --- |
| **Sum** | Calculating total quarterly sales by summing the sales of each month within that quarter.  Aggregating the approved headcount for multiple departments to calculate the total headcount for a business unit. |
| **None** | A line item for a specific discount percentage that shouldn't be added up across time or other hierarchies.  A line item containing an exchange rate that applies to all periods. Aggregating it'd be meaningless. |
| **Formula** | Calculating a Gross Margin % at a summary level, where the formula might be (Total Revenue - Total Cost of Goods Sold) / Total Revenue.  Calculating a 'Plan vs. Actual Variance %' at the summary level with the formula: (Total Actuals - Total Plan) / Total Plan. |
| **Average** | Finding the average deal size across all opportunities in a given quarter.  Calculating the average monthly rainfall over a year from monthly data points. |
| **Ratio** | Calculating the overall profit margin for a region by dividing the region's total profit by its total revenue.  Determining the overall marketing ROI for a campaign by dividing the total campaign-generated revenue by the total campaign cost. |
| **Min** | Identifying the earliest start date for a project by looking at the start dates of all its sub-tasks.  Identifying the lowest price quoted by a supplier from a list of several quotes. |
| **Max** | Finding the highest sales transaction in a month.  Finding the longest employee tenure in a company by looking at the tenure of all individual employees. |
| **Opening balance** | Carrying over the closing inventory balance from the previous year as the opening balance for the current year.  Taking the number of subscribers at the end of the last fiscal year to be the starting number for the new fiscal year.  To know how much cash was available at the start of a quarter. |
| **Closing balance** | The final inventory count at the end of a quarter becomes the summary value for that quarter.  The final number of open customer support tickets at the end of the month is the closing value for that month. |
| **Any** | A risk register where a category is flagged as "At Risk" (TRUE) if any single risk item within it is flagged as "At Risk" (TRUE).  A parent project is marked 'Overdue' (TRUE) if any of its sub-tasks are past their deadline (TRUE). |
| **All** | A checklist where a summary task is marked "Complete" (TRUE) only if all sub-tasks are also "Complete" (TRUE).  A summary for a system deployment is marked as 'Ready' (TRUE) only if all components ('Server Configured', 'Database Migrated', 'UAT Signed Off') are TRUE. |
| **First non-blank** | Finding the initial status of a project from a series of status updates over time.  Retrieving the original assigned owner of a support case from a log of ownership transfers. |
| **Last non-blank** | Identifying the current owner of a sales account from a history of ownership changes.  Identifying the final approver in a multi-step workflow from a series of approval timestamps. |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fsummary-methods-32821c05-3e6c-4b36-b04e-2fb840418936&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>