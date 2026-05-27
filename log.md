# Wiki Log

Append-only record of ingests, queries, and lint passes. Newest at the bottom.

Parse with: `grep "^## \[" log.md | tail -N`

---

## [2026-05-02] init | Wiki bootstrapped
Created folder structure (`raw/`, `wiki/{concepts,functions,modules,models,patterns,sources}`), `CLAUDE.md` schema, `index.md`, `log.md`.

## [2026-05-02] ingest | Anapedia — Line Items Introduction (demo)
Demo ingestion to illustrate the workflow. Touched: `Clippings/wiki/sources/2026-05-02-anapedia-line-items-intro.md` (created), `Clippings/wiki/concepts/line-item.md` (created), `Clippings/wiki/patterns/disco.md` (created, referenced from line item page), `index.md` (refreshed).

## [2026-05-02] schema-update | Path layout
Updated `CLAUDE.md` to reference `Clippings/raw/` and `Clippings/wiki/` (Obsidian Web Clipper drops files under `Clippings/`). Added a "Function pages policy" rule: do not duplicate Anapedia by creating one wiki page per function — categorize and synthesize instead, create individual function pages on demand.

## [2026-05-02] ingest | Anapedia — All Functions (145 function references)
Source: `Clippings/raw/docs/All functions.md` + 145 individual function clippings under same dir. Strategy: synthesis over duplication. Created:
- `Clippings/wiki/sources/2026-05-02-anapedia-all-functions.md` — source summary
- `Clippings/wiki/functions/index.md` — categorized master index of all 145 functions with syntax, 1-liner, raw link
- 10 category overview pages under `Clippings/wiki/functions/categories/`: aggregation, mapping, time-and-date, logical, numeric, text, financial, trigonometry, call-center, misc
- Refreshed `index.md`
Key insights captured: SUM+LOOKUP performance warning (in mapping page), Polaris vs Classic LOOKUP differences, MONTHTODATE-vs-MONTHVALUE distinction, Erlang B/C distinction.

## [2026-05-04] ingest | Anaplan Support — Planual (full, 38 raw files)
Source: 8 chapter overview pages + 30 sub-section pages clipped from `support.anaplan.com`. Mapped raw files to canonical Planual chapters by fetching each chapter's web TOC. Strategy: one curated wiki page per chapter, with sub-sections as H2 headings, preserving rule codes (`C.SS-NNx`) verbatim.
Created:
- `Clippings/wiki/patterns/planual.md` — hub: PLANS philosophy, rule numbering, chapter index
- `Clippings/wiki/patterns/planual/01-central-library.md` ... `08-data-orchestrator.md` — 8 chapter pages
- `Clippings/wiki/sources/2026-05-04-planual.md` — full source map (raw → chapter → sub-section → wiki page)
Updated: `index.md` (added Planual entries to Patterns, Wiki Sources, Raw Sources; refreshed stats).
Cross-links to existing pages: DISCO, line-item concept, function category pages (mapping/SUM+LOOKUP, time-and-date/PREVIOUS-CUMULATE-TIMESUM, aggregation, text).

## [2026-05-04] ingest | Anaplan Way — implementation methodology
Source: `Clippings/raw/docs/Anaplan Way.md` (single ~480-line document covering agile/scrum, 4 cornerstones, 6 phases, change management, monitoring). User flagged this as project-management material distinct from the model-building Planual, and asked for the agent to actively suggest implementation best practices going forward.
Strategy: mirror the document's natural structure — hub + cross-cutting fundamentals + one page per phase.
Created:
- `Clippings/wiki/patterns/anaplan-way.md` — hub: methodology overview, cornerstones, phase index, dirty dozen / tollgates
- `Clippings/wiki/patterns/anaplan-way/00-fundamentals.md` — agile values, scrum process, 4 cornerstones, Do/Don't, scrum roles
- `Clippings/wiki/patterns/anaplan-way/01-pre-release.md` ... `06-deployment.md` — 6 phase pages
- `Clippings/wiki/sources/2026-05-04-anaplan-way.md` — source summary
Updated: `index.md` (added Anaplan Way to Patterns/Wiki Sources/Raw Sources, refreshed stats).
Cross-linked back to Planual (Ch.2 Engine performance rules, § Data Hub) and DISCO from the relevant Anaplan Way pages.
Memory: saved a feedback memory so the agent proactively offers implementation/PM guidance from the Anaplan Way alongside model-building help.

