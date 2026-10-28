# 🌍 AccessAtlas

### Make educational access gaps easier to explore — responsibly.

[![Python tests](https://img.shields.io/badge/tests-pytest-blue)](tests/test_analysis.py)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776ab)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

**AccessAtlas** is an interactive, open-source dashboard for examining the relationship between access to educational resources and learning outcomes. It helps students, researchers, and community organizations explore *descriptive* differences across groups without pretending that correlation proves causation.

> **Demo-data warning:** The bundled 480 records are entirely fictional and generated programmatically. They are **not** research findings, actual students, or evidence that a particular intervention works.

## Features

- 📊 Interactive scores, attendance, internet access, and device-access metrics
- 🗺️ Compare simulated regions and rural/urban settings
- 🔎 Filter groups and inspect differences in mean assessment scores
- 📁 Upload your own *de-identified* CSV using a documented schema
- ⬇️ Export summarized group statistics
- 🧪 Reproducible demo generator and automated tests
- 🔒 No account or database required

## Quick start

Requires Python 3.11+.

```bash
git clone https://github.com/aqibsolangiali/AccessAtlas.git
cd AccessAtlas
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Or download this repository as ZIP from GitHub, extract it, and run the last two commands in the project folder.

## Try it instantly

The app loads 480 reproducible, fictional learner records by default. Select regions/settings to explore how group summaries change. No external dataset or API key is needed.

## Data dictionary

| Column | Description | Accepted values |
|---|---|---|
| `student_id` | Unique pseudonymous record key | Unique nonempty ID |
| `region` | Grouping label | Nonempty text |
| `setting` | Geographic context | Nonempty text (e.g., Rural, Urban) |
| `internet_access` | Internet available | `yes` / `no` |
| `device_access` | Device available | `yes` / `no` |
| `study_hours_week` | Weekly study hours | 0–168 |
| `attendance_pct` | Attendance rate | 0–100 |
| `assessment_score` | Assessment outcome | 0–100 |

Download a sample: [`data/sample_synthetic.csv`](data/sample_synthetic.csv).

## How the analysis works

- Access rates = percentage with `yes` access
- Group averages = arithmetic mean for all selected rows
- Score gap = mean score for `yes` minus mean score for `no`
- Plots show raw distributions or aggregates only; no prediction or statistical significance is claimed
- Scores are **not adjusted** for background differences or confounders

### Ethics and limitations

This is an educational demonstration, **not** an instrument for judging students, allocating resources, or asserting causal conclusions. The demo data includes intentionally generated associations. Real-world results require representative sampling, clear measurement definitions, research review, consent or other legal basis, privacy protections, and careful statistical analysis. Avoid uploading personal information; even pseudonyms may be linkable to individuals. Hosted deployment environments may process uploads on third-party infrastructure. Avoid reporting identifiable small groups.

## Run tests

```bash
pip install -r requirements-dev.txt
python -m pytest -q
```

GitHub Actions runs the tests on every push and pull request.

## Folder structure

```text
accessatlas/
├── app.py
├── accessatlas/
│   ├── __init__.py
│   ├── analysis.py
│   └── demo.py
├── data/
│   └── sample_synthetic.csv
├── tests/
│   └── test_analysis.py
├── .github/workflows/tests.yml
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Potential extensions

- Compare groups with confidence intervals when sample sizes permit
- Add clear visual uncertainty indicators and small-group suppression
- Support multi-year longitudinal analyses
- Add language localization and accessibility testing
- Conduct a rigorously reviewed real-world pilot with a faculty mentor

## About

Designed as a portfolio project at the intersection of **computer science, education, and community impact**. Contributions and feedback are welcome. MIT licensed.
