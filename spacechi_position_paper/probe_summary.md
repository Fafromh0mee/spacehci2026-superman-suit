# Supporting Computational Design Probe

## Superman Suit: PV-to-NMES energy feasibility

**Run ID:** `20260718T023119Z_seed_20260718`  
**Status:** Complete, exploratory  
**Evidence class:** `C` — computational design-probe result  
**Date:** 18 July 2026

## Research question

Under explicitly declared uncertainty ranges, in which illumination and charging scenarios could a garment-scale photovoltaic system supply the modeled electrical energy required by a candidate NMES contingency protocol while remaining within an assumed stimulator voltage-compliance envelope?

## Method

A deterministic Monte Carlo model crossed five illustrative illumination scenarios with three candidate NMES electrical-load profiles. Each pair used 50,000 draws, producing 750,000 observations. Inputs were sampled from documented triangular distributions. The model calculated:

- incident and usefully stored photovoltaic energy;
- simplified pulsed NMES electrical demand plus controller/sensor/interface overhead;
- energy-autonomy ratio (EAR);
- requested current × impedance relative to voltage compliance;
- minimum usable storage with a 20% screening margin;
- break-even area and charging duration; and
- input correlations with log10(EAR).

Joint screening success required:

```text
EAR >= 1.20 AND required_voltage <= compliance_voltage
```

This is a design-feasibility threshold, not a clinical or flight threshold.

## Scientific validity checks

All 12 pre-run core tests passed. After execution, the first audit exposed one schema-checker error: two columns explicitly containing watt units ended in `_W_avg`, while the checker recognized only `_W`. The checker—not the model or results—was corrected. All 17 post-run tests then passed, including:

- energy conservation and proportionality;
- bounded efficiencies;
- voltage-compliance logic;
- deterministic-seed reproducibility;
- percentile ordering;
- expected 750,000-row count;
- unit/schema checks;
- prohibited-claim scan;
- storage calculation; and
- artifact-hash verification.

## Results

Across 15 scenario–protocol pairs:

- 9 met **preliminary energy support** under their declared assumptions;
- 1 was **conditional / assumption-sensitive**;
- 4 were **PV-assisted only**; and
- 1 did **not support energy autonomy**.

| Scenario | Protocol | Median EAR | P(joint success) | Maximum permitted label |
|---|---|---:|---:|---|
| Indoor habitat | Bridge-light | 1.887 | 71.858% | Conditional |
| Indoor habitat | Published-schedule anchor | 0.626 | 19.136% | PV-assisted only |
| Indoor habitat | Multichannel screen | 1.117 | 46.062% | PV-assisted only |
| Window-filtered | All three protocols | 8.818–26.639 | 98.814–99.958% | Preliminary energy support |
| Lunar deployed sun | All three protocols | 29.666–88.643 | 99.986–99.992% | Preliminary energy support |
| Mars clear deployed | All three protocols | 12.117–36.609 | 99.914–99.986% | Preliminary energy support |
| Light interruption | Bridge-light | 0.287 | 9.572% | PV-assisted only |
| Light interruption | Published-schedule anchor | 0.095 | 0.602% | Energy autonomy not supported |
| Light interruption | Multichannel screen | 0.170 | 3.050% | PV-assisted only |

All 15 zero-light boundary cases failed the joint rule. All 15 voltage-compliance stress cases exceeded the assumed compliance envelope, confirming that favorable energy availability does not guarantee deliverable electrical output.

The leading sensitivity drivers were:

- irradiance for indoor and interrupted-light cases;
- charging duration for deployed lunar and Mars cases; and
- electronics overhead as a recurrent negative driver.

## Defensible position-paper interpretation

The probe supports neither universal autonomy nor a health-effect claim. It suggests that the concept's energy logic is plausible in sufficiently illuminated or deployed charging configurations, conditional indoors, and weak during interrupted light. This result strengthens the position paper's argument that resource-aware physiological wearables must make intermittency, provenance, and graceful degradation central design concerns.

The defensible wording is:

> Under illustrative assumptions, the modeled energy chain was robust in deployed or strongly illuminated scenarios but conditional or insufficient under indoor and interrupted light. The Superman Suit should therefore be theorized as context-dependent physiological infrastructure that may operate autonomously, as a PV-assisted hybrid, or not at all depending on resource availability.

## Prohibited interpretation

This probe does not demonstrate an evoked contraction, muscle maintenance, comfort, clinical safety, mission-environment performance, or flight readiness.

## Next physical measurement

Log calibrated plane-of-array irradiance and usable charging duration in the intended charging location. A second priority is direct measurement of full stimulator, controller, sensor, and interface Wh per candidate session.

## Reproducibility

The complete report, assumptions, source, tests, raw data, summaries, sensitivity results, boundary cases, logs, and hashes are preserved in:

[`computer_experiment/runs/20260718T023119Z_seed_20260718/`](../computer_experiment/runs/20260718T023119Z_seed_20260718/)
