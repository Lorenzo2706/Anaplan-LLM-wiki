---
title: "CUMIPMT | Anapedia"
source: "https://help.anaplan.com/cumipmt-2f6eca23-c0b6-4b4b-a68c-1def28d2dab6"
author:
published:
created: 2026-08-31
description: "The CUMIPMT function calculates the cumulative interest paid on a loan over a period given equal payments made to the balance."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The CUMIPMT function calculates the cumulative interest paid on a loan over a period given equal payments made to the balance.

For example, you can use the CUMIPMT function to see how much interest is paid during different periods for a loan.

`CUMIPMT(Interest rate, Number of periods, Principal, Start period, End period[, Timing])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Interest rate* (required) | Number | The interest rate of the loan.  This argument is best used with the [Percent format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a), as 0.1 equals 10%, and so on. |
| *Number of periods* (required) | Number | The number of periods that the *Principal* is paid over. |
| *Loan balance* (required) | Number | The total amount to be paid between the *Start period* and *End period*. |
| *Start period* (required) | Number | The period to start calculating cumulative interest from. |
| *End period* (required) | Number | The period to stop calculating cumulative interest at. |
| *Timing* | Number | Whether interest payments are made at the start or end of each period.  If a payment is made at the start of the period, that period's interest applies to it. You can enter a value of 0 or 1 for this argument. If you enter:  - 0, payments are made at the end of each period (the default if this argument is omitted) - 1, payments are made at the start of each period |

The CUMIPMT function returns a number, which is the cumulative interest payable between the *Start period* and *End period*.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The *Number of periods* argument enables you to specify the number of periods the loan is paid over. The *Start period* and *End period* arguments enable you to specify what range of periods to calculate the cumulative interest for.

The value you provide for the *Interest rate* argument must match the *Number of periods* arguments. For example, if the periods are years, you should provide the annual interest rate.

For any values you give the IPMT function via an argument, or that the function returns:

- a positive value represents money you receive, such as a dividend or loan
- a negative value represents money paid, such as a deposit or interest payment

The *Start period* and *End period* arguments must be less than the *Number of periods* argument.

[CUMIPMT](https://support.office.com/en-us/article/cumipmt-function-61067bb0-9016-427d-b95b-1a752af0e606)

In this example, there's a *Scenarios* list on columns, and line items on rows. There's one line item for each argument of the CUMIPMT function.

Each item in the *Scenario* list uses the same value for the *Interest rate*, *Number of periods*, and *Loan Balance* arguments. However, they use different values for the *Start period* and *End period* arguments. This highlights how the cumulative interest payable changes in different periods over the duration of a loan.

|  | **Scenario 1** | **Scenario 2** | **Scenario 3** | **Scenario 4** | **Scenario 5** | **Scenario 6** |
| --- | --- | --- | --- | --- | --- | --- |
| Interest rate | 2.5% | 2.5% | 2.5% | 2.5% | 2.5% | 2.5% |
| Number of periods | 30 | 30 | 30 | 30 | 30 | 30 |
| Loan Balance | 300,000 | 300,000 | 300,000 | 300,000 | 300,000 | 300,000 |
| Start period | 1 | 1 | 30 | 1 | 15 | 1 |
| End period | 1 | 1 | 30 | 15 | 30 | 30 |
| Timing | 0 | 1 | 0 | 0 | 0 | 0 |
| Cumulative interest paid  `CUMIPMT(Interest rate, Number of periods, Loan balance, Start period, End period, Timing)` | \-7,500 | 0 | \-349.59 | \-92,465.29 | \-42,211.51 | \-129,998.77 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcumipmt-2f6eca23-c0b6-4b4b-a68c-1def28d2dab6&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>