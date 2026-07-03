---
title: "TRIM | Anapedia"
source: "https://help.anaplan.com/trim-351955a5-838c-4f3b-9073-96732fc259a9"
author:
published:
created: 2026-05-02
description: "The TRIM function removes all leading and trailing spaces, and extra spaces between words in a text string."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The TRIM function removes all leading and trailing spaces, and extra spaces between words in a text string.

For example, if text imported from an external system includes irregular spaces, you can use the TRIM function to remove the spaces.

`TRIM(Text)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text* | Text | The text to trim extra spaces from. |

The TRIM function returns a text value.

You cannot currently use the TRIM function in Polaris.

In the Classic Engine, you can.

`TRIM(" Account  Summary ")`

[TRIM](https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9?ui=en-us&rs=en-us&ad=us)

In this example, the *Office locations* line item contains the *Las Vegas*, *London*, and *Melbourne* values. The formula removes all irregular spaces from each value, and replaces extra spaces between words with single space characters.

|  | **America** | **Europe** | **Australia** |
| --- | --- | --- | --- |
| Office locations | Las   Vegas | London | Melbourne |
| `TRIM(Office locations)` | Las Vegas | London | Melbourne |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftrim-351955a5-838c-4f3b-9073-96732fc259a9&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>