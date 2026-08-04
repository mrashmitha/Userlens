from core.roi import estimate_roi


def test_estimate_roi_returns_positive_savings():
    roi = estimate_roi(feedback_count=50, cycles_per_month=4, loaded_hourly_cost=100)

    assert roi["manual_hours"] > roi["userlens_hours"]
    assert roi["hours_saved_per_cycle"] > 0
    assert roi["annual_cost_savings"] > 0

