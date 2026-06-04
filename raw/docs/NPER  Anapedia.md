---
title: "NPER | Anapedia"
source: "https://help.anaplan.com/nper-2a6f370b-1c7d-490b-898e-0938abc47dc8"
author:
published:
created: 2026-05-02
description: "The NPER function calculates the required number of periods to achieve a certain value for a loan or investment. This is based on a given interest rate, consistent payments, and opening and closing balance."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The NPER function calculates the required number of periods to achieve a certain value for a loan or investment. This is based on a given interest rate, consistent payments, and opening and closing balance.

For example, you can use the NPER function to calculate how long it will take to pay off a loan.

`NPER(Interest rate, Payments, Present value [, Residual value] [, Timing])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Interest rate* (required) | Number | The interest rate of the loan.  This argument is best used with the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a), as 0.1 equals 10%, and so on. |
| *Payments* (required) | Number | The amount paid each period.  You can omit this argument by entering 0, but in this case, you must provide a value for the *Present value* argument. |
| *Present value* (required) | Number | The present value of the instrument, or initial investment. |
| *Residual value* | Number | The amount of loan left after the final payment is made. If omitted, this is assumed to be 0. |
| *Timing* | Number | Whether interest payments are made at the start or end of each period.  0 means payments are made at the start of each period. A non-zero value means payments are made at the end.  If omitted, payments are made at the start of each period. |

The NPER function returns a number.

Financial functions are currently unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

For any values you give the NPER function via an argument, or that the function returns:

- A positive value represents money you receive, such as a dividend or loan.
- A negative value represents money paid, such as a deposit or interest payment.

You can recreate the behavior of the NPER function. To do this, you can use the formula below with the values you would otherwise use as arguments for the NPER function.

`IF Interest rate = 0 THEN (-Present value - Residual value) / Payments ELSE LOG((-Interest rate * Residual value + Payments * (1 + Interest rate * Timing))/(Interest rate * Present value + Payments * (1 + Interest rate * Timing)))/LOG(1 + Interest rate)`

[NPER](https://support.office.com/en-gb/article/NPER-function-240535b5-6653-4d2d-bfcf-b6a38151d815)

In this example, there is a *Contracts* list on columns, and line items on rows. There are five line items, one for each argument of the NPER function. The sixth line item uses the NPER function to calculate the required payments.

|  | **Contract 1** | **Contract 2** | **Contract 3** | **Contract 4** | **Contract 5** |
| --- | --- | --- | --- | --- | --- |
| Interest rate | 4% | 4% | 8% | 1% | 15% |
| Payments | 300 | 300 | 300 | 1,500 | \-5,000 |
| Present value | 10,000 | 10,000 | 10,000 | \-50,000 | \-50,000 |
| Residual value | 0 | 0 | 0 | 25,000 | 0 |
| Timing | 0 | 1 | 0 | 0 | 0 |
| Number of periods  `NPER(Interest rate, Payments, Present value, Residual value, Timing)` | \-21.6 | \-21.04 | \-16.88 | \-13.14 | \-6.556 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fnper-2a6f370b-1c7d-490b-898e-0938abc47dc8&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>