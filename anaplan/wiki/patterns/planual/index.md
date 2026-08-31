---
title: Planual
type: pattern
tags: [anaplan, planual, best-practices, plans]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Chapter 1 Central library.md
  - raw/docs/Chapter 2 Engine  Anaplan Support.md
  - raw/docs/Chapter 3 UX principles.md
  - raw/docs/Chapter 4 UX build.md
  - raw/docs/Chapter 5 Integration  Anaplan Support.md
  - raw/docs/Chapter 6 Application Lifecycle Management.md
  - raw/docs/Chapter 7 Extensions  Anaplan Support.md
  - raw/docs/Chapter 8 Anaplan Data Orchestrator.md
---

# Planual

The **Planual** is Anaplan's official, systematic set of standards for model building. Think of it as Anaplan's "manual for planning" — a numbered rulebook that tells builders what to do, what to avoid, and why.

## PLANS — the design philosophy

Every Planual rule traces back to **PLANS**, the five qualities a well-built Anaplan model should have:

| Letter | Quality | Meaning |
|---|---|---|
| **P** | Performance | Calculations are fast; the engine isn't doing more work than necessary |
| **L** | Logical | Structures and formulas are easy to follow and audit |
| **A** | Auditable | Each calculation is split, named, and traceable |
| **N** | Necessary | No redundant dimensions, line items, or modules |
| **S** | Sustainable | The model survives time-rollovers, list growth, and ALM cycles |

When in doubt about a design choice, ask: *which of P/L/A/N/S does this support, and which does it hurt?*

## Rule numbering

Planual rules use a `C.SS-NNx` code (e.g. `2.02-08` "Never use SUM and LOOKUP together", `1.05-08a` exception for chart-of-accounts). The first number is the **chapter**, the second is the **section** within the chapter, then a sequence number. Sub-letters (`a`, `b`, ...) mark exceptions or qualifications.

This wiki preserves rule codes verbatim where they appear in the source, so you can look them back up on `support.anaplan.com`.

## Index

The Planual is organized into **8 chapters**, each grouping rules by what part of the platform they govern. Each chapter below has its own page with the underlying sub-sections as H2 headings.

| # | Chapter | What it covers |
|---|---|---|
| 1 | [[wiki/patterns/planual/01-central-library\|Central Library]] | The structures/dimensions of the model: Time, Versions, Users & Roles, Contents, Lists, Subsets, Line Item Subsets, Emojis |
| 2 | [[wiki/patterns/planual/02-engine\|Engine]] | The Hyperblock — Classic vs Polaris engines, plus rules for Modules, Line Items, Formulas |
| 3 | [[wiki/patterns/planual/03-ux-principles\|UX principles]] | Ten cross-cutting design principles for any Anaplan UX |
| 4 | [[wiki/patterns/planual/04-ux-build\|UX build]] | Building the UX: Apps, Pages, Filters |
| 5 | [[wiki/patterns/planual/05-integration\|Integration]] | Actions, Processes, Imports, Exports, Source models, Import data sources, Data Hub |
| 6 | [[wiki/patterns/planual/06-alm\|Application Lifecycle Management]] | Revision tags, Production lists, Architecture, Deployed mode, Managing changes |
| 7 | [[wiki/patterns/planual/07-extensions\|Extensions]] | Excel and PowerPoint add-ins |
| 8 | [[wiki/patterns/planual/08-data-orchestrator\|Anaplan Data Orchestrator]] | Connect, Convert, Catalog, Consume |

## How to use this wiki section

- Browse a chapter when you want a checklist for a specific build phase (e.g., before starting a new module, read `02-engine`).
- Search by rule code (e.g., `2.02-08`) when reviewing a model — they're cited inline in each chapter page.
- Cross-references link Planual rules to **concepts** (`[[wiki/concepts/...]]`), **functions** (`[[wiki/functions/...]]`) and other **patterns** like [[wiki/patterns/disco|DISCO]].

> [!note] Source of truth
> The raw chapter pages live under `raw/docs/`. The full ingest summary is in [[wiki/sources/2026-05-04-planual]].
