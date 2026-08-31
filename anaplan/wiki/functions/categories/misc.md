---
title: Miscellaneous Functions
type: function-category
tags: [anaplan, functions, hierarchy, list, version, ranking]
created: 2026-05-02
updated: 2026-05-02
---

# Miscellaneous Functions

Anapedia's catch-all. In practice most of these are *very* commonly used — especially the list/hierarchy navigation ones.

## Members & sub-buckets

### List / hierarchy navigation
- `ITEM(List)` — current list item / time period per cell.
- `PARENT(Child)` — parent in list or time hierarchy.
- `HIERARCHYLEVEL(List [, Direction] [, LevelType])` — position within hierarchy.
- `ITEMLEVEL(Item [, Direction])` — distance to root or leaf.

### Code / name conversion
- `CODE(Item)` — list item's code (string).
- `NAME(Item)` — list item's display name as text.
- `FINDITEM(List, Text)` — text → list item lookup.
- `VALUE(Text)` — text → number.

### Versions
- `CURRENTVERSION(Expr)` — value at the version flagged Current.
- `NEXTVERSION(Expr)`, `PREVIOUSVERSION(Expr)` — version-relative evaluation.

### Ranking
- `RANK(...)` — sequential ranks 1..N, with options for ties and grouping.
- `RANKCUMULATE(...)` — rank then accumulate in rank order.

### Line item subset utility
- `COLLECT()` — pull source line item values into a module containing a line item subset.

## See also
- [[wiki/functions/index]]
- [[wiki/concepts/anaplan concepts/10_line-item]]
