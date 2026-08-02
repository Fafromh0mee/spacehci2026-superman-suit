# PV-to-NMES computational feasibility screen

## 1. Executive result

This computer-only design probe estimates photovoltaic energy sufficiency and assumed stimulator voltage compliance. It provides **no human or hardware evidence** and does not evaluate physiological efficacy.

The strongest modeled pair was `LUNAR_DEPLOYED_SUN × MULTICHANNEL_SCREEN` with joint screening success in 99.99% of draws; its maximum permitted label is **PRELIMINARY ENERGY SUPPORT**.

The weakest modeled pair was `LIGHT_INTERRUPTION × HANSEN_ANCHORED` with joint screening success in 0.60% of draws; its maximum permitted label is **ENERGY AUTONOMY NOT SUPPORTED**.

Classification counts: CONDITIONAL / ASSUMPTION-SENSITIVE: 1, ENERGY AUTONOMY NOT SUPPORTED: 1, PRELIMINARY ENERGY SUPPORT: 9, PV-ASSISTED ONLY: 4.

## 2. Scope and prohibited claims

The model covers incident light, photovoltaic conversion, MPPT/storage losses, a simplified electrical NMES load, and voltage compliance. It does not model recruitment, evoked force, pain, skin response, muscle fatigue, muscle preservation, thermal-vacuum behavior, dust physics, battery hazards, or mission operations.

## 3. Research question and hypotheses

The question is whether declared illumination scenarios can cover candidate NMES electrical loads under uncertainty. The prespecified expectations were that deployed-light scenarios would outperform indoor/interrupted light, that a few material variables would dominate uncertainty, and that voltage compliance or lower-tail uncertainty would narrow favorable best-case arithmetic.

## 4. Human decisions

- H0/H1: the user authorized a scientific computer-only experiment; documented exploratory defaults were used.
- H2: acceptance was delegated to prespecified validity tests; all required tests must pass.
- H3: classifications use prespecified thresholds and are treated as maximum permitted wording.
- H4/H5: retain as exploratory design evidence only.

## 5. Environment and provenance

- Run ID: `20260718T023119Z_seed_20260718`
- Seed: `20260718`
- Draws per scenario-protocol pair: `50000`
- Total rows: `750000`
- Started UTC: `2026-07-18T02:36:53Z`
- Completed UTC: `2026-07-18T02:37:12Z`
- Assumptions SHA-256: `6f463bd9d9bafb15be5791306374d8e01ca2b83e1a6b434680b6cac59b3ee6ff`
- Code SHA-256: `6e73a784ce4c1d3ca1301bff3de04a977b1530244b1f663c9f38de1f58d5af60`

## 6. Approved assumptions

All numeric ranges are illustrative triangular-distribution inputs, not mission or hardware measurements. Five light scenarios and three candidate load profiles were crossed. Full values and units are preserved in `assumptions.json`.

## 7. Computational method

For each draw, useful harvested energy was calculated from irradiance, area, conversion efficiency, geometry, transmission, MPPT efficiency, storage efficiency, and charging duration. Electrical demand was calculated from a simplified biphasic pulsed resistive load plus controller/sensor/interface overhead. Joint success required `EAR ≥ 1.20` and `current × impedance ≤ compliance voltage`.

## 8. Validity tests

Unit, dimensional, deterministic-seed, artifact-schema, percentile-order, row-count, prohibited-claim, storage, and hash checks are implemented in `test_experiment.py`. All 17 post-run tests passed. The initial audit exposed one checker defect: two columns that explicitly contained watt units ended in `_W_avg`, while the checker accepted only `_W`. The checker was corrected without changing the model or numeric outputs, and the complete suite then passed.

## 9. Scenario × protocol results

