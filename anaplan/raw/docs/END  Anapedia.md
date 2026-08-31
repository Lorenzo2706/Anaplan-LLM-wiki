---
title: "END | Anapedia"
source: "https://help.anaplan.com/end-3d41a077-b391-45ca-a6e2-0c6dfaaeb85f"
author:
published:
created: 2026-05-02
description: "The END function returns the last date of a time period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

This function is useful if you want to calculate maturity dates or due dates that fall on the last day of the month.

`END([Time period]) `

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Time period (optional) | Time period | The time period used to find the end date from.  If you do not include an argument, END returns the last date of each period within the source module's time dimension. |

The END function returns a date value.

The format used to display the date depends on your OS/browser settings. For example, the U.S. date format displays the month before the day (mm/dd/yyyy).

Note: If the time period is blank, the result is blank.

- [EOMONTH](https://support.office.com/en-gb/article/EOMONTH-function-7314ffa1-2bc9-4005-9d66-f49db127d628)

The example below shows `END( )`. No argument is used and the module is time period formatted for months.

|  | **Jan 14** | **Feb 15** |
| --- | --- | --- |
| Period End Date  `END( )` | 31/01/2014 | 28/02/2014 |

The example below shows END with the *Time period* argument. *End Month* is formatted for months and *End Quarter* is formatted for quarters.

|  | **Key Dates** | **Expiry Dates** |
| --- | --- | --- |
| Month Period | Feb 14 | Apr 16 |
| Quarter Period | Q2 FY14 | Q3 FY16 |
| End Month  `END(Month Period)` | 28/02/2014 | 30/04/2016 |
| End Quarter  `END(Quarter Period)` | 30/06/2014 | 30/09/2016 |

The final example below shows END with a hard-coded argument.

|  | **Key Dates** | **Expiry Dates** |
| --- | --- | --- |
| Month Period | Feb 14 | Apr 15 |
| Quarter Period | Q2 FY14 | Q3 FY14 |
| End Date Absolute  `END(TIME.'FY14')` | 31/12/2014 | 31/12/2014 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fend-3d41a077-b391-45ca-a6e2-0c6dfaaeb85f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>