---
title: "Anaplan Way — Phase 4: Implementation"
type: pattern
tags: [anaplan-way, phase, implementation, sprints, unit-testing, performance, data-readiness]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
---

# Phase 4 — Implementation

> The build. Sprints execute the plan from Phase 3 and produce a working model that can enter testing.

Activities:

1. [Sprint execution](#sprint-execution)
2. [Project tracking](#project-tracking)
3. [Sprint meetings](#sprint-meetings)
4. [Unit testing](#unit-testing)
5. [Model performance analysis](#model-performance-analysis)
6. [Test plan](#test-plan)
7. [Data readiness](#data-readiness)
8. [Go/No-Go decision](#go-no-go-decision-to-testing)

---

## Sprint execution

- **Sprint cycles** — 2–4 weeks. Team: model builders + scrum team + 1 scrum master. Stories are sized.
- **P1 typically covers more complex features** that take longer.
- **Self-check at sprint planning**: *Can I actually get those user stories executed with the resources I have?* If no, **re-balance the buckets** — push stories to later sprints, or **deprioritize for another release**.
- **Sprint retrospective** at the end of each sprint.

## Project tracking

Use the **Anaplan Way Agile App**. Tracks:

- Product backlog
- Sprint backlog
- **Burndown chart**

## Sprint meetings

### Sprint planning meeting

- Define a **realistic sprint backlog**.
- Comes after requirements gathering.
- **First-time estimation** against user stories, then allocation into the sprint considering **Priority, Dependency, Capacity**. **Project Sponsor has the last word on priority.**
- **End result**: every story allocated.

### Daily stand-ups

15 minutes. Each member shares:

- What did you do yesterday?
- What are you doing today?
- What are the obstacles?

### Sprint reviews (end of each sprint + mini-planning)

- **Stakeholder-facing** meeting to communicate the product. Informal, **<2 hours**.
- Stakeholders give feedback on the prototype.

### All-Sprint Retrospective

- **Project Sponsor declares what's done.**
- What's not done **goes back to the product backlog** and is ranked.
- Scrum team, Project Sponsor, and stakeholders **convert feedback** into actionable items.
- **Project Sponsor reviews any new scope.**

## Unit testing

Test **each product increment during the build** against the acceptance criteria in the user story.

> **Sample / mock data must be realistic.** It should reflect production data **structure and quality**, and let the builder verify formulas easily.

## Model performance analysis

Review performance during the build. Make adjustments to organization, response time, visual appeal. **Discuss service levels with the customer** and agree on them.

### Performance baseline

- **Determine 5–7 core processes/actions** in the model — that's typically how many matter.
- **Baseline the current performance** for each.
- **Compare to desired performance.** Some processes are inherently slow — manage expectations.
- **Improve where needed** (see self-assessment below) — may take another conversation with the customer about service-level realism.

### Performance self-assessment

#### Model design

- **Module purpose** — followed [[wiki/patterns/disco|DISCO]] guidelines?
- **Dimensionality** — modules use **only the dimensions they really need**?
- **Subsets and composite lists** — only relevant dimensionality for the data?
- **Lists** — hierarchies correct? Numbered lists used where appropriate?
- **Sparsity** — may not slow performance everywhere, but adds to model size.

#### Calculations / formulas / blueprint

- Use **functions and intermediate calculations** instead of long, complex formulas. **Avoid SUM and LOOKUP in the same formula** ([Planual `2.02-08`](../planual/02-engine.md#formulas-classic)).
- Use **Booleans, especially for filtering** (Classic; in Polaris this rule doesn't carry the same memory benefit — see [[wiki/patterns/planual/02-engine#polaris|Planual § Polaris]]).
- **Summary methods + blueprint settings** — turn off what's unnecessary.

#### Model behavior / core code

May be beyond a self-assessment depending on skill. Look at configuration issues that affect performance and overall functioning. Optimize the model's "code" and assess core-level functioning.

### Model Review / Optimization test

Request via your Anaplan Business Partner. Available in **Implementation or Testing** phases — earlier is better. Average turnaround **7–10 days**.

**When to request**:

- Slow model open / long rollback times
- Specific actions or processes have become slow
- Cell-input duration has increased
- UI screens slow to load

**Results include**:

- Cause of slow performance + recommendations
- Design issues affecting performance + fixes
- Possible workarounds and best-practice advice

**Benefits**:

- Single-user baseline that performs well (better foundation for concurrency testing)
- Findings contributed to the community for shared learning
- Some issues may be shared with product design → platform improvements

### Sign-off

**Document agreed performance levels and obtain sign-off** from the project team. Email is fine. Keep with project documentation.

## Test plan

Prepare data and approach for the [[wiki/patterns/anaplan-way/05-testing|Testing phase]]. The plan establishes:

- **How testing is to be done**
- **How feedback will be documented**
- **Process for making changes based on feedback**
- **Process for retesting** if necessary

## Data readiness

Fundamental for UAT. Three options:

1. **Sample / mock data** — for functional tests.
2. **Small amount of production data** — better realism, lower risk.
3. **Actual production data imported before UAT** — most realistic, **risky**.

> **Best practice: involve the customer's CoE.**

## Go/No-Go decision (to testing)

Pre-tollgate review covering all of the above.

## Phase activity summary

- Model build and optimization
- Project tracking
- Sprint reviews and retrospectives
- Deployment readiness
- Data readiness
- Change management (continues)
- All-sprint retrospective
- **Tollgate meeting**

## See also

- [[wiki/patterns/anaplan-way/03-design|Phase 3 — Design]] (sprint plan inputs)
- [[wiki/patterns/anaplan-way/05-testing|Phase 5 — Testing]]
- [[wiki/patterns/planual/index|Planual]] — applied throughout the build
- [[wiki/patterns/planual/02-engine|Planual Ch.2 Engine]] — performance rules referenced in self-assessment