| Scenario | Protocol | EAR p05 | EAR median | EAR p95 | P(EAR≥1) | P(joint) | P(compliance) | Harvested median Wh | Demand median Wh | PV fraction median | Minimum storage median Wh | Label |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| INDOOR_HABITAT | BRIDGE_LIGHT | 0.506 | 1.887 | 6.161 | 0.790 | 0.719 | 1.000 | 0.780 | 0.419 | 1.000 | 0.503 | CONDITIONAL / ASSUMPTION-SENSITIVE |
| INDOOR_HABITAT | HANSEN_ANCHORED | 0.167 | 0.626 | 2.057 | 0.266 | 0.191 | 1.000 | 0.778 | 1.258 | 0.626 | 1.510 | PV-ASSISTED ONLY |
| INDOOR_HABITAT | MULTICHANNEL_SCREEN | 0.306 | 1.117 | 3.588 | 0.557 | 0.461 | 1.000 | 0.782 | 0.706 | 1.000 | 0.848 | PV-ASSISTED ONLY |
| WINDOW_FILTERED | BRIDGE_LIGHT | 6.393 | 26.639 | 95.633 | 1.000 | 1.000 | 1.000 | 11.074 | 0.419 | 1.000 | 0.503 | PRELIMINARY ENERGY SUPPORT |
| WINDOW_FILTERED | HANSEN_ANCHORED | 2.077 | 8.818 | 32.185 | 0.993 | 0.988 | 1.000 | 10.939 | 1.259 | 1.000 | 1.511 | PRELIMINARY ENERGY SUPPORT |
| WINDOW_FILTERED | MULTICHANNEL_SCREEN | 3.771 | 15.878 | 56.747 | 0.999 | 0.998 | 1.000 | 11.052 | 0.706 | 1.000 | 0.847 | PRELIMINARY ENERGY SUPPORT |
| LUNAR_DEPLOYED_SUN | BRIDGE_LIGHT | 28.848 | 88.643 | 250.784 | 1.000 | 1.000 | 1.000 | 37.023 | 0.419 | 1.000 | 0.502 | PRELIMINARY ENERGY SUPPORT |
| LUNAR_DEPLOYED_SUN | HANSEN_ANCHORED | 9.590 | 29.666 | 82.345 | 1.000 | 1.000 | 1.000 | 37.039 | 1.252 | 1.000 | 1.503 | PRELIMINARY ENERGY SUPPORT |
| LUNAR_DEPLOYED_SUN | MULTICHANNEL_SCREEN | 17.380 | 52.924 | 144.916 | 1.000 | 1.000 | 1.000 | 37.092 | 0.706 | 1.000 | 0.847 | PRELIMINARY ENERGY SUPPORT |
| MARS_CLEAR_DEPLOYED | BRIDGE_LIGHT | 10.947 | 36.609 | 110.355 | 1.000 | 1.000 | 1.000 | 15.273 | 0.419 | 1.000 | 0.503 | PRELIMINARY ENERGY SUPPORT |
| MARS_CLEAR_DEPLOYED | HANSEN_ANCHORED | 3.649 | 12.117 | 36.963 | 1.000 | 0.999 | 1.000 | 15.163 | 1.255 | 1.000 | 1.506 | PRELIMINARY ENERGY SUPPORT |
| MARS_CLEAR_DEPLOYED | MULTICHANNEL_SCREEN | 6.510 | 21.629 | 64.634 | 1.000 | 1.000 | 1.000 | 15.137 | 0.707 | 1.000 | 0.848 | PRELIMINARY ENERGY SUPPORT |
| LIGHT_INTERRUPTION | BRIDGE_LIGHT | 0.032 | 0.287 | 1.656 | 0.130 | 0.096 | 1.000 | 0.118 | 0.417 | 0.287 | 0.501 | PV-ASSISTED ONLY |
| LIGHT_INTERRUPTION | HANSEN_ANCHORED | 0.011 | 0.095 | 0.552 | 0.011 | 0.006 | 1.000 | 0.118 | 1.254 | 0.095 | 1.505 | ENERGY AUTONOMY NOT SUPPORTED |
| LIGHT_INTERRUPTION | MULTICHANNEL_SCREEN | 0.019 | 0.170 | 0.971 | 0.046 | 0.030 | 1.000 | 0.119 | 0.706 | 0.170 | 0.847 | PV-ASSISTED ONLY |

