---
title: Composite Hierarchies
type: concept
tags: [anaplan, composite-hierarchies, lists, numbered-lists, hierarchy, dimensions, PARENT, ISANCESTOR]
created: 2026-05-13
updated: 2026-07-08
sources:
  - raw/docs/Composite hierarchies.md
  - raw/docs/List hierarchies.md
  - raw/docs/List types.md
  - raw/docs/Use numbered lists in composite hierarchies.md
  - raw/docs/Configure lists.md
---

# Composite Hierarchies

A **composite hierarchy** is a multi-level list structure built from **two or more separate lists** that each roll up to a parent list. The child list's **Parent Hierarchy** setting points to the list one level above it, creating a chain from the most granular level up to a single top-level list.

---

## Structure

```
G1 Region  (Top Level: Total Company)
    ↑  Parent Hierarchy
G2 Country
    ↑  Parent Hierarchy
G3 Location
```

In General Lists this looks like:

| List name | Top Level | Parent Hierarchy |
|---|---|---|
| G1 Region | Total Company | — |
| G2 Country | — | G1 Region |
| G3 Location | — | G2 Country |

Each list is an independent list object in the model. The **Parent Hierarchy** column creates the rollup linkage between them.

A list can participate in more than one composite hierarchy for different purposes. For example, an *Employees* list in an `<<Employee Hierarchy>>` can roll up to `G3 Location`, while `G3 Location` itself rolls up within the geographic hierarchy.

---

## Why Use a Composite Hierarchy

| Need | How composite hierarchy helps |
|---|---|
| Multi-level rollup across distinct entity types | Keeps each level as its own list (its own dimension) while enabling aggregation upward |
| Reuse of intermediate lists in multiple hierarchies | The same `G2 Country` can be a child of `G1 Region` and a parent of `G3 Location` simultaneously |
| Ragged hierarchies (different numbers of levels per branch) | Each list only needs items relevant to its level; branches can end at different depths |
| PARENT / ISANCESTOR resolution | These functions only work within a single list; composite hierarchy resolves this by making each level its own list yet keeping the parent chain navigable |

---

## How PARENT and ISANCESTOR Work in Composite Hierarchies

`PARENT` and `ISANCESTOR` in Anaplan operate **within one list**. They cannot directly traverse from an item in `G3 Location` to an item in `G1 Region` in a single call. The composite hierarchy solves this by making the parent-child relationship explicit through the **Parent Hierarchy** configuration: when a module is dimensioned by `G3 Location` with `G2 Country` as its parent, Anaplan's aggregation engine automatically rolls up through the chain.

> [!important]
> If you dimension a module by `G3 Location`, rollup values appear at the `G2 Country` and `G1 Region` levels in the module's hierarchy — but `PARENT(ITEM(G3 Location))` returns the direct parent within `G3 Location` itself (i.e., a node in the same list), not a `G2 Country` item. Cross-list navigation relies on the hierarchy configuration, not on `PARENT`/`ISANCESTOR` directly.

---

## Numbered Lists in Composite Hierarchies

Numbered lists can serve as child lists in a composite hierarchy. This is required when leaf-level items need to:
- Have duplicate display names (e.g., multiple employees with the same name across departments).
- Be keyed by an external integer identifier.
- Participate in the hierarchy without name collision.

Example:

```
Departments (named list)
    ↑  Parent Hierarchy
#Employees (numbered list)
```

Each `#Employees` item is assigned a parent from `Departments`. Because the integer index is always unique, there is no ambiguity even when display names repeat.

> [!warning]
> Converting a list that already participates in a composite hierarchy to a numbered list **removes parent list items** from the converted list (the top-level item is preserved). Plan the conversion before building out hierarchy memberships.

See [[15_numbered-lists]] for conversion rules and display name patterns.

---

## Top Level Item

The **top-most list** in a composite hierarchy carries a **Top Level Item** (e.g., `Total Company` for `G1 Region`). This item:
- Is the single rollup point for the entire hierarchy.
- Cannot hold entered data — it is always an aggregate.
- Can optionally be set as the **default page selector** in the UX.

Lower-level lists (G2, G3) do not need their own top-level item — their rollup is handled by the parent list above them.

---

## Naming Conventions

Anaplan recommends prefixing each list name with a level indicator to make the hierarchy self-documenting:

- `G1 Region`, `G2 Country`, `G3 Location` — geographic levels
- `L1 Cost Center Group`, `L2 Cost Center` — financial org levels
- `P1 Product Family`, `P2 Product`, `P3 SKU` — product levels

This makes the **Parent Hierarchy** column entries immediately readable and reduces the risk of misconfiguring the chain.

---

## Constraints and Gotchas

- **Each list is still a separate dimension.** A module can only be dimensioned by one level at a time. To show data at G3 and roll up to G1 in the same module view, the module must be dimensioned by G3 (the leaf); G1 and G2 appear as hierarchy parents in the view, not as separate dimensions.
- **Cross-list PARENT/ISANCESTOR does not work natively** — see note above. Design formulas to work at a single list level and rely on aggregation for rollups.
- **Deleting a list in the middle of a chain** will break the hierarchy for lists below it. Always remove from the bottom up.
- **Performance**: very large composite hierarchies with millions of leaf items can affect calculation and load times. Prefer fewer, wider lists over many thin levels when the intermediate levels add no analytical value.
- **Selective Access** applies per-list. If a user lacks access to items in `G2 Country`, their view of `G3 Location` items rolled up under those countries will be restricted accordingly.

---

## See Also

- [[11_lists]] — list fundamentals, types, properties, and subsets
- [[15_numbered-lists]] — integer-indexed lists; required for certain composite hierarchy leaf patterns
- [[07_dimensions]] — how lists combine with Time and Versions to define module structure
- [[Ragged hierarchy with per-level factors]] — the AAC-model ragged hierarchy pattern (per-level factors, Polaris)
