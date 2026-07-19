DOC_ID: PROTO_CACHE_01  
Keywords: cache, llm, embedding, retrieval, tools, session, speed, tokens

CACHE_01: GOAL
Minimize repeated computation.
Reduce tokens.
Increase speed.
Reuse results across agents.

CACHE_02: STRUCTURE
Cache Manager contains:

LLM Cache

Embedding Cache

Tool Cache

Retrieval Cache

Session Memory

Each cache is isolated.
Coordinator + Agents may access via protocol only.

CACHE_03: LLM_CACHE
Purpose: Store previous LLM outputs.

Store:

Final answers

Summaries

Parsed structures

Validated results

Never Store:

Raw long text

Reasoning traces

Partial drafts

Unverified outputs

Lookup:  
Key = (Task_ID, Input_Fingerprint).
Return cached result if identical.

CACHE_04: EMBEDDING_CACHE
Purpose: Avoid recomputing embeddings.

Store:

Embeddings for text chunks

Embeddings for protocol sections

Embeddings for agent roles

Lookup:  
Key = Hash(text).
Return vector if exists.

Rules:  
Stable chunking.
Stable IDs.
No re-embedding unless text changed.

CACHE_05: TOOL_CACHE
Purpose: Cache tool results.

Store:

API responses

Parsed tool outputs

Validated tool data

Never Store:

Errors

Partial responses

Unstable data

Lookup:  
Key = (Tool_Name, Params_Fingerprint).

CACHE_06: RETRIEVAL_CACHE
Purpose: Cache retrieval results.

Store:

Top‑K results

Ranked lists

Metadata

Chunk IDs

Lookup:  
Key = Query_Fingerprint.

Rules:  
Reuse retrieval before re-querying.
Invalidate only when corpus changes.

CACHE_07: SESSION_MEMORY
Purpose: Short‑term working memory.

Store:

Facts

Decisions

TODOs

References

Never Store:

Greetings

Reasoning

Formatting

Examples

Repeated facts

Rules:  
Session-only.
Cleared after session ends.

CACHE_08: TOKEN_OPTIMIZATION (link: efficiency.md)
Cache summaries

Cache diffs

Cache validated outputs

Cache embeddings

Cache retrieval results

Avoid recomputation

Avoid re-embedding

Avoid re-querying tools

CACHE_09: ORCHESTRATION_INTEGRATION (link: orchestration.md)
Coordinator uses caches to:

Skip repeated LLM calls

Skip repeated embeddings

Skip repeated retrieval

Skip repeated tool calls

Reduce agent activation

Reduce context size

CACHE_10: AGENT_ACCESS
Agents may request cached data via Coordinator only.

Agents cannot write directly.
Coordinator validates before storing.

CACHE_11: INVALIDATION
Invalidate when:

Input changes

Protocol changes

Tools change

Corpus changes

Session ends

CACHE_12: META
All protocols must use cache.md.
All agents must use cache.md.
Cache Manager is global.
Coordinator enforces usage.