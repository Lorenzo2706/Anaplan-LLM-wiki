---
title: "FIRSTNONZERO | Anapedia"
source: "https://help.anaplan.com/firstnonzero-1c44ab3b-8499-41a1-bf7b-3f0bcfc8f150"
author:
published:
created: 2026-05-02
description: "The FIRSTNONZERO function searches through two or more numeric arguments and returns the first value that is not zero."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The FIRSTNONZERO function searches through two or more numeric arguments and returns the first value that is not zero.

For example, you can use the FIRSTNONZERO function to avoid complex conditional formulas you would otherwise have to use to determine the first non-zero value in a collection of numbers.

The two formulas below are equivalent:

- `FIRSTNONZERO(a, b, c)`
- `IF a <> 0 THEN a ELSE IF b <> 0 THEN b ELSE IF c <> 0 THEN c ELSE 0`

`FIRSTNONZERO(Value 1, Value 2, [etc.])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| Value | Number | The FIRSTNONZERO function assesses each instance of this argument and returns the first value that is not zero.  This argument can be given multiple times. You must provide a minimum of two values for the FIRSTNONZERO function to compare.  The FIRSTNONZERO function assesses values in the order they're provided as arguments. |

The FIRSTNONZERO function returns a numeric result.

In the example below, five line items that contain numeric values display on rows, named *a* through *e*. The Time dimension displays on columns.

Two line items contain formulas that demonstrate the FIRSTNONZERO function.

The *Alphabetical order* line item searches each line item for a non-zero value in alphabetical order, as the arguments are provided to the FIRSTNONZERO function in that order. The opposite is true for the formula in the *Reverse alphabetical order* line item.

|  | **Jan 22** | **Feb 22** | **Mar 22** |
| --- | --- | --- | --- |
| a | 5 | 0 | 0 |
| b | 3 | 0 | 0 |
| c | 12 | 2 | 7 |
| d | 4 | 2 | 0 |
| e | 56 | 2 | 4 |
| Alphabetical order  `FIRSTNONZERO(a, b, c, d, e)` | 5 | 2 | 7 |
| Reverse alphabetical order  `FIRSTNONZERO(e, d, c, b, a)` | 56 | 2 | 4 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ffirstnonzero-1c44ab3b-8499-41a1-bf7b-3f0bcfc8f150&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>