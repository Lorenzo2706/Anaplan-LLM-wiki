---
title: Circular Reference — Patterns & Workarounds
type: pattern
tags: [anaplan, circular-reference, formula, workaround, polaris, classic]
created: 2026-06-15
updated: 2026-07-08
sources:
  - raw/docs/circular reference Volumes.md
  - raw/docs/How to avoid Circular Reference.md
  - raw/docs/Avoiding Circular Reference.md
---

# Circular Reference — Patterns & Workarounds

Anaplan blocks circular references entirely. Because the engine recalculates all values whenever an input changes, it requires a strictly directed acyclic graph (DAG) of dependencies — no formula can directly or indirectly depend on its own result.

---

## What triggers the error

A **circular reference** occurs when:
1. **Direct loop**: Module A references Module B, and Module B references Module A (or the same line item references itself).
2. **Indirect loop**: A → B → C → A across multiple modules or line items.
3. **False/apparent circular**: A formula on list member X reads from the same line item on member Y, which in turn reads from member X. Anaplan sees the line item referencing itself even though the calculation is not actually recursive in practice (e.g., Plant 1 → Plant 2 → Plant 1 across different members of the same list).

> [!important]
> Anaplan does **not** check that list members differ — it evaluates dependency at the line-item level. A formula like `Transfer In = [LOOKUP: Source Plant].Transfer Out` still triggers a circular reference if `Transfer In` and `Transfer Out` live in the same module and the mapping can produce a self-reference.

---

## Common scenarios

### 1 — Cross-module feed creating a loop

The simplest case: `DATA02.Volumes` references `REV02 Volumes Inputs`, and `REV02 Volumes Inputs` references back `DATA02.Volumes`. Check the full reference chain, not just the immediate formula.

**Fix**: Break the chain by introducing an intermediate staging module, or by restructuring so data flows in one direction only (consistent with [[wiki/patterns/disco|DISCO]] — Data → Inputs → Calculations → Outputs).

---

### 2 — Cumulative/running calculation using PREVIOUS()

`PREVIOUS(Result)` refers to the prior time period of the same line item. If the same module also computes the inputs used in `Result`, Anaplan interprets this as a self-reference within the block — circular reference.

**Root cause**: Anaplan's block structure groups line items by their dimension signature. A module dimensionalized by native Time (Month) with a formula that reads `PREVIOUS(self)` is fine *only* if there is no other line item in the same block whose value feeds back into `self`. When the input and the running total share the same dimensional block, the loop is flagged.

**Workaround — Fake Time list pattern** (see source: [[wiki/sources/2026-06-15-circular-reference|Community thread — How to avoid Circular Reference]]):

The approach uses a *custom list that mirrors native Time* as a stand-in dimension, allowing the PREVIOUS() accumulation to run in a separate block. High-level steps:

1. **Create a `Fake Months` list** with one item per month in the model calendar (names matching native Time exactly to simplify FINDITEM lookups).

2. **Create `SYS Months Properties`** (dimensioned by native Time):
   - `Item Txt = NAME(ITEM(Time))`
   - `Link to Fake Months = FINDITEM(Fake Months, Item Txt)`

3. **Create `SYS Fake Months`** (dimensioned by Fake Months):
   - `Item Txt = NAME(ITEM(Fake Months))`
   - `Time List = FINDITEM(Time, Item Txt)`

4. **Create `SYS Filter Days`** (dimensioned by native Time at **Day** granularity, one-year Time Range):
   - `Date = START()` (Timescale: Day)

5. **Create `SYS Index Properties`** (dimensioned by your row-count list, e.g. 1–256):
   - `Days` (Date format) — paste the day dates from `SYS Filter Days` as static data.

6. **Create `CALC Circular`** (dimensioned by **Fake Months × native Time**, Timescale: Day, one-year TR). Because Fake Months and native Time are *different* dimensions, PREVIOUS() here operates in a separate block — no circular reference:
   - `Sales Premium = Source Module.Sales Premium[LOOKUP: SYS Fake Months.Time List, LOOKUP: SYS Filter Days.Row Count List]`
   - `Sales to Info = Source Module.Sales to Info[LOOKUP: …]` (same pattern)
   - `Result = IF 'SYS Filter Days'.First Member? THEN Sales Premium * Sales to Info ELSE Sales Premium * Sales to Info + PREVIOUS(Result) * Persistency Result`

7. **Back in the original module** (dimensioned by native Time × row-count index):
   - `Result = CALC Circular.Result[LOOKUP: SYS Row Count.Day, LOOKUP: SYS Months.Link to Fake Months]`

> [!note] Why this works
> The accumulation in `CALC Circular` lives in a block whose row dimension is **Fake Months** (a list), not native Time. PREVIOUS() steps along the *native Time* day axis within that block. Because the two blocks are separate, Anaplan sees no loop even though the result is eventually mapped back to the original module via LOOKUP.

---

### 3 — List-member-to-member transfer (apparent circular)

Scenario: a list of Manufacturing Plants where `Transfer Out` from Plant 1 becomes `Transfer In` for Plant 2. The formula `Transfer In[Plant Y] = Transfer Out[Plant X]` references the same line item on a different list member — Anaplan flags this as circular because the dependency is at the line-item level, not the member level.

**Workaround A — SYS module LOOKUP**:
Create a `SYS Plants` module that stores, for each plant, a list-formatted line item pointing to its *source* plant. Then:
```
Transfer In = 'Calculation Module'.Transfer Out[LOOKUP: 'SYS Plants'.Source Plant]
```
This makes the dependency explicit via a mapping rather than a self-referential formula.

**Workaround B — Time-axis substitution**:
If no time dimension is needed for the actual calculation, map each list member to a time period (e.g., Transfer 1 → Week 1, Transfer 2 → Week 2). Run all calculations on the time dimension using PREVIOUS(), then LOOKUP the results back to the list dimension. This mirrors the Fake Time pattern above.

---

## Decision guide

| Scenario | Recommended workaround |
|---|---|
| Direct cross-module loop | Restructure data flow (DISCO DAG) |
| Running/cumulative total needs PREVIOUS() | Fake Time list + CALC module in separate block |
| Same-LI formula across different list members | SYS mapping module + LOOKUP |
| No time needed; list-member ordering matters | Map members → Time periods; use PREVIOUS() on time |

---

## Cross-references

- [[wiki/patterns/disco|DISCO — Module Classification]] — structuring modules to avoid accidental loops
- [[wiki/functions/categories/time-and-date|PREVIOUS()]] — time-stepping function at the center of workaround 2
- [[wiki/functions/categories/misc|FINDITEM()]] — used in the Fake Time mapping modules
- [[wiki/functions/categories/mapping|LOOKUP]] — used to map Fake Time results back to native dimensions
