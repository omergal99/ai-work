# Token Economics and Cost Control

## Executive Summary
The cost problem in agentic systems is not only model price. It is context churn, repeated history, and poorly scoped retrieval.

## Key Findings
- Long conversational sessions resend prior context repeatedly.
- Large context windows can increase cost and latency even when the model is capable of handling them.
- The best fix is early, deliberate compaction rather than waiting for runaway context growth.

## Recommended Operating Rules
- Compact long sessions before they reach extreme size.
- Prefer small, dense reasoning prompts over large text dumps.
- Use retrieval triggers and state manifests instead of feeding the full repo into every prompt.
- Use budget windows and cost guards at the agent runtime level.

## Practical Thresholds
- For 1M-token windows, a proactive compaction threshold around 250K tokens is a strong starting point.
- Use automated compaction to cut history to a compact summary before the next agent loop.

## Example Policy
- If session tokens exceed the safe threshold, compact to a summarized state and continue with a reduced context window.
- Keep the compacted state focused on objectives, latest results, blockers, and next actions.

## Repository Integration
- Enforce token budgets in the shared state manifest.
- Track token usage in evals and observability logs.
- Use retrieval-first behavior to avoid repeated context bloat.
