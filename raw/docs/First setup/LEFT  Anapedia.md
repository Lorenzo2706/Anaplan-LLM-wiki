---
title: "LEFT | Anapedia"
source: "https://help.anaplan.com/left-9c2a45d9-5af8-433a-b45c-46b0d6ae8462"
author:
published:
created: 2026-05-02
description: "Extracts a string of characters from text, starting from the left."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, if a product SKU is prefixed with a code of fixed length, you can use the LEFT function to extract this from the rest of the text.

`LEFT(Text [, Number of characters]) `

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text* | Text  Can be a line item, text constant, or general expression. | The text to extract characters from. |
| *Number of characters* (optional) | Number  Can be a line item, property, or expression. | The number of characters to extract from the string.  If you omit this argument, the LEFT function returns only the first, left, character from the text string.  If you use a negative number or zero for this argument, the LEFT function returns a blank result.  If this argument is greater than the number of characters in the *Text* argument, the LEFT function returns only the characters in the string. |

The LEFT function returns a text-formatted result.

In Polaris, the LEFT function behaves as expected with all text values, including those that contain composite characters or characters from outside the Basic Multilingual Plane (BMP).

In the Classic Engine, the LEFT function considers the length of:

- Unicode characters from within the BMP to be 1
- Unicode characters from outside the BMP to be 2
- The length of composite characters (such as those with accents or diacritic marks) to be equal to the number of components

`LEFT(Product SKU, 3)`

In this example, a line item named *Product SKU* contains a list of strings that identify different products. Each SKU starts with a three character string that describes the product category.

This formula uses the *Product SKU* line item for the *Text* argument and 3 for the *Number of characters* argument. As a result, the formula returns the first three characters for each product SKU as a text-formatted result.

The LEFT function cannot be used with list items. [Convert](https://help.anaplan.com/1a1ac604-62d2-4288-abaa-55fd8e2ee8e2) list items to text-formatted with the [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d) function if you need to use the LEFT function with them.

[LEFT](https://support.office.com/en-gb/article/LEFT-LEFTB-functions-9203d2d2-7960-479b-84c6-1ea52b99640c)

In this example, a *Clothing* list displays on columns. It contains four items, *Hats*, *Shirts*, *Shorts*, and *Trousers*.

Three text-formatted line items display on rows, *Red Product*, *Blue Product*, and *Yellow Product*. These contain product names. There is also one list-formatted line item, *Clothing List*, which contains product types. These line items contain the values used for the *Text* argument.

The bottom four rows contain formulas that use the LEFT function to extract characters from the left of the text strings.

|  | **Hats** | **Shirts** | **Shorts** | **Trousers** |
| --- | --- | --- | --- | --- |
| Red Product | Red Hats | Red Shirts | Red Shorts | Red Trousers |
| Blue Product | Blue Hats | Blue Shirts | Blue Shorts | Blue Trousers |
| Yellow Product | Yellow Hats | Yellow Shirts | Yellow Shorts | Yellow Trousers |
| Clothing List | Hats | Shirts | Shorts | Trousers |
| `LEFT(Red Product, 3)` | Red | Red | Red | Red |
| `LEFT(Blue Product, 7)` | Blue Ha | Blue Sh | Blue Sh | Blue Tr |
| `LEFT(Yellow Product, 10)` | Yellow Hat | Yellow Shi | Yellow Sho | Yellow Tro |
| `LEFT(NAME(Clothing List), 3)` | Hat | Shi | Sho | Tro |

You can use the [ITEM](https://help.anaplan.com/Calculation_Functions/All/ITEM.html) function to return the list-formatted column names. Then, you can use the [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d) function to convert the names to be text-formatted, which is compatible with the LEFT function.

In this example, the *Fruit* list displays on columns, and two line items display on rows. Both line items contain formulas.

|  | **Apples** | **Peaches** | **Bananas** | **Pears** | **Carrots** | **Cucumbers** | **Lettuce** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ITEM(Products)` | Apples | Peaches | Bananas | Pears | Carrots | Cucumbers | Lettuce |
| `LEFT(NAME(ITEM(Products)), 5)` | Apple | Peach | Banan | Pears | Carro | Cucum | Lettu |

In this example, *5* is used for the the *Number of characters* argument, so the formula returns the first five letters of the list-formatted *Products* strings.

`LEFT("Favorite Team", 8) `

This example uses the LEFT function with a text string typed directly into the formula. It uses *8* for the *Number of characters* argument. This means it returns *Favorite*, the first eight characters of the text string.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fleft-9c2a45d9-5af8-433a-b45c-46b0d6ae8462&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>