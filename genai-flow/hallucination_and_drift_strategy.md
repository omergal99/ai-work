# Hallucination and Drift Strategy

## Executive Summary
For customer-facing GenAI products, hallucination and drift are first-class risks. They must be managed with both prevention and detection.

## Prevention
- ground outputs in trusted docs or structured state
- use retrieval with relevance checks
- require explicit tool evidence before claims
- keep prompts concise and task-specific
- route high-risk tasks through stricter verification

## Detection
- run eval suites on representative tasks
- track drift in outputs over time
- compare new outputs to reference baselines
- monitor confidence, tool usage, and retrieval relevance
- inspect transcripts and traces when failures spike

## Drift Signals
- prompt or tool behavior changes without intent
- retrieval quality drops
- outputs become more verbose or less grounded
- customer feedback shifts
- eval pass rates decline

## Operating Policy
If drift or hallucination risk rises, pause rollout, inspect the failing cases, and fix the underlying cause before continuing.
