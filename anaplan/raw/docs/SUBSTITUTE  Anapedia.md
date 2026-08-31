---
title: "SUBSTITUTE | Anapedia"
source: "https://help.anaplan.com/substitute-841babeb-4694-4761-91c1-18d920edb879"
author:
published:
created: 2026-05-02
description: "The SUBSTITUTE function finds all occurrences of a text value within another one, and replaces them with a given value."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The SUBSTITUTE function finds all occurrences of a text value within another one, and replaces them with a given value.

For example, you can use the SUBSTITUTE function to change the content of a text string based on its dimensionality, such as region.

`SUBSTITUTE(Text to search in, Text to find, Replacement text)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text to search* | Text | The text to search for instances of the *Text to replace* argument. |
| *Text to replace* | Text | The text value to substitute with *Replacement text* within *Text to search in*. Each instance of the text value is replaced. |
| *Replacement text* | Text | The text value to replace the *Text to replace* argument with. |

The SUBSTITUTE argument returns a text value.

In Polaris, the SUBSTITUTE function does not match the base characters of a composite characters. For example, the SUBSTITUTE function does not consider â to contain a or が to contain か.

In the Classic Engine, the SUBTITUTE function matches the base characters of composite characters. For example, the SUBSTITUTE function considers â to contain a or が to contain か.

`SUBSTITUTE( Email content, "[Region placeholder]", Region name)`

The SUBSTITUTE function only looks for exact text matches. It is not possible to use search patterns such as [regular expressions](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference) or wildcards.

If the *Text to search in* value contains multiple instances of the *Text to replace* value, the SUBSTITUTE function replaces each of them. The replacement is in the order that the *Text to replace* values display, from left to right. However, it is not recursive. This means that if the *Replacement text* argument contains the text value from the *Text to replace* argument, the result is not substituted also.

If the *Text to search in* value does not contain the *Text to replace* value, the SUBSTITUTE function returns the *Text to replace* value unchanged. This means that if a blank value is used for the *Text to replace* argument, the SUBSTITUTE function has no effect.

The SUBSTITUTE function is case sensitive. It also works with emoji and other characters that are not part of the Unicode [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_\(Unicode\)#Basic_Multilingual_Plane).

The SUBSTITUTE function does not consider [canonically equivalent characters](https://en.wikipedia.org/wiki/Unicode_equivalence#:~:text=For%20example%2C%20the%20code%20point,%22%20of%20the%20Spanish%20alphabet) to be the same character. For example, U+00E2 (Latin Small Letter A with Circumflex), which renders as â. This is not equivalent to the combination of U+0061 (Latin Small Letter A) and U+0302 (Combining Circumflex Accent), which also renders as â.

[SUBSTITUTE](https://support.office.com/en-ie/article/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332)

You can enclose text in double quotation marks to enter literal text values directly into the SUBSTITUTE function. In this example, each argument is enclosed in double quotation marks. The following formula:

`SUBSTITUTE("ababababa", "aba", "c")`

searches the text *ababababa* for any instances of *aba* and replaces them with *c*. This means it returns a text value of *cbcba*.

This example uses data from three modules.

The first module, *Email Templates*, contains only text line items. Each of these line items contain the phrases *\[Region Placeholder\]* and *\[Revenue Placeholder\],* which are the text to be substituted using the SUBSTITUTE function.

| Financial performance | Financial performance in \[Region Placeholder\] changed by \[Revenue Placeholder\]. |
| --- | --- |
| Revenue against target | Revenue in \[Region Placeholder\] was \[Revenue Placeholder\]. The target for this period was \[Target Revenue Placeholder\]. |

The second module, *Profit and loss summary*, contains the *Cities* list on columns. On rows, there are line items that contain a variety of financial results.

|  | **Tokyo** | **Munich** | **Tel Aviv** | **Abu Dhabi** |
| --- | --- | --- | --- | --- |
| Revenue | $213,458 | $648,751 | $366,951 | $104,853 |
| Operating costs | $153,948 | $486,795 | $295,657 | $54,843 |
| Operating profit  `Revenue - Operating costs` | $59,510 | 161,956 | $71,294 | $50,010 |

The third module, *Revenue Email*, has the *Cities* list on columns, and line items on rows. The line items contain two formulas that use data from the *Email templates* and *Profit and loss* modules to create text that changes based on the data within the modules.

|  | **Tokyo** | **Munich** | **Tel Aviv** | **Abu Dhabi** |
| --- | --- | --- | --- | --- |
| Financial performance template with region  `SUBSTITUTE(Email Templates.'Financial performance', "[Region Placeholder]", NAME(ITEM(Region)))` | Financial performance in Tokyo changed by \[Revenue Placeholder\]. | Financial performance in Munich changed by \[Revenue Placeholder\]. | Financial performance in Tel Aviv changed by \[Revenue Placeholder\]. | Financial performance in Abu Dhabi changed by \[Revenue Placeholder\]. |
| Financial performance template with region and revenue  `SUBSTITUTE(Financial performance template with region, "[Revenue Placeholder]",  TEXT(Profit and loss summary.'Revenue') & " USD")` | Financial performance in Tokyo changed by 213458 USD. | Financial performance in Munich changed by 648751 USD. | Financial performance in Tel Aviv changed by 366951 USD. | Financial performance in Abu Dhabi changed by 104853 USD. |

The second formula uses the result of the first formula for the *Text to search* argument. This is because each usage of the SUBSTITUTE function can search only for a single text value. In order to replace two different strings, you need to use the SUBSTITUTE function twice.

You can use SUBSTITUTE to replace underscores, or other characters, in text with spaces. To do so, you must use a space enclosed in double quotation marks for the *Replacement text* argument. A line item cannot contain only a space, so this is the only method you can use.

`SUBSTITUTE("Text_with_underscores", "_", " ")`

The result of this formula would be *Text with underscores*, with the underscores replaced with spaces.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fsubstitute-841babeb-4694-4761-91c1-18d920edb879&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>