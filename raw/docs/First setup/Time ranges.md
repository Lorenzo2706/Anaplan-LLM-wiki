---
title: "Time ranges"
source: "https://help.anaplan.com/time-ranges-1d28b6e4-184b-4ba2-990c-defcaf65bde6"
author:
published:
created: 2026-05-13
description: "Time ranges are a type of dimension that are used in modules and line items to enable the analysis of time-based data. You can restrict the range of periods into which data can be entered or displayed, over a time period longer or shorter than the main timescale."
tags:
  - "clippings"
---
[Dimensions](https://help.anaplan.com/dimensions-e020c93d-9f3e-4cce-8294-2d34073b302a "Dimensions")

Time ranges are a type of dimension that are used in modules and line items to enable the analysis of time-based data. You can restrict the range of periods into which data can be entered or displayed, over a time period longer or shorter than the main timescale.

**Note**: Time Ranges in Polaris can be found [here](https://help.anaplan.com/46c1b737-2735-43f0-95a2-71c8b786b87e).

Each time range is an independent entity with a **Start Period** and a defined **Number of Periods** in years. These are measured in units of a fiscal year and are independent of the Model Calendar. They are not locked to the current fiscal year, or to the number of past or future years configured for the Model Calendar.

The start point of a time range is tied to the **Fiscal Year Start Month** of the **Model Calendar**. If this value is changed, all time ranges will realign accordingly.

You can [create as many time ranges](https://help.anaplan.com/04ba8a9c-9bee-410f-955d-a7467804a519) as needed and define how the data is summed or aggregated.

There are a number of advantages in using time ranges in your modeling activities.

| Less sparsity | The calculation engine can ignore any empty cells, and it is not necessary to perform aggregations in time or in other dimensions. |
| --- | --- |
| Less workarounds | It’s often impractical to expand the model calendar to handle all time periods that may be required. In this case the model builder may employ custom time lists to handle the differing ranges of periods which can have undesirable consequences. |
| More accessible views | They give independent, finer-grained control of the available aggregations. Currently, if you enable Quarter totals for the model calendar, they are calculated for all line items that vary by time, and appear in all module views. |
| Greater time period range | 2-digit format calendars enable you to plan up to 50 years into the future, with the limit being 2078. 4-digit format calendars enable you to plan up to 100 years into the future from the set start date. |
| Multiple time ranges | Each time range allows independent aggregation of the line items within the span of the time range. |
| ALM support | Application Lifecycle Management (ALM) supports time ranges to enable you to synchronize your data across environments. |

Time ranges have some known limitations. They:

- can only use units of whole years.
- do not support the Weeks: General calendar type.
- do not vary by version, or by any other list.
- cannot be marked as production data (ALM).
- have a fixed span, for example, they do not update with the Current Period.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftime-ranges-1d28b6e4-184b-4ba2-990c-defcaf65bde6&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>