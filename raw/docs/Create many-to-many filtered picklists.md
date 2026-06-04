---
title: "Create many-to-many filtered picklists"
source: "https://help.anaplan.com/create-many-to-many-filtered-picklists-4969bb8c-edae-47be-8241-9dd3942671bd"
author:
published:
created: 2026-05-13
description: "A picklist is a dropdown list that provides users with a list of valid values to select from. Filtered picklists contain more complexity and reference other lists in a model: the driver and filter lists. Selections made in a driver list determine what users can select in a filter list.Many-to-many filtered picklists map multiple list items in a driver list with multiple list items in a filter list. For example, Executive, Senior Director, and Senior Manager in the Role list qualify for Plan A in the Compensation Plan list. The Senior Director and Senior Manager roles also qualify for Plan B."
tags:
  - "clippings"
---
[Picklists](https://help.anaplan.com/picklists-ddeaf549-4699-4e56-be9a-185205c49823 "Picklists")

A picklist is a dropdown list that provides users with a list of valid values to select from. Filtered picklists contain more complexity and reference other lists in a model: the driver and filter lists. Selections made in a driver list determine what users can select in a filter list.

Many-to-many filtered picklists map multiple list items in a driver list with multiple list items in a filter list. For example, *Executive, Senior Director,* and *Senior Manager* in the *Role* list qualify for *Plan A* in the *Compensation Plan* list. The *Senior Director* and *Senior Manager* roles also qualify for *Plan B*.

[Create](https://help.anaplan.com/d16ed36a-0836-44f7-9db5-e7f0477a9213) your driver and filter lists in **General Lists** in the model settings bar.

Unlike [one-to-many filtered picklists](https://help.anaplan.com/cfeebee8-6803-4941-bf65-bc2d58578fd2), many-to-many filtered picklists also require a valid combinations list to map the relationship between list items in the driver and filter lists. An example of the valid combinations list could be *Compensation Plan Lookup*. Ensure all three lists contain list items.

For example, the *Compensation Plan Lookup* list contains the *Role Compensation 1*, *Role Compensation 2*, and *Role Compensation 3* list items.

1. Select **General Lists** in the model settings bar, select your valid combinations list, then select **Open**.
2. Select **Properties** > **Insert**, then [create two list-formatted properties](https://help.anaplan.com/da73f852-e39f-4046-bf97-675274ce0947). For example, *Role* (driver) and *Compensation Plan* (filter).
3. Select **OK**.
4. Select the driver list property, then select the ellipsis (...) in the **Format** column.
5. Select **List** in the **Type** dropdown, then select the driver list(*Role*) in the **List** dropdown.
6. Select **OK**.
7. Select the filter list property, then select the ellipsis (...) in the **Format** column.
8. Select **List** in the **Type** dropdown, then select the filter list (*Compensation Plan*)in the **List** dropdown.
9. Select **OK**.
1. Select **Grid View** in the valid combinations list.
2. Map the relationships between list items in the driver and filter lists.

|  | **Parent** | **Code** | **Role (driver)** | **Compensation Plan (filter)** |
| --- | --- | --- | --- | --- |
| Role Compensation 1 |  |  | Executive | Plan A |
| Role Compensation 2 |  |  | Senior Director | Plan A |
| Role Compensation 3 |  |  | Senior Director | Plan B |
| Role Compensation 4 |  |  | Senior Manager | Plan A |
| Role Compensation 5 |  |  | Senior Manager | Plan B |

1. Select **Modules** in the model settings bar, then select **Insert Module**.
2. Insert two line items that represent the driver and filter lists on columns. For example, *Role* and *Compensation Plan*. In this example, you can also add the *Employees* list on rows, and remove Time.
3. Select **OK**.
4. In **Blueprint** select the driver line item, then select the ellipsis (...) in the **Format** column.
5. Select **List** in the **Type** dropdown, then select the driver list in the **List** dropdown.
6. Select **OK**.
7. Select the filter line item, then select the ellipsis (...) in the **Format** column.
8. Select **List** in the **Type** dropdown, then select the filter list in the **List** dropdown.
9. Select **Dependent** in the **Filter** options, then select the driver list in the **Filter based on data in** dropdown to view combination examples. If you want users to access all list items in the filter list, select **Allow access to unfiltered items** in the **Format** dialog to enable **Show All** at the bottom of the filtered picklist.
![The Format dialog shows Dependent formatting options for the Compensation Plan line item.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/befa278f-2412-48fa-b446-da6a2497fd82/Many-to-many-format.png)
10. Select **OK**.

In your module, you can map list items in the driver line item to valid values in the filter line item.

|  | **Role** | **Compensation Plan** |
| --- | --- | --- |
| Employee A | Executive | Plan A |
| Employee B | Senior Director | Plan A |
| Employee C | Senior Director | Plan A |
| Employee D | Senior Manager | Plan B |
| Employee E | Senior Manager | Plan B |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcreate-many-to-many-filtered-picklists-4969bb8c-edae-47be-8241-9dd3942671bd&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>