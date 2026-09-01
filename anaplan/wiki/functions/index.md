---
title: Functions — Index
type: function-index
tags:
  - anaplan
  - functions
  - reference
created: 2026-05-02
updated: 2026-08-31
sources:
  - wiki/sources/2026-05-02-anapedia-all-functions.md
  - wiki/sources/2026-08-31-anapedia-variance-aggregation.md
---

# Anaplan Functions —  Index

All 147 Anaplan formula functions, organized by category. Each row links to the raw Anapedia clipping. Category overviews live under [[wiki/functions/categories/index|wiki/functions/categories]].

> Source: [[wiki/sources/2026-05-02-anapedia-all-functions|Anapedia — All Functions]]

## Aggregation functions  ([[wiki/functions/categories/aggregation|overview]])
Source-to-target aggregation using `[FUNC: Mapping, ...]` selector syntax.

| Function | Syntax | Description |
|---|---|---|
| ALL | `Source[ALL: Mapping, ...]` | TRUE for all values matching Boolean criteria. [[raw/docs/ALL  Anapedia\|raw]] |
| ANY | `Source[ANY: Mapping, ...]` | TRUE if any value matches Boolean criteria. [[raw/docs/ANY  Anapedia\|raw]] |
| AVERAGE | `Values[AVERAGE: Mapping, ...]` | Mean of source values. [[raw/docs/AVERAGE  Anapedia\|raw]] |
| FIRSTNONBLANK | `Source[FIRSTNONBLANK: Mapping, ...]` | First non-blank value per group. [[raw/docs/FIRSTNONBLANK  Anapedia\|raw]] |
| LASTNONBLANK | `Source[LASTNONBLANK: Mapping, ...]` | Last non-blank value per group. [[raw/docs/LASTNONBLANK  Anapedia\|raw]] |
| MAX (agg) | `Source[MAX: Mapping, ...]` | Max value per group. [[raw/docs/MAX (Aggregation function)\|raw]] |
| MIN (agg) | `Source[MIN: Mapping, ...]` | Min value per group. [[raw/docs/MIN (Aggregation function)\|raw]] |
| SUM | `Values[SUM: Mapping, ...]` | Sum values into result module by mapping. [[raw/docs/SUM  Anapedia\|raw]] |
| TEXTLIST (agg) | `Values[TEXTLIST: Mapping, ...]` | Concat values to comma-separated string. [[raw/docs/TEXTLIST (Aggregation function)\|raw]] |
| VARP | `Source[VARP: Mapping, ...]` | Population variance per group. Polaris-only. [[raw/docs/VARP aggregation function\|raw]] |
| VARS | `Source[VARS: Mapping, ...]` | Unbiased sample variance per group. Polaris-only. [[raw/docs/VARS aggregation function\|raw]] |

## Mapping functions  ([[wiki/functions/categories/mapping|overview]])
Cross-module value retrieval. ⚠️ Never combine SUM and LOOKUP in one formula.

| Function | Syntax | Description |
|---|---|---|
| LOOKUP | `Values[LOOKUP: Mapping, ...]` | Retrieve value from source via mapping line items. [[raw/docs/LOOKUP  Anapedia\|raw]] |
| SELECT | `Source[SELECT: Target item]` | Return values from a specific list item or time period. [[raw/docs/SELECT  Anapedia\|raw]] |

## Time and date functions  ([[wiki/functions/categories/time-and-date|overview]])
Largest category. Covers period math, cumulation (xTODATE), period values (xVALUE), offsets (LAG/LEAD/OFFSET/POST), date components, and moving aggregates.

