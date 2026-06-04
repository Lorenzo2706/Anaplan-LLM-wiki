---
title: "Anaplan Support"
source: "https://support.anaplan.com/time-d129f700-8a7d-44df-bce7-2e1408055db5"
author:
published:
created: 2026-05-04
description: "Planual Rules regarding Native Time"
tags:
  - "clippings"
---
This goes against the Sustainable element of PLANS, and the hard coding can cause issues when updating the timescales of the model. Modules with Time formatted items to be used as sums and lookups are the better option.

| **1.01-01a Generic Time periods** | It's OK to use SELECT with Generic Time periods such as Actual Period, Current Period, YTD, YTG, ALL Periods. |
| --- | --- |

| 1.01-01a Generic Time periods | It's OK to use SELECT with Generic Time periods such as Actual Period, Current Period, YTD, YTG, ALL Periods. |
| --- | --- |

As the Model Calendar is dynamic, there are a lot of advantages in using it for most modules. Choose suitable time settings (past and future years) that cover most of the requirements and use the model calendar to set these for the most part.

For the exceptions outside the “norm”, use time ranges for efficiency of calculations and for keeping the model size under control. But remember, Time Ranges may need to be updated manually on a year-end rollover.

[Time Range Application](https://anaplan.vanillacommunities.com/t5/Best-Practices/Time-Range-Application/ta-p/30479)

Utilizing the Current Period within the Time Settings allows the use of CURRENTPERIODSTART(), CURRENTPERIODEND() and can be used to create lookup modules to hold the current period automatically.

Consider the use of All Periods. This is effectively the Top Level for time and while it slightly increases the model cell count, it does allow for flexibility in modelling. This is especially useful if you need to reference the same calculation many times.

Turn the "include" settings off by default and only include these if absolutely necessary. These additional settings (Quarter totals, Year to date, Year to go, etc.) will be included in all modules with the model calendar as the time dimension. This means they'll perform calculations on these subtotals. Consider if you really need these values for all modules with the Model Calendar.

Note that you can specify different "include" settings for different Time Ranges, although by default Time Ranges will inherit the Model Calendar settings.

Keep the naming short using the FYxx-FYyy format. This format allows the administrator to see the scope and name of the Time Range in the module blueprint without referring to the Time Range itself. It fits within the column of the blueprint, which aids auditing and analysis.

However, this does mean that you may need to rename the Time Range if the range changes. So, if your Time Range needs to be incremented each year, and it's clearly documented, an alternative would be to use a generic name ("History Years"). It requires less maintenance but isn't as clear.

[Time Range Application](https://community.anaplan.com/t5/Best-Practices/Time-Range-Application/ta-p/30479)

Use Time Ranges to optimize the modules where the default model calendar is not appropriate. Consider the dimensionality for the data and set up the Time Range accordingly.

[Time Range Application](https://community.anaplan.com/t5/Best-Practices/Time-Range-Application/ta-p/30479)

Review the need for daily granularity for long timescales, specifically if the daily timescale spans five years or more. Use time ranges to restrict the daily calendars if possible and also use PREVIOUS rather than CUMULATE to optimize calculation efficiency.

Back to top