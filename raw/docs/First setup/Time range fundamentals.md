---
title: "Time range fundamentals"
source: "https://help.anaplan.com/time-range-fundamentals-16731ae9-6d65-4b72-a4ab-40ee64527b51"
author:
published:
created: 2026-05-13
description: "There are a number of concepts and notions that drive time range planning, creation, and use. These include the time range's length and granularity."
tags:
  - "clippings"
---
[Time ranges](https://help.anaplan.com/time-ranges-1d28b6e4-184b-4ba2-990c-defcaf65bde6 "Time ranges")

There are a number of concepts and notions that drive time range planning, creation, and use. These include the time range's length and granularity.

When you work with time ranges, consider how different time ranges work with the type of data you need and how it's summarized.

You define a time range in units of the model's fiscal year. You define the units in terms of a start period and a number of fiscal years, with a selection of available aggregations.

The **Start Period** of a time range is tied to the **Fiscal Year Start Month** of the model calendar.

A time range can begin before, extend after, or exist entirely within or outside the Model calendar. They do not react to changes to fiscal year or the number of past or future years, or Current period.

However, if the Start period in the Model calendar is amended, all time ranges align with the new value. So, if the Model calendar financial year starts in April, every time range aligns to start in April of the Model calendar's start year.

![A chart with columns for FY19, FY20, FY21, FY22, FY23, and FY24 across the top. At the bottom is a key with green for Within, purple for Extending after, light blue for Extending before, and dark blue for Not overlapping. In the column headers, FY20 is marked as the previous year and FY22 is marked as the future year. The column headers for FY20, FY21, and FY22 each contain a box with the text JFM|AMJ|JAS|OND. Below this is a line across all columns labelled as Model Calendar. Under this in the FY21 column is a green box with the text JFM|AMJ|JAS|OND. Below this in the FY21, FY22, and FY23 columns is a purple box that contains JFM|AMJ|JAS|OND. Below this in the FY19, FY20, and FY21 columns is a light blue box that contains JFM|AMJ|JAS|OND. Below this in the FY23 and FY24 columns is a dark blue box that contains JFM|AMJ|JAS|OND.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/c3edb8aa-b5b5-4a4c-8b26-f4975e5e82b6/how-time-ranges-work-2.PNG)

Before you implement a time range that is shorter than, or outside the current model calendar, make sure you do not need the current data stored in the model. This is particularly important when you implement time ranges for the first time.

If you're unsure:

- Back up the data to a file
- Copy the existing data on the line item to other line items that use the model calendar
- Back up the entire model

Some changes to the Model calendar can affect time ranges and model data:

| Model calendar setting | Effect |
| --- | --- |
| **Fiscal Year** **Start** or **Fiscal Year End** | This realigns all time ranges to the new fiscal year definition, which can cause data loss. |
| **Available Aggregations** | This has no effect on time ranges but does affect the default settings for new time ranges.  If you remove aggregation levels, and the granularity is set to the aggregation level you remove, this can cause data loss in any line items the model calendar applies to. |
| Settings for weeks calendar types, such as the Week Grouping option for Weeks 4-4-5 | These changes are inherited by time ranges but have no effect on data. |

The ability to define a different aggregation level for every time range provides increased flexibility for the design of models and data analysis.

Available aggregations are configured in the **New** or **Edit** dialog in the **Time Ranges** tab. You can select these for each time range or model calendar. The level of aggregation controls:

- Default module view
- Granularities available for line item dimensionality
- Granularities available for time period format
- Totals that can be referenced by calculations
- Behavior of functions such as PARENT

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftime-range-fundamentals-16731ae9-6d65-4b72-a4ab-40ee64527b51&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>