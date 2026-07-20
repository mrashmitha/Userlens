# Product Requirements Document

## UserLens AI: Feedback Intelligence for Faster Product Decisions

**Status:** MVP shipped  
**Owner:** Rashmitha Mamillapalli  
**Repository:** github.com/mrashmitha/Userlens  

## 1. Problem

Product teams collect feedback continuously, but the signal is scattered across interviews, support tickets, surveys, sales calls, and internal notes. PMs often wait 3-4 weeks for formal research synthesis before they can confidently identify patterns, validate hypotheses, or make roadmap tradeoffs.

This delay creates three problems:

- Important user friction is discovered after design or engineering work has started.
- PMs rely on anecdotal feedback because synthesis takes too long.
- Roadmap decisions are made without a clear view of frequency, severity, and affected user segments.

## 2. Target Users

- Product managers making roadmap and prioritization decisions
- UX researchers looking for early signal detection before deeper studies
- Designers validating where users are confused before committing to flows
- Startup founders synthesizing qualitative feedback without a research team

## 3. Value Proposition

UserLens AI turns raw user feedback into near-real-time product intelligence: repeated themes, sentiment, urgency, user needs, hypotheses, and prioritized opportunities.

It does not replace formal research. It helps teams learn faster and decide what deserves deeper validation.

## 4. MVP Scope

### In Scope

- Upload or use a sample feedback CSV
- Download sample feedback datasets for testing
- Redact obvious PII before analysis
- Classify each feedback item into a product theme
- Label sentiment and urgency
- Group feedback into product opportunities
- Score opportunities using frequency, negative sentiment, and high urgency
- Generate a Markdown report with evidence snippets and hypotheses

### Out of Scope

- Login/authentication
- Production database
- Real-time third-party integrations
- LLM API calls
- Embedding-based clustering
- Persona chat
- Full research repository management

## 5. User Journey

1. PM opens UserLens AI.
2. PM uploads a CSV of user feedback or uses the included sample dataset.
3. UserLens redacts common PII patterns.
4. UserLens classifies feedback into product themes.
5. PM sees prioritized opportunities and evidence snippets.
6. PM downloads a Markdown report for roadmap, research, or design discussions.

## 6. Success Criteria

- A new user can run the app locally in under five minutes.
- The sample dataset produces multiple product opportunity themes.
- The top opportunity includes evidence, affected user segment, and a hypothesis.
- PII redaction tests pass for emails, phone numbers, and IP addresses.
- The repo clearly communicates PM judgment, technical execution, and roadmap thinking.

## 7. Product Metrics

For a real product launch, success would be measured through:

- Time from raw feedback to synthesis
- Number of actionable themes identified per dataset
- PM confidence in prioritization decisions
- Reduction in repeated unresolved feedback themes after product changes ship
- Number of hypotheses moved into discovery, prototype, or roadmap review

## 8. Opportunity Scoring

The MVP scores each opportunity using:

- Theme frequency
- Negative sentiment count
- High-urgency count

The score is intentionally simple and explainable for an MVP. A future version could add account value, customer segment, retention risk, and confidence scoring.

The current MVP does not use an LLM for pattern detection or scoring. The methodology is documented in [methodology.md](methodology.md).

## 9. AI Roadmap

The first version is local-first so anyone can test it without API keys. The next version should add LLM-assisted synthesis:

- Extract nuanced themes from long-form interview transcripts
- Generate clearer opportunity narratives
- Suggest research questions for each hypothesis
- Summarize evidence with confidence labels
- Integrate with Slack, Zendesk, Intercom, Dovetail, Productboard, and Linear

## 10. Interview Positioning

UserLens AI demonstrates the core skill set of an AI Product Manager:

- Translating an ambiguous workflow problem into an MVP
- Designing a human-in-the-loop AI product
- Protecting user privacy before analysis
- Creating explainable prioritization logic
- Shipping a working product with tests, examples, and documentation
