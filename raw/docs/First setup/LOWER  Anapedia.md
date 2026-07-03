---
title: "LOWER | Anapedia"
source: "https://help.anaplan.com/lower-610b25eb-611f-412e-ab2d-dc8083dc22d4"
author:
published:
created: 2026-05-02
description: "The LOWER function converts text values to lowercase."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

`LOWER(Text [, Locale])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text* (required) | Text | The text to make lowercase. |
| *Locale* | Keyword | The locale to use. Only has an effect with certain languages.  The available locales are based on ISO 639 and ISO 3166 codes. |

The LOWER function returns a text value.

In Polaris, you cannot use the *Locale* argument with the LOWER function.

In the Classic Engine, you can use the *Locale* argument.

`LOWER(Customer comments)`

The Locale argument accepts ISO language codes that correspond to the locales available in [Java 8](https://www.oracle.com/java/technologies/javase/jdk8-jre8-suported-locales.html). You can use either:

- Two letter ISO 639 language codes such as en, fr, de, or tr.
- Four letter codes made of both ISO 639 language codes and ISO 3166 country codes such as en-us, fr-be, de-at, or tr-tr. However you must replace the hyphen (-) with an underscore (\_) in Anaplan, so these become en\_us, fr\_be, de\_at, and tr\_tr respectively.

The *Locale* argument only has an effect on certain languages. For example, Turkish, which is represented by the tr code. In Turkish, there are four versions of the character *i*. Lowercase and uppercase versions, both with and without a dot.

[LOWER](https://support.office.com/en-gb/article/LOWER-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4)

This example has a *Territory* list on columns, and two line items on rows. The first line item contains the product categories sold in each region. The second line item contains a formula that uses LOWER to make the product categories lowercase, for use in another system.

|  | **New York** | **San Francisco** | **London** | **York** | **Tokyo** | **Osaka** |
| --- | --- | --- | --- | --- | --- | --- |
| Product categories | Accessories, Footwear, Innerwear, Outerwear, Sports Equipment | Accessories, Footwear, Sports equipment, | Accessories, Footwear, Innerwear, Outerwear, Sports Equipment | Outerwear, Sports Equipment | Accessories, Footwear, Innerwear, Outerwear, Sports Equipment | Accessories, Outerwear, Sports Equipment |
| Lowercase product categories  `LOWER(Product categories)` | accessories, footwear, innerwear, outerwear, sports equipment | accessories, footwear, sports equipment, | accessories, footwear, innerwear, outerwear, sports equipment | outerwear, sports equipment | accessories, footwear, innerwear, outerwear, sports equipment | accessories, outerwear, sports equipment |

In this example, a module contains a list of languages on columns. The are two line items on rows, one that contains international characters, and another that uses the LOWER function to make them lowercase.

|  | **Accented character** | **Cyrillic** | **Greek** | **Chinese** | **Japanese** | **Korean** |
| --- | --- | --- | --- | --- | --- | --- |
| Uppercase character | Å | Ж | Ψ | 中 | あ | ㅏ |
| Lowercase character  `LOWER(Uppercase character)` | å | ж | ψ | 中 | あ | ㅏ |

The LOWER function works with most languages without the *Locale* argument. However, it has no effect on certain languages, such as Chinese, Japanese, or Korean, as these languages do not have uppercase or lowercase characters.

If you use the LOWER function with a text string that contains an uppercase I and use the tr\_tr code for the *Locale* argument, the result contains a lowercase i without a dot, ı.

`LOWER("I", tr)`

The result of this formula is ı.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Flower-610b25eb-611f-412e-ab2d-dc8083dc22d4&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>