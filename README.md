DOC_ID: AI_CONFIG_01
Keywords: agent-config, orchestration, evals, skills, prompts

# AI Work Config

## What this repository is
This repository is a compact AI operating system for agents and humans working across a workspace.
Its purpose is to make agent work more predictable, more reusable, and easier to review by keeping shared rules, context, workflows, evaluation guidance, and knowledge in one coherent place.

## Why it exists
The goal is not to force one rigid process. The goal is to give every agent and every developer a shared baseline for how to work:
- preserve context and memory
- keep workflows structured
- reduce hallucination through evidence and review
- make handoffs and collaboration clearer
- keep knowledge reusable across projects and tools

## Main layers
- config/ — the first-read layer for shared state, memory, and onboarding guidance
- core/ — the consolidated operational layer for agents, protocols, prompts, skills, templates, ops, and related standards
- genai-flow/ — product-level guidance for LLM behavior, RAG, drift handling, and evaluation
- knowledge/ — curated design, roadmap, adoption, efficiency, and token guidance
- docs/ — roadmap and next-step notes

## How to use it
1. Start with this README.
2. Read config/README.md for the first-stop rules.
3. Read core/README.md for the consolidated operating structure.
4. Open the relevant section in genai-flow/ or knowledge/ for the task at hand.
5. Keep shared state explicit, reviewable, and evidence-based.

## Simple mental model
```text
Shared config -> core operating rules -> agent roles -> workflows -> evals -> better outcomes
```

## Suggested next additions
- a shared agent registry
- a lightweight decision log format
- template-driven workflow examples for common agent tasks
- more eval cases for drift, retrieval quality, and review quality
