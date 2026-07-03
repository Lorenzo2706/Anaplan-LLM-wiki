---
title: "MAX (Aggregation function)"
source: "https://help.anaplan.com/max-aggregation-function-29e3860f-86d6-419d-83f3-9c4af61a59d2"
author:
published:
created: 2026-05-02
description: "The MAX aggregation function returns the maximum value from a line item in a source module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The MAX aggregation function returns the maximum value from a line item in a source module.

For example, you can use the MAX aggregation function to show the most recent employee start date in different departments and cities.

`Source[MAX: Mapping, MAX: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source* | Number, date, time period | The line item to search for the maximum value.  The maximum value for a number is the highest value, and the maximum value for a date or time period is the most recent date or time period. |
| *Mapping* | List | The line item to use as search criteria.  If you want to provide multiple criteria, you can repeat this argument. |

The MAX aggregation function returns a result of the same data type as the *Source* line item.

- The list that is used to format the mapping line item in the source module must be a dimension of the target line item that uses the MAX aggregation function.
- The dimensions of the mapping line item must also appear in the source line item.
- You can reference the *Users* list with the MAX function. However, you cannot reference specific users in the *Users* list as this is [production data](https://help.anaplan.com/d129b0e3-34f7-4135-b27e-5956ed56e8d2), which can change and make your formula invalid.

In this example, the *Employee details* module has line items on columns, and the *Employees* list on rows. The module shows employee start months and city locations.

The *Start month* line item has a time period data type. The *City* line item has a list data type, and is formatted on the *City* list.

|  | **Start month** | **City** |
| --- | --- | --- |
| Employee A | Jan 21 | London |
| Employee B | Jul 21 | New York |
| Employee C | Jul 21 | San Francisco |
| Employee D | Sept 21 | Edinburgh |
| Employee E | Feb 21 | New York |
| Employee F | Apr 21 | London |
| Employee G | Aug 21 | Edinburgh |

Below, the *New employees FY21* module has the *Most recent hire* line item on rows, and the *City* list on columns.

The formula uses the MAX aggregation function to show the most recent hire in each city.

|  | **London** | **Edinburgh** | **San Francisco** | **New York** |
| --- | --- | --- | --- | --- |
| **Most recent hire**   `Employee details.Start month[MAX: Employee details.City]` | Apr 21 | Sept 21 | Jul 21 | Jul 21 |

In this example, the *Employee details* module has line items on columns, and the *Employees* list on rows. The module shows employee start months and their year.

The *Start month* line item has a time period data type. The *Year* line item has a list data type, and is formatted on the *Year* list.

|  | **Start month** | **Year** |
| --- | --- | --- |
| Employee A | Jan 21 | FY21 |
| Employee B | Apr 25 | FY25 |
| Employee C | Apr 23 | FY23 |
| Employee D | Oct 24 | FY24 |
| Employee E | Apr 25 | FY25 |
| Employee F | Dec 25 | FY25 |

Below, the *New employees* module has the *Last hire in the year* line item on rows, and the *Year* list on columns.

The formula uses the MAX aggregation function to show the last hire in each year.

|  | **FY21** | **FY22** | **FY23** | **FY24** | **FY25** |
| --- | --- | --- | --- | --- | --- |
| **Last hire in the year   **`Employee details.Start month[MAX: Employee details.Year]` | Jan 21 |  | Apr 23 | Oct 24 | Dec 25 |

Another example uses the *Employee Details* module as above, but includes an additional *Department* line item. *Department* has a list data type, and is formatted on the *Department* list.

|  | **Start month** | **Department** | **City** |
| --- | --- | --- | --- |
| Employee A | Jan 21 | HR | London |
| Employee B | Jul 21 | Finance | New York |
| Employee C | Jul 21 | Sales | San Francisco |
| Employee D | Sept 21 | Marketing | Edinburgh |
| Employee E | Feb 21 | Finance | New York |
| Employee F | Apr 21 | HR | London |
| Employee G | Aug 21 | Marketing | Edinburgh |

Below, the *New employees FY21* module has the *Most recent hire* line item on pages, the *Department* list on rows, and the *City* list on columns.

The formula in the line item uses the MAX aggregation function to show most recent hires in different departments and cities: `Employee Details.Start month[MAX: Employee Details.City, MAX: Employee Details.Department]`.

For example, the latest hire in the HR department in London was Apr 21.

|  | **London** | **Edinburgh** | **San Francisco** | **New York** |
| --- | --- | --- | --- | --- |
| HR | Apr 21 |  |  |  |
| Finance |  |  |  | Jul 21 |
| Sales |  |  | Jul 21 |  |
| Marketing |  | Sept 21 |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmax-aggregation-function-29e3860f-86d6-419d-83f3-9c4af61a59d2&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>