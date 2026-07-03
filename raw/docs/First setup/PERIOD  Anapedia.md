---
title: "PERIOD | Anapedia"
source: "https://help.anaplan.com/period-110a2a13-de1b-4274-82ee-c4ecd5e2dc90"
author:
published:
created: 2026-05-02
description: "The PERIOD function converts a date to a time period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the PERIOD function to show which financial quarter a date falls under.

`PERIOD(Date)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Date* | Date | The date to convert the time period from. |

The PERIOD function returns a time period.

In Polaris, you can only use PERIOD in a line item that has a **Type** of **Time Period**. The result has the same timescale as the line item type.

- Source must be date formatted.
- Result must be time period formatted.
- Result must fall within the time bounds of the model.

In the example, the formula returns the month and quarter for the date *12/02/2015*.

*Period Month* has the time period set to month, and *Period Quarter* has the time period set to quarter.

|  | **Key Date** |
| --- | --- |
| Date | 12/02/2015 |
| Period Month  `PERIOD(Date)` | Feb 2015 |
| Period Quarter  `PERIOD(Date)` | Q1 FY15 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fperiod-110a2a13-de1b-4274-82ee-c4ecd5e2dc90&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>