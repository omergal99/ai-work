# Freshness and Evidence Handling

## Purpose
Prevent stale or outdated context from dominating the reasoning process.

## Principles
- distinguish stable knowledge from volatile knowledge
- prefer current evidence when freshness matters
- require explicit handling of uncertainty when sources conflict

## Recommended pattern
1. Label evidence by freshness and confidence.
2. Prefer newer evidence for dynamic topics.
3. Keep older evidence as background context when it remains valid.
4. Flag unresolved conflicts for review.

## Benefits
- improves trustworthiness
- reduces stale answers
- makes uncertainty visible

## Guardrails
- do not silently ignore outdated evidence without explanation
- keep support for freshness explicit in the workflow
- surface uncertainty rather than hiding it
