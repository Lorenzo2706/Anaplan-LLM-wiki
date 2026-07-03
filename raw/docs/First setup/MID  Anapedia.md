---
title: "MID | Anapedia"
source: "https://help.anaplan.com/mid-5e5cc593-8bb2-4417-8daf-ed57b552e2cc"
author:
published:
created: 2026-05-02
description: "Extracts a number of characters from a text string, starting from a character you select."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, if a product SKU is prefixed with a code of fixed length, you can use the MID function to extract the characters after the code.

`MID(Text, Start position [, Number of characters])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Text* (required) | Text  Can be a line item, text constant, or general expression. | The text to extract characters from. |
| *Start position* (required) | Number  Can be a line item, property, or expression. | The numeric starting position in the text string. The extracted characters include the character in the start position you select.  If you use a *Start position* that is not present in the text string, or a negative number, the function returns a blank result. |
| *Number of characters* | Number  Can be a line item, property, or expression. | The number of characters to extract from the text string.  If you omit this argument, the MID function returns the character in the position specified in the *Start position* argument.  If you use a negative number or zero for this argument, the MID function returns a blank result.  If this argument is greater than the number of characters in the *Text* argument, the MID function returns only the characters in the string. |

The MID function returns a text-formatted result.

In Polaris, the MID function behaves as expected with all text values, including those that contain composite characters or characters from outside the Basic Multilingual Plane (BMP).

In the Classic Engine, the MID function considers the length of:

- Unicode characters from within the BMP to be 1
- Unicode characters from outside the BNP to be 2
- The length of composite characters (such as those with accents or diacritic marks) to be equal to the number of components

`MID(Product SKU, 4, 10)`

In this example, a line item named *Product SKU* contains a list of strings that identify different products. Each SKU starts with a three character string that describes the product category. After this, the product SKU contains a unique string of between five and 10 characters in length that identifies each product.

This formula uses the *Product SKU* line item for the *Text* argument, *4* for the *Start position* argument, and *10* for the *Number of characters* argument. As a result, The formula returns the unique string that starts from the fourth character of the product SKU. The formula returns up to 10 characters for each unique string, which includes all characters for those with less than 10.

The MID function cannot be used with list items. [Convert](https://help.anaplan.com/1a1ac604-62d2-4288-abaa-55fd8e2ee8e2) list items to text-formatted with the [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d) function if you need to use the MID function with them.

[MID](https://support.office.com/en-gb/article/MID-MIDB-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028)

In this example, the *Location code* line item contains an eight character code. Each part of the code is two characters long and separated by a hyphen. The first and second characters indicate the city, the fourth and fifth characters the region, and the seventh and eighth characters the country.

In order to extract the region code, this example uses 4 for the *Start position* argument, and 2 for the *Number of characters* argument. As a result, the formula extracts two characters starting from the fourth character, which is the region code. This can then be used in other parts of the model or exported.

|  | **Sapporo** | **Hakodate** | **Tokyo** | **Hachiōji** | **Kyoto** | **Uji** | **Naha** | **Okinawa** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Location code | 01-01-JP | 02-01-JP | 01-13-JP | 02-13-JP | 01-26-JP | 01-26-JP | 01-47-JP | 02-47-JP |
| `MID(Location code, 4, 2)` | 01 | 01 | 13 | 13 | 26 | 26 | 47 | 47 |

You can use the [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d) function to convert a list item to text so that you can use the MID function with it. You can also use [ITEM](https://help.anaplan.com/41298b7a-e877-40e8-8cfa-8d7009d8686f) function to return a list item that you can then use with the NAME function.

This example uses the same data as the previous example, but the *Location code* line item is list-formatted instead. As a result, it must be converted to text-formatted in order to use the MID function with it.

|  | **Sapporo** | **Hakodate** | **Tokyo** | **Hachiōji** | **Kyoto** | **Uji** | **Naha** | **Okinawa** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Location code | 01-01-JP | 02-01-JP | 01-13-JP | 02-13-JP | 01-26-JP | 01-26-JP | 01-47-JP | 02-47-JP |
| `MID(NAME(Location code), 4, 2)` | 01 | 01 | 13 | 13 | 26 | 26 | 47 | 47 |

You can use the MID function in combination with the [LENGTH](https://help.anaplan.com/49846ba7-7b09-4d11-b203-58ba512e7727) function to extract characters a set number of characters from the end of a string. This can be useful if the starting characters of a text string are variable but the ending characters are consistent.

To do this:

1. Provide a text-formatted line item, text constant, or general expression for the *Text* argument.
2. Use an expression enclosed in parentheses for the *Start position* argument.
	- Use LENGTH to determine the number of characters in each value of the *Text* argument.
		- Use a negative number to count back the number of characters from the end of the string to extract text from.
3. For the *Number of characters* argument, specify the number of characters you want to extract.

In this example, the *Product Code* line item contains a code. The code describes the wine type, an identifying number, and a region number. As the words used for wine type are of varying length, the identifying number is not a set number of characters from the start of the *Product Code* line item.

The bottom line item in this table contains a formula that demonstrates the above procedure. This means that it extracts a string a set number of characters from the end of the product code.

|  | **Sauvignon Blanc** | **Chianti** | **Riesling** | **Merlot** | **Pinot Noir** | **Zinfandel** |
| --- | --- | --- | --- | --- | --- | --- |
| Product Code | White-101-FR | White-102-BR | White-103-AU | Red-201-ES | Red-202-AR | Red-203-NZ |
| `MID(Product Code, (LENGTH(Product Code) -6), 3)` | 101 | 102 | 103 | 201 | 202 | 203 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmid-5e5cc593-8bb2-4417-8daf-ed57b552e2cc&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>