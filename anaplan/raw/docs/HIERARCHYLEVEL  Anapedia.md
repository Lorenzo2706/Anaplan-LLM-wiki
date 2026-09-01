---
title: "HIERARCHYLEVEL | Anapedia"
source: "https://help.anaplan.com/hierarchylevel-fb423834-dfce-4add-bbb5-0526148e818a"
author:
published:
created: 2026-08-31
description: "Use HIERARCHYLEVEL to find a coordinate's position in a given list. Given a value in a line item, this function uses its coordinate to identify its level in the specified list. This can help you ‌determine how far the item is from the root (top-level ancestor) or from the furthest leaf (bottom-level descendant) in the list."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use HIERARCHYLEVEL to find a coordinate's position in a given list. Given a value in a line item, this function uses its coordinate to identify its level in the specified list. This can help you ‌determine how far the item is from the root (top-level ancestor) or from the furthest leaf (bottom-level descendant) in the list.

`HIERARCHYLEVEL(List[, Direction[, Level type]])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *List* (required) | List or Time | The name of the list or Time in which the coordinate'sdistance to either the root ancestor or the most distant leaf descendant is to be returned.  The list you provide must be related to one of the dimensions used by the line item on which the formula is set. |
| *Direction* (optional) | Keyword | Determines the direction in which the distance is measured.  The keywords are `ROOT` and `LEAF`:  - `ROOT` - Counts how many ancestors the coordinate has, plus itself.   	This is the default keyword if you omit the *Direction* argument. - `LEAF` - Counts the number of items in the path to the coordinate's furthest descendant, plus itself.  This argument is optional. But if you want to use the *Level type*,you must provide this argument. |
| *Level type* (optional) | Keyword | Determines which list items to include in the count.  The keywords are `ALL` and `EXPLICIT`:  - `ALL` - Includes all list items in the count.   	This is the default keyword if you omit the *Level type* argument. - `EXPLICIT` - Includes only one item for each distinct list that makes up the hierarchy.  This argument is optional. But if you want to use this argument, you must provide the *Direction* argument. |

The `HIERARCHYLEVEL` function returns a numeric value.

This function is only available in the Polaris Calculation Engine.

`HIERARCHYLEVEL(Geographic hierarchy)`

For each value of the line item, this function returns the number of ancestors of the coordinate of the value in the `Geographic hierarchy` hierarchy, including the coordinate itself in the count.

`HIERARCHYLEVEL(Geographic hierarchy, LEAF, ALL)`

This function returns the distance to the furthest leaf descendant of the coordinate within the given list `Geographic hierarchy`, plus itself, including `ALL` the list items in the count.

The function's result depends on the type of list and the coordinate's position within it:

- If the coordinate isn't part of the specified list, the result is 0.
- Returns 0 if,
	- In the `ROOT` direction, the coordinate doesn't have a root ancestor.
		- In the `LEAF` direction, the coordinate doesn't have any leaf descendants.
- Top-level items are treated as the (unique) root of the corresponding lists.

- The list you provide must be related to one of the dimensions used by the line item on which the formula is set.
- It also won’t work with ancestor hierarchies of the target dimension.  
	For example, if your line item uses `listB` as its dimension, you can’t use this function with `listA`, if `listA` is a parent of `listB`.

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
- `Result 1`, `Result 2`, `Result 3`, and `Result 4` have the `HIERARCHYLEVEL` formulas.

| **Item** | **Result 1**  `HIERARCHYLEVEL(Geographic hierarchy)` | **Result 2**  `HIERARCHYLEVEL(Geographic hierarchy, LEAF)` | **Result 3**  `HIERARCHYLEVEL(Geographic hierarchy, ROOT, EXPLICIT)` | **Result 4**  `HIERARCHYLEVEL(Geographic hierarchy, ROOT, ALL)` |
| --- | --- | --- | --- | --- |
| Spain | 3 | 1 | 2 | 3 |
| Italy | 3 | 1 | 2 | 3 |
| England | 4 | 1 | 2 | 4 |
| Scotland | 4 | 1 | 2 | 4 |
| Wales | 4 | 1 | 2 | 4 |
| Greater London | 4 | 1 | 2 | 4 |
| United Kingdom | 3 | 2 | 2 | 3 |
| France | 3 | 1 | 2 | 3 |
| Germany | 3 | 1 | 2 | 3 |
| Europe | 2 | 3 | 2 | 2 |
| India | 3 | 1 | 2 | 3 |
| China | 3 | 1 | 2 | 3 |
| Japan | 3 | 1 | 2 | 3 |
| Asia | 2 | 2 | 2 | 2 |
| San Jose | 5 | 1 | 2 | 5 |
| San Francisco | 5 | 1 | 2 | 5 |
| Los Angeles | 5 | 1 | 2 | 5 |
| California | 4 | 2 | 2 | 4 |
| Texas | 4 | 1 | 2 | 4 |
| New York | 4 | 1 | 2 | 4 |
| United States | 3 | 3 | 2 | 3 |
| Canada | 3 | 1 | 2 | 3 |
| North America | 2 | 4 | 2 | 2 |
| All regions | 1 | 5 | 1 | 1 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fhierarchylevel-fb423834-dfce-4add-bbb5-0526148e818a&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>