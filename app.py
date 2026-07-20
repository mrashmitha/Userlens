"""Streamlit demo for UserLens AI."""

from __future__ import annotations

import io
from pathlib import Path

import pandas as pd
import streamlit as st

from core.analyzer import analyze_feedback
from core.io import load_feedback_csv
from core.report_writer import write_markdown_report


ROOT = Path(__file__).parent
SAMPLES = {
    "SaaS onboarding": ROOT / "examples" / "sample_feedback.csv",
    "Mobile app reviews": ROOT / "examples" / "sample_mobile_app_feedback.csv",
    "E-commerce checkout": ROOT / "examples" / "sample_ecommerce_feedback.csv",
    "B2B support tickets": ROOT / "examples" / "sample_b2b_support_feedback.csv",
}


st.set_page_config(page_title="UserLens AI", page_icon="UL", layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2.4rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }
    [data-testid="stSidebar"] {
        background: rgba(127, 127, 127, 0.04);
    }
    div[data-testid="stMetric"] {
        border: 1px solid rgba(127, 127, 127, 0.18);
        border-radius: 12px;
        padding: 16px 18px;
    }
    div[data-testid="stFileUploader"] {
        border: 1px solid rgba(14, 165, 233, 0.45);
        border-radius: 14px;
        padding: 10px;
    }
    h1, h2, h3 {
        letter-spacing: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("UserLens AI")
st.caption("Executive feedback intelligence for faster product decisions.")

with st.sidebar:
    st.header("Analyze Feedback")
    st.caption("Upload your CSV or test with a sample dataset.")
    uploaded = st.file_uploader("Upload feedback CSV", type=["csv"], label_visibility="collapsed")
    sample_name = st.selectbox("Sample dataset", list(SAMPLES.keys()))
    use_sample = st.toggle("Use selected sample", value=True)

    sample_path = SAMPLES[sample_name]
    st.download_button(
        "Download sample CSV",
        sample_path.read_text(encoding="utf-8"),
        file_name=sample_path.name,
        mime="text/csv",
        width="stretch",
    )
    st.divider()
    st.caption("Expected columns: source, user_type, date, feedback")
    st.caption("MVP method: deterministic taxonomy + scoring. No LLM API key required.")


def load_records():
    if uploaded is not None:
        text = uploaded.getvalue().decode("utf-8")
        return load_feedback_csv(io.StringIO(text))
    if use_sample:
        return load_feedback_csv(SAMPLES[sample_name])
    return []


records = load_records()

if not records:
    st.info("Upload a CSV or use the sample feedback to generate insights.")
    st.stop()

analysis = analyze_feedback(records)
report = write_markdown_report(analysis)
top = analysis["top_opportunity"]

metric_cols = st.columns(4)
metric_cols[0].metric("Feedback records", analysis["total_feedback"])
metric_cols[1].metric("Opportunity themes", len(analysis["opportunities"]))
metric_cols[2].metric("Top score", top["opportunity_score"])
metric_cols[3].metric("Top theme", top["theme"])

st.divider()
st.subheader("Executive Decision Brief")
brief_cols = st.columns([1.2, 1])
with brief_cols[0]:
    st.markdown(f"### {top['theme']}")
    st.write(top["need"])
    st.markdown(f"**Hypothesis:** {top['hypothesis']}")

with brief_cols[1]:
    st.markdown("### Evidence")
    for evidence in top["evidence"]:
        st.write(f"- {evidence}")

st.download_button(
    "Download Roadmap Report",
    report,
    file_name="userlens_feedback_report.md",
    mime="text/markdown",
)

st.divider()
st.subheader("Prioritized Opportunities")
opportunity_df = pd.DataFrame(analysis["opportunities"])
st.dataframe(
    opportunity_df[
        [
            "theme",
            "frequency",
            "dominant_user_type",
            "sentiment",
            "high_urgency_count",
            "opportunity_score",
            "hypothesis",
        ]
    ],
    width="stretch",
    hide_index=True,
)

with st.expander("View full roadmap report"):
    st.markdown(report)

with st.expander("View labeled feedback"):
    st.dataframe(pd.DataFrame(analysis["records"]), width="stretch", hide_index=True)