| Function | Syntax | Description |
|---|---|---|
| ADDMONTHS | `ADDMONTHS(Date, n)` | Add n months to a date. [[raw/docs/ADDMONTHS  Anapedia\|raw]] |
| ADDYEARS | `ADDYEARS(Date, n)` | Add n years to a date. [[raw/docs/ADDYEARS  Anapedia\|raw]] |
| CUMULATE | `CUMULATE(Values [, Bool] [, List])` | Running sum over time or list. [[raw/docs/CUMULATE  Anapedia\|raw]] |
| CURRENTPERIODEND | `CURRENTPERIODEND()` | End date of model's current period. [[raw/docs/CURRENTPERIODEND  Anapedia\|raw]] |
| CURRENTPERIODSTART | `CURRENTPERIODSTART()` | Start date of model's current period. [[raw/docs/CURRENTPERIODSTART  Anapedia\|raw]] |
| DATE | `DATE(Y, M, D)` | Build date from components. [[raw/docs/DATE  Anapedia\|raw]] |
| DAY | `DAY(Date)` | Day of month (1–31). [[raw/docs/DAY  Anapedia\|raw]] |
| DAYS | `DAYS([Period])` | Days in a time period. [[raw/docs/DAYS  Anapedia\|raw]] |
| DAYSINMONTH | `DAYSINMONTH(Y, M)` | Days in a given month. [[raw/docs/DAYSINMONTH  Anapedia\|raw]] |
| DAYSINYEAR | `DAYSINYEAR(Y)` | Days in a given year. [[raw/docs/DAYSINYEAR  Anapedia\|raw]] |
| DECUMULATE | `DECUMULATE(Value [, List])` | Subtract previous value from current. [[raw/docs/DECUMULATE  Anapedia\|raw]] |
| END | `END([Period])` | Last date of a period. [[raw/docs/END  Anapedia\|raw]] |
| HALFYEARTODATE | `HALFYEARTODATE(Line item)` | Half-year cumulation. [[raw/docs/HALFYEARTODATE  Anapedia\|raw]] |
| HALFYEARVALUE | `HALFYEARVALUE(Line item)` | Half-year summary value. [[raw/docs/HALFYEARVALUE  Anapedia\|raw]] |
| INPERIOD | `INPERIOD(Date, Period)` | TRUE if date falls in period. [[raw/docs/INPERIOD  Anapedia\|raw]] |
| LAG | `LAG(Value, Offset, Default [, ...])` | Value from prior position. [[raw/docs/LAG  Anapedia\|raw]] |
| LEAD | `LEAD(Value, Offset, Default [, ...])` | Value from later position. [[raw/docs/LEAD  Anapedia\|raw]] |
| MONTH | `MONTH(Value [, method])` | Month number from date/period. [[raw/docs/MONTH  Anapedia\|raw]] |
| MONTHTODATE | `MONTHTODATE(Line item)` | Monthly cumulation. [[raw/docs/MONTHTODATE  Anapedia\|raw]] |
| MONTHVALUE | `MONTHVALUE(Line item)` | Monthly summary value. [[raw/docs/MONTHVALUE  Anapedia\|raw]] |
| MOVINGSUM | `MOVINGSUM(Line item [, Start] [, End] [, Method] [, List])` | Aggregate over rolling window. [[raw/docs/MOVINGSUM  Anapedia\|raw]] |
| NEXT | `NEXT(Expr [, List])` | Evaluate expression at next position. [[raw/docs/NEXT  Anapedia\|raw]] |
| OFFSET | `OFFSET(Value, Offset, Default [, List])` | Shift along a dimension. [[raw/docs/OFFSET  Anapedia\|raw]] |
| PERIOD | `PERIOD(Date)` | Convert date to time period. [[raw/docs/PERIOD  Anapedia\|raw]] |
| POST | `POST(Value, Offset [, List])` | Shift values along dimension; adds collisions. [[raw/docs/POST  Anapedia\|raw]] |
| PREVIOUS | `PREVIOUS(Expr [, List])` | Evaluate expression at prior position. [[raw/docs/PREVIOUS  Anapedia\|raw]] |
| PROFILE | `PROFILE(Numbers, Profile [, List])` | Multiply by a profile series. [[raw/docs/PROFILE  Anapedia\|raw]] |
| QUARTERTODATE | `QUARTERTODATE(Line item)` | Quarterly cumulation. [[raw/docs/QUARTERTODATE  Anapedia\|raw]] |
| QUARTERVALUE | `QUARTERVALUE(Line item)` | Quarterly summary value. [[raw/docs/QUARTERVALUE  Anapedia\|raw]] |
| SPREAD | `SPREAD(Value, Count [, List])` | Even split of a value. [[raw/docs/SPREAD  Anapedia\|raw]] |
| START | `START(Period)` | First date of a period. [[raw/docs/START  Anapedia\|raw]] |
| TIMESUM | `TIMESUM(Line item [, Start] [, End] [, Method])` | Aggregate between two periods. [[raw/docs/TIMESUM  Anapedia\|raw]] |
| WEEKDAY | `WEEKDAY(Date [, FirstDay])` | Day of week (1–7). [[raw/docs/WEEKDAY  Anapedia\|raw]] |
| WEEKTODATE | `WEEKTODATE(Line item)` | Weekly cumulation. [[raw/docs/WEEKTODATE  Anapedia\|raw]] |
| WEEKVALUE | `WEEKVALUE(Line item)` | Weekly summary value. [[raw/docs/WEEKVALUE  Anapedia\|raw]] |
| YEAR | `YEAR(Value [, method])` | Year from date/period. [[raw/docs/YEAR  Anapedia\|raw]] |
| YEARTODATE | `YEARTODATE(Line item)` | Yearly cumulation. [[raw/docs/YEARTODATE  Anapedia\|raw]] |
| YEARVALUE | `YEARVALUE(Line item)` | Yearly summary value. [[raw/docs/YEARVALUE  Anapedia\|raw]] |

