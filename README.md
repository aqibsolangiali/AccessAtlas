# 🌍 AccessAtlas

### Make educational access gaps easier to explore — responsibly.

[🚀 **Live Demo**](https://aqibsolangiali-accessatlas-app-0zuuk2.streamlit.app/) · [💻 **Source Code**](https://github.com/aqibsolangiali/AccessAtlas) · [🐛 **Report an Issue**](https://github.com/aqibsolangiali/AccessAtlas/issues)

![Python tests](https://github.com/aqibsolangiali/AccessAtlas/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

**AccessAtlas** is an interactive, open-source Python dashboard for exploring educational resource access and learning outcomes. It helps students, researchers, and community organizations examine descriptive differences between groups and ask better questions about educational inequality.

The project emphasizes responsible data exploration: observed differences do not automatically establish causation, and descriptive statistics alone cannot explain why gaps exist.

## 📸 Dashboard Preview

![AccessAtlas dashboard](assets/accessatlas-dashboard.png)

*Explore simulated learner data, compare groups, and examine educational access indicators.*

**Try it now:** [Open the live AccessAtlas dashboard](https://aqibsolangiali-accessatlas-app-0zuuk2.streamlit.app/)

## ✨ Features

- 📊 **Educational indicators:** Explore assessment scores, attendance, internet access, and device access.
- 🗺️ **Group comparisons:** Compare simulated regions and rural/urban settings.
- 🔎 **Interactive filters:** Examine differences in group averages and access rates.
- 📁 **CSV uploads:** Analyze compatible, de-identified datasets using the documented schema.
- ⬇️ **Summary exports:** Export summarized group statistics.
- 🧪 **Automated testing:** Run reproducible tests locally and through GitHub Actions.
- 🔒 **Simple setup:** Explore the included demo data without an account, database, or external API key.

## 🚀 Quick Start

You need Python 3.11 or later.

### 1. Clone the repository

```bash
git clone https://github.com/aqibsolangiali/AccessAtlas.git
cd AccessAtlas
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

Streamlit will provide a local URL where you can open the application in your browser.

Alternatively, try the [hosted demo](https://aqibsolangiali-accessatlas-app-0zuuk2.streamlit.app/) without installing anything.

## 🧪 Run the Tests

Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the automated test suite:

```bash
python -m pytest -q
```

GitHub Actions runs the configured test workflow on pushes and pull requests.

## 📊 Demo Dataset

AccessAtlas includes **480 synthetic learner records** generated programmatically. The dataset is fictional and is intended to demonstrate the dashboard's analytical features.

No real students are represented in the bundled sample.

### Data Dictionary

| Column | Description | Accepted values |
|---|---|---|
| `student_id` | Unique record identifier | Unique, nonempty ID |
| `region` | Region or grouping label | Nonempty text |
| `setting` | Geographic context | For example, Rural or Urban |
| `internet_access` | Internet availability | `yes` / `no` |
| `device_access` | Device availability | `yes` / `no` |
| `study_hours_week` | Weekly study hours | 0–168 |
| `attendance_pct` | Attendance percentage | 0–100 |
| `assessment_score` | Assessment score | 0–100 |

Download the [sample synthetic dataset](data/sample_synthetic.csv).

## 🔍 How the Analysis Works

- **Access rates:** Percentage of selected records reporting access.
- **Group averages:** Arithmetic means calculated for the selected records.
- **Score gap:** Difference between the mean assessment scores of records with and without the specified access.
- **Visualizations:** Show distributions or aggregated statistics to support exploration.

These are descriptive analyses. Scores are not adjusted for confounding factors, and the project does not claim predictive accuracy, statistical significance, or causal effects.

## 🛡️ Ethics, Privacy, and Limitations

AccessAtlas is an educational demonstration, not a tool for judging individual students, allocating resources, or making high-stakes decisions.

The synthetic data contains intentionally generated associations. These patterns are illustrative and should not be interpreted as real-world findings or evidence that an intervention works.

Responsible real-world analysis requires appropriate sampling, clearly defined measures, suitable statistical methods, privacy protections, and applicable consent or other legal authorization.

**Protect personal data:** Avoid uploading identifiable or sensitive information. Pseudonymous records may still be linkable to individuals, and hosted applications may process uploaded files on third-party infrastructure. Exercise caution when interpreting or sharing results for small groups.

## 📁 Project Structure

```text
AccessAtlas/
├── .github/
│   └── workflows/
│       └── tests.yml
├── accessatlas/
│   ├── __init__.py
│   ├── analysis.py
│   └── demo.py
├── data/
│   └── sample_synthetic.csv
├── tests/
│   └── test_analysis.py
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── DEPLOY.md
├── LICENSE
└── README.md
```

## 🔮 Potential Extensions

- Add confidence intervals where sample sizes and assumptions permit.
- Improve uncertainty visualization and suppression of small groups.
- Support longitudinal comparisons across multiple years.
- Add language localization and accessibility testing.
- Explore a rigorously reviewed real-world pilot with an appropriate research partner.

These are possible future improvements, not features currently claimed as complete.

## 👋 About

AccessAtlas is a portfolio project exploring the intersection of **technology, education, and social impact**.

The project aims to make educational access indicators easier to explore while encouraging careful interpretation, responsible data use, and evidence-informed questions.

Contributions, suggestions, and feedback are welcome.

**License:** MIT. See [LICENSE](LICENSE) for details.

---

[🚀 Try AccessAtlas](https://aqibsolangiali-accessatlas-app-0zuuk2.streamlit.app/) · [💻 View the repository](https://github.com/aqibsolangiali/AccessAtlas)
