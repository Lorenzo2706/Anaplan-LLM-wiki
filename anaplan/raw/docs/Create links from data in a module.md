---
title: "Create links from data in a module"
source: "https://help.anaplan.com/create-links-from-data-in-a-module-07fc6c3d-5997-444a-9c4b-ac2c8a8052c3"
author:
published:
created: 2026-05-13
description: "Model builders can use formulas to create links from data in modules. For example, if a module contains information about products you sell, you can create links to the online store page for those products."
tags:
  - "clippings"
---
Model builders can use formulas to create links from data in modules. For example, if a module contains information about products you sell, you can create links to the online store page for those products.

[Create any modules](https://help.anaplan.com/686ff444-5356-48d1-9a9c-7cb2544e31d8) or [line items](https://help.anaplan.com/47f768d6-71fd-497f-8f7d-c4e45adfa12b) you might need in **Modules** in the model settings bar, then [format the line item](https://help.anaplan.com/bf3a0391-5c5a-4da2-9445-685a204d3e68) that will contain a link. Make sure the line item has a **Text** - **Link** data type.

For example, if you want to generate a link to the `https://myproducts.com` website, add a formula to the line item that contains the link.

[Type the following formula](https://help.anaplan.com/293fd5d3-7ad6-4c83-84f6-efd85981f265) in the line item you want to use: [`MAKELINK(`](https://help.anaplan.com/0dbc28e2-da61-4b82-95c7-11fe707a06ab)`"Click Here", "http://www.myproducts.com")`

- `"Click Here"` appears in the cell as a clickable link.
- `"http://www.myproducts.com"` is the URL for the link.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcreate-links-from-data-in-a-module-07fc6c3d-5997-444a-9c4b-ac2c8a8052c3&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>