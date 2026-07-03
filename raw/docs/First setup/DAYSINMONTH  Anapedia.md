---
title: "DAYSINMONTH | Anapedia"
source: "https://help.anaplan.com/daysinmonth-bd6910ee-1a50-43e7-8bc1-c672899149df"
author:
published:
created: 2026-05-02
description: "The DAYSINMONTH function returns the number of days in a month you specify."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use DAYSINMONTH to check if a leap year occurs in February, so you can plan accordingly.

`DAYSINMONTH(Year, Month)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Year* | Number | The year that contains the month to determine the number of days within. |
| *Month* | Number | The month to determine the number of days within.  Should be a number between 1 and 12 (the function returns a value of 0 for numbers outside this range). |

The DAYSINMONTH function returns a numeric result.

`DAYSINMONTH(2024, 2)`

This example returns the number of days in February 2024. This is 29, as 2024 is a leap year.

The DAYSINMONTH function returns a value of zero for any values outside of the date range of 01/01/1900-12/31/2399.

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `DAYSINMONTH(2023, 1)` | Returns the number of days in January 2023. | 31 |
| `DAYSINMONTH(2023, 2)` | Returns the number of days in February 2023. | 28 |
| `DAYSINMONTH(2024, 1)` | Returns the number of days in January 2024. | 31 |
| `DAYSINMONTH(2024, 2)` | Returns the number of days in February 2024. | 29 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fdaysinmonth-bd6910ee-1a50-43e7-8bc1-c672899149df&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>