---
title: "Anaplan Support"
source: "https://support.anaplan.com/subsets-46124ef2-8062-4a5e-9999-a6b66facbdf3"
author:
published:
created: 2026-05-04
description: "Planual Rules regarding Subsets"
tags:
  - "clippings"
---
Prefix the subset with the name of the list (‌for example, P3 Products: Active Products).

[Good Practice Naming Conventions](https://help.anaplan.com/name-conventions-aeb0b95e-f7a3-4fe5-81c7-aec9a12f80be)

Lists and subsets take up space within a model, so if you need multiple subsets of the same list, consider whether they would be better as separate lists. This is especially valid if the lists don't overlap and they're being fed from a Data Hub. For overlapping subsets or if there is a need to “consolidate” the value back to the primary list then subsets are a valid construct for model efficiency.

If possible, try and avoid single item subsets. If there's a top level in the list, a single item subset will always have two members. Consider using a Boolean flag in a SYS module or a LOOKUP line item against the desired item (to avoid using SELECT).

Back to top