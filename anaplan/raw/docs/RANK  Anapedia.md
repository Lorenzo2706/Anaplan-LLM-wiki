---
title: "RANK | Anapedia"
source: "https://help.anaplan.com/rank-a5f5778e-5e88-48ad-96ad-715178cda9b2"
author:
published:
created: 2026-05-02
description: "The RANK function evaluates a set of values and assigns sequential rankings starting at 1."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the RANK function to rank different territories by sales revenue.

`RANK(Source values [, Direction] [, Equal value behavior] [, Include value] [, Ranking groups])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source values* | Number, date, or time period | The number, date, or time period to rank. |
| *Direction* (optional) | Keyword | Determines the direction to rank in.  The keywords are DESCENDING and ASCENDING. There's more information in the Direction argument keywords section below. |
| *Equal value behavior* (optional) | Keyword | Determines how to rank equal values.  The keywords are MINIMUM, MAXIMUM, AVERAGE, and SEQUENTIAL. There's more information in the Equal value behavior argument keywords section below. |
| *Include value* (optional) | Boolean | Determines if a value is ranked.  The default value, TRUE, includes a value in the ranking. |
| *Ranking groups* (optional) | Number, Boolean, date, time period, list. Text is supported in Classic only. | If provided, the source values are ranked independently for each value in the Ranking groups argument. |

The RANK function returns a number-formatted result.

| **Keyword** | **Description** |
| --- | --- |
| DESCENDING | The default keyword if you omit the *Direction* argument.  When used, the RANK function assigns the highest source value rank 1, the second highest source value rank 2, and so on. |
| ASCENDING | When used, the RANK function assigns the lowest source value rank 1, the second lowest source value rank 2, and so on. |

| **Keyword** | **Description** |
| --- | --- |
| MINIMUM | The default keyword if you omit the *Equal value behavior* argument.  Gives tied values the lowest ranking of their range. |
| MAXIMUM | Gives tied values the highest ranking of their range. |
| AVERAGE | Gives tied values the average of the range of applicable rankings. |
| SEQUENTIAL | Gives tied values separate rankings, in the order they occur in the underlying list. |

In Polaris, RANK cannot be used when the target is dimensioned by a line item subset, or the function makes a reference to a line item subset.

In Classic, a value of FALSE for the *Include value* argument omits a value from the ranking and returns a result of NaN (Not a Number). In Polaris it returns a value of 0 (zero).

In Classic, you can use a text data type for the *Ranking groups* argument. In Polaris, you cannot.

In Polaris you do not have a cell limit. In Classic, it is 50 million cells.

In Classic, infinities and NaN are automatically excluded from the RANK function and return a result of NaN. In Polaris, NaN values are automatically excluded from the RANK function and return a result of 0. Infinities have also been removed.

In Polaris, blank values have a rank of 0, while in Classic, they are assigned the lowest available rank.

`RANK(Revenue, DESCENDING, MINIMUM, Include in Ranking?, Region)`

This formula ranks the values of *Revenue* line item if the *Include in Ranking?* line item is TRUE. It ranks values in separate groups determined by *Region*.

As the formula uses the DESCENDING and MINIMUM keywords:

- the highest values of the *Revenue* line item are ranked 1.
- if there are any tied values for the Revenue line item, it assigns them both the lower rank.

The *Source values* argument for the RANK function can be a number-, date-, or time period-formatted line item, property, or expression. However, the function always returns a number-formatted result.

When the RANK function ranks values with the default DESCENDING keyword for the *Direction* argument, the function ranks the highest value as 1, the second highest as 2, and so on. If you use RANK with:

- numbers, the function ranks the largest number the highest.
- dates, the function ranks the latest date the highest.
- time periods, the function ranks the most latest time period the highest.

If the module that contains the *Source values* argument applies to more than one other dimension (excluding **Time** and **Versions**), the ranking applies across all combinations of those dimensions. This includes values that do not currently display on your view of the data.

Consider a module with two line items, *Sales* and *Sales Rank*, which apply to *Region* and *Product.* There are 100 products sold in 50 regions.

`Sales Rank = RANK(Sales)`

In this example, the formula returns ranks between 1 and 5,000, ranking each combination of *Product* and *Region* across all pages.

You can reference the Users list with the RANK function. However, you can't reference specific users within the Users list as this is [production data](https://help.anaplan.com/f8a7c584-8620-4a61-b8f4-d56a19eb8c20), which can change and make your formula invalid.

In the Classic calculation engine, Anaplan imposes an artificial limit of 50 million cells to prevent the ranking of large data sets that would slow down the server. If you use more than 50 million cells with the RANK function, the model rolls back and a notification displays.

The 50 million cell limit does not account for [summarized values](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) or the **Time** and **Versions** lists. This means you can use the RANK function with a line item with a **Cell Count** of greater than 50 million cells if there are less than 50 million non-summarized cells.

As the number of cells you use with the RANK function increases, so does the duration of the calculations.

Infinities and NaN are automatically excluded from the RANK function and return a result of NaN.

[RANK](https://support.office.com/en-gb/article/RANK-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723)

|  | London | Birmingham | **UK** | Paris | Lyon | **France** | Munich | Berlin | **Germany** | New York | Los Angeles | **USA** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sales | 11,000 | 20,000 | 31,000 | 14,000 | 14,000 | 28,000 | 25,000 | 1,000 | 26,000 | 8,000 | 30,000 | 38,000 | 123,000 |
| `RANK (Sales)` | 6 | 3 |  | 4 | 4 |  | 2 | 8 |  | 7 | 1 |  |  |

This example contains an *Organization* list on columns, where cities are children of regions. There are two line items on rows, one for *Sales*, and one for the formula that contains the RANK function.

The cities are ranked by their value for the *Sales* line item. As the parent regions are summaries, they omit from the ranking.

As the formula only contains the *Source values* argument, the default keywords are used for the optional *Direction* and *Equal value behavior* arguments.

The default DESCENDING keyword is used for the *Direction* argument. This means the city with the largest value for the *Sales* line item ranks the highest.

The default MINIMUM keyword is used for the *Equal value behavior* argument. This means that *Paris* and *Lyon*, which both have the same value for the *Sales* line item, are both assigned the lower ranking. In this case, 4.

|  | London | Birmingham | **UK** | Paris | Lyon | **France** | Munich | Berlin | **Germany** | New York | Los Angeles | **USA** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sales | 11,000 | 20,000 | 31,000 | 14,000 | 14,000 | 28,000 | 25,000 | 1,000 | 26,000 | 8,000 | 30,000 | 38,000 | 123,000 |
| `RANK (Sales, DESCENDING)` | 6 | 3 |  | 4 | 4 |  | 2 | 8 |  | 7 | 1 |  |  |
| `RANK (Sales, ASCENDING)` | 3 | 6 |  | 4 | 4 |  | 7 | 1 |  | 2 | 8 |  |  |

This example shows the behavior of the two keywords for the *Direction* argument.

The result of the DESCENDING keyword is that the largest value for the *Sales* line item ranks as 1, through to the smallest value, which ranks as 8.

The result of the ASCENDING keyword is that the smallest number for the *Sales* line item ranks as 1, through to the largest value, which ranks as 8.

|  | London | Birmingham | **UK** | Paris | Lyon | **France** | Munich | Berlin | **Germany** | New York | Los Angeles | **USA** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sales | 11,000 | 20,000 | 31,000 | 14,000 | 14,000 | 28,000 | 25,000 | 1,000 | 26,000 | 8,000 | 30,000 | 38,000 | 123,000 |
| `RANK (Sales, DESCENDING, MINIMUM)` | 6 | 3 |  | 4 | 4 |  | 7 | 1 |  | 2 | 8 |  |  |
| `RANK (Sales, DESCENDING, MAXIMUM)` | 6 | 3 |  | 5 | 5 |  | 7 | 1 |  | 2 | 8 |  |  |
| `RANK (Sales, DESCENDING, AVERAGE)` | 6 | 3 |  | 4.5 | 4.5 |  | 7 | 1 |  | 2 | 8 |  |  |
| `RANK (Sales, DESCENDING, SEQUENTIAL)` | 6 | 3 |  | 4 | 5 |  | 7 | 1 |  | 2 | 8 |  |  |

This example shows the behaviors of the four keywords for the *Equal value behavior* argument. The values for the *Sales* line item for *Paris* and *Lyon* are both the same, *14,000*, so they highlight the different behaviors:

- The MINIMUM keyword assigns both *Paris* and *Lyon* the numerically lower rank, *4*.
- The MAXIMUM keyword assigns both *Paris* and *Lyon* the numerically higher rank, *5*.
- The AVERAGE keyword assigns both *Paris* and *Lyon* the average of their ranks, *4.5*.
- The SEQUENTIAL keyword assigns both *Paris* and *Lyon* ranks in the order of the underlying list, regardless of the parent hierarchy.

|  | London | Birmingham | **UK** | Paris | Lyon | **France** | Munich | Berlin | **Germany** | New York | Los Angeles | **USA** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sales | 11,000 | 20,000 | 31,000 | 14,000 | 14,000 | 28,000 | 25,000 | 1,000 | 26,000 | 8,000 | 30,000 | 38,000 | 123,000 |
| Include in Ranking? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `RANK(Sales, DESCENDING, MINIMUM, Sales > 10000 AND Sales < 24000)` | 4 | 1 |  | 2 | 2 |  | NaN | NaN |  | NaN | NaN |  |  |
| `RANK(Sales, DESCENDING, MINIMUM, Sales > 10000)` | 6 | 3 |  | 4 | 4 |  | 2 | NaN |  | NaN | 1 |  |  |
| `RANK(Sales, DESCENDING, MINIMUM, Include in Ranking? = TRUE)` | 5 | 2 |  | 3 | 3 |  | 1 | NaN |  | 6 | NaN |  |  |

**Note:** In Polaris, all cells where the *includeRankingValue?* above is false, the cell will have a value of 0, instead of NaN.

The *Include value* argument enables you to use a Boolean statement to determine whether a value is ranked. This can be a reference to a Boolean-formatted line item, or a Boolean statement entered directly into the formula.

In the first two formulas, the values to include in the ranking are determined by Boolean statements that specify they must either be:

- Larger than 10,000 and smaller than 24,000.
- Larger than 10,000.

The third formula contains a reference to the *Include in Ranking?* Boolean-formatted line item. As a result, it only ranks items in the *Organization* list, which the *Include in Ranking?* line item has a value of TRUE for.

|  | London | Birmingham | **UK** | Paris | Lyon | **France** | Munich | Berlin | **Germany** | New York | Los Angeles | **USA** | **Total Company** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sales | 11,000 | 20,000 | 31,000 | 14,000 | 14,000 | 28,000 | 25,000 | 1,000 | 26,000 | 8,000 | 30,000 | 38,000 | 123,000 |
| Store Type | Ministore | Superstore |  | Ministore | Ministore |  | Superstore | Warehouse |  | Warehouse | Superstore |  |  |
| Opening Date | 20/3/20/21 | 20/03/2021 |  | 20/03/2021 | 29/04/2020 |  | 29/04/2020 | 20/03/2021 |  | 25/06/2020 | 05/07/2020 |  |  |
| `RANK(Sales, DESCENDING, MINIMUM, Sales > 0, PARENT(ITEM(Organization)))` | 2 | 1 |  | 1 | 1 |  | 1 | 2 |  | 2 | 1 |  |  |
| `RANK(Sales, DESCENDING, MINIMUM, Sales > 0, Store Type)` | 2 | 3 |  | 1 | 1 |  | 2 | 2 |  | 1 | 1 |  |  |
| `RANK(Sales, DESCENDING, MINIMUM, Sales > 0, Opening Date)` | 3 | 1 |  | 2 | 2 |  | 1 | 4 |  | 1 | 1 |  |  |
| `RANK(Sales, DESCENDING, MINIMUM, Sales > 0, YEAR(Opening Date))` | 3 | 1 |  | 2 | 3 |  | 2 | 4 |  | 4 | 1 |  |  |

The *Ranking groups* argument enables you to specify criteria so that data ranks within sub-groups. The four example formulas in the table above demonstrate the following types of data used for the *Ranking groups* argument:

- The parent item of each territory within the *Organization* list (retrieved with a combination of the [PARENT](https://help.anaplan.com/1cdc486d-c4d7-42db-8b1a-d9e12c060999) and [ITEM](https://help.anaplan.com/41298b7a-e877-40e8-8cfa-8d7009d8686f) functions). This means that territories rank among their peers within each region. For example, *London* and *Birmingham* for the *UK*, *Paris* and *Lyon* for *France*, and so on.
- A list-formatted *Store Type* line item that contains the type of store for each territory within the *Organization* list. Territories rank within groups for each store type.
- The *Opening date* for each territory. If territories share their opening date, they rank among one another.
- The *Opening date* for each territory used with the [YEAR](https://help.anaplan.com/d5b458d3-b0f7-4b70-a28a-342ea85f8416) function to return the year that date's in. Territories with an opening date in the same year rank among one another.

|  | Store 1 | Store 2 | Store 3 | Store 4 | Store 5 | Store 6 | Store 7 | Store 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Store Closure Date | 01/01/21 | 02/06/21 | 16/07/21 | 04/03/21 | 14/08/21 |  | 30/04/21 | 10/09/21 |
| `RANK(Store Closure Date, ASCENDING)` | 2 | 5 | 6 | 3 | 7 | 1 | 4 | 8 |
| Store Open Time Period | Jan 19 | Mar 19 | Jul 19 | Oct 19 | Sep 19 |  | Jun 19 | Apr 19 |
| `RANK(Store Open Time Period, ASCENDING)` | 2 | 3 | 6 | 8 | 7 | 1 | 5 | 4 |

You can also use a date- or time period-formatted value for the *Source values* argument. If you do this, values rank in chronological order.

If you use the default DESCENDING keyword for the *Direction* argument, the most recent value ranks as 1, the second most recent value tanks as 2, and so on.

If you use the ASCENDING keyword for the *Direction* argument, the oldest value ranks as 1, the second oldest value ranks as 2, and so on.

In Classic, a blank value for a date- or time period-formatted value is ranked as old as possible by the RANK function. As such, in this example, the RANK function ranks the blank value as 8 for the DESCENDING keyword, and 1 for the ASCENDING keyword. In Polaris, blank is unranked and the RANK function will return 0

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Frank-a5f5778e-5e88-48ad-96ad-715178cda9b2&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>