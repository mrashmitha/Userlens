# UserLens AI Evaluation Results

| Dataset | Records | Theme Recall | Evidence Grounded | Actionable Outputs | Result |
|---|---:|---:|---|---|---|
| examples/sample_feedback.csv | 12 | 100% | True | True | Pass |
| examples/sample_mobile_app_feedback.csv | 10 | 100% | True | True | Pass |
| examples/sample_ecommerce_feedback.csv | 10 | 100% | True | True | Pass |
| examples/sample_b2b_support_feedback.csv | 10 | 100% | True | True | Pass |

## Evaluation Criteria

- Theme recall checks whether expected product themes appear in the output.
- Evidence grounding checks whether each opportunity includes source feedback snippets.
- Actionability checks whether each opportunity includes a user need and hypothesis.

These evals test the deterministic MVP. Future LLM evals should add hallucination checks, citation accuracy, and human-rated usefulness.
