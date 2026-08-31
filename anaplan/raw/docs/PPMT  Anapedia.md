---
title: "PPMT | Anapedia"
source: "https://help.anaplan.com/ppmt-03959ad1-338f-4c10-8623-f6dc86bc7c23"
author:
published:
created: 2026-05-02
description: "The PPMT function calculates how much of a payment is allocated to its principal part rather than interest. The function assumes a consistent interest rate and payment timings in each period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The PPMT function calculates how much of a payment is allocated to its principal part rather than interest. The function assumes a consistent interest rate and payment timings in each period.

For example, you could use the PPMT function to calculate equity built during a loan.

`PPMT(Interest rate, Period to examine, Number of periods, Present value [, Future value] [, Timing])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Interest rate* (required) | Number | The interest rate of the loan.  This argument is best used with the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a), as 0.1 equals 10%, and so on. |
| *Period to examine* (required) | Number | The period to return the amount paid towards the principal for. |
| *Number of periods* (required) | Number | The number of periods that the loan is paid over. |
| *Present value* (required) | Number | The principal amount of the loan. |
| *Future value* | Number | The amount of loan left after the final payment is made. If omitted, this is assumed to be 0. |
| *Timing* | Number | Whether interest payments are made at the start or end of each period.  0 means payments are made at the start of each period. A non-zero value means payments are made at the end.  If omitted, payments are made at the start of each period. |

The PPMT function returns a number.

The *Period to examine* and *Number of periods* arguments enable you to specify the number of periods interest accrues over, and which period to view the interest for.

The values you provide for the *Interest rate*, *Period to examine*, and *Number of periods* arguments should all use the same time scale. For example, if the periods are years, you should provide the annual interest rate.

For any values you give for the *Present value* or *Future value* arguments, or that the PPMT function returns:

- A positive value represents money you receive, such as a dividend or loan.
- A negative value represents money paid, such as a deposit or interest payment.

[PPMT](https://support.office.com/en-us/article/ppmt-function-c370d9e3-7749-4ca4-beea-b06c6ac95e1b)

In this example, a module has eight line items on rows, and a *Loans* list on columns. The first four line items contain data for each of the required arguments for the PPMT function. The fifth line item uses the PPMT function to calculate the principal paid.

The sixth and seventh line items contain data for the optional arguments for the PPMT function. The eighth line item uses the PPMT function to calculate the principal paid with both optional arguments applied.

|  | **Loan 1** | **Loan 2** | **Loan 3** | **Loan 4** | **Loan 5** |
| --- | --- | --- | --- | --- | --- |
| Present value | 70,000 | 330,000 | 500,000 | 500,000 | 500,000 |
| Interest rate | 5.5% | 3.5% | 1.44% | 1.44% | 1.44% |
| Period to examine | 1 | 1 | 10 | 10 | 10 |
| Number of periods | 6 | 25 | 25 | 25 | 25 |
| Principal paid  `PPMT(Interest rate, Period to examine, Number of periods, Present value)` | \-10,162.53 | \-11,547.06 | \-19,058.85 | \-19,058.85 | \-19,058.85 |
| Future value | 0 | 30,000 | 0 | 10,000 | 10,000 |
| Timing | 0 | 0 | 0 | 0 | 1 |
| Amended principal paid  `PPMT(Interest rate, Period to examine, Number of periods, Present value, Future value, Timing)` | \-10,162.53 | \-12,596.79 | \-19,058.85 | \-19,440.02 | \-19,164.06 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fppmt-03959ad1-338f-4c10-8623-f6dc86bc7c23&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>