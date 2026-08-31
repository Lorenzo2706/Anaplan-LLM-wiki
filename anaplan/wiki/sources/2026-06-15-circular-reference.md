---
title: Circular Reference — Community Threads (3 discussions)
type: source
tags: [anaplan, circular-reference, workaround, community, formula]
created: 2026-06-15
updated: 2026-06-15
sources:
  - raw/docs/circular reference Volumes.md
  - raw/docs/How to avoid Circular Reference.md
  - raw/docs/Avoiding Circular Reference.md
---

# Circular Reference — Community Threads (3 discussions)

Three Anaplan Community discussions on circular reference errors, grouped as a single ingest because they cover the same root problem from complementary angles.

## Sources

| File | Original URL | Published |
|---|---|---|
| `circular reference Volumes.md` | https://community.anaplan.com/discussion/160828/ | 2025-08-23 |
| `How to avoid Circular Reference.md` | https://community.anaplan.com/discussion/139009/ | 2022-06-02 |
| `Avoiding Circular Reference.md` | https://community.anaplan.com/discussion/156120/ | 2023-07-04 |

## Key takeaways

**Thread 1 — "Circular reference: Volumes"** (2025-08-23): A user hitting a circular reference when pulling `DATA02 SKU Volumes.Volumes` into `REV02 Volumes Inputs`. Community response confirms the root cause: the output of the source module is informing the outcome of the target, completing a loop. Diagnostic advice: check both the target *and* source formulas for indirect references.

**Thread 2 — "How to avoid Circular Reference"** (2022-06-02): The most technically detailed thread. A user needs a cumulative/running calculation where each period's result depends on the previous period's result (`PREVIOUS(Result)`). The standard `PREVIOUS()` in a single-block module creates a circular dependency on the inputs. **Solution**: the **Fake Time list pattern** — create a custom list mirroring native Time, build a CALC module on `Fake Months × native Time (Day)`, run `PREVIOUS()` within that separate block, and LOOKUP the result back. Includes step-by-step module setup with SYS mapping modules.

**Thread 3 — "Avoiding Circular Reference"** (2023-07-04): A manufacturing plant scenario where `Transfer Out` from Plant A becomes `Transfer In` for Plant B. Even though the calculation is not logically recursive, Anaplan flags the line items as circular because the dependency check is at the line-item level, not the list-member level. **Solutions proposed**: (a) SYS Plants LOOKUP mapping; (b) time-axis substitution using PREVIOUS() on a per-member time-period proxy.

## Wiki pages created/updated

- [[wiki/patterns/circular-reference]] — new pattern page with all three workarounds documented