## [2026-05-05] ingest | FSP 2.0 — model CSV export (first real model)
Source: 5 CSVs under `Clippings/raw/models/` — Modules (68), General Lists (28), Line Items (471), Line Item Subsets (1), Versions (1). Stedin Netbeheer financial-statement plan for DSO regulated activities.
Strategy: model dossier (overview + modules catalog + lists + versions) without per-line-item pages — 471 line items would dilute value, and Modules.csv already lists item names per module so on-demand drill-down is cheap.
Created:
- `Clippings/wiki/sources/2026-05-05-fsp-2-0-model.md` — source summary
- `Clippings/wiki/models/FSP 2.0/index.md` — overview, DISCO mapping, calc flow, dimensionality, design choices
- `Clippings/wiki/models/FSP 2.0/modules.md` — full 48-module catalog (LO/DA/CA/IP/FS/RE/MA/IM/SM)
- `Clippings/wiki/models/FSP 2.0/lists.md` — version lists, SIP hierarchy, org hierarchy L3→L4→L5, dimensional + dummy lists
- `Clippings/wiki/models/FSP 2.0/versions.md` — deep dive on the version-as-list pattern (no native Versions used)
- `Clippings/wiki/patterns/version-as-list.md` — extracted reusable pattern
Updated: `index.md` (added Models section entry, version-as-list pattern, source).
Key insights: DISCO with `LO/DA/CA/IP/FS/RE` prefixes; LOAD≠INPUT split (loaded vs user-edited); version-as-list with `SM 08 FSP Version Control` carrying `Previous Version` self-reference + chained MJP→FSP→SIP; one `IM xx.` system module per significant list for properties; subsets per Applies To to manage 41M-cell calc spine (CA 03).

## [2026-05-05] update | FSP 2.0 — flagged as Polaris model
Added engine = Polaris note to `models/FSP 2.0/index.md`, source summary, and `index.md` entry. Important for future formula reasoning (Polaris vs Classic differs on `LOOKUP`, sparsity, formula scope).

## [2026-05-06] ingest-delta | FSP 2.0 — model CSV re-upload
Source: re-uploaded `Clippings/raw/models/*.csv` (Modules, Line Items, General Lists, LIS, Versions, Time Ranges). Diff vs 2026-05-05.
Delta: +4 modules (`DA 05. ACM Data`, `CA 08. Short vs Long Term Investments`, `IP 06. ABN Parameters per periode`, `SM 09. Time Settings - Historical data`), 1 moved (`RE 02 → IP 06` — recategorized from regulatory output to user input), +27 line items, lists/LIS/Versions unchanged. `Time Ranges.csv` newly exported (5 ranges, including TR-Historic ACM).
Created: `Clippings/wiki/sources/2026-05-06-fsp-2-0-model-delta.md`. Updated: `models/FSP 2.0/modules.md` (added new modules, removed RE 02 with note), `models/FSP 2.0/index.md` (refreshed prefix counts, linked naming convention).

## [2026-05-07] ingest-delta | FSP 2.0 — model CSV re-upload
Source: re-uploaded `Clippings/raw/models/*.csv`. Diff vs 2026-05-06.
Delta: +4 modules (`LO 09. Werkpakket to tafel/thema`, `DA 06. SIP total OPEX/CAPEX`, `CA 09. Thema Distribution`, `RP 01. Werkpakket LTIP`), new RP prefix section added to wiki. IM 19 confirmed (previously said IM 01–18). Two additional Time Ranges noted (`TR - WACC`, `TR - 20Y`). Lists/LIS/Versions unchanged.
Created: `Clippings/wiki/sources/2026-05-07-fsp-2-0-model-delta.md`. Updated: `models/FSP 2.0/modules.md` (new rows + RP section, count 52→56), `models/FSP 2.0/index.md` (prefix table), `index.md`.

