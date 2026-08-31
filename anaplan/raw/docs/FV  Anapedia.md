---
title: "FV | Anapedia"
source: "https://help.anaplan.com/fv-9edb6d8b-3001-458f-b620-ebe2a70cc992"
author:
published:
created: 2026-05-02
description: "The FV function calculates the future value of an investment. The future value is the lump sum or closing balance received at the end of an investment."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The FV function calculates the future value of an investment. The future value is the lump sum or closing balance received at the end of an investment.

For example, you could use this function to calculate the return of an investment given a certain interest rate, principal, and regular payments into the investment.

`FV(Interest rate, Number of periods, Payments [, Present value] [, Payment timing])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Interest rate* (required) | Number | The interest rate per period. |
| *Number of periods* (required) | Number | The number of periods that the investment is held for, and that the interest rate applies to. |
| *Payments* (required) | Number | The amount paid into the investment each period. |
| *Present value* | Number | The present value of the investment at the start of the investment period.  If you omit this argument, the present value is equivalent to 0. |
| *Payment timing* | Number | Determines whether each payment is made at the start or end of each period. If a payment is made at the start of the period, that period's interest applies to it.  You can enter a zero or non-zero number for this argument. If you enter:  - zero, payments are made at the end of each period - a non-zero number, payments are made at the start of each period |

The FV function returns a number, which is the future value of the investment.

You can create a formula equivalent to the FV function with the structure below:

`IF Rate = 0 THEN - Present value - Payments * Number of periods ELSE - Present value * POWER(1 + Interest rate, Number of periods) - Payments * (1 + Interest rate * Payment timing) * (POWER(1 + Rate, Number of periods) - 1) /Interest rate`

In this formula, *Payment timing* must either be zero for payments to be made at the start of each period, or non-zero for the end.

For any values you give the FV function via an argument, or that the function returns:

- a positive value represents money you receive, such as a dividend or loan
- a negative value represents money paid, such as a deposit or interest payment

You must use the same time period granularity for the *Interest rate*, *Number of periods*, and *Payments* arguments. This means that they should all consistently be monthly, quarterly, annual, or over another interval.

For example, an investment might over 3 years. In this case, there are 36 monthly periods, and you should divide the annual interest rate by 12. Additionally, any payment amounts should also be monthly.

[FV](https://support.office.com/en-gb/article/FV-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3)

In this example, the five items within the *Contracts* list are on columns. On rows, there are six line items. One for each of the arguments of the FV function, and one that uses the FV function to calculate the future value of each contract.

|  | **Contract 1** | **Contract 2** | **Contract 3** | **Contract 4** | **Contract 5** |
| --- | --- | --- | --- | --- | --- |
| Interest rate | 0.4000% | 0.7974% | 0.7974% | 0.4000% | 0.4000% |
| Number of periods | 24 | 12 | 12 | 12 | 12 |
| Payments | 300 | 0 | 300 | 300 | 300 |
| Present value | \-10,000 | \-10,000 | \-10,000 | \-10,000 | \-10,000 |
| Payment timing | 0 | 0 | 0 | 0 | 1 |
| Future value  `FV(Interest rate, Number of periods, Payments, Present value, Payment timing)` | 3,464 | 11,000 | 7,238 | 6,810 | 6,796 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ffv-9edb6d8b-3001-458f-b620-ebe2a70cc992&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>