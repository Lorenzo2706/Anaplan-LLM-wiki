---
title: "Manage images in a central module"
source: "https://help.anaplan.com/manage-images-in-a-central-module-531cb70a-bd02-44e3-ab42-dad9188107cc"
author:
published:
created: 2026-05-13
description: "If you centralize your image URLs in one module, you can reference the same cell in all other modules that use the URL and anywhere the image displays. This ensures any change to an image updates consistently across your model and apps."
tags:
  - "clippings"
---
[Line items](https://help.anaplan.com/line-items-52d76cdd-2571-4400-8f34-b15dd5651b9f "Line items")

If you centralize your image URLs in one module, you can reference the same cell in all other modules that use the URL and anywhere the image displays. This ensures any change to an image updates consistently across your model and apps.

You can store URLs either as a line item or list item property with the format **Text** and the type **Link**.

If you manage [your image URLs](https://help.anaplan.com/3f9d38bc-faf7-47fe-a78f-861092fde283) in a central image module, this enables you to:

- Store data that relates to the image alongside the image (for example, store product information with your product images)
- Trace use of the image URL through the model app, via the [line item](https://help.anaplan.com/52d76cdd-2571-4400-8f34-b15dd5651b9f)
- [Filter](https://help.anaplan.com/5c7d1754-29cf-4861-a369-69c8fe0c31a1) on the image URL in the module
- Use [summary methods](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) on image URLs
- Use image URLs in [formulas](https://help.anaplan.com/293fd5d3-7ad6-4c83-84f6-efd85981f265)

Consider how you want to use the image and image data in your model as you design your image module.

To display the image on a dashboard, board, or worksheet, you must have a line item that contains the URL. However, you can store the URL in a list-item property and enter a formula in the line item that references the property. Format the line item as **Text** with type **Link**.

Suppose you have a list, *ProductImageURLs*, with a property, *ImageURL*, that stores the image URLs within a module.

You can create a reference module *Retail Products*, with *ProductImageURLs* on rows, and line items on columns. The line items can contain additional information about each product in the list. You can then format the line item *Image* as **Text** with the type **Link** and add a formula that references the list-item property *ProductImageURLs.ImageURL*.

![A module, Retail Products, with product ID numbers on rows and product details on columns. The Image column is selected and contains image URLs.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/b57c396f-2cc5-482f-801d-dca5084fef4d/ProductModule.png)

When you publish the module grid to a dashboard, you can add an image placeholder and link it to the *Image* line item. When you select each product in the grid, the placeholder updates to display the image hosted at that URL. This enables you to identify the product.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmanage-images-in-a-central-module-531cb70a-bd02-44e3-ab42-dad9188107cc&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>