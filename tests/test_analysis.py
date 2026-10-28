import pandas as pd
import pytest
from accessatlas.analysis import validate_data, overview, group_summary, access_gap
from accessatlas.demo import make_demo


def test_demo_is_reproducible():
    assert make_demo().equals(make_demo())
    assert len(make_demo()) == 480


def test_validate_and_overview():
    df = validate_data(make_demo())
    assert overview(df)["learners"] == 480
    assert 0 <= overview(df)["internet_pct"] <= 100


def test_group_counts_sum():
    df = validate_data(make_demo())
    assert group_summary(df, "region")["learners"].sum() == len(df)


def test_gap_is_difference_of_means():
    df = validate_data(make_demo())
    gap = access_gap(df)
    assert gap["gap_points"] == round(gap["yes_mean"] - gap["no_mean"], 2) or abs(gap["gap_points"] - (gap["yes_mean"] - gap["no_mean"])) < 0.011
    assert gap["yes_count"] + gap["no_count"] == len(df)


def test_gap_missing_group_returns_none():
    df = validate_data(make_demo())
    assert access_gap(df[df["internet_access"] == "yes"]) is None


def test_missing_column_fails():
    with pytest.raises(ValueError, match="Missing columns"):
        validate_data(make_demo().drop(columns=["assessment_score"]))


def test_invalid_score_fails():
    df = make_demo()
    df.loc[0, "assessment_score"] = 150
    with pytest.raises(ValueError, match="assessment_score"):
        validate_data(df)


def test_duplicate_id_fails():
    df = make_demo()
    df.loc[0, "student_id"] = df.loc[1, "student_id"]
    with pytest.raises(ValueError, match="unique"):
        validate_data(df)


def test_invalid_group_rejected():
    with pytest.raises(ValueError, match="Unsupported"):
        group_summary(validate_data(make_demo()), "student_id")
