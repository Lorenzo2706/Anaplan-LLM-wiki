---
title: "Actions and filtered picklists"
source: "https://help.anaplan.com/actions-and-filtered-picklists-031355eb-ce48-4b79-a071-3dd2294a9e8c"
author:
published:
created: 2026-05-13
description: "A picklist is a dropdown list that provides users with a list of valid values to select from. Filtered picklists contain more complexity and reference other lists in a model: the driver and filter lists. Selections made in a driver list determine what users can select in a filter list."
tags:
  - "clippings"
---
[Picklists](https://help.anaplan.com/picklists-ddeaf549-4699-4e56-be9a-185205c49823 "Picklists")

A picklist is a dropdown list that provides users with a list of valid values to select from. Filtered picklists contain more complexity and reference other lists in a model: the driver and filter lists. Selections made in a driver list determine what users can select in a filter list.

[Create](https://help.anaplan.com/d16ed36a-0836-44f7-9db5-e7f0477a9213) your driver, filter, and valid combinations lists in **General Lists** in the model settings bar. See examples in [Create many-to-many filtered picklists](https://help.anaplan.com/4969bb8c-edae-47be-8241-9dd3942671bd).

If you want to create many-to-many filtered picklists, you can use the **Assign** action with a valid combinations list to map the relationship between list items in the driver and filter lists.

The **Assign** action enables you to easily assign a list item to a parent. The action requires a numbered list with at least one list-formatted property, and a parent hierarchy. For many-to-many filtered picklists, the driver list must be a parent of the valid combinations list.

1. Select **General Lists** in the model settings bar, select your valid combinations list, then select **Open**.
2. Select **Configure**.
3. Select the driver list in **Parent Hierarchy**. For example, *Role*.
4. Select the **Numbered List?** checkbox.
5. Select **Apply**.
1. Select **Properties** > **Insert**, then [create a filter list property](https://help.anaplan.com/da73f852-e39f-4046-bf97-675274ce0947). For example, *Compensation Plan* (filter).
2. Select **OK**.
3. Select the filter list property, then select the ellipsis (...) in the **Format** column.
4. Select **List** in the **Type** dropdown, then select the filter list in the **List** dropdown. For example, *Compensation Plan*.
5. Select **OK**.
1. Select **Modules** in the model settings bar, then select **Insert Module**.
2. Add the valid combinations list on columns, insert line items on rows, and remove Time. Your line items might be *Role Compensation 1*, *Role Compensation 2*, etc.
3. Select **View** > **Publish to Dashboard** > **New Dashboard**, then type a name for the [dashboard](https://help.anaplan.com/904f39ff-0fb8-4426-86c0-dacc48d1095d). For example, *Valid Combinations of Role to Compensation Plan*.
4. Select **Save**.
5. Select **Save & Exit** in the dashboard toolbar. If the dashboard toolbar is hidden, right-click on the dashboard tab to show the toolbar.
1. Select **Actions** in the model settings bar, then select **New Action** > [**Assign**](https://help.anaplan.com/4b6861d6-7587-4eb7-85f9-262cbfec4de3).
2. Type a name for the **Button text**. For example, *Assign*.
3. In **Using list-formatted property**, select the filter list property in the valid combinations list.
4. Select **OK**.
5. Select the action, then select **View** > **Publish to Dashboard**. Publish to the same dashboard that you created earlier. For example, *Valid Combinations of Role to Compensation Plan*.
6. Select **Save & Exit** in the dashboard toolbar.
1. In your dashboard, select a list item from the driver list (*Role*), then select the **Assign** action.
2. Select the right arrow to move list items from the filter list in the left-hand unassigned field to the right-hand assigned field. For example, if you select *Executive* in the *Role* list, you can assign *Plan A* and *Plan B* to that role.
3. Select **OK**.

When you assign driver list items to filter list items, they populate the valid combinations list in **Grid View**. As the valid combinations list is a [numbered list](https://help.anaplan.com/371af0ef-1465-4c4f-9a73-4150f4a6ee95), each list item in the filter list contains a unique identifier.

|  | **Parent** | **Code** | **Compensation Plan (Filter)** |
| --- | --- | --- | --- |
| #1 | Executive |  | Plan A |
| #2 | Executive |  | Plan B |
| **Executive** |  |  |  |
| #3 | Senior Manager |  | Plan C |
| **Senior Manager** |  |  |  |
| #4 | Manager |  | Plan D |
| **Manager** |  |  |  |

When you have set up the relationships between driver and filter list items in the valid combinations list, follow the steps in [Create many-to-many filtered picklists](https://help.anaplan.com/4969bb8c-edae-47be-8241-9dd3942671bd) to create a module for the filtered picklist.

When you format the filter line item in your module, the **Parent Hierarchy** in the valid combinations list is the parent that drives the combinations. In this example, the parent is the driver (*Role*) list.

![The image displays the Format dialog for the filter line item. It shows valid combinations between list items in the driver list, and list items in the filter list.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/7466104c-170d-4019-aac9-1b4a97899c58/Capto_Capture%202021-10-13_05-34-13_pm.png)

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Factions-and-filtered-picklists-031355eb-ce48-4b79-a071-3dd2294a9e8c&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>