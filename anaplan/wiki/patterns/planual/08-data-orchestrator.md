---
title: "Planual Chapter 8 — Anaplan Data Orchestrator (ADO)"
type: pattern
tags: [anaplan, planual, ado, data-orchestrator, integration]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Support 22.md
  - raw/docs/Anaplan Support 23.md
  - raw/docs/Anaplan Support 24.md
  - raw/docs/Anaplan Support 25.md
---

# Chapter 8 — Anaplan Data Orchestrator (ADO)

> ADO is Anaplan's modern data preparation pipeline. The Planual rules in this chapter help you **connect**, **convert**, **catalog**, and **consume** data correctly.

Sub-sections: [Connect](#connect) · [Convert](#convert) · [Catalog](#catalog) · [Consume](#consume)

---

## Connect

How source data enters ADO.

### From Anaplan

- **Build a dedicated module** for ADO extraction — only the data you want to push into ADO. ADO will copy *everything* in the module, including calculated and aggregated cells.
- **No subsidiary views** when extracting Anaplan modules — produces complex structures with columns irrelevant to specific line items, and you can't scope the extract via a saved view. Build a separate module instead.

### From files (CSV, S3, local)

- **All non-structured sources arrive as strings.** Add a transform to **CAST** columns to their correct type — required for downstream type-aware functions like aggregations.
- **CSV/text format**: column names in **row 1**, data from row 2. Names must be **unique** and contain **no special characters** (spaces, dots) — special chars are auto-replaced with underscores.

### Pipeline structure

- **Single transformation as fan-out point** — instead of multiple transformation chains referencing a source dataset directly, create one transformation off the source and feed it into all downstream transformations and links. Makes source replacement and structural changes much easier.

### Salesforce caveat (deletes)

Salesforce doesn't immediately purge records, even after recycle-bin deletion. The records remain visible via API with `isDeleted = TRUE`. Two options:

- **Wait** between deletion and resync (in append mode) — the deleted row won't be added.
- **Filter explicitly**: add an ADO transformation filter to drop rows where `isDeleted = TRUE`.

### Connector performance

Three drivers of connector throughput:

1. **The connector itself** — interface technology + source-side governors. SAP OData, for example, is rate-limited by SAP.
2. **Volume** — fixed startup cost per sync, so rows-per-second rises with row count up to a max. Column count matters less.
3. **Location** — same region (and ideally same data center) between source and ADO is materially faster. On-prem adds the customer's network topology to the equation.

## Convert

Transformation rules.

### Pipeline shape

- **Trim the volume early** — apply filters, aggregations, and column selection at the front of the chain, not the back. Less data through downstream transforms = less work.

### Hash-based unique keys

The `HASH` function returns a deterministic 56-character key. Truncating from the left is safe to a smaller width with negligible collision probability:

| Domain size | Safe truncation length |
|---|---|
| ≤ 1,000 items | 10 chars |
| ≤ 1 million items | 15 chars |
| ≤ 1 billion items | 20 chars |

(<0.0001% chance of collision at these widths.) Shorter hashes are more readable as codes.

### Type conversion

- **Date casting**: prefer `TO_DATE` (lets you specify the date format). Generic `CAST` assumes US `mm/dd/yyyy`.
- **Type-conversion functions**: `TO_NUMBER`, `TO_DATE`, `TO_TIMESTAMP` (string → typed); `TO_CHAR` (typed → string in a chosen format); `CAST` for general type conversion.
- **Type-checks**: `IS_FLOAT`, `IS_INTEGER`, `IS_BOOLEAN` validate strings before CAST.
  - **Caveat**: `IS_FLOAT` / `IS_INTEGER` reject strings with thousands separators. Wrap with `SUBSTITUTE` to strip commas first:
    ```
    IF IS_FLOAT(SUBSTITUTE('CC Test'.'New column1', ",", ""))
    THEN CAST(SUBSTITUTE('CC Test'.'New column1', ",", ""), "FLOAT")
    ELSE 0
    ```

### Joins

- **No cartesian-product joins by default** — prevents accidental cross-products between large datasets. To intentionally join in a constant value, add a calculated column with the same constant on both sides.
- **Equality-only joins** — you can't join on the result of an expression. For range/conditional joins (e.g. `TransactionDate >= ProductMaster.StartDate`):
  1. Join on the equality predicate (`Productcode = ProductCode`)
  2. Add a calculated column `InRelevantDateRange = TransactionDate >= StartDate`
  3. Filter the result on `InRelevantDateRange = TRUE`
- **Filter timing**: detail filters apply *after* column calculations. To filter on **original** values, do the calculation in one transformation view, then base the next view on it with the detail filter.

## Catalog

How ADO objects are organized and searched.

- **Naming conventions matter** — well-considered naming makes objects easier to find and maintain.
- **Inventory pages** offer property-based filters: criteria within the same property are OR-ed; across properties they're AND-ed.
- **Search box** restricts to objects whose name contains the search text.
- **Filters and column selections don't persist** beyond the page/session — re-apply when you return.

## Consume

Pushing ADO output back into Anaplan.

### Workspace and dataset shape

- **Free workspace before pushing large data** — if workspace size is insufficient, the link can complete with status `completed` but **no list members** are added.
- **Only the columns you need** in the input dataset — superfluous columns slow list/module updates measurably.
- **De-duplicate the source** — fewer duplicates → less data pushed → faster updates.

### Views vs tables

- **Push from views/transformations, not tables.** Exporting from tables yields larger files and slower pushes. Views are also easier to maintain — change the view definition and the link follows.

### Lists and codes

- **Use numbered lists tagged as Production Data** — simplifies mapping. ADO requires:
  - Numbered lists → **code** must be mapped
  - Standard lists → **name** must be mapped (code becomes an updatable attribute)
- **Numbered list round-trips**: when pulling a numbered list from Anaplan into ADO and pushing it back, **include or generate a unique code** — the auto-generated item number isn't included in the export.

---

## See also

- [[wiki/patterns/planual/05-integration|Chapter 5 — Integration]] — classic Imports/Exports/Data Hub
- [[wiki/patterns/planual/06-alm|Chapter 6 — ALM]] — production-data discipline interacts with ADO list pushes
