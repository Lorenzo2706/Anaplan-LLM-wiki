---
title: "Selective access example"
source: "https://help.anaplan.com/selective-access-example-337bef27-c1c9-4678-9fa1-d35f61061db6"
author:
published:
created: 2026-05-13
description: "This example shows how a workspace administrator can enable and assign selective access in a list with a parent hierarchy."
tags:
  - "clippings"
---
[Selective access](https://help.anaplan.com/selective-access-f0dd364d-cd04-429e-b788-15c79d8cf698 "Selective access")

This example shows how a workspace administrator can enable and assign selective access in a list with a parent hierarchy.

The example below illustrates that when you enable selective access to a child list, you also enable it to the parent of the child list. It also shows how different levels of access interact in a list hierarchy. The example has two stages:

1. Enable and assign access to a child list.
2. Assign access in a parent list.

A Manager, Patrice Planner, needs:

- Write access to data for employees in their country.
- Read access to data for employees in other countries.

Kiran is an employee in the same country as Patrice, France, but Sylvia is an employee in a different country, Canada. Patrice needs:

- Write access for Kiran's data.
- Read access to Sylvia's data.

To assign selective access in this case:

1. Create an *L1 Employees* list that contains at least the items:
	- *Kiran Contributor*
		- *Sylvia Sales*
2. Create the list *L2 Countries* with the items:
	- *France*
		- *Canada*
3. In **General Lists**, set *L2 Countries* as the parent list of *L1 Employees*.
4. In the *L1 Employees* list, select *Canada* as the parent item for *Sylvia Sales* and *France* as the parent item of *Kiran Contributor*.
5. In **General lists**, enable **Selective Access** for *L1 Employees*.  
	This automatically enables selective access for *L2 Countries.*
6. Go to **Users** and assign *Patrice Planner* accessto:
	- *Kiran Contributor* under *L1 Employees Write.*
		- *Sylvia Sales* under *L1 Employees Read*.

| **First name** | **Last Name** | **L1 Employees Write** | **L1 Employees Read** | **L2 Countries Write** | **L2 Countries Read** |
| --- | --- | --- | --- | --- | --- |
| Patrice | Planner | Kiran Contributor | Sylvia Sales |  |  |

Additional employees join the company in both France and Canada, with additional managers.

Patrice needs write access to their direct reports, but they only need read access to employees that report to other managers.

Go to **Users** and assign both *France* and *Canada* to Patrice under *L2 Countries Read*.

| **First name** | **Last Name** | **L1 Employees Write** | **L1 Employees Read** | **L2 Countries Write** | **L2 Countries Read** |
| --- | --- | --- | --- | --- | --- |
| Patrice | Planner | Kiran Contributor |  |  | Canada, France |

*Sylvia Sales* no longer displays in the *L1 Employees Read* column, as the read permission for the parent list includes access to this list item. *Kiran Contributor* still displays in the *L1 Employees Write* column, as the write access overrules the read access to *France*.

Any module that includes the *L1 Employees* list as a dimension, displays both *France* and *Canada* for Patrice as summaries, and the individual employees continue to display as list items. However, ‌individual employees can only edit data for *Kiran Contributor*.

If a module includes the *L1 Employees* list as a dimension, it displays *France* and *Canada* for Patrice as summaries and the individual employees as list items. However, individual employees can only edit data for *Kiran Contributor*.

Suppose the business no longer wants managers to have read access to data for employees outside their management chain. You can remove read access to Canada and France. Patrice still has access to *Kiran Contributor,* as this is a higher level of access, but no longer has read access to *Sylvia Sales* or employees in any other teams.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fselective-access-example-337bef27-c1c9-4678-9fa1-d35f61061db6&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>