---
title: "Cell count limit on line item blocks"
source: "https://help.anaplan.com/cell-count-limit-on-line-item-blocks-8b535ad6-79fd-4793-8435-2248913bf8ab"
author:
published:
created: 2026-05-13
description: "Module data is stored in cells where line items intersect with other dimensions. Cells are stored in blocks, each of which contains the cells for one combination of time period, version, and list level for a line item. Each line item block can contain up to 2,147,483,647 cells."
tags:
  - "clippings"
---
Module data is stored in cells where line items intersect with other dimensions. Cells are stored in blocks, each of which contains the cells for one combination of time period, version, and list level for a line item. Each line item block can contain up to 2,147,483,647 cells.

A [line item](https://help.anaplan.com/52d76cdd-2571-4400-8f34-b15dd5651b9f) can have more cells than the limit for a block. This is because one line item can apply to several periods, versions, lists, and levels within a list. However, the limit can affect line items if:

- You try to create a line item that uses a block that exceeds the limit.
- You change the lists in the **Applies To** column for a line item in a way that would put a line item block over the limit.
- You make a change to one of the lists that applies to a line item in a way that would put a line item block over the limit.

If any change you try to make would cause a block to exceed the cell count limit, the change is not applied. A notification advises you to reduce the cell count.

You can [check the total cell count](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) for a line item in the Blueprint view of a module. This is a count for the cells in all the blocks the line item contains.

If write [access is granted to a list by model role](https://help.anaplan.com/2a2c1ccd-b2d4-420c-b58d-3a24f0e03295), additional cells are pre-allocated to any line item block that applies to the list. This enables efficient recalculation of values in the block when items are added or removed by users who have that role.

Pre-allocated cells do not count towards your workspace allowance until you use them. They also do not display in the line item cell count or list item count. However, they do count towards the number of cells in your line item block. In rare cases, this may mean that a block exceeds the cell count limit, even though you're not currently using those cells.

Create a line item, *Units Sold*, that applies to two lists, *Cities* and *Product*, as well as Time and Versions.

Set the Model Calendar for a single year with the Calendar Type **Calendar Months/Quarters/Years**. Set the time scale for the line item to **Months**.

Ensure the model has three versions: *Actual*, *Budget*, and *Forecast*.

| London | Mar 21 | Budget |
| --- | --- | --- |

|  | Apples | Oranges | Pears |
| --- | --- | --- | --- |
| Units Sold | 5,000 | 4,000 | 3,000 |

*Cities* has three items and *Product* has four items. 3 x 4 = 12.

There are 17 time periods: 12 months, 4 quarters, and 1 year. 12 x 17 = 204.

With three versions, the number of cells is: 12 x 17 x 3 = 612.

However, the blocks that store this data each only contain the data for one period, version, and list level combination.

So the data for the intersection of *Mar 21*, *Budget*, *Cities*, and *Product*, with *Units Sold* is a single block. As only one version and time period apply to the block, the cell count is based on the number of items in the list level: 3 x 4 = 12.

In this case, both *Cities* and *Product* only have a single level. However, if you add a summary or top level, the line item has additional blocks for each of these.

Add a *Countries* list as the parent of *Cities*, with two items, *UK* and *Japan*. *UK* provides a summary level for the two *Cities* items, *London* and *Manchester*. *Japan* provides a summary for units sold in *Tokyo* and *Osaka*.

As *Countries* only has two items, blocks for the *Countries* list level are smaller: 3 x 2 = 6. And this is multiplied by time period and versions: 6 x 17 x 3 = 306.

Add this to the cell count from the child list level, and the line item cell count is now: 612 + 306 = 918.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcell-count-limit-on-line-item-blocks-8b535ad6-79fd-4793-8435-2248913bf8ab&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>