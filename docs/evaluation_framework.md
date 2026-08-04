# Evaluation Framework

## Why Evaluation Matters

UserLens AI is designed for product decisions, so outputs need to be trustworthy. The evaluation framework checks whether the system finds expected themes, grounds insights in feedback evidence, and produces actionable product outputs.

## Current MVP Evals

Run evals with:

```bash
python evals/eval_runner.py
```

The current evals check:

- **Theme recall:** expected product themes appear in the output.
- **Evidence grounding:** every opportunity includes source feedback snippets.
- **Actionability:** every opportunity includes a user need and hypothesis.

Current results are published in [eval_results.md](../evals/eval_results.md).

## Why These Evals Are Useful

They make the product more credible because the repo does not just show an output. It shows how the output is checked.

This is especially important before adding LLM features. A deterministic baseline gives the team something to compare future AI-enhanced synthesis against.

## Future LLM Evals

When UserLens adds LLM-assisted synthesis, the eval framework should expand to check:

- Hallucination risk: does the model invent facts not found in feedback?
- Citation accuracy: does each insight cite the correct evidence?
- Theme quality: are themes specific, useful, and non-overlapping?
- Recommendation quality: is the suggested action clear enough for a PM?
- Consistency: are outputs stable across repeated runs?
- Human usefulness: would PMs or researchers act on this output?

## AI Evaluation Principle

The goal is not to make AI sound impressive. The goal is to make AI outputs useful, evidence-backed, and safe enough to support product judgment.

