# RAG Strategy

This area is the operating playbook for grounding agent work with retrieval, ranking, and evidence-aware reasoning.

## Core principles
- Retrieve before answering whenever the task depends on repository, policy, or historical context.
- Use hybrid search when keyword and semantic signals both matter.
- Separate old and new evidence, and prefer fresh sources when freshness matters.
- Rank results carefully and use only the top relevant evidence for the current task.
- Keep retrieval quality visible through evaluation and review.

## Recommended operating pattern
1. Retrieve broadly enough to avoid missing key context.
2. Rank and filter aggressively so only the best evidence survives.
3. Keep the answer tied to the retrieved evidence rather than raw memory.
4. Surface the evidence used so reviewers can validate the output.
5. Track freshness and drift so stale context does not silently dominate.

## Strong patterns
- Hybrid retrieval: combine lexical and semantic retrieval.
- RAG graph patterns: connect evidence chunks, summaries, and context nodes into a graph-like structure for richer reasoning.
- Ranking and filtering: score candidates and discard weak matches early.
- Freshness handling: distinguish stable knowledge from volatile or recently changed information.
- Evidence assembly: present the retrieved evidence alongside the answer so reviewers can validate it.
- Top-k selection: use a controlled number of high-value results rather than overwhelming the agent with too much context.

## Pattern library
- patterns/hybrid_search.md
- patterns/rag_graph.md
- patterns/ranking_and_topk.md
- patterns/freshness_and_evidence.md

## Why this matters
A well-structured retrieval layer makes agent behavior more grounded, cheaper, and easier to trust than relying on memory alone.
