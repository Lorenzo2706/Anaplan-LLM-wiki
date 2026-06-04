---
title: "COLLECT | Anapedia"
source: "https://help.anaplan.com/collect-887a0bce-034b-4a0b-9e5f-262ec2f47e35"
author:
published:
created: 2026-05-02
description: "Use the COLLECT function in a module that includes a line item subset to pull the source line item values into the module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use the COLLECT function in a module that includes a line item subset to pull the source line item values into the module.

For example, you might want to compare 2 months and view the variance between those months for different line items.

To create a comparison, create a line item subset to group line items from different modules in one place. Then, create a staging module and pull the data from the line items into the module using the COLLECT function.

`COLLECT()`

The COLLECT function does not use any arguments.

This function returns numbers.

The source modules must contain the line items in the line item subset used in the result module. The result module must have a line item subset as a dimension.

See [Line item subset example](https://help.anaplan.com/84d95131-a83a-45b7-ba41-71defbb732ff) for more information.

The function's behavior may change if there's a mismatch in list hierarchy for the applied dimensions of line items within a line item subset.

The COLLECT function can be used to collect values from a line item subset. In this example, the two source modules for the line item subset are named *P&L* and *Fixed assets*. The aggregated total for FY22 from the Time dimension displays as the single column in both modules, and line items on rows.

*P&L* module:

|  | **FY22** |
| --- | --- |
| Sales last year | 1200000 |
| % increase | 5% |
| Sales | 1260000 |
| Margin % | 40% |
| Cost of sales | 756000 |
| **Gross margin** | 2016000 |
| Headcount | 10 |
| Cost per employee |  |
| Staff costs | 360000 |
| Rent & rates | 12000 |
| Utilities | 12000 |
| Marketing | 12000 |
| IT costs | 12000 |
| Total overheads | 408000 |
| **Operating profit** | 1608000 |

*Revenue* module:

|  | **FY22** |
| --- | --- |
| Assets sold | 720000 |
| Buildings | 120000 |
| Fixtures | 120000 |
| Software | 120000 |
| Patents | 120000 |
| Assets purchased | 480000 |

The line items selected for the line item subset display as below within **Line item subsets**. The line item subset is named *Receipts and payments*.

|  | **Receipts and payments** |
| --- | --- |
| **P&L** |  |
| Sales last year |  |
| % increase |  |
| Sales |  |
| Margin % |  |
| Cost of sales |  |
| **Gross margin** |  |
| Headcount |  |
| Cost per employee |  |
| Staff costs |  |
| Rent & rates |  |
| Utilities |  |
| Marketing |  |
| IT costs |  |
| Total overheads |  |
| **Operating profit** |  |
| **Fixed assets** |  |
| Assets sold |  |
| Buildings |  |
| Fixtures |  |
| Software |  |
| Patents |  |
| Assets purchased |  |

The above line item subset is used for the rows dimension in a *Receipts and payments* module. FY22 from the Time dimension is on columns, and a single line item is on the pages dimension. The line item contains this formula: `COLLECT()`. This collects the values from the *P&L* and *Fixed assets* source modules:

|  | **FY22** |
| --- | --- |
| Sales | 1260000 |
| Cost of sales | 756000 |
| **Gross margin** | 2016000 |
| Staff costs | 360000 |
| Rent & rates | 12000 |
| Utilities | 12000 |
| Marketing | 12000 |
| IT costs | 12000 |
| **Total overheads** | 408000 |
| Operating profit | 1608000 |
| Assets sold | 720000 |
| Buildings | 120000 |
| Fixtures | 120000 |
| Software | 120000 |
| Patents | 120000 |
| Assets purchased | 480000 |

The [Variance report staging module](https://help.anaplan.com/37dfbb55-5a5b-4277-8ffe-0d9dd419efa4) step of the [Line item subset example](https://help.anaplan.com/84d95131-a83a-45b7-ba41-71defbb732ff) contains an example of how you can use the COLLECT function.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcollect-887a0bce-034b-4a0b-9e5f-262ec2f47e35&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>