## 10. Sensitivity ranking

The table lists the three strongest linear correlations with log10(EAR) for each pair. Correlation indicates model sensitivity, not real-world causation.

| Scenario | Protocol | Rank | Input | Pearson r with log10(EAR) |
|---|---|---:|---|---:|
| INDOOR_HABITAT | BRIDGE_LIGHT | 1 | irradiance_W_m2 | 0.597 |
| INDOOR_HABITAT | BRIDGE_LIGHT | 2 | overhead_power_W | -0.424 |
| INDOOR_HABITAT | BRIDGE_LIGHT | 3 | charge_hours | 0.423 |
| INDOOR_HABITAT | HANSEN_ANCHORED | 1 | irradiance_W_m2 | 0.599 |
| INDOOR_HABITAT | HANSEN_ANCHORED | 2 | charge_hours | 0.433 |
| INDOOR_HABITAT | HANSEN_ANCHORED | 3 | overhead_power_W | -0.424 |
| INDOOR_HABITAT | MULTICHANNEL_SCREEN | 1 | irradiance_W_m2 | 0.599 |
| INDOOR_HABITAT | MULTICHANNEL_SCREEN | 2 | charge_hours | 0.433 |
| INDOOR_HABITAT | MULTICHANNEL_SCREEN | 3 | overhead_power_W | -0.384 |
| LIGHT_INTERRUPTION | BRIDGE_LIGHT | 1 | irradiance_W_m2 | 0.586 |
| LIGHT_INTERRUPTION | BRIDGE_LIGHT | 2 | charge_hours | 0.480 |
| LIGHT_INTERRUPTION | BRIDGE_LIGHT | 3 | geometry_factor | 0.297 |
| LIGHT_INTERRUPTION | HANSEN_ANCHORED | 1 | irradiance_W_m2 | 0.590 |
| LIGHT_INTERRUPTION | HANSEN_ANCHORED | 2 | charge_hours | 0.480 |
| LIGHT_INTERRUPTION | HANSEN_ANCHORED | 3 | transmission_factor | 0.299 |
| LIGHT_INTERRUPTION | MULTICHANNEL_SCREEN | 1 | irradiance_W_m2 | 0.591 |
| LIGHT_INTERRUPTION | MULTICHANNEL_SCREEN | 2 | charge_hours | 0.478 |
| LIGHT_INTERRUPTION | MULTICHANNEL_SCREEN | 3 | transmission_factor | 0.302 |
| LUNAR_DEPLOYED_SUN | BRIDGE_LIGHT | 1 | charge_hours | 0.661 |
| LUNAR_DEPLOYED_SUN | BRIDGE_LIGHT | 2 | overhead_power_W | -0.494 |
| LUNAR_DEPLOYED_SUN | BRIDGE_LIGHT | 3 | pv_area_m2 | 0.327 |
| LUNAR_DEPLOYED_SUN | HANSEN_ANCHORED | 1 | charge_hours | 0.656 |
| LUNAR_DEPLOYED_SUN | HANSEN_ANCHORED | 2 | overhead_power_W | -0.485 |
| LUNAR_DEPLOYED_SUN | HANSEN_ANCHORED | 3 | pv_area_m2 | 0.329 |
| LUNAR_DEPLOYED_SUN | MULTICHANNEL_SCREEN | 1 | charge_hours | 0.667 |
| LUNAR_DEPLOYED_SUN | MULTICHANNEL_SCREEN | 2 | overhead_power_W | -0.446 |
| LUNAR_DEPLOYED_SUN | MULTICHANNEL_SCREEN | 3 | pv_area_m2 | 0.327 |
| MARS_CLEAR_DEPLOYED | BRIDGE_LIGHT | 1 | charge_hours | 0.567 |
| MARS_CLEAR_DEPLOYED | BRIDGE_LIGHT | 2 | overhead_power_W | -0.456 |
| MARS_CLEAR_DEPLOYED | BRIDGE_LIGHT | 3 | irradiance_W_m2 | 0.387 |
| MARS_CLEAR_DEPLOYED | HANSEN_ANCHORED | 1 | charge_hours | 0.568 |
| MARS_CLEAR_DEPLOYED | HANSEN_ANCHORED | 2 | overhead_power_W | -0.459 |
| MARS_CLEAR_DEPLOYED | HANSEN_ANCHORED | 3 | irradiance_W_m2 | 0.388 |
| MARS_CLEAR_DEPLOYED | MULTICHANNEL_SCREEN | 1 | charge_hours | 0.574 |
| MARS_CLEAR_DEPLOYED | MULTICHANNEL_SCREEN | 2 | overhead_power_W | -0.423 |
| MARS_CLEAR_DEPLOYED | MULTICHANNEL_SCREEN | 3 | irradiance_W_m2 | 0.392 |
| WINDOW_FILTERED | BRIDGE_LIGHT | 1 | irradiance_W_m2 | 0.531 |
| WINDOW_FILTERED | BRIDGE_LIGHT | 2 | charge_hours | 0.516 |
| WINDOW_FILTERED | BRIDGE_LIGHT | 3 | overhead_power_W | -0.394 |
| WINDOW_FILTERED | HANSEN_ANCHORED | 1 | charge_hours | 0.527 |
| WINDOW_FILTERED | HANSEN_ANCHORED | 2 | irradiance_W_m2 | 0.526 |
| WINDOW_FILTERED | HANSEN_ANCHORED | 3 | overhead_power_W | -0.390 |
| WINDOW_FILTERED | MULTICHANNEL_SCREEN | 1 | irradiance_W_m2 | 0.539 |
| WINDOW_FILTERED | MULTICHANNEL_SCREEN | 2 | charge_hours | 0.524 |
| WINDOW_FILTERED | MULTICHANNEL_SCREEN | 3 | overhead_power_W | -0.353 |

