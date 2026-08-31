---
title: "MIN (Aggregation function)"
source: "https://help.anaplan.com/min-aggregation-function-7ddb1ccd-5fcd-4af0-aa7a-eadfa2c3a7c8"
author:
published:
created: 2026-05-02
description: "The MIN aggregation function returns the minimum value from a line item in a source module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The MIN aggregation function returns the minimum value from a line item in a source module.

For example, you can use the MIN aggregation function to show the lowest salary level across different departments in an organization.

`Source[MIN: Mapping, MIN: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source* | Number, date, time period | The line item to search for the minimum value.  The minimum value for a number is the lowest value, and the minimum value for a date or time period is the earliest date or time period. |
| *Mapping* | List | The line item to use as search criteria.  If you want to provide multiple criteria, you can repeat this argument. |

The MIN aggregation function returns a result of the same data type as the *Line item* argument. When there are no values to compare, the function returns 0 for numbers and BLANK for other data types.

In Polaris, when comparing a blank date value to a non-blank date value, the MIN function returns the non-blank value.

In the Classic Engine, when comparing a blank date value to a non-blank date value, the MIN function returns the blank value.

- The list that's used to format the mapping line item in the source module, must be a dimension of the target line item that uses the MIN aggregation function.
- The dimensions of the mapping line item must also appear in the source line item.
- You can reference the *Users* list with the MIN function. However, you can't reference specific users in the *Users* list as this is production data, which can change and make your formula invalid.

In this example, the *Salary Details* module has line items on columns, and the *Employees* list on rows. The module shows employee salaries and city locations.

The *Salary* line item has a number data type. The *City* line item has a list data type, and is formatted on the *City* list.

|  | **Salary** | **City** |
| --- | --- | --- |
| Employee A | 35,000 | London |
| Employee B | 54,000 | New York |
| Employee C | 38,000 | San Francisco |
| Employee D | 24,000 | Edinburgh |
| Employee E | 60,000 | New York |
| Employee F | 40,000 | London |

Below, the *Minimum Salary Details* module has the *Minimum salary for city* line item on rows, and the *City* list on columns.

The formula uses the MIN aggregation function to show the lowest salary in each city.

|  | **London** | **Edinburgh** | **San Francisco** | **New York** |
| --- | --- | --- | --- | --- |
| Minimum salary for city  `Salary Details.Salary[MIN: Salary Details.City]` | 35,000 | 24,000 | 38,000 | 54,000 |

Another example uses the *Salary Details* module as above, but includes an additional *Department* line item. *Department* has a list data type, and is formatted on the *Department* list.

|  | **Salary** | **Department** | **City** |
| --- | --- | --- | --- |
| Employee A | 35,000 | HR | London |
| Employee B | 54,000 | Finance | New York |
| Employee C | 38,000 | Marketing | San Francisco |
| Employee D | 27,500 | Marketing | San Francisco |
| Employee E | 24,000 | Sales | Edinburgh |
| Employee F | 60,000 | Finance | New York |
| Employee G | 40,000 | HR | London |

Below, the *Minimum Salary Details* module has the *Minimum salary for city* line item on pages, the *Department* list on rows, and the *City* list on columns.

The formula in the line item uses the MIN aggregation function to show the lowest salary in different departments and cities: `Salary Details.Salary[MIN: Salary Details.City, MIN: Salary Details.Department]`.

For example, the lowest salary in the Finance department in New York is 54,000.

|  | **London** | **Edinburgh** | **San Francisco** | **New York** |
| --- | --- | --- | --- | --- |
| HR | 35,000 |  |  |  |
| Finance |  |  |  | 54,000 |
| Sales |  | 24,000 |  |  |
| Marketing |  |  | 27,500 |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmin-aggregation-function-7ddb1ccd-5fcd-4af0-aa7a-eadfa2c3a7c8&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>