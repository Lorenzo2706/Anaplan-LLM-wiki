---
title: "NPV | Anapedia"
source: "https://help.anaplan.com/npv-d2331d84-a431-4179-8c82-9846f0c453d0"
author:
published:
created: 2026-05-02
description: "The NPV function calculates the net present value for a series of cash flows, which can be positive (inflows) or negative (outflows), using a constant interest rate."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The NPV function calculates the net present value for a series of cash flows, which can be positive (inflows) or negative (outflows), using a constant interest rate.

NPV of an investment enables you to know how much a future investment is worth today. You could use the `NPV()` function to assess whether an investment is worthwhile while accounting for depreciation.

`NPV(Discount rate, Cash flows)`

`NPV(Discount rate, Cash flows, Dates, Transaction list)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Discount rate* | Number | An estimate discount rate of the NPV. Note that this argument is expressed as a decimal number rather than a percentage, so 0.1 is equivalent to 10%. |
| *Cash flows* | Number | A line item that contains a series of positive and negative values that represent cash inflow and outflow.  The line item used for this argument must have a time dimension. |

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Discount rate* | Number | An estimate discount rate of the NPV. Note that this argument is expressed as a decimal number rather than a percentage, so 0.1 is equivalent to 10%. |
| *Cash flows* | Number | A series of positive and negative values that represent cash inflow and outflow.  This must have the list used for the *Transaction list* argument as a dimension. |
| *Dates* | Date | The dates associated with each value of the *Cash flows* argument. |
| *Transaction list* | List | A list of transaction *identifiers*, which must be a common dimension of the *Cash flows* and *Dates* argument. |

The `NPV()` function returns a number.

| **Behavior** | **Classic** | **Polaris** |
| --- | --- | --- |
| First cash flow selection   (applies only to the dates variant) | If the cash flows are out of order with respect to the *Transaction list* dimension, Classic can associate the wrong index to some cash flows, which leads to unreliable results. | Polaris always gives you the right result regardless of the order of transactions. |
| Scaling factor (applies only to the time dimension variant) | In Classic, the scaling factor is determined entirely by the time scale of the time dimension of *Cash flows*, regardless of the actual structure of that time dimension. | In Polaris, the scaling factor is the average number of leaf periods (of the time dimension of *Cash flows*) in a fiscal year.  **Note:** When using the general weeks calendar type, that is, when there are no fiscal years, weekly transactions are converted to daily transactions and a fixed 365 scaling factor is used, the same as in Classic. |
| *Discount rate* is NaN | Result is undefined. | Returns NaN. |
| Blank values in *Dates* | Treated as 12/31/1899 (one day before Anaplan era). | Returns NaN, regardless of cash flow values. |
| Target line item dimensionality | Can be dimensioned by *Transaction list*. | For the time dimension variant, the target line item can't have a time dimension. |
| *Transaction list* is empty | The engine rejects the formula and gives an error message. | In Polaris, this function always returns 0 unless the *Discount rate* is NaN, in that case, the function returns NaN instead. |

The `NPV()` function has two different syntaxes. One operates on transactions expressed as cash flows with a time dimension. And the other one operates on transactions expressed as pairs of dates and cash flows.

$\hspace{10 mm} \text{NPV} = \displaystyle\sum_{i = 0}^{n} \dfrac{C_i}{(1+\rho)^{ik_T}}$

$\hspace{10 mm} \text{NPV} = \displaystyle\sum_{i = 0}^{n} \dfrac {C_i}{(1+\rho)^{{d_i}/{365}}}$

where

- *n* is the total number of cash flows.
- *C* *<sub>i</sub>* is the cash flow at the *i* -th time period.
- *ρ* is the discount rate.
- *k* *<sub>T</sub>* is the scaling factor based on ‌time granularity.
- *d* *<sub>i</sub>* is the number of days between the date of the *i* -th transaction and the date of the earliest transaction in the sequence.

The function automatically scales based on the given time granularity and chooses the proper scaling factor *k* *<sub>T</sub>*. This lets users ‌express the calculation at the original time granularity of the investments being analyzed. Also, ‌users can compare the resulting NPV values with different time granularities, without any additional calculations. See below how the scaling factor is calculated in each case:

| **Engine** | **Calendar type** | **Scaling factor,** ***kT*****, used** |
| --- | --- | --- |
| **Polaris** | Fiscal years | Number of leaf periods / number of years counted in the time dimension of the *Cash flows* line item. |
|  | General weeks | 365 for weeks and days.  Weekly transactions are treated as if they were daily transactions occurring on the first day of the week. |
| **Classic** | Fiscal years | Based on the timescale of the *Cash flows* time dimension:  - 1 for years - 2 for half years - 4 for quarters - 12 for months |
|  | General weeks | 365 for weeks and days**.**  Weekly transactions are treated as if they were daily transactions occurring on the first day of the week. |

Using a [production list](https://help.anaplan.com/f8a7c584-8620-4a61-b8f4-d56a19eb8c20) as a *Transaction list*, such as the **Users** list, can unexpectedly affect calculation results as these lists are meant to change over the lifetime of the model.

In Polaris, the dates variant can't be used if the target module has a dimension that is related to *Transaction list*.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fnpv-d2331d84-a431-4179-8c82-9846f0c453d0&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>