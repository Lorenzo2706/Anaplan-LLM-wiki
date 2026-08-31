---
title: "COMPARE | Anapedia"
source: "https://help.anaplan.com/compare-75708762-3891-4277-9265-9a46b1f0169d"
author:
published:
created: 2026-05-02
description: "The COMPARE function compares text values. If they're the same, it returns 0. If the first text value is greater, it returns 1, and if the first text value is less, it returns -1."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The COMPARE function compares text values. If they're the same, it returns 0. If the first text value is greater, it returns 1, and if the first text value is less, it returns -1.

You could use COMPARE as the basis of conditional formatting for identical text values.

`COMPARE(Text to compare 1, Text to compare 2 [, Comparison mode] [, Locale])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text to compare 1* (required) | Text | The first text value to compare. |
| *Text to compare 2* (required) | Text | The second text value to compare. |
| *Comparison mode* | Keyword | The comparison mode to use.  The available keywords are IDENTICAL, PRIMARY, SECONDARY, and TERTIARY.  There's more information in the Comparison mode argument keywords section below. |
| *Locale* | Keyword | The locale to use. This only affects certain languages.  The available locales are based on ISO 639 and ISO 3166 codes. |

The COMPARE function returns a number.

For more information about how to determine if

| **Keyword** | **Description** |
| --- | --- |
| IDENTICAL | Compares the *Text to compare 1* and *Text to compare 2* arguments to check if they're identical in all regards. |
| PRIMARY | Compares the base characters of the *Text to compare 1* and *Text to compare 2* arguments.  The alphabetical order of text values is compared from left to right, in line with the locale chosen.  If the starting characters of two text values are the same, but one contains more characters, the string with more characters is greater. |
| SECONDARY | Compares the base characters and accents of the Text to compare 1 and Text to compare 2 arguments.  If the base characters of two text values are the same, COMPARE considers the one that contains accents as greater. |
| TERTIARY | The default keyword if you omit the *Comparison mode* argument.  Compares the base characters, accents, and case of the *Text to compare 1* and *Text to compare 2* arguments.  If the base characters and accents of two text values are the same, but one contains uppercase characters, COMPARE considers the one that contains uppercase characters as greater. |

You cannot use the COMPARE function in Polaris.

In the Classic engine, you can.

`COMPARE(Top Salesperson North, Top Salesperson South)`

Whether a text value is considered greater than or less than another text value is based on several criteria, similar to [collation](https://en.wikipedia.org/wiki/Collation) in Unicode or Java.

The Comparison mode keywords compare the base characters, accents, and case of text values respectively. However, this behavior varies depending upon the locale chosen.

When you use the SECONDARY or TERTIARY keywords to compare the accents or case of text values, the COMPARE function also applies prior criteria. For example, if you use TERTIARY to compare the case of text values, it first compares the base characters and accents.

The Locale argument accepts ISO language codes that correspond to the locales available in [Java 8](https://www.oracle.com/java/technologies/javase/jdk8-jre8-suported-locales.html). You can use either:

- Two letter ISO 639 language codes such as en, fr, de, or tr.
- Four letter codes made of both ISO 639 language codes and ISO 3166 country codes such as en-us, fr-be, de-at, or tr-tr. However you must replace the hyphen (-) with an underscore (\_) in Anaplan, so these become en\_us, fr\_be, de\_at, and tr\_tr respectively.

The *Locale* argument only has an effect on certain languages. For example, Turkish, which is represented by the tr code. In Turkish, there are four versions of the character *i*. Lowercase and uppercase versions, both with and without a dot.

The *Locale* argument of the COMPARE function may alter the fundamental properties of a character, such as its position in the roman alphabet. Here are some examples of how the *Locale* argument can affect the COMPARE function:

- With the English en language code, the Danish character ø is treated as if it's the base character of o. With the Danish da language code, the base character of ø is not considered to be an accented character, and it comes after z in alphabetical order.
- In Swedish, represented by the sv language code, the characters v and w are considered to be the same.
- In Lithuanian, represented by the lt language code, the character y precedes j in alphabetical order.

[EXACT](https://support.office.com/en-gb/article/EXACT-function-d3087698-fc15-4a15-9631-12575cf29926)

In this example, Time displays on columns. On rows, there are three line items. The first two line items show the top sales performer for All Regions and North. The third line item contains a formula that uses COMPARE to see if the top sales performer in the North region is the same as in all regions.

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Top Sales All Regions | Peter | Rashid | Jenny |
| Top Sales North | Peter | Peter | John |
| Top Sales in North?  `COMPARE(Top Sales All Regions, Top Sales North)` | 0 | 1 | \-1 |

The formula uses the default behavior for the *Locale* argument, which is the ‘en’ ISO 369 language code.

In *Jan 21*, *Peter* was the text value for both All Regions and North. As they're identical, COMPARE returns a value of 0.

In *Feb 21*, *Rashid* was the text value for All Regions, and *Peter* the text value for North. As the first letter of both *Rashid* and *Peter* is different, the COMPARE function compares these characters. R comes after P in alphabetical order, so the text value Rashid is considered greater and the formula returns a value of 1.

In *Mar 21*, *Jenny* was the text value for all regions, and *John* the text value for North. The first letter of both Jenny and John, J, is the same, so it's ignored in the comparison. This means the second letter of each text value is compared. As e comes before o in alphabetical order, the formula considers the text value John greater, and returns a value of -1.

If you use the PRIMARY keyword for the *Comparison mode* argument, the COMPARE function compares the two text values for any differences in base characters.

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Chosen Employee 1 | Tim | Tim | Tim |
| Chosen Employee 2 | Tim | Tom | Tam |
| `COMPARE(Chosen Employee 1, Chosen Employee 2, PRIMARY)` | 0 | \-1 | 1 |

If you use the SECONDARY keyword for the *Comparison mode* argument, the COMPARE function:

1. Compares the two text values for any differences in base characters.
2. If there's no difference in base characters, compares the accents in the two text values.

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Chosen Employee 1 | Soren | Soren | Søren |
| Chosen Employee 2 | Soren | Søren | Soren |
| `COMPARE(Chosen Employee 1, Chosen Employee 2, SECONDARY)` | 0 | \-1 | 1 |

If you use the TERTIARY keyword for the *Comparison mode* argument, the COMPARE function:

1. Compares the two text values for any differences in base characters.
2. If there's no difference in base characters, compares the accents in the two text values.
3. If there's no difference in base characters or accents, compares the case of the two text values.

|  | **Jan 21** | **Feb 21** | **Mar 21** |
| --- | --- | --- | --- |
| Chosen Employee 1 | Frank | frank | Frank |
| Chosen Employee 2 | Frank | Frank | frank |
| `COMPARE(Chosen Employee 1, Chosen Employee 2, TERTIARY)` | 0 | \-1 | 1 |

This example shows how the result the COMPARE returns changes based on the *Comparison mode* argument.

|  | **Primary difference** | **Secondary difference** | **Tertiary difference** |
| --- | --- | --- | --- |
| Text 1 | b | á | Á |
| Text 2 | a | a | á |
| `COMPARE('Text 1', 'Text 2', PRIMARY)` | 1 | 0 | 0 |
| `COMPARE('Text 1', 'Text 2', SECONDARY)` | 1 | 1 | 0 |
| `COMPARE('Text 1', 'Text 2', TERTIARY)` | 1 | 1 | 1 |

When used for the *Locale* argument, some codes change how the COMPARE function treats characters. For example, if you use the Swedish language code, sv, the letters w and v are considered to be the same base character.

|  | **Region** |
| --- | --- |
| English | Sweden |
| Swedish | Sveden |
| `COMPARE(English, Swedish, PRIMARY)` | 1 |
| `COMPARE(English, Swedish, PRIMARY, sv)` | 0 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcompare-75708762-3891-4277-9265-9a46b1f0169d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>