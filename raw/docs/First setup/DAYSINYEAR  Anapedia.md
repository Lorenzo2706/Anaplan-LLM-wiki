---
title: "DAYSINYEAR | Anapedia"
source: "https://help.anaplan.com/daysinyear-3f9b1d05-fd59-4d27-90a7-55e3d4a2beba"
author:
published:
created: 2026-05-02
description: "The DAYSINYEAR function returns the number of days in a year you specify."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use DAYSINYEAR to check if a year contains 365 or 366 days and plan accordingly.

`DAYINYEAR(Year)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Year* | Number | The year to determine the number of days within. |

The DAYSINYEAR function returns a numeric result.

`DAYSINYEAR(2024)`

This example returns the number of days in the year 2024. This is 366 days, as 2024 is a leap year.

The DAYSINYEAR function returns a value of zero for any values outside of the date range of 01/01/1900-12/31/2399.

[YEAR](https://support.office.com/en-us/article/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9)

| **Formula** | **Description** | **Result** |
| --- | --- | --- |
| `DAYSINYEAR(2020)` | Returns the number of days in the year 2020. | 366 |
| `DAYSINYEAR(2021)` | Returns the number of days in the year 2021. | 365 |
| `DAYSINYEAR(2022)` | Returns the number of days in the year 2022. | 365 |
| `DAYSINYEAR(2023)` | Returns the number of days in the year 2023. | 365 |
| `DAYSINYEAR(2024)` | Returns the number of days in the year 2024. | 366 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fdaysinyear-3f9b1d05-fd59-4d27-90a7-55e3d4a2beba&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>