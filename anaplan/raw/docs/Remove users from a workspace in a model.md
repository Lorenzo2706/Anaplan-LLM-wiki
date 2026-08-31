---
title: "Remove users from a workspace in a model"
source: "https://help.anaplan.com/remove-users-from-a-workspace-in-a-model-946d76eb-9b81-4340-8abf-0107f741a3d6"
author:
published:
created: 2026-05-13
description: "You can remove a user or users from a workspace when you no longer want them to have access to any models or data in that workspace."
tags:
  - "clippings"
---
You can remove a user or users from a workspace when you no longer want them to have access to any models or data in that workspace.

You can manage user access to workspaces in three ways:

- A user administrator can create users, add them to workspaces, or delete them from workspaces in **Administration**.
- A workspace administrator can add or remove users from the **Users** pane in a model.
- A workspace administrator can import a list of users to add users and update user details in a model.
- A workspace administrator can create a shorter users list subset from the larger **Users** lists in **General lists**, which can also be used to control user access within a model.

If a user administrator and workspace administrator input user changes that conflict, the most recent transaction determines the user account status.

To avoid user status conflicts, we recommend that your organization use the User Administrator role to add or remove users. Workspace administrators can then refine model-level access from the **Users** pane in a model.

**Note**: If a tenant administrator turns on the [user management switch in **Administration**](https://help.anaplan.com/522db396-572f-4375-83d4-4284ee6fc427):

- Only user administrators can add or remove users from the **Internal** page in **Administration**. They can also invite or remove visiting users from the **Visiting** page in **Administration**.
- Workspace administrators can't add or remove users from within models. They also can't add users through an import. However, they can run an import to update user attributes.

This procedure is for when you want to remove users from a workspace when you're in a model. Learn how to [manage user access](https://help.anaplan.com/1ec79e9c-2927-4f30-9c2f-9c062352933c), as a user administrator, from the **Administration** console.

It’s quicker to delete several users at the same time than to delete each separately. You can delete up to 250 users at a time.

You must be in a model within the workspace from which you want to delete the user or users.

**Note:** If you delete users from any model in the workspace, they’re removed from all models in that workspace. If you only want to remove a user’s access to a specific model in a workspace, change their model [role](https://help.anaplan.com/anapedia/Content/Modeling/Users/Roles.html#CSHID=1189) instead.

Before you launch the **Delete from Users** wizard, select the users you want to remove from the workplace. If you do not select any users, the first user in the list is automatically selected.

| **If you want to select:** | **then:** |
| --- | --- |
| a single user | select any cell in the row that contains that user. |
| all users | click the top-left corner of the grid.  **Note:** you cannot delete yourself, so your user is not selected for deletion in the wizard. |
| multiple users in adjacent rows of the grid | 1. Press and hold the Shift key. 2. Select anywhere in the row for the first user you want to select. 3. Select anywhere in the row for the last user you want to select. 4. Release the Shift key.   	All the users between the first user you clicked and the last user you clicked are selected.  If you want to change your selection:  1. Press and hold the Shift key. 2. Select anywhere in the row for the user you want to be at the new outer edge of the selection. 3. Release the Shift key.   	The limit of the selection changes to the row of the user you selected in step 2. |
| multiple users that are not adjacent in the grid | 1. Press and hold the Command key (on a Mac) or the Control key (on a PC). 2. Select the header for each row (the user’s email address) for each user you want to select. 3. Release the Command or Control key.   	All the users for each row you clicked are selected.  If you want to change your row selection:  1. Press and hold the Command key (on a Mac) or the Control key (on a PC). 2. Click anywhere in the row of any additional users you want to include in the selection. 3. Click anywhere in the row of currently selected users that you want to deselect. 4. Release the Command or Control key. |

To delete the selected user or users from your workspace:

1. In the **Users** pane of the model, click **Delete users** in the toolbar.  
	The **Delete from Users** wizard displays.  
	The list of users to keep displays on the left under **Click to make a selection**.  
	The users to delete display on the right under **Items to delete**.  
	Your user displays under **Click to make a selection**, but you cannot select your user for deletion.
2. Optionally, amend your selection of users to delete:
	- Select users under **Click to make a selection** to move them to the **Items to delete** column.
		- Click **Keep** to the right of any users selected for deletion to remove them from the **Items to delete** column.
		- Click **Delete All >>** to move all users except yourself to the **Items to delete** column.
		- Click **<< Keep All** to remove all users from the **Items to delete** column.
3. Click **OK** when you're happy with your selection of users to delete.
4. Click **OK** in the confirmation dialog to confirm the deletion, or **Cancel** to return to the wizard.  
	A message displays the progress of your deletion. When this completes, your results display.

There are three possible results:

| **Result** | **Message** |
| --- | --- |
| Success | The number of users deleted displays. |
| Partial Success | The number of users deleted displays.  A list of the users not deleted also displays, so you can try again. |
| Unsuccessful | A confirmation that no users were deleted displays.  A list of the users not deleted displays, so you can try again. |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fremove-users-from-a-workspace-in-a-model-946d76eb-9b81-4340-8abf-0107f741a3d6&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>