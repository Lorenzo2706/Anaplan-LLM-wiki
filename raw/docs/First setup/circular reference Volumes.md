---
title: "circular reference: Volumes"
source: "https://community.anaplan.com/discussion/160828/circular-reference-volumes/p1"
author:
  - "[[DCampelo]]"
published: 2025-08-23
created: 2026-06-15
description: "I am trying to write this formula DATA02 SKU Volumes.Volumes in REV02 Volumes Inputs to pull Data from DATA02 SKU Volumes Model. When I do I get an error message Circular reference: Volumes. I checked and there are no other formulas in either Model. I even tried turning SUM to None in Summary field. Could someone tell me…"
tags:
  - "clippings"
---
Anaplan doesn’t allow circular references, which happen when a formula (directly or indirectly) points back to its own result. Since the platform recalculates values whenever inputs change, it requires a clear and non-recursive calculation path.

I’d suggest checking the formula in DATA02 SKU Volumes.Volumes to confirm whether it is directly or indirectly referencing REV02 Volumes Inputs. If there’s any dependency between the two, that could be causing the circular reference error.

[![User: "ChrisAHeathcote"](https://us.v-cdn.net/6037036/av/19172.jpeg "ChrisAHeathcote")](https://community.anaplan.com/profile/19172/ChrisAHeathcote)

The output of the source module is informing the outcome of the target and therefore the formula is incompatible.

Can you post a picture of the error and the formula of the target and source line items. Without seeing these it is hard to support you any further.