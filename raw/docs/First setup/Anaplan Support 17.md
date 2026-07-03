---
title: "Anaplan Support"
source: "https://support.anaplan.com/imports-7a942bf1-95a0-4c96-8ba9-92789375b2de"
author:
published:
created: 2026-05-04
description: "Planual rules regarding Imports"
tags:
  - "clippings"
---
Ideally, this would be a separate file that's unique as opposed to using the same file for the transactional load. By creating a file of unique members, the volume and size of the file will be much smaller than the full transactional file.

| 5.04-01a Code is >60 characters | If the code is >60 characters, you will have to use a combination of properties. |
| --- | --- |

The data file should have the key and values based on the dimensions. Non-dimensional data should be in a different file.

[Data Hub: Purpose and Peak Performance](https://community.anaplan.com/t5/Best-Practices/Data-Hubs-Purpose-and-Peak-Performance/ta-p/48866)

Consider what ‌makes the row unique and include only attributes in the key, not data fields or dates.

[Data Hubs: Purpose and Peak Performance](https://community.anaplan.com/t5/Best-Practices/Data-Hubs-Purpose-and-Peak-Performance/ta-p/48866)

Use the Ignore field if there are any unwanted fields in the source data.

Ignoring unneeded fields in the source will make the action perform better and the system won't create a warnings log.

When possible, aggregations should be done in the source system. This will boost the performance of the import action and the Anaplan Engine as well as reduce the size of the file.

Only imported data at the granularity needed. There's no need to bring in transactional data at a weekly level when Planning happens at the month level.

Line items storing the imported data should reflect the correct data format: List formatted, numbers, and dates. Don’t use text (unless it is a true text field).

Import sources should always be done from a module view or a file. This allows for filtering and only including the elements required for each import.

By using a List as the source, the action will always bring over the entire list, not what's been recently added.

Saved views should be used as the source for model to model imports. Using views allows the action to import data that is needed (newly loaded). When using a module or a list, filters can't be applied and will import all data.

Use a generic date format (for example, YYYYMMDD) whenever possible to simplify the imports and remove the need for date mismatches and manipulations.

Back to top