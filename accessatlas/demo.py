"""Deterministic fictional example data. Not real people or observed research."""
import numpy as np
import pandas as pd


def make_demo(n: int = 480, seed: int = 2026) -> pd.DataFrame:
    if n < 1:
        raise ValueError("n must be positive")
    rng = np.random.default_rng(seed)
    region = rng.choice(["North Valley", "Riverbend", "East Ridge", "Lakeside"], n)
    setting = rng.choice(["Rural", "Urban"], n, p=[0.55, 0.45])
    rural = setting == "Rural"
    internet = rng.random(n) < np.where(rural, 0.52, 0.86)
    devices = rng.random(n) < np.where(rural, 0.64, 0.92)
    study = np.clip(rng.normal(8.0 + 1.2 * internet + 0.8 * devices, 3.2, n), 0, 24)
    attendance = np.clip(rng.normal(76 + 4 * internet + 3 * devices, 10, n), 35, 100)
    # Synthetic relationship designed only for demonstrating dashboard behavior.
    score = np.clip(30 + 1.3 * study + 0.27 * attendance + 3.0 * devices +
                    2.0 * internet + rng.normal(0, 11, n), 0, 100)
    return pd.DataFrame({
        "student_id": [f"DEMO-{i:04d}" for i in range(1, n + 1)],
        "region": region, "setting": setting,
        "internet_access": np.where(internet, "yes", "no"),
        "device_access": np.where(devices, "yes", "no"),
        "study_hours_week": np.round(study, 1),
        "attendance_pct": np.round(attendance, 1),
        "assessment_score": np.round(score, 1),
    })
