---
title: "Add formulas to list properties"
source: "https://help.anaplan.com/add-formulas-to-list-properties-8130ef62-1a04-4325-80e3-9b657e6acf8d"
author:
published:
created: 2026-05-13
description: "Model builders add formulas to list properties to pull data from modules or line items into lists."
tags:
  - "clippings"
---
[General lists](https://help.anaplan.com/general-lists-403a1ed1-ad7b-4ab3-b40c-61dd9d651075 "General lists")

Model builders add formulas to list properties to pull data from modules or line items into lists.

[Create any lists](https://help.anaplan.com/d16ed36a-0836-44f7-9db5-e7f0477a9213) or [list properties](https://help.anaplan.com/da73f852-e39f-4046-bf97-675274ce0947) you might need in **General Lists** in the model settings bar.

For example, if you want to [create display names for a numbered list](https://help.anaplan.com/a916143c-d348-4e0c-afaf-100198dcd2ef), set up a formula that pulls employee names into the **Display name** list property.

| **List property** | **Format** | **Formula** |
| --- | --- | --- |
| Display name | Text | `'SYS08 Employee Details'.Name` |

Another example shows how you can use a list property formula to [preserve list item names](https://help.anaplan.com/23c8c165-4d3a-4875-9b74-97e24b4df042) before you [convert a list to a numbered list](https://help.anaplan.com/9559a607-7944-4d80-af0d-14503538cdfb).

| **List property** | **Format** | **Formula** |
| --- | --- | --- |
| Display name | Text | `NAME(ITEM(Listname))` |

To add a formula to a list property:

1. Select **General Lists** in the model settings bar.
2. Select a list, then select **Open**.
3. Select **Properties**.
4. Type the formula in the list property's **Formula** column.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fadd-formulas-to-list-properties-8130ef62-1a04-4325-80e3-9b657e6acf8d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>