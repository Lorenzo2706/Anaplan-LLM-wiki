---
title: "Create an access driver module"
source: "https://help.anaplan.com/create-an-access-driver-module-16e25678-22af-418b-b599-ba7e53b8269d"
author:
published:
created: 2026-05-13
description: "Create an access driver module to store access drivers. Access drivers are line items with Boolean data types that define the dimensions that you want to control cell data access to."
tags:
  - "clippings"
---
Create an access driver module to store access drivers. Access drivers are line items with Boolean data types that define the dimensions that you want to control cell data access to.

An access driver's dimensions must be compatible with those of the target module or line item it's applied to. The dimensions are compatible if:

- The access driver module and target module or line item have at least one matching dimension, or
- The driver line item is dimensioned against users, or
- The driver line item is dimensioned against the parent hierarchy and the target module or line item is dimensioned against the child hierarchy.

And

- The access driver is a Boolean formatted line item with any of these summary methods: All, Any, None, or Formula (Boolean line items have a summary method of None by default)

For every list dimension in the target module that does not match the list dimensions in the access driver module, set a **Top Level Item** for flat lists.Set a **Top Level Item** on the [**Configure** tab of the list](https://help.anaplan.com/4764efd5-3f7c-4537-9202-de21a858cade).

To create an access driver module that enables you to set access manually:

1. [Create a module](https://help.anaplan.com/686ff444-5356-48d1-9a9c-7cb2544e31d8) that is dedicated to access drivers.
	- Select the dimensions that you want to control access to the target cell data with. For example, use the Time dimension on columns.
		- If you want to control access to cell data for individual users, add the *Users* list.
		- Optionally, name the module to describes its purpose. For example, *SYS01 Access - Time*.
2. [Insert line items](https://help.anaplan.com/47f768d6-71fd-497f-8f7d-c4e45adfa12b) to control access. For example, create one line item for read access, and one for write access. You can add extra line items to use with different target line items.
3. In Blueprint, [format](https://help.anaplan.com/46d8e4e5-544e-48a8-9c4b-d9c240ff4c53) the *Read* and *Write* line items as Boolean.  
	**Note:** You can use formulas to automatically enable or disable the access driver checkboxes depending on an external factor, such as the start of a new time period. To see examples, [download the Dynamic Cell Access – Learning App](https://community.anaplan.com/t5/learning/Dynamic-Cell-Access-Learning-App/ba-p/33869) .
4. Select **Blueprint** to move into Grid view. For write access, in the *Write* line item, select the cells that you want to be writeable. The *Read* line item is read-only. The leaf-level cells that were not selected in Write, are selected.  
	For example, if you have a driver for write and a driver for read, and they're both on the line item you're controlling access to, then your access is:
	- Write: false, Read: false = no write, no read
		- Write: false, Read: true = no write, yes read
		- Write: true, Read: false = yes write, yes read
		- Write: true, Read: true = yes write, yes read  
		  
		Write driver gives read access.

|  | **Jan 22** | **Feb 22** | **Mar 22** | **Q1 FY22** | **Apr 22** | **May 22** | **Jun 22** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Write** |  |  |  |  |  |  |  |
| **Read** |  |  |  |  |  |  |  |

To control access to cell data by user, enable **Show All Users** in the target module.

To apply access drivers to target cell data:

1. Open the target module in Blueprint.
2. Navigate to the **Read Access Driver** or **Write Access Driver** columns, then select the appropriate access driver line item. To apply the access driver at module level, select the access driver in the first row. Access drivers cascade to every line item in the module where there's a hyphen. The same level of access applies to all cell data in the module when the driver is set at the module level.
3. If you want a very fine level of granularity, you can apply separate access drivers to each line item.

|  | **Read Access Driver** | **Write Access Driver** |
| --- | --- | --- |
| Products over time | Access - Time.Read | Access - Time.Write |
| Product A | \- | \- |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcreate-an-access-driver-module-16e25678-22af-418b-b599-ba7e53b8269d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>