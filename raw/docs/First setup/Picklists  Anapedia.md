---
title: "Picklists | Anapedia"
source: "https://help.anaplan.com/picklists-ddeaf549-4699-4e56-be9a-185205c49823"
author:
published:
created: 2026-05-13
description: "A picklist is a dropdown list that provides users with a list of valid values to select from."
tags:
  - "clippings"
---
[Dimensions](https://help.anaplan.com/dimensions-e020c93d-9f3e-4cce-8294-2d34073b302a "Dimensions")

A picklist is a dropdown list that provides users with a list of valid values to select from.

Simple picklists are list-formatted line items. You can select list items from a [list](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075), [list subset](https://help.anaplan.com/589d9f5d-f439-40a4-905f-5027c2dc9c21), or line item subset to populate line items with data.

For example, if you want to assign new employees to a department, you can create a *Department* line item that is formatted on the *Departments* list.

|  | **Department** |
| --- | --- |
| Employee A | HR |
| Employee B | Marketing |
| Employee C | Sales |

Filtered picklists, like simple picklists, are list-formatted line items. There are two types of filtered picklist: [one-to-many](https://help.anaplan.com/cfeebee8-6803-4941-bf65-bc2d58578fd2) and [many-to-many](https://help.anaplan.com/4969bb8c-edae-47be-8241-9dd3942671bd).

Unlike simple picklists, filtered picklists contain more complexity and reference other lists in a model: the driver and filter lists. Selections made in a driver list determine what users can select in a filter list.

You can also create an additional list that maps the relationship between list items in the driver and filter lists.

For example, if you want to update compensation plans for different roles, use filtered picklists to guide users to the correct values.

In this example, the *Role* line item is list-formatted on the *Role* list, the driver, and the *Compensation Plan* line item is list-formatted on the *Compensation Plan* list, the filter. Only *Plan A* appears as a valid list item for the *Executive* role, but both *Plan A* and *Plan B* appear as valid list items for the *Senior Director* role.

|  | **Role** | **Compensation Plan** |
| --- | --- | --- |
| Employee A | Executive | Plan A |
| Employee B | Senior Director | Plan A |
| Employee C | Senior Director | Plan B |
| Employee D | Team Leader | Plan C |
| Employee E | Staff Member | Plan E |

Manage all lists for use as picklists in **General Lists** in the model settings bar.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fpicklists-ddeaf549-4699-4e56-be9a-185205c49823&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>