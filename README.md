# Userlens AI

Near-real-time feedback intelligence for faster product decisions.

Userlens AI helps product managers turn scattered user feedback into product themes, user needs, hypotheses, and roadmap-ready prioritization signals before waiting weeks for a formal research synthesis cycle.

## Why I Built This

Product teams make design and roadmap decisions while feedback is still scattered across interviews, support tickets, surveys, sales notes, and internal docs. Formal research is valuable, but it can take 3-4 weeks to recruit, conduct, synthesize, and socialize findings.

Userlens AI is built around a practical PM workflow:

1. Bring messy feedback into one place.
2. Redact obvious PII.
3. Detect repeated product themes and urgency.
4. Convert those patterns into hypotheses to validate.
5. Use evidence-backed opportunity scores to inform roadmap tradeoffs.

The goal is not to replace user research. The goal is to help product teams learn faster and decide what deserves deeper validation.

## What The MVP Does

- Loads feedback from a CSV file
- Redacts emails, phone numbers, IP addresses, and user/account IDs
- Classifies feedback into product themes
- Labels sentiment and urgency
- Scores product opportunities by frequency, severity, and urgency
- Generates a Markdown report with evidence snippets and hypotheses
- Estimates time and cost savings from faster feedback synthesis
- Includes an evaluation framework for theme recall, evidence grounding, and actionability
- Runs locally without requiring an LLM API key

## Methodology

The MVP does not use an LLM yet. Pattern detection uses a transparent taxonomy, and scoring uses an explainable formula based on frequency, negative sentiment, and urgency. This keeps the first version easy to test, inspect, and discuss in interviews.

Read the full methodology in [docs/methodology.md](docs/methodology.md).

## Business Case

UserLens AI helps reduce the time from raw feedback to product insight. The app includes a conservative ROI estimate based on manual review time, UserLens-assisted review time, review frequency, and loaded hourly cost.

Read the business case in [docs/business_case.md](docs/business_case.md).

## Evaluation

The repo includes lightweight evals so the system can be checked as it evolves.

```bash
python evals/eval_runner.py
```

Current eval results: [evals/eval_results.md](evals/eval_results.md)

## Demo Use Case

A PM has 12 pieces of feedback from interviews, support tickets, sales calls, and in-app surveys. Userlens AI identifies the strongest product opportunity, explains which user segment is most affected, and produces a report the PM can use in roadmap or design discussions.

![UserLens AI demo](assets/userlens-demo.jpg)

Example output:

| Theme | Signal | Product Decision |
|---|---|---|
| Admin and permissions | High urgency, repeated admin confusion | Improve role explanations and permission previews |
| Onboarding friction | First-time evaluators unsure what to do first | Add guided setup and safer invite previews |
| Workflow efficiency | Power users repeating manual work | Explore bulk actions and workspace templates |

## Quickstart

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL and keep "Use sample feedback" enabled.

## Test The App

Try the live app and follow the tester guide:

- [Live UserLens AI app](https://userlensai-uixn8nwtchddbfycj369hy.streamlit.app/)
- [How to test UserLens AI](docs/how_to_test.md)

## CSV Format

Userlens expects a CSV with these columns:

```csv
source,user_type,date,feedback
Interview,First-time evaluator,2026-07-01,"Onboarding was confusing..."
Support ticket,Admin user,2026-07-02,"The permissions screen is unclear..."
```

See [examples/sample_feedback.csv](examples/sample_feedback.csv).

## Product Thinking

This project demonstrates AI product management skills across:

- Problem framing and MVP scoping
- User research synthesis
- Privacy-aware AI workflow design
- Prioritization and roadmap tradeoffs
- Evaluation-first product development
- Clear communication for product, design, and engineering audiences

## Architecture

![UserLens AI workflow](assets/userlens-workflow.svg)

```mermaid
flowchart LR
    A[Feedback CSV] --> B[PII Redaction]
    B --> C[Theme Classification]
    C --> D[Sentiment and Urgency Labels]
    D --> E[Opportunity Scoring]
    E --> F[Roadmap Insights Report]
```

Read more in [docs/architecture.md](docs/architecture.md).

## Repository Guide

- [docs/PRD.md](docs/PRD.md): Product requirements and portfolio narrative
- [docs/how_to_test.md](docs/how_to_test.md): Step-by-step tester guide
- [docs/business_case.md](docs/business_case.md): ROI model and impact framing
- [docs/evaluation_framework.md](docs/evaluation_framework.md): Eval strategy and future LLM checks
- [docs/product_decisions.md](docs/product_decisions.md): MVP tradeoffs and AI roadmap
- [docs/methodology.md](docs/methodology.md): Pattern detection, scoring logic, and future LLM plan
- [docs/demo_results.md](docs/demo_results.md): What the sample demo proves
- [examples/sample_output_report.md](examples/sample_output_report.md): Example generated report
- [evals/eval_results.md](evals/eval_results.md): Current evaluation results
- [tests](tests): Basic PII and analysis tests

## Roadmap

- Add LLM-assisted synthesis for richer evidence-backed summaries
- Add confidence labels for each insight
- Add integrations with Slack, Zendesk, Intercom, Dovetail, Productboard, and Linear
- Add a hypothesis backlog view
- Add before/after tracking to measure whether shipped changes reduce repeated feedback themes
