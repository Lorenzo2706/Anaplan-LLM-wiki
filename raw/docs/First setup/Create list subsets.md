---
title: "Create list subsets"
source: "https://help.anaplan.com/create-list-subsets-3503ac4b-3778-47ba-97ac-769826df0180"
author:
published:
created: 2026-05-13
description: "Model builders use list subsets to create a shorter list of items from larger lists.For example, if you have a long list, you can create a list subset to target specific list items."
tags:
  - "clippings"
---
[List subsets](https://help.anaplan.com/list-subsets-589d9f5d-f439-40a4-905f-5027c2dc9c21 "List subsets")

Model builders use list subsets to create a shorter list of items from larger lists.

For example, if you have a long list, you can create a list subset to target specific list items.

[Create any lists](https://help.anaplan.com/d16ed36a-0836-44f7-9db5-e7f0477a9213) you might need in **General Lists** in the model settings bar.

1. Select **General Lists** in the model settings bar.
2. Select a list, then select **Open**.
3. Select **Subsets** > **Insert**.
4. Type a name for the list subset. Create extra list subsets by typing each list subset on a new line. Select **Start** or **End** to add the list subset to the start or to the end of the list.

**Note**: use proper [naming conventions](https://help.anaplan.com/aeb0b95e-f7a3-4fe5-81c7-aec9a12f80be) for your list subset. For example, add a prefix (*ls*, *sub*, *ss*) to indicate that the list is a subset of a larger list.

5. Select **OK**. The list subset appears as an additional column in **Grid View**.
6. Select **Grid View** and select the list items you want to include in the list subset.  
	You can assign items to a list subset by import. The subset displays as [a list property that you can map](https://help.anaplan.com/29a86b5d-82cd-49c0-80f9-a4ec781911fa) to any Boolean-format source column.  
	For example, you can include two employees from the *Employees* list in the *Sales team* list subset.

|  | **Parent** | **Code** | **List subset (Sales team)** |
| --- | --- | --- | --- |
| Employee A | Sales | SA01 |  |
| Employee B | Sales | SA02 |  |
| Employee C | Product Management | PM01 |  |

6. Apply the subset as a dimension in your modules, views, or calculations. For example, if a module uses the `Products` list as a dimension, you can replace it with the `Active Products Subset` to limit its scope.

To reorder list subsets, select **Reorder** then choose from one of the options, or drag the list subset into a new position.

When you create a list subset, it appears in the larger list's **Subsets** column in **General Lists**.

You can create list subsets that are driven by conditions in line items.

1. In the parent list, add a new property, or in a module add a line item, with a Boolean format. Name the property something descriptive like `Include in Subset`.
2. Define a formula or manually set the Boolean values to determine inclusion. For example, if the list represents products, you might use a formula such as `'Product Status' = "Active"`. This ensures only active products are included in the subset.
3. Define the subset.
	1. Go to the **Lists** tab in the Anaplan model.
		2. Select the parent list, and under **Subsets**, create a new subset.
		3. Name the subset, for example: `Active Products Subset`.
4. Check the items manually or via the Boolean property in the list editor. There is no automatic synchronization between properties and subsets, so the process may involve regular updates, especially for dynamic conditions.
5. Apply the subset as a dimension in your modules, views, or calculations. For example, if a module uses the `Products` list as a dimension, you can replace it with the `Active Products Subset` to limit its scope.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcreate-list-subsets-3503ac4b-3778-47ba-97ac-769826df0180&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>