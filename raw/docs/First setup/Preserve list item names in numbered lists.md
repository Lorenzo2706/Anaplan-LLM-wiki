---
title: "Preserve list item names in numbered lists"
source: "https://help.anaplan.com/preserve-list-item-names-in-numbered-lists-23c8c165-4d3a-4875-9b74-97e24b4df042"
author:
published:
created: 2026-05-13
description: "When model builders convert lists to numbered lists, existing list items change to numbers. If you preserve list item names before a conversion, you can use them to create display names in a numbered list."
tags:
  - "clippings"
---
[Numbered lists](https://help.anaplan.com/numbered-lists-371af0ef-1465-4c4f-9a73-4150f4a6ee95 "Numbered lists")

When model builders convert lists to numbered lists, existing list items change to numbers. If you preserve list item names before a conversion, you can use them to create display names in a numbered list.

[Create any lists](https://help.anaplan.com/d16ed36a-0836-44f7-9db5-e7f0477a9213) or [display names](https://help.anaplan.com/a916143c-d348-4e0c-afaf-100198dcd2ef) you might need in **General Lists** in the model settings bar.

Use formulas to preserve list item names.

To add a formula to a list property:

1. Select **General Lists** in the model settings bar.
2. Select a list, then select **Open**.
3. Select **Properties**.
4. Type `NAME(ITEM(Listname))` in the **Formula** column of your display name list property.**Note**:`List name` is the name of the list that contains the names you want to preserve. The ITEM function identifies the list item, and the NAME function converts the list item to text. Learn more in [NAME](https://help.anaplan.com/bb3d44df-6980-4266-b9f8-42b053e7826d).
5. Ensure that the existing list item names appear in the **Display name** column in **Grid View**.
6. Remove the formula.

Next, [convert your list to a numbered list](https://help.anaplan.com/9559a607-7944-4d80-af0d-14503538cdfb).

After you convert your list to a numbered list, you must define its list property in **General Lists** in the model settings bar. This ensures that your display names appear for each list item.

To define the display name list property for a numbered list:

1. Select **General Lists** in the model settings bar.
2. Select a list, then select your list property in the **Display Name Property** column.

Your list now displays numbered list items as their original names. If you [add list items to your numbered list](https://help.anaplan.com/ca13a66c-6233-48fe-be64-95c69de5192a) after the conversion, each list item displays as a number.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpreserve-list-item-names-in-numbered-lists-23c8c165-4d3a-4875-9b74-97e24b4df042&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>