---
name: anaplan-module-mapping
description: >
  Provide dual explanations — financial/functional logic AND Anaplan technical mechanics — 
  whenever mapping, wiring, or connecting line items across Anaplan modules. Use this skill 
  whenever the user asks to connect or feed one module into another, requests cross-module 
  formulas (anything using SUM:, LOOKUP:, SELECT:, or dot-notation references across modules), 
  asks what a line item should pull from, asks to explain data flow between modules, or asks 
  why a formula is written a certain way in the context of financial statements or calculations. 
  Always apply the dual-explanation format — even for single formulas, even for "simple" references. 
  The user cannot evaluate correctness without understanding both the business intent and the 
  Anaplan mechanics; skipping either half leaves the formula unverifiable.
---

# Anaplan Module Mapping — Dual Explanation Standard

When you map or connect a line item in one Anaplan module to a source in another, always 
deliver two explanations for every formula. Do not combine them into one paragraph — keep 
them distinct so the user can read the one they need without having to parse the other.

## The Two Explanations

### 1. Financial / Functional Logic

Answer: *What does this number represent, and why should it flow from this source?*

- State what the target line item means in business or accounting terms (what it represents 
  on the P&L, balance sheet, cashflow, or other report).
- Explain why the source module is the right place to read it from — what calculation or 
  data it holds, and how that relates to the target.
- Note any classification choices that matter: why something appears on this line rather 
  than another (e.g., why hybrid interest goes to "dividend paid" rather than "interest paid"; 
  why an item is LT vs ST; why a cost appears in OPEX vs CAPEX).
- If the sign is flipped, explain the accounting convention that requires it (costs are 
  positive in a calculation module but negative on a P&L; cash outflows are negative in 
  cashflow statements, etc.).
- If the user's model uses a language the user may not be fluent in (e.g., Dutch module/LI 
  names), translate the relevant terms in plain English as part of this section.

### 2. Anaplan Technical Mechanics

Answer: *How does the formula actually work step by step?*

- Identify the dimension mismatch between source and target, and explain what aggregation 
  or lookup resolves it (SUM vs LOOKUP, and why for this specific case).
- Name the mapping line item(s) used and which module they live in — explain what each 
  one contains (e.g., "IM 13.L3 Entiteit maps each L5 Afdeling to its parent L3 entity").
- If Polaris auto-sums residual source dimensions not covered by the explicit SUM: selector, 
  call this out explicitly rather than leaving it implicit.
- Note any sign transformation in formula terms (negation, multiplication by -1, etc.) and 
  distinguish it from the financial reason for the sign (explained in part 1).
- Flag dependencies: mapping LIs that must exist before the formula can be entered, helper 
  line items that need to be pre-built in the source module, etc.
- If the formula uses a helper line item in the source module (e.g., a pre-filtered variant 
  like "Netto rentelasten ex hybride"), briefly state what that helper does rather than 
  treating it as a black box.

## Output Structure

For each target line item, follow this layout:

```
### `[Target module].[Target LI name]` — [English translation of what it means]

[Formula — paste-ready]

**Financial logic.** [Explanation: what this number is, why it comes from this source, 
sign convention, any classification choice worth knowing.]

**Anaplan mechanics.** [Explanation: dimension mismatch, what the SUM:/LOOKUP: mapping 
does, any auto-aggregation, dependencies, helper LIs.]
```

When multiple target LIs share the same aggregation pattern, you may group the mechanics 
explanation ("same SUM: pattern as above") but always write a separate financial logic 
section — the business meaning of each line is different even when the formula structure 
is identical.

## Dimension Alignment Checklist (run before writing any formula)

Before writing, resolve these in order:

1. **What dimensions does the target module have?** (e.g., FSP versies × L3 Entiteit × Year)
2. **What extra dimensions does the source module have that the target does not?** These must 
   be explicitly aggregated (SUM:) or the remaining ones will be auto-summed by Polaris.
3. **Are any target dimensions absent from the source?** These need a LOOKUP.
4. **Is the target at a parent level of the source's list?** Use SUM: with a mapping that 
   routes each child item to its parent.
5. **Is the target at a child level of the source's list?** Use LOOKUP to spread the parent 
   value to each child (or use a designated "one L5 per L3" mapping module).
6. **What summary method do source line items use?** If Sum summaries are set on a list 
   dimension, note that Polaris leverages these in cross-module aggregation.

## Sign Convention Reference

Keep these consistent across the model:

| Context | Convention |
|---|---|
| Calculation modules (CA) | Costs are **positive**; revenues are **positive** (treat separately) |
| P&L (FS 01) | Costs are **negative** (reduce profit); revenues are **positive** |
| Cashflow (FS 03) | Outflows are **negative**; inflows are **positive** |
| Rollforward / Verloopstaat (FS 04) | Items that reduce a balance are **negative**; additions are **positive** |

Always state which convention applies when explaining a negation.

## Common Mapping Scenarios

### CA (calculation) → FS 01 P&L (L5 Afdeling)
Source is typically at L3 Entiteit or a list not present in FS 01. Use `[SUM: IM 11.'Mapping X']` 
where IM 11 routes each L3 entity to one designated L5 Afdeling. If source has a subset of 
L5 already, SUM: the instrument/item dimension only — L5 aligns automatically.

### CA (calculation) → FS 03 Cashflow (L3 Entiteit)
Source often has an extra instrument or item dimension (e.g., Debt Items L2) plus L5 Afdeling 
subset. Use `[SUM: 'IM 13. L5 Afdeling'.'L3 Entiteit']` to aggregate L5 → L3; Polaris 
auto-sums the remaining extra dimension (e.g., L2).

### CA (calculation) → FS 04 Verloopstaat (L3 Entiteit)
Same pattern as FS 03. Distinguish between movement line items (additions/reductions that 
feed the rollforward formula) and position line items (closing balances). Only movements 
should be wired from CA; closing balances are computed within FS 04 from the movements.

### SUM vs LOOKUP decision rule
- **SUM:** Source list maps → Target list item (source is more granular than target, or has 
  an extra dimension being collapsed). The mapping LI lives in a module dimensioned by the 
  **source** list.
- **LOOKUP:** Target list maps → Source list item (target needs to navigate to the right row 
  in the source). The mapping LI lives in a module dimensioned by the **target** list.
