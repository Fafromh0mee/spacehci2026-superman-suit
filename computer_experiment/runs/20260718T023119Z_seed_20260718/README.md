# PV-to-NMES computational feasibility screen

**Run ID:** `20260718T023119Z_seed_20260718`  
**Status:** `COMPLETE_EXPLORATORY`  
**Scope:** Computer-only Monte Carlo design probe  
**Seed:** `20260718`  
**Planned draws:** 50,000 per scenario-protocol pair

This run tests whether modeled photovoltaic energy can cover a simplified candidate NMES electrical load under explicitly illustrative uncertainty ranges. It also checks whether requested current would remain within an assumed stimulator voltage-compliance envelope.

It does not involve a human or physical hardware and cannot establish human efficacy, medical safety, comfort, muscle preservation, exercise equivalence, or flight readiness.

## Human decisions

- H0 scope: approved through the user's instruction to run any required scientific computer experiment.
- H1 assumptions: approved as exploratory defaults through the same instruction; all values remain labeled illustrative and unmeasured.
- H2 run validity: delegated to prespecified unit, artifact, determinism, and provenance tests. Accept only if all required tests pass.
- H3 interpretation: apply the prespecified rule and choose no stronger than the most conservative permitted label.
- H4 report: accept only if the prohibited-claim scan and artifact tests pass.
- H5 retention: retain as exploratory, never as physiological or flight-validation evidence.

## Reproduction

From this directory:

```bash
python3 -m unittest -v test_experiment.py
python3 run_experiment.py
python3 -m unittest -v test_experiment.py
```

## Completion

- Completed UTC: `2026-07-18T02:37:12Z`
- Final automated status: `COMPLETE_EXPLORATORY`
- Post-run tests: `17/17 passed`
- Audit note: the first post-run audit exposed a unit-name checker defect for two columns containing `_W_avg`; only the checker was corrected, after which all tests passed. Numeric outputs and model equations were unchanged.
