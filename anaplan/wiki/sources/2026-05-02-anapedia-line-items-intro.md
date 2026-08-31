---
title: Anapedia — Line Items Introduction
type: source
tags: [anaplan, line-item, fundamentals]
created: 2026-05-02
updated: 2026-05-02
raw: raw/docs/anapedia-line-items-intro.md
---

# Anapedia — Line Items Introduction

**Raw:** `raw/docs/anapedia-line-items-intro.md`

## Summary
Introductory overview of line items: the atomic unit of a module. Each line item has a Format, an optional Formula, and a Summary method. Line items can be categorized by purpose (Input / Calculation / Output), which maps onto the [[wiki/patterns/disco|DISCO]] module-classification pattern.

## Key takeaways
- Line items live inside modules and span the module's dimensions.
- Three core attributes: **Format**, **Formula**, **Summary**.
- Six formats called out: Number, Boolean, Date, Time Period, List, Text.
- Seven summary methods: Sum, Average, Min, Max, None, Formula, Ratio.
- Purpose-based classification (Input/Calc/Output) is the foundation of [[wiki/patterns/disco|DISCO]].

## Wiki pages touched
- Created [[wiki/concepts/anaplan concepts/10_line-item]]
- Created [[wiki/patterns/disco]]

## Open questions / follow-ups
- How does **Summary: Formula** vs **Summary: Ratio** behave at parent levels? (Need a dedicated source.)
- What does the **Time Scale** property add on top of Format = Time Period?
