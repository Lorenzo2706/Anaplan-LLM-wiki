---
title: "Anaplan Way — Phase 6: Deployment / Go-Live"
type: pattern
tags: [anaplan-way, phase, deployment, go-live, change-management, training, hypercare, monitoring]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Way.md
---

# Phase 6 — Deployment / Go-Live

> **Deployment is both a cornerstone and a phase.** It must be top-of-mind during *every* phase — if you wait until it's time to deploy, it's too late.

After go-live, the project enters **warranty / hypercare** for a defined period.

## Deployment plan — objectives

The plan is developed early on with the customer (started in [[wiki/patterns/anaplan-way/02-foundation#deployment-plan|Phase 2]]). Three objectives:

### 1. Get buy-in from users

#### Engage end users

- **Influential users involved early.**
- **Let them own some design decisions** — early buy-in boosts confidence.
- **Sneak-peeks at the model** — for example, during sprint reviews.
- **Re-engage early-buy-in users at the end** — they become **Anaplan champions**.

#### Involve respected SMEs

- **Right away** — preferably in requirements gathering during Foundation.
- **Re-engage at ~90% completion** if they can't be constantly involved.
- Involvement reinforces **joint ownership** of the solution.

### 2. Make the Anaplan process stick in the organization

Deployment is change management. Without adoption, ROI evaporates.

### 3. Secure ROI for the customer

The whole point of the implementation.

---

## Change management activities

Three pillars: **Communication**, **Training**, **Documentation**.

### Communication

Work with the **Project Sponsor** to create a **communication plan early** in the project.

#### The plan must cover

- **Overall communication goal**
- **Audience**
- **Communication objective**
- **Message**
- **Communication channel**
- **Timing**

#### Best practices

- **Good communication can eliminate end-user excuses** for not adopting the solution.
- **Tailor the message to the audience** — communication to end users ≠ to managers ≠ to C-Levels.
- **Over-communication is a good approach.**
- **Status reporting** to executives or a Steering Committee is critical. Big projects often have a customer template; if not, you provide one.

### Training

> Critical change-management activity for ensuring **user adoption and ROI**.

#### Best practices

- **Train-the-trainer** — solution architect trains super-users; super-users train end users.
- **Video and/or step-by-step e2e documentation** is effective.
- **Hold meetings with demos.**
- **Customer building their own training material** is great when it happens (rare).
- **Visit end users**, especially if geographically dispersed.
- **L1 model-builder training early on** for customer model builders.
- **Schedule end-user training close to go-live** — avoids users forgetting how to use the system.
- **Super-users in UAT must be trained early.**

### Documentation

Provides a **lasting record** that supports future releases and new use cases. Keep it in a **collaborative, secured folder**.

Anaplan and/or the partner Project Manager + the customer Project Manager are responsible for creating, maintaining, and distributing:

- **Overall model schema**
- **Regional and business-unit model schemas**
- **Data and metadata schemas + processes** documentation
- **Model maintenance** documentation
- **Model data flow**
- **Base model blueprints**
- **FAQs**

---

## Monitor performance

After go-live, monitor performance to ensure goals are met for **adoption, customer experience, and service levels**.

### When monitoring is required

Monitor an app when **one or more** of the following holds:

- **High volume**
- **High complexity**
- **High concurrency**

### The Anaplan Performance App

Create an **Anaplan performance app** to monitor performance. Determine:

- **Frequency of monitoring**
- **Audience**
- **Clear translations of the data** for the project team

### Metrics — capture Min / Max / Average / Median for

- **Model load time**
- **Model save time**
- **Toaster time**
- **Response time by object** (in milliseconds):
  - Dashboards
  - Modules
  - Large calculations
  - List loads
  - Actions
  - Processes
  - User

### Sharing performance data

> **Establish SLAs first**, then share. Be selective about who receives statistics — some need translation before they're useful.

---

## See also

- [[wiki/patterns/anaplan-way/00-fundamentals#cornerstone-4-deployment-change-management|Fundamentals § Deployment cornerstone]]
- [[wiki/patterns/anaplan-way/02-foundation#deployment-plan|Phase 2 — Deployment plan setup]]
- [[wiki/patterns/anaplan-way/05-testing|Phase 5 — Testing]] (where the go/no-go is decided)
