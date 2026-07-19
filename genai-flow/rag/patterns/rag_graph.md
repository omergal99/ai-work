# RAG Graph Patterns

## Purpose
Represent knowledge as connected evidence units so the agent can traverse relationships instead of reading isolated chunks.

## Recommended use
- multi-hop reasoning
- architecture or dependency exploration
- large documentation sets
- workflows that require linking several evidence pieces together

## Pattern
1. Chunk the source material.
2. Create lightweight nodes for facts, summaries, and source links.
3. Connect related nodes with explicit relationships.
4. Retrieve and traverse the graph during reasoning.

## Benefits
- richer retrieval
- better context assembly
- less brittle reasoning

## Guardrails
- keep the graph simple and explainable
- avoid over-connecting weak or noisy content
- preserve traceability to the original source
