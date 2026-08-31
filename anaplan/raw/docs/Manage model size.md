---
title: "Manage model size"
source: "https://help.anaplan.com/manage-model-size-b4f86ac2-5059-4977-b051-14f461373bfa"
author:
published:
created: 2026-05-13
description: "When you build a model, to ensure efficiency, it's important that you consider the model's size."
tags:
  - "clippings"
---
[Model settings](https://help.anaplan.com/model-settings-800dd9b8-6b08-46bf-95c6-9ea6a266ca63 "Model settings")

When you build a model, to ensure efficiency, it's important that you consider the model's size.

**Note:** Calculating a model's size is not an exact science. It depends on many factors including the object types, line item formats, and the number of dimensions and list items.

| **Object** | **Amount (Bytes)** |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Empty** | **1 char** | **60 char** | **1 million char** |
| Item name (e.g. list name) |  | 500 | 500 |  |
| Item code (e.g. list code) | 0 | 0 | 0 |  |
| No data formatted line item cell | 0 |  |  |  |
| Number formatted line item cell | 8 | 8 | 8 |  |
| Text formatted line item cell | 8 | 8 | 8 | 8 |
| Time period formatted line item cell | 4 | 4 | 4 |  |
| Date formatted line item cell | 4 | 4 | 4 |  |
| Boolean formatted line item cell | 1 | 1 | 1 |  |
| List formatted line item cell | 4 | 4 | 4 |  |

[Line item subsets](https://help.anaplan.com/fd6bfccc-fd3b-4d55-b838-59cdda9c572c) contain line items from the same or different modules in a model. If you want to manage the size of your model, use line item subsets to avoid line item duplication in other modules. To avoid further duplication, you can also use the [COLLECT](https://help.anaplan.com/887a0bce-034b-4a0b-9e5f-262ec2f47e35) function to pull values into a target module from a source module.

Additionally, it's best practice to set your line item's [summary method](https://help.anaplan.com/32821c05-3e6c-4b36-b04e-2fb840418936) to **None**, and only use another summary method when you need it. This approach ensures that aggregated cells are only calculated when you require them.

You can also incorporate [numbered lists](https://help.anaplan.com/371af0ef-1465-4c4f-9a73-4150f4a6ee95) to increase model efficiency. Use numbered lists to manage duplicate names in a model, avoiding empty cells.

It's also important to consider the number of dimensions in your model. For example, if a module contains more than five dimensions, you should split the module in two.

You can view the size of your module in the **Cell Count** column in **Modules**.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmanage-model-size-b4f86ac2-5059-4977-b051-14f461373bfa&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>