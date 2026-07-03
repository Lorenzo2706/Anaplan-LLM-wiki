---
title: "Anaplan Support"
source: "https://support.anaplan.com/consume-872fb11d-55ee-423b-9854-1eea182a9fde"
author:
published:
created: 2026-05-04
description: "Planual rules for Core integration."
tags:
  - "clippings"
---
Ensure the Anaplan model workspace has enough free space before pushing large data through the Anaplan Data Orchestrator link.

If the workspace size is insufficient, you may encounter an issue where no list members are added in Anaplan when data is pushed to a list, even though the link push completes with a 'completed' message.

The link performance is optimal if the input dataset includes just those columns that are needed.

We have observed that the presence of superfluous columns has a negative impact on the time required to update lists and modules.

This reduces the volume of data pushed to the model. The more duplicates that exist in the original source data, the greater the benefit of removing these when updating the model.

We have observed that exporting data from tables results in larger file sizes and that pushing data from the source data can take longer. These effects can be minimized by using a view or transformation instead. This also helps with maintenance, since it makes it simpler to amend the definition of a view that a link is based upon.

This complicates the mapping process.

In Data Orchestrator, we require that code be mapped for numbered lists and that name be mapped for standard lists. When you map with name, the code is considered an attribute to be updated. We recommend that you work with numbered lists that are also tagged as Production Data.

If you pull numbered lists from an Anaplan model into Data Orchestrator (which will be pushed back into numbered lists), ensure that you either include or generate a unique code. The generated item number isn't included in the export from the model.

Back to top