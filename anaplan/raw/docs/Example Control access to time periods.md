---
title: "Example: Control access to time periods"
source: "https://help.anaplan.com/example-control-access-to-time-periods-4bfffe68-dc64-4ec3-836b-685db349a787"
author:
published:
created: 2026-05-13
description: "This example demonstrates how to use dynamic cell access to control read and write access to time periods."
tags:
  - "clippings"
---
This example demonstrates how to use dynamic cell access to control read and write access to time periods.

Before you create an access driver module, create a simple *Products* [list](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075), such as:

**All products**

To control access to time periods:

1. Select **Modules** in the model settings bar.
2. [Create an access driver module](https://help.anaplan.com/16e25678-22af-418b-b599-ba7e53b8269d), and name it *Access drivers - time.*
	1. Position **Time** on columns.
		2. [Insert two line items](https://help.anaplan.com/47f768d6-71fd-497f-8f7d-c4e45adfa12b), *Read* and *Write*. These are the access drivers.
		3. Select **Blueprint** , then change the format of both line items to **Boolean**.
3. Create a target module, and name it *Products over time*.
	1. Position **Time** on columns.
		2. Insert a line item, name it *Data,* and position it on [**Pages**](https://help.anaplan.com/17b0ba75-c9dc-4b68-840f-6f846632a42b).
		3. Position the *Products* list on rows.
		4. Select **Blueprint** , then apply the *Access drivers - time.Read* and *Access drivers - time.Write* access drivers to the **Read Access Driver** and **Write Access Driver** columns, respectively.
		5. In Grid view, enter some numbers.

|  | Jan-22 | Feb-22 | Mar-22 | Apr-22 | May-22 | Jun-22 |
| --- | --- | --- | --- | --- | --- | --- |
| Soft drinks | 10 | 80 | 110 | 80 | 10 | 90 |
| Beer | 60 | 50 | 100 | 40 | 30 | 80 |
| Red wine | 50 | 100 | 90 | 10 | 60 | 10 |
| Rose wine | 50 | 20 | 50 | 40 | 50 | 80 |
| White wine | 70 | 70 | 30 | 80 | 100 | 50 |
| Craft ale | 80 | 50 | 10 | 60 | 30 | 60 |
| Coffee | 90 | 30 | 40 | 70 | 0 | 70 |
| Tea | 100 | 70 | 20 | 30 | 80 | 60 |
| **All products** | **510** | **470** | **450** | **410** | **360** | **500** |

4. For the purposes of this example, [publish both modules to a single dashboard](https://help.anaplan.com/2e008f1e-e3c8-4056-8629-d25465528397), and name it *Product sales data.*
5. Use the access driver checkboxes to dynamically control access to product sales data in the target module, *Products over time*.
	1. For example, select both **Read** and **Write** for March 22 to enable write access to product sales in March 22. You can edit blue values.
			2. Select **Read** for Jan 22 and Feb 22 to enable read access to product sales in those months.  
		Product sales data is invisible for the other months because both **Read** and **Write** are deselected.
![Dashboard that shows Access drivers - time module and Products over time module, so you can see the impact of selecting read and right cells..](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/16ccc1b6-85cc-48cd-9c29-a6d381ad9861/Access%20driver%20example%201.jpg)

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fexample-control-access-to-time-periods-4bfffe68-dc64-4ec3-836b-685db349a787&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>