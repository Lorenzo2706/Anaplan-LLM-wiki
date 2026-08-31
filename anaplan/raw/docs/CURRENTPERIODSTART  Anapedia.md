---
title: "CURRENTPERIODSTART | Anapedia"
source: "https://help.anaplan.com/currentperiodstart-a7af7113-e1dc-478d-bbbe-ecb597092991"
author:
published:
created: 2026-05-02
description: "The CURRENTPERIODSTART function returns the start date from a model's current period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the CURRENTPERIODSTART function to ensure that a formula only applies to the current period in a financial year.

`CURRENTPERIODSTART()`

The CURRENTPERIODSTART function does not use any arguments.

This function returns a date result.

`CURRENTPERIODSTART()`

In this example, the formula returns the start date from the current period.

- `CURRENTPERIODSTART()` function will return a blank value if no **Current Period** is specified in the **Model Calendar**.
- When the **Current Period** is changed, any cells with the `CURRENTPERIODSTART()` formula will also be updated to reflect the new value.

In this example, the formula returns TRUE for the date that is set as the model's **Current Period**.

|  | **Jan 20** | **Feb 20** |
| --- | --- | --- |
| First day of month | 01/01/2021 | 01/02/2021 |
| Current period?  `CURRENTPERIODSTART() = START()` |  |  |

In this example, a *Product Sales* module has Time on columns, and line items on rows. The *Current week?* line item has a Boolean data type. The model calendar is set to [**Weeks: General**](https://help.anaplan.com/ba7ab203-412d-48b5-ba4a-bf9695448cff).

The formula returns TRUE for the week that is set as the model's **Current Period**.

|  | **31 Aug 21** | **7 Sep 21** | **14 Sep 21** | **21 Sep 21** |
| --- | --- | --- | --- | --- |
| Chocolate | 1,450 | 1,344 | 1,100 | 806 |
| Fudge | 754 | 887 | 1,003 | 1,012 |
| Current period?  `CURRENTPERIODSTART() = START()` |  |  |  |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcurrentperiodstart-a7af7113-e1dc-478d-bbbe-ecb597092991&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>