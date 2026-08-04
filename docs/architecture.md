# Architecture

```mermaid
flowchart LR
    A[Feedback CSV] --> B[PII Redaction]
    B --> C[Theme Classification]
    C --> D[Sentiment and Urgency Labels]
    D --> E[Opportunity Scoring]
    E --> F[Business Impact Estimate]
    F --> G[Roadmap Insights Report]
    G --> H[Evaluation Checks]
```

## Pipeline

1. Load feedback from a CSV file.
2. Redact common PII patterns such as emails, phone numbers, IP addresses, and user IDs.
3. Classify each feedback item into a product theme.
4. Label sentiment and urgency.
5. Group patterns into prioritized opportunities.
6. Estimate time and cost savings from faster synthesis.
7. Generate a Markdown report with evidence snippets and hypotheses to validate.
8. Run eval checks for theme recall, evidence grounding, and actionability.

## Scoring

Opportunity score is based on:

- Frequency of the theme
- Number of negative feedback items
- Number of high-urgency items

The score is capped at 100 so it is easy to compare across themes.

## MVP Method

The current MVP uses deterministic pattern detection and scoring. It does not call an LLM.

This keeps the first version:

- Easy to run without credentials
- Reproducible across demos
- Transparent for product and technical review
- Ready for a future LLM-assisted synthesis layer

See [methodology.md](methodology.md) for the full explanation.
