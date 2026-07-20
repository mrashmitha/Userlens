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
SAMPLE_FEEDBACK = ROOT / "examples" / "sample_feedback.csv"


st.set_page_config(page_title="UserLens AI", page_icon="UL", layout="wide")

st.title("UserLens AI")
st.caption("Turn scattered feedback into prioritized product opportunities.")

with st.sidebar:
    st.header("Input")
    uploaded = st.file_uploader("Upload feedback CSV", type=["csv"])
    use_sample = st.toggle("Use sample feedback", value=True)
    st.divider()
    st.caption("Expected columns: source, user_type, date, feedback")


def load_records():
    if uploaded is not None:
        text = uploaded.getvalue().decode("utf-8")
        return load_feedback_csv(io.StringIO(text))
    if use_sample:
        return load_feedback_csv(SAMPLE_FEEDBACK)
    return []


records = load_records()

if not records:
    st.info("Upload a CSV or use the sample feedback to generate insights.")
    st.stop()

analysis = analyze_feedback(records)
report = write_markdown_report(analysis)

metric_cols = st.columns(4)
metric_cols[0].metric("Feedback records", analysis["total_feedback"])
metric_cols[1].metric("Opportunity themes", len(analysis["opportunities"]))
metric_cols[2].metric("Top score", analysis["top_opportunity"]["opportunity_score"])
metric_cols[3].metric("Top theme", analysis["top_opportunity"]["theme"])

top = analysis["top_opportunity"]

st.subheader("Decision Brief")
brief_cols = st.columns([1.2, 1])
with brief_cols[0]:
    st.markdown(f"### {top['theme']}")
    st.write(top["need"])
    st.markdown(f"**Hypothesis:** {top['hypothesis']}")

with brief_cols[1]:
    st.markdown("### Evidence")
    for evidence in top["evidence"]:
        st.write(f"- {evidence}")

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

st.download_button(
    "Download Roadmap Report",
    report,
    file_name="userlens_feedback_report.md",
    mime="text/markdown",
)

with st.expander("View full roadmap report"):
    st.markdown(report)

with st.expander("View labeled feedback"):
    st.dataframe(pd.DataFrame(analysis["records"]), width="stretch", hide_index=True)
