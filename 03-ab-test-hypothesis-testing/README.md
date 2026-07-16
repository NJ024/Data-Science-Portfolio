# Hypothesis Testing on A/B Test Results

Analyzed a two-variant landing-page A/B test (control vs. treatment) to determine whether the
observed lift in conversion rate is statistically significant, using a two-proportion z-test,
a 95% confidence interval, and a secondary t-test on session duration.

## Why this project
Anyone can eyeball "11.2% vs 13.1%" and call it a win. The actual skill is knowing whether that
difference could plausibly have happened by chance given the sample size — which is what
hypothesis testing is for. This project also reports a confidence interval and checks a
secondary metric, since a single p-value doesn't tell the full story a stakeholder needs.

## Data
`data/ab_test_data.csv` — ~8,350 simulated users split into `control` (baseline conversion
~11.2%) and `treatment` (~13.1%) groups, with session duration and device type as additional
fields.

## Files
| File | Purpose |
|---|---|
| `notebook.ipynb` | Full statistical workflow: conversion rates → z-test → confidence interval → t-test → segment check |
| `data/ab_test_data.csv` | Simulated experiment data |

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Method
1. **Two-proportion z-test** — H0: conversion rate is equal between groups. Computed the pooled
   proportion, standard error, z-statistic, and p-value manually (not just calling a library
   black box) to make the mechanics explicit.
2. **95% confidence interval** on the absolute lift, so the result is reported as a range, not
   just "significant / not significant."
3. **Independent t-test** on session duration as a secondary metric — a variant can lift
   conversions while quietly hurting engagement, worth catching before a full rollout.
4. **Device-level segment check** to confirm the effect isn't concentrated in (or masked by)
   one device type.

## Findings
The notebook shows the treatment's conversion lift is statistically significant at α = 0.05
(p < 0.05), with a 95% confidence interval on the lift reported alongside the point estimate.
See the notebook for the exact numbers from this run.
