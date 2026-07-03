---
title: "Create one-to-many filtered picklists"
source: "https://help.anaplan.com/create-one-to-many-filtered-picklists-cfeebee8-6803-4941-bf65-bc2d58578fd2"
author:
published:
created: 2026-05-13
description: "A picklist is a dropdown list that provides users with a list of valid values to select from. Filtered picklists contain more complexity and reference other lists in a model: the driver and filter lists. Selections made in a driver list determine what users can select in a filter list.One-to-many filtered picklists map single list items in a driver list to multiple list items in a filter list. For example, Senior Director in the Role list qualifies for Plan B and Plan C in the Compensation Plan list."
tags:
  - "clippings"
---
[Picklists](https://help.anaplan.com/picklists-ddeaf549-4699-4e56-be9a-185205c49823 "Picklists")

A picklist is a dropdown list that provides users with a list of valid values to select from. Filtered picklists contain more complexity and reference other lists in a model: the driver and filter lists. Selections made in a driver list determine what users can select in a filterlist.

One-to-many filtered picklists map single list items in a driver list to multiple list items in a filter list. For example, *Senior Director* in the *Role* list qualifies for *Plan B* and *Plan C* in the *Compensation Plan* list.

[Create](https://help.anaplan.com/d16ed36a-0836-44f7-9db5-e7f0477a9213) your driver and filter lists in **General Lists** in the model settings bar. Ensure both lists contain list items.

For example, the *Role* list (driver) includes the *Executive*, *Senior Director*, and *Team Leader* list items. The *Compensation List* (filter) includes the *Plan A*, *Plan B*, and *Plan C* list items.

1. Select **General Lists** in the model settings bar, select the filter list, then select **Open**.
2. Select **Properties** > **Insert**, then [create a driver list property](https://help.anaplan.com/da73f852-e39f-4046-bf97-675274ce0947). For example, *Role (driver)*.
3. Select **OK**.
4. Select the driver list property, then select the ellipsis (...) in the **Format** column.
5. Select **List** in the **Type** dropdown, then select the driver list in the **List** dropdown.
6. Select **OK**.
1. Select **Grid View** in the filter list.
2. Map the relationships between list items in the driver and filter lists. For example, *Senior Director* maps to *Plan B* and *Plan C*.

|  | **Parent** | **Code** | **Role (driver)** |
| --- | --- | --- | --- |
| Plan A |  |  | Executive |
| Plan B |  |  | Senior Director |
| Plan C |  |  | Senior Director |
| Plan D |  |  | Team Leader |
| Plan E |  |  | Staff Member |

1. Select **Modules** in the model settings bar, then select **Insert Module**.
2. Insert two line items on columns that represent the driver and filter lists. For example, *Role* and *Compensation Plan*. In this example, you can also add the *Employees* list on rows, and remove Time.
3. Select **OK**.
4. In **Blueprint**,select the driver line item, then select the ellipsis (...) in the **Format** column.
5. Select **List** in the **Type** dropdown, then select the driver list in the **List** dropdown.
6. Select **OK**.
7. Select the filter line item, then select the ellipsis (...) in the **Format** column.
8. Select **List** in the **Type** dropdown, then select the filter list in the **List** dropdown.
9. Select **Dependent** in the **Filter** options, then select the driver list in the **Filter based on data in** dropdown to view combination examples. If you want users to access all list items in the filter list, select **Allow access to unfiltered items** in the **Format** dialog to enable **Show All** at the bottom of the filtered picklist.
10. Select **OK**.

In your module, you can map list items in the driver line item to valid values in the filter line item.

|  | **Role** | **Compensation Plan** |
| --- | --- | --- |
| Employee A | Executive | Plan A |
| Employee B | Senior Director | Plan B |
| Employee C | Senior Director | Plan C |
| Employee D | Team Leader | Plan D |
| Employee E | Staff Member | Plan E |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcreate-one-to-many-filtered-picklists-cfeebee8-6803-4941-bf65-bc2d58578fd2&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>