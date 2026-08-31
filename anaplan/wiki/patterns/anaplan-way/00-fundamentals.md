---
title: "Anaplan Way — Fundamentals (Agile, Cornerstones, Scrum)"
type: pattern
tags: [anaplan-way, agile, scrum, cornerstones, fundamentals]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
---

# Anaplan Way — Fundamentals

The cross-cutting concepts. These don't live in any one phase — they apply everywhere.

---

## Agile values

The four agile values, applied to Anaplan implementations:

1. **Individuals and interactions** over processes and tools.
2. **Working software** over comprehensive documentation.
3. **Customer collaboration** over contract negotiation.
4. **Responding to change** over following a plan.

### Why agile / scrum vs waterfall

- Flexibility to adapt to **emerging or undiscovered** business needs.
- Communication and collaboration are first-class citizens.
- Delivery in **short cycles** (sprints).
- Built-in mechanism for **continual improvement** and rapid adaptation.

### Scrum process at a glance

- **Product Backlog** — repository of *all* user stories. (Tooling: a "bucket" in the Anaplan Way Agile app.)
- **Sprint Backlog** — the slice of stories committed to the current sprint.
- **Sprint cycles** — typically **2–4 weeks**, with a daily 15-min stand-up. Focus is **MVP plus incremental features** that satisfy user stories.
- **Outcome of a sprint** — a *potentially usable* product increment + sign-off on covered user stories.

---

## Cornerstones

The Anaplan Way's **four cornerstones** must be **planned, executed, and tracked in every phase**. This is the most important framing concept on the page.

### 1. Process — the business process the model supports

Clarify and document **before** the project begins. The process is the basis for collecting user stories.

- Understand the **end-to-end** process — upstream and downstream impacts.
- **Rethink and optimize** — don't just replicate the old way.
- Clean data and test data flows.
- Identify pain points and exceptions; understand inputs and outputs.
- Capture **stakeholder perspective** (high-level only? or detail-oriented?).
- Draw **swim lanes** between roles.
- Account for parallel projects that may impact this one.
- Set **clear expectations across stakeholders**.
- Use a **helicopter view** — look beyond the current process.

### 2. Data — master, meta, transactional

All data needed for the model:

- **Master data** + hierarchies are the highest-priority items.
- **Meta data** describes the context: time, version, customer, SKU, etc.
- **Transactional data** populates the model.

Critical practices:

- **Identify data sources** early.
- **Scope the dataset** before scoping the model build.
- **All data set up before UAT** — non-negotiable.
- Coordinate with other ongoing data-migration initiatives.
- Discuss **data governance** with the customer.
- **Data is the most likely reason for timeline slip.** Collect data ASAP. Loop in IT immediately.

### 3. Model — design, build, test

The Anaplan model itself.

- **At least two trained model builders on the customer staff** — they assist the build and gain experience for ongoing ownership.
- The build follows the [[wiki/patterns/planual/index|Planual]] rules and the [[wiki/patterns/disco|DISCO]] module classification.

### 4. Deployment — change management

> **Deployment IS change management.** It is fundamental to involve users and SMEs.

#### Engaging end users

- Get **influential users involved early**.
- Let influential end users **own some design decisions** — early buy-in lifts confidence in deployment.
- Run **early sneak-peeks** (e.g. during sprint reviews).
- **Consider involving a detractor** — they'll voice what others are only thinking. Converting them is high-value social proof.
- **Re-engage early-buy-in users at the end** — they become Anaplan champions.
- Engage end users **in testing**, not just at go-live.

#### Engaging SMEs

- Involve right away — **preferably in requirements gathering**.
- If they can't be constantly involved, re-engage them when the model is **~90% done** to evaluate before testing.

---

## Do's and Don'ts

### Do

- **Talk to other successful customers, partners, and Anaplan Business Partners** with experience in your use case. Get their take.
- **Rethink and optimize current processes** — leverage Anaplan's strengths, don't shoehorn legacy logic.
- **Keep it simple.**

### Don't

- **Don't replicate** a process from another system into Anaplan unchanged. It almost never works.
- **Don't try to rebuild a broken process** in the middle of building an Anaplan solution. You will fail.
- **Don't include everything in the first release** — additional iterations follow quickly.

---

## Roles — the scrum team

Roles established during [[02-foundation|Foundation]], but useful to understand here:

| Role | Description | Where it sits |
|---|---|---|
| **Project Sponsor** (business owner) | Owns ROI, vision, prioritization. Final decision on timeline, scope, user-story priority, releases. Represents stakeholders. | **Customer side** |
| **Scrum Master** | Leader without management authority. Facilitates, makes forecasts, tracks updates, shields the team from external interference. | Ideally customer side, not strictly required |
| **Scrum team** | Cross-functional team of **5–10 people**: model builders, developers, testers, analysts, designers. Full-time, self-organizing, includes customer staff. | Mixed |

---

## Risk vocabulary

- **Dirty Dozen** — Anaplan's checklist of twelve common implementation risks. Use it as a heuristic at every tollgate.
- **Tollgates** — formal checkpoints between phases (one between each pair). The team pauses, evaluates progress against goals, and decides to proceed or recalibrate.

---

## See also

- [[wiki/patterns/anaplan-way/index|Anaplan Way (hub)]]
- [[wiki/patterns/anaplan-way/02-foundation|Phase 2 — Foundation]] (where scrum team and deployment plan are formally established)
- [[wiki/patterns/planual/index|Planual]] (the build-time rulebook)
