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
st.caption("Near-real-time feedback intelligence for faster product decisions.")

with st.sidebar:
    st.header("Input")
    uploaded = st.file_uploader("Upload feedback CSV", type=["csv"])
    use_sample = st.toggle("Use sample feedback", value=True)
    st.divider()
    st.write("Expected columns: source, user_type, date, feedback")


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
    use_container_width=True,
    hide_index=True,
)

left, right = st.columns([1, 1])
with left:
    st.subheader("Feedback With AI-Ready Labels")
    st.dataframe(pd.DataFrame(analysis["records"]), use_container_width=True, hide_index=True)

with right:
    st.subheader("Roadmap Report")
    st.download_button(
        "Download Markdown Report",
        report,
        file_name="userlens_feedback_report.md",
        mime="text/markdown",
    )
    st.markdown(report)