## Logical functions  ([[wiki/functions/categories/logical|overview]])

| Function | Syntax | Description |
|---|---|---|
| COMPARE | `COMPARE(T1, T2 [, Mode] [, Locale])` | Compare two text values (-1/0/1). [[raw/docs/COMPARE  Anapedia\|raw]] |
| IF THEN ELSE | `IF Bool THEN R1 ELSE R2` | Conditional. [[raw/docs/IF THEN ELSE\|raw]] |
| ISACTUALVERSION | `ISACTUALVERSION()` | TRUE for the version flagged Actual. [[raw/docs/ISACTUALVERSION  Anapedia\|raw]] |
| ISANCESTOR | `ISANCESTOR(Anc, Desc)` | TRUE if first is ancestor of second. [[raw/docs/ISANCESTOR  Anapedia\|raw]] |
| ISBLANK | `ISBLANK(Value)` | TRUE for blank values. [[raw/docs/ISBLANK  Anapedia\|raw]] |
| ISCURRENTVERSION | `ISCURRENTVERSION()` | TRUE for the version flagged Current. [[raw/docs/ISCURRENTVERSION  Anapedia\|raw]] |
| ISFIRSTOCCURRENCE | `ISFIRSTOCCURRENCE(Values, ListDim)` | TRUE for first occurrence in list. [[raw/docs/ISFIRSTOCCURRENCE  Anapedia\|raw]] |
| ISNOTBLANK | `ISNOTBLANK(Value)` | TRUE for non-blank values. [[raw/docs/ISNOTBLANK  Anapedia\|raw]] |

## Numeric functions  ([[wiki/functions/categories/numeric|overview]])

| Function | Syntax | Description |
|---|---|---|
| ABS | `ABS(Number)` | Absolute value. [[raw/docs/ABS  Anapedia\|raw]] |
| DIVIDE | `DIVIDE(Dividend, Divisor)` | Safe division. [[raw/docs/DIVIDE  Anapedia\|raw]] |
| EXP | `EXP(Number)` | e raised to a power. [[raw/docs/EXP  Anapedia\|raw]] |
| FIRSTNONZERO | `FIRSTNONZERO(V1, V2, ...)` | First non-zero value. [[raw/docs/FIRSTNONZERO  Anapedia\|raw]] |
| LN | `LN(Number)` | Natural logarithm. [[raw/docs/LN  Anapedia\|raw]] |
| LOG | `LOG(Number, Base)` | Logarithm in arbitrary base. [[raw/docs/LOG  Anapedia\|raw]] |
| MAX (numeric) | `MAX(V1, V2, ...)` | Max of values (also dates). [[raw/docs/MAX  Anapedia\|raw]] |
| MIN (numeric) | `MIN(V1, V2, ...)` | Min of values (also dates). [[raw/docs/MIN (Numeric function)\|raw]] |
| MOD | `MOD(Dividend, Divisor)` | Remainder. [[raw/docs/MOD  Anapedia\|raw]] |
| MROUND | `MROUND(N [, Multiple] [, Direction])` | Round to nearest multiple. [[raw/docs/MROUND  Anapedia\|raw]] |
| POWER | `POWER(N, P)` | Raise to a power. [[raw/docs/POWER  Anapedia\|raw]] |
| ROUND | `ROUND(N [, Decimals] [, Direction] [, Method])` | Round to N decimals/integer. [[raw/docs/ROUND  Anapedia\|raw]] |
| SIGN | `SIGN(Number)` | -1/0/1 for sign. [[raw/docs/SIGN  Anapedia\|raw]] |
| SQRT | `SQRT(Number)` | Square root. [[raw/docs/SQRT  Anapedia\|raw]] |

