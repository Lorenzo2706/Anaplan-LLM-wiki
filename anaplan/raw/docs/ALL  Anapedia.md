---
title: "ALL | Anapedia"
source: "https://help.anaplan.com/all-c9035c86-1e45-4774-9463-cc5aca76fc7e"
author:
published:
created: 2026-05-02
description: "The ALL aggregation function returns a TRUE result for all values that match specific Boolean criteria in a source module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ALL aggregation function returns a TRUE result for all values that match specific Boolean criteria in a source module.

For example, you can use the ALL aggregation function to identify all employees who received a bonus in the first quarter of a year.

`Source[ALL: Mapping, ALL: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source* | Boolean | The line item to search for all values that match criteria in the *Mapping* argument. |
| *Mapping* | List | The line item to use as search criteria.  If you want to provide multiple criteria, you can repeat this argument. |

The ALL aggregation function returns a Boolean result.

In Polaris, the default value for cells not mapped with the ALL aggregation function is FALSE.

In the Classic Engine, the default value is TRUE.

- The list that is used to format the mapping line item in the source module must be a dimension of the target line item that uses the ALL aggregation function.
- The dimensions of the mapping line item must also appear in the source line item.
- You can reference the *Users* list with the ALL function. However, you cannot reference specific users in the *Users* list as this is [production data](https://help.anaplan.com/d129b0e3-34f7-4135-b27e-5956ed56e8d2), which can change and make your formula invalid.

[AND](https://support.microsoft.com/en-gb/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9?ui=en-us&rs=en-gb&ad=gb)

In this example, the *Salary Details* module has line items on columns, and the *Employees* list on rows. The module shows employee bonuses and city locations.

The *Bonus* line item has a Boolean data type. The *City* line item has a list data type, and is formatted on the *City* list.

|  | **Bonus** | **City** |
| --- | --- | --- |
| Employee A |  | London |
| Employee B |  | New York |
| Employee C |  | San Francisco |
| Employee D |  | Edinburgh |
| Employee E |  | New York |
| Employee F |  | London |

Below, the *All Employee Bonus Locations* module has the *All locations with employee bonuses* line item on rows, and the *City* list on columns. The *All locations with employee bonuses* line item has a Boolean data type.

The formula uses the ALL aggregation function to show cities where all employees have received a bonus.

|  | **London** | **Edinburgh** | **San Francisco** | **New York** |
| --- | --- | --- | --- | --- |
| All locations with employee bonuses  `Salary Details.Bonus[ALL: Salary Details.City]` |  |  |  |  |

Another example uses the *Salary Details* module as above, but includes an additional *Department* line item. *Department* has a list data type, and is formatted on the *Department* list.

|  | **Bonus** | **Department** | **City** |
| --- | --- | --- | --- |
| Employee A |  | Sales | London |
| Employee B |  | Sales | New York |
| Employee C |  | HR | San Francisco |
| Employee D |  | HR | San Francisco |
| Employee E |  | Sales | New York |
| Employee F |  | Sales | London |

Below, the *All Employee Bonus Locations* module has the *All locations with employee bonuses* line item on pages, the *Department* list on rows, and the *City* list on columns. The *All locations with employee bonuses* line item has a Boolean data type.

The formula in the line item uses the ALL aggregation function to show all employees with bonuses in different departments and cities: `Salary Details.Bonus[ALL: Salary Details.City, ALL: Salary Details.Department]`.

The formula only returns a TRUE result if all employees in the same city and department received a bonus.

|  | **London** | **San Francisco** | **New York** |
| --- | --- | --- | --- |
| Sales |  |  |  |
| HR |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fall-c9035c86-1e45-4774-9463-cc5aca76fc7e&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>