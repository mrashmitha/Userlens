"""Business impact estimates for feedback synthesis workflows."""

from __future__ import annotations


def estimate_manual_hours(feedback_count: int) -> float:
    """Estimate manual review and synthesis hours for a feedback batch."""
    base_hours = 1.0
    minutes_per_item = 3.0
    return round(base_hours + (feedback_count * minutes_per_item / 60), 1)


def estimate_userlens_hours(feedback_count: int) -> float:
    """Estimate UserLens-assisted review hours, including human review time."""
    base_hours = 0.25
    minutes_per_item = 0.35
    return round(base_hours + (feedback_count * minutes_per_item / 60), 1)


def estimate_roi(
    feedback_count: int,
    cycles_per_month: int = 4,
    loaded_hourly_cost: int = 100,
) -> dict:
    """Return conservative time and cost savings estimates."""
    manual_hours = estimate_manual_hours(feedback_count)
    userlens_hours = estimate_userlens_hours(feedback_count)
    hours_saved_per_cycle = max(0, round(manual_hours - userlens_hours, 1))
    monthly_hours_saved = round(hours_saved_per_cycle * cycles_per_month, 1)
    annual_hours_saved = round(monthly_hours_saved * 12, 1)
    annual_cost_savings = round(annual_hours_saved * loaded_hourly_cost)
    cycle_cost_savings = round(hours_saved_per_cycle * loaded_hourly_cost)

    return {
        "manual_hours": manual_hours,
        "userlens_hours": userlens_hours,
        "hours_saved_per_cycle": hours_saved_per_cycle,
        "cycle_cost_savings": cycle_cost_savings,
        "monthly_hours_saved": monthly_hours_saved,
        "annual_hours_saved": annual_hours_saved,
        "annual_cost_savings": annual_cost_savings,
        "cycles_per_month": cycles_per_month,
        "loaded_hourly_cost": loaded_hourly_cost,
    }

