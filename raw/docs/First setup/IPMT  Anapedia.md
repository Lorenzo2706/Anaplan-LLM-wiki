---
title: "IPMT | Anapedia"
source: "https://help.anaplan.com/ipmt-03571086-c1de-40b1-8706-a3f22eed7c36"
author:
published:
created: 2026-05-02
description: "The IPMT function calculates the amount of interest to be paid on a loan in a given payment period. The function assumes a consistent interest rate and payment timings in each period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The IPMT function calculates the amount of interest to be paid on a loan in a given payment period. The function assumes a consistent interest rate and payment timings in each period.

For example, you can use the IPMT function to see how the interest due changes over the duration of loan.

`IPMT(Interest rate, Period to examine, Number of periods, Present value [, Future value] [, Payment timing])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Interest rate* (required) | Number | The interest rate to apply to the *Present value* each period.  This argument is best used with the [**Percent** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a), as 0.1 equals 10%, and so on. |
| *Period to examine* (required) | Number | The period to return the amount of interest due for. |
| *Number of periods* (required) | Number | The number of periods that the *Present value* is paid over. |
| *Present value* (required) | Number | The total amount to be paid over the *Number of periods*. |
| *Future value* | Number | The amount of loan left after the final payment is made. If omitted, this assumed to be 0. |
| *Payment timing* | Number | Whether interest payments are made at the start or end of each period.  0 means payments are made at the end of each period. This is the default behavior if you omit the *Payment timing* argument.  A non-zero value means payments are made at the start end. |

The IPMT function returns a number, which is the interest due in the *Period to examine*.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The *Period to examine* and *Number of periods* arguments enable you to specify the number of periods interest accrues over, and the period for which to view the interest.

The values you provide for the *Interest rate*, *Period to examine*, and *Number of periods* arguments should all use the same time scale. For example, if the periods are years, you should provide the annual interest rate.

For any values you give for the *Present value* or *Future value* arguments, or that the IPMT function returns:

- A positive value represents money you receive, such as a dividend or loan.
- A negative value represents money paid, such as a deposit or interest payment.

[IPMT](https://support.office.com/en-us/article/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f)

In this example, a module has eight line items on rows, and a *Loans* list on columns. The first four line items contain data for each of the required arguments for the IPMT function. The fifth line item uses the IPMT function to calculate interest payments.

The sixth and seventh line items contain data for the optional arguments for the IPMT function. The eighth line item uses the IPMT function to calculate interest payments with both optional arguments applied.

|  | **Loan 1** | **Loan 2** | **Loan 3** | **Loan 4** | **Loan 5** |
| --- | --- | --- | --- | --- | --- |
| Present value | 70,000 | 330,000 | 500,000 | 500,000 | 500,000 |
| Interest rate | 5.5% | 3.5% | 1.44% | 1.44% | 1.44% |
| Period to examine | 1 | 1 | 10 | 10 | 10 |
| Number of periods | 6 | 25 | 25 | 25 | 25 |
| Interest due for period  `IPMT(Interest rate, Period to examine, Number of periods, Present value)` | \-3,850 | \-8,475.38 | \-4,898.82 | \-4,898.82 | \-4,898.82 |
| Future value | 0 | 30,000 | 0 | 10,000 | 10,000 |
| Timing | 0 | 0 | 0 | 0 | 1 |
| Amended interest due for period  `IPMT(Interest rate, Period to examine, Number of periods, Present value, Future value, Timing)` | \-3,850 | \-8,195.87 | \-4,898.82 | \-4,852.79 | \-4,783.90 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fipmt-03571086-c1de-40b1-8706-a3f22eed7c36&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>