---
title: "RATE | Anapedia"
source: "https://help.anaplan.com/rate-00695a6a-3250-41e8-9f43-549609d19188"
author:
published:
created: 2026-05-02
description: "The RATE function calculates the interest rate for a loan or investment based on the duration, payment amounts, and the present and future values."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The RATE function calculates the interest rate for a loan or investment based on the duration, payment amounts, and the present and future values.

For example, you can use the RATE function to calculate the monthly interest rate for a loan.

`RATE(Number of periods, Payments, Present value[, Future value[, Payment timing[, Rate estimate]]])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of periods* (required) | Number | The number of periods that the interest rate is applied to.  Any decimal value will be rounded up to its ‌nearest whole number. |
| *Payments* (required) | Number | The amount paid into the investment each period. |
| *Present value* (required) | Number | The present value of the investment. |
| *Future value* (optional) | Number | The future value of the investment. |
| *Payment timing* (optional) | Number | Determines whether each payment is made at the start or end of each period. If a payment is made at the start of the period, that period's interest applies to it.  You can enter a value of 0 or 1 for this argument. If you enter:  - 0, payments are made at the start of each period - 1, payments are made at the end of each period |
| *Rate estimate* (optional) | Number | The estimated interest rate. |

The RATE function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

For any values you provide to the RATE function as arguments, or that the function returns:

- A positive value represents money you receive, such as a dividend or loan.
- A negative value represents money you pay, such as a deposit or interest payment.

[RATE](https://support.microsoft.com/en-gb/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce?ui=en-us&rs=en-gb&ad=gb)

For example, an *Interest rates* module has the *Contracts* list on columns and line items on rows. The module shows different loan amounts and monthly payments for two customer contracts.

The formula in the *Monthly interest rate* line item calculates the periodic interest rate for each contract. Here, the *Number of periods*, 59.5, in **Contract 2** is rounded up to its nearest whole number, 60, during the calculation.

|  | **Contract 1** | **Contract 2** |
| --- | --- | --- |
| Loan amount | $5,000 | $7,500 |
| Monthly payment | \-$95 | \-$135 |
| Number of periods | 60 | 59.5 |
| Monthly interest rate  `RATE(Number of periods, Monthly payment, Loan amount)` | 0.440039% | 0.255868% |

In this example, the formula in the *Annual interest rate* line item calculates the yearly interest rate for each contract. Here, the *Number of periods*, 58.7, in **Contract 2** is rounded up to its nearest whole number, 59, during the calculation.

|  | **Contract 1** | **Contract 2** |
| --- | --- | --- |
| Loan amount | $5,000 | $7,500 |
| Monthly payment | \-$95 | \-$135 |
| Number of periods | 60 | 58.7 |
| Annual interest rate  `RATE(Number of periods, Monthly payment, Loan amount) * 12` | 5.28047% | 2.4324% |

In this example, the formula calculates the required interest rates for two investments to return a future value. Here, the *Number of periods*, 36.3, in **Contract 2** is rounded up to its nearest whole number, 36, during the calculation.

|  | **Contract 1** | **Contract 2** |
| --- | --- | --- |
| Number of periods | 12 | 36.3 |
| Payments | 0 | 0 |
| Current value | \-$5,000 | \-$7,500 |
| Future value | $15,000 | $25,000 |
| Interest rate  `RATE(Number of periods, Payments, Current value, Future value)` | 9.58727% | 3.40092% |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Frate-00695a6a-3250-41e8-9f43-549609d19188&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>