# Product Decisions

## Positioning

UserLens AI is a feedback intelligence tool for product managers. It helps teams identify user research patterns earlier, form sharper hypotheses, and make better prioritization decisions before a full research cycle is complete.

## Why This MVP Is Local-First

The first version does not require an LLM API key. That makes it easy for recruiters, hiring managers, and interviewers to run the demo in under five minutes.

The local classifier is intentionally transparent:

- Product themes are mapped through a visible taxonomy.
- PII redaction happens before analysis.
- Opportunity scores are simple enough to explain in an interview.
- The output is reproducible from the sample dataset.

No LLM is used in the MVP. This is a product scoping decision, not a technical limitation. The first release proves the workflow and makes the prioritization logic inspectable.

## What AI Adds Next

The next layer should add LLM-assisted synthesis after the deterministic pipeline:

1. Better theme extraction from long-form interviews.
2. More nuanced product hypotheses.
3. Evidence-backed summaries with confidence labels.
4. Integrations with Slack, Zendesk, Intercom, Dovetail, Productboard, or Linear.

## What This Product Does Not Claim

UserLens AI does not replace formal user research. It helps PMs make sense of weak signals earlier and decide what deserves deeper validation.