## [2026-05-06] ingest | Stedin Naming Convention
Source: `Clippings/raw/docs/Naming Convention stedin.md`. Stedin-internal naming guideline covering Lists, Modules, Line Items, Actions, Dashboards.
Created: `Clippings/wiki/patterns/naming-convention-stedin.md` (full pattern page), `Clippings/wiki/sources/2026-05-06-naming-convention-stedin.md` (source summary).
Cross-linked to FSP 2.0 (modules.md, index.md), DISCO, Planual. Updated `index.md` (Patterns, Wiki Sources, Raw Sources, Stats).

## [2026-05-08] restructure | per-model subfolders + skill fix

Added per-model subfolders to support multiple models (FSP 2.0 + new AAC). Moved `Clippings/raw/models/*.csv` into `Clippings/raw/models/FSP 2.0/` and `Clippings/wiki/models/fsp-2-0/*` into `Clippings/wiki/models/FSP 2.0/`. Created empty `Clippings/raw/models/AAC/` and `Clippings/wiki/models/AAC/` for the upcoming AAC ingest. Updated all path references in wiki pages, `index.md`, and `log.md`. Updated `CLAUDE.md` Layers section to document the per-model subfolder convention (filenames repeat across models; directory name disambiguates).

Skill fix: project-skill discovery requires `.claude/skills/<skill-name>/SKILL.md`, but the file was at `.claude/skills/SKILL.md` directly so it never registered. Moved it (plus `references/`) into `.claude/skills/anaplan-formula-agent/`. The skill now appears in the available-skills list. Updated `CLAUDE.md` Skills section with the corrected path.

## [2026-05-08] ingest | AAC — initial CSV ingest (Polaris)

First-time ingest of Stedin's **AAC** (activity-based cost allocation) model, dropped in `Clippings/raw/models/AAC/` (6 CSVs: Modules 64, Lists 30, Line Items 711, LIS 5, Versions 1, Actions 86). User confirmed engine = **Polaris**.

Created: `Clippings/wiki/sources/2026-05-08-aac-model.md` (source summary), `Clippings/wiki/models/AAC/{index,modules,lists,lis,actions,versions,ragged-engine}.md` (7 model pages), `Clippings/wiki/patterns/ragged-hierarchy.md` (new pattern extracted from AAC). Updated: `index.md` (Models, Patterns, Wiki Sources), `Clippings/wiki/patterns/version-as-list.md` (added AAC as second confirmed instance), `MEMORY.md` (added AAC-is-Polaris memory).

Highlights surfaced: 9-level ragged hierarchy with composite `AAC Ragged` list (~48k items), per-level factors with upstream/downstream cumulative products, `COLLECT()`-over-LIS pattern in `CA 01.1`, billion-cell-class intersections in `IP 01./IP 02./CA 04./RP 02./UFI 02.` (only tractable on Polaris). Two flagged issues for the user: (1) suspected off-by-one in `CA 01.Cumulative Factor L3 Upstream` (`* Factor L2` instead of `* Factor L3`); (2) `CA 04.Toeslag materiaal` reads `'DEL IM 14. Artikelen'.Materiaal Groep` — deleting that DEL module would break the calc.

## [2026-05-08] restructure | add raw/logs/ folder

Added `Clippings/raw/logs/` with per-model subfolders (`FSP 2.0/`, `AAC/`) for error/diagnostic logs from imports/actions/processes. Same per-model subfolder convention as `raw/models/`. Updated `CLAUDE.md` Layers section to document the new layer and its purpose (ground truth for debugging action/import failures).

