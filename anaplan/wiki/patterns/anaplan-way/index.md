---
title: The Anaplan Way
type: pattern
tags: [anaplan, anaplan-way, methodology, project-management, agile, scrum, implementation]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
---

# The Anaplan Way

> Methodology to ensure transparency during an Anaplan implementation. **Agile by design.**

The Anaplan Way is the project-management framework for delivering an Anaplan implementation — distinct from the [[wiki/patterns/planual/index|Planual]], which governs *how to build models*. The Anaplan Way governs *how to run the project that builds them*.

## Two key concepts up-front

- **Dirty Dozen** — implementation-risk checklist (twelve common pitfalls) used to anticipate problems early. Watch for these every phase.
- **Tollgates** — checkpoints between project phases. Pause, evaluate, decide whether to proceed. Each phase has one.

## When to use this wiki section

- **Starting a project**: read the [[wiki/patterns/anaplan-way/00-fundamentals|Fundamentals]] page (agile values, cornerstones, scrum roles), then the phase pages in order.
- **Mid-project**: jump to the current phase page for a checklist of activities, decisions, and traps.
- **Reviewing implementation choices**: cross-reference [[wiki/patterns/anaplan-way/00-fundamentals#cornerstones|the four cornerstones]] — Process / Data / Model / Deployment must each be planned and tracked in **every** phase.

## Index

### [[wiki/patterns/anaplan-way/00-fundamentals|0. Fundamentals]]
Agile values, scrum roles and process, the four cornerstones (Process / Data / Model / Deployment), Do's and Don'ts.

### Phases

| # | Phase | Tollgate output | What to deliver |
|---|---|---|---|
| 1 | [[wiki/patterns/anaplan-way/01-pre-release\|Pre-release]] | Signed SOW | Rough Cut → Scoping → SOW |
| 2 | [[wiki/patterns/anaplan-way/02-foundation\|Foundation]] | Kick-off complete, scrum team established | Manifesto, deployment plan, CoE setup |
| 3 | [[wiki/patterns/anaplan-way/03-design\|Design & Process Planning]] | Sprint plan, model design reviewed | Wireframes, user stories (INVEST), model schema, sprint backlog |
| 4 | [[wiki/patterns/anaplan-way/04-implementation\|Implementation]] | Go/No-Go for testing | Built and unit-tested model, sprint reviews, performance baseline |
| 5 | [[wiki/patterns/anaplan-way/05-testing\|Testing]] | Go/No-Go for go-live | Concurrency tests, UAT, triage, exit criteria |
| 6 | [[wiki/patterns/anaplan-way/06-deployment\|Deployment / Go-Live]] | Successful adoption | Change management, training, hypercare, performance monitoring |

## Methodology in one diagram

```
PRE-RELEASE → FOUNDATION → DESIGN → IMPLEMENTATION → TESTING → DEPLOYMENT
   (Tollgate)   (Tollgate)   (Tollgate)   (Tollgate)    (Tollgate)   (Tollgate)
        ↑                                                                    ↓
        └──── 4 cornerstones tracked through every phase ───────────────────┘
              Process · Data · Model · Deployment
```

## Cross-references

- [[wiki/patterns/disco|DISCO]] — module classification used during model design (phase 3)
- [[wiki/patterns/planual/index|Planual]] — the rulebook applied during build (phase 4)
- [[wiki/patterns/planual/02-engine|Planual Ch.2 Engine]] — the performance self-assessment in phase 4 references these rules
