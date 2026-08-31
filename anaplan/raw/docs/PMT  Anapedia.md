---
title: "PMT | Anapedia"
source: "https://help.anaplan.com/pmt-07d126f7-dd4d-4510-b15d-add22fc527fd"
author:
published:
created: 2026-05-02
description: "The PMT function calculates the payments due for a loan or annuity over a specified number of periods, given a consistent interest rate and payment amount."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The PMT function calculates the payments due for a loan or annuity over a specified number of periods, given a consistent interest rate and payment amount.

For example, you can use the PMT function to calculate the monthly amount required to pay back a loan given each payment is equal.

`PMT(Interest rate, Number of periods, Present value [, Future value] [, Timing])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Interest rate* (required) | Number | The interest rate of the loan.  This argument is best used with the [**Percent** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a), as 0.1 equals 10%, and so on. |
| *Number of periods* (required) | Number | The number of periods that the loan is paid over. |
| *Present value* (required) | Number | The present value of the instrument, or initial investment. |
| *Future value* | Number | The amount of loan left after the final payment is made. If omitted, this assumed to be 0. |
| *Timing* | Number | Whether interest payments are made at the start or end of each period. If a payment is made at the start of the period, that period's interest applies to it.  A value of 0 means payments are made at the end of each period. This is the default behavior if you omit the *Payment timing* argument.  A non-zero value means payments are made at the start end. |

The PMT function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The *Number of periods* argument enables you to specify the number of periods interest accrues over.

The values you provide for the *Interest rate* and *Number of periods* arguments should use the same time scale. For example, if the periods are years, you should provide the annual interest rate.

For any values you give for the *Present value* or *Future value* arguments, or that the PMT function returns:

- A positive value represents money you receive, such as a dividend or loan.
- A negative value represents money paid, such as a deposit or interest payment.

You can recreate the behavior of the PMT function. To do this, you can use the formula below with the values you would otherwise use as arguments for the PMT function.

`IF Interest rate = 0 THEN (-Present value -Future value) / Number of periods ELSE Interest Rate / ((1 - POWER(1 + Interest rate, Number of periods)) * (1 + Interest Rate * Timing)) * (Future value + Present value * POWER(1 + Interest rate, Number of periods))`

[PMT](https://support.office.com/en-gb/article/PMT-function-0214da64-9a63-4996-bc20-214433fa6441)

In this example, there is a *Contracts* list on columns, and line items on rows. There are five line items, one for each argument of the PMT function. The sixth line item uses the PMT function to calculate the required payments.

|  | **Contract 1** | **Contract 2** | **Contract 3** | **Contract 4** | **Contract 5** |
| --- | --- | --- | --- | --- | --- |
| Interest rate | 8.00% | 8.00% | 5.00% | 3.50% | 0.10% |
| Number of periods | 10 | 10 | 25 | 4 | 8 |
| Present value | \-10,000 | \-10,000 | \-250,000 | \-5,000 | \-1,000 |
| Future value | 0 | 0 | 0 | 0 | 4,000 |
| Timing | 0 | 1 | 0 | 0 | 1 |
| Payment due each period  `PMT(Interest rate, Number of periods, Present value, Future value, Timing)` | 1,490.29 | 1,379.90 | 17,738.11 | 1,361.26 | \-348.59 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpmt-07d126f7-dd4d-4510-b15d-add22fc527fd&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>