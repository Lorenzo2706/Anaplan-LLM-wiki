---
title: "Anaplan Support"
source: "https://support.anaplan.com/versions-e574057c-2269-4efc-8d3d-a012e7c7f5a5"
author:
published:
created: 2026-05-04
description: "Planual Rules regarding Native Versions"
tags:
  - "clippings"
---
Utilizing the Current (and Actual) checkbox within the Version Settings allows the use of CURRENTVERSION() and ACTUALVERSION() in calculations, in SELECT statements, and ISCURRENTVERSION and ISACTUALVERSION() for Boolean checks.

Current version also acts as a top level for Versions. If you have a source module with versions (and Current ticked) in a target module without versions, the value from the current version will automatically be returned without needing additional functions or SELECT statements.

While this is a simple construct and it might be OK for simple models, it effectively adds size to models every time versions are used in a module even if you don't want the variance.

Also, in modules with three or more dimensions, if you have calculation line items and aggregations, the results may not always give the expected result due to different calculation priorities. Finally, you can't amend the summary method for a version formula within the versions setting.

Use these as a simple, administrator-led control for read and write access to versions. For more granular control, use Dynamic Cell Access.

Using switchover means the historic periods are effectively cleared out. This does have the benefit of reducing model size as the historic cells are cleared, but switchover should be moved forward only. Moving it backward will blank out the respective period removing any values that were previously held.

Versions have built-in functionality that's not available for normal lists. However, a large number of Versions (for example, 10+), can have performance implications due to the block structure. Review the need for a large number of Versions, and if the native functionality isn't critical or needed, consider using a normal list to represent Versions.

Back to top