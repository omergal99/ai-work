# Ranking and Top-k Selection

## Purpose
Select the most relevant evidence rather than flooding the model with too much context.

## Principles
- rank retrieved candidates by relevance and usefulness
- keep the top-k small and deliberate
- discard weak or redundant content early

## Recommended pattern
1. Score each candidate.
2. Remove low-value or duplicate items.
3. Keep the top-k strongest results.
4. Pass only that evidence into the reasoning step.

## Benefits
- improves precision
- reduces token waste
- keeps reasoning focused

## Guardrails
- do not choose top-k purely by similarity score without context checks
- keep the selection explainable
- review whether the top-k is too narrow for the task
