# LLM-as-a-Judge

## Purpose
Use a second model or a second role to review, critique, or score a draft answer before it is accepted.

## When to use it
- when the task has high impact or high ambiguity
- when the first answer may be overconfident
- when correctness matters more than speed

## Pattern
1. Generate a draft answer.
2. Ask a judge role to evaluate it for correctness, completeness, risk, and evidence support.
3. Return a revised answer or a clear reason for rejection.
4. Keep the critique short and actionable.

## Benefits
- improves quality control
- exposes hidden assumptions
- reduces hallucinated certainty

## Guardrails
- do not let the judge be too weak or too sycophantic
- require evidence-backed scoring
- keep the workflow auditable
