---
title: "Anaplan Way — Phase 1: Pre-release"
type: pattern
tags: [anaplan-way, phase, pre-release, scoping, sow, rough-cut]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
---

# Phase 1 — Pre-release

> Everything that happens before the project is formally signed. The point of this phase is to **understand enough to commit credibly**.

Three sequential activities: [Rough Cut](#rough-cut) → [Scoping](#scoping) → [SOW](#sow).

---

## Rough Cut

A first-cut **estimate of time** to have the system up and running. Built from:

- Project estimated duration
- Resource plan

Treat the Rough Cut as a sanity check before investing in scoping. If the Rough Cut signals "yes, this is feasible," move to Scoping.

---

## Scoping

A **high-level understanding of requirements**, performed *before* the SOW. The scoping deliverable feeds the SOW.

Scoping has four components:

### 1. Scope of work — process flows + business requirements

Run a **scoping workshop** that white-boards the entire process workflow Anaplan will address, **start to finish**. Identify which areas/processes Anaplan covers vs. which are out of scope.

**Required attendees**:
- **Business process owners** — understand the end-to-end process.
- **End users** — responsible for their in-scope process components.
- **Data specialists** — understand inputs, calculations, outputs.
- **Core project team**.

### 2. Data readiness and data integration

> **Never make assumptions about the customer's data.**

Best practices:

- Start the **data discussion with key customer stakeholders before the project begins**.
- **Clearly identify data sources and components** (lists, properties, hierarchies, subsets, transactional data) **in the SOW**.
- **Assign the customer homework** — production-quality data must be ready and available at project start. Get early insight into completeness, quality, integrity. Build contingencies and identify critical risks/dependencies during planning.

### 3. Level of effort

Estimate the design and build effort needed.

### 4. Environment size

Determine the workspace and tenant footprint required.

---

## SOW (Statement of Work)

If the Rough Cut + Scoping look good, formalize the project. The **SOW is a letter of intent** — a starting point for setting customer expectations, **not a rigid contract**.

The SOW defines:

- **Project-specific activities**
- **Project deliverables**
- **Project timeline**
- **Business requirements**
- **Pricing**

> [!tip] What "letter of intent" means in practice
> The SOW is the baseline against which scope changes are negotiated later (see [[wiki/patterns/anaplan-way/05-testing#triage-bugs-vs-change-requests|Phase 5 § Triage]] — change requests outside the SOW require an impact analysis, quote, and written approval).

---

## Tollgate → Foundation

Pause and evaluate before [[wiki/patterns/anaplan-way/02-foundation|Phase 2: Foundation]]:

- Is the SOW signed and clearly scoped?
- Are data sources known and committed?
- Are stakeholders identified?
