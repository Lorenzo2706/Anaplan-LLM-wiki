---
title: "Anaplan Support"
source: "https://support.anaplan.com/filters-5e54b65f-92ed-4f2e-a2ba-7023c825ede6"
author:
published:
created: 2026-05-04
description: "Planual rules regarding Filters"
tags:
  - "clippings"
---
For the most efficient performance, use filters that have only one Boolean condition. When multiple filters are needed for the same "filter tab", create a new line item encapsulating both conditions and use the new line item as the filter.

When multiple filters are defined for the same tab, the engine reads the filters sequentially, not at the same time. That means the data is read and the first filter is applied; then that filter two is applied to the result set of the first filter.

[Filter Best Practice](https://community.anaplan.com/t5/Best-Practices/Filter-Best-Practice/ta-p/37595)

Try and keep filters in separate System modules. They can then be reused for different modules and not defined multiple times.

Don't use the Show/Hide function for time; these are static. Instead, use the Time Settings module since this makes the filtering dynamic when the model calendar changes.

Create filter modules dimensioned by the Users list to support dynamic filtering of module data.

[Increase end-user adoption with smart filters](https://community.anaplan.com/discussion/42821/increase-end-user-adoption-with-smart-filters)

If possible, try and avoid filtering on nested dimensions. Try and pivot the view differently. If this isn't possible, ensure the filters are efficient.

[Filter Best Practice](https://community.anaplan.com/t5/Best-Practices/Filter-Best-Practice/ta-p/37595)

Make use of the notes section in the Blueprint to document where a line item is used as a filter. This will help in the auditing of a model for saved views, as well as with dashboard filters.

Back to top