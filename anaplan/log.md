# Operation Log

Append-only. Newest entries at the bottom.

## [2026-08-31] lint | post-restructure wiki-lint pass (verification step of the single→multi-customer restructure)
Scanned `anaplan/` (481 md files) plus cross-domain link targets. Fixes applied in this domain:
- `index.md`: corrected stale "8 standalone patterns" → "7" (a customer-specific naming-convention page had been moved out to that customer's own `wiki/patterns/` earlier in this restructure; `wiki/patterns/index.md`'s own "7 standalone pages" count was already correct — the two pages had drifted apart).
- `wiki/patterns/index.md`: reworded the Number Format Standard summary row from naming a specific customer model to "links to one customer model's audit history" — removes a customer-identifying reference from tracked/public content (Minor per the brief, page body itself was already generic).
- `wiki/functions/index.md` and `wiki/sources/2026-05-02-anapedia-all-functions.md`: fixed two `[[wiki/functions/categories]]` folder-links (Obsidian does not auto-resolve a folder link to its `index.md`) → now point at `wiki/functions/categories/index`.
- `wiki/patterns/data-loading-best-practices.md`: removed two reverse cross-domain references (a body link and a `sources:` frontmatter entry) that pointed into a customer domain's `wiki/sources/...` and `raw/docs/...` — this generic/public pattern page would have shipped a dangling, customer-identifying pointer to template users with no customer tree at all. Replaced with generic, non-linking prose; the page's own guidance content is unchanged.

Verified clean (no fix needed):
- All forward cross-domain links from customer-domain model/source pages into `anaplan/wiki/patterns/*` and `anaplan/wiki/functions/categories/*` (disco, planual chapters, ragged-hierarchy, version-as-list, data-loading-best-practices, circular-reference, number-format-standard) resolve correctly.
- Concept/function/pattern page counts elsewhere in `index.md` and sub-indexes cross-checked against actual file counts — all correct (145 functions/10 categories, 22 core concepts + 2 flat pages, 15-chapter Demand & Inventory app with 4 "-detailed" companions = 19 files, Planual 8 chapters, The Anaplan Way 7 pages).

Flagged, not fixed (needs a human/data decision, no fabrication):
- `wiki/functions/index.md` row for **ACOSH**: links to `raw/docs/ACOSH  Anapedia` which does not exist anywhere in the vault, even though every sibling hyperbolic-function raw doc (ASINH, ATANH, COSH, SINH, TANH) does. Looks like the ACOSH Anapedia page was never actually clipped/ingested despite being listed. Needs either the missing raw doc ingested or the dead raw-source link removed from that row.

