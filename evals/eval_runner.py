"""Evaluation runner for UserLens AI deterministic synthesis."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.analyzer import analyze_feedback
from core.io import load_feedback_csv

EXPECTED_THEMES = ROOT / "evals" / "expected_themes.json"


def evaluate_dataset(dataset_path: str, expected_themes: list[str]) -> dict:
    records = load_feedback_csv(ROOT / dataset_path)
    analysis = analyze_feedback(records)
    actual_themes = {item["theme"] for item in analysis["opportunities"]}
    expected = set(expected_themes)
    matched = expected & actual_themes
    missed = expected - actual_themes
    unexpected = actual_themes - expected

    theme_recall = round(len(matched) / len(expected), 2) if expected else 1.0
    grounded = all(item["evidence"] for item in analysis["opportunities"])
    actionable = all(item["hypothesis"] and item["need"] for item in analysis["opportunities"])
    passed = theme_recall >= 0.8 and grounded and actionable

    return {
        "dataset": dataset_path,
        "records": len(records),
        "expected_themes": sorted(expected),
        "actual_themes": sorted(actual_themes),
        "matched_themes": sorted(matched),
        "missed_themes": sorted(missed),
        "unexpected_themes": sorted(unexpected),
        "theme_recall": theme_recall,
        "evidence_grounded": grounded,
        "actionable_outputs": actionable,
        "passed": passed,
    }


def run_evals() -> list[dict]:
    expected = json.loads(EXPECTED_THEMES.read_text(encoding="utf-8"))
    return [evaluate_dataset(path, themes) for path, themes in expected.items()]


def write_markdown(results: list[dict]) -> str:
    lines = [
        "# UserLens AI Evaluation Results",
        "",
        "| Dataset | Records | Theme Recall | Evidence Grounded | Actionable Outputs | Result |",
        "|---|---:|---:|---|---|---|",
    ]
    for result in results:
        status = "Pass" if result["passed"] else "Needs review"
        lines.append(
            f"| {result['dataset']} | {result['records']} | {result['theme_recall']:.0%} | "
            f"{result['evidence_grounded']} | {result['actionable_outputs']} | {status} |"
        )

    lines.extend(
        [
            "",
            "## Evaluation Criteria",
            "",
            "- Theme recall checks whether expected product themes appear in the output.",
            "- Evidence grounding checks whether each opportunity includes source feedback snippets.",
            "- Actionability checks whether each opportunity includes a user need and hypothesis.",
            "",
            "These evals test the deterministic MVP. Future LLM evals should add hallucination checks, citation accuracy, and human-rated usefulness.",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    eval_results = run_evals()
    output = write_markdown(eval_results)
    output_path = ROOT / "evals" / "eval_results.md"
    output_path.write_text(output + "\n", encoding="utf-8")
    print(output)