## 11. Boundary and break-even cases

All 15 zero-light scenario-protocol cases failed the joint rule, as required by energy conservation. All 15 voltage-compliance stress cases exceeded the assumed compliance envelope. Complete coordinate-low, mode, high, zero-light, maximum-overhead, and voltage-stress results are in `boundary_cases.csv`.

Break-even area and charging duration distributions are included in the raw and summary artifacts. They are model outputs, not wearable design requirements until irradiance and device load are measured.

## 12. Human-approved interpretation boundary

A favorable pair supports only bounded energy plausibility under its declared assumptions. Conditional and negative results are retained. No result establishes muscle maintenance or validates a space environment.

## 13. Limitations

- Inputs are illustrative and partly span orders of magnitude.
- The electrical NMES load is a simplified resistive pulse model.
- Output voltage compliance does not demonstrate an evoked contraction.
- Standby, thermal-control, communications, battery aging, and environmental qualification loads are incomplete.
- Correlated real-world inputs were sampled independently.
- Scenario labels do not constitute lunar or Martian environmental validation.
- Monte Carlo precision does not correct uncertain or unmeasured assumptions.

## 14. Required next physical measurement

Log calibrated plane-of-array irradiance and usable charging duration in the intended location.

## 15. Artifact manifest

The run directory contains assumptions, environment, source, tests, raw results, summaries, sensitivity results, boundary cases, this report, logs, and SHA-256 hashes.

## Position-paper use

Use this result as a bounded design probe. Report the negative and conditional cases alongside favorable cases. Keep full computational detail in supplementary material and preserve the position paper's primary contribution as the design theory of resource-aware physiological infrastructure.
