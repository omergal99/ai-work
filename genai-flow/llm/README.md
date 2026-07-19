# LLM Strategy

This area is the operating playbook for making LLM-based agents more robust, more diverse, and less likely to hallucinate.

## Core principles
- Use multiple perspectives instead of one deterministic answer.
- Introduce controlled variation in temperature, model choice, and role framing when appropriate.
- Use debate-style review loops to expose weak assumptions.
- Combine evidence-backed reasoning with retrieval and explicit verification steps.
- Keep drift visible through evals, reviews, and traceable decision records.

## Recommended operating pattern
1. Create one primary answer path.
2. Add a critic or judge role to challenge it.
3. Require every high-impact claim to be linked to evidence or retrieved context.
4. Compare outputs over time and flag drift.
5. Keep the final response short, grounded, and reviewable.

## Strong patterns
- LLM-as-a-judge: use a secondary model or role to critique, score, or validate outputs.
- Debate agents: let specialist agents challenge each other before finalizing a result.
- Role variation: rotate hats such as critic, explainer, skeptic, and implementer.
- Evidence-first reasoning: require claims to be tied to source context or retrieved evidence.
- Drift detection: compare outputs over time and flag deviations that may signal prompt or state drift.
- LoRA and adaptation concepts: treat adaptation as a tool for consistency, but keep the base workflow grounded and auditable.

## Pattern library
- patterns/llm-as-a-judge.md
- patterns/debate_agents.md
- patterns/temperature_and_model_variation.md
- patterns/evidence_and_drift.md

## Why this matters
Variety reduces false confidence. When an agent sees multiple angles and must justify its answer with evidence, the result becomes more reliable and easier to review.
