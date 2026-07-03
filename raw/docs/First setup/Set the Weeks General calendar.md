---
title: "Set the Weeks: General calendar"
source: "https://help.anaplan.com/set-the-weeks-general-calendar-ba7ab203-412d-48b5-ba4a-bf9695448cff"
author:
published:
created: 2026-05-13
description: "The Weeks: General timescale has no concept of financial years, only weeks. This means that you cannot include Year, Year to Date (YTD), or Year To Go (YTG) summaries.However, you can use Current Period in calculations that use the CURRENTPERIODSTART and CURRENTPERIODEND functions."
tags:
  - "clippings"
---
The **Weeks: General** timescale has no concept of financial years, only weeks. This means that you cannot include Year, Year to Date (YTD), or Year To Go (YTG) summaries.

However, you can use **Current Period** in calculations that use the `CURRENTPERIODSTART` and `CURRENTPERIODEND` functions.

To set the **Weeks: General** calendar type:

1. Select **Time** in the model settings bar.
2. Select **Weeks: General** in **Calendar Type**.

You can set the following options:

**Timescale** can be set in a:

- ‌2-digit format: Allows you to plan up to 2078.
- 4-digit format: Allows you to plan up to 100 years into the future from the set start date.

This setting also changes how the **Current Fiscal Year** and **Current Period** fields display. For example, if you select a 2-digit format, Fiscal Year 26 will display as FY26. If you select a 4-digit format, it'll display as FY2026. If your current period is January 2025, it'll display as Jan 25 for a 2-digit format, and Jan 2025 for a 4-digit format.

Select the calendar start date.

Type the total number of weeks that you want to include in the calendar.

You typically set **Current Period** to the last time period for actual [version](https://help.anaplan.com/19b4391f-5257-40ee-8dfb-36f0ab426c8f) data.

A benefit of setting **Current Period** is that you can refer to it in formulas instead of hard coding the specific time period. For example, you could use:

`Revenue.Data[SELECT: TIME.'Current Period']`

You can also use these functions:

- [`CURRENTPERIODSTART`](https://help.anaplan.com/a7af7113-e1dc-478d-bbbe-ecb597092991) to return the start date of the current period
- [`CURRENTPERIODEND`](https://help.anaplan.com/5c7aa5ad-1a45-4b48-8dca-6707ba964883) to return the end date of the current period

If **Current Period** is not set, the formula returns a blank value.

You can update the **Current Period** via the [**Update Current Period** action](https://help.anaplan.com/e94034cd-8004-479f-8c1a-655a296398f0), as well as the **Model Calendar**. This lets you set the current period using a line item with a Time Period data type, and import the **Current Period** from a data hub.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fset-the-weeks-general-calendar-ba7ab203-412d-48b5-ba4a-bf9695448cff&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>