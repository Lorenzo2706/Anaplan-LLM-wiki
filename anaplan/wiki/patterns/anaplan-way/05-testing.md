---
title: "Anaplan Way — Phase 5: Testing"
type: pattern
tags: [anaplan-way, phase, testing, uat, concurrency, triage, change-requests]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
---

# Phase 5 — Testing

> Verify that the model meets the acceptance criteria, performs under realistic load, and is ready for go-live.

Activities:

1. [Set up the testing bench](#set-up-the-testing-bench)
2. [Test scripts (automated + UAT)](#test-scripts)
3. [Automated concurrency testing](#automated-concurrency-testing)
4. [UAT](#uat)
5. [Triage — bugs vs change requests](#triage-bugs-vs-change-requests)
6. [Go/No-Go for go-live](#gono-go-for-go-live)

---

## Set up the testing bench

Define scripts, look up SLAs, clarify acceptance criteria, perform performance testing.

### Best practices

- **Overestimate prep time** — writing scripts and preparing data takes longer than expected.
- **Send meeting invitations in advance.**
- **Communicate project scope properly and in time** — to all levels, including end users.
- **Allow enough time** to run testing and make model adjustments.
- **Identify testable criteria up front** — as early as user-story writing during Foundation.
- **Identify individuals for live testing (UAT).**
- **Identify potential hurdles** — technical limitations, global audience, localization.

## Test scripts

> **Test scripts are required for both automated and human testing.**

### For automated testing

- The project team completes a **Model Interaction Specification** document — captures detailed information on **how each user type interacts with the model** as part of regular duties. This enables the **model concurrency team** to create test scripts that simulate concurrent interaction realistically.

### For UAT

- The project team writes **step-by-step instructions** ("UAT test scripts") for users to follow, assessing whether **acceptance criteria are met** for each user story.
- **Broader end-to-end process flow testing** should also be captured in the scripts.

### Writing scripts — required components

- The **user story** being tested.
- Clear **success criteria** — broad description of what the test should achieve and how it fits the business need.
- **Pre-requisites** — anything the user must complete before executing (e.g. login, environment prep).
- **Known behaviors** that may affect completion — intermittent bugs, undefined behavior.
- A **step-by-step script in tabulated form**:

| Column | Purpose |
|---|---|
| **Step number** | Sequencing |
| **Step description** | What the tester does |
| Requirements mapping (if applicable) | The Requirement ID this step maps to — not all steps need one |
| **Comments** | Where the tester records observations ("could not find that option / could not click that button") |
| **Pass / Fail** | Test result |

## Automated concurrency testing

Automated testing of **peak load, stress, and concurrency** on model performance. Goal: simulate real-world concurrent usage.

> **Not always required.** Some projects skip it.

### Engagement rules

- **Request at the very start of the implementation project** so milestones can be agreed and inputs scheduled.
- Contact the **Customer Success Business Partner** to engage the model concurrency team.
- **Single-user (or 2–3 user) functionality and performance must already be verified/optimized** before concurrency testing — issues observed at low concurrency get **significantly amplified** at high concurrency.
- Project duration ranges **1.5 to 4 weeks** depending on variables.

### Targets and customer requirements

- **90th or 95th percentile target response times** for each transaction. *Typical goal: ≤2 seconds on popular requests at normal concurrency.*
- **Expected load volumes** by end users (pacing).
- **Concurrency level of the user base** — typically **15%–20%**.

### Model sanitization

Manipulate model data to values that don't identify any company, person, precise location, company plan, or sensitive financial data.

## UAT

> Live testing matters because **humans notice usability issues machines won't** — confusing charts, unclear text, unexpected behavior under "off-script" use.

### Capture beyond functionality

- Use of the model **with different bandwidths**
- Different **operating systems**
- **Location** differences
- **Browser** compatibility

### Best practices for UAT

- **Test every user story.**
- **Test the end-to-end flow.**
- **Test the admin path** too.
- If possible, test a **real-world scenario**.
- **Incorporate training into testing** — kills two birds.
- **Limit users involved** to those who provide the best inputs.
- **Formal go/no-go meeting** at the end of UAT.
- **Daily UAT Q&A meetings** for testers — end-of-day reviews.
- **Set expectations before testing begins.**
- **At least 1 week** of UAT.
- **No more than 20 steps per script** — keep it simple.

### Preparing for UAT

- **Agree which actions** are in each test script and the steps testers will follow.
- **Write scripts one sprint behind** — in sprint two, write scripts for sprint one's stories.
- **Testable data loaded in advance** — production-quality and production-quantity.
- **Roles + selective access** defined; assign appropriate testers to each role.
- **Create a presentation** to guide users on test day.
- **Everyone online** — testers, project team, Anaplan consultants.
- **Provide basic Anaplan end-user training before UAT** — reduces "bugs" caused by user unfamiliarity.
- **Consultants watch Splunk reports + server log files** throughout testing.

### User survey

Questions cover conditions during testing — internet connectivity, speed variations, performance over the testing window.

> **Skip the survey only if you already know performance is poor.** As a general rule, conduct human testing **only when results are expected to be acceptable**. Major system issues should be eliminated in **automated testing**, not UAT.

## Triage — bugs vs change requests

Feedback from testing produces **bugs (defects)** to fix or **change requests (enhancements)** to add to the Product Backlog.

### Triage committee

- **Anaplan Business Partner**
- **Solution Architect** (partner or Anaplan)
- **Customer SME**
- **Project Sponsor**

The committee:

- Classifies feedback as **bug or change request**.
- Assigns a **severity level**.

### Severity levels

| Level | Bug | Change Request |
|---|---|---|
| **L1** | Must fix in next UAT | Show-stopper functionality — must have in current release |
| **L2** | Must fix and include in current release | Desirable; include in current release if possible |
| **L3** | Desirable; may defer to a future release | Likely in a future release |

### Fixing bugs

Determine time and resources needed to fix bugs so the customer can complete UAT. **If many L1 bugs exist and fixing them is extensive, lower-level bugs are pushed to the next release.** Reference the **UAT exit criteria** as the guide.

### Adding change requests

> Every customer's SOW contains the requirements for the model and the procedures for incorporating changes.

When testing feedback is **out of SOW scope**:

- Anaplan or the implementation partner notifies the customer with:
  - **Impact analysis**
  - **Quote** for additional work
  - **Action plan** for handling the request
- **All change requests must be mutually approved in writing** before scope-change work begins.

Prioritize change requests by severity. **Show-stoppers** get top priority; less severe ones may become part of the next release.

### UAT exit criteria

Often a team decision: a **percentage of L1 bugs and a percentage of L1 change requests** that must be completed before UAT exits.

## Go/No-Go for go-live

> **Schedule the Go/No-Go meeting well in advance** — mitigates calendar conflicts as the date approaches and gives the team a fixed completion target.

## See also

- [[wiki/patterns/anaplan-way/04-implementation|Phase 4 — Implementation]] (test plan and data readiness preparation)
- [[wiki/patterns/anaplan-way/06-deployment|Phase 6 — Deployment]]
