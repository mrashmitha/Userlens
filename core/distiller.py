"""Backward-compatible facade for the original UserLens distiller class."""

from __future__ import annotations

from typing import Dict, List

from core.analyzer import FeedbackRecord, analyze_feedback
from core.pii import redact_pii


class UserLensDistiller:
    """Transforms raw user feedback into roadmap-ready product insights."""

    def scrub_pii(self, raw_text: str) -> str:
        return redact_pii(raw_text)

    def generate_persona_schema(self, text_chunks: List[str]) -> Dict:
        records = [
            FeedbackRecord(source="Text chunk", user_type="Unknown user", feedback=chunk)
            for chunk in text_chunks
        ]
        analysis = analyze_feedback(records)
        return {"status": "complete", "persona_clusters": analysis["opportunities"]}

    def analyze(self, records: List[FeedbackRecord]) -> Dict:
        return analyze_feedback(records)

