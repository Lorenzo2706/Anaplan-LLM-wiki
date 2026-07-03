---
title: "Create display names for numbered lists"
source: "https://help.anaplan.com/create-display-names-for-numbered-lists-a916143c-d348-4e0c-afaf-100198dcd2ef"
author:
published:
created: 2026-05-13
description: "Workspace administrators can create display names for list items in numbered lists. These are list properties with Text or List formats that you set as display names for the list in General lists."
tags:
  - "clippings"
---
[Numbered lists](https://help.anaplan.com/numbered-lists-371af0ef-1465-4c4f-9a73-4150f4a6ee95 "Numbered lists")

Workspace administrators can create display names for list items in numbered lists. These are list properties with **Text** or **List** formats that you set as display names for the list in **General lists**.

Before you can assign properties as display names, you must have a numbered list that has list items in it.

If you want to use item names from another list to provide display names for the numbered list, you must create the other list first.

To create display names for items in a numbered list is a two-stage process:

1. Create a display name list property
2. Add display names to the numbered list items

To create a the list property:

1. In **General lists** select the numbered list you want to create display names for, then select **Open**.
2. Select the **Properties** tab, then **Insert**.
3. Type a name for the list property, such as *Display name*.
4. Select **OK**.
5. Select the ellipsis () in the **Format** column.
6. Select **Text** or **List** from the **Type** dropdown.  
	If you select **List**:
	1. Choose a list as the source for your display names from the **List** dropdown.
		2. Optionally filter the list items available as display names. Select:
		- **Selective Access** to filter by the user's [selective access permissions within the picklist](https://help.anaplan.com/b0a5b483-422f-48bb-a2e4-42ecdf1e5e3b).
				- **Dependent** to create a [one-to-many](https://help.anaplan.com/cfeebee8-6803-4941-bf65-bc2d58578fd2) or [many-to-many dependent dropdown](https://help.anaplan.com/4969bb8c-edae-47be-8241-9dd3942671bd).
				- **Allow access to unfiltered items** if you want to filter the list, but have a **Show All** option so users can view other results.
7. Go to **General lists** and select the property you created in the **Display Name Property** dropdown.

To add a display name to numbered list items:

1. In **General lists** select the numbered list you want to create display names for, then select **Open**.
2. Select **Grid View**.
3. Enter a display name in the display name property for the item you want to name:
	- For text-formatted display name properties, type a display name in the property's column.
		- For list-formatted display name properties, select the option from the dropdown list in the property's column.

The display names show in place of the numbered items of the list. However, if more than one item has the same display name, the numbers display in brackets when you view the list in Tree View. For example, if you have a list of three people (Rajesh Patel, Fiona Green, and Rajesh Patel), then in Tree View, this displays as:

- *Rajesh Patel (#1)*
- *Fiona Green*
- *Rajesh Patel (#3)*

Everywhere else, the two items with the same display name show as just *Rajesh Patel*.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcreate-display-names-for-numbered-lists-a916143c-d348-4e0c-afaf-100198dcd2ef&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>