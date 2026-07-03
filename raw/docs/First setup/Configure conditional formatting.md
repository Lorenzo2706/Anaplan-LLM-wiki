---
title: "Configure conditional formatting"
source: "https://help.anaplan.com/configure-conditional-formatting-67aa850e-090b-447a-9c9e-cf4d2826247d"
author:
published:
created: 2026-06-04
description: "Conditional formatting enables you to change the visual style and color of cells with values in defined ranges. Use this feature to highlight important information for your end users."
tags:
  - "clippings"
---
[Conditional formatting](https://help.anaplan.com/conditional-formatting-077b0f84-a07a-47b7-afc3-894792119257 "Conditional formatting")

Conditional formatting enables you to change the visual style and color of cells with values in defined ranges. Use this feature to highlight important information for your end users.

Conditional formatting on a line item persists when you [pivot](https://help.anaplan.com/1dc471a1-7ace-440f-8c3e-d6a430943b3f) it to a different dimension.

**Note:** Conditional formatting can't be used on text-formatted line items with subsidiary views.

To configure conditional formatting:

1. Select a custom view and open conditional formatting.
2. Select values to base your formatting on.
3. Set formatting style and conditions.

When you set your formatting style and conditions, you enter a **Minimum**, **Maximum**, and optionally one or more **Midpoint** values. You can also select a color for each value. As a result, any cells between the entered values are shaded in a gradient with the selected colors.

Cells with values:

- Equal to or lower than the **Minimum** value display in the color you've specified.
- Equal to or higher than the **Maximum** value display in the color you've specified.
- Close to the **Midpoint** values display in the color you've specified.

To select a module for your custom view:

1. Select **Configure grid** on a new worksheet, or **Select view** on an existing worksheet. Alternatively, create and configure a new grid or KPI card.  
	The **Select data source** dialog opens in the **Select primary grid** or **Card configuration panel**, depending on whether you're designing a view for a worksheet or card.
2. Select the **Custom views** tab.
3. Select a module.  
	A toolbar displays in the top-right of the preview, next to any [context selectors](https://help.anaplan.com/c99d08f7-d7ab-464b-bf2e-69d2d367b6ca).

To select values on which to base your formatting:

1. Select the line item to configure conditional formatting.
2. Select **Conditional formatting**.
3. On the grid, select the context selector value, row heading, or column heading containing the line item to apply conditional formatting to.  
	Alternatively, select the line item from the **Line item** dropdown in the **Conditional formatting** panel.
4. In the **Value** dropdown, select the line item that contains the values to base the conditional formatting on.  
	The default is the line item you selected in the grid.

To set formatting style and conditions:

1. In the **Style** dropdown, select the formatting style to apply to your conditional formatting:
	- **Background** fills the background of each formatted cell with a solid color.
		- **Border** adds a colored border to each formatted cell. This makes sure that cell values remain easy to read.
		- **Font** changes the font color of the line item. It overrides any UX changes, grid formatting changes, and any theme-based colors.
		- **Morse** adds a colored dot or dash to the left of the cell's value. The size of the dot or dash depends on the cell value.  
		The **Color Range** bar displays a sample gradient of your current selection. As you select values and colors below, the gradient bar changes to match your selections.
2. Beneath the **Minimum** heading, enter the lowest value for your conditional formatting in the **Enter lowest value...** field. Then select **Select a color** and select a color.
3. Optionally, add **Midpoint (optional)** headings. The first midpoint input field is visible. Select the plus sign to add more midpoints. For each midpoint, enter the value for your conditional formatting in the **Enter a value...** field. Then select **Select a color** and select a color.  
	You can remove midpoint values by selecting the minus sign above the value's color swatch.
4. Beneath the **Maximum** heading, enter the highest value for your conditional formatting in the **Enter highest value...** field. Then select **Select a color** and select a color.
5. Select **Apply**.  
	Conditional formatting applies to your view, based upon your selections.
6. Select **Next**.  
	To make a further change, select **Back** and modify the custom view.
7. Select **Update** to apply your conditional formatting.  
	Your page displays in designer mode with the formatting you've configured.

**Note:** The **Border** or **Morse** conditional formatting styles can result in cell values being truncated if a column isn't wide enough. To [adjust column width](https://help.anaplan.com/7104f33b-e765-49b6-bf8f-f5719f1ab234), select and drag the line between two columns in a column header.