---
title: Configuring a Network (Exercise 16)
type: concept
tags: [anaplan, demand-supply-chain-app, inventory, network, supply-planning]
created: 2026-05-12
updated: 2026-05-12
sources: [raw/docs/16 Configuring a Network.md]
---

# Configuring a Network

## Purpose

Extend the inventory plan from independent DC replenishment into a **multi-tiered distribution network**, where some DCs supply other DCs rather than sourcing externally. In the worked example, a **Central DC** replenishes the **North** and **South** DCs; the Central DC therefore sees two demand streams (direct customer demand + replenishment demand from North/South), and its own replenishment becomes the signal to production.

Without this step, DC-level replenishment requirements are open-ended — the model knows each DC needs inventory but not where it comes from. Network configuration closes that loop.

## Configuration steps

### 1. Create empty list placeholders (page 904)

Run the **Create Location Related Lists** process to pre-create placeholder list items for transfer lanes. The app pattern is to populate existing placeholders rather than have planners add list items directly (see the broader app convention of placeholder-driven planning inputs).

### 2. Define transfer lanes (page 910)

On the **Manage Transfer Lanes** page:

- Each lane is a **child of the destination DC** (the DC receiving inventory).
- Select the **"From DC"** (source of inventory) — e.g. Central -> North, Central -> South.
- Set the **routine disaggregation %** per lane: how much of the destination DC's replenishment requirement is met through this lane. In the example, 100% of North's and 100% of South's replenishment comes from Central.
- Select the **transit mode** (e.g. road), which governs which lead time applies.

### 3. Set lead times (page 912)

On the **Edit Lead Times** page, input the lead time for each lane / transit mode combination — e.g. **1 period (1 week)** for road transit Central -> North/South. The lead time offsets ship date at source vs receipt date at destination.

### 4. Validate flows (page 222 — Inventory Transfers)

After selecting the correct scenario and DC filter:

- Each lane shows weekly volume flowing through it.
- Volumes are timestamped at **receipt into destination**; ship-out from source is the same volume offset back by the lead time.

### 5. Review impact on the inventory plan (page 240)

The inventory plan uses a **tier selector**:

- **Tier 1**: direct customer demand only (committed + forecast).
- **Tier 1 and 2**: layers in the additional demand from replenishing downstream DCs ("simulated network replenishment").

For the **Central DC**, Tier 1+2 reveals the full demand picture (customers + serving North/South). For the **North/South DCs**, Tier 1+2 shows their replenishment requirement being **received through the network** rather than left as an open-ended simulated requirement.

## Ad hoc network transfers

Briefly noted as a related but separate concept: **occasional rebalancing** moves between DCs, distinct from the routine, lane-driven flows configured above. Not modeled in this exercise.

## Extending to more tiers

The two-tier configuration is **extensible** to deeper networks. Additional tiers are added by **adding versions** in the underlying model — each version represents another replenishment loop around the network. The "current version" (last in the version list) is used for the live plan; additional versions feed deeper tier rollups.

## Key takeaways

- **Lanes are owned by the destination DC** (child relationship), but the user selects the source ("From DC").
- The combination of **lane + routine disaggregation % + transit mode + lead time** fully specifies a network edge.
- The **tier selector** in the inventory plan is the planner's primary lens — always review the **highest tier** for a complete demand picture per DC. Lower tiers show only partial demand and have limited planning value on their own.
- The Central (upstream) DC's plan absorbs downstream replenishment as additional simulated demand; its own replenishment requirement becomes the **production signal** for the network as a whole.
- Multi-tier networks (>2 tiers) are configured via **versions**, not by adding more lane attributes — a notable Anaplan modeling choice that uses the Versions dimension as a tier index.

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary]]
