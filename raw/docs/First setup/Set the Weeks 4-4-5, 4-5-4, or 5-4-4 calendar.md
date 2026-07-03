---
title: "Set the Weeks: 4-4-5, 4-5-4, or 5-4-4 calendar"
source: "https://help.anaplan.com/set-the-weeks-4-4-5-4-5-4-or-5-4-4-calendar-150f3b73-8be1-4d95-92fd-24daa46ae869"
author:
published:
created: 2026-05-13
description: "Select Weeks: 4-4-5, 4-5-4, or 5-4-4 to select a pattern for grouping weeks into months (4-4-5, 4-5-4, or 5-4-4)."
tags:
  - "clippings"
---
Select **Weeks: 4-4-5, 4-5-4, or 5-4-4** to select a pattern for grouping weeks into months (4-4-5, 4-5-4, or 5-4-4).

Typically, every quarter has 13 weeks. However, as one year isn't exactly 52 weeks, you can compensate for this with a 14-week quarter once every five or six years. A 4-4-5 fiscal month and a calendar month aren't the same.

To set the **Weeks: 4-4-5, 4-5-4, or 5-4-4** calendar type:

1. Select **Time** in the model settings bar.
2. Select **Weeks: 4-4-5, 4-5-4, or 5-4-4** in **Calendar Type**.

You can set the following options:

Select the pattern for how weeks are grouped into months for each quarter.

For example, some organizations report by 4-4-5 quarters (four weeks in the first month, four weeks in the second month, and five weeks in the third).

You can set when the end of the fiscal year falls.

The options are:

- **Last** ***Day*** **in** ***Month***, for example, **Last** ***Sat*** **in** ***Dec****.*
- ***Day*** **nearest to end of** ***Month***, for example, ***Sat*** **nearest to end of** ***Dec****.*

The option that you choose automatically adjusts the values available in **Current Fiscal Year** to align with your selection.

**Timescale** can be set in a:

- ‌2-digit format: Allows you to plan up to 2078.
- 4-digit format: Allows you to plan up to 100 years into the future from the set start date.

This setting also changes how the **Current Fiscal Year** and **Current Period** fields display. For example, if you select a 2-digit format, Fiscal Year 26 will display as FY26. If you select a 4-digit format, it'll display as FY2026. If your current period is January 2025, it'll display as Jan 25 for a 2-digit format, and Jan 2025 for a 4-digit format.

