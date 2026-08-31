---
title: "Planual Chapter 2 — Engine"
type: pattern
tags: [anaplan, planual, engine, classic, polaris, modules, line-items, formulas]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Support 6.md
  - raw/docs/Anaplan Support 7.md
  - raw/docs/Anaplan Support 8.md
  - raw/docs/Line Items  Anaplan Support.md
  - raw/docs/Anaplan Support 9.md
  - raw/docs/Anaplan Support 10.md
  - raw/docs/Anaplan Support 11.md
---

# Chapter 2 — Engine

> Anaplan's heart is the **Hyperblock** in-memory engine: spreadsheet flexibility + relational scale + multidimensional cube calc/aggregation.

Two engines — **Classic** and **Polaris** — share the Planual but optimize for different shapes of data:

- **Classic** — dense data sets where the majority of cells are populated. Calculates logic at *every intersection*.
- **Polaris** — sparse data sets, near-unlimited dimensionality. Calculates *only where source cells are populated*.

> All Classic rules still apply to Polaris unless explicitly overridden. Some Classic rules (e.g. `2.02-08` Never combine SUM and LOOKUP) matter **even more** in Polaris.

Sub-sections:

1. [Classic](#classic) — including [Modules](#modules-classic), [Line Items](#line-items-classic), [Formulas](#formulas-classic)
2. [Polaris](#polaris) — including [Polaris-specific module guidance](#modules-polaris) and [Performant formulas](#formulas-polaris)

---

## Classic

The general-purpose multidimensional engine. Classic calculates **logic at every intersection** of data, regardless of whether the cell is populated.

### Modules (Classic)

#### Naming, structure, organization

- **`2.01-01`** Keep names short and alphanumeric. **No DISCO prefix** — align modules with **functional areas** instead.
  - **`2.01-01a`** User-facing modules can be renamed for dashboard space, but don't cram dashboards (UX principles).
- **Functional areas** categorize modules; group "like" modules together inside each area.
- **Use empty modules (no line items)** as section headers/ordering inside Functional Areas. **No emojis.**

#### Dimensionality and views

- **Avoid Subsidiary Views** — hard to audit. Group calculation modules by like dimensionality instead.
  - **`2.01-06a..e`** Exceptions: dashboard-display attributes, ratio numerators/denominators, page-sync line items, sort-helper line items, reporting/export modules (mark these as subsidiary views to minimize calc).
- **Consistent dimension order** across modules — calc is faster when common dimensions appear in the **same order as the Applies To**. **Order matters more than list size.**
- **Lists replacing native time/versions** → place those lists as the **first two** in the dimension order to mirror native settings.
- **Don't add dimensions to fix a wrong formula.** If output is wrong, fix the formula or check whether an existing calculation module already has the dimensionality you need.

#### DISCO module types

(See also the [[wiki/patterns/disco|DISCO pattern page]].)

- **Time-only modules**: separate modules for time functions/filters. They re-calc only on model open or time-setting change.
- **One module per time granularity** (week/month/quarter/year).
- **System modules for hierarchy attributes**: at minimum, a SYS module with code + parent line items per hierarchy level.
  - **`2.01-08a`** SYS module isn't needed if the hierarchy is never referenced as a filter or selector.
- **Dimensionless assumptions module**: hold global SELECT values, time assumptions, ALM-friendly settings here.
- **Calculation modules**: house line items that share dimensionality. Avoid Subsidiary Views.
- **Filters in separate System modules** — reusable across modules. Document usage in the notes section (Reference By won't show filter views).
- **Access Drivers in separate modules** for relevant combinations — enables reuse and keeps access logic in one place.
- **Data Tags** can flag DISCO category if not used otherwise.
- **Hubs**: keep non-time data separate from static attributes.

#### Operational notes

- **Keep summaries off** by default. Use `SUM` for downstream aggregation when full hierarchy levels aren't needed.
  - **`2.01-10a`** When *all* aggregation levels are needed, native aggregation beats `SUM`.
- **Don't combine Select Levels with filters on the same hierarchy** — double filter, both fire. Use one or the other; a Boolean line item in a SYS module with `none` summary achieves the same outcome.
- **Copying large modules** is slow and locks the model. For large modules, **re-create** is often faster.

### Line Items (Classic)

- **Summaries off initially**, add back when needed. Especially true for Calculation modules and conditional-formatting line items.
  - **`2.03-01a`** Input/Output modules surfaced on Pages typically *do* need summary options.
- **Numbers and Booleans first** — Anaplan (like all computers) is optimized for numeric formats. Text is the most expensive format. Minimize text.
- **Set to BLANK** rather than leaving empty or with invalid text.
- **Headers → No Data** to avoid unnecessary calculations.

### Formulas (Classic)

These are the rules that move the needle on performance. Most can be summarized as: **split, simplify, reuse**.

#### Split and simplify

- **Avoid stacked `IF`s.** Split into separate line items + `LOOKUP`s or alternative constructs.
- **One simple sentence test**: if a formula needs more than one sentence to describe, split it.
- **Calculate once, reference many** — repeated expressions belong on their own line item.
- **Break long formulas** into separate line items. The engine parallelizes better, and stable subtotals don't recompute when other parts change.
- **Refer back to ultimate source** when possible — fewer dependencies → more parallel calc.

#### Text handling

- Text is expensive. Avoid multiple joins; split common joins to separate line items.
- **`IF ISBLANK()` when joining text.** If empty, set to BLANK.
- **Build joins in the smaller list first** to keep intermediate strings short.

#### Numeric tricks

- **Booleans take ⅛ the space of a number** in Classic — prefer TRUE/FALSE over numeric flags unless arithmetic is needed.
- **`A=B` is faster than `A-B=0`.**

#### Aggregation and time

- **`2.02-08` Never `SUM` and `LOOKUP` in the same expression.** Causes huge intermediate calcs, especially when Time is a dimension or source/target structures differ. **Split into separate line items.**
- **Use built-in summary methods** to avoid extra line items + IFs.
- **`2.02-10` PREVIOUS beats CUMULATE on long timescales** — fewer reads. Pattern:
  `Calc = data + PREVIOUS(Calc)` instead of `CUMULATE(data)`.
  - **`2.02-10a`** Short timescales (yearly, few years) → `CUMULATE` is faster.
- **`TIMESUM` shouldn't be used in a Time-dimensioned line item** — the calc is duplicated per period. If you need a full-timescale total, use `line item[SELECT: Time.All Periods]`. For partial windows, `MOVINGSUM` or `YEARTODATE`.
- **`TEXTLIST()` is memory-heavy** — prefer 2D modules + Boolean flags + `ANY`, or `FIRSTNONBLANK`/`LASTNONBLANK`.

#### List references

- **No direct list references** like `IF ITEM(list)=list.xx`. Use a SYS module Boolean → multiple members can share the same logic.
- **`2.02-14` Avoid hard-coded SELECT.** Use a constants module + `LOOKUP`.
  - **`2.02-14a`** SELECT for Versions is OK.
  - **`2.02-14b`** SELECT for the Top Level of a list is OK; for actual members, use mock parent lists + extra modules.
- **`POST` for simple offsets is wrong** — use `OFFSET`, `LAG`, or `MOVINGSUM`.

#### `FINDITEM` patterns

- `FINDITEM` on blanks is inefficient — it scans the whole list before returning blank. Pick the form that matches blank density:
  - Mostly *not* blank: `IF ISNOTBLANK(li) THEN FINDITEM(List, li) ELSE BLANK`
  - Mostly blank: `IF ISBLANK(li) THEN BLANK ELSE FINDITEM(List, li)`
  - Never blank: `FINDITEM(List, li)` — no check needed.

#### Conditionals

- Include a short-circuit conditional to avoid further references when a condition is satisfied.
- **Most-common branch first** — engine works through conditionals in order.

#### Heavy functions

- **`RANK`, `RANKCUMULATE`, `ISFIRSTOCCURRENCE`** can't multi-thread. With large lists they tank performance.

> [!tip] Cross-links
> Functions referenced here all have category pages: [[wiki/functions/categories/aggregation|Aggregation]], [[wiki/functions/categories/mapping|Mapping]] (SUM/LOOKUP warning lives there too), [[wiki/functions/categories/time-and-date|Time & Date]], [[wiki/functions/categories/text|Text]].

---

## Polaris

> All Classic Planual rules apply to Polaris unless explicitly stated otherwise. *Some* matter even more — `2.02-08` (no SUM+LOOKUP) is the canonical example.

**Why Polaris is different.** Polaris allows almost unlimited dimensionality. Classic models routinely use workarounds (concatenated lists, flattened dimensionality) to fit in workspace limits — none of those workarounds are needed in Polaris. Consequence: Polaris models are bound by **calculation effort**, not dimensionality. A bad formula that triggers work on every cell of a massively dimensioned line item will hurt much more in Polaris than any formula can in Classic.

### Modules (Polaris)

- **No concatenated lists** — Polaris doesn't need them. Still: **only use dimensions you need**. End-user navigation matters.
- **Dimension order doesn't matter** in Polaris (unlike Classic). Skip the Classic dimension-order optimization.

### Formulas (Polaris) — performant patterns

Polaris introduces a **Calculation Complexity** column on line items, telling you how the engine plans the work. Three categories:

#### One-to-One — most efficient

The engine drives the calc by iterating only over the **populated cells of one source**. Example: `Revenue = Units * Price` — multiplying every non-zero `Units` cell is enough; multiplying every `Price` is also valid but less efficient. The engine picks the cheapest path. Three real calculations instead of fifteen.

#### One-to-Many(x) — fan-out

Each populated source cell triggers `x` target cells. Example: `Units Months = QUARTERVALUE(Units Quarters)` → `One-to-Many(3)`. A signal data is being **spread out** along a dimension. Manageable at moderate `x`, expensive at high `x`.

#### All Cells — least efficient at scale

The engine has to compute every target cell. Example: `Units Total = Units + 1`. This is how Classic calculates almost everything; in Polaris with significant dimensionality, it's a red flag.

### Polaris-specific guidance

- **Booleans don't save space** in Polaris (they're roughly the same size as other formats). The Classic "use Boolean for flags" rule **doesn't carry over** as a memory optimization.
- **IF order doesn't matter** in Polaris. `IF X THEN Y ELSE Z` ≡ `IF NOT X THEN Z ELSE Y`. (Classic's "most-common-branch-first" is a Classic rule.)
- **Default values matter — keep them as the common case.** Polaris stores only non-default (non-blank, non-zero, non-FALSE) cells. If TRUE is the common case, **invert the logic** to make FALSE the default.
- **Constants and `ITEM(list)` make a module 100% dense** — every cell populated, every cell stored. Use sparingly.
- **Inherently expensive functions** in significant dimensionality: `ISFIRSTOCCURRENCE()`, `RANK()`, `CUMULATE()`.
- **`SUM` + `LOOKUP` is paramount to avoid in Polaris.** Even more critical than in Classic. Split LOOKUP into its own line item, then SUM separately.
- **`LOOKUP` is computationally heavy** in Polaris — the engine iterates every item in the looked-up dimension. Make LOOKUPs their own line item to amortize the cost across consumers.

---

## See also

- [[wiki/patterns/disco|DISCO]] — module classification used by all DISCO rules above
- [[wiki/patterns/planual/01-central-library|Chapter 1 — Central Library]] (Time, Versions, Lists)
- [[wiki/functions/categories/mapping|Mapping functions]] — SUM/LOOKUP warning
- [[wiki/functions/categories/time-and-date|Time & Date functions]] — PREVIOUS, CUMULATE, TIMESUM, MOVINGSUM
