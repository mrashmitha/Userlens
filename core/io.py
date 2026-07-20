"""CSV loading utilities for UserLens AI."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import TextIO

from core.analyzer import FeedbackRecord


def _get(row: dict, *names: str) -> str:
    normalized = {key.strip().lower(): value for key, value in row.items()}
    for name in names:
        value = normalized.get(name)
        if value:
            return value.strip()
    return ""


def load_feedback_csv(file_obj: TextIO | Path | str) -> list[FeedbackRecord]:
    if isinstance(file_obj, (Path, str)):
        with open(file_obj, newline="", encoding="utf-8") as handle:
            return load_feedback_csv(handle)

    reader = csv.DictReader(file_obj)
    records = []
    for row in reader:
        feedback = _get(row, "feedback", "comment", "text", "response")
        if not feedback:
            continue
        records.append(
            FeedbackRecord(
                source=_get(row, "source", "channel") or "Unknown",
                user_type=_get(row, "user_type", "segment", "persona") or "Unknown user",
                date=_get(row, "date", "created_at"),
                feedback=feedback,
            )
        )
    return records

