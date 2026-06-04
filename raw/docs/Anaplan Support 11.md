---
title: "Anaplan Support"
source: "https://support.anaplan.com/formulas-eccb1b4a-e2a1-499e-b189-52d81b8a35f5"
author:
published:
created: 2026-05-04
description: "Best practices in creating performant formulas in Polaris."
tags:
  - "clippings"
---
[Polaris](https://support.anaplan.com/polaris-c265a8ac-e457-46a7-b307-1fe62ffa4730 "Polaris")

Polaris achieves calculation efficiency by minimizing the number of cells that the engine has to do work for. Some formulas can be calculated very efficiently by only doing work for 'populated' cells. The Calculation Complexity column will tell the modeler how the engine is interpreting a formula and how much work will be required for each populated source cell.

There are three types of Calculation Complexity: One-to-One, One-to-Many, and All Cells.

**One-to-One**

This is the most efficient type of formula. ‌A One-to-One formula is a formula where the engine can ‘drive’ the calculation by only iterating over the populated cells in one or more of the source line items. In the example of “Revenue = Units \* Price”, it's possible to drive this calculation in several ways:

- You could calculate every target cell in Revenue.
- You could multiply each non-zero value in Units to get the result, since the formula is a straight multiplication and anything multiplied by zero is zero.
- You could also do a multiplication of every item in Price, but this would be less efficient.
![One-to-One](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/7f243cf8-a885-4d27-b283-aa89309b2773/One%20to%20One.png)

In this case, the Polaris engine chooses the most efficient way to calculate the result. It takes only three real calculations instead of 15. This is key to efficiently calculating at high dimensionality.

**One-to-Many**

One-to-Many formulas require a multiple of work for every populated source cell. This is displayed in the Calculation Complexity column as One-to-Many(x) where x is the 'Fan-out factor' or the number of calculations that has to be done for every source cell.  
  
Having a formula with One-To-Many(x) can be a sign that data is being spread out over a dimension.

![One-to-Many](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/9c59b15d-7cc4-4cf8-a69f-f8e24bede793/Fan-Out.png)

The formula for Units Months= QuarterValue(Units Quarters)

In this example, a simple reference between two line items where the target has a finer granularity than the source will have a Calculation Complexity of One-to-Many(3). ‌Note that not all cells are having to be calculated (or populated) here, but a multiple of the number of source cells are having work done.

**All Cells**

All Cells is the least efficient when modeling with significant dimensionality. ‌This is the simplest to explain, in that the only mathematically valid way for Polaris to calculate the result of the formula is to do a calculation for every target cell. This is ‌how Classic calculates line items in almost all cases. This becomes very inefficient with significant dimensionality due to the sheer number of cells.

![All Cells](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/35a26277-bc27-4c2b-a1c7-bf0ac262a6f9/All%20Cells.png)

The formula for Units Total = Units + 1

Having a large Fan-Out in the Complexity Column can lead to performance issues with line items with significant dimensionality.

Having All Cells in the Complexity Column can lead to performance issues with line items having significant dimensionality.

Unlike Classic, using Booleans instead of Number format isn't a big benefit because Boolean are about the same size as other formats.

In general, Polaris will interpret the meaning of the formula and attempt to identify the most efficient way to drive the calculation. The order of cases in an IF clause doesn't matter. For example, **IF X THEN Y ELSE Z** is exactly equivalent to **IF NOT X THEN Z ELSE Y**.

Polaris only uses memory when storing populated (non-default) values. This is why it's important to ensure that the logic of a model maintains default values (blank, false, and zero) as often as possible. For example, if the common scenario is for a value to be TRUE, consider reversing the logic and making the common result FALSE which is the default value.

Using constants and item(list) will create a 100% dense module as every cell will be populated.

A few functions are inherently computationally intensive. Used in significant dimensionality, they can be very slow to calculate. Examples of these are:

- ISFIRSTOCCURRENCE()
	- RANK()
	- CUMULATE()

While SUM/LOOKUP combination should be avoided in Classic, it's paramount to avoid using it in Polaris. ‌The net result of a SUM and LOOKUP in the same formula is that the engine has to do a very large number of calculations for every target cell in a line item. Although the logic will take up a smaller amount of space, it's MUCH more efficient to split the LOOKUP into a different line item and then do the SUMs separately.

LOOKUPs in Polaris are computationally quite intensive, especially with significant dimensionality. The engine must iterate over every item in the dimension being LOOKED UP over. Consider making LOOKUPs their own line item. This might make the system work better by reducing how many times a LOOKUP needs to be calculated.

Back to top