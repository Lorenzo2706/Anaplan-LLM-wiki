---
title: "Planual Chapter 3 — UX Principles"
type: pattern
tags: [anaplan, planual, ux, design-principles]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Hierarchy of information  Anaplan Support.md
  - raw/docs/Smart grouping  Anaplan Support.md
  - raw/docs/Reduce visual load  Anaplan Support.md
  - raw/docs/Progressive disclosure  Anaplan Support.md
  - raw/docs/Use consistency and standards.md
  - raw/docs/Provide help and guidance.md
  - raw/docs/Use the correct data type.md
  - raw/docs/Give users visibility into status.md
  - raw/docs/Match with real-world scenarios.md
  - raw/docs/Check in with end users frequently.md
---

# Chapter 3 — UX Principles

> Broad UX guidelines tailored for Anaplan. They apply to **every** page you build, regardless of app or module type.

The chapter contains 10 principles. Each is a single design idea, not a checklist of fields — use them as a lens when reviewing or designing pages.

---

## 1. Hierarchy of information

A clear visual hierarchy makes content easy to read and creates a path for the viewer's eye.

- **Use a landing page** to provide key summary info — orients new users and gives a navigation jump-off.
- **Summary first, detail after** within each category. Add instructions explaining what end users should do.
- **Most-important info at the top** — typically KPIs.

## 2. Smart grouping

The mind groups similar items together to simplify input. Visual grouping helps users locate what they need faster.

- **Split content using categories** that match users' mental model — e.g. functional areas.
- **Tell a story** through page order; group and order pages accordingly.

## 3. Reduce visual load

Fewer items on a page → faster decisions.

- **Landing pages**: minimize/summarize and hyperlink to detail (cross-link: `3.01-03 Summaries first`).
- **Set a default color palette** — company-approved, consistent across the whole application.
- **Multiple pages > one scrolling page.**

## 4. Progressive disclosure

Present data in digestible chunks. Start simple, expose complexity only when needed.

- **Key info on first page**, link to a follow-up page for detail.
- **Granular pages support more tasks** (analysis, edit) — the driving grid should be a deeper view of the previous page.
- **Use the Additional Insights panel** for useful-but-not-essential navigation links.

## 5. Use consistency and standards

Users shouldn't have to wonder if different words mean the same thing.

- **Define naming, color, and link conventions for the tenant up-front.**
- **Same elements in the same spot** across pages.
- **Same metric, same color** wherever it appears.

## 6. Provide help and guidance

- **Easy-access help** — tooltips or a definitions page for metrics.
- **Use text and instructions sparingly** — keep them simple, no jargon overload.
- **Tooltips on visualizations** so users understand what they're seeing.

## 7. Use the correct data type (chart picking)

Match the visualization to the question.

| Use | When to use |
|---|---|
| **Grid** | Reading specific values across products × time. Not for trends. |
| **Line chart** | Trends over a continuous timeframe; comparing series over time. Use contrasting colors + legend. |
| **Column chart** | Comparing values across line/list items, or items over time. |
| **Bar chart** | Comparing across line/list items — preferable to columns when labels are too long for the X-axis. **Not for time.** |
| **Stacked column** | Part-to-whole with multiple series (e.g. revenue split into margin + expenses). |
| **Pie chart** | Parts of a whole, **not over time**. |
| **Funnel** | Stages in a sales process. |
| **Timeline** | Visualizing chronological process — project schedules, calendars of events. |
| **Waterfall** | Gradual transition between two periods (e.g. revenue/profit walk). |
| **Combination** | Two related variables with different magnitudes/scales. |

## 8. Give users visibility into status

Pages should keep users informed via appropriate feedback in a reasonable time. Knowing the status helps users decide what to do next and recognize mistakes.

- **Review pages with end users often** — drives requirements alignment and smoothes UAT.
- Cross-link: `3.10-01 During the design`.

## 9. Match with real-world scenarios

Speak the user's language — words, phrases, and concepts they already know.

- **Map the process in advance**, then let Anaplan **follow real-world conventions** so information appears in a natural order.

## 10. Check in with end users frequently

Put end users at the heart of the process.

- **Initial check-in** at design — learn needs, define what/how to build.
- **During build** — confirm direction.
- **After go-live** — ensure things work in practice.
- **Mix interviews and observation**: talk through ideas during build; later, watch users actually use the system and adjust where they get stuck.

---

## See also

- [[wiki/patterns/planual/04-ux-build|Chapter 4 — UX build]] (Apps, Pages, Filters — the *how*)
