---
title: "Time period selection"
source: "https://help.anaplan.com/time-period-selection-f5263813-9086-4554-a8ec-5197a2ddc10f"
author:
published:
created: 2026-05-13
description: "The settings a workspace administrator chooses for the Model calendar create time periods. These periods become aggregation levels and options users can select in various parts of the model."
tags:
  - "clippings"
---
[Time](https://help.anaplan.com/time-53836b0c-1238-48ef-834a-8728b24f3d8e "Time")

The settings a workspace administrator chooses for the Model calendar create time periods. These periods become aggregation levels and options users can select in various parts of the model.

Which time period options display for you depends on the part of the model you are in, and whether the model uses time ranges.

If you use time ranges, the set of periods you can select from depends on context. In some places the options are by time ranges, in others, you can choose from the time period superset.

The time period superset includes both time ranges and all time periods across the Model calendar and their aggregation levels. This includes time periods not contained by a time range.

For example, if you create a series of time ranges between 2018 and 2021, and then add a time range for 2023. The superset contains values for 2020 even though there is no time range for that period.

If you enable the optional aggregation levels **Quarter** and **Half-Year**, these are also part of the superset.

Changes to time ranges can affect the superset. For example, if you:

- Add a new time range, or edit an existing one, to include periods not present in any existing time range, the new periods are added to the superset.
- Edit a time range to remove periods, providing those periods are not in any other time range, they're removed from the superset.
- Edit a time range to add an aggregation level that's not already in the superset, it's included.
- Edit a time range to remove an aggregation level, where the aggregation level is not in any other time range, it's removed from the superset.

This table shows which model elements use which time period options:

| **Model element** | **Time options are determined by** |
| --- | --- |
| Line item time scale | Line item time range |
| Time period format | Superset |
| Versions:  - Switchover - Edit from - Edit to - Bulk copy | Superset |
| Modules:  - Filter - Compare - Import (except for the **Selected Year** setting) | Module time range |
| Import > **Selected Year** setting | Superset |
| Current period | Model calendar settings |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ftime-period-selection-f5263813-9086-4554-a8ec-5197a2ddc10f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>