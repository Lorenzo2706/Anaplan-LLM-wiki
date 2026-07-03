---
title: "VALUE | Anapedia"
source: "https://help.anaplan.com/value-a2cbfb0f-64c5-4a9c-b1f4-11eb41b54fa8"
author:
published:
created: 2026-05-02
description: "The VALUE function converts text representations of numbers into numeric values."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use VALUE in combination with other functions to remove currency symbols or codes from data and convert the values to numbers.

`VALUE(Value to convert)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Value to convert* | Text | The text value to convert into a number value. |

The VALUE function returns a numeric result.

In Polaris, you can't use the VALUE function with non-decimal representations of numbers (for example, “ `0x11.11p0` ”).

In the Classic Engine, you can use non-decimal representations of numbers.

`VALUE(Revenue as text)`

This example uses the The VALUE function to convert the *Revenue as text* line item to a number value.

The VALUE function works only with text values that represent numbers. The value to be converted can contain non-numeric characters if they are:

- Special numbers such as Infinity, -Infinity, or NaN.
- A hexadecimal number.
- Numbers that use scientific notation.
- Negative numbers that contain the - symbol.

If the *Value to convert* argument contains any other characters, such as a comma, %, $, or £, the VALUE function returns a value of NaN (not a number).

You can use the VALUE function to return a hexadecimal value as a number. For example, the formula `VALUE(“0x11.11p0")` returns a number value of 17.07.

The VALUE function also works with special numbers such as Infinity, -Infinity, or NaN.

[VALUE](https://support.microsoft.com/en-gb/office/value-function-257d0108-07dc-437d-ae1c-bc2d3953d8c2?ui=en-us&rs=en-gb&ad=gb)

This example has a list on columns that contains items with descriptive names for the values they contain. On rows, there are two line items:

- *Text value*, which contains the text values.
- *Converted number-formatted values*, which uses the VALUE function to convert the text values to number values.  
	This formula also highlights how the VALUE function interacts with numbers that contain non-numeric characters.

|  | **Positive** | **Negative** | **Dollar** | **Sterling** | **Comma separators** | **Scientific notation** | **Hexadecimal** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Text value | 134486.12 | \-134486.12 | $134486.12 | £134486.12 | 134,486.12 | 3E8 | 0x11.11p0 |
| Converted number-formatted values  `VALUE('Text value')` | 134,486 | \-134,486 | NaN | NaN | NaN | 300,000,000 | 17.07 |

Some functions, such as MID, return a text-formatted result. If these results are numeric, you can use the VALUE function to convert them to number-formatted.

For example, you can use the MID function to extract all characters after the first character. This enables you to remove currency symbols from numbers stored as text. The result can then be used with the VALUE function.

In this example the *Revenue as text* line item is text, and contains a value for several different currencies. The *Revenue as number* line item uses the MID and VALUE functions to convert the text that contains a number to numbers.

|  | **US Dollars** | **British Pound** | **Euro** | **Yen** |
| --- | --- | --- | --- | --- |
| Revenue as text | $2348765.38 | £1674500.96 | €1945632.29 | ¥257478438.94 |
| Revenue as number  `VALUE(MID(Revenue as text, 4, 3))` | 2,348,765 | 1,674,500 | 1,945,632 | 25,747,843 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fvalue-a2cbfb0f-64c5-4a9c-b1f4-11eb41b54fa8&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>