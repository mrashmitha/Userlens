"""Product feedback taxonomy used by the MVP classifier."""

from __future__ import annotations

THEME_KEYWORDS: dict[str, list[str]] = {
    "Onboarding friction": [
        "onboarding",
        "setup",
        "start",
        "getting started",
        "first time",
        "invite",
        "activation",
        "configure",
    ],
    "Admin and permissions": [
        "admin",
        "permission",
        "role",
        "access",
        "tenant",
        "security",
        "audit",
        "sso",
    ],
    "Reporting and visibility": [
        "report",
        "dashboard",
        "visibility",
        "export",
        "analytics",
        "metrics",
        "status",
    ],
    "Pricing and packaging": [
        "price",
        "pricing",
        "plan",
        "upgrade",
        "billing",
        "seat",
        "trial",
        "cost",
    ],
    "Workflow efficiency": [
        "slow",
        "manual",
        "bulk",
        "repeat",
        "automate",
        "workflow",
        "time",
        "copy",
    ],
    "Trust and reliability": [
        "bug",
        "broken",
        "error",
        "trust",
        "reliable",
        "sync",
        "missing",
        "incorrect",
    ],
}

SENTIMENT_KEYWORDS: dict[str, list[str]] = {
    "Negative": [
        "confusing",
        "frustrated",
        "blocked",
        "hard",
        "difficult",
        "annoying",
        "missing",
        "broken",
        "unclear",
        "slow",
        "worried",
    ],
    "Positive": [
        "love",
        "helpful",
        "easy",
        "clear",
        "fast",
        "great",
        "useful",
        "works",
    ],
}

URGENCY_KEYWORDS: dict[str, list[str]] = {
    "High": ["blocked", "cannot", "can't", "churn", "urgent", "security", "compliance", "broken"],
    "Medium": ["need", "missing", "hard", "manual", "unclear", "slow", "confusing"],
}