## [2026-05-12] ingest-delta | FSP 2.0

Re-upload of FSP 2.0 model CSVs + first-time ingest of `Actions.csv`. Modules 56→58 (+CA 10 Commercial Afschrijving, +CA 11 Central Cost Calculation w/ inflation [110M cells — now largest module], +IP 07 Allocatie naar Product/Domein). DA renumbering: old DA 04 Allocatie → IP 07; old DA 05/06 → DA 04/05. Renames: IP 03 → "ACM Historic Data"; IP 06 → "REG Parameters per periode" (+Inflation adjustment line item). MA 02 redimensioned FSP versions → Reguleringsperiodes. New page `wiki/models/FSP 2.0/actions.md` covers 7 processes / 22 imports / 1 selective-delete (DH 2.0, MJP, SIP-related upstream sources). Lists/LIS/Versions/Time Ranges unchanged.

## [2026-05-12] ingest | Anaplan Demand & Inventory Reference App (video transcripts)
Source: ~62 transcript files in `Clippings/raw/docs/` covering chapters 01, 03–12, 14–17 of the Demand Planning + Supply/Inventory reference-app configuration curriculum. Not tied to any active model — ingested as durable reference. Created `Clippings/wiki/sources/2026-05-12-anaplan-demand-supply-chain-app.md` and 15 chapter summary pages under `Clippings/wiki/concepts/anaplan-applications/demand-and-inventory/` (+ index page). Chapters 02, 13, and 17-04 not present in source set. Updated `index.md`.

## [2026-05-12] ingest-delta | Demand & Inventory app — added 17-04 Remaining Shelf Life
Added missing transcript `Clippings/raw/docs/17-04 Inventory reporting-remaining shelflife report.md`. Updated `17-inventory-reporting.md` (sources list, dedicated 17-04 section with RSL 526 parameter and true-expiry vs stop-sell detail) and the source summary's sources list + scope note. Chapters 02 and 13 confirmed unavailable — not pursuing.

## [2026-05-13] ingest | Anapedia — Missing Files (LIS, Modules, Actions, Contents)
File audit revealed 10 raw docs in `Clippings/raw/docs/` that had never been indexed. Ingested in a follow-up pass.
Created: 4 new concept pages (`line-item-subsets`, `modules`, `actions`, `contents-panel`). Updated `functions/categories/text.md` (TEXTLIST Text variant Classic-only warning). Skipped 7 files (duplicates, minor UX tips, already-covered topics). Source page: `Clippings/wiki/sources/2026-05-13-anapedia-missing-files.md`. Updated `index.md` (18→22 concepts).

## [2026-05-13] ingest | Anapedia — Core Concepts & Security (103 files)
Source: 103 new Anapedia files added to `Clippings/raw/docs/` covering core model structure, lists (general/numbered/composite), versions, time ranges, model calendar, access & security (model roles, selective access, DCA, access drivers), users, picklists, and data tags.
Created: 17 new concept pages + 1 new pattern page (`variance-reporting`) + 1 updated concept page (`line-item`). Source page: `Clippings/wiki/sources/2026-05-13-anapedia-core-concepts.md`. Updated `index.md` (stats: 1→18 concepts, 4→5 patterns, 186→289 raw files).
Key content: deep access/security cluster (`access-security` hub + `model-roles` + `selective-access` + `dynamic-cell-access` + `access-drivers` + `users`) — each with design patterns, gotchas, and interaction rules. Variance reporting pattern with SYS11/REP05/REP06 three-module chain and LIS + COLLECT() approach for Polaris. Model calendar gotcha: calendar type is effectively permanent. Mixed time scales disaggregation rule: coarser→finer returns blank, not an error.

## [2026-05-18] ingest-delta | AAC — Modules.csv major restructure