## Text functions  ([[wiki/functions/categories/text|overview]])

| Function | Syntax | Description |
|---|---|---|
| FIND | `FIND(Find, In [, Start])` | Position of first occurrence. [[raw/docs/FIND  Anapedia\|raw]] |
| LEFT | `LEFT(Text [, N])` | First N chars. [[raw/docs/LEFT  Anapedia\|raw]] |
| LENGTH | `LENGTH(Text)` | Char count. [[raw/docs/LENGTH  Anapedia\|raw]] |
| LOWER | `LOWER(Text [, Locale])` | Lowercase. [[raw/docs/LOWER  Anapedia\|raw]] |
| MAILTO | `MAILTO(Text, To [, CC] [, BCC] [, Subj] [, Body])` | Build a mailto link. [[raw/docs/MAILTO  Anapedia\|raw]] |
| MAKELINK | `MAKELINK(Text, URL)` | Build a clickable link. [[raw/docs/MAKELINK  Anapedia\|raw]] |
| MID | `MID(Text, Start [, N])` | Substring. [[raw/docs/MID  Anapedia\|raw]] |
| RIGHT | `RIGHT(Text [, N])` | Last N chars. [[raw/docs/RIGHT  Anapedia\|raw]] |
| SUBSTITUTE | `SUBSTITUTE(Text, Find, Replace)` | Replace all occurrences. [[raw/docs/SUBSTITUTE  Anapedia\|raw]] |
| TEXT | `TEXT(Number)` | Number → text. [[raw/docs/TEXT  Anapedia\|raw]] |
| TEXTLIST (text) | `TEXTLIST(Text, Sep, List [, DupBehavior])` | Concat texts in list order. [[raw/docs/TEXTLIST (Text function)\|raw]] |
| TRIM | `TRIM(Text)` | Strip whitespace. [[raw/docs/TRIM  Anapedia\|raw]] |
| UPPER | `UPPER(Text [, Locale])` | Uppercase. [[raw/docs/UPPER  Anapedia\|raw]] |

## Financial functions  ([[wiki/functions/categories/financial|overview]])

