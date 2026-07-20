"""Local-first feedback intelligence engine for UserLens AI."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable

from core.pii import redact_pii
from core.taxonomy import SENTIMENT_KEYWORDS, THEME_KEYWORDS, URGENCY_KEYWORDS


@dataclass(frozen=True)
class FeedbackRecord:
    source: str
    user_type: str
    feedback: str
    date: str = ""


def classify_theme(text: str) -> str:
    lower = text.lower()
    scores = {
        theme: sum(1 for keyword in keywords if keyword in lower)
        for theme, keywords in THEME_KEYWORDS.items()
    }
    best_theme, best_score = max(scores.items(), key=lambda item: item[1])
    return best_theme if best_score > 0 else "General feedback"


def classify_sentiment(text: str) -> str:
    lower = text.lower()
    negative = sum(1 for keyword in SENTIMENT_KEYWORDS["Negative"] if keyword in lower)
    positive = sum(1 for keyword in SENTIMENT_KEYWORDS["Positive"] if keyword in lower)
    if negative > positive:
        return "Negative"
    if positive > negative:
        return "Positive"
    return "Neutral"


def classify_urgency(text: str) -> str:
    lower = text.lower()
    for urgency, keywords in URGENCY_KEYWORDS.items():
        if any(keyword in lower for keyword in keywords):
            return urgency
    return "Low"


def extract_need(text: str, theme: str) -> str:
    need_map = {
        "Onboarding friction": "Help new users reach first value with less setup ambiguity.",
        "Admin and permissions": "Make access control, roles, and admin actions easier to understand.",
        "Reporting and visibility": "Give teams clearer visibility into status, outcomes, and exports.",
        "Pricing and packaging": "Clarify package value and reduce uncertainty before purchase or upgrade.",
        "Workflow efficiency": "Reduce repetitive manual work and make high-frequency tasks faster.",
        "Trust and reliability": "Increase confidence that the product is accurate, stable, and safe.",
        "General feedback": "Investigate the request through follow-up research before roadmap commitment.",
    }
    return need_map.get(theme, need_map["General feedback"])


def build_hypothesis(theme: str, user_type: str) -> str:
    hypothesis_map = {
        "Onboarding friction": f"If {user_type.lower()} users get guided setup and clearer next steps, activation will improve.",
        "Admin and permissions": f"If {user_type.lower()} users get simpler role explanations and permission previews, setup errors will decrease.",
        "Reporting and visibility": f"If {user_type.lower()} users get clearer dashboards and exports, decision confidence will increase.",
        "Pricing and packaging": f"If {user_type.lower()} users see clearer plan comparisons, conversion confidence will improve.",
        "Workflow efficiency": f"If repetitive tasks are batched or automated for {user_type.lower()} users, task completion time will decrease.",
        "Trust and reliability": f"If reliability issues are made visible and recoverable, {user_type.lower()} users will trust the workflow more.",
        "General feedback": f"If the team interviews {user_type.lower()} users about this feedback, roadmap confidence will improve.",
    }
    return hypothesis_map.get(theme, hypothesis_map["General feedback"])


def score_opportunity(frequency: int, negative_count: int, high_urgency_count: int) -> int:
    return min(100, (frequency * 12) + (negative_count * 8) + (high_urgency_count * 15))


def analyze_feedback(records: Iterable[FeedbackRecord]) -> dict:
    analyzed = []
    for record in records:
        redacted = redact_pii(record.feedback)
        theme = classify_theme(redacted)
        sentiment = classify_sentiment(redacted)
        urgency = classify_urgency(redacted)
        analyzed.append(
            {
                "source": record.source,
                "user_type": record.user_type or "Unknown user",
                "date": record.date,
                "feedback": redacted,
                "theme": theme,
                "sentiment": sentiment,
                "urgency": urgency,
                "need": extract_need(redacted, theme),
            }
        )

    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in analyzed:
        grouped[item["theme"]].append(item)

    opportunities = []
    for theme, items in grouped.items():
        user_types = Counter(item["user_type"] for item in items)
        sentiment_counts = Counter(item["sentiment"] for item in items)
        urgency_counts = Counter(item["urgency"] for item in items)
        dominant_user_type = user_types.most_common(1)[0][0]
        frequency = len(items)
        score = score_opportunity(
            frequency=frequency,
            negative_count=sentiment_counts["Negative"],
            high_urgency_count=urgency_counts["High"],
        )
        opportunities.append(
            {
                "theme": theme,
                "frequency": frequency,
                "dominant_user_type": dominant_user_type,
                "sentiment": sentiment_counts.most_common(1)[0][0],
                "high_urgency_count": urgency_counts["High"],
                "opportunity_score": score,
                "need": items[0]["need"],
                "hypothesis": build_hypothesis(theme, dominant_user_type),
                "evidence": [item["feedback"] for item in items[:3]],
            }
        )

    opportunities.sort(key=lambda item: item["opportunity_score"], reverse=True)
    return {
        "total_feedback": len(analyzed),
        "records": analyzed,
        "opportunities": opportunities,
        "top_opportunity": opportunities[0] if opportunities else None,
    }

