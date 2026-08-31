---
title: Ragged hierarchy with per-level factors
type: pattern
tags: [anaplan, pattern, hierarchy, ragged, polaris, factor]
created: 2026-05-08
updated: 2026-05-08
sources:
  - raw/models/AAC/Modules.csv
  - raw/models/AAC/Line Items.csv
---

# Ragged hierarchy with per-level factors

A pattern for modelling N-level hierarchies where **leaves can sit at any depth** and where each level contributes a multiplicative **factor** to costs/quantities rolling up or down the tree.

Extracted from a production Polaris model that needed exactly this kind of uneven, per-level-factor hierarchy.

## When to use it

- The business hierarchy is **uneven**: some chains end at level 4, others go to level 8. Padding short chains with phantom items distorts roll-ups and inflates list size unnecessarily.
- Each level applies a **factor** (allocation key, throughput multiplier, conversion ratio, etc.) and you need both *upstream* (propagate to root) and *downstream* (project to leaves) cumulative products.
- Inputs and reports need to dimension on **one** logical hierarchy, not nine separate per-level lists.

## The shape

### Lists

1. One numbered list per level: `X_L0`, `X_L1`, …, `X_LN`. Each `X_Lk` parents to `X_L{k-1}` with `Display Name` property.
2. One **composite flat list** `X Ragged` (or `X Composite`) with all items from all levels. Set its property to a Text "Full name" and *don't* number it (codes are imported from the source).
3. One per-level **system module** `IM 0k. X_Lk` exposing the level's factor and the bridge into `X Ragged`.
4. One **composite hub module** `IM 10. X ragged` (`Applies To: X Ragged`) that does all the level-aware reasoning.

### The hub module — required line items

```
Hierarchy level (matched)   :: HIERARCHYLEVEL(<X Ragged>) - 1     -- 0..N
Level 0..N                  :: ISNOTBLANK('AN Item Lk')           -- one per level
AN Item Lk                  :: IF 'Hierarchy level (matched)' = k THEN ITEM(<X Ragged>) ELSE BLANK
AN Item combined L0-LN      :: <pick AN Item Lk by level>
Parent 1..(N-1)             :: PARENT('AN Item combined L0-LN'), then PARENT(...) of previous

AN X_Lk                     :: IF 'Level k' THEN FINDITEM('X_Lk', CODE('AN Combined item incl. parents'))
                                ELSE PARENT('AN X_L{k+1}')
                               -- top-down for matched level, otherwise inherit from level below

Factor AN X_Lk              :: 'IM 0k. X_Lk'.'Factor Lk'[LOOKUP: 'AN X_Lk']    -- with default-1 guard

Cumulative Factor Upstream  :: <product Factor AN X_L0 × ... × Factor AN X_Lk> branching by 'Hierarchy level (matched)'
Cumulative Factor Downstream :: <product Factor AN X_Lk × ... × Factor AN X_LN> branching by 'Hierarchy level (matched)'
```

### Ingest pipeline

A staging module (`LO 01. ...` in AAC) holds the raw N-column CSV (Code Level k, Name Level k, Factor Level k for every k) and computes per-row validation booleans (`Level k complete?`). Imports then create/update each `X_Lk` list from the matching staging columns; finally `Combi 01. Create X hierarchy (complete)` assembles `X Ragged` from the per-level lists. The `Create/Update X Ragged?` line item on each `IM 0k.` decides which rows to push.

## The two products: upstream vs downstream

- **Upstream cumulative factor** = product of factors from this item's level *up to root*. Use it when each ancestor's factor scales costs that arrive from below (cost roll-up: `cost_at_root = cost_at_leaf × ∏ ancestor_factors`).
- **Downstream cumulative factor** = product of factors from this item's level *down to leaves*. Use it when costs declared at this level need to be **projected down** (cost spread / re-allocation to descendants).

In practice both directions are needed: AAC uses upstream in `CA 04. UMDT on AAC Ragged` (cost roll-up) and downstream/cascading-cumulate in `RP 01. UMDT report high level` (re-projection at any chosen level).

## Filter cascade for the UX

A user-driven page selector for "show at level k, optionally constrained to a chosen ancestor" composes cleanly as a cumulative AND:

```
Filter select level 0 :: ISBLANK(<sel L0>) OR <sel L0> = 'IM 10.'.AN X_L0
Filter select level k :: 'Filter select level {k-1}'
                          AND (ISBLANK(<sel Lk>) OR <sel Lk> = 'IM 10.'.AN X_Lk)
Final combined filter :: Combined show booleans AND 'Filter select level N'
```

Each level extends the path constraint without restating the previous ones — important when N grows.

## Optional refinement: `COLLECT()` over a level LIS

Define a Line Item Subset over the per-level cumulative factors (`Cumulative Factor L0`…`Cumulative Factor LN`). A module dimensioned `X Ragged × <Level LIS>` can then write:

```
COLLECT                 :: COLLECT()
Factor at matched level :: IF <Level LIS>.Code = 'IM 10.'.'Hierarchy level (matched)'
                           THEN COLLECT ELSE 0
```

…and surface "the cumulative factor for *my own level*" without an N-deep IF chain. Pattern present in `CA 01.1 LIS AAC Ragged factors - test`.

## Engine notes

- Designed for **Polaris** — the composite list (`X Ragged`) crossed with multiple time-and-org dimensions yields multi-billion-cell intersections that are intractable on Classic. AAC's `CA 04.` is 5 B cells, `IP 01.` is 3 B cells. See [[wiki/patterns/planual/02-engine|Planual Ch.2 — Polaris]].
- `HIERARCHYLEVEL`, `FINDITEM`, `LOOKUP`, `PARENT` are all available on Polaris with the standard semantics — but verify any nuance in `.claude/skills/anaplan-formula-agent/references/classic-vs-polaris.md` before adopting.

## Pitfalls (lessons from AAC)

1. **Off-by-one in cumulative chains.** Easy to write `Cumulative L3 = Cumulative L2 × Factor L2` instead of `× Factor L3`. Audit each link explicitly.
2. **`Factor` default-1 is mandatory.** A blank/zero factor at any level wipes out the whole cumulative product. Wrap every `Factor Lk` definition with `IF Factor <> 0 THEN Factor ELSE 1`.
3. **Naming.** `Cumulative Factor L1-LN Upstream` reads as "starts at L1" but the implementation includes L0 in the product. Document the convention in the line-item Notes column.
4. **Cross-cutting LOOKUPs into deprecated modules.** AAC's `CA 04.` reads `'DEL IM 14. Artikelen'.Materiaal Groep` — deleting `DEL IM 14.` would break the calc. Trace inbound references before deleting any `DEL`-prefixed module.
5. **List size.** Per-level lists at L5..L8 are ~48k each → composite list near 50k. Acceptable on Polaris; on Classic this would be a hard stop.

## Confirmed instances

- A production Polaris model — N=8, ~48k composite items, 5 B-cell calculation.
