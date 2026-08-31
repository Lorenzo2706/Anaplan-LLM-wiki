---
title: Conditional Formatting
type: concept
tags: [anaplan, ux, formatting, page-builder, module]
created: 2026-06-05
updated: 2026-07-08
sources:
  - wiki/sources/2026-06-05-conditional-formatting.md
---

# Conditional Formatting

Conditional formatting colors module cells (or page-builder grid/KPI cards) based on the numeric value of a line item. It surfaces threshold breaches and data-quality issues without requiring users to scan raw numbers.

> [!note]
> Conditional formatting cannot be applied to **text-formatted line items that also have subsidiary views**.

---

## How it works

You define a gradient scale (2-color or 3-color) between a **Minimum** and a **Maximum** value, with optional **Midpoints**. Cells whose values fall between those thresholds are shaded proportionally along the gradient. Cells below the Minimum get the Minimum color; cells above the Maximum get the Maximum color.

**Key insight — the formatted LI and the value-source LI can be different.** You can color the *Grade* (text) line item based on the numeric values of an *Error Grade* line item — useful for form validation (see [[#Form validation pattern]] below).

Conditional formatting applied to a line item **persists when that line item is pivoted** to a different dimension.

---

## Configuration: new UX (Page Builder)

Used when building **worksheets** or **KPI cards** in the new UX (NUX).

### Via a saved view

If the source module already has conditional formatting configured, select a **saved view** when building the worksheet or card — the formatting is inherited automatically.

> [!warning]
> Designing a **custom view** strips any CF configured in the source module. To use CF in a custom view, configure it via the **Card configuration panel** instead (see below).

### Via Card configuration panel

1. Select the line item on the grid (or pick it from the **Line item** dropdown in the panel).
2. In the **Value** dropdown, select the line item whose numeric values drive the colors (default: same LI).
3. Choose a **Style**:
   - **Background** — fills cell background with a solid color.
   - **Border** — adds a colored border (keeps cell values readable; note: narrow columns may truncate values).
   - **Font** — changes font color; overrides any UX, grid-formatting, or theme-based colors.
   - **Morse** — adds a colored dot or dash to the left of the cell value (size scales with the value).
4. Set **Minimum** value + color.
5. Optionally add one or more **Midpoints** (tap **+** to add, **−** to remove).
6. Set **Maximum** value + color.
7. **Apply → Next → Update**.

The **Color Range** bar previews the gradient as you work.

---

## Configuration: classic module / dashboard

Used when formatting directly inside a **module** or on a **classic dashboard** (classic dashboards are not supported for new customers — build pages/apps in NUX instead).

### In a module

1. Open **Format → Conditional formatting** (toolbar) or the **Conditional formatting** toolbar button.
2. Select **New Rule**.
3. From the first dropdown, select the **line item to format**.
4. From the second dropdown, select the **value-source line item** (default: same LI).
5. Choose **2-color scale** or **3-color scale**; set Minimum, (Midpoint), Maximum values and colors.
6. Select **OK** to save the rule.
7. Tick the **Enable Conditional formatting** checkbox (bottom-right of dialog).
8. Select **OK** to apply.

> [!important]
> You must **save a view** of the module to retain conditional formatting. CF is stored on a view, not on the line item itself.

To remove: deselect the **Conditional formatting** checkbox in the toolbar.

### On a classic dashboard

CF applied to a classic dashboard grid is **independent** of the module's CF. Multiple grids on the same dashboard backed by the same module can each carry different CF without affecting each other or the source module.

---

## Form validation pattern

Use conditional formatting to highlight data-entry errors:

1. Add a **numeric helper LI** (e.g. *Error Grade*) that returns an error code:
   ```
   Error Grade = IF ISBLANK([Grade], 2, 0)
   ```
   Returns `0` (valid), `1` (warning), or `2` (error) — or any numeric scale.

2. Apply CF to the **display LI** (*Grade*) using *Error Grade* as the value source:
   - Minimum 0 → white
   - Midpoint 1 → yellow
   - Maximum 2 → red

3. Hide the *Error Grade* LI from the end-user view.

Result: cells in *Grade* glow red/yellow when blank or invalid, white when correctly filled. No user needs to look at raw numeric codes.

See also: [[wiki/functions/categories/logical|IF THEN ELSE]], [[wiki/concepts/anaplan concepts/10_line-item|Line Items]]

---

## Constraints & gotchas

| Constraint | Detail |
|---|---|
| Text LIs with subsidiary views | CF not supported |
| Custom views in NUX | Strip source-module CF — must reconfigure via Card config panel |
| Narrow columns (Border / Morse style) | Values may be truncated — widen columns |
| Module-level CF | Stored on a **saved view**, not on the LI — must save a view to persist |
| Classic dashboards | Deprecated for new customers; use NUX pages instead |

---

## References

- `raw/docs/Configure conditional formatting.md` (NUX step-by-step)
- `raw/docs/Apply conditional formatting.md` (module/classic)
- `raw/docs/Conditional formatting in a saved view.md`
- `raw/docs/Conditional formatting with data.md` (hub)
- `raw/docs/Use conditional formatting to validate forms.md` (pattern)
