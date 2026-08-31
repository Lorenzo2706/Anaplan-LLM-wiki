---
title: "Anaplan Way — Phase 3: Design and Process Planning"
type: pattern
tags: [anaplan-way, phase, design, wireframes, user-stories, invest, model-schema, planning-poker, sprint-planning]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
---

# Phase 3 — Design and Process Planning

> Sometimes called "requirements gathering". Translates the SOW into a buildable plan.

Three families of activity, then sprint planning:

1. [Wireframing](#wireframing)
2. [Writing user stories](#writing-user-stories)
3. [Model design](#model-design)
4. [Sprint planning](#sprint-planning) — Planning Poker, sprint calculations, bucket management

---

## Wireframing

Building **mock-ups of the end-user experience** in Anaplan. This is **front-to-back model design** — focus on the data and functionality each end-user role needs.

### Useful questions

- What's the process performed in Anaplan?
- Who are the users?
- How are end users interacting with this model?
- What is the end-user's process?

### Front-to-back design flow

> **UX → modules needed → data needed → calculations → dimensions → lists**

Wireframes keep people focused on outcomes and let solution architects derive the model from there.

---

## Writing user stories

User stories are the **lowest level of detail** used to build the model's functionality. Each story describes how an end user wants to interact with the model to complete a specific task.

### Process

- **SME describes** the business process to the scrum team.
- **Scrum team helps build** the user story.
- **User-story owners** are assigned.
- **Business stakeholders own user stories** (not the build team).

### INVEST — quality criteria for a user story

| Letter | Meaning |
|---|---|
| **I**ndependent | As much as possible — can be sequenced without dependency knots |
| **N**egotiable | A starting point for conversation, not a frozen contract |
| **V**aluable | Relevant to the customer |
| **E**stimable | Developers can determine priority and effort |
| **S**mall | The longer the story, the more likely the scoping/estimation is wrong |
| **T**estable | Without testability, you can't accept it |

### Acceptance criteria

For each story:

- Define **when the feature is working correctly**.
- Written from the **user's point of view**.
- Include a **description of how it should be tested**.

### EPICs

Clusters of user stories — useful for the high-level view of project goals.

### Backlog tooling

The **"Agile Implementation — the Anaplan Way"** workspace is the recommended tool for tracking user stories.

### Coverage rule

> Capture **95% of cases** with user stories. **Don't over-focus on exceptions.**

---

## Model design

Develop the basic design of the model — data flow, lists, user inputs, calculations, output. **Use the [[wiki/patterns/disco|DISCO]] framework** for module design.

### Inputs to model design

| Input | Source |
|---|---|
| High-level business requirements | SOW |
| Who will use the model | SOW |
| How users interact with the model | Wireframes + user stories |
| How data flows through the model | Rough Cut or SOW |

### Model schema

> Best practice: create a **model schema** that captures the design. Anaplan recommends **Lucidchart**.

Schema-building process:

- Determine **output modules** based on wireframes.
- Determine **how to transform inputs into outputs** (Data Hub involvement?).
- Determine **dimensions** and **data flows** required.
- The schema is a **flexible roadmap** to build the model — not a frozen blueprint.

### Preparing the data for integration

- **Assign accountability** for the data work-stream to a specific customer-team member. The customer must hold them accountable throughout.
- **Start small, focus on data quality.**
- **Bring in expert help for data cleaning** if it makes sense — many organizations supplement with external data tools.
- **Automate later.** Begin with **manual uploads**. Lack of automation won't stop the project; **poor data will.**
- **Add data tasks as user stories** so they show up in the backlog (track in the Agile Implementation app).
- **Pay as much attention to data as to the model build.**

### Model design review

Best practices:

- **Schedule a check-in** with your Business Partner or a more experienced model builder. Send the **model schema link** with the meeting invitation.
- Prepare by completing the **Model Design Check-in Checklist**. During the meeting, describe the **customer perspective**, show your **schema**, and explain how the model solves the customer problem.
- **Listen** to the changes the reviewer proposes.
- **Document** the meeting — keep a copy of the checklist in project files.

---

## Sprint planning

Turning customer requirements into a plan for executing the model build during the [[wiki/patterns/anaplan-way/04-implementation|Implementation phase]]. Two activities:

### 1. Estimating effort — Planning Poker

The **standard agile approach** to effort estimation.

#### Why Planning Poker

- **Builds team engagement** — collaborative, defines roles, can be fun.
- **Diverse perspectives** — multiple heads beat one. Encourages **independent** thinking before consensus.
- **Consistency** — produces a consensus estimate and an agreed unit of measurement. Easier to recalculate sprints if estimates miss.
- **Tests user-story quality** — wide ranges flag stories that are unclear, missing info, or too large. Better to find out *now*.

#### Process

1. **Establish complexity levels** for user stories.
2. Pick a story with **medium complexity** to **estimate first** — this becomes the baseline.
3. Assign a **unit value** (e.g. a 1–5 numeric scale).
4. Use that value as the **baseline** for the rest of the stories.
5. **Estimate independently**, then compare and reach consensus before moving on. The discussion itself surfaces insights. **Clients must be on board** — they know their data and process.
6. The **Anaplan Way app has a dedicated dashboard** to support this.
7. If the client is unfamiliar with poker, use **High / Medium / Low** sizing first.

#### Effort matrix (canonical Anaplan Way table)

| Time Intensive \\ Build Complexity | Low | Medium | High |
|---|---|---|---|
| **Low** | 1/2 | 1 | 3 |
| **Medium** | 2 | 8 | 13 |
| **High** | 5 | 20 | 40 |

> **Baseline IS NOT a straight estimate of time** — it's an estimate of *complexity and effort* that **equates** to time. Subtle but important.
>
> Examples (from the table):
> - Medium complexity × Medium time = **8 points**
> - Medium complexity × Low time = **2 points**
> - Medium complexity × High time = **20 points**
>
> After Planning Poker, **develop a consensus estimate** of the time the baseline story will take, then **translate points → development hours via a multiplier.**

### 2. Sprint calculations

#### Total development capacity

```
Total dev capacity = (model builders) × (length of Implementation phase)
```

Example: 5 builders × 40 h/week × 8 weeks = **1600 hours of development time**.

> **Account for review and testing time** as you determine capacity — not just raw build hours.

#### Priorities (assigned by the Project Sponsor)

| Priority | Meaning |
|---|---|
| 1 | Must complete in the first **two sprints** |
| 2 | Important — current release |
| 3 | Useful — current release if possible |
| 4 | Backlog (default for stories not assigned 1/2/3) |

> Watch dependencies — a P1 story that depends on something assigned P3 is **blocked** until you re-prioritize.

#### Buckets

- **Master Bucket** — initial repository of *all* user stories.
- After Planning Poker (sizing) and prioritization, stories are placed into **Sprint Buckets**.

#### Managing the buckets

The art of allocating stories into sprints based on priority and total dev capacity. Three balancing levers:

- **Timeline** — sprint length.
- **Resources** — people allocated to the sprint.
- **Scope (user stories)** — stories can be moved across sprints.

> The "Managing the Buckets" conversation **controls scope creep** and revisits priorities when re-planning sprints. As long as priorities are correct and **everyone agrees the bucket plan represents a good Release 1** (good enough, not perfect), you've managed the buckets.

---

## Tollgate → Implementation

Before sprints begin:

- Wireframes and user stories complete and INVEST-compliant?
- Model schema reviewed by an experienced builder?
- All stories sized via Planning Poker?
- Sprint buckets allocated within total dev capacity?
- Data work-stream owner identified on the customer side?

## See also

- [[wiki/patterns/disco|DISCO]] — module classification framework used in model design
- [[wiki/patterns/planual/index|Planual]] — the rulebook applied during the build
- [[wiki/patterns/anaplan-way/04-implementation|Phase 4 — Implementation]]
