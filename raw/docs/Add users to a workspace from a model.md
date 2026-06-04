---
title: "Add users to a workspace from a model"
source: "https://help.anaplan.com/add-users-to-a-workspace-from-a-model-37eebabd-4fb5-4b4e-9198-a43c8e2afbca"
author:
published:
created: 2026-05-13
description: "Workspace administrators can add users to a workspace to enable them to view and edit model data."
tags:
  - "clippings"
---
Workspace administrators can add users to a workspace to enable them to view and edit model data.

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

Workspace administrators can add new users to a workspace. Learn how to [import a list of users](http://help.anaplan.com/anapedia/default.htm#cshid=1035) or [provision user access](https://help.anaplan.com/1ec79e9c-2927-4f30-9c2f-9c062352933c) from the **Administration** console.

When you add a user to a workspace from within a model you determine their [level of model access](https://help.anaplan.com/44fec486-243d-4980-b7ae-60c7ab84f4c9) for that model.

However, when you add a user to a workspace from a model, you add them to all models in that workspace.

Workspace administrators have **Full Access** to the other models by default, even if you select the **No Access** role for them in the current model. Other users have **No Access** to other models by default, regardless of which role you select for the current model.

To change the workspace access for the user, go into each model individually and change their [model role](https://help.anaplan.com/30783e17-b789-4005-b87a-ff15cd3c9044).

When you add a new user to a workspace from a model, an email notification tells them the workspace to which they've been added. The email contains a link to the workspace so they can log in.

To add a user to a workspace from a model:

1. In the model to which you want to add the user, navigate to the **Users** tab of the **Users** pane.
2. Select **Add User**.
3. Enter details into the relevant fields:
	- **Email address**

The email address must:

- Follow the standard email address format. For example, name@domain.com
- Contain a maximum of 60 characters.
- Can't start or end with an \_ (underscore) character.

- **First name**
	- **Last name**
5. Optionally, select the workspace administrator checkbox to make them a workspace administrator.
6. Select or deselect the **Authentication with** **Single Sign-On** checkbox. If selected, the user must sign in with single sign-on. If deselected, the user can sign in with their Anaplan username and password, or with single sign-on.
7. Select a **Role** for the user. By default, new users have the Full Access role for the model to which you add them.
8. Select **OK**. The user is added to the workspace and displays in the **Users** list of the model.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fadd-users-to-a-workspace-from-a-model-37eebabd-4fb5-4b4e-9198-a43c8e2afbca&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>