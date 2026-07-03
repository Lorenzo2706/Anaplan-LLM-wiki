---
title: "Users list"
source: "https://help.anaplan.com/users-list-f3333ecf-a1cc-43d8-af03-ec65c5cdd428"
author:
published:
created: 2026-05-13
description: "The Users list is a list of all the users that have access to a model."
tags:
  - "clippings"
---
[Dimensions](https://help.anaplan.com/dimensions-e020c93d-9f3e-4cce-8294-2d34073b302a "Dimensions")

The Users list is a list of all the users that have access to a model.

Workspace administrators can [control user access to the model](https://help.anaplan.com/8c495688-216e-49c4-aa56-a4b70487e5d7) from the **Users** pane in the model settings bar.

The Users pane displays all users that have access to a workspace. This includes users that have the **No Access** model role for the current model, but can access other models in the workspace. However, the Users list only includes those with access to the model.

You can use the Users list as a dimension in modules.

When you use the Users list as a module dimension, workspace administrators can view all users in the list and any top-level item on the list. Other users can only see their own email address, and they can't see any top-level item that's been added.

If a user is assigned the [**No Access**](https://help.anaplan.com/30783e17-b789-4005-b87a-ff15cd3c9044) model role, the user doesn't display in the module dimension for all users.

If a module has Users as a dimension, you can create a rule to [filter](https://help.anaplan.com/43b09d33-2e2b-4405-8641-f8e4fefac445) by the **Current User**. When you filter by **Current User** only data for the current user displays. This applies even if the user is a workspace administrator, and the Users list is on Pages, and you select a different user from the Pages dropdown.

You can also select **Show All Users: On** or **Show All Users: Off** in the **Users List** column of the Modules pane or Blueprint view for the module. This toggles whether workspace administrators can view the full list or only their own user name. It applies only to what displays in the dimension, and not in any line item you format with the User list.

The Users list is always treated as [production data](https://help.anaplan.com/def2aa72-278a-4b85-97fb-d858c1dbbe97), which means you can't select users as list items to reference directly in formulas. That is, you can't refer to a Users list item with the syntax `Users.username`.

You can use the Users list to format a line item as a [picklist](https://help.anaplan.com/ddeaf549-4699-4e56-be9a-185205c49823). By default, the picklist dropdown displays all the users in the list, even to users who aren't workspace administrators.

As a workspace administrator, you can limit the picklist so non-workspace admins only see their own names. To set this limitation, select **Selective Access** as a filter in the line item **Format** dialog. If you also select **Allow access to unfiltered items**, users can select **Show All** to view the entire Users list.

![The line item Format dialog with List selected as the Type and Users selected as the list. Selective Access and Allow access to unfiltered items are selected for the Filter options.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/96c332cd-126c-4526-96cc-7e9017ba477b/format-users-picklist.png)

The full list still displays for workspace administrators.

**Note:** Selective access for the Users list differs from [selective access](https://help.anaplan.com/f0dd364d-cd04-429e-b788-15c79d8cf698) that applies to general lists. Workspace administrators control selective access for general lists in the Users pane or in Grid view for each list. Selective access for the Users list only ever filters access to the user's own user name in a picklist.

The **Users** list displays at the top of [**General lists**](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075). The Users list contains all the users that have access to the model.

The Users list can be used as a [dimension](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a) in modules and can be used for [list-formatted line items](https://help.anaplan.com/bf3a0391-5c5a-4da2-9445-685a204d3e68).

**Note**: You are unable to delete or rename the Users list. You are also unable to reorder, add, edit, or delete users from the Users list.

Workspace administrators can [add a top-level item](https://help.anaplan.com/62030bd7-4e9a-4e9d-b3cd-84eaaac68ff0) to the **Users** list. The top-level item enables you to view the total data across the users list, and it's based on the [summary method](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) you selected.

With this Users list, you can also set the top-level item in the list as a [default page](https://help.anaplan.com/4764efd5-3f7c-4537-9202-de21a858cade).

Workspace administrators can [create a list subset](https://help.anaplan.com/e8469111-0e83-4c36-87b3-3a1dfe563eb9) with the **Users** list in **General list**. The Users list subset can also be used as a [dimension](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a) in modules and can be used for [list-formatted line items](https://help.anaplan.com/bf3a0391-5c5a-4da2-9445-685a204d3e68).

If you add a top-level item to the Users list and you use the list subset as a dimension in a module, the top-level item displays in the module and can't be deleted. The top-level item represents only the items in the subset.

If a user is assigned the **Full Access** [model role](https://help.anaplan.com/30783e17-b789-4005-b87a-ff15cd3c9044) or a custom model role in the **Users** pane, the user displays in the **Users** list in **General lists**. If a user is assigned the **No Access** model role, the user doesn't display in the list.

In a module that uses the Users list or list subset:

- Workspace administrators can see everyone in the list, and can see the top-level item.
- Nonworkspace administrator that are added to the Users list or list subset can only see themselves, and are unable to see the top-level item.
- Nonworkspace administrator that aren't added to the Users list or list subset are unable to see themselves or anyone in the list.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fusers-list-f3333ecf-a1cc-43d8-af03-ec65c5cdd428&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>