Re-upload of `Modules.csv` (prior version overwritten — raw file lost; future uploads should use date-suffix naming). This was a major module refactoring: prefix convention overhauled (MA→MM, SE/FI/DF→FM, UFI→UF, SYS→SM, SEC→AM, new LM). -7 modules removed (DEL IM 14 finally cleaned up, CA 01.1 test module + IM 13 LIS module removed, SE 02 + FI 05 + DF 01 + UFI 08 merged/removed), +5 added (MM 03, IM 13 Afdeling, IM 14 Subafdeling, LM 01 Lookup, UF 07 AAC L4). Net: 54 functional modules. Cell counts dropped ~80% (hierarchy data reduced). IM cumulative factors now computed per level in IM 01–09 modules. CA 02/03 simplified. DEL IM 14 dependency on CA 04 resolved.

Key: model is now aligned with the `Roles Modules.csv` design spec uploaded earlier today. Updated: `wiki/models/AAC/modules.md` (full rewrite), `wiki/models/AAC/index.md` (DISCO table, calc flow), `wiki/models/AAC/roles.md` (design-spec warning resolved). Created: `wiki/sources/2026-05-18-aac-modules-restructure.md`.

## [2026-05-18] ingest-delta | AAC — Roles family (5 new CSVs)

Re-upload of AAC model CSVs. Structural files (Modules, Lists, Line Items, LIS, Actions, Versions) unchanged vs 2026-05-08 first ingest. 5 new Roles files added: Roles.csv, Roles Modules.csv, Roles Actions.csv, Roles Lists.csv, Roles Versions.csv. Users.csv not included (privacy). Delta: +0 modules · +0 lists · +0 line items · +1 wiki page (roles.md).

Key findings: 4 roles (Full Access, Read-only, Super user, Regular user). List admin is Super-user-only. All roles get Write to Actual version. Notable: `Roles Modules.csv` and `Roles Actions.csv` use design-spec module/action names that don't match the implemented model — flagged in roles.md as an alignment issue before go-live.

Created: `Clippings/wiki/models/AAC/roles.md`, `Clippings/wiki/sources/2026-05-18-aac-model-roles.md`. Updated: `Clippings/wiki/models/AAC/index.md` (Roles section), `index.md` (AAC sub-page count 7→8, stats).

## [2026-05-19] ingest-delta | FSP 2.0
Re-upload of `Modules.csv` and `Line Items.csv` only (lists/LIS/versions/time/actions untouched). Delta vs 2026-05-12: **+7 modules** (CA 12 GAW skeleton; IP 08 Long-Term Growth Parameters, IP 09 Degressieve factor, IP 10 Nieuwe Investeringen; FS 04 Verloopstaat — ~80-line asset/equity/debt rollforward; UF 01/02 — new `FILTER MODULES` user-dashboarding pair). MA 02 Reguleringsperiode→Tijd time range widened from Model Calendar to TR-Depreciation (78 → 1 326 cells). New cross-refs on CA 06 (← IP 10) and SM 05 (→ FS 04). IM 06 added `Tech - Begin/Einde reguleringsperiode` accessors.

Touched: `Clippings/wiki/sources/2026-05-19-fsp-2-0-model-delta.md` (new), `Clippings/wiki/models/FSP 2.0/modules.md` (+7 module rows, new UF section, MA 02 note), `Clippings/wiki/models/FSP 2.0/index.md` (prefix counts CA 11→12, IP 7→10, FS 3→4, +UF row), root `index.md` (source line).

> [!warning] Prior raw CSVs were overwritten in place — no `__YYYY-MM-DD` snapshot retained. Future deltas should preserve the prior file per CLAUDE.md raw-file-handling rule.

