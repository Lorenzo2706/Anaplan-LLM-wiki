---
title: "Subsidiary views"
source: "https://help.anaplan.com/subsidiary-views-b208ed3b-c958-4a55-94db-c297bc7c95cb"
author:
published:
created: 2026-05-13
description: "If you change the dimensionality of a line item, a subsidiary view is automatically created. You can do this by changing a line item's dimensions in the Applies To, Time Scale, Time Range, and Versions columns in a module's Blueprint. Subsidiary views increase a model's efficiency by reducing the number of cells in line items."
tags:
  - "clippings"
---
[Saved views](https://help.anaplan.com/saved-views-81a92257-5ed0-429a-b4e8-fbde8c05a3fc "Saved views")

If you change the dimensionality of a line item, a subsidiary view is automatically created. You can do this by changing a line item's dimensions in the **Applies To**, **Time Scale**, **Time Range**, and **Versions** columns in a module's Blueprint. Subsidiary views increase a model's efficiency by reducing the number of cells in line items.

The dimensionality of a subsidiary view can vary by any [list](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075), [Time](https://help.anaplan.com/53836b0c-1238-48ef-834a-8728b24f3d8e), or [version](https://help.anaplan.com/19b4391f-5257-40ee-8dfb-36f0ab426c8f) in a model.

Consider a subsidiary view if:

- A line item has the same result across all or many dimensions. Any dependencies or references to this line item are unaffected.
- A line item does not need to be visible to end users.

It's a good idea to create multiple modules if you want to simplify your processes. A subsidiary view can only display one line item, so it might be difficult to understand a module if it contains more than one subsidiary view.

If an end user needs to view a line item on a [dashboard](https://help.anaplan.com/f95d9d39-5ece-46a2-9cc3-2e76563b8fb2), it's best practice to [create another module](https://help.anaplan.com/686ff444-5356-48d1-9a9c-7cb2544e31d8), as opposed to a subsidiary view.

This is because:

- You can't edit subsidiary views if you [publish selected line items to a dashboard](https://help.anaplan.com/701c866f-ddd0-4434-84ef-f739d339be7b).
- The space occupied by subsidiary views on a dashboard can cause issues when you align dashboard elements.
- When you publish a subsidiary view to a dashboard, you can only hide the module name if you hide the line item.
- You can't publish multiple subsidiary views with the same [dimensions](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a) as another subsidiary view.
- You can only apply filters to a subsidiary view using its own data. You can't base the filter on another line item.

The examples demonstrate the situations in which you might want to publish subsidiary views to dashboards. In both examples, the module must display in its default dimensionality.

If the [list](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075) is positioned on rows or columns, you can edit the line item in the list's parent list item instead of the child item.

This happens when a [list subset](https://help.anaplan.com/589d9f5d-f439-40a4-905f-5027c2dc9c21) is used as a dimension of a subsidiary view, and the full list is used in the default dimensionality. When the [page selector](https://help.anaplan.com/1511eecc-add8-4fec-b95e-685cd6bcb0df) being viewed exists in the list subset, the data in the cells can be viewed by end users. When the page being viewed isn't part of the list subset, the cells are blank.

The **Start of Section** option in **Blueprint** changes the dimensionality of all line items that follow a selected line item, without creating a subsidiary view.You shouldn't reorder line items, as this significantly affects a module's dimensionality.

If you select a list in **Applies To,** and then select **Start of Section**, any following line items that don't have any lists take their dimensionality from the list specified. You can repeat this process for all line items.

Use **Start of Section** where a change in dimensionality reflects a subset of the default dimension. For example, say you're preparing an *Income Statement* that refers to the *Profit Centers* list, which is a subset of the *Organization* list. If you use **Start of Section**, you can change the dimensionality from *Organization* to *Profit Centers* without creating a subsidiary view for each line item.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fsubsidiary-views-b208ed3b-c958-4a55-94db-c297bc7c95cb&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>