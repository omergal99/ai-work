# Evaluation Suite

## Purpose
This folder defines how agent behavior is tested and improved over time.

## Evaluation Types
- capability evals: measure whether the agent can perform important tasks
- regression evals: protect known-good behavior
- quality evals: check clarity, correctness, and tool use
- drift evals: detect degradation over time

## Recommended Structure
- cases/: concrete task cases
- rubrics/: scoring rules
- reports/: latest results
- harness/: runner logic

## Core Principles
- Use deterministic checks where possible
- Use rubric-based checks for open-ended quality
- Keep tasks grounded in real use cases
- Review transcripts and traces regularly

## Integration With the Repo
Every major feature should have at least one eval case before it is considered stable.
