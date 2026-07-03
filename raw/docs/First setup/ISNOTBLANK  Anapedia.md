---
title: "ISNOTBLANK | Anapedia"
source: "https://help.anaplan.com/isnotblank-1463efe5-aff5-43fa-abf7-39b7d95a6692"
author:
published:
created: 2026-05-02
description: "The ISNOTBLANK function returns a Boolean result for values that are not blank."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the ISNOTBLANK function to find employees without a leaving date.

`ISNOTBLANK(Value to test)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Value to test | Date, time period, text, or list | The value to test if it is blank. |

The ISNOTBLANK function returns a Boolean result.

In Polaris, the ISNOTBLANK function considers a text value that consists exclusively of carriage return characters to be a blank value.

In the Classic Engine, the ISNOTBLANK function considers a carriage return to be a non-blank value.

`ISNOTBLANK(Panel interview)`

In this example, *Panel interview* is a line item with a text format. The formula returns true if a value from the line item contains text, which means a candidate has completed that stage of the interview process.

`ISNOTBLANK(Rehire date)`

In this example, *Rehire date* is a line item with a date format. The formula returns true for values that contain dates for rehired employees.

|  | **Hannah Smith** | **Eric Jones** | **Paul Turner** |
| --- | --- | --- | --- |
| Rehire date | 5/06/2021 |  | 8/03/2021 |
| `ISNOTBLANK(Rehire date)` |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fisnotblank-1463efe5-aff5-43fa-abf7-39b7d95a6692&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>