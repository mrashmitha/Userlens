from core.analyzer import FeedbackRecord, analyze_feedback, classify_theme


def test_classifies_admin_permissions_theme():
    assert classify_theme("Roles and permissions are unclear for admins") == "Admin and permissions"


def test_analyze_feedback_prioritizes_high_urgency_patterns():
    records = [
        FeedbackRecord("Support", "Admin", "SSO is broken and we are blocked"),
        FeedbackRecord("Interview", "Admin", "Permissions are unclear"),
        FeedbackRecord("Survey", "Buyer", "Pricing is confusing"),
    ]

    analysis = analyze_feedback(records)

    assert analysis["total_feedback"] == 3
    assert analysis["top_opportunity"]["theme"] == "Admin and permissions"
    assert analysis["top_opportunity"]["opportunity_score"] > 0

