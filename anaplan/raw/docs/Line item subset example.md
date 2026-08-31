---
title: "Line item subset example"
source: "https://help.anaplan.com/line-item-subset-example-84d95131-a83a-45b7-ba41-71defbb732ff"
author:
published:
created: 2026-05-13
description: "You can use a line item subset to pull line item data from different modules and view them in a single place. This example describes how to create a page that lets you select between two months, and view the variance between those months on five different items. As you select different months, the values change."
tags:
  - "clippings"
---
You can use a line item subset to pull line item data from different modules and view them in a single place. This example describes how to create a page that lets you select between two months, and view the variance between those months on five different items. As you select different months, the values change.

Download the *Anaplan Level 1 Model Building* model. This model is available when you sign up for the Level 1 Model Building course in the [Anaplan Community](https://community.anaplan.com/t5/On-Demand-Courses/Level-1-Model-Building/ta-p/54499) . In Lesson 1, go to *Activity: Add Example Model to Your Workspace*.

[Create the *EMP03 Employee Expenses by Country*](https://help.anaplan.com/d52da97f-02ab-4dba-acc8-87f336c4035f) module. It's based on *EMP02 Employee Expenses*, and includes the Time [dimension](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a), and the *G2 Country* [list](https://help.anaplan.com/403a1ed1-ad7b-4ab3-b40c-61dd9d651075).

The goal is to have a board with two cards within the Anaplan [User Experience](https://help.anaplan.com/fed5bb63-0592-4402-b290-e708f500f14f). One card allows you to select which months you want to compare, and another card shows the variance per country.

![A board that shows two cards, one that allows you to choose the months to compare (Month 1 and Month 2).The second card that shows the values for Month 1 and Month 2 for the Variance for Margin, Salary, Bonus, Rent, and Utilities.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/736e60a0-110b-42e3-8478-c0ffa4191ec3/nmx_variance_board.jpg)

To create this board:

1. [Create a line item subset called *LIS: Multi-variance reporting*](https://help.anaplan.com/19dc483a-d7b8-4886-a557-f6823e87988b) that takes line items from three modules.
2. [Create a staging module called *REP05 Variance Report Staging*](https://help.anaplan.com/37dfbb55-5a5b-4277-8ffe-0d9dd419efa4) to pull the line item data into using the COLLECT() function.
3. [Create an input module called *SYS11 Time Variance Reporting*](https://help.anaplan.com/93d50c3d-c1da-4410-9f5f-3fcd99e3b0fc).
4. [Create a variance report module called *REP06 Variance Report*](https://help.anaplan.com/30b4a210-8ac9-4832-bd01-97381f8c996d).
5. [Create a page called *Variance report*](https://help.anaplan.com/19370381-42d5-4a2f-a559-33f0f03b5aef)*.*

When you've created the board, you can select different months on one card, and see the variance per country reflected on the other.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fline-item-subset-example-84d95131-a83a-45b7-ba41-71defbb732ff&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>