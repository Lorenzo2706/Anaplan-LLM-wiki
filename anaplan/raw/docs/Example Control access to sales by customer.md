---
title: "Example: Control access to sales by customer"
source: "https://help.anaplan.com/example-control-access-to-sales-by-customer-02998179-f051-4dbb-a978-910633eeff80"
author:
published:
created: 2026-05-13
description: "This example demonstrates how to use dynamic cell access to control access to monthly product sales by customer."
tags:
  - "clippings"
---
This example demonstrates how to use dynamic cell access to control access to monthly product sales by customer.

Before you create an access driver module, create a simple *Products* [list](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075), and a short *Customer* list such as:

| **Products** | **Customers** |
| --- | --- |
| **All products** |

To control access to sales by customer:

1. Select **Modules** in the model settings bar.
2. [Create an access driver module](https://help.anaplan.com/16e25678-22af-418b-b599-ba7e53b8269d), and name it *Access drivers - Products, Customers*.
	1. Position the *Customers* list on [**Pages**](https://help.anaplan.com/17b0ba75-c9dc-4b68-840f-6f846632a42b), and the *Products* list on **Columns**. Remove **Time**.
		2. [Insert two line items](https://help.anaplan.com/47f768d6-71fd-497f-8f7d-c4e45adfa12b), *Read* and *Write*. These are the access drivers.
		3. Select **Blueprint** , then change the format of both line items to **Boolean**.
3. Create a target module, and name it *Products by Customer.*
	1. Position **Time** on columns.
		2. Insert a line item, name it *Data*, and position it on **Pages**.
		3. [Nest](https://help.anaplan.com/b6f2ae19-d6b8-486d-88ef-6875274625c8) the *Customers* and *Products* lists on rows.
		4. Select **Blueprint** , then apply *Access drivers - Products, Customers.Read* and *Access drivers - Products, Customers.Write* to the **Read Access Driver** and **Write Access Driver** columns, respectively.
		5. In the *Access drivers – Products, Customers* module, select the checkboxes for both customers, and enter some numbers.
4. For the purposes of this example, [publish both modules to a single dashboard](https://help.anaplan.com/2e008f1e-e3c8-4056-8629-d25465528397), and name it *Product sales by Customer.*
![Dashboard that shows access drivers set by product and customer.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/8b3d84f9-679f-49c8-819a-0407f6c5d155/Access%20driver%20example%202.jpg)

In the *Access drivers - Products, Customers* module, for *Customer - Galaxy*, the *Soft Drinks*, *Coffee*, and *Tea* list items have *Read* access. *Rose Wine* is not set for either *Read* or *Write,* so no data is visible. *Red Wine, White Wine,* and *Craft Ale* are set to *Write.*

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fexample-control-access-to-sales-by-customer-02998179-f051-4dbb-a978-910633eeff80&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>