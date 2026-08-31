---
title: "Planual Chapter 6 — Application Lifecycle Management"
type: pattern
tags: [anaplan, planual, alm, revision-tags, production-lists, deployed-mode]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Revision tags  Anaplan Support.md
  - raw/docs/Production lists  Anaplan Support.md
  - raw/docs/Anaplan Support 19.md
  - raw/docs/Deployed mode  Anaplan Support.md
  - raw/docs/Managing changes during development.md
---

# Chapter 6 — Application Lifecycle Management (ALM)

> ALM (Professional and Enterprise subscriptions) controls development, testing, deployment, and ongoing enhancement of models.

Sub-sections: [Revision tags](#revision-tags) · [Production lists](#production-lists) · [Architecture](#architecture) · [Deployed mode](#deployed-mode) · [Managing changes during development](#managing-changes-during-development)

---

## Revision tags

- **Naming**: be consistent — `Major.Minor` works well (`R1.01`, `R1.02`, `R2`). The description is **permanent** — can't be changed afterward.
- **Tag often during intense development** — and test each tag against a "shell" model.
- **For richer revision history**, create a non-production list and store revision details (Approved date, User Story, Developer, Tested date, Sign-off date) in a module dimensioned by it.
- **Sync regularly** — keeps Production and Development aligned, minimizing synchronization-error risk.
- **Shell model** (`create from revision`, no production members) is the safe place to test revisions and iterate.

## Production lists

Production lists let end users add/edit list members without breaking the ALM sync of the structure.

- **Don't set every list to Production Data initially.** Switching back to Structural after a sync **wipes** existing Production list data even when members are identical.
- **No hard-coded references** to items in a Production Data list — that member could be deleted by an end user. (Cross-link: `6.02-02 Formula protection — Hard-coding`.)
- **Only flag a list as Production Data** when it's modified by the business process or by imports.
- **Audit before flagging**: review the list's `Referenced by` column — hard-coded formula references will cause sync rollbacks.

## Architecture

The single rule that matters more than all the others: **stay in Deployed mode**.

- **Once ALM is initiated and Deployed mode is on, Production should never come out of Deployed mode.**
  - **`6.03-01a`** Exception: when copying a Production model to seed an initial ALM environment, or when re-creating Dev as part of a "reset".
  - **`6.03-01b` There are no other exceptions.** ALM brings control; Deployed mode is the keystone.
- **Dev models can also be in Deployed mode** — prevents inadvertent structural changes outside normal dev cycles.
- **Test models = Production models.** Treat Test as Production: gives accurate UAT, prevents accidental Test→Prod sync.

## Deployed mode

- **Revert-fix-sync-restore technique**: revert Dev to a prior revision, make the fix, sync to Prod, then bring Dev back to where it was. Works only on **existing** line items, not net-new line items introduced in the fix revision.
- **After a revision, create multiple revision tags with different switchover dates** before starting new development.
- **Master dashboards (Classic only)** delete users' personal dashboards. Mitigation: copy + migrate users to the new dashboards. *Note: no longer applies to the current UX.*

## Managing changes during development

### Topology

- **DEV → Test and DEV → Prod** is more flexible than chaining. Multiple Test models can be spun up/torn down without compromising Prod. **Always sync from Dev to the target** to maintain segregation of duties.
- **Compatible models can be archived** without breaking the ALM link.
- **Restoring an archive**: bring it back into Deployed mode if the archive was Production or Test.

### Dev model size

- **Keep the Dev model small.** Use only a slice of production-list members. Use **`create from revision`** to seed Dev.
- **Don't `create from revision` *from* a Production model** — it creates a new revision in Prod that's then out of sync with Dev.
- **Use Data Hub saved views** to populate Dev — defines the data and structures needed for build and component testing.

---

## See also

- [[wiki/patterns/planual/01-central-library|Chapter 1 § Lists]] — list design upstream of Production-list flagging
- [[wiki/patterns/planual/05-integration|Chapter 5 § Source models]] — Dev/source-model cleanup
