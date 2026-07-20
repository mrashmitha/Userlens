# How To Test UserLens AI

Thank you for testing UserLens AI.

UserLens AI helps product teams turn scattered user feedback into product themes, opportunity scores, hypotheses, and an executive decision brief.

## Live App

Open the app here:

[Test UserLens AI](https://userlensai-uixn8nwtchddbfycj369hy.streamlit.app/)

## What To Test

Please spend 5-10 minutes testing the core workflow.

### 1. Start With The Default Sample

When you open the app, UserLens automatically runs a sample feedback dataset.

Check:

- Can you understand the top product opportunity within 30 seconds?
- Do the KPI cards make sense?
- Is the Executive Decision Brief clear?
- Does the evidence support the top opportunity?

### 2. Try A Different Sample

Use the sample dropdown to switch datasets.

Try at least one:

- SaaS onboarding
- Mobile app reviews
- E-commerce checkout
- B2B support tickets

Check:

- Does the dashboard update clearly?
- Are the top themes different across samples?
- Does the result feel useful for product decision-making?

### 3. Download And Re-Upload A Sample

Click **Download sample**, then upload that CSV through **Browse files**.

Check:

- Is it obvious how to upload feedback?
- Does the app process the uploaded file correctly?
- Is the upload flow easy to follow?

### 4. Download The Roadmap Report

Click **Download Roadmap Report**.

Check:

- Would this report be useful in a roadmap, research, or design review?
- Are the hypotheses actionable?
- Is the evidence easy to understand?

## Feedback Questions

Please share feedback on:

1. What was clear?
2. What was confusing?
3. What insight felt most useful?
4. What would make this more valuable for a PM or UX researcher?
5. Would you trust this as an early signal before formal research? Why or why not?

## Test Data Format

If you want to test your own file, upload a CSV with these columns:

```csv
source,user_type,date,feedback
Interview,Admin user,2026-07-01,"The permissions screen is unclear."
Support ticket,First-time user,2026-07-02,"Onboarding was confusing."
```

## Important Note

This MVP does not use an LLM yet. Pattern detection and scoring are deterministic so testers can run the app without an API key and understand how the results are produced.

Read more in [methodology.md](methodology.md).
