---
title: "TIMESUM | Anapedia"
source: "https://help.anaplan.com/timesum-45c3bc48-4d80-490d-9b18-76af505c6907"
author:
published:
created: 2026-05-02
description: "The TIMESUM function aggregates values between two time periods and returns a single value."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the TIMESUM function to aggregate the revenue for previous periods through to the current period.

`TIMESUM(Line item to aggregate [, Start period] [, End period] [, Aggregation method])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Line item to aggregate* (required) | Number, boolean, date, list, or text | The reference value that you want to aggregate over a period of time.  This argument must be a line item, and this line item must have Time as a dimension. |
| *Start period* | Number, date, time period | The starting value for the aggregation. This period is included in the aggregation.  When you omit this argument, it considers the entire range of the time period for the calculation. |
| *End period* | Number, date, time period  Mirrors *Start period* data type | The ending value for the aggregation.  When you omit this argument, it defaults to the same value as the *Start period*. |
| *Aggregation method* | Keyword | The aggregation method to use.  The available keywords are SUM, AVERAGE, MIN, MAX, ANY, ALL, FIRSTNONBLANK, LASTNONBLANK, and TEXTLIST.  There's more information in the **Aggregation method keywords** section below. |

The TIMESUM function returns a value that matches the data type of the *Line item to aggregate* argument.

| **Keyword** | **Data type** | **Purpose** |
| --- | --- | --- |
| SUM | Number | Adds the input values |
| AVERAGE | Number | Calculates the average of the input values |
| MIN | Number, date | Identifies the minimum input value |
| MAX | Number, date | Identifies the maximum input value |
| ANY | Boolean | Checks and returns TRUE if at least one input value is TRUE |
| ALL | Boolean | Checks and returns TRUE only if all input values are TRUE |
| FIRSTNONBLANK | Date, list, text | Returns the first non-blank input value |
| LASTNONBLANK | Date, list, text | Returns the last non-blank input value |
| TEXTLIST | Text | Concatenates the input values with a ", " separator to create a single text value |

When you omit the *Aggregation method* argument, the default behavior depends on the data type of the *Line item to aggregate* argument:

- If the data type of the *Line item to aggregate* is a number, the default method is SUM.
- If the data type of the *Line item to aggregate* is boolean, the default method is ANY.
- If the data type of the *Line item to aggregate* is a date, list, or text, the default method is FIRSTNONBLANK.

In Polaris:

- You can only use a number or Boolean type for the *Line item* to aggregate arguments.
- If you only provide a value for the *Start period* argument and not the *End period* argument, the TIMESUM function aggregates all values from the *Start period* through to the end of the applicable time range.
- When you use date values for the *Start period* and *End period* arguments, they behave as expected.
- If *Start period* or *End period* are outside the range of the time dimension, then TIMESUM returns 0.

In the Classic Engine:

- You can use a value with a data type of number, Boolean, date, list, or text for the *Line item to aggregate* argument.
- If you only provide a value for the *Start period* argument and not the *End period* argument, the TIMESUM function returns the value from the *Start period*.
- When you use date values for the *Start period* and *End period* arguments, the behavior is inverted. This means that the date for the *Start period* should be in the period where aggregation ends and the date for the *End period* should be in the period where aggregation begins.

`TIMESUM(Revenue, -2, 0, SUM)`

This formula sums the values for the *Revenue* line item from two periods before the current period through to the current period. This is inclusive of the start and end period.

The default aggregation method used when you omit the *Aggregation method* argument varies based on the data type of the *Line item to aggregate* argument. If the data type of the *Line item to aggregate* argument is:

- Number, the default behavior is to SUM.
- Boolean, the default behavior is ANY.
- Date, list, or text. The default behavior is FIRSTNONBLANK.

No matter how the inputs are passed to the function, TIMESUM still aggregates values between two periods in the time dimension:

- When used with a single argument, `TIMESUM (lineItem)`, it aggregates values across the whole time dimension, from the start period defaults to the first period in the dimension. The end period defaults to the last period in the dimension.
- When used with numerical arguments, such as `TIMESUM(lineItem, 1, 3)`, those numbers represent offsets from **Current Period**, so in this example the start period is `'Current Period' + 1` and the end period is `'Current Period' + 3`.

The *Start period* and *End period* arguments for the TIMESUM function define the period to aggregate values over. The TIMESUM function only returns a single value, the aggregated value over this defined range of periods. As a result, it's best to use the TIMESUM in a line item without the **Time** dimension to optimize module performance.

Use *Start period* and *End period* arguments with number, date, or time period data type values. You can use different data types for each argument.

For example, you can specify a time period for the *Start period* argument, and 0 (zero) for the *End period* argument. This aggregates values between the specified time period and the current period and updates automatically as the current period changes.

- The *Line item to aggregate* argument must have Time as a dimension.
- You must define a **Current Period** in **Model Settings** to use a number value for the *Start period* or *End period* arguments.
- If you use a date value for either the *Start period* or *End period* argument, their positions are swapped. This means that the *End period* argument should be a date in the period when aggregation begins and *Start period* should a the date in the period when aggregation ends.

In this example, there are two modules. The first module contains the **Time** dimension on columns, and the *Revenue* line item on rows. The module is named *Revenue 2021*, which is referenced in later formulas.

The **Current Period** in this model, as defined in **Model Settings > Time**, is *May 21*.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** | **May 21** | **Jun 21** | **Jul 21** | **Aug 21** | **Sep 21** | **Oct 21** | **Nov 21** | **Dec 21** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 101,480 | 130,156 | 117,021 | 122,556 | 123,160 | 143,432 | 130,784 | 134,415 | 115,309 | 117,279 | 128,835 | 108,029 |

The second module contains only line items, which each contain formulas. These formulas highlight how you can use the *Start period* and *End period* arguments to specify the period of aggregation.

The reason the formulas are in a separate module is because you should use TIMESUM in a module without the **Time** dimension to improve performance.

| Revenue for all periods   `TIMESUM(Revenue 2021.Revenue)` | 1,472,456 |
| --- | --- |
| Revenue for 2 months ago   `TIMESUM(Revenue 2021.Revenue, -2)` | 117,021 |
| Revenue from 2 months ago to current period   `TIMESUM(Revenue 2021.Revenue, -2, 0)` | 362,737 |
| Revenue for duration of Spring campaign   `TIMESUM(Revenue 2021.Revenue, TIME.'Jan 21', TIME.'Apr 21')` | 471,213 |

The first formula, in the *Revenue for all periods* line item, uses only the *Revenue* line item for the *Line item to aggregate* argument. This means that the formula uses the default behavior for TIMESUM and sums all values in the module. This behavior can be useful when you use **Weeks: General** in **Model Settings > Time**, as this **Calendar Type** does not contain a summary of all periods.

The second formula, in the *Revenue for 2 months ago* line item, uses the *Revenue* line item for the *Line item to aggregate* argument. The formula uses *\-2* for the *Start period* argument. This means that the formula returns only the value from the period two periods before the **Current Period**, May 21. In this case, this is the value 117,021 from Mar 21.

In Polaris, this formula would aggregate all values from and including Mar 21 until the last period in the applicable time range.

The third formula, in the *Revenue from 2 months ago to current period* line item, uses the *Revenue* line item for the *Line item to aggregate* argument. The formula uses *\-2* for the *Start period* argument and *0* for the *End period* argument. This means that the formula sums the values from two periods before the current period, through to the current period. In this case, this is 362,737, the sum of the values for Mar 21, Apr 21, and May 21.

The fourth formula, in the *Revenue for duration of Spring campaign* line item, uses the *Revenue* line item for the *Line item to aggregate* argument. The formula uses references to the **Time** dimension for the *Start period* and *End period* arguments. *Time.'Jan 21'* and *Time.'Apr 21'* respectively. This means that the formula sums the values of the *Revenue* line item for and between these periods. As the formula uses references to the **Time** dimension, the values for the formula do not change as the current period in the **Model Calendar** changes.

In this example, there are two modules. The first module contains the **Time** dimension on columns, and multiple line items on rows. The module is named *Initiative KPIs 2021*, which is referenced in later formulas.

The **Current Period** in this model, as defined in **Model Settings > Time**, is Dec 21.

|  | **Jan 21** | **Feb 21** | **Mar 21** | **Apr 21** | **May 21** | **Jun 21** | **Jul 21** | **Aug 21** | **Sep 21** | **Oct 21** | **Nov 21** | **Dec 21** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 101,480 | 130,156 | 117,021 | 122,556 | 123,160 | 143,432 | 130,784 | 134,415 | 115,309 | 117,279 | 128,835 | 108,029 |
| Promotion Active? |  |  |  |  |  |  |  |  |  |  |  |  |
| New product release date |  |  | 3/24/2021 | 4/30/2021 |  |  | 7/14/2021 |  |  | /10/15/2021 | 11/1/2021 |  |
| Product name |  |  | Apple pie | Cinnamon swirl |  |  | Sugar donut |  |  | Lemon meringue pie | Mille-feuille |  |

The second module contains only line items, which each contain formulas. These formulas highlight the behavior of the different keywords for the *Aggregation method* argument. Each formula uses a *Start period* of *\-2* and *End period* of *0*. This means that they apply to the values for *Oct 21*, *Nov 21*, and *Dec 21*.

The reason the formulas are in a separate module is because you should use TIMESUM in a module without the **Time** dimension to optimize performance.

| Total revenue for last 3 months  `TIMESUM(Initiative KPIS 2021.Revenue, -2, 0, SUM)` | 354,143 |
| --- | --- |
| Average revenue for last 3 months  `TIMESUM(Initiative KPIS 2021.Revenue, -2, 0, AVERAGE)` | 118,048 |
| Lowest revenue for last 3 months  `TIMESUM(Initiative KPIS 2021.Revenue, -2, 0, MIN)` | 108,029 |
| Highest revenue for last 3 months  `TIMESUM(Initiative KPIS 2021.Revenue, -2, 0, MAX)` | 128,835 |
| Promotion active last 3 months?  `TIMESUM(Initiative KPIS 2021.Promotion active?, -2, 0, ANY)` |  |
| Promotion active for entirety of last 3 months?  `TIMESUM(Initiative KPIS 2021.Promotion active?, -2, 0, ALL)` |  |
| First product release date in last 3 months  `TIMESUM(Initiative KPIS 2021.New product release date, -2, 0, FIRSTNONBLANK)` | 10/15/2021 |
| Last product release in last 3 months  `TIMESUM(Initiative KPIS 2021.New product release date, -2, 0, LASTNONBLANK)` | 11/1/2021 |
| Names of products released in last 3 months  `TIMESUM(Initiative KPIS 2021.Product name, -2, 0, TEXTLIST)` | Lemon meringue pie, Mille-feuille |

The first four line items contain formulas that show the behavior of the SUM, AVERAGE, MIN, and MAX keywords, respectively. These aggregation methods can only be used with number-formatted values. For the values of Oct 21, Nov 21, and Dec 21, which are 117,279, 128,835, and 108,029, the formulas:

- Sum each of the three values for a total of 354,143.
- Return the mean average of the three values, 118,048.
- Return the lowest value of the three, 108,029.
- Return the highest value of the three, 128,835.

The fifth and sixth line items contain formulas that show the behavior of the ANY and ALL keywords, respectively. These aggregation methods can only be used with Boolean-formatted values. For the values of Oct 21, Nov 21, and Dec 21, the formulas:

- Check if any of the Boolean values are TRUE. As two of the three are, it returns a value of TRUE.
- Check if all of the Boolean values are TRUE. As only two of the three are, it returns a value of FALSE.

The seventh and eighth line items contain formulas that show the behavior of the FIRSTNONBLANK and LASTNONBLANK keywords, respectively. These aggregation methods can be used with number-, date-, list-, or text-formatted values. In this case, the line items contain dates that represent product release dates. For the values of Oct 21, Nov 21, and Dec 21, the formulas:

- Return the first non-blank date-formatted value, 10/15/2021.
- Return the last non-blank date-formatted value, 11/1/2021.

The ninth line item contains a formula that shows the behavior of the TEXTLIST keyword. This aggregation method can only be used with text-formatted values. The formula concatenates the values of Oct 21, Nov 21, and Dec 21, separating each value with a comma. It returns *Lemon meringue pie, Mille-feuille*.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftimesum-45c3bc48-4d80-490d-9b18-76af505c6907&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>