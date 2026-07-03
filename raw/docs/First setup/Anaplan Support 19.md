---
title: "Anaplan Support"
source: "https://support.anaplan.com/architecture-37ebe652-1a7b-4f5d-8bed-31d6329b8ecc"
author:
published:
created: 2026-05-04
description: "Planual rules regarding ALM Architecture"
tags:
  - "clippings"
---
Once ALM has been initiated, and Deployed mode is turned on, the Production model should **never** be taken out of Deployed mode.

| 6.03-01a Development Model creation | Used when copying a Production model to create the initial ALM environment, or when re-creating the DEV model as part of a “reset”. |
| --- | --- |
| 6.03-01b There are no other exceptions! | It's not worth it. ALM brings control, but there are rules, and Deployed mode is the key rule. |

[ALM Explained—Part 1: Compatibility](https://community.anaplan.com/t5/Best-Practices/ALM-Explained-Part-1-Compatibility/ta-p/84294)

Setting deployed mode for devlopment models is OK and can prevent inadvertent structural changes being made outside of normal development cycles.

Test models should be treated as Production models. This gives a true representation of testing and also prevents inadvertent synchronization from Test to Prod.

Back to top