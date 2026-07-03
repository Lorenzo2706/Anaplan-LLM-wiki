---
title: "ITEMLEVEL | Anapedia"
source: "https://help.anaplan.com/itemlevel-756d1428-5f1d-4d79-8274-d075a1bd312f"
author:
published:
created: 2026-05-02
description: "Use ITEMLEVEL to find a given item's position within its list. The list is identified based on the given item's data type. You can use this function to find the distance from the item to either its root ancestor or its furthest leaf descendant."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use `ITEMLEVEL` to find a given item's position within its list. The list is identified based on the given item's data type. You can use this function to find the distance from the item to either its root ancestor or its furthest leaf descendant.

`ITEMLEVEL(Item[, Direction])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Item* | List item | A list item whose distance to either the root ancestor or the most distant leaf descendant is to be returned. |
| *Direction* (optional) | Keyword | Determines the direction in which the distance is measured.  The keywords are `ROOT` and `LEAF`:  - `ROOT` - Counts the number of root ancestors the *Item* has, plus itself.   	This is the default keyword if you omit the *Direction* argument. - `LEAF` - Counts the number of items in the path to the *Item* 's furthest descendant, plus itself. |

The `ITEMLEVEL` function returns a numeric value.

This function is only available in the Polaris Calculation Engine.

`ITEMLEVEL(United States)`

The item `United States` belongs to a list called `Geographic hierarchy`. The function returns the number of items in the list from `United States` to its root ancestor, including the item itself in the count.

`ITEMLEVEL(United States, LEAF)`

This function returns the number of items in the `Geographic hierarchy` list from `United States` down to its furthest descendant, including the item itself in the count.

The function's result depends on the type of list and the list item's position within it. Key points include:

- The function counts only the items in the list. The list is identified based on the item's data type.
- Returns 0 if,
	- In the `ROOT` direction, *Item* doesn't have a root ancestor.
		- In the `LEAF` direction, *Item* doesn't have any leaf descendants.
- If the list item is blank, the result is 0.
- Top-level items are treated as the (unique) root of the corresponding lists.

The following is an example of a `Geographic hierarchy`:

|  |  | Spain |  |  |
| --- | --- | --- | --- | --- |
|  |  | Italy |  |  |
|  |  |  | England |  |
|  |  |  | Scotland |  |
|  |  |  | Wales |  |
|  |  |  | Greater London |  |
|  |  | **United Kingdom** |  |  |
|  |  | France |  |  |
|  |  | Germany |  |  |
|  | **Europe** |  |  |  |
|  |  | India |  |  |
|  |  | China |  |  |
|  |  | Japan |  |  |
|  | **Asia** |  |  |  |
|  |  |  |  | San Jose |
|  |  |  |  | San Francisco |
|  |  |  |  | Los Angeles |
|  |  |  | **California** |  |
|  |  |  | Texas |  |
|  |  |  | New York |  |
|  |  | **United States** |  |  |
|  |  | Canada |  |  |
|  | **North America** |  |  |  |
| **All regions** |  |  |  |  |

`All regions` has three children: `North America`, `Asia`, and `Europe`.

- `North America` has two children: `Canada` and `United States`.
	- `United States` has three children: `New York`, `Texas`, and `California`.
		- `California` has three children: `Los Angeles`, `San Francisco`, and `San Jose`.
- `Asia` has three children: `Japan`, `China`, and `India`.
- `Europe` has five children: `Germany`, `France`, `United Kingdom`, `Italy`, and `Spain`.
	- `United Kingdom` has four children: `Greater London`, `Wales`, `Scotland`, and `England`.

The following module has three line items:

- `Item` contains all the list items from `Geographic hierarchy`.
- `Result 1` and `Result 2` have the `ITEMLEVEL` formulas.

| **Item** | **Result 1**  `ITEMLEVEL(Item)` | **Result 2**  `ITEMLEVEL(Item, LEAF)` |
| --- | --- | --- |
| Spain | 3 | 1 |
| Italy | 3 | 1 |
| England | 4 | 1 |
| Scotland | 4 | 1 |
| Wales | 4 | 1 |
| Greater London | 4 | 1 |
| United Kingdom | 0 | 0 |
| France | 3 | 1 |
| Germany | 3 | 1 |
| Europe | 0 | 0 |
| India | 3 | 1 |
| China | 3 | 1 |
| Japan | 3 | 1 |
| Asia | 0 | 0 |
| San Jose | 5 | 1 |
| San Francisco | 5 | 1 |
| Los Angeles | 5 | 1 |
| California | 0 | 0 |
| Texas | 4 | 1 |
| New York | 4 | 1 |
| United States | 0 | 0 |
| Canada | 3 | 1 |
| North America | 0 | 0 |
| All regions | 0 | 0 |

- `ITEMLEVEL(Item)` counts the number of root ancestors ‌the *Item* has, plus itself.
- `ITEMLEVEL(Item, LEAF)` counts the number of items in the path to the *Item* 's furthest descendant, plus itself.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fitemlevel-756d1428-5f1d-4d79-8274-d075a1bd312f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>