---
title: "IRR | Anapedia"
source: "https://help.anaplan.com/irr-3e65abd3-a8d8-4cb7-af34-937232ae79c5"
author:
published:
created: 2026-05-02
description: "The IRR function calculates the internal rate of return for a series of cash flows, which can be positive (inflows) or negative (outflows)."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The IRR function calculates the internal rate of return for a series of cash flows, which can be positive (inflows) or negative (outflows).

The function automatically chooses the appropriate timescale based on the cash flow time period, for example, daily, monthly, quarterly, etc. Cash flows at the week timescale are treated as if they happened on the first day of the week. And cash flows at the day timescale are treated as if they happened on that day.

`IRR (Cash flows [, Estimate])`

`IRR (Cash flows, Dates, Transaction list [, Estimate])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Cash flows* (required) | Number | A line item that contains a series of positive and negative values that represent cash inflow and outflow.  The line item used for this argument must have a time dimension. |
| *Estimate* (optional) | Number | An estimate discount rate of the IRR. Note that this argument is expressed as a decimal number rather than a percentage, so 0.1 is equivalent to 10%.  This argument is optional. If omitted, the default value is 0.1. |

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Cash flows* (required) | Number | A series of positive and negative values that represent cash inflow and outflow.  Must have the list used for the *Transaction list* argument as a dimension. |
| *Dates* (required) | Date | The dates associated with each value of the *Cash flows* argument. |
| *Transaction list* (required) | List | A list of transaction *identifiers*, which must be a common dimension of the *Cash flows* and *Dates* argument. |
| *Estimate* (optional) | Number | An estimate discount rate of the IRR. This argument accepts a number but interprets it as a percentage. For example, a value of 0.1 is treated as 10%.  This argument is optional. If omitted, the default value is 0.1. |

The `IRR()` function returns a number.

| **Behavior** | **Classic** | **Polaris** |
| --- | --- | --- |
| First cash flow selection   (applies only to the dates variant) | If the cash flows are out of order with respect to the *Transaction list* dimension, Classic can associate the wrong index to some cash flows, which leads to unreliable results. | Polaris always gives you the right result regardless of the order of transactions. |
| Scaling factor   (applies only to the time dimension variant) | In Classic, the scaling factor is determined entirely by the time scale of the time dimension of *Cash flows*, regardless of the actual structure of that time dimension. | In Polaris, the scaling factor is the average number of leaf periods (of the time dimension of *Cash flows*) in a fiscal year.  **Note:** When using the general weeks calendar type, that is, when there are no fiscal years, weekly transactions are converted to daily transactions and a fixed 365 scaling factor is used, the same as in Classic. |
| *Estimate* is NaN | Result is undefined. | Returns NaN. |
| All cash flows are zero | Returns NaN if values are exactly zero. | Returns 0 if values are tolerantly equal to zero. |
| Blank values in *Dates* | Treated as 12/31/1899 (one day before Anaplan era). | Returns NaN, regardless of cash flow values. |
| Target line item dimensionality | Can be dimensioned by *Transaction list*. | Can't be dimensioned by *Transaction list*.  For the time dimension variant, the target line item can't have a time dimension. |
| *Transaction list* is empty | Returns NaN. | In Polaris, this function always returns 0 unless the *Estimate* is NaN, in that case, the function returns NaN instead. |

The `IRR()` function has two different syntaxes. One operates on transactions expressed as cash flows with a time dimension. And the other one operates on transactions expressed as pairs of dates and cash flows, which is a direct equivalent of Excel's XIRR. They both are called IRR, but take different arguments. The syntax that applies depends on whether you use more or less than two arguments with the function.

$\hspace{10 mm} 0 = \text{NPV} = \displaystyle\sum_{i=0}^{n}\dfrac{C_i}{(1+\rho)^{ik_T}}$

$\hspace{10 mm} 0 = \text{NPV} = \displaystyle\sum_{i = 0}^{n}\dfrac{C_i}{(1+\rho)^{d_i/{365}}}$

where

- *n* is the total number of cash flows.
- *C* *<sub>i</sub>* is the cash flow at the *i* -th time period.
- *ρ* is the discount rate.
- *k* *<sub>T</sub>* is the scaling factor based on ‌time granularity.
- *d* *<sub>i</sub>* is the number of days between the date of the *i* -th transaction and the date of the earliest transaction in the sequence.

The function automatically scales based on the given time granularity and chooses the appropriate scaling factor *k* *<sub>T</sub>*. This lets users ‌express the calculation at the original time granularity of the investments being analyzed. Also, ‌users can compare the resulting IRR values with different time granularities, without any additional calculations. See below how the scaling factor is calculated in each case:

| **Engine** | **Calendar type** | **Scaling factor,** ***kT*****, used** |
| --- | --- | --- |
| **Polaris** | Fiscal years | Number of leaf periods/number of years counted in the time dimension of the *Cash flows* line item. |
|  | General weeks | 365 for weeks and days.  Weekly transactions are treated as if they were daily transactions occurring on the first day of the week. |
| **Classic** | Fiscal years | Based on the timescale of the *Cash flows* time dimension:  - 1 for years - 2 for half years - 4 for quarters - 12 for months |
|  | General weeks | 365 for weeks and days.  Weekly transactions are treated as if they were daily transactions occurring on the first day of the week. |

Using a [production list](https://help.anaplan.com/f8a7c584-8620-4a61-b8f4-d56a19eb8c20) as a *Transaction list*, such as the **Users** list, can unexpectedly affect calculation results as these lists are meant to change over the lifetime of the model.

- In Polaris, the dates variant can't be used if the target module has a dimension that is related to *Transaction list*.
- The function accepts any cash flow sequence. However, if the *Cash flows* argument doesn't contain at least one positive and one negative value, the equation is guaranteed to have no solution. In that case, `IRR()` will return NaN, unless ‌all the cash flows are 0 and you're using Polaris.

- [IRR](https://support.office.com/en-us/article/IRR-function-64925eaa-9988-495b-b290-3ad0c163c1bc)
- [XIRR](https://support.office.com/en-us/article/XIRR-function-de1242ec-6477-445b-b11b-a303ad9adc9d)

**Excel's IRR** function assumes cash flows are equally spaced and fixes the time scaling factor *k* *<sub>T</sub>* = 1, regardless of the actual time intervals between them. This function matches Anaplan’s time dimension variant of IRR when the *Cash flows* line item ‌has its timescale set to **Years**, and only in that case.

**Excel's XIRR** function accepts actual dates and always uses *k* *<sub>T</sub>* \= 1/365, assuming daily compounding. It always returns an annualized IRR of the sequence of cash flows. This makes it easier to compare the IRR of different cash flow sequences, but requires the user to perform extra calculations to derive the appropriate transaction dates when the cash flows are given at a time granularity other than days.

**Anaplan’s IRR** function returns an annual equivalent rate by automatically choosing the appropriate *k* *<sub>T</sub>* based on the timescale of the *Cash flows* line item, for example, daily, monthly, quarterly. Refer to the table above to see how the scaling factor *k* *<sub>T</sub>* is determined for each case. This enables the users to compare the resulting IRR values without further conversions.

Polaris has a stricter verification threshold to ensure the reliability and comparability of IRR results in financial analysis. In theory, Polaris may return NaN for IRR more often than Classic or Excel. But in practice, this rarely happens, and only when very small changes in the IRR result in unusually large changes in the NPV, typically when the IRR is very close to −1. This approach helps improve the trustworthiness and reliability of Polaris compared to Classic or Excel.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Firr-3e65abd3-a8d8-4cb7-af34-937232ae79c5&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>