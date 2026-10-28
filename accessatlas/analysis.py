"""Pure analysis functions for reproducible educational-access exploration.

All differences shown are descriptive associations, not causal effects.
"""
from __future__ import annotations
import pandas as pd

REQUIRED = {
    "student_id", "region", "setting", "internet_access", "device_access",
    "study_hours_week", "attendance_pct", "assessment_score"
}
BINARY = {"yes", "no"}


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return validated, normalized copy or raise informative ValueError."""
    missing = REQUIRED - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    if data.empty:
        raise ValueError("Dataset has no rows.")
    df = data.copy()
    for key in ("internet_access", "device_access"):
        df[key] = df[key].astype(str).str.strip().str.lower()
        if not df[key].isin(BINARY).all():
            raise ValueError(f"{key} must contain only yes/no values.")
    for key in ("region", "setting"):
        df[key] = df[key].astype(str).str.strip()
        if df[key].eq("").any() or df[key].eq("nan").any():
            raise ValueError(f"{key} cannot have missing values.")
    if df["student_id"].isna().any() or df["student_id"].duplicated().any():
        raise ValueError("student_id must be present and unique.")
    for key, low, high in [
        ("study_hours_week", 0, 168), ("attendance_pct", 0, 100),
        ("assessment_score", 0, 100)
    ]:
        df[key] = pd.to_numeric(df[key], errors="coerce")
        if df[key].isna().any() or not df[key].between(low, high).all():
            raise ValueError(f"{key} must contain numbers from {low} to {high}.")
    return df


def overview(df: pd.DataFrame) -> dict:
    """Calculate descriptive summary for previously validated data."""
    return {
        "learners": len(df),
        "internet_pct": round(100 * df["internet_access"].eq("yes").mean(), 1),
        "device_pct": round(100 * df["device_access"].eq("yes").mean(), 1),
        "avg_score": round(df["assessment_score"].mean(), 1),
        "avg_attendance": round(df["attendance_pct"].mean(), 1),
    }


def group_summary(df: pd.DataFrame, group: str = "region") -> pd.DataFrame:
    if group not in {"region", "setting", "internet_access", "device_access"}:
        raise ValueError("Unsupported grouping.")
    out = df.groupby(group, dropna=False).agg(
        learners=("student_id", "size"),
        average_score=("assessment_score", "mean"),
        attendance=("attendance_pct", "mean"),
        avg_study_hours=("study_hours_week", "mean"),
        internet_rate=("internet_access", lambda v: 100 * v.eq("yes").mean()),
        device_rate=("device_access", lambda v: 100 * v.eq("yes").mean()),
    ).reset_index()
    for c in ["average_score", "attendance", "avg_study_hours", "internet_rate", "device_rate"]:
        out[c] = out[c].round(1)
    return out.sort_values("learners", ascending=False).reset_index(drop=True)


def access_gap(df: pd.DataFrame, column: str = "internet_access") -> dict | None:
    """Mean score difference for access vs no access. Positive means yes > no."""
    if column not in ("internet_access", "device_access"):
        raise ValueError("Unsupported access column.")
    yes = df.loc[df[column].eq("yes"), "assessment_score"]
    no = df.loc[df[column].eq("no"), "assessment_score"]
    if yes.empty or no.empty:
        return None
    return {
        "gap_points": round(float(yes.mean() - no.mean()), 2),
        "yes_count": len(yes), "no_count": len(no),
        "yes_mean": round(float(yes.mean()), 2),
        "no_mean": round(float(no.mean()), 2),
    }
