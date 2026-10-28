"""AccessAtlas Streamlit dashboard; run: streamlit run app.py."""
import io
import pandas as pd
import plotly.express as px
import streamlit as st
from accessatlas.analysis import validate_data, overview, group_summary, access_gap
from accessatlas.demo import make_demo

st.set_page_config(page_title="AccessAtlas | Educational Opportunity", page_icon="🌍", layout="wide")
st.markdown("""<style>
.block-container{padding-top:2rem;max-width:1240px}
h1,h2,h3{letter-spacing:-0.035em}
[data-testid='stMetricValue']{font-weight:750}
.hero{border-radius:18px;padding:25px 30px;background:linear-gradient(110deg,#123b52,#247f81);color:#fff;margin-bottom:16px}
.hero h1{color:white;margin:0;font-size:2.5rem}
.hero p{color:#e3f6f5;margin:8px 0 0}
.note{background:#eff8f7;padding:14px 20px;border-radius:12px;border-left:4px solid #268c86;color:#193b42}
</style>""", unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>AccessAtlas 🌍</h1><p>Explore learning access, uncover descriptive gaps, ask better questions.</p></div>', unsafe_allow_html=True)
st.caption("Open-source educational equity explorer · Built for transparent, reproducible exploration")

with st.sidebar:
    st.header("Explore the data")
    source = st.radio("Data source", ["Fictional demo dataset", "Upload your CSV"])
    uploaded = st.file_uploader("Choose CSV", type="csv") if source == "Upload your CSV" else None
    if source == "Upload your CSV":
        st.caption("Use de-identified, consented data only. Uploaded files are processed within this running session; deployment hosting policies also apply.")
        if uploaded is None:
            st.info("Upload a CSV or switch to fictional demo data.")
            st.stop()
    st.divider()
    st.markdown("**What can this tool tell you?**")
    st.caption("Group-level patterns and average differences. Not causation, individual predictions, or educational decisions.")

try:
    raw = pd.read_csv(uploaded) if uploaded is not None else make_demo()
    data = validate_data(raw)
except (ValueError, pd.errors.ParserError, UnicodeDecodeError) as exc:
    st.error(f"Could not load dataset: {exc}")
    st.stop()

if source == "Fictional demo dataset":
    st.warning("DEMO ONLY: These 480 learners are entirely synthetic. Charts and gaps do not represent observed educational outcomes.")

left, middle, right = st.columns(3)
regions = left.multiselect("Region", sorted(data["region"].unique()), default=sorted(data["region"].unique()))
settings = middle.multiselect("Setting", sorted(data["setting"].unique()), default=sorted(data["setting"].unique()))
access_choice = right.selectbox("Analyze access to", ["internet_access", "device_access"], format_func=lambda x: x.replace('_', ' ').title())
df = data.loc[data["region"].isin(regions) & data["setting"].isin(settings)].copy()
if df.empty:
    st.info("No records match these filters. Adjust the selection above.")
    st.stop()

stats = overview(df)
a,b,c,d = st.columns(4)
a.metric("Learners", f"{stats['learners']:,}")
b.metric("Internet access", f"{stats['internet_pct']}%")
c.metric("Device access", f"{stats['device_pct']}%")
d.metric("Mean assessment", f"{stats['avg_score']} / 100")

st.subheader("Where are the access gaps?")
gap = access_gap(df, access_choice)
if gap:
    st.markdown(f"**Mean score difference (access − no access): {gap['gap_points']:+.2f} points** "
                f"· Access group: {gap['yes_count']} learners · No access: {gap['no_count']} learners")
    if min(gap['yes_count'], gap['no_count']) < 10:
        st.warning("At least one comparison group is very small; interpret cautiously.")
else:
    st.info("Both access groups must be present to calculate a mean difference.")

plot1, plot2 = st.columns(2)
with plot1:
    fig = px.box(df, x=access_choice, y="assessment_score", color=access_choice,
                 category_orders={access_choice: ["no", "yes"]}, points=False,
                 labels={"assessment_score": "Assessment score", access_choice: "Access"},
                 title="Score distributions by access")
    fig.update_layout(showlegend=False, margin=dict(l=10,r=10,t=50,b=10))
    st.plotly_chart(fig, use_container_width=True)
with plot2:
    by_setting = group_summary(df, "setting")
    fig = px.bar(by_setting, x="setting", y="internet_rate", color="setting",
                 labels={"internet_rate": "Internet access (%)", "setting": "Setting"},
                 title="Internet access rate by setting", range_y=[0,100])
    fig.update_layout(showlegend=False, margin=dict(l=10,r=10,t=50,b=10))
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Compare regions")
regional = group_summary(df)
if not regional.empty:
    fig = px.bar(regional.sort_values("average_score"), x="average_score", y="region",
                 orientation="h", color="internet_rate", color_continuous_scale="Teal",
                 hover_data=["learners", "attendance", "device_rate"],
                 labels={"average_score": "Average assessment score", "region": "Region", "internet_rate": "Internet access (%)"})
    fig.update_layout(margin=dict(l=10,r=10,t=10,b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(regional, use_container_width=True, hide_index=True)
    st.download_button("Download filtered group summary (CSV)", data=regional.to_csv(index=False).encode(),
                       file_name="accessatlas_group_summary.csv", mime="text/csv")

with st.expander("Methodology, interpretation, and data schema"):
    st.markdown("""**Methods:** arithmetic means and proportions. Access gap = mean assessment score of learners with access minus mean score without access. Filtering recalculates all figures. No predictive model, significance test, causal inference, or fairness guarantee is implied.

**Required CSV columns:** `student_id`, `region`, `setting`, `internet_access` (`yes`/`no`), `device_access` (`yes`/`no`), `study_hours_week` (0–168), `attendance_pct` (0–100), and `assessment_score` (0–100).

**Privacy:** never upload names, emails, student numbers, medical information, or otherwise identifying student records. Suppress or aggregate small groups before sharing outputs. For research involving real participants, consult an appropriate ethics review board first.

**Limitations:** descriptive differences can reflect confounding, selection effects, measurement error, and unequal groups. Synthetic demo effects are intentionally programmed, not discovered.
""")

st.caption("AccessAtlas · Demonstration and education only · No data sent to a custom backend by this app")
