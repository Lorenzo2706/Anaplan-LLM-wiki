---
title: "Anaplan Way — methodology document (full ingest)"
type: source
tags: [anaplan-way, methodology, source-summary]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
  - raw/assets/Anaplan Way.png
---

# Source — The Anaplan Way

A single comprehensive methodology document (~480 lines) covering the full Anaplan implementation framework: agile/scrum foundations, four cornerstones, six phases, change management, and monitoring.

## What it is

**The Anaplan Way** is the project-management methodology Anaplan and its partners use to deliver implementations. It complements (does not overlap) the [[wiki/patterns/planual/index|Planual]]:

- **Planual** = how to *build* models (rules)
- **Anaplan Way** = how to *deliver* the project that builds them (process)

## Wiki mapping

The single raw document was decomposed into **8 wiki pages** mirroring its structure (hub + fundamentals + 6 phases):

| Wiki page | Source content |
|---|---|
| [[wiki/patterns/anaplan-way/index\|Hub]] | Methodology overview, agile values, dirty dozen, tollgates, phase index |
| [[wiki/patterns/anaplan-way/00-fundamentals\|Fundamentals]] | Agile values, scrum process, 4 cornerstones (Process / Data / Model / Deployment), Do/Don't, scrum roles |
| [[wiki/patterns/anaplan-way/01-pre-release\|Phase 1 — Pre-release]] | Rough Cut, Scoping, SOW |
| [[wiki/patterns/anaplan-way/02-foundation\|Phase 2 — Foundation]] | Project planning, kick-off, manifesto, scrum team, deployment plan, CoE setup |
| [[wiki/patterns/anaplan-way/03-design\|Phase 3 — Design]] | Wireframing, user stories (INVEST/EPICs/AC), model design, sprint planning (Planning Poker, sprint calculations, bucket management) |
| [[wiki/patterns/anaplan-way/04-implementation\|Phase 4 — Implementation]] | Sprint execution, project tracking, sprint meetings, unit testing, performance analysis + self-assessment, test plan, data readiness |
| [[wiki/patterns/anaplan-way/05-testing\|Phase 5 — Testing]] | Testing bench, scripts (auto + UAT), concurrency testing, UAT, triage, exit criteria, go/no-go |
| [[wiki/patterns/anaplan-way/06-deployment\|Phase 6 — Deployment]] | Deployment objectives, change management (communication / training / documentation), monitoring, performance app |

## Key concepts captured

- **PLANS** is the Planual's design philosophy; the Anaplan Way's analogous lens is the **4 cornerstones** (Process, Data, Model, Deployment) tracked through every phase.
- **Tollgates** are the formal go/no-go checkpoints between phases.
- **Dirty Dozen** — Anaplan's 12-item implementation-risk checklist (referenced in source; specific items not enumerated in this clipping).
- **Planning Poker effort matrix** captured in [[wiki/patterns/anaplan-way/03-design#effort-matrix-canonical-anaplan-way-table|Phase 3]].
- **Triage severity levels (L1/L2/L3)** for bugs vs change requests captured in [[wiki/patterns/anaplan-way/05-testing#severity-levels|Phase 5]].
- **Performance app metrics** (Min/Max/Avg/Median for load, save, response by object) captured in [[wiki/patterns/anaplan-way/06-deployment#metrics-capture-min-max-average-median-for|Phase 6]].

## Cross-references created

- → [[wiki/patterns/disco|DISCO]] — module classification (used in design + performance self-assessment)
- → [[wiki/patterns/planual/index|Planual]] hub — applied throughout the build phase
- → [[wiki/patterns/planual/02-engine|Planual Ch.2 Engine]] — performance self-assessment references SUM+LOOKUP rule, Boolean optimization, etc.
- → [[wiki/patterns/planual/05-integration#data-hub|Planual § Data Hub]] — referenced from CoE setup

## Notes / open items

- The raw document references "**Dirty Dozen**" without enumerating the 12 items. If a separate clipping listing them is added later, link from the [[wiki/patterns/anaplan-way/index#two-key-concepts-up-front|hub]].
- The raw document includes embedded OneNote links (`onenote:#...`) for "Implementation Phase" and "Testing Summary" — these are local to the original author's notebook and aren't reachable from the wiki.
- Asset: `raw/assets/Anaplan Way.png` (referenced at the end of the source).
