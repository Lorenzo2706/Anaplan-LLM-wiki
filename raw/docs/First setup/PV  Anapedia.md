---
title: "PV | Anapedia"
source: "https://help.anaplan.com/pv-e245a888-0e90-47a4-943c-556a497e8a77"
author:
published:
created: 2026-05-02
description: "The PV function calculates the present value of an investment or the principal value of a loan."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The PV function calculates the present value of an investment or the principal value of a loan.

For example, you can use the PV function to calculate the amount you can borrow for a loan, or the amount you need to invest to achieve a financial goal.

`PV(Interest rate, Number of periods, Payments, Future value, Payment timing)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Interest rate* (required) | Number | The interest rate per period. |
| *Number of periods* (required) | Number | The total number of periods. |
| *Payments* (required) | Number | The amount paid each period. |
| *Future value* (required) | Number | The future value of the investment or loan.  For a loan, the future value is 0. |
| *Payment timing* (required) | Number | Determines whether each payment is made at the start or end of each period. If a payment is made at the start of the period, that period's interest applies to it.  You can enter a value of 0 or 1 for this argument. If you enter:  - 0, payments are made at the end of each period. - 1, payments are made at the start of each period. |

The PV function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

For any values you give the PV function via an argument, or that the function returns:

- a positive value represents money you receive, such as a dividend or loan.
- a negative value represents money paid, such as a deposit or interest payment.

You must use the same time periods for the *Interest rate*, *Number of periods*, and *Payments* arguments. For example, an investment might over 3 years. In this case, there are 36 monthly periods, and you should divide the annual interest rate by 12. Additionally, any payment amounts should also be monthly.

[PV](https://support.microsoft.com/en-us/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd?ui=en-us&rs=en-us&ad=us)

In this example, a module has the *Mortgages* list on columns, and line items on rows. The *Interest rate* line item uses the [**Percentage** format](https://help.anaplan.com/46d8e4e5-544e-48a8-9c4b-d9c240ff4c53).

The formula uses the PV function to calculate the amount a customer can borrow for each mortgage. The interest rate is divided by 12 to reflect monthly payments at the end of each period.

|  | **Mortgage 1** | **Mortgage 2** |
| --- | --- | --- |
| Interest rate | 5% | 5% |
| Number of periods | 360 | 300 |
| Payments | 1000 | 550 |
| Principal loan value  `PV(Interest rate / 12, Number of periods, Payments, 0, 1)` | \-$187,057.79 | \-$94,475.04 |

In this example, a module has the *Customers* list on columns, and line items on rows. The *Interest rate* line item uses the [**Percentage** format](https://help.anaplan.com/46d8e4e5-544e-48a8-9c4b-d9c240ff4c53).

The formula uses the PV function to calculate the required investment amount for each customer. For example, if a customer wants to save $50,000 over 10 years at an interest rate of 5%, they need to initially invest $30,358.

|  | **Customer 1** | **Customer 2** |
| --- | --- | --- |
| Interest rate | 5% | 7.5% |
| Number of periods | 120 | 36 |
| Future value | $50,000 | $10,000 |
| Present investment value  `PV(Interest rate / 12, Number of periods, 0, Future value, 0)` | \-$30,358 | \-$7,991 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpv-e245a888-0e90-47a4-943c-556a497e8a77&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>