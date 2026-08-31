---
title: "Dimensions | Anapedia"
source: "https://help.anaplan.com/dimensions-e020c93d-9f3e-4cce-8294-2d34073b302a"
author:
published:
created: 2026-05-13
description: "Dimensions are the lists that workspace administrators select to be a module's rows, columns, and pages. They provide the structure of a module and define the context for data in cells."
tags:
  - "clippings"
---
Dimensions are the lists that workspace administrators select to be a module's rows, columns, and pages. They provide the structure of a module and define the context for data in cells.

Dimensions can be:

- Lists that workspace administrators create in the General lists pane.  
	You can use list subsets as dimensions if only some items in a list apply to a module's data.
- Time, Versions, Users, and Organization, which are default lists that exist in every model.
- The line items of the module, or a line item subset.

The data in a cell has meaning due to the context given by the dimensions that apply to the cell.

You select the lists to use as the dimensions of a module when you [create the module](https://help.anaplan.com/686ff444-5356-48d1-9a9c-7cb2544e31d8). You can change the dimensions that apply to a module's data in the **Applies To** field of the **Modules** pane, or in Blueprint view for a module.

Once selected, you can [pivot](https://help.anaplan.com/1fcfb4a7-e576-46f7-81a1-4b0eb18294c3) your dimensions to move them between rows, columns, or pages.

Default lists exist in all models. They cannot be deleted and are always available to use as dimensions.

Organization is a default list that can be configured in **General lists**. It's automatically populated with the list item **Total Company***.* To summarize your data, **Total Company** is automatically set as the **Top Level** item that all other list items roll up to.

Time, Versions, and Users are more complex than the lists workspace administrators create in General lists. Each has its own pane where you can configure the specific settings for that dimension and import data.

You can select **Time** , **Versions** , and **Users** from **Model settings** to open a configuration pane.

This *Country Margin Report* module has a *Products* liston rows, line items on columns, and Time and *Countries* on pages.

| **FY22** | **Germany** |
| --- | --- |

|  | **Revenue** | **Cost of Sales** | **Margin** | **Margin %** |
| --- | --- | --- | --- | --- |
| **Chocolates** | 2,675,773 | 744,867 | 1,930,906 | 72.16% |
| **Sours** | 3,132,459 | 805,269 | 2,327,190 | 74.29% |
| **Taffy** | 3,436,924 | 843,154 | 2,593,771 | 75.47% |
| **Fudge** | 1,957,370 | 520,075 | 1,437,295 | 73.43% |
| **All Products** | 11,202,526 | 2,913,365 | 8,289,161 | 73.99% |

The values you select for the dimensions on pages define the context for the module grid: *FY22* is selected as the time and *Germany* is selected as the country. So, the grid displays data for Germany in financial year 22.

The context for each cell is further refined by the values in the rows and columns that apply to the cell. So the cell in the top left, with a value of *2,675,773*, is the *Revenue* from *Chocolates* sold in *Germany*, in *FY22*.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fdimensions-e020c93d-9f3e-4cce-8294-2d34073b302a&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>