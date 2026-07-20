from core.pii import contains_pii, redact_pii


def test_redacts_email_phone_and_ip():
    text = "Email maya@example.com, call 312-555-1212, IP 10.0.0.1"

    redacted = redact_pii(text)

    assert "maya@example.com" not in redacted
    assert "312-555-1212" not in redacted
    assert "10.0.0.1" not in redacted
    assert "[EMAIL]" in redacted
    assert "[PHONE]" in redacted
    assert "[IP_ADDRESS]" in redacted


def test_contains_pii_detects_supported_patterns():
    assert contains_pii("customer email is test@example.com")