| Function | Syntax | Description |
|---|---|---|
| COUPDAYBS | `COUPDAYBS(Set, Mat, Freq [, Basis])` | Days from coupon period start to settlement. [[raw/docs/COUPDAYBS  Anapedia\|raw]] |
| COUPDAYS | `COUPDAYS(Set, Mat, Freq [, Basis])` | Days in coupon period containing settlement. [[raw/docs/COUPDAYS  Anapedia\|raw]] |
| COUPDAYSNC | `COUPDAYSNC(Set, Mat, Freq [, Basis])` | Days from settlement to next coupon. [[raw/docs/COUPDAYSNC  Anapedia\|raw]] |
| COUPNCD | `COUPNCD(Set, Mat, Freq)` | Next coupon date after settlement. [[raw/docs/COUPNCD  Anapedia\|raw]] |
| COUPNUM | `COUPNUM(Set, Mat, Freq)` | Coupons between settlement and maturity. [[raw/docs/COUPNUM  Anapedia\|raw]] |
| COUPPCD | `COUPPCD(Set, Mat, Freq)` | Previous coupon date before settlement. [[raw/docs/COUPPCD  Anapedia\|raw]] |
| CUMIPMT | `CUMIPMT(Rate, NPer, Pv, Start, End [, Timing])` | Cumulative interest paid. [[raw/docs/CUMIPMT  Anapedia\|raw]] |
| CUMPRINC | `CUMPRINC(Rate, NPer, Pv, Start, End [, Timing])` | Cumulative principal paid. [[raw/docs/CUMPRINC  Anapedia\|raw]] |
| DURATION | `DURATION(Set, Mat, Rate, Yld, Freq [, Basis])` | Macauley duration. [[raw/docs/DURATION  Anapedia\|raw]] |
| FV | `FV(Rate, NPer, Pmt [, Pv] [, Timing])` | Future value. [[raw/docs/FV  Anapedia\|raw]] |
| IPMT | `IPMT(Rate, Per, NPer, Pv [, Fv] [, Timing])` | Interest portion of a payment. [[raw/docs/IPMT  Anapedia\|raw]] |
| IRR | `IRR(Cashflows [, Estimate])` | Internal rate of return. [[raw/docs/IRR  Anapedia\|raw]] |
| MDURATION | `MDURATION(Set, Mat, Rate, Yld, Freq [, Basis])` | Modified Macauley duration. [[raw/docs/MDURATION  Anapedia\|raw]] |
| NPER | `NPER(Rate, Pmt, Pv [, Fv] [, Timing])` | Number of periods. [[raw/docs/NPER  Anapedia\|raw]] |
| NPV | `NPV(Rate, Cashflows)` | Net present value. [[raw/docs/NPV  Anapedia\|raw]] |
| PMT | `PMT(Rate, NPer, Pv [, Fv] [, Timing])` | Periodic payment. [[raw/docs/PMT  Anapedia\|raw]] |
| PPMT | `PPMT(Rate, Per, NPer, Pv [, Fv] [, Timing])` | Principal portion of a payment. [[raw/docs/PPMT  Anapedia\|raw]] |
| PRICE | `PRICE(Set, Mat, Rate, Yld, Red, Freq [, Basis])` | Bond price per 100. [[raw/docs/PRICE  Anapedia\|raw]] |
| PV | `PV(Rate, NPer, Pmt, Fv, Timing)` | Present value. [[raw/docs/PV  Anapedia\|raw]] |
| RATE | `RATE(NPer, Pmt, Pv [, Fv] [, Timing] [, Estimate])` | Implied interest rate. [[raw/docs/RATE  Anapedia\|raw]] |
| YEARFRAC | `YEARFRAC(Start, End [, Basis])` | Year fraction between dates. [[raw/docs/YEARFRAC  Anapedia\|raw]] |
| YIELD | `YIELD(Set, Mat, Rate, Price, Red, Freq [, Basis])` | Yield to maturity. [[raw/docs/YIELD  Anapedia\|raw]] |

## Trigonometry and maths functions  ([[wiki/functions/categories/trigonometry|overview]])

| Function | Syntax | Description |
|---|---|---|
| ACOS | `ACOS(V)` | Inverse cosine. [[raw/docs/ACOS  Anapedia\|raw]] |
| ACOSH | `ACOSH(V)` | Inverse hyperbolic cosine. [[raw/docs/ACOSH  Anapedia\|raw]] |
| ASIN | `ASIN(V)` | Inverse sine. [[raw/docs/ASIN  Anapedia\|raw]] |
| ASINH | `ASINH(V)` | Inverse hyperbolic sine. [[raw/docs/ASINH  Anapedia\|raw]] |
| ATAN | `ATAN(V)` | Inverse tangent. [[raw/docs/ATAN  Anapedia\|raw]] |
| ATANH | `ATANH(V)` | Inverse hyperbolic tangent. [[raw/docs/ATANH  Anapedia\|raw]] |
| COS | `COS(Angle)` | Cosine. [[raw/docs/COS  Anapedia\|raw]] |
| COSH | `COSH(V)` | Hyperbolic cosine. [[raw/docs/COSH  Anapedia\|raw]] |
| E | `E()` | Euler's number. [[raw/docs/E  Anapedia\|raw]] |
| PI | `PI()` | π. [[raw/docs/PI  Anapedia\|raw]] |
| SIN | `SIN(Angle)` | Sine. [[raw/docs/SIN  Anapedia\|raw]] |
| SINH | `SINH(V)` | Hyperbolic sine. [[raw/docs/SINH  Anapedia\|raw]] |
| TAN | `TAN(Angle)` | Tangent. [[raw/docs/TAN  Anapedia\|raw]] |
| TANH | `TANH(V)` | Hyperbolic tangent. [[raw/docs/TANH  Anapedia\|raw]] |
| TODEGREES | `TODEGREES(Angle)` | Radians → degrees. [[raw/docs/TODEGREES  Anapedia\|raw]] |
| TORADIANS | `TORADIANS(Angle)` | Degrees → radians. [[raw/docs/TORADIANS  Anapedia\|raw]] |