## [2026-05-22] ingest-delta | FSP 2.0
Re-upload of `Modules.csv`, `Line Items.csv`, and `General Lists.csv` (LIS, Versions, Time Ranges, Actions untouched). Largest delta since first ingest. **Modules 65 → 80** (+15 net): new depreciation/asset-base/WACC stack (**CA 13 Investment base**, **CA 14 Depreciation Methods** — 18.2M cells, now 2nd-largest module after CA 11; **CA 15 RFR**, **IP 11 RFR Historic**, **RP 02 Degressief Aschrijving Waterfall**); new Bloomberg market-data chain (**LO 10 Bloomberg Data → DA 06 Bloomberg → CA 15 RFR**, companion **MM 03 Bloomberg Items**); **CA 12 GAW fully fleshed out** (was 0-cell skeleton on 2026-05-19, now 19 line items in Historisch/Toekomstig/Totals groups). **MA → MM prefix migration** completed. Renames: IP 02 Wening Parameters → Versie Parameters; IP 06 REG Parameters per periode → ACM Parameters per periode (reverted to original ACM name; new `Degressief Factor (Jaar)` LI); RE 01 Regulering 2027 → Regulatory revenue (+`Verwijderen gasaansluitingen/netten`, `Gereguleerde Afschrijvingen` LIs). IP 10 Nieuwe Investeringen redimensioned: added `ACM Amortization Terms` dimension (1 680 → 20 160 cells); now feeds CA 12 GAW + CA 13 (was CA 06). SM 03 Time Settings - Year: TR widened Model Calendar → TR-Depreciation. SM 05 added Data Type + Dashboarding LI groups. SM 08 line items renamed to Dutch (Vorige Versie, Export Versie?, Historische ACM Data, Start/Eind Jaar, SIP Planvariant, MJP Version). IM 06 +Beginning/Ending Year; IM 18 +Short Term Investments; IP 05 +Amortization Term (List)/ACM; IP 09 Lineair? → Linear?. List changes: +Bloomberg Tickers (4), +Bloomberg Items (4); ACM Amort Terms 11→12; Reguleringsperiodes 13→14; Debt Items L2 0→6; Dummy Time subsets 4→5 (added SS Tijd dummy CY+10).

Raw files snapshotted as `Modules__2026-05-22.csv`, `Line Items__2026-05-22.csv`, `General Lists__2026-05-22.csv` so future deltas have a diff base (closing the gap flagged 2026-05-19).

Touched: `wiki/sources/2026-05-22-fsp-2-0-model-delta.md` (new), `wiki/models/FSP 2.0/modules.md` (rewrite), `wiki/models/FSP 2.0/lists.md` (Bloomberg lists + count refreshes + Dummy Time subset note), `wiki/models/FSP 2.0/index.md` (prefix table 65→80, MA→MM, calc-flow extended for GAW/depreciation/WACC), root `index.md` (source line).

## [2026-05-27] ingest-delta | FSP 2.0
Re-upload of `Modules.csv` and `Line Items.csv` only (General Lists, LIS, Versions, Time Ranges, Actions untouched). **Modules 80 → 81** (+1): new **CA 16 Ratios** — FFO/ND ratio and solvency module (`FSP versies`, Year/Model Calendar, 560 cells, 52 pop, 366 kB). Reads FS 01 (`EBITDA`, `Vrijval klantbijdragen`), FS 02 (debt lines), FS 03 (`Betaalde belasting: resultaat`). FS 01/02/03 Referenced-By lists updated to include CA 16. New cross-references: **IP 10 now reads CA 06 and IP 05** (new wiring, likely for investment-base lookup). Data-only shifts: CA 13 pop 6 898 → 3 778; CA 14 pop 5.36M → 4.87M, memory 143 → 136.4 MB. Typo flagged: CA 12 LI `Stijging GAW aboslute` (transposed letters) — model carries the typo.

Raw files snapshotted as `Modules__2026-05-27.csv`, `Line Items__2026-05-27.csv`.

Touched: `wiki/sources/2026-05-27-fsp-2-0-model-delta.md` (new), `wiki/models/FSP 2.0/modules.md` (+CA 16 row, FS 01/02/03 + CA 06 + IP 05 ref notes, CA 13/14 pop counts, CA 12 typo), root `index.md` (source line).
