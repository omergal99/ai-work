# GenAI Flow Layer

## Purpose
This layer captures the operating principles for building a GenAI Flow product that can handle real workloads, many requests, and evolving quality expectations.

## Core design goals
- support many users and many requests
- reduce hallucination risk
- detect drift over time
- keep the system observable and eval-driven
- make flows understandable to both humans and agents

## Product concerns
- hallucination control
- grounding and retrieval quality
- tool reliability
- prompt drift
- state drift
- regression detection
- human oversight for high-risk flows

## Recommended practices
- use grounded retrieval and structured state
- define clear success criteria for each flow stage
- score outputs with evals and feedback loops
- maintain a registry of flows, prompts, tools, and outcomes
- keep a documented decision trail for major changes

## Subareas
- llm/ — patterns for model variety, critique loops, evidence-first reasoning, and drift handling
- rag/ — retrieval architecture, ranking, hybrid search, freshness handling, and top-k strategies

## Pattern library
- llm/patterns/llm-as-a-judge.md
- llm/patterns/debate_agents.md
- llm/patterns/temperature_and_model_variation.md
- llm/patterns/evidence_and_drift.md
- rag/patterns/hybrid_search.md
- rag/patterns/rag_graph.md
- rag/patterns/ranking_and_topk.md
- rag/patterns/freshness_and_evidence.md
