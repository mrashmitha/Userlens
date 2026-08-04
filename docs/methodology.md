# Methodology

## Does The MVP Use An LLM?

No. The current MVP does not use an LLM for pattern detection or scoring.

This is intentional for the first public version:

- Anyone can run the demo without an API key.
- Results are deterministic and easy to explain.
- Recruiters and interviewers can inspect the logic directly.
- The product demonstrates the workflow before adding model complexity.

## Pattern Detection

Pattern detection uses a transparent taxonomy in `core/taxonomy.py`.

Each feedback item is compared against keyword groups such as:

- Onboarding friction
- Admin and permissions
- Reporting and visibility
- Pricing and packaging
- Workflow efficiency
- Trust and reliability

The theme with the strongest keyword match becomes the detected pattern. If no theme matches, the item is labeled as general feedback.

## Sentiment And Urgency

Sentiment and urgency are also rule-based in the MVP.

Sentiment checks whether the feedback contains positive or negative signal words. Urgency checks for words that imply blocking risk, compliance risk, broken workflows, or time-sensitive issues.

## Opportunity Scoring

The opportunity score is calculated in `core/analyzer.py`:

```text
score = frequency * 12 + negative_count * 8 + high_urgency_count * 15
```

The score is capped at 100.

This simple scoring model helps PMs compare opportunity areas using three interpretable signals:

- Frequency: how often the theme appears
- Negative sentiment: how painful the theme feels
- High urgency: whether the issue blocks adoption, trust, or rollout

## Where An LLM Fits Next

An LLM should be added after the deterministic workflow proves useful. Good next steps:

- Use an LLM to extract themes from longer interview transcripts.
- Use an LLM to summarize evidence snippets into sharper product insights.
- Use an LLM to generate research questions for each hypothesis.
- Use embeddings to cluster semantically similar feedback that does not share exact keywords.
- Add confidence labels and citations so users can trace every insight back to source feedback.

## Why This Matters For Product Management

The MVP is built to show the product workflow clearly: raw feedback becomes patterns, patterns become hypotheses, and hypotheses become prioritization inputs.

The AI roadmap should improve synthesis quality, but the product value is the decision loop.

## Evaluation Baseline

The MVP includes deterministic evals in `evals/`.

These evals check:

- Whether expected themes appear for each sample dataset.
- Whether each opportunity includes evidence snippets.
- Whether each opportunity includes a user need and hypothesis.

This gives UserLens a baseline before adding LLM-assisted synthesis. Future AI features should improve synthesis quality without reducing evidence grounding or actionability.
