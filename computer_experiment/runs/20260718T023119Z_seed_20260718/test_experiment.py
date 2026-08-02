#!/usr/bin/env python3
"""Scientific validity and artifact tests for the computational design probe."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import unittest
from pathlib import Path

import run_experiment as experiment


RUN_DIR = Path(__file__).resolve().parent


def fixed_inputs() -> dict[str, float]:
    return {
        "irradiance_W_m2": 100.0,
        "charge_hours": 2.0,
        "geometry_factor": 0.5,
        "transmission_factor": 0.8,
        "pv_area_m2": 0.3,
        "pv_efficiency_fraction": 0.15,
        "mppt_efficiency_fraction": 0.9,
        "storage_efficiency_fraction": 0.85,
        "commanded_current_A": 0.06,
        "electrode_impedance_ohm": 500.0,
        "compliance_voltage_V": 100.0,
        "pulse_width_s": 0.0004,
        "phases_per_pulse": 2.0,
        "pulse_frequency_Hz": 60.0,
        "train_on_s": 5.0,
        "train_off_s": 10.0,
        "output_efficiency_fraction": 0.8,
        "overhead_power_W": 0.6,
    }


def fixed_protocol() -> dict[str, float | int]:
    return {"sessions_per_day": 1, "minutes_per_session": 30.0, "simultaneous_channels": 2}


class CoreModelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs = fixed_inputs()
        self.protocol = fixed_protocol()
        self.margin = 1.2

    def calculate(self, inputs: dict[str, float] | None = None):
        return experiment.calculate_draw(inputs or self.inputs, self.protocol, self.margin)

    def test_t01_zero_irradiance_returns_zero_harvest(self) -> None:
        inputs = dict(self.inputs)
        inputs["irradiance_W_m2"] = 0.0
        result = self.calculate(inputs)
        self.assertEqual(result["harvested_energy_Wh_day"], 0.0)
        self.assertEqual(result["energy_autonomy_ratio"], 0.0)

    def test_t02_doubling_area_doubles_harvest(self) -> None:
        baseline = self.calculate()
        inputs = dict(self.inputs)
        inputs["pv_area_m2"] *= 2
        doubled = self.calculate(inputs)
        self.assertAlmostEqual(
            doubled["harvested_energy_Wh_day"], 2 * baseline["harvested_energy_Wh_day"], places=12
        )

    def test_t03_doubling_charge_duration_doubles_harvest(self) -> None:
        baseline = self.calculate()
        inputs = dict(self.inputs)
        inputs["charge_hours"] *= 2
        doubled = self.calculate(inputs)
        self.assertAlmostEqual(
            doubled["harvested_energy_Wh_day"], 2 * baseline["harvested_energy_Wh_day"], places=12
        )

    def test_t04_harvest_does_not_exceed_incident_energy(self) -> None:
        result = self.calculate()
        self.assertLessEqual(result["harvested_energy_Wh_day"], result["incident_energy_Wh_day"])

    def test_t05_invalid_efficiency_is_rejected(self) -> None:
        inputs = dict(self.inputs)
        inputs["pv_efficiency_fraction"] = 1.01
        with self.assertRaises(ValueError):
            self.calculate(inputs)

    def test_t06_ear_is_finite_and_nonnegative(self) -> None:
        result = self.calculate()
        self.assertTrue(math.isfinite(float(result["energy_autonomy_ratio"])))
        self.assertGreaterEqual(float(result["energy_autonomy_ratio"]), 0)

    def test_t07_required_voltage_is_current_times_impedance(self) -> None:
        result = self.calculate()
        self.assertAlmostEqual(
            float(result["required_voltage_V"]),
            self.inputs["commanded_current_A"] * self.inputs["electrode_impedance_ohm"],
            places=12,
        )

    def test_t08_excessive_current_impedance_is_compliance_limited(self) -> None:
        inputs = dict(self.inputs)
        inputs["commanded_current_A"] = 0.1
        inputs["electrode_impedance_ohm"] = 1000.0
        inputs["compliance_voltage_V"] = 80.0
        result = self.calculate(inputs)
        self.assertFalse(result["compliance_ok"])

    def test_t09_same_seed_reproduces_samples(self) -> None:
        assumptions = experiment.load_and_validate_assumptions()
        scenario = assumptions["scenarios"]["INDOOR_HABITAT"]
        rng_a = random.Random(20260718)
        rng_b = random.Random(20260718)
        sample_a = experiment.sample_inputs(rng_a, scenario, assumptions["pv_chain"], assumptions["nmes_device"])
        sample_b = experiment.sample_inputs(rng_b, scenario, assumptions["pv_chain"], assumptions["nmes_device"])
        self.assertEqual(sample_a, sample_b)

    def test_t10_different_seed_changes_samples(self) -> None:
        assumptions = experiment.load_and_validate_assumptions()
        scenario = assumptions["scenarios"]["INDOOR_HABITAT"]
        sample_a = experiment.sample_inputs(
            random.Random(20260718), scenario, assumptions["pv_chain"], assumptions["nmes_device"]
        )
        sample_b = experiment.sample_inputs(
            random.Random(20260719), scenario, assumptions["pv_chain"], assumptions["nmes_device"]
        )
        self.assertNotEqual(sample_a, sample_b)

    def test_t11_percentiles_are_ordered(self) -> None:
        summary = experiment.summarize_values([9, 2, 7, 1, 5, 3, 8, 4, 6])
        self.assertLessEqual(summary["p05"], summary["median"])
        self.assertLessEqual(summary["median"], summary["p95"])

    def test_t15_minimum_storage_is_margin_times_demand(self) -> None:
        result = self.calculate()
        self.assertAlmostEqual(
            float(result["minimum_usable_storage_Wh"]),
            self.margin * float(result["system_energy_Wh_day"]),
            places=12,
        )


class ArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summary_path = RUN_DIR / "summary.json"
        if not cls.summary_path.exists():
            raise unittest.SkipTest("post-run artifacts do not exist yet")
        cls.summary = json.loads(cls.summary_path.read_text(encoding="utf-8"))

    def test_t12_raw_row_count_matches_design(self) -> None:
        expected = (
            int(self.summary["metadata"]["draws_per_pair"])
            * int(self.summary["metadata"]["scenario_count"])
            * int(self.summary["metadata"]["protocol_count"])
        )
        raw_path = RUN_DIR / "raw_results.csv"
        with raw_path.open(encoding="utf-8", newline="") as handle:
            actual = sum(1 for _ in handle) - 1
        self.assertEqual(actual, expected)
        self.assertEqual(actual, int(self.summary["metadata"]["raw_row_count"]))

    def test_t13_csv_columns_have_units_or_are_dimensionless(self) -> None:
        raw_path = RUN_DIR / "raw_results.csv"
        with raw_path.open(encoding="utf-8", newline="") as handle:
            fields = next(csv.reader(handle))
        dimensionless = {
            "scenario_id",
            "protocol_id",
            "draw_index",
            "geometry_factor",
            "transmission_factor",
            "pv_efficiency_fraction",
            "mppt_efficiency_fraction",
            "storage_efficiency_fraction",
            "phases_per_pulse",
            "output_efficiency_fraction",
            "sessions_per_day",
            "simultaneous_channels",
            "compliance_ok",
            "pulse_fraction",
            "train_duty_fraction",
            "energy_autonomy_ratio",
            "pv_fraction_of_demand",
            "joint_success",
        }
        allowed_unit_suffixes = (
            "_W_m2",
            "_hours",
            "_m2",
            "_A",
            "_ohm",
            "_V",
            "_s",
            "_Hz",
            "_W",
            "_W_avg",
            "_Wh_day",
            "_Wh",
            "_minutes",
            "_per_session",
        )
        offenders = [
            field for field in fields if field not in dimensionless and not field.endswith(allowed_unit_suffixes)
        ]
        self.assertEqual(offenders, [])

    def test_t14_report_does_not_assert_prohibited_phrases(self) -> None:
        report = (RUN_DIR / "report.md").read_text(encoding="utf-8").lower()
        prohibited_assertions = [
            "proves muscle preservation",
            "safe for astronauts",
            "flight-ready",
            "replaces exercise",
            "clinically effective",
        ]
        for phrase in prohibited_assertions:
            self.assertNotIn(phrase, report)

    def test_t16_hash_manifest_matches_artifacts(self) -> None:
        manifest_path = RUN_DIR / "SHA256SUMS.txt"
        self.assertTrue(manifest_path.exists())
        for line in manifest_path.read_text(encoding="utf-8").splitlines():
            expected_hash, filename = line.split("  ", 1)
            path = RUN_DIR / filename
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(digest, expected_hash, filename)

    def test_t17_summary_percentiles_and_probabilities_are_valid(self) -> None:
        for row in self.summary["results"]:
            self.assertLessEqual(row["ear_p05"], row["ear_median"])
            self.assertLessEqual(row["ear_median"], row["ear_p95"])
            for key in ("p_ear_ge_1", "p_joint_success", "p_compliance_ok", "pv_fraction_median"):
                self.assertGreaterEqual(row[key], 0)
                self.assertLessEqual(row[key], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
