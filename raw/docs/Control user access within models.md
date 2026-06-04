---
title: "Control user access within models"
source: "https://help.anaplan.com/control-user-access-within-models-8c495688-216e-49c4-aa56-a4b70487e5d7"
author:
published:
created: 2026-05-13
description: "Workspace administrators can control access to features of a model via the Users pane and model Contents."
tags:
  - "clippings"
---
Workspace administrators can control access to features of a model via the **Users** pane and model **Contents**.

You can control user access at the tenant, workspace, and model level.

From **Administration**, tenant administrators assign administration roles. Users with administration roles can control access within a tenant.

You can control access to a workspace both from **Administration** and within a model. User administrators [provision user access to a workspace](https://help.anaplan.com/1ec79e9c-2927-4f30-9c2f-9c062352933c) from **Administration.** Workspace administrators [add users within a model](https://help.anaplan.com/37eebabd-4fb5-4b4e-9198-a43c8e2afbca) and control access to model content. Workspace administrators can also [create Users list subsets](https://help.anaplan.com/e8469111-0e83-4c36-87b3-3a1dfe563eb9), which can also control user access within models.

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

In a model, you're either a workspace administrator or a user.

Some model features are only available to workspace administrators, and they control the [level of access](https://help.anaplan.com/44fec486-243d-4980-b7ae-60c7ab84f4c9) for other users. Workspace administrators can:

- Add or remove users in a workspace
- Assign access to other features of the model via model roles, selective access, and model contents
- Designate other workspace administrators
- Control exceptions to single sign-on for users
- Import or export a file containing user account data

Most user access in models is defined by model roles. These enable you to manage ‌access for users who perform the same business function and share common data access needs. You can also set landing dashboards and the order of model **Contents**, so users view the most relevant data first.

As you plan how to control access to your model, follow a process flow:

1. Create model roles that align with business functions that share common data needs.
2. Assign module, version, list, and action permissions to your model roles.
3. Specify a landing dashboard for each model role.
4. Select the content to display in the **Contents** panel.

When you need to apply more specific controls, you can use selective access to limit access to lists and list items for each user.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcontrol-user-access-within-models-8c495688-216e-49c4-aa56-a4b70487e5d7&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>