The **Fiscal Year Label** appears in modules that use the Time [dimension](https://help.anaplan.com/e020c93d-9f3e-4cce-8294-2d34073b302a). The default is **FY**.

You can change the label if the model timescale doesn't represent your fiscal year. For example, you can change it from **FY** to **CY** if the model uses the calendar year. The length of the label is two characters.

The **Fiscal Year Label** is mandatory. Use the same **Fiscal Year Label** if you have related models to provide consistency.

If you [change the **Fiscal Year Label**](https://help.anaplan.com/b5fd95e3-86ec-4e4c-8807-3463d3fe0747),be aware of the impact on any imports, exports, or filters in your model. Try changing the **Fiscal Year Label** in a development model first so you can check that your imports and exports work correctly.

Align the **Fiscal Year Label** with the end month or start month of the fiscal year. Use this option when the fiscal year does not coincide with the calendar year of January 1 to December 31.

For **Calendar Months/Quarters/Years**, the options are:

- **End Month of the Fiscal Year**.
- **Start Month of the Fiscal Year**.

For **Weeks: 4-4-5, 4-5-4 or 5-4-4**, and **Weeks: 13 4 week Periods**, the options are:

- **End Week of the Fiscal Year**: the calendar year that contains the first day of the last week of the fiscal year.
- **Start Week of the Fiscal Year**: the calendar year that contains the final day of the first week of the fiscal year.

The date ranges available adjust based on what you set as the **Fiscal Year Start Month**.

If you change the **Current Fiscal Year,** the new year starts with a clean, unpopulated model. If you want to keep data from previous years, before you change the model, either:

- Copy the model.
- Set the **Number of Past Years** to 1 or more, depending on how many years of data you want to keep.

You can set this option up to 20 years into the past. Use the smallest timescale possible, as each additional year substantially increases the size of the model. Use **Time Ranges** for longer periods.

You can set this option up to 50 years into the future. Use the smallest timescale possible, as each additional year substantially increases the size of the model. Use **Time Ranges** for longer periods.

Weekly calendar timescales represent 52 weeks, or 364 days in a year. The standard calendar year has 365 days, and every fourth year has 366 days. This means that the financial year is shorter than the calendar year.

To correct this, approximately every 6 years, there are 53 weeks in the financial year. The year when you have 53 weeks is calculated for you, based on this setting, and the setting for **End of Fiscal Year is**.

Select the time period to which you want to add the 53rd week.

Select the week format:

- **Numbered**, for example *Week 8 FY23*
- **Week Commencing**, for example *W/c 23 Jan 23*
- **Week Ending**, for example *W/e 29 Jan 23*

You typically set **Current Period** to the last time period for actual [version](https://help.anaplan.com/19b4391f-5257-40ee-8dfb-36f0ab426c8f) data.

A benefit of setting **Current Period** is that you can refer to it in formulas instead of hard coding the specific time period. For example, you could use:

`Revenue.Data[SELECT: TIME.'Current Period']`

You can also use these functions:

- [`CURRENTPERIODSTART`](https://help.anaplan.com/a7af7113-e1dc-478d-bbbe-ecb597092991) to return the start date of the current period
- [`CURRENTPERIODEND`](https://help.anaplan.com/5c7aa5ad-1a45-4b48-8dca-6707ba964883) to return the end date of the current period

If **Current Period** is not set, the formula returns a blank value.

You can update the **Current Period** via the [**Update Current Period** action](https://help.anaplan.com/e94034cd-8004-479f-8c1a-655a296398f0), as well as the **Model Calendar**. This lets you set the current period using a line item with a Time Period data type, and import the **Current Period** from a data hub.

Includes the **Quarter Totals** summary in the Time dimension. For example, *Q1 FY22*. If you select **Quarter Options**, you can also select **Quarter** for a module or line item in the **Time Scale** column.

Includes the **Half-Year Totals** summary in the Time dimension. For example, *H2 FY22.* If you select **Half-Year Totals**, you can also select **Half-Year** for a module or line item in the **Time Scale** column.

**Year To Date** (YTD) is used with the **Current Period.** YTD is added as an extra summary period for the year that contains the **Current Period**.

For example, if the model calendar is set to *Jan 2020 - Dec 2021*, and the **Current Period** is *June 2021*, the **YTD** column is added as a summary period for 2021. The **YTD** column shows you the summary of the data from *Jan 2021 - Jun 2021*.

If you select this option, you can use it with the SELECT formula. For example, you can apply this expression to a line item:

`*Source line item*` `[SELECT: TIME.YTD]`

**Year To Go** (YTG) is used with the **Current Period.** YTG is added as an extra summary period for the year that contains the **Current Period**.

For example, if the model calendar is *Jan 2020 - Dec 2021*, and the **Current Period** is *June*, the **YTG** column shows you the summary of the data from *July 2021 - Dec 2021.*

If you select this option, you ca use it with the SELECT formula. For example, you can apply this expression to a line item:

`*Source line item*` `[SELECT: TIME.YTG]`

Displays the total of all the periods in the **All Periods** column. If you select this option, you can use it with the SELECT formula. For example, you can apply this expression to a line item:

`*Source line item*` `[SELECT: TIME.All Periods]`

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fset-the-weeks-4-4-5-4-5-4-or-5-4-4-calendar-150f3b73-8be1-4d95-92fd-24daa46ae869&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>