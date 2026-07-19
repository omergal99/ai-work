# Temperature and Model Variation

## Purpose
Introduce controlled variability to reduce overconfident or brittle behavior.

## Principles
- keep the main path stable
- vary the model or temperature only when the task needs a second perspective
- use variation to expose weak assumptions, not to create noise

## Recommended approach
- use a lower temperature for deterministic execution tasks
- use a higher temperature or alternative model for brainstorming, critique, or option generation
- keep the final answer anchored to the strongest evidence or the most reliable model

## Benefits
- improves diversity of reasoning
- reduces false confidence
- helps identify fragile answers

## Guardrails
- do not rely on randomness blindly
- always evaluate the result after variation
- avoid using multiple models just for the sake of it
