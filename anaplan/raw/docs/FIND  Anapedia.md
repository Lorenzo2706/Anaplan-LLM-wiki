---
title: "FIND | Anapedia"
source: "https://help.anaplan.com/find-b4571668-130a-4de8-a7b2-57439714f344"
author:
published:
created: 2026-05-02
description: "The FIND function searches for the first occurrence of a text value within another one. If the text contains the specified characters, the function returns a number. This number indicates the position of the first occurrence of the text value searched for."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The FIND function searches for the first occurrence of a text value within another one. If the text contains the specified characters, the function returns a number. This number indicates the position of the first occurrence of the text value searched for.

For example, you can use FIND to identify items that contain a specific product name.

`FIND(Text to find, Text to search [, Starting character])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text to find* (required) | Text | The text value to locate in the *Text to search* argument. |
| *Text to search* (required) | Text | The text value to search within for an instance of the *Text to find* argument. |
| *Starting position* | Number | The position to start the search from. Includes spaces.  Does not affect the numeric result the FIND function returns. |

The FIND function returns a numeric result.

In Polaris, the FIND function considers the length of all Unicode characters to be one. This means that the FIND function returns the correct starting character.

In the Classic Engine, the FIND function considers the length of:

- Unicode characters from within the Basic Multilingual Plane (BMP) to be 1
- Unicode characters from outside the BMP to be 2
- The length of composite characters (such as those with accents or diacritic marks) to be equal to the number of components

`FIND("Ltd.", Companies)`

If the FIND function does not find an instance for the Text to find argument, it returns a value of 0.

The FIND function is case-sensitive. This means that if the *Text to search* argument contains the *Text to find* argument with different capitalization, the FIND function returns a value of 0.

The FIND function considers spaces to be a character like letters or numbers.

The FIND function only looks for exact text matches. It is not possible to use search patterns such as [regular expressions](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference) or wildcards.

If you use emoji with the FIND function, the result of the function can be incorrect.

- [FIND](https://support.office.com/en-gb/article/FIND-FINDB-functions-c7912941-af2a-4bdf-a553-d0d89b0a0628)
- [SUBSTITUTE](https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332)

In this example, a module has a *Companies* list on columns. There are two line items on rows. The first contain several company names. The second contains a formula that uses the FIND function.

|  | **Company 1** | **Company 2** | **Company 3** | **Company 4** |
| --- | --- | --- | --- | --- |
| Company Name | Imperial ABC ltd | Imperial abc ltd | ABC ltd | Company ABC |
| Character that ABC starts at  `FIND("ABC", Company Name, 4)` | 10 | 0 | 0 | 9 |

In this example, the FIND function looks for the text string ABC, starting from the 4th character. It returns a result of 0 for the text string *Imperial abc ltd* because the string *abc* is not capitalized. It returns a result of 0 for the text string *ABC ltd* because *ABC* is within the first four characters.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ffind-b4571668-130a-4de8-a7b2-57439714f344&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>