## Call center planning functions  ([[wiki/functions/categories/call-center|overview]])
Erlang-family workforce calculations.

| Function | Syntax | Description |
|---|---|---|
| AGENTS | `AGENTS(SLA, RT, Arr, Dur)` | Servers needed to meet SLA. [[raw/docs/AGENTS  Anapedia\|raw]] |
| AGENTSB | `AGENTSB(SLA, Arr, Dur)` | Servers needed for busy-period SLA. [[raw/docs/AGENTSB  Anapedia\|raw]] |
| ANSWERTIME | `ANSWERTIME(N, SLA, Arr, Dur)` | Min hold time to meet SLA. [[raw/docs/ANSWERTIME  Anapedia\|raw]] |
| ARRIVALRATE | `ARRIVALRATE(N, SLA, RT, Dur)` | Max arrival rate to meet SLA. [[raw/docs/ARRIVALRATE  Anapedia\|raw]] |
| AVGDURATION | `AVGDURATION(N, SLA, RT, Arr)` | Required avg call duration. [[raw/docs/AVGDURATION  Anapedia\|raw]] |
| AVGWAIT | `AVGWAIT(N, Arr, Dur)` | Avg waiting time. [[raw/docs/AVGWAIT  Anapedia\|raw]] |
| ERLANGB | `ERLANGB(N, Arr, Dur)` | Probability of being blocked. [[raw/docs/ERLANGB  Anapedia\|raw]] |
| ERLANGC | `ERLANGC(N, Arr, Dur)` | Probability of being queued. [[raw/docs/ERLANGC  Anapedia\|raw]] |
| SLA | `SLA(N, RT, Arr, Dur)` | % of calls answered within target. [[raw/docs/SLA  Anapedia\|raw]] |

## Miscellaneous functions  ([[wiki/functions/categories/misc|overview]])

| Function | Syntax | Description |
|---|---|---|
| CODE | `CODE(Item)` | List item's code. [[raw/docs/CODE  Anapedia\|raw]] |
| COLLECT | `COLLECT()` | Pull line item subset values into module. [[raw/docs/COLLECT  Anapedia\|raw]] |
| CURRENTVERSION | `CURRENTVERSION(Expr)` | Value at version flagged Current. [[raw/docs/CURRENTVERSION  Anapedia\|raw]] |
| FINDITEM | `FINDITEM(List, Text)` | Lookup list item by text. [[raw/docs/FINDITEM  Anapedia\|raw]] |
| HIERARCHYLEVEL | `HIERARCHYLEVEL(List [, Direction] [, LevelType])` | Position in hierarchy. [[raw/docs/HIERARCHYLEVEL  Anapedia\|raw]] |
| ITEM | `ITEM(List)` | Item per cell along a list/time. [[raw/docs/ITEM  Anapedia\|raw]] |
| ITEMLEVEL | `ITEMLEVEL(Item [, Direction])` | Distance to root/leaf in list. [[raw/docs/ITEMLEVEL  Anapedia\|raw]] |
| NAME | `NAME(Item)` | List item → text. [[raw/docs/NAME  Anapedia\|raw]] |
| NEXTVERSION | `NEXTVERSION(Expr)` | Evaluate expr at next version. [[raw/docs/NEXTVERSION  Anapedia\|raw]] |
| PARENT | `PARENT(Child)` | Parent in list/time hierarchy. [[raw/docs/PARENT  Anapedia\|raw]] |
| PREVIOUSVERSION | `PREVIOUSVERSION(Expr)` | Evaluate expr at previous version. [[raw/docs/PREVIOUSVERSION  Anapedia\|raw]] |
| RANK | `RANK(Source [, Dir] [, Equal] [, Inc] [, Groups])` | Sequential ranking. [[raw/docs/RANK  Anapedia\|raw]] |
| RANKCUMULATE | `RANKCUMULATE(CumVals, RankVals [, Dir] [, Inc] [, Groups])` | Rank then cumulate. [[raw/docs/RANKCUMULATE  Anapedia\|raw]] |
| VALUE | `VALUE(Text)` | Text → number. [[raw/docs/VALUE  Anapedia\|raw]] |
