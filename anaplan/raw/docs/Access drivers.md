---
title: "Access drivers"
source: "https://help.anaplan.com/access-drivers-49b4b687-ded5-4c80-8509-777906bc98bc"
author:
published:
created: 2026-05-13
description: "Workspace administrators can set up access drivers to control read and write access to cell data."
tags:
  - "clippings"
---
Workspace administrators can set up access drivers to control read and write access to cell data.

Use access drivers to implement [Dynamic Cell Access](https://help.anaplan.com/55ae93e6-5139-4bbf-93f9-c8cb06f68f75).

You can control any line item in your model with an access driver. You can also include the [*Users* list](https://help.anaplan.com/f3333ecf-a1cc-43d8-af03-ec65c5cdd428) in an access driver.

Depending on the granularity of access you need, apply the access drivers to target cell data at line item or module level. Then, you can control access to the data defined by the access drivers either manually, or through simple formulas. For example, use a Time function to make cell values in the **Current Period** editable.

You can use Dynamic Cell Access with [**Selective Access**](https://help.anaplan.com/f0dd364d-cd04-429e-b788-15c79d8cf698). Selective Access restricts access to lists and list items by user, but not to cell data. If both mechanisms are used together, the most restrictive level of access applies. For example, use Selective Access to restrict access driver modules to workspace administrators only.

Apply access drivers to target cell data in the **Read Access Driver** and **Write Access Driver** columns in **Blueprint** . These columns determine whether cell data is read-only, editable, or hidden.

When you apply an access driver to a line item or to a module, control access to the target cell data by selecting the checkboxes for combinations of dimensions. You can automate this process with line item [formulas](https://help.anaplan.com/e1cc95b4-915d-435b-98cc-d34fbf2ab032).

Changes to access drivers are recorded in the [change history](https://help.anaplan.com/6d96706b-61cc-4b15-84a6-00c9f8a15cc2) of a model as **Security Changes**.

You can use an access driver module with no dimensions as a global access driver. Use global access drivers to control access to cell data regardless of the dimensionality of the target module or line item.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Faccess-drivers-49b4b687-ded5-4c80-8509-777906bc98bc&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>