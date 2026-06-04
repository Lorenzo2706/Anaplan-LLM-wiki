---
title: "RANKCUMULATE | Anapedia"
source: "https://help.anaplan.com/rankcumulate-1af75839-f426-43bf-b864-9027f1770161"
author:
published:
created: 2026-05-02
description: "The RANKCUMULATE function ranks values and then cumulates values in order of the ranking. It can perform ranking separately across different groups."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The RANKCUMULATE function ranks values and then cumulates values in order of the ranking. It can perform ranking separately across different groups.

For example, you can use the RANKCUMULATE function to cumulatively sum employees sales revenue in order of their length of service. There is an example of this in the Examples section.

`RANKCUMULATE(Cumulation values, Ranking values [, Direction] [, Include value] [, Ranking groups])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Cumulation values* (required) | Number, line item, property, or expression. | The number to cumulate, based on ranking criteria. |
| *Ranking values* (required) | Number, date, or time period  Can be a line item, property, or expression. | The ranking criteria to perform cumulation based on. |
| *Direction* | Keyword | Determines the direction to rank in.  The keywords are `DESCENDING` and `ASCENDING`. For more information, see the **Direction argument keywords** section below. |
| *Include value* | Boolean | Determines if a value is ranked.  The default value, TRUE, includes a value in the ranking.  A value of FALSE omits a value from the ranking and returns a result of 0. |
| *Ranking groups* | Number, Boolean, date, time period, list. Text is supported in Classic only. | If provided, values are ranked independently for each value of the *Ranking groups* argument. |

The RANKCUMULATE function returns a number.

| **Keyword** | **Description** |
| --- | --- |
| DESCENDING | When used, the RANKCUMULATE function assigns the highest source value rank 1, the second highest source value rank 2, and so on. |
| ASCENDING | The default keyword if you omit the *Direction* argument.  When used, the RANKCUMULATE function assigns the lowest source value rank 1, the second lowest source value rank 2, and so on. |

In Polaris, RANKCUMULATE can't be used when the target is dimensioned by a line item subset, or the function makes a reference to a line item subset.

In Polaris you don't have a cell limit. In Classic, it's 50 million cells.

Polaris doesn't support infinities, in Classic it does. In Classic, if a cumulation source contains an Infinity, then the result from then on until the end of the cumulation is that infinity. However, if an opposite Infinity follows it, the result becomes NaN (Not a Number). In Polaris it'll return NaN instead of Infinity.

In Polaris, blank is unordered, so it's unrankable. For RANKCUMULATE, if the ranking value is blank the the function returns zero.

In Polaris, the ranking values can be the BLANK literal. This is, `RANKCUMULATE(1, BLANK)` is valid, although the function will always return zero in this case.

In Polaris, blank values have a rank of 0, while in Classic, they are assigned the lowest available rank.

`RANKCUMULATE(Revenue, Transaction Date, DESCENDING, Eligible transaction?, Region)`

The *Ranking values* argument for the RANKCUMULATE function can be a number, date, or time period type line item, property, or expression. However, the function always returns a number.

When the RANKCUMULATE function ranks values with the default ASCENDING keyword for the *Direction* argument, the function ranks the lowest value as 1, the second lowest as 2, and so on. If you use RANKCUMULATE with:

- Numbers, the function ranks the largest number the highest.
- Dates, the function ranks the date furthest in the future the highest.
- Time periods, the function ranks the time period furthest in the future the highest.

If two values of the *Cumulation values* argument share the same ranking for the *Ranking values* argument, ranking follows the order of any associated list items within <ads-icons dimension-lists /> **General Lists**.

You can reference the **Users** list with the RANKCUMULATE function. However, you can't reference specific users in the **Users** list as this is [production data](https://help.anaplan.com/f8a7c584-8620-4a61-b8f4-d56a19eb8c20). This can change and make your formula invalid.

In the Classic Engine, this has a cell limit of 50 million cells to prevent ranking of large data sets that would slow down the server. If more than 50 million cells are used with the RANKCUMULATE function, the model is rolled back and a notification displays.

The 50 million cell limit doesn't account for [summarized values](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) or the **Time** and **Versions** lists. This means you can use the RANKCUMULATE function with a line item with a **Cell Count** of greater than 50 million cells if there are fewer than 50 million nonsummarized cells.

As the number of cells you use with the RANKCUMULATE function increases, so does the duration of the calculation.

If you use positive infinity, negative infinity, or NaN (Not a Number) for the *Ranking values* argument, the RANKCUMULATE function returns 0.

If your cumulation source is a large data set, the addition of numbers with a large number of decimal places can result in floating point errors for the least significant digits.

[RANKCUMULATE](https://support.office.com/en-gb/article/RANK-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723)

The following examples have the list *Salespeople* on columns and list items on rows.

This example helps to track sales by salespeople and accumulates bonus points based on their sales in *DESCENDING* order, without using the *Ranking groups* parameter.

|  | **Alice** | **Bob** | **Carol** | **Dan** | **Ellie** | **Felix** |
| --- | --- | --- | --- | --- | --- | --- |
| **Sales** | 200 | 300 | 400 | 500 | 600 | 700 |
| **Bonus points** | 5 | 10 | 20 | 15 | 25 | 80 |
| **Result**  `RANKCUMULATE(Bonus points, Sales, DESCENDING)` | 155 | 150 | 140 | 120 | 105 | 80 |

This example helps to track sales by salespeople and accumulates bonus points based on their sales in *ASCENDING* order per *Region*. Here, *Region* is a list.

|  | **Alice** | **Bob** | **Carol** | **Dan** | **Ellie** | **Felix** |
| --- | --- | --- | --- | --- | --- | --- |
| **Sales** | 200 | 300 | 400 | 500 | 600 | 700 |
| **Bonus points** | 5 | 10 | 20 | 15 | 25 | 80 |
| **Region** | West | South | West | East | South | North |
| **Result**  `RANKCUMULATE(Bonus points, Sales, ASCENDING, TRUE, Region)` | 5 | 10 | 25 | 15 | 35 | 80 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Frankcumulate-1af75839-f426-43bf-b864-9027f1770161&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>