---
title: "INPERIOD | Anapedia"
source: "https://help.anaplan.com/inperiod-3b64fe69-0d31-49b8-ab40-e7c1a3d01137"
author:
published:
created: 2026-05-02
description: "The INPERIOD function returns a TRUE result for a date that falls under a time period or a module's Time dimension. It returns FALSE for all other dates."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The INPERIOD function returns a TRUE result for a date that falls under a time period or a module's Time dimension. It returns FALSE for all other dates.

For example, you can use the INPERIOD function to show new employees at a company in the last year.

`INPERIOD(Date to test, Time period)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Date to test* | Date | The date to test if it falls under a time period or Time dimension. |
| *Time period* (Optional) | Time period | The time period to test.  If your module does not have Time as a dimension, this argument is required. |

The INPERIOD function returns a Boolean result.

The first argument in the function must be a date and not a time period.

In this example, an *Employee Details* module has line items on rows, the *Employees* list on columns, and Time on pages. *Start date* has a date format, and *New employees FY21* has a Boolean format.

The formula returns a TRUE result for new employees in FY21. It returns FALSE for all other employees.

|  | **Employee A** | **Employee B** | **Employee C** | **Employee D** |
| --- | --- | --- | --- | --- |
| Start date | 12/03/2021 | 5/06/2020 | 15/03/2021 | 17/08/2018 |
| New employees FY21  `INPERIOD(Start date)` |  |  |  |  |

Another example of the *Employee Details* module does not have Time as a dimension. *Start date* has a date format, *Month period* has the time period format set to months, and *Is in period?* has a Boolean format.

The formula returns a TRUE result for employees with the correct *Start date* and *Month period*.

|  | **Employee A** | **Employee B** | **Employee C** | **Employee D** |
| --- | --- | --- | --- | --- |
| Start date | 12/03/2021 | 5/06/2020 | 15/03/2021 | 17/08/2018 |
| Month period | Mar 21 | May 20 | Mar 21 | Sept 18 |
| Is in period?  `INPERIOD(Start date, Month period)` |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Finperiod-3b64fe69-0d31-49b8-ab40-e7c1a3d01137&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>