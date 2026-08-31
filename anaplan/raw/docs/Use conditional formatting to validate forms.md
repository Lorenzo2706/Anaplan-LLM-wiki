---
title: "Use conditional formatting to validate forms"
source: "https://help.anaplan.com/use-conditional-formatting-to-validate-forms-c1e90db0-3e96-4c2b-80a2-008a32a6a65f"
author:
published:
created: 2026-06-04
description: "Use conditional formatting to ensure that any data entry errors or omissions are clearly highlighted."
tags:
  - "clippings"
---
To validate data-entry forms:

1. Add a new line item to your module. This acts as an error measure for another data-entry line item. In the example below, *Error Grade* is the error measure.
2. Create a formula to return an error measure value, conditional on the value entered in another line item. In the example below, the formula [`IF ISBLANK`](https://help.anaplan.com/709bc8d0-f645-4a83-b7d9-7cd2476cee12) is entered into the number-formatted *Error Grade* line item. The error measure value is returned in the text-formatted *Grade* line item.
![Error grade line item is highlighted with the formula visible.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/d9225723-28dd-4e4c-b5fd-b0ad341d3c78/8.png)
3. Select **Conditional formatting** from the toolbar.
4. From the dialog box, select the **New Rule** button.
5. Select the line item you want to format, from the dropdown menu.  
	In the example, *Grade* is selected.
6. From the dropdown menu, select the line item that contains the values the color code should be based on.  
	In the example, *Error Grade* is selected.
7. Choose the **Values and colors**. You can:
	- Select a **2-color scale** and set the **Minimum** and **Maximum** values.
		- Select a **3-color scale** and set the **Minimum**, **Mid-point** and **Maximum values**.
8. Select **OK** to apply your conditional formatting rule.

From the example, the cells in the *Grade* line item are colored:

- White, when the value of the cells in *Error Grade* is 0
	- Yellow, when the value of the cells in *Error Grade* is 1
	- Red, when the value of the cells in *Error Grade* is 2
![New conditional formatting rule created](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/feea2bb5-a908-4a0a-807f-ce21b6ee0742/10.png)

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fuse-conditional-formatting-to-validate-forms-c1e90db0-3e96-4c2b-80a2-008a32a6a65f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>