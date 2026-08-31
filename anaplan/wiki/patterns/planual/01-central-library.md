---
title: "Planual Chapter 1 — Central Library"
type: pattern
tags: [anaplan, planual, central-library, time, versions, lists, subsets, users]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Support.md
  - raw/docs/Anaplan Support 1.md
  - raw/docs/Anaplan Support 2.md
  - raw/docs/Anaplan Support 3.md
  - raw/docs/Anaplan Support 4.md
  - raw/docs/Anaplan Support 5.md
  - raw/docs/Users and Roles  Anaplan Support.md
  - raw/docs/Line Item Subsets  Anaplan Support.md
---

# Chapter 1 — Central Library

> The Central Library is where we hold and create the **structures or dimensions** of the model.

This chapter governs everything that defines the *shape* of a model — the dimensions modules will later be built on. Eight sub-sections, in canonical order:

1. [Time](#time) · 2. [Versions](#versions) · 3. [Users and Roles](#users-and-roles) · 4. [Contents](#contents) · 5. [Lists](#lists) · 6. [Subsets](#subsets) · 7. [Line Item Subsets](#line-item-subsets) · 8. [Emojis](#emojis)

---

## Time

Hard-coding time goes against the **Sustainable** in PLANS — it breaks on rollover. Prefer the dynamic Model Calendar with selective Time Ranges for the exceptions.

### Key rules

- **Avoid SELECT on hard-coded time periods.** Use Time-formatted line items in modules instead, then SUM/LOOKUP against them.
  - **`1.01-01a`** Generic Time periods (Actual Period, Current Period, YTD, YTG, ALL Periods) → SELECT is OK.
- **Use the Model Calendar** for most modules; choose past/future-year settings that cover the bulk of requirements.
- **Use Time Ranges for the exceptions** — modules outside the "norm" run faster and keep model size down. Time Ranges may need manual updates at year-end rollover.
- **Enable Current Period** in Time Settings to use `CURRENTPERIODSTART()` / `CURRENTPERIODEND()` and to drive automatic "current period" lookup modules.
- **Consider All Periods** as a Top Level for time — small cell-count cost, big flexibility win when the same calculation is referenced many times.
- **Turn "include" settings off by default** (Quarter totals, YTD, YTG, etc.). They re-calculate in *every* module on the Model Calendar.
- **Time Range naming** — short `FYxx-FYyy` format fits the blueprint column. For ranges that scroll yearly, a generic name like "History Years" needs less maintenance.
- **Daily granularity ≥ 5 years**: prefer `PREVIOUS` over `CUMULATE`, and restrict the daily calendar with a Time Range.

> [!tip] Time and formulas
> See also [Chapter 2 — Engine § Formulas](02-engine.md#formulas-classic) for `2.02-10` (PREVIOUS vs CUMULATE) and `2.02-23` (TIMESUM in Time-dimensioned line items).

---

## Versions

Native Versions add features lists don't have, but each version costs cells across every module that uses them.

- **Use Current/Actual checkboxes** to enable `CURRENTVERSION()`, `ACTUALVERSION()`, `ISCURRENTVERSION()`, `ISACTUALVERSION()`.
  - Current version doubles as a Top Level for Versions: a versioned source feeding a non-versioned target returns Current automatically.
- **Caveats** with native Versions:
  - Increases module size whenever Versions are referenced, even when no variance is needed.
  - In modules with 3+ dimensions plus calculation line items, calculation priorities can produce unexpected results.
  - You can't change the summary method on a version-formula line item from inside Versions settings.
- **Read/write access**: native version-level access is administrator-led; for finer control use **Dynamic Cell Access**.
- **Switchover** clears historic period cells (saves space) but is **forward-only** — moving it back blanks data permanently.
- **>10 versions → reconsider**. Native version block-structure has performance implications. If native functionality isn't critical, model versions as a normal list.

---

## Users and Roles

- **Don't grant list access roles unless end users edit list members.** Roles on lists consume memory; users can edit module data without list-level access.
- **Workspace user hygiene** — when a user no longer needs a model, remove access. The Users list size has a real cost when heavily used.
- **Role-specific entry pages**: each role gets its own landing page; avoid generic landing pages.

---

## Contents

The Contents tab defines what end users see. Treat it as a curated UX surface, not a model directory.

- **Remove Modules from the Contents panel** — users should enter data through dashboards/pages.
- **Split functional areas**: one set for dashboards, a separate set for modules (e.g. "Reports" vs "Report Modules").
- **"Show New Content" toggle**: ON for dashboard areas (auto-publish on role update), OFF for module areas (no surprise additions). Lets you build new content without disturbing live users.

---

## Lists

The single chapter the most rules — lists are where dimensionality starts and where size problems begin.

### Naming and codes

- **Hierarchies prefixed by letter+level**: `P1 Product Category`, `P2 Product Family`, `P3 Products`. **No `L` prefix on lists.**
- **Always have a code** — faster loads, more efficient. Especially critical for numbered lists.
  - **`1.05-02a`** Static non-hierarchy lists (e.g. Yes/No) — code optional, but `Y`/`N` work fine.

### List properties

- Properties have line-item-like behavior with **many limitations** — keep calculations in modules (`Module.Line Item`), not properties.
- Exceptions where properties are required (**`1.05-03a..e`**):
  - Reference module line items via formula where possible (audit trail intact)
  - Numbered-list `Assign` actions and associated filters (require properties)
  - Export labels
  - Conditional Page navigation
  - Dependent drop-downs (driver/dependent lists)
  - **`1.05-04a`** When the source has no code → combination of properties as fallback (slower, harder).
- **Display Name on numbered lists** → format as **List Formatted, not Text** (more efficient, fewer line items, simpler mappings). Reuse an existing list rather than spinning a new one.

### Top Level

- **Only when sums are actually needed.** Skip Top Level for currency codes, True/False indicators, children of composite lists.
- **Top-level calc on a large list can't be split** → grows linearly worse. If you need a total, add **intermediate parent totals** or use `SUM` for validation aggregations.

### Hierarchies — composite vs not

- **Composite > non-composite**: more flexible, calc more efficient. Try to **balance hierarchies** wherever possible.
  - **`1.05-08a`** Chart of Accounts / financial reporting hierarchies are valid non-composite uses.

### Organization & maintenance

- Use **placeholder lists** to organize General Lists; put Subsets and Line Item Subsets at the bottom (so they're easily identified in `Applies To`). Emojis on placeholder lists are OK (but see [Emojis](#emojis) elsewhere).
- **Don't clear-and-reload lists.** Increases structural changes, forces model save, removes pre-allocated memory blocks. Use a unique key + update; add a `TRUE` flag to know which records imported.
- **Codes don't carry data.** Don't bake dates or values into list codes — code-based attributes should be *derived*, not stored, otherwise list size explodes.
- **Avoid hierarchies in Data Hub.** Hierarchies belong in planning models.

---

## Subsets

- **Prefix with the parent list name**: `P3 Products: Active Products`.
- **Multiple subsets of the same list?** Consider whether they'd be better as **separate lists** — especially for non-overlapping subsets fed from a Data Hub. Subsets remain valid for overlapping ranges or when consolidating back to the primary list.
- **Avoid single-item subsets.** If the parent has a Top Level, a single-item subset is always 2 members. Use a Boolean flag in a SYS module or a `LOOKUP` against the desired item (avoids `SELECT`).

---

## Line Item Subsets

Line Item Subsets (LIS) let you treat a set of line items as a dimension — useful for variant formulas and reporting.

- **Naming**: prefix `LIS` then a description or the source-module name. For LIS spanning multiple modules, use a descriptive generic name. (Cross-link: rule `1.08-01` Avoid emojis applies — see [Emojis](#emojis).)
- **Per-version numeric formulae** — Use a LIS to hold version-specific numeric formulas, avoiding stacked `IF`s.
- **Summaries off by default** when using `COLLECT()` — summaries on top of `COLLECT()` aggregate data that's typically not needed.
  - Cross-links: `2.01-10` Calculation modules · `2.03-01` Keep Summary options off (see [Chapter 2 — Engine](02-engine.md)).

---

## Emojis

- **No emojis in names of lists, modules, line items, or actions** — they break integrations and ALM syncs (even on Functional Areas).
- **For pages not in an integration path**, emojis are tolerable if **UTF-8 compliant**.

---

## See also

- [[wiki/concepts/anaplan concepts/10_line-item|Line Item]]
- [[wiki/patterns/disco|DISCO]] (module classification used together with these structures)
- [[wiki/patterns/planual/02-engine|Chapter 2 — Engine]]
