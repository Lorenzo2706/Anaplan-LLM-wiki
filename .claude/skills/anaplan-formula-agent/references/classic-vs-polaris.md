# Classic vs Polaris — Full Reference

Last updated: 2025. Cross-reference with [Anapedia](https://help.anaplan.com)
and [Planual](https://planual.com) for the latest updates.

---

## What is Polaris?

Polaris is Anaplan's next-generation in-memory calculation engine. It replaces
the Classic engine with a columnar, parallel architecture designed for faster
calculations on large, sparse datasets. Polaris is not backward-compatible in
all cases — some Classic functions are removed, some behave differently, and
new Polaris-only functions are available.

**How to check which engine a model uses:**
Model Settings → Calculation Engine → Classic or Polaris

---

## 1. Functions Removed in Polaris (Classic-only)

These functions **cannot be used in Polaris models**. If you encounter them in
a Polaris context, replace with the listed alternative.

| Function | Reason Removed | Polaris Alternative |
|---|---|---|
| `POST` | Replaced by OFFSET/LAG | `OFFSET(line item, n, 0)` or `LAG(line item, n, 0)` |
| `PREVIOUS` (Classic time shift) | Superseded | `OFFSET(line item, -1, 0)` |
| `NEXT` (Classic time shift) | Superseded | `OFFSET(line item, 1, 0)` |
| `MOVINGSUM` with POST pattern | POST removed | Rewrite using `MOVINGSUM` with period argument |
| `TEXTLIST` with mapping | Behavior changed — see section 3 | Rewrite or use `COLLECT` |

> **Note:** `NEXT` and `PREVIOUS` as standalone functions were deprecated. 
> As property references (e.g. `item.NEXT`) they may still work in some 
> contexts — verify on Anapedia.

---

## 2. New Functions in Polaris (not available in Classic)

| Function | Description | Example |
|---|---|---|
| `COLLECT` | Aggregates values from a list using a parent-child hierarchy without requiring an explicit mapping module. Polaris-only. | `COLLECT(SRC Module.Revenue, Hierarchy List)` |
| `CUMULATE` | Cumulative sum along a list dimension (not time). Polaris-only. | `CUMULATE(Line Item, List)` |
| `DISTRIBUTE` | Distributes a parent value down to children proportionally. Polaris-only. | `DISTRIBUTE(Parent.Value, Weight, List)` |
| `RANK` (enhanced) | Polaris RANK supports sparse data natively and performs better on large lists | Same syntax, better performance |

---

## 3. Functions That Behave Differently

### LOOKUP

| Aspect | Classic | Polaris |
|---|---|---|
| Sparse data | Returns 0 or blank inconsistently on sparse hierarchies | Handles sparse data correctly; returns BLANK as expected |
| Performance | Can be slow on large mapping modules | Significantly faster due to columnar storage |
| Level mismatch error | Throws error | Same — still throws error; dimension must align |
| Mapping direction | Same rule applies | Same rule applies |

**Formula pattern unchanged** — behavior improvement only.

---

### SUM

| Aspect | Classic | Polaris |
|---|---|---|
| Aggregation of sparse data | May produce unexpected totals on sparse lists | Correctly excludes BLANK cells from aggregation |
| Cross-hierarchy SUM | Requires explicit mapping | Same |

---

### FINDITEM

| Aspect | Classic | Polaris |
|---|---|---|
| Behavior on blank input | Returns error or 0 | Returns BLANK (safer, but still guard with ISNOTBLANK) |
| Performance | Slow on large text lists | Faster |

**Best practice in both engines:**
```
IF ISNOTBLANK(text_line_item)
THEN FINDITEM(List, text_line_item)
ELSE BLANK
```

---

### SELECT

| Aspect | Classic | Polaris |
|---|---|---|
| Hard-coded member select | Works but is a Planual anti-pattern | Works but strongly discouraged — use LOOKUP on SYS module instead |
| Performance impact | High — forces single-threaded evaluation | High — same; avoid in both engines |

---

### RANK / RANKCUMULATE / ISFIRSTOCCURRENCE

| Aspect | Classic | Polaris |
|---|---|---|
| Threading | Single-threaded (one thread regardless of list size) | Single-threaded in Polaris too — same performance risk |
| Large list risk | High — flag for lists > 10k items | High — same warning applies |

**Mitigation:** Pre-filter using a Boolean line item to reduce the ranked 
population before applying RANK.

---

### TIMESUM

| Aspect | Classic | Polaris |
|---|---|---|
| On time-dimensioned line items | Works but is semantically incorrect | Works but produces same result — still prefer MOVINGSUM |
| On non-time-dimensioned items | Correct use | Correct use |

**Rule (both engines):** If the source line item is already time-dimensioned,
use `MOVINGSUM` or `YEARTODATE` — not `TIMESUM`.

---

### OFFSET / LAG

| Aspect | Classic | Polaris |
|---|---|---|
| Syntax | `OFFSET(line item, periods, default)` | Identical |
| Performance | Standard | Faster on large time-dimensioned modules |
| Negative offset (look back) | `OFFSET(x, -1, 0)` | Identical |
| Positive offset (look forward) | `OFFSET(x, 1, 0)` | Identical |

**In Polaris, OFFSET replaces POST entirely.** Always use OFFSET in Polaris.

---

### MOVINGSUM

| Aspect | Classic | Polaris |
|---|---|---|
| Syntax | `MOVINGSUM(line item, periods, [FULL])` | Identical |
| Sparse handling | Can return unexpected results at period boundaries | Handles correctly |

---

### YEARTODATE

| Aspect | Classic | Polaris |
|---|---|---|
| Syntax | `YEARTODATE(line item)` | Identical |
| Fiscal year alignment | Uses model calendar fiscal year start | Same |
| Time scale requirement | Source must be time-dimensioned | Same |

---

### IF / THEN / ELSE

| Aspect | Classic | Polaris |
|---|---|---|
| Short-circuit evaluation | **No** — both branches evaluate even if condition is false | **Yes** — only the matching branch evaluates |
| Performance implication | Expensive nested IFs evaluate all paths | Polaris can be faster for deeply nested IFs, but Planual rule (avoid > 3 IFs) still applies |

**Implication:** A FINDITEM inside an IF branch that could error on blanks is
safer in Polaris (because the branch may not evaluate), but you should still
always guard with ISNOTBLANK for portability.

---

### CHILDREN / DESCENDANTS / PARENT / LEVEL

| Aspect | Classic | Polaris |
|---|---|---|
| Hierarchy traversal | Supported | Supported |
| Performance on deep hierarchies | Can be slow | Faster |
| COLLECT as alternative | Not available | Use COLLECT instead of CHILDREN-based SUM patterns |

---

### TEXT / TEXTLIST / CONCATENATION (`&`)

| Aspect | Classic | Polaris |
|---|---|---|
| `TEXTLIST` with mapping | Works | Works but behavior on sparse data differs |
| `&` concatenation | Works | Works — same Planual caution: minimize in large modules |
| Case functions (UPPER, LOWER, CONTAINS, LEFT, RIGHT, MID, LENGTH) | Available | Available — same syntax |

---

## 4. Calculation Architecture Differences

| Aspect | Classic | Polaris |
|---|---|---|
| Calculation model | Row-based (sequential) | Columnar (parallel) |
| Sparse data handling | Stores zeros — large memory footprint | Stores only non-zero values — efficient on sparse models |
| Dependency chain | Evaluated in dependency order, single-threaded for some functions | Parallel where possible |
| Large model performance | Degrades on models > ~1GB | Scales better; designed for large sparse models |
| Recalculation trigger | Full recalc on dependency invalidation | Incremental recalc where possible |
| Time-based calculations | Standard | Optimized for time-series patterns |

---

## 5. Migration Patterns — Classic to Polaris

### Replace POST with OFFSET
```
-- Classic
POST(Revenue, 1)

-- Polaris
OFFSET(Revenue, 1, 0)
```

### Replace PREVIOUS/NEXT with OFFSET
```
-- Classic
PREVIOUS(Revenue)

-- Polaris
OFFSET(Revenue, -1, 0)
```

### Replace CHILDREN-based aggregation with COLLECT
```
-- Classic
SUM(Child Module.Revenue, Child List.Parent)

-- Polaris (when hierarchy is available)
COLLECT(Child Module.Revenue, Parent List)
```

### Replace nested IF chains with LOOKUP
```
-- Classic / Polaris (anti-pattern — avoid in both)
IF Region = 'North' THEN 0.1
ELSE IF Region = 'South' THEN 0.15
ELSE IF Region = 'East' THEN 0.12
ELSE 0.1

-- Both engines (Planual-compliant)
-- SYS Rate Module: Rate [dimensioned by Region]
-- Formula on target: SYS Rate Module.Rate
```

### FINDITEM guard (use in both engines)
```
IF ISNOTBLANK(text_line_item)
THEN FINDITEM(List, text_line_item)
ELSE BLANK
```

---

## 6. Quick Decision Guide — Which Engine?

Use this when writing a formula and the engine is unknown:

| Formula uses... | Classic? | Polaris? | Action |
|---|---|---|---|
| `POST` | ✅ | ❌ | Replace with OFFSET |
| `COLLECT` | ❌ | ✅ | Classic alternative: SUM with mapping |
| `CUMULATE` | ❌ | ✅ | Classic alternative: running total via OFFSET |
| `DISTRIBUTE` | ❌ | ✅ | Classic: manual proportional formula |
| `OFFSET` / `LAG` | ✅ | ✅ | Preferred time-shift in both |
| `RANK` (large list) | ⚠️ | ⚠️ | Flag performance risk in both |
| `SELECT` (hard-coded) | ⚠️ | ⚠️ | Avoid in both — use LOOKUP on SYS |
| `IF` (deep nesting) | ⚠️ | ⚠️ | Avoid in both — use LOOKUP mapping |
| `FINDITEM` | ✅ | ✅ | Guard with ISNOTBLANK in both |

---

## 7. Anapedia & Planual References

- **Anapedia (official Anaplan documentation):**
  https://help.anaplan.com
  → Functions reference: Help → Model Building → Formulas → Functions
  → Polaris engine: Help → Model Building → Calculation Engine

- **Planual (community best practices guide):**
  https://planual.com
  → Section 2: Formula writing best practices
  → Section 3: Performance and scalability
  → Section 4: Naming conventions

When a specific function's behavior is in doubt, always defer to Anapedia as
the authoritative source, as function behavior can change across engine
versions.
