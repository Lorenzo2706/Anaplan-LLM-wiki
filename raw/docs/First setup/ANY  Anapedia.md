---
title: "ANY | Anapedia"
source: "https://help.anaplan.com/any-8ad06ef2-8b17-4f21-b2df-990eca953ac4"
author:
published:
created: 2026-05-02
description: "The ANY aggregation function returns a TRUE result for any value that matches specific Boolean criteria in a source module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ANY aggregation function returns a TRUE result for any value that matches specific Boolean criteria in a source module.

For example, you can use the ANY aggregation function to identify any employees in an organization with a car allowance.

`Source[ANY: Mapping, ANY: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source* | Boolean | The line item to search for any values that match criteria in the *Mapping* argument. |
| *Mapping* | List | The line item to use as search criteria.  If you want to provide multiple criteria, you can repeat this argument. |

The ANY aggregation function returns a Boolean result.

- The list that is used to format the mapping line item in the source module must be a dimension of the target line item that uses the ANY aggregation function.
- The dimensions of the mapping line item must also appear in the source line item.
- You can reference the *Users* list with the ANY function. However, you cannot reference specific users in the *Users* list as this is [production data](https://help.anaplan.com/d129b0e3-34f7-4135-b27e-5956ed56e8d2), which can change and make your formula invalid.

[OR](https://support.microsoft.com/en-gb/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0?ui=en-us&rs=en-gb&ad=gb)

In this example, the *Salary Details* module has line items on columns, and the *Employees* list on rows. The module shows employee car allowances and city locations.

The *Car Allowance* line item has a Boolean data type. The *City* line item has a list data type, and is formatted on the *City* list.

|  | **Car Allowance** | **City** |
| --- | --- | --- |
| Employee A |  | London |
| Employee B |  | New York |
| Employee C |  | San Francisco |
| Employee D |  | Edinburgh |
| Employee E |  | New York |
| Employee F |  | London |

Below, the *Any Employee Car Allowance* module has the *Any location with employee car allowances* line item on rows, and the *City* list on columns. The *Any location with employee car allowances* line item has a Boolean data type.

The formula uses the ANY aggregation function to show any employees with car allowances in different cities.

|  | **London** | **Edinburgh** | **San Francisco** | **New York** |
| --- | --- | --- | --- | --- |
| Any location with employee car allowances  `Salary Details.Car Allowance[ANY: Salary Details.City]` |  |  |  |  |

Another example uses the *Salary Details* module above, but includes an additional *Department* line item. *Department* has a list data type, and is formatted on the *Department* list.

|  | **Car Allowance** | **Department** | **City** |
| --- | --- | --- | --- |
| Employee A |  | Sales | London |
| Employee B |  | Sales | London |
| Employee C |  | HR | San Francisco |
| Employee D |  | HR | San Francisco |
| Employee E |  | Marketing | New York |
| Employee F |  | Finance | Edinburgh |

Below, the *Any Employee Car Allowance* module has the *Any location with employee car allowances* line item on pages, the *Department* list on rows, and the *City* list on columns. The *Any location with employee car allowances* line item has a Boolean data type.

The formula in the line item uses the ANY aggregation function to show any employees with car allowances in different cities and departments: `Salary Details.Car Allowance[ANY: Salary Details.City, ANY: Salary Details.Department]`.

The formula only returns a TRUE result if any employee in a department or city has a car allowance.

|  | **London** | **Edinburgh** | **San Francisco** | **New York** |
| --- | --- | --- | --- | --- |
| Sales |  |  |  |  |
| HR |  |  |  |  |
| Marketing |  |  |  |  |
| Finance |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fany-8ad06ef2-8b17-4f21-b2df-990eca953ac4&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>