---
title: "PROFILE | Anapedia"
source: "https://help.anaplan.com/profile-41b5fb84-395b-489f-80be-521add72c581"
author:
published:
created: 2026-05-02
description: "Use the PROFILE function to multiply values over any dimension, based on a series of numbers, or a profile."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use the PROFILE function to multiply values over any dimension, based on a series of numbers, or a profile.

For example, you can use the PROFILE function to calculate the value of an item based on estimated depreciation.

`PROFILE(Numbers to change, Profile [, List])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Numbers to change* | Number | The numbers to change. |
| *Profile* | Number | The values that changes to the *Numbers to change* argument are based on. The *Numbers to change* argument is multiplied by the values of this argument.  This must be a line item. |
| *List* (Polaris-only) | List | The list over which the function should operate.  See ***Calculation engine functionality differences****.* |

The PROFILE function returns a number.

- In Polaris, the lookup dimension of the *Profile* line item can't be related to any of the dimensions of the target line item to which the formula is applied. *See* **Additional information**.
- In Polaris, you can't use the PROFILE function for line items that have the **Formula** summary method. In the Classic Engine, you can.
- In Polaris, you can use the PROFILE function over any dimension, by including an additional argument. In the Classic Engine, you can't. Where, if the additional argument isn't included, the function defaults to Time as the dimension.

The lookup dimension is a dimension of the *Profile* line item. It's a unique dimension which is unrelated to any of the dimensions of the target line item in which the formula is applied to. For example, consider

*The Profile* line item that has three dimensions: *listA*, *listB*, and *listC*.  
The target line item has two dimensions: *listA* and *listB*.

Here, *listC* is the lookup dimension.

The *Profile* argument should contain a sequence of several values dimensioned by a list.

Each value in the *Numbers to change* line item is multiplied by each value in the *Profile* line item. The first value is multiplied by the first value in the *Profile* within the same target item. Then in the next target item, it is multiplied by the second value in the *Profile*, and so on.

The *Numbers to change* line item can contain multiple values. In this case, the PROFILE function applies the behavior described above to each value independently and sums the results.

As the values in the *Numbers to change* are multiplied by the values in the *Profile*, it can be useful to use the **Percentage** "Number" format for your profile.

The *Numbers to change* argument must have a valid line item reference from the *Numbers to change* argument to the resulting line item.

The time range used for the *Value to compare* argument must match the time range for the result line item.

This example uses two modules. The first module, *Profile*, contains a list with 5 list items that represent months, and a single line item, *Depreciation*. The module is below:

|  | **Depreciation** |
| --- | --- |
| This month | 100.0% |
| Next month | 75.0% |
| Month+2 | 55.0% |
| Month+3 | 30.0% |
| Month+4 | 15.0% |

The second module shows the PROFILE function used in another module with the *Depreciation* above.

|  | **Jan 22** | **Feb 22** | **Mar 22** | **Apr 22** | **May 22** | **Jun 22** | **Jul 22** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Single asset value** | 10,000 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Multiple asset values** | 10,000 | 0 | 0 | 10,000 | 0 | 0 | 10,000 |
| `PROFILE(Single asset value, Profile.Depreciation)` | 10,000 | 7,500 | 5,500 | 3,000 | 1,500 | 0 | 0 |
| `PROFILE(Multiple asset values, Profile.Depreciation)` | 10,000 | 7,500 | 5,500 | 13,000 | 9,000 | 5,500 | 13,000 |

As in the *Multiple asset values depreciation* line item, the PROFILE function can be used with multiple values. In this case, the function applies the profile to each value independently and then sums them.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fprofile-41b5fb84-395b-489f-80be-521add72c581&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>