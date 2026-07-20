"""Markdown report generation for UserLens AI."""

from __future__ import annotations

from datetime import date


def write_markdown_report(analysis: dict) -> str:
    top = analysis.get("top_opportunity")
    lines = [
        "# UserLens AI Feedback Intelligence Report",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Feedback records analyzed: {analysis['total_feedback']}",
        "",
        "## Executive Summary",
        "",
    ]

    if not top:
        lines.append("No feedback records were available for analysis.")
        return "\n".join(lines)

    lines.extend(
        [
            f"The strongest opportunity is **{top['theme']}** with an opportunity score of **{top['opportunity_score']}/100**.",
            f"This pattern appears most often among **{top['dominant_user_type']}** users.",
            "",
            "## Prioritized Opportunities",
            "",
            "| Rank | Theme | Frequency | Dominant User | Sentiment | High Urgency | Score |",
            "|---:|---|---:|---|---|---:|---:|",
        ]
    )

    for index, item in enumerate(analysis["opportunities"], start=1):
        lines.append(
            f"| {index} | {item['theme']} | {item['frequency']} | {item['dominant_user_type']} | "
            f"{item['sentiment']} | {item['high_urgency_count']} | {item['opportunity_score']} |"
        )

    lines.extend(["", "## Roadmap-Ready Insights", ""])
    for item in analysis["opportunities"]:
        lines.extend(
            [
                f"### {item['theme']}",
                "",
                f"**User need:** {item['need']}",
                "",
                f"**Hypothesis to validate:** {item['hypothesis']}",
                "",
                "**Evidence snippets:**",
            ]
        )
        for evidence in item["evidence"]:
            lines.append(f"- {evidence}")
        lines.append("")

    lines.extend(
        [
            "## Recommended Next Research Actions",
            "",
            "1. Run five targeted interviews around the top two opportunity themes.",
            "2. Prototype the highest-scoring workflow improvement before engineering commitment.",
            "3. Track whether the theme frequency declines after the design change ships.",
            "",
            "## PM Decision Framing",
            "",
            "UserLens AI does not replace formal user research. It helps product teams detect weak signals earlier, form sharper hypotheses, and decide what deserves deeper validation.",
        ]
    )
    return "\n".join(lines)

