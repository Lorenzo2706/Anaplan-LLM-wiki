---
title: "LENGTH | Anapedia"
source: "https://help.anaplan.com/length-49846ba7-7b09-4d11-b203-58ba512e7727"
author:
published:
created: 2026-05-02
description: "The LENGTH() function, also known as LEN(), returns the number of characters in a text string."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The `LENGTH()` function, also known as `LEN()`, returns the number of characters in a text string.

For example, you can use `LENGTH()` to determine if a string is within the character limit for another system.

`LENGTH(Text to evaluate)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text to evaluate* | Text | The text to evaluate the number of characters within. The `LENGTH()` function returns the number of characters as a number. |

The `LENGTH()` function returns a number.

In Polaris, the `LENGTH()` function behaves as expected with all text values, including those that contain composite characters or characters from outside the Basic Multilingual Plane (BMP).

In the Classic Engine, the `LENGTH()` function considers the length of:

- Unicode characters from within the BMP to be 1
- Unicode characters from outside the BNP to be 2
- The length of composite characters (such as those with accents or diacritic marks) to be equal to the number of components

`LENGTH(Customer comments)`

In this example, the `LENGTH()` function returns the number of characters for each value of the text-formatted *Customer comments* line item.

- When the *Text to evaluate* argument contains whitespace characters, each of these is counted as a single character by the `LENGTH()` function.
- If a value for the *Text to evaluate* argument has no characters, the `LENGTH()` function returns a value of zero.

**Note:** `LENGTH()` can also be written as `LEN()`. They're the same function with different names.

For some unicode symbols outside the Basic Multilingual Plane, the `LENGTH()` function returns 2 for a single character. For example, text values that are encoded as a combination of two characters (a base character and an accent), or emoji.

[LEN](https://support.office.com/en-gb/article/LEN-LENB-functions-29236f94-cedc-429d-affd-b5e33d2c67cb)

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Profit Commentary | The profit in January was slightly below target, possibly due to the supply chain issue. | The profit in February was on target. | The profit in March surpassed the target due to the new campaign. |
| Commentary Length  `LENGTH(Profit Commentary)` | 88 | 37 | 65 |
| Within character limit for reports?  `Commentary Length < 70` |  |  |  |

In this example, a module contains information about the profit for each month. Time displays on columns, and line items on rows.

- The text-formatted *Profit Commentary* line item contains manually entered text about each month's profit.
- The number-formatted *Commentary Length* line item uses the `LENGTH()` function to return the number of characters in *Profit Commentary* as a number.
- The Boolean line item *Within character limit for reports?* uses the result of *Commentary Length* and calculates if it's under 70.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Flength-49846ba7-7b09-4d11-b203-58ba512e7727&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>