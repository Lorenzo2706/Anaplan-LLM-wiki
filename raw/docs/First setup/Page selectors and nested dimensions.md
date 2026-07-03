---
title: "Page selectors and nested dimensions"
source: "https://help.anaplan.com/page-selectors-and-nested-dimensions-0c637bf9-24ed-4d2d-be92-1311d6a429eb"
author:
published:
created: 2026-05-13
description: "You can use page selectors and nested dimensions to add more dimensions to the context of your data. Without these, you could only have one dimension on rows and one on columns."
tags:
  - "clippings"
---
[Dimensions](https://help.anaplan.com/dimensions-e020c93d-9f3e-4cce-8294-2d34073b302a "Dimensions")

You can use page selectors and nested dimensions to add more dimensions to the context of your data. Without these, you could only have one dimension on rows and one on columns.

Workspace administrators can arrange dimensions as nested, or put them on pages, when they [create a module](https://help.anaplan.com/686ff444-5356-48d1-9a9c-7cb2544e31d8) or [saved view](https://help.anaplan.com/81a92257-5ed0-429a-b4e8-fbde8c05a3fc). Any user can [pivot](https://help.anaplan.com/1fcfb4a7-e576-46f7-81a1-4b0eb18294c3) the view to change how the data displays, but their changes only last for their current browser session.

If you place a dimension on pages, the data that displays in the grid only relates to the item currently selected in the page selector. Users can select a different item to see data that relates to the new item.

You can display any dimension as a page selector. In modules and on dashboards, page selectors display as dropdowns above the grid. One page selector displays for each dimension.

For Time or Versions, the default value for a page selector matches the model's current period or current version. You can configure page selectors on dashboards, to change the default value for Time and Versions page selectors.

Suppose you want a module that displays margin data for products, but you want to be able to see that data according to different time periods and countries.

You can create a *Country Margin* module that has a *Products* list on rows and has line items for *Revenue*, *Cost of Sales*, and *Margin* on columns. To add further context to the data, you can add *Time* and a *Countries* list as page selectors.

| FY23 | USA |
| --- | --- |

|  | **Revenue** | **Cost of Sales** | **Margin** |
| --- | --- | --- | --- |
| **Chocolates** | 2,675,773 | 744,867 | 1,930,906 |
| **Sours** | 3,132,459 | 805,269 | 2,327,190 |
| **Taffy** | 3,436,924 | 843,154 | 2,593,771 |
| **Fudge** | 1,957,370 | 520,075 | 1,437,295 |
| **All Products** | 11,202,526 | 2,913,365 | 8,289,161 |

This grid has **FY23** selected in the *Time* page selector and *USA* selected in the *Countries* page selectors. So the grid displays data for the USA for financial year 2023.

Workspace administrators can [publish a page selector to a dashboard](https://help.anaplan.com/2c695910-872d-4ed0-b686-740338546279) by itself. If you enable synchonized paging, you can use the page selector to define the context for all dashboards and modules that use that dimension. If you disable synchronized paging, modules and dashboards that share that dimension can display different contexts.

You can nest up to three dimensions on rows or columns as an alternative way to add further context to your data.

**Note:** In Polaris, you can nest up to 8 dimensions on an axis.

You nest on the **New Module** or **Pivot** screen, when you place more than one dimension on rows or columns. The top dimension becomes the outer dimension on the grid and the bottom dimension the inner dimension.

![The Pivot dialog for a module grid. Three dimensions are on rows: Time, Countries, and Products. Line items is on rows.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/f26b5a78-e65e-47c5-a9a8-fc48560263c4/nested-pivot.png)

Each item in the outer dimension has each item from the next dimension as a separate row within it. If you nest three dimensions, each item from the middle dimension has a row for each item in the inner dimension within that.

![A module grid with three dimensions nested on rows: Time as the outer dimension, Countries as the middle dimension, and Products as the inner dimension. The first item for Time, Jan 22, has rows for Japan, UK, USA, and All countries next to it. Each country then has rows for Chocolates, Sours, Taffy, Fudge, and All products next to it.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/5919a315-67b1-42f4-a984-c1e2d23deaf7/nested-grid.png)

**Note:** If your module contains large amounts of data, it's best practice to use [page selectors](https://help.anaplan.com/1511eecc-add8-4fec-b95e-685cd6bcb0df) so the data is easy to view.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpage-selectors-and-nested-dimensions-0c637bf9-24ed-4d2d-be92-1311d6a429eb&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>