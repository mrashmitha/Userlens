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
    .stApp {
        background: linear-gradient(180deg, #f7fafc 0%, #eef6f7 100%);
        color: #102033;
    }
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 3rem;
        max-width: 1160px;
    }
    [data-testid="stSidebar"] {
        background: #f8fbfb;
        border-right: 1px solid #d9e7e8;
    }
    section[data-testid="stSidebar"] {
        display: none;
    }
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #dbe8ea;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 8px 24px rgba(15, 45, 61, 0.06);
    }
    div[data-testid="stFileUploader"] {
        background: #ffffff;
        border: 1.5px dashed #5aa6b1;
        border-radius: 16px;
        padding: 12px;
    }
    div[data-testid="stFileUploaderDropzone"] {
        background: #ffffff !important;
        border: 1.5px dashed #5aa6b1 !important;
        border-radius: 14px !important;
    }
    div[data-testid="stFileUploaderDropzone"] button,
    div.stButton > button,
    div.stDownloadButton > button {
        background: #0f4c5c !important;
        border: 1px solid #0f4c5c !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }
    div[data-testid="stFileUploaderDropzone"] button:hover,
    div.stButton > button:hover,
    div.stDownloadButton > button:hover {
        background: #093945;
        border-color: #093945;
        color: #ffffff;
    }
    div[data-testid="stFileUploaderDropzone"] button:focus,
    div.stButton > button:focus,
    div.stDownloadButton > button:focus {
        outline: 3px solid #8fd3dc;
        outline-offset: 2px;
        box-shadow: none;
    }
    div[data-testid="stFileUploaderDropzone"] small,
    div[data-testid="stFileUploaderDropzone"] span,
    div[data-testid="stFileUploaderDropzone"] p {
        color: #102033 !important;
    }
    div[data-baseweb="select"] > div {
        background: #ffffff !important;
        border-color: #9ec9ce !important;
        color: #102033 !important;
    }
    div[data-baseweb="select"] span {
        color: #102033 !important;
    }
    h1, h2, h3 {
        letter-spacing: 0;
        color: #102033;
    }
    .hero {
        background: #ffffff;
        border: 1px solid #dbe8ea;
        border-radius: 20px;
        padding: 16px 22px;
        box-shadow: 0 12px 30px rgba(15, 45, 61, 0.07);
        margin-bottom: 10px;
        min-height: 245px;
    }
    .eyebrow {
        color: #287782;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .hero h1 {
        font-size: 1.9rem;
        line-height: 1.12;
        margin: 0 0 6px;
    }
    .hero p {
        color: #5d6f7b;
        font-size: 0.96rem;
        margin: 0;
        max-width: 720px;
    }
    .mini-flow {
        color: #287782;
        font-size: 0.9rem;
        font-weight: 650;
        margin-top: 8px;
    }
    .input-panel {
        background: #ffffff;
        border: 1px solid #dbe8ea;
        border-radius: 18px;
        padding: 12px 14px;
        margin: 0;
        box-shadow: 0 10px 26px rgba(15, 45, 61, 0.05);
    }
    .input-heading {
        color: #102033;
        font-size: 0.98rem;
        font-weight: 750;
        margin-bottom: 2px;
    }
    .input-subcopy {
        color: #637786;
        font-size: 0.88rem;
        margin-bottom: 0;
    }
    .compact-input {
        background: #ffffff;
        border: 1px solid #dbe8ea;
        border-radius: 18px;
        padding: 12px 14px;
        margin: 8px 0 10px;
        box-shadow: 0 8px 20px rgba(15, 45, 61, 0.05);
    }
    .brief-card {
        background: #ffffff;
        border: 1px solid #dbe8ea;
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 10px 26px rgba(15, 45, 61, 0.06);
        margin: 0 0 14px;
    }
    .brief-label {
        color: #287782;
        font-weight: 700;
        font-size: 0.78rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .brief-title {
        color: #102033;
        font-size: 1.35rem;
        font-weight: 750;
        margin: 6px 0 8px;
    }
    .brief-text {
        color: #425565;
        line-height: 1.55;
        margin-bottom: 12px;
    }
    .evidence-list {
        margin: 10px 0 0;
        padding-left: 18px;
        color: #425565;
        line-height: 1.55;
    }
    .opportunity-card {
        background: #ffffff;
        border: 1px solid #dbe8ea;
        border-radius: 16px;
        padding: 14px;
        min-height: 130px;
        box-shadow: 0 8px 22px rgba(15, 45, 61, 0.05);
    }
    .rank {
        color: #287782;
        font-size: 0.82rem;
        font-weight: 750;
    }
    .opp-title {
        color: #102033;
        font-size: 1.08rem;
        font-weight: 750;
        margin: 8px 0;
    }
    .opp-meta {
        color: #60727f;
        font-size: 0.9rem;
        margin-bottom: 10px;
    }
    .score-pill {
        display: inline-block;
        background: #e8f6f7;
        color: #176d78;
        border: 1px solid #bfe2e5;
        border-radius: 999px;
        padding: 4px 10px;
        font-size: 0.84rem;
        font-weight: 750;
    }
    .section-heading {
        color: #102033;
        font-size: 1.22rem;
        font-weight: 750;
        margin: 16px 0 10px;
    }
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 16px;
        margin: 6px 0 12px;
    }
    .metric-card {
        background: #ffffff;
        border: 1px solid #dbe8ea;
        border-radius: 16px;
        padding: 14px 16px;
        box-shadow: 0 8px 24px rgba(15, 45, 61, 0.06);
    }
    .metric-label {
        color: #637786;
        font-size: 0.86rem;
        font-weight: 650;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #102033;
        font-size: 1.55rem;
        font-weight: 780;
        line-height: 1.1;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    @media (max-width: 760px) {
        .metric-grid {
            grid-template-columns: 1fr 1fr;
        }
        .hero {
            padding: 22px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

top_left, top_right = st.columns([1.6, 1])
with top_left:
    st.markdown(
        """
        <div class="hero">
          <div class="eyebrow">Feedback intelligence</div>
          <h1>UserLens AI</h1>
          <p>Turn scattered user feedback into executive-ready opportunity areas, hypotheses, and roadmap actions.</p>
          <div class="mini-flow">1. Upload feedback · 2. Review signals · 3. Act on the top opportunity</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with top_right:
    with st.container(border=True):
        st.markdown('<div class="input-heading">Upload your CSV</div>', unsafe_allow_html=True)
        uploaded = st.file_uploader(
            "Upload feedback CSV",
            type=["csv"],
            label_visibility="collapsed",
            help="Expected columns: source, user_type, date, feedback",
        )
        st.markdown('<div class="input-heading">Try sample data</div>', unsafe_allow_html=True)
        sample_name = st.selectbox("Sample dataset", list(SAMPLES.keys()), label_visibility="collapsed")
        sample_path = SAMPLES[sample_name]
        st.download_button(
            "Download sample CSV",
            sample_path.read_text(encoding="utf-8"),
            file_name=sample_path.name,
            mime="text/csv",
            width="stretch",
        )
        st.caption("No CSV uploaded? The selected sample runs automatically.")


def load_records():
    if uploaded is not None:
        text = uploaded.getvalue().decode("utf-8")
        return load_feedback_csv(io.StringIO(text))
    return load_feedback_csv(SAMPLES[sample_name])


records = load_records()

if not records:
    st.info("Upload a CSV or use the sample feedback to generate insights.")
    st.stop()

analysis = analyze_feedback(records)
report = write_markdown_report(analysis)
top = analysis["top_opportunity"]

st.markdown(
    f"""
    <div class="metric-grid">
      <div class="metric-card"><div class="metric-label">Feedback records</div><div class="metric-value">{analysis['total_feedback']}</div></div>
      <div class="metric-card"><div class="metric-label">Opportunity themes</div><div class="metric-value">{len(analysis['opportunities'])}</div></div>
      <div class="metric-card"><div class="metric-label">Top score</div><div class="metric-value">{top['opportunity_score']}</div></div>
      <div class="metric-card"><div class="metric-label">Top theme</div><div class="metric-value">{top['theme']}</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-heading">Executive Decision Brief</div>', unsafe_allow_html=True)
brief_cols = st.columns([1.2, 1])
with brief_cols[0]:
    st.markdown(
        f"""
        <div class="brief-card">
          <div class="brief-label">Top opportunity</div>
          <div class="brief-title">{top['theme']}</div>
          <div class="brief-text">{top['need']}</div>
          <div class="brief-label">Recommended hypothesis</div>
          <div class="brief-text">{top['hypothesis']}</div>
          <span class="score-pill">Opportunity score {top['opportunity_score']}/100</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with brief_cols[1]:
    evidence_items = "".join(f"<li>{evidence}</li>" for evidence in top["evidence"])
    st.markdown(
        f"""
        <div class="brief-card">
          <div class="brief-label">Evidence</div>
          <ul class="evidence-list">{evidence_items}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.download_button(
    "Download Roadmap Report",
    report,
    file_name="userlens_feedback_report.md",
    mime="text/markdown",
)

st.markdown('<div class="section-heading">Prioritized Opportunities</div>', unsafe_allow_html=True)
card_cols = st.columns(3)
for index, opportunity in enumerate(analysis["opportunities"][:3], start=1):
    with card_cols[index - 1]:
        st.markdown(
            f"""
            <div class="opportunity-card">
              <div class="rank">#{index} opportunity</div>
              <div class="opp-title">{opportunity['theme']}</div>
              <div class="opp-meta">{opportunity['frequency']} signals · {opportunity['dominant_user_type']} · {opportunity['sentiment']}</div>
              <span class="score-pill">Score {opportunity['opportunity_score']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

opportunity_df = pd.DataFrame(analysis["opportunities"])
with st.expander("View opportunity table"):
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
