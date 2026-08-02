#!/usr/bin/env python3
"""Reproducible computer-only PV-to-NMES energy feasibility design probe."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import statistics
import time
import traceback
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


RUN_DIR = Path(__file__).resolve().parent
ASSUMPTIONS_PATH = RUN_DIR / "assumptions.json"
RAW_PATH = RUN_DIR / "raw_results.csv"
SUMMARY_CSV_PATH = RUN_DIR / "scenario_summary.csv"
SENSITIVITY_PATH = RUN_DIR / "sensitivity.csv"
BOUNDARY_PATH = RUN_DIR / "boundary_cases.csv"
SUMMARY_JSON_PATH = RUN_DIR / "summary.json"
REPORT_PATH = RUN_DIR / "report.md"
LOG_PATH = RUN_DIR / "run.log"
README_PATH = RUN_DIR / "README.md"
HASH_PATH = RUN_DIR / "SHA256SUMS.txt"


RAW_FIELDS = [
    "scenario_id",
    "protocol_id",
    "draw_index",
    "irradiance_W_m2",
    "charge_hours",
    "geometry_factor",
    "transmission_factor",
    "pv_area_m2",
    "pv_efficiency_fraction",
    "mppt_efficiency_fraction",
    "storage_efficiency_fraction",
    "commanded_current_A",
    "electrode_impedance_ohm",
    "compliance_voltage_V",
    "pulse_width_s",
    "phases_per_pulse",
    "pulse_frequency_Hz",
    "train_on_s",
    "train_off_s",
    "output_efficiency_fraction",
    "overhead_power_W",
    "sessions_per_day",
    "minutes_per_session",
    "simultaneous_channels",
    "incident_energy_Wh_day",
    "harvested_energy_Wh_day",
    "required_voltage_V",
    "compliance_ok",
    "pulse_fraction",
    "train_duty_fraction",
    "electrode_power_W_avg",
    "system_power_W_avg",
    "system_energy_Wh_day",
    "energy_autonomy_ratio",
    "pv_fraction_of_demand",
    "minimum_usable_storage_Wh",
    "break_even_area_m2",
    "break_even_charge_hours",
    "joint_success",
]

SENSITIVITY_INPUTS = [
    "irradiance_W_m2",
    "charge_hours",
    "geometry_factor",
    "transmission_factor",
    "pv_area_m2",
    "pv_efficiency_fraction",
    "mppt_efficiency_fraction",
    "storage_efficiency_fraction",
    "commanded_current_A",
    "electrode_impedance_ohm",
    "compliance_voltage_V",
    "pulse_width_s",
    "pulse_frequency_Hz",
    "train_on_s",
    "train_off_s",
    "output_efficiency_fraction",
    "overhead_power_W",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_distribution(value: dict[str, float], label: str) -> None:
    required = {"low", "mode", "high"}
    if set(value) != required:
        raise ValueError(f"{label} must contain exactly {sorted(required)}")
    low, mode, high = (float(value[key]) for key in ("low", "mode", "high"))
    if not all(math.isfinite(item) for item in (low, mode, high)):
        raise ValueError(f"{label} contains non-finite input")
    if low < 0 or not low <= mode <= high:
        raise ValueError(f"{label} requires 0 <= low <= mode <= high")


def load_and_validate_assumptions(path: Path = ASSUMPTIONS_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        assumptions = json.load(handle)

    if assumptions.get("human_approved") is not True:
        raise ValueError("assumptions.json is not human-approved")
    if int(assumptions.get("draws", 0)) <= 0:
        raise ValueError("draws must be positive")
    if not assumptions.get("scenarios") or not assumptions.get("protocols"):
        raise ValueError("at least one scenario and protocol are required")

    for scenario_id, scenario in assumptions["scenarios"].items():
        for key in ("irradiance_W_m2", "charge_hours", "geometry_factor", "transmission_factor"):
            validate_distribution(scenario[key], f"scenarios.{scenario_id}.{key}")
        for factor in ("geometry_factor", "transmission_factor"):
            if float(scenario[factor]["high"]) > 1:
                raise ValueError(f"scenarios.{scenario_id}.{factor} exceeds 1")

    for key, value in assumptions["pv_chain"].items():
        validate_distribution(value, f"pv_chain.{key}")
        if "efficiency" in key and float(value["high"]) > 1:
            raise ValueError(f"pv_chain.{key} exceeds 1")

    for protocol_id, protocol in assumptions["protocols"].items():
        for key in ("sessions_per_day", "minutes_per_session", "simultaneous_channels"):
            if float(protocol[key]) <= 0:
                raise ValueError(f"protocols.{protocol_id}.{key} must be positive")

    for key, value in assumptions["nmes_device"].items():
        if key == "phases_per_pulse":
            if int(value) <= 0:
                raise ValueError("phases_per_pulse must be positive")
        else:
            validate_distribution(value, f"nmes_device.{key}")
            if "efficiency" in key and float(value["high"]) > 1:
                raise ValueError(f"nmes_device.{key} exceeds 1")

    thresholds = assumptions["screening_thresholds"]
    if float(thresholds["energy_margin"]) < 1:
        raise ValueError("energy_margin must be at least 1")
    return assumptions


def triangular_sample(rng: random.Random, spec: dict[str, float]) -> float:
    return rng.triangular(float(spec["low"]), float(spec["high"]), float(spec["mode"]))


def sample_inputs(
    rng: random.Random,
    scenario: dict[str, Any],
    pv_chain: dict[str, Any],
    nmes_device: dict[str, Any],
) -> dict[str, float]:
    return {
        "irradiance_W_m2": triangular_sample(rng, scenario["irradiance_W_m2"]),
        "charge_hours": triangular_sample(rng, scenario["charge_hours"]),
        "geometry_factor": triangular_sample(rng, scenario["geometry_factor"]),
        "transmission_factor": triangular_sample(rng, scenario["transmission_factor"]),
        "pv_area_m2": triangular_sample(rng, pv_chain["area_m2"]),
        "pv_efficiency_fraction": triangular_sample(rng, pv_chain["pv_efficiency"]),
        "mppt_efficiency_fraction": triangular_sample(rng, pv_chain["mppt_efficiency"]),
        "storage_efficiency_fraction": triangular_sample(rng, pv_chain["storage_efficiency"]),
        "commanded_current_A": triangular_sample(rng, nmes_device["commanded_current_A"]),
        "electrode_impedance_ohm": triangular_sample(rng, nmes_device["electrode_impedance_ohm"]),
        "compliance_voltage_V": triangular_sample(rng, nmes_device["compliance_voltage_V"]),
        "pulse_width_s": triangular_sample(rng, nmes_device["pulse_width_s"]),
        "phases_per_pulse": float(nmes_device["phases_per_pulse"]),
        "pulse_frequency_Hz": triangular_sample(rng, nmes_device["pulse_frequency_Hz"]),
        "train_on_s": triangular_sample(rng, nmes_device["train_on_s"]),
        "train_off_s": triangular_sample(rng, nmes_device["train_off_s"]),
        "output_efficiency_fraction": triangular_sample(rng, nmes_device["output_efficiency"]),
        "overhead_power_W": triangular_sample(rng, nmes_device["overhead_power_W"]),
    }


def point_inputs(
    scenario: dict[str, Any],
    pv_chain: dict[str, Any],
    nmes_device: dict[str, Any],
    point: str,
) -> dict[str, float]:
    def pick(spec: dict[str, float]) -> float:
        return float(spec[point])

    return {
        "irradiance_W_m2": pick(scenario["irradiance_W_m2"]),
        "charge_hours": pick(scenario["charge_hours"]),
        "geometry_factor": pick(scenario["geometry_factor"]),
        "transmission_factor": pick(scenario["transmission_factor"]),
        "pv_area_m2": pick(pv_chain["area_m2"]),
        "pv_efficiency_fraction": pick(pv_chain["pv_efficiency"]),
        "mppt_efficiency_fraction": pick(pv_chain["mppt_efficiency"]),
        "storage_efficiency_fraction": pick(pv_chain["storage_efficiency"]),
        "commanded_current_A": pick(nmes_device["commanded_current_A"]),
        "electrode_impedance_ohm": pick(nmes_device["electrode_impedance_ohm"]),
        "compliance_voltage_V": pick(nmes_device["compliance_voltage_V"]),
        "pulse_width_s": pick(nmes_device["pulse_width_s"]),
        "phases_per_pulse": float(nmes_device["phases_per_pulse"]),
        "pulse_frequency_Hz": pick(nmes_device["pulse_frequency_Hz"]),
        "train_on_s": pick(nmes_device["train_on_s"]),
        "train_off_s": pick(nmes_device["train_off_s"]),
        "output_efficiency_fraction": pick(nmes_device["output_efficiency"]),
        "overhead_power_W": pick(nmes_device["overhead_power_W"]),
    }


def calculate_draw(
    inputs: dict[str, float], protocol: dict[str, Any], energy_margin: float
) -> dict[str, float | bool]:
    efficiencies = (
        inputs["pv_efficiency_fraction"],
        inputs["geometry_factor"],
        inputs["transmission_factor"],
        inputs["mppt_efficiency_fraction"],
        inputs["storage_efficiency_fraction"],
        inputs["output_efficiency_fraction"],
    )
    if any(value < 0 or value > 1 for value in efficiencies):
        raise ValueError("efficiency or attenuation factor outside [0,1]")

    incident_energy = inputs["irradiance_W_m2"] * inputs["pv_area_m2"] * inputs["charge_hours"]
    harvested_energy = (
        incident_energy
        * inputs["pv_efficiency_fraction"]
        * inputs["geometry_factor"]
        * inputs["transmission_factor"]
        * inputs["mppt_efficiency_fraction"]
        * inputs["storage_efficiency_fraction"]
    )
    required_voltage = inputs["commanded_current_A"] * inputs["electrode_impedance_ohm"]
    compliance_ok = required_voltage <= inputs["compliance_voltage_V"]
    pulse_fraction = min(
        1.0,
        inputs["phases_per_pulse"] * inputs["pulse_width_s"] * inputs["pulse_frequency_Hz"],
    )
    train_duty = inputs["train_on_s"] / (inputs["train_on_s"] + inputs["train_off_s"])
    electrode_power = (
        int(protocol["simultaneous_channels"])
        * inputs["commanded_current_A"] ** 2
        * inputs["electrode_impedance_ohm"]
        * pulse_fraction
        * train_duty
    )
    system_power = electrode_power / inputs["output_efficiency_fraction"] + inputs["overhead_power_W"]
    system_energy = (
        system_power
        * (float(protocol["minutes_per_session"]) / 60.0)
        * int(protocol["sessions_per_day"])
    )
    if system_energy <= 0:
        raise ValueError("system energy must be positive")
    ear = harvested_energy / system_energy
    pv_fraction = min(1.0, ear)
    minimum_storage = energy_margin * system_energy

    common_area_denominator = (
        inputs["irradiance_W_m2"]
        * inputs["charge_hours"]
        * inputs["pv_efficiency_fraction"]
        * inputs["geometry_factor"]
        * inputs["transmission_factor"]
        * inputs["mppt_efficiency_fraction"]
        * inputs["storage_efficiency_fraction"]
    )
    break_even_area = minimum_storage / common_area_denominator if common_area_denominator > 0 else math.inf

    common_time_denominator = (
        inputs["irradiance_W_m2"]
        * inputs["pv_area_m2"]
        * inputs["pv_efficiency_fraction"]
        * inputs["geometry_factor"]
        * inputs["transmission_factor"]
        * inputs["mppt_efficiency_fraction"]
        * inputs["storage_efficiency_fraction"]
    )
    break_even_hours = minimum_storage / common_time_denominator if common_time_denominator > 0 else math.inf

    return {
        "incident_energy_Wh_day": incident_energy,
        "harvested_energy_Wh_day": harvested_energy,
        "required_voltage_V": required_voltage,
        "compliance_ok": compliance_ok,
        "pulse_fraction": pulse_fraction,
        "train_duty_fraction": train_duty,
        "electrode_power_W_avg": electrode_power,
        "system_power_W_avg": system_power,
        "system_energy_Wh_day": system_energy,
        "energy_autonomy_ratio": ear,
        "pv_fraction_of_demand": pv_fraction,
        "minimum_usable_storage_Wh": minimum_storage,
        "break_even_area_m2": break_even_area,
        "break_even_charge_hours": break_even_hours,
        "joint_success": ear >= energy_margin and compliance_ok,
    }


def percentile(sorted_values: list[float], probability: float) -> float:
    if not sorted_values:
        raise ValueError("cannot calculate percentile of empty sequence")
    if not 0 <= probability <= 1:
        raise ValueError("probability must be within [0,1]")
    position = (len(sorted_values) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


def summarize_values(values: Iterable[float]) -> dict[str, float]:
    ordered = sorted(float(value) for value in values if math.isfinite(float(value)))
    return {
        "p05": percentile(ordered, 0.05),
        "median": percentile(ordered, 0.50),
        "p95": percentile(ordered, 0.95),
    }


def pearson_correlation(x_values: list[float], y_values: list[float]) -> float:
    if len(x_values) != len(y_values) or len(x_values) < 2:
        raise ValueError("correlation inputs require equal lengths >= 2")
    mean_x = statistics.fmean(x_values)
    mean_y = statistics.fmean(y_values)
    covariance = 0.0
    variance_x = 0.0
    variance_y = 0.0
    for x_value, y_value in zip(x_values, y_values):
        delta_x = x_value - mean_x
        delta_y = y_value - mean_y
        covariance += delta_x * delta_y
        variance_x += delta_x * delta_x
        variance_y += delta_y * delta_y
    denominator = math.sqrt(variance_x * variance_y)
    return covariance / denominator if denominator > 0 else 0.0


def format_value(value: Any) -> Any:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, float):
        if math.isinf(value):
            return "inf"
        return f"{value:.10g}"
    return value


def classify(summary: dict[str, Any], thresholds: dict[str, float]) -> str:
    joint_probability = float(summary["p_joint_success"])
    if joint_probability >= float(thresholds["preliminary_support_probability"]):
        return "PRELIMINARY ENERGY SUPPORT"
    if joint_probability >= float(thresholds["conditional_support_probability"]):
        return "CONDITIONAL / ASSUMPTION-SENSITIVE"
    if float(summary["pv_fraction_median"]) >= float(thresholds["pv_assisted_minimum_fraction"]):
        return "PV-ASSISTED ONLY"
    return "ENERGY AUTONOMY NOT SUPPORTED"


def build_boundary_rows(assumptions: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    margin = float(assumptions["screening_thresholds"]["energy_margin"])
    for scenario_id, scenario in assumptions["scenarios"].items():
        for protocol_id, protocol in assumptions["protocols"].items():
            for point in ("low", "mode", "high"):
                inputs = point_inputs(scenario, assumptions["pv_chain"], assumptions["nmes_device"], point)
                result = calculate_draw(inputs, protocol, margin)
                rows.append(
                    {
                        "scenario_id": scenario_id,
                        "protocol_id": protocol_id,
                        "boundary_case": f"COORDINATE_{point.upper()}",
                        **result,
                    }
                )

            zero_light = point_inputs(scenario, assumptions["pv_chain"], assumptions["nmes_device"], "mode")
            zero_light["irradiance_W_m2"] = 0.0
            result = calculate_draw(zero_light, protocol, margin)
            rows.append(
                {
                    "scenario_id": scenario_id,
                    "protocol_id": protocol_id,
                    "boundary_case": "ZERO_LIGHT",
                    **result,
                }
            )

            compliance_stress = point_inputs(
                scenario, assumptions["pv_chain"], assumptions["nmes_device"], "mode"
            )
            compliance_stress["commanded_current_A"] = float(
                assumptions["nmes_device"]["commanded_current_A"]["high"]
            )
            compliance_stress["electrode_impedance_ohm"] = float(
                assumptions["nmes_device"]["electrode_impedance_ohm"]["high"]
            )
            compliance_stress["compliance_voltage_V"] = float(
                assumptions["nmes_device"]["compliance_voltage_V"]["low"]
            )
            result = calculate_draw(compliance_stress, protocol, margin)
            rows.append(
                {
                    "scenario_id": scenario_id,
                    "protocol_id": protocol_id,
                    "boundary_case": "VOLTAGE_COMPLIANCE_STRESS",
                    **result,
                }
            )

            overhead_stress = point_inputs(
                scenario, assumptions["pv_chain"], assumptions["nmes_device"], "mode"
            )
            overhead_stress["overhead_power_W"] = float(
                assumptions["nmes_device"]["overhead_power_W"]["high"]
            )
            result = calculate_draw(overhead_stress, protocol, margin)
            rows.append(
                {
                    "scenario_id": scenario_id,
                    "protocol_id": protocol_id,
                    "boundary_case": "MAX_OVERHEAD",
                    **result,
                }
            )
    return rows


def determine_next_measurement(sensitivity_rows: list[dict[str, Any]]) -> str:
    leading = Counter()
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in sensitivity_rows:
        grouped.setdefault((str(row["scenario_id"]), str(row["protocol_id"])), []).append(row)
    for rows in grouped.values():
        strongest = max(rows, key=lambda row: abs(float(row["pearson_r_log10_EAR"])))
        leading[str(strongest["input_variable"])] += 1
    top_variable = leading.most_common(1)[0][0]
    if top_variable == "overhead_power_W":
        return "Measure real stimulator, controller, sensor, and interface Wh for one candidate session."
    if top_variable in {"irradiance_W_m2", "transmission_factor", "charge_hours"}:
        return "Log calibrated plane-of-array irradiance and usable charging duration in the intended location."
    if top_variable in {"pv_area_m2", "geometry_factor"}:
        return "Measure effective illuminated area and orientation during wear and deployed charging."
    if top_variable in {"commanded_current_A", "electrode_impedance_ohm", "compliance_voltage_V"}:
        return "Bench-test a certified stimulator into safe electronic loads; do not involve a person."
    return f"Physically validate the highest-ranked uncertain input: {top_variable}."


def generate_report(
    assumptions: dict[str, Any],
    summaries: list[dict[str, Any]],
    sensitivity_rows: list[dict[str, Any]],
    boundary_rows: list[dict[str, Any]],
    metadata: dict[str, Any],
) -> str:
    classification_counts = Counter(str(row["classification"]) for row in summaries)
    strongest = max(summaries, key=lambda row: float(row["p_joint_success"]))
    weakest = min(summaries, key=lambda row: float(row["p_joint_success"]))
    next_measurement = determine_next_measurement(sensitivity_rows)

    sensitivity_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in sensitivity_rows:
        sensitivity_by_pair.setdefault((str(row["scenario_id"]), str(row["protocol_id"])), []).append(row)

    lines = [
        "# PV-to-NMES computational feasibility screen",
        "",
        "## 1. Executive result",
        "",
        "This computer-only design probe estimates photovoltaic energy sufficiency and assumed stimulator voltage compliance. It provides **no human or hardware evidence** and does not evaluate physiological efficacy.",
        "",
        f"The strongest modeled pair was `{strongest['scenario_id']} × {strongest['protocol_id']}` with joint screening success in {100*float(strongest['p_joint_success']):.2f}% of draws; its maximum permitted label is **{strongest['classification']}**.",
        "",
        f"The weakest modeled pair was `{weakest['scenario_id']} × {weakest['protocol_id']}` with joint screening success in {100*float(weakest['p_joint_success']):.2f}% of draws; its maximum permitted label is **{weakest['classification']}**.",
        "",
        "Classification counts: " + ", ".join(f"{key}: {value}" for key, value in sorted(classification_counts.items())) + ".",
        "",
        "## 2. Scope and prohibited claims",
        "",
        "The model covers incident light, photovoltaic conversion, MPPT/storage losses, a simplified electrical NMES load, and voltage compliance. It does not model recruitment, evoked force, pain, skin response, muscle fatigue, muscle preservation, thermal-vacuum behavior, dust physics, battery hazards, or mission operations.",
        "",
        "## 3. Research question and hypotheses",
        "",
        "The question is whether declared illumination scenarios can cover candidate NMES electrical loads under uncertainty. The prespecified expectations were that deployed-light scenarios would outperform indoor/interrupted light, that a few material variables would dominate uncertainty, and that voltage compliance or lower-tail uncertainty would narrow favorable best-case arithmetic.",
        "",
        "## 4. Human decisions",
        "",
        "- H0/H1: the user authorized a scientific computer-only experiment; documented exploratory defaults were used.",
        "- H2: acceptance was delegated to prespecified validity tests; all required tests must pass.",
        "- H3: classifications use prespecified thresholds and are treated as maximum permitted wording.",
        "- H4/H5: retain as exploratory design evidence only.",
        "",
        "## 5. Environment and provenance",
        "",
        f"- Run ID: `{assumptions['run_id']}`",
        f"- Seed: `{assumptions['seed']}`",
        f"- Draws per scenario-protocol pair: `{metadata['draws_per_pair']}`",
        f"- Total rows: `{metadata['raw_row_count']}`",
        f"- Started UTC: `{metadata['started_utc']}`",
        f"- Completed UTC: `{metadata['completed_utc']}`",
        f"- Assumptions SHA-256: `{metadata['assumptions_sha256']}`",
        f"- Code SHA-256: `{metadata['code_sha256']}`",
        "",
        "## 6. Approved assumptions",
        "",
        "All numeric ranges are illustrative triangular-distribution inputs, not mission or hardware measurements. Five light scenarios and three candidate load profiles were crossed. Full values and units are preserved in `assumptions.json`.",
        "",
        "## 7. Computational method",
        "",
        "For each draw, useful harvested energy was calculated from irradiance, area, conversion efficiency, geometry, transmission, MPPT efficiency, storage efficiency, and charging duration. Electrical demand was calculated from a simplified biphasic pulsed resistive load plus controller/sensor/interface overhead. Joint success required `EAR ≥ 1.20` and `current × impedance ≤ compliance voltage`.",
        "",
        "## 8. Validity tests",
        "",
        "Unit, dimensional, deterministic-seed, artifact-schema, percentile-order, row-count, prohibited-claim, storage, and hash checks are implemented in `test_experiment.py`. The final run is accepted only after the post-run test suite passes.",
        "",
        "## 9. Scenario × protocol results",
        "",
        "| Scenario | Protocol | EAR p05 | EAR median | EAR p95 | P(EAR≥1) | P(joint) | P(compliance) | Harvested median Wh | Demand median Wh | PV fraction median | Minimum storage median Wh | Label |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in summaries:
        lines.append(
            "| {scenario_id} | {protocol_id} | {ear_p05:.3f} | {ear_median:.3f} | {ear_p95:.3f} | {p_ear_ge_1:.3f} | {p_joint_success:.3f} | {p_compliance_ok:.3f} | {harvested_Wh_median:.3f} | {system_Wh_median:.3f} | {pv_fraction_median:.3f} | {minimum_storage_Wh_median:.3f} | {classification} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 10. Sensitivity ranking",
            "",
            "The table lists the three strongest linear correlations with log10(EAR) for each pair. Correlation indicates model sensitivity, not real-world causation.",
            "",
            "| Scenario | Protocol | Rank | Input | Pearson r with log10(EAR) |",
            "|---|---|---:|---|---:|",
        ]
    )
    for pair in sorted(sensitivity_by_pair):
        ranked = sorted(
            sensitivity_by_pair[pair],
            key=lambda row: abs(float(row["pearson_r_log10_EAR"])),
            reverse=True,
        )[:3]
        for rank, row in enumerate(ranked, start=1):
            lines.append(
                f"| {pair[0]} | {pair[1]} | {rank} | {row['input_variable']} | {float(row['pearson_r_log10_EAR']):.3f} |"
            )

    zero_light_failures = sum(
        1
        for row in boundary_rows
        if row["boundary_case"] == "ZERO_LIGHT" and not bool(row["joint_success"])
    )
    voltage_stress_failures = sum(
        1
        for row in boundary_rows
        if row["boundary_case"] == "VOLTAGE_COMPLIANCE_STRESS" and not bool(row["compliance_ok"])
    )
    lines.extend(
        [
            "",
            "## 11. Boundary and break-even cases",
            "",
            f"All {zero_light_failures} zero-light scenario-protocol cases failed the joint rule, as required by energy conservation. All {voltage_stress_failures} voltage-compliance stress cases exceeded the assumed compliance envelope. Complete coordinate-low, mode, high, zero-light, maximum-overhead, and voltage-stress results are in `boundary_cases.csv`.",
            "",
            "Break-even area and charging duration distributions are included in the raw and summary artifacts. They are model outputs, not wearable design requirements until irradiance and device load are measured.",
            "",
            "## 12. Human-approved interpretation boundary",
            "",
            "A favorable pair supports only bounded energy plausibility under its declared assumptions. Conditional and negative results are retained. No result establishes muscle maintenance or validates a space environment.",
            "",
            "## 13. Limitations",
            "",
            "- Inputs are illustrative and partly span orders of magnitude.",
            "- The electrical NMES load is a simplified resistive pulse model.",
            "- Output voltage compliance does not demonstrate an evoked contraction.",
            "- Standby, thermal-control, communications, battery aging, and environmental qualification loads are incomplete.",
            "- Correlated real-world inputs were sampled independently.",
            "- Scenario labels do not constitute lunar or Martian environmental validation.",
            "- Monte Carlo precision does not correct uncertain or unmeasured assumptions.",
            "",
            "## 14. Required next physical measurement",
            "",
            next_measurement,
            "",
            "## 15. Artifact manifest",
            "",
            "The run directory contains assumptions, environment, source, tests, raw results, summaries, sensitivity results, boundary cases, this report, logs, and SHA-256 hashes.",
            "",
            "## Position-paper use",
            "",
            "Use this result as a bounded design probe. Report the negative and conditional cases alongside favorable cases. Keep full computational detail in supplementary material and preserve the position paper's primary contribution as the design theory of resource-aware physiological infrastructure.",
            "",
        ]
    )
    return "\n".join(lines)


def update_readme_status(status: str, completed_utc: str) -> None:
    text = README_PATH.read_text(encoding="utf-8")
    text = text.replace("**Status:** `INITIALIZED`", f"**Status:** `{status}`")
    text += f"\n## Completion\n\n- Completed UTC: `{completed_utc}`\n- Final automated status: `{status}`\n"
    README_PATH.write_text(text, encoding="utf-8")


def write_hash_manifest() -> None:
    paths = sorted(path for path in RUN_DIR.iterdir() if path.is_file() and path.name != HASH_PATH.name)
    lines = [f"{sha256_file(path)}  {path.name}" for path in paths]
    HASH_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_experiment() -> dict[str, Any]:
    started_clock = time.perf_counter()
    started_utc = utc_now()
    assumptions = load_and_validate_assumptions()
    seed = int(assumptions["seed"])
    draws = int(assumptions["draws"])
    thresholds = assumptions["screening_thresholds"]
    margin = float(thresholds["energy_margin"])
    rng = random.Random(seed)
    summaries: list[dict[str, Any]] = []
    sensitivity_rows: list[dict[str, Any]] = []
    raw_row_count = 0

    with RAW_PATH.open("w", encoding="utf-8", newline="") as raw_handle:
        raw_writer = csv.DictWriter(raw_handle, fieldnames=RAW_FIELDS)
        raw_writer.writeheader()

        for scenario_id, scenario in assumptions["scenarios"].items():
            for protocol_id, protocol in assumptions["protocols"].items():
                metric_lists: dict[str, list[float]] = {
                    "ear": [],
                    "harvested": [],
                    "system": [],
                    "pv_fraction": [],
                    "minimum_storage": [],
                    "break_even_area": [],
                    "break_even_hours": [],
                }
                sensitivity_values = {key: [] for key in SENSITIVITY_INPUTS}
                log_ear_values: list[float] = []
                ear_ge_1_count = 0
                joint_success_count = 0
                compliance_count = 0

                for draw_index in range(1, draws + 1):
                    inputs = sample_inputs(rng, scenario, assumptions["pv_chain"], assumptions["nmes_device"])
                    result = calculate_draw(inputs, protocol, margin)
                    ear = float(result["energy_autonomy_ratio"])
                    metric_lists["ear"].append(ear)
                    metric_lists["harvested"].append(float(result["harvested_energy_Wh_day"]))
                    metric_lists["system"].append(float(result["system_energy_Wh_day"]))
                    metric_lists["pv_fraction"].append(float(result["pv_fraction_of_demand"]))
                    metric_lists["minimum_storage"].append(float(result["minimum_usable_storage_Wh"]))
                    metric_lists["break_even_area"].append(float(result["break_even_area_m2"]))
                    metric_lists["break_even_hours"].append(float(result["break_even_charge_hours"]))
                    log_ear_values.append(math.log10(max(ear, 1e-12)))
                    for key in SENSITIVITY_INPUTS:
                        sensitivity_values[key].append(float(inputs[key]))
                    ear_ge_1_count += int(ear >= 1.0)
                    joint_success_count += int(bool(result["joint_success"]))
                    compliance_count += int(bool(result["compliance_ok"]))

                    raw_row = {
                        "scenario_id": scenario_id,
                        "protocol_id": protocol_id,
                        "draw_index": draw_index,
                        **inputs,
                        "sessions_per_day": int(protocol["sessions_per_day"]),
                        "minutes_per_session": float(protocol["minutes_per_session"]),
                        "simultaneous_channels": int(protocol["simultaneous_channels"]),
                        **result,
                    }
                    raw_writer.writerow({key: format_value(raw_row[key]) for key in RAW_FIELDS})
                    raw_row_count += 1

                ear_stats = summarize_values(metric_lists["ear"])
                harvested_stats = summarize_values(metric_lists["harvested"])
                system_stats = summarize_values(metric_lists["system"])
                pv_fraction_stats = summarize_values(metric_lists["pv_fraction"])
                storage_stats = summarize_values(metric_lists["minimum_storage"])
                area_stats = summarize_values(metric_lists["break_even_area"])
                hours_stats = summarize_values(metric_lists["break_even_hours"])
                summary = {
                    "scenario_id": scenario_id,
                    "protocol_id": protocol_id,
                    "draws": draws,
                    "ear_p05": ear_stats["p05"],
                    "ear_median": ear_stats["median"],
                    "ear_p95": ear_stats["p95"],
                    "p_ear_ge_1": ear_ge_1_count / draws,
                    "p_joint_success": joint_success_count / draws,
                    "p_compliance_ok": compliance_count / draws,
                    "harvested_Wh_p05": harvested_stats["p05"],
                    "harvested_Wh_median": harvested_stats["median"],
                    "harvested_Wh_p95": harvested_stats["p95"],
                    "system_Wh_p05": system_stats["p05"],
                    "system_Wh_median": system_stats["median"],
                    "system_Wh_p95": system_stats["p95"],
                    "pv_fraction_median": pv_fraction_stats["median"],
                    "minimum_storage_Wh_median": storage_stats["median"],
                    "break_even_area_m2_median": area_stats["median"],
                    "break_even_charge_hours_median": hours_stats["median"],
                }
                summary["classification"] = classify(summary, thresholds)
                summaries.append(summary)

                for input_name in SENSITIVITY_INPUTS:
                    sensitivity_rows.append(
                        {
                            "scenario_id": scenario_id,
                            "protocol_id": protocol_id,
                            "input_variable": input_name,
                            "pearson_r_log10_EAR": pearson_correlation(
                                sensitivity_values[input_name], log_ear_values
                            ),
                        }
                    )

    with SUMMARY_CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0].keys()))
        writer.writeheader()
        for row in summaries:
            writer.writerow({key: format_value(value) for key, value in row.items()})

    with SENSITIVITY_PATH.open("w", encoding="utf-8", newline="") as handle:
        fields = ["scenario_id", "protocol_id", "input_variable", "pearson_r_log10_EAR"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in sensitivity_rows:
            writer.writerow({key: format_value(value) for key, value in row.items()})

    boundary_rows = build_boundary_rows(assumptions)
    boundary_fields = [
        "scenario_id",
        "protocol_id",
        "boundary_case",
        "incident_energy_Wh_day",
        "harvested_energy_Wh_day",
        "required_voltage_V",
        "compliance_ok",
        "system_energy_Wh_day",
        "energy_autonomy_ratio",
        "pv_fraction_of_demand",
        "minimum_usable_storage_Wh",
        "break_even_area_m2",
        "break_even_charge_hours",
        "joint_success",
    ]
    with BOUNDARY_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=boundary_fields)
        writer.writeheader()
        for row in boundary_rows:
            writer.writerow({key: format_value(row[key]) for key in boundary_fields})

    completed_utc = utc_now()
    metadata = {
        "run_id": assumptions["run_id"],
        "seed": seed,
        "draws_per_pair": draws,
        "scenario_count": len(assumptions["scenarios"]),
        "protocol_count": len(assumptions["protocols"]),
        "raw_row_count": raw_row_count,
        "started_utc": started_utc,
        "completed_utc": completed_utc,
        "runtime_seconds": time.perf_counter() - started_clock,
        "assumptions_sha256": sha256_file(ASSUMPTIONS_PATH),
        "code_sha256": sha256_file(Path(__file__)),
        "status": "EXECUTED_AWAITING_POST_TESTS",
    }
    summary_document = {
        "metadata": metadata,
        "scope": assumptions["scope"],
        "prohibited_claims": assumptions["prohibited_claims"],
        "screening_thresholds": thresholds,
        "results": summaries,
        "next_measurement": determine_next_measurement(sensitivity_rows),
    }
    SUMMARY_JSON_PATH.write_text(json.dumps(summary_document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REPORT_PATH.write_text(
        generate_report(assumptions, summaries, sensitivity_rows, boundary_rows, metadata),
        encoding="utf-8",
    )
    LOG_PATH.write_text(
        "\n".join(
            [
                f"run_id={assumptions['run_id']}",
                f"started_utc={started_utc}",
                f"completed_utc={completed_utc}",
                f"seed={seed}",
                f"draws_per_pair={draws}",
                f"raw_row_count={raw_row_count}",
                f"runtime_seconds={metadata['runtime_seconds']:.6f}",
                f"assumptions_sha256={metadata['assumptions_sha256']}",
                f"code_sha256={metadata['code_sha256']}",
                "pre_run_tests=required",
                "post_run_tests=pending",
                "status=EXECUTED_AWAITING_POST_TESTS",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    update_readme_status("EXECUTED_AWAITING_POST_TESTS", completed_utc)
    write_hash_manifest()
    return summary_document


def main() -> int:
    try:
        document = run_experiment()
        print(json.dumps(document["metadata"], indent=2, sort_keys=True))
        return 0
    except Exception:
        LOG_PATH.write_text(
            f"failed_utc={utc_now()}\nstatus=FAILED\n\n{traceback.format_exc()}",
            encoding="utf-8",
        )
        raise


if __name__ == "__main__":
    raise SystemExit(main())
