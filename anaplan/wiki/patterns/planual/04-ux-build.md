---
title: "Planual Chapter 4 — UX Build"
type: pattern
tags: [anaplan, planual, ux, apps, pages, filters]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Support 12.md
  - raw/docs/Anaplan Support 13.md
  - raw/docs/Anaplan Support 14.md
---

# Chapter 4 — UX Build

> Building the UX. Where Chapter 3 is the *why*, this chapter is the *how*: Apps, Pages, Filters.

Sub-sections: [Apps](#apps) · [Pages](#pages) · [Filters](#filters)

---

## Apps

- **Naming** — short and practical. Use **alphanumeric prefixes** on Page names so they sort correctly on the App Contents page.
- **Custom Views** unlock richer conditional formatting. Use them when the page builder needs that flexibility.
- **Output modules for custom views** — when the page builder doesn't need staging line items, build an output module dedicated to the Custom View.
- **Page types**:
  - **Boards** — KPIs, graphs, variance reporting, multi-module reviews, landing pages.
  - **Worksheets** — entering/editing large datasets, pivoting data.
- **Mobile apps** — design page flow left-to-right within each row on a Board. Often a separate mobile app with proper spacing is the right call.
- **Card templates** — when a module powers multiple cards of the same "card type", save it as a template. Big efficiency win on Boards/Worksheets.

## Pages

### Design process

- **Start with the end** — walk through UX principles. Requirements drive which modules supply which values, not the other way around.
- **Don't horizontally scroll the whole screen** — fix the grid and scroll inside the grid.
- **Build for the smallest user screen size**, not yours. Change resolution to verify.

### Selectors and navigation

- **Separate page selectors > module page selectors**, especially when the same dimension appears across multiple cards.
- **Show the page selector** but drive selection from a **general** page selector.
- **Selection module on a separate page** keeps main pages clean and lets users move efficiently up/down hierarchies.
- **App Menu / module hyperlinks for navigation** — don't clutter pages with buttons.
- **Refresh discipline** — train users to use the toolbar Refresh, not "refresh" action buttons.

### Content

- **Charts with filtered axes**: configure with filter showing all items first, publish the chart, then re-apply the desired filter.
- **Use the card's Title and Description** rather than adding text directly on the page.
- **Imports/Exports vs Processes** — imports/exports must be republished if modified or replaced; **Processes** stay consistent with whatever they contain. Prefer Processes for management.
- **Don't expose list-element maintenance** to end users (they could delete history). Keep list maintenance in admin processes.
- **Image URLs in Assets**, surfaced via a SYS module on the relevant list.
- **My Pages** — let users personalize views.

### Performance

- **List-formatted line items are expensive** on pages, especially with large lists.
- **Limit displayed line items per module**; if needed, split list-formatted line items into separate modules.

## Filters

- **One Boolean condition per filter for max performance.** When you need multiple conditions on the same tab, **combine them into one line item** and filter on that.
  - *Why*: when multiple filters sit on the same tab, the engine reads them sequentially (filter 2 applies to filter 1's result set), not in parallel. Combining is faster.
- **Filters in separate System modules** — reusable across modules; don't redefine filter logic per consumer.
- **Don't use Show/Hide for time** — it's static. Use the Time Settings module so filters track Model Calendar changes dynamically.
- **User-list-dimensioned filter modules** support per-user dynamic filtering.
- **Avoid filtering on nested dimensions** — pivot the view differently first; if you must, ensure the filter expression itself is efficient.
- **Document filter usage in Blueprint notes** — saved-view and dashboard filter audits are easier when filters are annotated. Reference By doesn't list filters on views.

---

## See also

- [[wiki/patterns/planual/03-ux-principles|Chapter 3 — UX principles]] (the design philosophy these rules implement)
- [[wiki/patterns/planual/02-engine|Chapter 2 — Engine § Modules]] (filters in System modules pattern)
