# Business Case

## Why UserLens AI Matters

Product teams already collect user feedback, but turning that feedback into decisions is slow. Feedback is scattered across interviews, support tickets, sales calls, surveys, app reviews, and internal notes.

UserLens AI reduces the time from raw feedback to product insight by creating a first-pass synthesis: themes, urgency signals, opportunity scores, evidence snippets, and hypotheses to validate.

## Impact Of Not Having It

Without a workflow like UserLens, teams are more likely to:

- Prioritize based on anecdotes instead of repeated patterns.
- Miss early warning signs in onboarding, pricing, permissions, reliability, or workflow friction.
- Wait weeks for synthesis before deciding what to validate.
- Discover user confusion after design or engineering work has started.
- Spend PM, design, research, and engineering time on avoidable rework.

## ROI Model

The MVP includes a conservative business impact estimate.

```text
manual_hours = 1 hour base synthesis time + 3 minutes per feedback item
userlens_hours = 0.25 hour base review time + 0.35 minutes per feedback item
hours_saved = manual_hours - userlens_hours
cost_savings = hours_saved * loaded_hourly_cost
```

Default assumptions:

- 4 feedback review cycles per month
- $100/hour loaded PM, researcher, or product team cost
- Human review is still required

## Example

For 50 feedback records:

```text
Manual review estimate: 3.5 hours
UserLens-assisted estimate: 0.5 hours
Savings: 3.0 hours per cycle
Cost savings: $300 per cycle
Annualized impact at 4 cycles/month: $14,400
```

These are planning estimates, not production claims. The goal is to help PMs explain the value of faster synthesis and better prioritization.

## Strongest Business Value

The largest benefit is not only labor savings. It is earlier decision quality:

- Faster discovery of repeated user pain
- Better prioritization evidence
- Clearer research hypotheses
- Lower risk of late-stage design or engineering rework
- Better alignment between PM, design, research, and leadership

