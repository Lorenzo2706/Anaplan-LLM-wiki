---
title: "RIGHT | Anapedia"
source: "https://help.anaplan.com/right-f076e4fd-3f63-4b7b-9ed2-3769a0dfd0e7"
author:
published:
created: 2026-05-02
description: "Extracts a string of characters from text, starting from the right."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, if an automatically generated string ends with numbers that represent a date, you can use the RIGHT function to extract the date.

`RIGHT(Text [, Number of characters])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text* | Text  Can be a line item, text constant, or general expression. | The text to extract characters from. |
| *Number of characters* (optional) | Number  Can be a line item, property, or expression. | The number of characters to extract from the text string.  If you omit this argument, the RIGHT function returns only the last, right, character from the text string.  If you use a negative number or zero for this argument, the RIGHT function returns a blank result.  If this argument is greater than the number of characters in the *Text* argument, the RIGHT function returns only the characters in the string. |

The RIGHT function returns a text-formatted result.

In Polaris, the RIGHT function behaves as expected with all text values, including those that contain composite characters or characters from outside the Basic Multilingual Plane (BMP).

In the Classic Engine, the RIGHT function considers the length of:

- Unicode characters from within the BMP to be 1
- Unicode characters from outside the BMP to be 2
- The length of composite characters (such as those with accents or diacritic marks) to be equal to the number of components

`RIGHT(Feedback ID, 10)`

In this example, each piece of feedback Anaplan receives from another system has a unique code that identifies it. This ends with a 10 character string that corresponds to the date in the format dd-mm-yyyy.

This formula uses the *Feedback ID* line item for the *Text* argument and *10* for the *Number of characters* argument. As a result, this formula extracts the 10 characters that represent the date from the end of each feedback ID. This can then be used in other parts of the model or exported.

The RIGHT function cannot be used with list items. [Convert](https://help.anaplan.com/1a1ac604-62d2-4288-abaa-55fd8e2ee8e2) list items to text-formatted with the [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d) function if you need to use the RIGHT function with them.

[RIGHT](https://support.office.com/en-gb/article/RIGHT-RIGHTB-functions-240267ee-9afa-4639-a02b-f19e1786cf2f)

In this example, a *Clothing* list displays on columns, with four items, *Hats*, *Shirts*, *Shorts*, and *Trousers*.

Three text-formatted line items display on rows, *Red Product*, *Blue Product*, and *Yellow Product*. These contain product names. There's also one list-formatted line item, *Clothing List*, which contains product types. These line items contain the values used for the *Text* argument.

The bottom four rows contain formulas that use the RIGHT function to extract characters from the right of the text strings.

|  | **Hats** | **Shirts** | **Shorts** | **Trousers** |
| --- | --- | --- | --- | --- |
| Red Product | Red Hats | Red Shirts | Red Shorts | Red Trousers |
| Blue Product | Blue Hats | Blue Shirts | Blue Shorts | Blue Trousers |
| Yellow Product | Yellow Hats | Yellow Shirts | Yellow Shorts | Yellow Trousers |
| Clothing List | Hats | Shirts | Shorts | Trousers |
| `RIGHT(Red Product, 4)` | Hats | irts | orts | sers |
| `RIGHT(Blue Product, 6)` | e Hats | Shirts | Shorts | ousers |
| `RIGHT(Yellow Product, 8)` | low Hats | w Shirts | w Shorts | Trousers |
| `RIGHT(NAME(Clothing List), 3)` | ats | rts | rts | ers |

You can use the [ITEM](https://help.anaplan.com/Calculation_Functions/All/ITEM.html) function to return the list-formatted column names. Then, you can use the [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d) function to convert the names to be text-formatted, which is compatible with the RIGHT function.

In this example, the *Fruit* list displays on columns, and two line items display on rows. Both line items contain formulas.

|  | **Apples** | **Peaches** | **Bananas** | **Pears** | **Carrots** | **Cucumbers** | **Lettuce** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ITEM(Products)` | Apples | Peaches | Bananas | Pears | Carrots | Cucumbers | Lettuce |
| `RIGHT(NAME(ITEM(Products)), 5)` | pples | aches | nanas | Pears | rrots | mbers | ttuce |

`RIGHT("Favorite Team", 4) `

This example uses the RIGHT function with a text string typed directly into the formula. It uses *4* for the *Number of characters* argument. This means it returns *Team*, the last four characters of the text string.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fright-f076e4fd-3f63-4b7b-9ed2-3769a0dfd0e7&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>