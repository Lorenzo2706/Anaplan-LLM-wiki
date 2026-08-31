---
title: Text Functions
type: function-category
tags: [anaplan, functions, text]
created: 2026-05-02
updated: 2026-05-02
---

# Text Functions

String manipulation, plus link builders.

## Members
**FIND, LEFT, LENGTH, LOWER, MID, RIGHT, SUBSTITUTE, TEXT, TEXTLIST, TRIM, UPPER, MAILTO, MAKELINK**

## Common patterns
- Slice: `LEFT`, `MID`, `RIGHT` (positional) and `FIND` to locate a delimiter first.
- Clean: `TRIM`, `LOWER`, `UPPER`, `SUBSTITUTE`.
- Convert: `TEXT(num)` and inverse via `VALUE()` (in [[wiki/functions/categories/misc|Misc]]).
- Concatenate: `TEXTLIST(text, sep, list)` (text version) or use `&` for two values.
- Build clickable cell content: `MAKELINK("Open", URL)`, `MAILTO(...)` — useful in dashboard line items.

## TEXTLIST — two functions, one name
- **Aggregation** version: `Source[TEXTLIST: Mapping, ...]` — concat across mapping (see [[wiki/functions/categories/aggregation]]).
- **Text** version: `TEXTLIST(text, sep, list)` — concat across a list dimension within one cell.

> [!warning] TEXTLIST (Text function) — Classic engine only
> The Text variant supports a `UNIQUE` / `ALL` keyword to control duplicate handling and has a 10,000-character output limit (truncated with ellipsis). Key constraints:
> - **Does not work in Polaris** — Classic engine only.
> - Cannot reference individual named Users list items (only the Users list as a dimension).
> - Source: `raw/docs/TEXTLIST (Text function).md`

## See also
- [[wiki/functions/index]]
