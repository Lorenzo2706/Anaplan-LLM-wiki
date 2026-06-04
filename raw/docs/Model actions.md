---
title: "Model actions"
source: "https://help.anaplan.com/model-actions-69250a43-3266-4c04-bda9-bfb50ece9623"
author:
published:
created: 2026-05-13
description: "Workspace administrators can create model actions that enable you to repeat and automate routine tasks. Where actions can be run by non-workspace administrators, you can publish them to dashboards in models. You can also publish imports, exports, and processes to pages in the User Experience."
tags:
  - "clippings"
---
Workspace administrators can create model actions that enable you to repeat and automate routine tasks. Where actions can be run by non-workspace administrators, you can publish them to dashboards in models. You can also publish imports, exports, and processes to pages in the User Experience.

You can [publish actions to dashboard](https://help.anaplan.com/1e633acd-83eb-44f3-931c-ae89aecf81da) as a button, to better integrate with your workflow.

Some actions can be combined to form a sequential [process](https://help.anaplan.com/c01dd9ae-2390-4623-87bd-60b208a84f23).

You can also use integrations, such as [Anaplan Connect](https://help.anaplan.com/e3a9f00c-3924-4cfb-aed0-1ec14233821b), to schedule actions and processes.

You must be a workspace administrator to set up an action. All model actions, except imports and exports, are set up in the **Actions** pane, from the **New Action** menu.

Workspace administrators can also create imports and exports. When you set up an import or export, it's saved as an action in the **Actions** pane. This enables the [import or export action](https://help.anaplan.com/b945e7f1-71c8-42ce-82ec-0987edd28bea) to be repeated.

To help users identify an action, apply best practice [name conventions](https://help.anaplan.com/aeb0b95e-f7a3-4fe5-81c7-aec9a12f80be) when setting up the action. If the action takes users from one dashboard to another, it's helpful to include the source and the destination location in the name.

**Note:** Some actions must be [published to a dashboard](https://help.anaplan.com/1e633acd-83eb-44f3-931c-ae89aecf81da) before you can run them. Others can also be configured to open another dashboard when run. It's helpful to create any dashboards you need before you set up the action.

Workspace administrators can run model actions from the **Actions** pane, except for those that need to be published to a dashboard.

When an action is running, the last action duration doesn’t reset to zero or continually update. It displays the duration of the previous run until the action completes.

If you're not a workspace administrator, you can run model actions published to a dashboard or [added to a page](https://help.anaplan.com/878d48f4-1d5d-4014-a33c-3220f15a1d4f) in the User Experience.

To enable users to run actions in a specified order, create a process and [add model actions to the process](https://help.anaplan.com/e2caf934-9923-48f7-84ed-e52ff77ece64).

You can then [publish the process to a dashboard](https://help.anaplan.com/cd348496-8fdb-479b-b2f4-7c1aa5e67146) or add it to an [action card](https://help.anaplan.com/fd2c16d5-5a5c-4aab-8935-d976a9908b4e) in the User Experience. This enables the process to be run by non-workspace administrators.

Workspace administrators can also [run processes](https://help.anaplan.com/ad71ca5c-00d5-4acf-86d4-483df419cb40) from the **Actions** pane like other actions.

**Note:** The most **Recent Action** is the most recent complete action. Any canceled action isn't counted as a recent action.

When you create actions, it's useful to think about who you want to run them and on what parts of Anaplan they can access. For example, users who aren't workspace administrators can only access dashboards in a model, but you might prefer to keep their workflow in the [User Experience](https://help.anaplan.com/fed5bb63-0592-4402-b290-e708f500f14f).

Page builders can add imports and exports directly to [action cards](https://help.anaplan.com/fd2c16d5-5a5c-4aab-8935-d976a9908b4e) in the User Experience, along with various [page actions](https://help.anaplan.com/2e2385ee-409d-4d69-92a0-450fe4ab08e9). Other actions can be run in the User Experience, but you must add them to a process first.

This table displays the model actions that you can add to processes, and those that you must be a workspace administrator to run.

| **Action** | **Can be added to a process** | **For workspace administrators only** |
| --- | --- | --- |
| [Imports and exports](https://help.anaplan.com/b945e7f1-71c8-42ce-82ec-0987edd28bea) | Yes | If the default file is set to **Admins Only**. |
| [Delete from list using selection](https://help.anaplan.com/04b746ca-cc8f-4f12-bd1e-da9bbd2b3fa5) | Yes | No |
| [Order list](https://help.anaplan.com/22a2640b-8e60-4732-9d7b-10660c463023) | Yes | No |
| [Open dashboard](https://help.anaplan.com/8a5210a5-5676-4ef9-8e60-284425617d24) | No | No |
| [Create](https://help.anaplan.com/3cda6b84-708f-40c5-996d-631eb70d6134) | No | No |
| [Delete branch](https://help.anaplan.com/5ad85b31-fa3b-4412-9970-68ddc73dc371) | No | No |
| [Assign and Assign only](https://help.anaplan.com/4b6861d6-7587-4eb7-85f9-262cbfec4de3) | No | No |
| [Update current period](https://help.anaplan.com/e94034cd-8004-479f-8c1a-655a296398f0) | Yes | Yes |
| [Copy branch](https://help.anaplan.com/12aca940-6143-4231-bb7d-bc1639b8375e) | No | No |
| [Optimizer](https://help.anaplan.com/e8eac6ea-bfac-43a1-abbb-3dad60cea523) | Yes | No |
| [Bulk copy](https://help.anaplan.com/46ae3b0c-ce5c-4313-a765-fb22ddd62da1) | Yes | Yes, unless enabled for all users. |

**Note:** To use Optimizer actions you must have an Enterprise subscription, and Optimizer must be enabled in your tenant. You can only run Optimizer as part of a process. Optimizer is not available in Polaris.

Actions help you keep order in your model, and so do [numbered lists](https://help.anaplan.com/371af0ef-1465-4c4f-9a73-4150f4a6ee95). You can manage and maintain [numbered lists](https://help.anaplan.com/371af0ef-1465-4c4f-9a73-4150f4a6ee95) with Create, Assign and Assign only, Copy branch, or Delete branch actions.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmodel-actions-69250a43-3266-4c04-bda9-bfb50ece9623&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>