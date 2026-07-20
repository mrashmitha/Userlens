"""PII redaction helpers for local feedback analysis."""

from __future__ import annotations

import re


PII_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[EMAIL]"),
    (r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b", "[PHONE]"),
    (r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "[IP_ADDRESS]"),
    (r"\b(?:user|customer|account|tenant)[-_ ]?id[:= ]+[A-Za-z0-9-]+\b", "[USER_ID]"),
)


def redact_pii(text: str) -> str:
    """Mask common PII patterns while preserving enough context for synthesis."""
    cleaned = str(text)
    for pattern, replacement in PII_PATTERNS:
        cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)
    return cleaned


def contains_pii(text: str) -> bool:
    """Return True when any supported PII pattern is found."""
    return any(re.search(pattern, str(text), flags=re.IGNORECASE) for pattern, _ in PII_PATTERNS)

