---
title: "Anaplan Support"
source: "https://support.anaplan.com/formulas-80dbd4d9-a674-430c-8dd6-87f64db40d29"
author:
published:
created: 2026-05-04
description: "Planual rules regarding Formulas."
tags:
  - "clippings"
---
[Classic](https://support.anaplan.com/classic-a182c8c4-2e69-437d-8871-78346dc8b1bf "Classic")

Avoid using multiple IFs. It's better to split the formula into several line items and use LOOKUPs or alternative constructs.

If it takes you longer than one simple sentence to describe what the formula is doing, it's probably too long. Try not to mix expressions.

If the expression is repeated in the formula (or other modules), put it on a separate line item. “Calculate once, reference many times.”

Treat text strings with caution. Try and avoid multiple joins and split common joins to separate line items. Make use of IF ISBLANK() when joining text. If the strings are empty, set to BLANK.

If a text string join is needed, create the joins in the smaller lists first to minimize the size of the text strings.

[Formula Optimization in Anaplan](https://community.anaplan.com/t5/Knowledge/Formula-Optimization-in-Anaplan/ta-p/41663)

It's faster to check A=B rather than A-B=0.

In Classic, booleans take up 1/8th of the space as a number, so unless a numeric value is needed try to use TRUE or FALSE.

SUM and LOOKUP used in the same expression generally cause large formula calculations and may cause intermediate relationship calculations, especially if Time is a dimension or when the source and target structures are very different. Splitting them into different modules and line items considerably reduces the size of the intermediate calculations.

[Formulas and their effect on model performance](https://community.anaplan.com/t5/Best-Practices/Formulas-and-their-effect-on-model-performance/ta-p/33556)

Use these summary methods to minimize the use of additional line items and IF statements.

For long timescales, using PREVIOUS is faster than CUMULATE due to the number of "reads" required for the calculation. So, the expression should be: 'Calc line item' = 'data line item' + PREVIOUS('Calc line item') rather than CUMULATE('data line item').

| 2.02-10a Short timescales | Where the number of periods is small (Year granularity with a small number of years), CUMULATE is faster. |
| --- | --- |

[Performance Issues with Cumulate Over Lists](https://community.anaplan.com/t5/Best-Practices/Performance-Issues-with-Cumulate-Over-Lists/ta-p/57720)

TEXTLIST() requires a lot of memory for calculations and should be avoided if possible. Using two dimensional modules and Boolean flags with ANY is a better alternative. Other alternatives are using FIRSTNONBLANK as well as LASTNONBLANK.

Avoid direct references to list item, for example, IF ITEM(list)=list.xx. Instead, use a SYS module with a line item having a Boolean format as this makes the formula more dynamic (multiple members can use the same logic).

[Decreasing the Length of Your Formulas](https://community.anaplan.com/t5/Best-Practices/Decreasing-the-Length-of-Your-Formulas/ta-p/88467)

Don't use POST for simple data offsets as OFFSET, LAG, or MOVINGSUM are more efficient.

Avoid hard coding using SELECT if possible. Use a constants module and LOOKUP instead.

| 2.02-14a Versions | It's OK to use SELECT for versions. |
| --- | --- |
| 2.02-14b For top-level items on lists | It's OK to reference the Top Level item of a list with SELECT. For other items (actual list members), it's better to use mock parent lists and additional modules. |

[Decreasing the length of your formulas](https://community.anaplan.com/t5/Best-Practices/Decreasing-the-Length-of-Your-Formulas/ta-p/88467)

Doing a FINDITEM() on blank values is inefficient as the function has to traverse the entire list before it returns a blank.

If the majority are NOT blank:

- If ISNOTBLANK(Line Item) THEN FINDITEM(List, line item) ELSE BLANK

If the majority are blank:

- If ISBLANK(Line Item) THEN BLANK else FINDITEM(List, line item)

The number of blanks the line item could have will dictate which formula to use.. If there are more blanks than not, then use the second formula. If Line Item is more dense (has more values than not), then the first formula should be used. If there will never be blanks in the values, there's no need to check for blanks:

- FINDITEM(List, line item)

In multiple conditional statements, try and include a conditional to prevent further referencing in the formula if the condition is satisfied.

For formula efficiency, put the conditional with the most common occurrence first in the formula.

The engine works more efficiently when calculations are broken up into separate line items. So, break up formula expressions where possible. This is especially true for calculations that are referenced many times and/or calculations that don't change often.

[Decreasing the Length of Your Formulas](https://community.anaplan.com/t5/Best-Practices/Decreasing-the-Length-of-Your-Formulas/ta-p/88467)

Always refer back to the ultimate source if possible, to avoid creating more dependencies than necessary. This allows more parallel calculations to be run, increasing efficiency and speeding up calculations.

[Best Practices for Module Design](https://community.anaplan.com/t5/Best-Practices/Best-Practices-for-Module-Design/ta-p/35993)

RANK is a calculation-intensive formula that can't multi-thread. Used in conjunction with large lists, it can lead to poorly performing calculations. The same applies to RANKCUMULATE and ISFIRSTOCCURRENCE.

TIMESUM formulas shouldn't be used in a line item that applies to Time as the calculation will be duplicated for each time period.

If the line item contains time periods, consider using MOVINGSUM or YEARTODATE. If you need the total for the entire timescale, consider using line item\[Select: Time. All Periods\].

Back to top