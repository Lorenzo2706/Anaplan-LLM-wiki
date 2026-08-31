---
title: Financial Functions
type: function-category
tags: [anaplan, functions, financial, bonds, loans]
created: 2026-05-02
updated: 2026-05-02
---

# Financial Functions

Loan/annuity math + bond pricing. Mostly mirrors Excel financial functions.

## Sub-buckets

### Loan / annuity (regular cash-flow streams)
`PMT`, `PPMT`, `IPMT`, `CUMPRINC`, `CUMIPMT`, `NPER`, `RATE`, `PV`, `FV`

### Cash-flow analysis
`NPV` (net present value), `IRR` (internal rate of return)

### Bond pricing
`PRICE`, `YIELD`, `DURATION`, `MDURATION`

### Coupon date math
`COUPNCD`, `COUPPCD`, `COUPNUM`, `COUPDAYS`, `COUPDAYBS`, `COUPDAYSNC`

### Date utility
`YEARFRAC` — fraction of a year between two dates, with day-count basis.

## Sign convention
By Anaplan convention (matching Excel):
- Cash *paid out* is negative (loan payments, investments).
- Cash *received* is positive (loan principal received, returns).

Mismatching this is the most common source of nonsensical results.

## See also
- [[wiki/functions/index]]
