---
title: "START | Anapedia"
source: "https://help.anaplan.com/start-bc44fa0b-7af8-4a8f-ad8f-cbeaccf22003"
author:
published:
created: 2026-05-02
description: "The START function returns the first date of a time period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

`START(Time period)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Time period* | Time period | The time period to find the first date of.  If left blank, returns the first date from the source module.  If a line item with the time period data type is used, returns the first date from that time period. A blank time period returns a blank result.  If a direct reference to a time period is used (Time.'Period'), returns the first date from that time period. |

The START function returns a date result.

The format used to display the date depends on your OS/browser settings. For example, the U.S. date format displays the month before the day (mm/dd/yyyy).

The example below shows `START()`. No parameter is used and the module is time period formatted for months.

|  | **Jan 14** | **Feb 15** |
| --- | --- | --- |
| Period Start Date  `START()` | 01/01/2014 | 01/02/2014 |

The example below shows START with a parameter. *Start Month* is formatted for months and *Start Quarter* is formatted for quarters.

|  | **Key Dates** | **Expiry Dates** |
| --- | --- | --- |
| Month Period | Feb 14 | Apr 16 |
| Quarter Period | Q2 FY14 | Q3 FY16 |
| Start Month  `START(Month Period)` | 01/02/2014 | 01/04/2016 |
| Start Quarter  `START(Quarter Period)` | 01/04/2014 | 01/07/2016 |

The final example below shows START with a hard-coded parameter. The current year is set to *FY16* and the model **Time Scale** includes the past 2 years.

|  | **Key Dates** | **Expiry Dates** |
| --- | --- | --- |
| Month Period | Feb 14 | Apr 15 |
| Quarter Period | Q2 FY14 | Q3 FY14 |
| Start Date Absolute  `START(TIME.'FY14')` | 01/01/2014 | 01/01/2014 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fstart-bc44fa0b-7af8-4a8f-ad8f-cbeaccf22003&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>