---
title: "Composite hierarchies"
source: "https://help.anaplan.com/composite-hierarchies-cabf4596-28b5-4849-a028-d2e610905b7d"
author:
published:
created: 2026-05-13
description: "Model builders use composite hierarchies to create structure in lists. Composite hierarchies contain multiple lists that each roll up to a parent list."
tags:
  - "clippings"
---
[List hierarchies](https://help.anaplan.com/list-hierarchies-2fc52da8-b161-4d29-acfb-9aafde1b5bae "List hierarchies")

Model builders use composite hierarchies to create structure in lists. Composite hierarchies contain multiple lists that each roll up to a parent list.

For example, the *<<Organization Hierarchy>>* includes the *G1 Region*, *G2 Country*, and *G3 Location* lists.

In **General Lists** in the model settings bar, the **Top Level** column represents the highest level in a hierarchy, and summarizes the data in your list. For example, *Total Company* is the top level for *G1 Region*.

*G3 Location* rolls up to *G2 Country*, and *G2 Country* rolls up to *G1 Region*. Each list's parent hierarchy displays in the **Parent Hierarchy** column.

| **List name** | **Top Level** | **Parent Hierarchy** |
| --- | --- | --- |
| <<Organization Hierarchy>> |  |  |
| G1 Region | Total Company |  |
| G2 Country |  | G1 Region |
| G3 Location |  | G2 Country |

**Note**: You can use lists in other hierarchies for different purposes. For example, the *Employees* list in the *<<Employee Hierarchy>>* rolls up to *G3 Location*.

To create a composite hierarchy:

1. Select **General Lists** in the model settings bar.
2. Select a list, then select **Open**.
3. Select **Configure.**
4. Select a parent list in **Parent Hierarchy**.
5. If necessary, type a name for the top level item in **Top Level Item**.

Alternatively, define the top level item and parent hierarchy in the **Top Level** and **Parent Hierarchy** columns for your list in **General Lists**.

**Note**: You can configure whether a list's top level item is a default page selector in the [User Experience](https://help.anaplan.com/fed5bb63-0592-4402-b290-e708f500f14f). Learn more in [Configure lists](https://help.anaplan.com/4764efd5-3f7c-4537-9202-de21a858cade).

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcomposite-hierarchies-cabf4596-28b5-4849-a028-d2e610905b7d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>