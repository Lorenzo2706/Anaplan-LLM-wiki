---
title: "Example: Create a page called Variance report"
source: "https://help.anaplan.com/-example-create-a-page-called-variance-report-19370381-42d5-4a2f-a559-33f0f03b5aef"
author:
published:
created: 2026-05-13
description: "As part of the line item subset example, create a page that allows you to select between two months and view the variance between those months on five different items. As you select different months, the values change."
tags:
  - "clippings"
---
As part of the line item subset example, create a page that allows you to select between two months and view the variance between those months on five different items. As you select different months, the values change.

**Note**: See [Line item subset example](https://help.anaplan.com/84d95131-a83a-45b7-ba41-71defbb732ff) for the complete list of steps.

The goal is to have a page with two cards. One card allows you to select which months you want to compare, and another card shows the variance per country.

![A board that shows two cards, one that allows you to choose the months to compare (Month 1 and Month 2).The second card that shows the values for Month 1 and Month 2 for the Variance for Margin, Salary, Bonus, Rent, and Utilities.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/736e60a0-110b-42e3-8478-c0ffa4191ec3/nmx_variance_board.jpg)
1. [Create a page](https://help.anaplan.com/0e49fef9-6e99-4456-9912-57445d84f14c) that uses a board.
2. Name the page *Variance report*, and select the workspace and model that contains the modules you created for the Line item subset example.
3. Add a [grid card](https://help.anaplan.com/c4c27b0f-bb99-4fc8-b2c4-405498fcd9ad) to the board and configure the card:
	- To display the *SYS11 Time Variance Reporting* module.
		- Give it a title such as *Select the months to compare*.
		- Select **Grid** and turn on **Allow editing**.
4. Add a second grid card to the board and configure it:
	- To display the *REP06 Variance Report*.
		- Select **Pivot** , drag **Line items** onto **Columns**, and the line item subset *LIS Multi-variance reporting* onto **Rows**. Select **Update**.
		- Give it a title such as *Variance per country*.
		- Select **Cog** for **All Regions** and select **Show/Hide**. Ensure that the *G2 Country* level is selected and select **Apply**.
5. To test the Variance report, select **Publish**. In the *Select months to compare* card, select two different months and see the values change in the *Variance per country* card.

You can configure the page in different ways. In the example shown, the *Users* list is hidden on both cards, but you could choose to show it. There's also a [text card](https://help.anaplan.com/4de76302-1d96-4cd3-a107-77970643049a) with instructions.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2F-example-create-a-page-called-variance-report-19370381-42d5-4a2f-a559-33f0f03b5aef&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>