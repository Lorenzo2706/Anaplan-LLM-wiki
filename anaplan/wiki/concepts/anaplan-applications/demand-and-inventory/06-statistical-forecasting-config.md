---
title: "Chapter 06 — Configuring and Exploring Statistical Forecasting"
type: concept
tags: [anaplan, demand-supply-chain-app, statistical-forecasting]
created: 2026-05-12
updated: 2026-05-12
sources:
  - raw/docs/06-01 Configuring and Exploring Statistical Forecasting-Overview.md
  - raw/docs/06-02 Configuring and Exploring Statistical Forecasting-Coefficients.md
  - raw/docs/06-03 Configuring and Exploring Statistical Forecasting-Back-testing.md
  - raw/docs/06-04 Configuring and Exploring Statistical Forecasting-method utilization.md
---

# Chapter 06 — Configuring and Exploring Statistical Forecasting

## Purpose

This chapter walks through the configuration of the **Statistical Forecasting** module of the Anaplan Demand & Supply Chain application. The objective is to land on a working statistical forecast with a **best-fit method selection** per product/customer combination, ready to be passed into downstream Demand Planning. Three configuration areas are covered:

1. **Coefficients** (alphas and betas) used by smoothing-style methods.
2. **Back-testing** parameters that drive the best-fit method selection.
3. **Global parameters** controlling method behaviour and utilisation (seasonality overlay, moving-average window, regression window, etc.).

The chapter also touches on the relationship between traditional statistical methods and **PlanIQ**, particularly around how back-testing applies differently to each.

---

## Steps covered per sub-video

### 06-01 — Overview

- Introduces the configuration goals: coefficients (alphas/betas), best-fit via back-testing, and other miscellaneous parameters.
- Outputs of the exercise: a statistical forecast with a best-fit selection per product/customer, ready for handover to demand planning.
- Notes PlanIQ's role as an alternative forecasting engine that can be plugged into the same workflow.

### 06-02 — Coefficients (alphas and betas)

- Alphas and betas are smoothing parameters used by a subset of methods:
  - **Simple Exponential Smoothing** — alpha only.
  - **Croston's Method** — alpha and beta (separate option lists).
  - **Modified Croston's** — alpha and beta.
  - **Double Exponential Smoothing** — alpha and beta.
- Each coefficient is **picked from a discrete list** of candidate values in the range 0–1 (e.g. `0.05, 0.10, 0.15, 0.20`). The application does not search continuously between 0 and 1.
- Configuration page lives under **Stat Optimization** in the app; adding a value (e.g. `0.025`) and submitting makes it available to the optimization step.
- The optimizer evaluates all candidate values and selects one alpha/beta per product/customer combination. Different combinations may select different values (demonstrated in the video by switching products).
- **Model size implication:** more candidates = more permutations to evaluate = larger model and slower calculation. Configure the list carefully — enough to give the optimiser useful choice, not so many that the model bloats.

### 06-03 — Back-testing

Back-testing measures how well past forecasts *would have* predicted the known actuals, producing an accuracy metric (RMSE) per method, ranked to pick the **best fit** per product/customer.

Three parameters drive the back-test:

| Parameter | Meaning | Practical tuning rule |
|---|---|---|
| **Lead-time offset** | How many periods before the actual the forecast was produced (i.e. the lag being assessed). | Match the organisation's true supply-chain lead time. Don't test 4-week accuracy if sourcing requires 12 weeks. |
| **Periods to sum** | Block size over which actuals and forecasts are aggregated before comparing (e.g. predict a 4-week block rather than a single week). | Match the ordering cadence (e.g. monthly orders to a contract manufacturer → 4 weekly periods). |
| **Number of tests** | How many distinct historical forecasts to evaluate. | More tests → more confidence, but requires more history. |

Example from the video (weekly grain, actuals through September):

- Offset = 4, periods-to-sum = 2, tests = 1 → use the April-produced forecast to predict the Aug+Sep block.
- Offset = 4, periods-to-sum = 2, tests = 4 → assess Jan, Feb, Mar, Apr forecasts predicting their respective 2-week blocks.

In the app (page 360, **Best Fit Analysis**) the yellow band represents the testing window. Increasing the offset shifts the window backwards; increasing the number of tests widens it.

Per-method **RMSE** is computed across the window and ranked; the lowest-error method becomes the best fit.

> [!important] PlanIQ and back-testing
> Traditional statistical methods can be re-run dynamically inside Anaplan to compute the historical forecast values needed for back-testing. **PlanIQ cannot** — it requires archived snapshots of past forecasts to feed the same testing methodology. Without those archives PlanIQ is excluded from the comparative best-fit assessment.

### 06-04 — Method utilisation and global parameters

App section **900 / Global Parameters** holds the remaining controls:

- **Alpha/Beta optimisation** — additional levers around the optimiser (including overriding with a manual value).
- **Best-fit parameters** — the offset / periods-to-sum / tests covered in 06-03.
- **Disaggregation** — variability-based disaggregation from a higher level (covered in chapter 05).
- **Seasonality overlay** — a switch that applies a seasonal index on top of methods that do *not* inherently model seasonality.
  - Methods like **multiplicative decomposition** already incorporate seasonality.
  - Methods like **simple moving average** and **trend-based methods** do not — they capture level/growth but not seasonality. The overlay lets these methods benefit from a seasonal index without changing the underlying method.
- **Per-method parameters**, for example:
  - Moving-average window length (how many periods to average).
  - Rolling linear regression window length.

---

## Key takeaways

### Forecast methods supported

Roughly 20 methods are evaluated per product/customer combination. Mentioned by name in this chapter:

- **Simple Exponential Smoothing** (alpha).
- **Double Exponential Smoothing** (alpha, beta).
- **Croston's Method** (alpha, beta) — for intermittent demand.
- **Modified Croston's** (alpha, beta).
- **Multiplicative Decomposition** — inherently seasonal.
- **Simple Moving Average** — non-seasonal; benefits from seasonality overlay.
- **Rolling Linear Regression** — trend-based, non-seasonal.
- Other trend-based methods that capture growth/decline but not seasonality.

PlanIQ can also be plugged in as an alternative engine but is excluded from automated back-testing unless forecast archives are available.

### How back-testing works (in one paragraph)

For each candidate method, the application reconstructs forecasts that *would have been produced* at past points in time (offset by the configured lead-time). It sums those forecasts and the matching actuals over the configured period block, repeats across the configured number of tests, and computes **RMSE** across the testing window. The method with the lowest RMSE is selected as the best fit for that product/customer. The three parameters (offset, periods-to-sum, number-of-tests) should be set to mirror the customer's real supply-chain lead time and ordering cadence, not left at defaults.

### Configuration discipline

- **Coefficient lists drive model size** — keep them tight.
- **Best-fit parameters must mirror supply-chain reality** — offset ≈ real lead time, periods-to-sum ≈ ordering block, tests ≈ as many as history supports.
- **Seasonality overlay** is a cheap way to make non-seasonal methods competitive in seasonal demand profiles.
- **PlanIQ inclusion in best-fit** requires snapshot/archive plumbing that traditional methods do not need.

---

## Cross-references

- [[wiki/sources/2026-05-12-anaplan-demand-supply-chain-app|Source summary — Anaplan Demand & Supply Chain app walkthrough]]
- Chapter 05 — Statistical Forecasting (initial setup, disaggregation, variability).
- Concepts: forecast accuracy, RMSE, best-fit selection, exponential smoothing, Croston's method, seasonality decomposition.
