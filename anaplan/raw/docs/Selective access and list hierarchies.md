---
title: "Selective access and list hierarchies"
source: "https://help.anaplan.com/selective-access-and-list-hierarchies-1c6a58c5-b116-40d9-bd0d-e619144b46f6"
author:
published:
created: 2026-05-13
description: "As a workspace administrator, you can enable selective access for a list and assign it to list items. If the list has parents or children, the access you assign can impact other lists or list items in the list hierarchy."
tags:
  - "clippings"
---
[Selective access](https://help.anaplan.com/selective-access-f0dd364d-cd04-429e-b788-15c79d8cf698 "Selective access")

As a workspace administrator, you can enable selective access for a list and assign it to list items. If the list has parents or children, the access you assign can impact other lists or list items in the list hierarchy.

When enabling selective access, the rules below apply:

| **Event** | **Child List** | **Parent List** |
| --- | --- | --- |
| Enable selective access | Selective access is enabled on all parent lists of the list. | If the parent has child lists, the child list items inherit their selective access from the parent list.  Enable selective access on child lists if more granular access control is required. |

When assigning selective access or removing it from a child or parent list, the rules below apply:

| **Event** | **Child List** | **Parent List** |
| --- | --- | --- |
| Assign selective access  See the [Selective access example](https://help.anaplan.com/337bef27-c1c9-4678-9fa1-d35f61061db6). | Assigning selective access to a child list or its list items, the parent doesn't automatically receive the same level of access. | Child lists receive the same level of access. If the child list's access is:  - Equal to or more restrictive than the access to the parent list, the access only displays in the **Read** and **Write** columns of the parent list. - Greater than the parent list, this access displays against the child list or list item. |
| Remove selective access |  | Any child lists where access was equal to or more restrictive than the parent's has its access removed. |
| Remove list items from a parent with selective access |  | The child's list items become orphaned and lose the parent's access settings.  To maintain the parent's access, either:  - Assign access to the orphan list items. - Import a parent, and apply the access to it.  Orphan list items can result from a data import or manually deselecting the parent. |

These rules also apply to other levels in a parent hierarchy. Take this example:

- Regions is the parent to Countries.
- Countries is the parent to Employees*.*

If you grant read access to the EMEA region, you grant read access not only to its child items (for example, UK and France) but also to all UK and France employees.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fselective-access-and-list-hierarchies-1c6a58c5-b116-40d9-bd0d-e619144b46f6&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>