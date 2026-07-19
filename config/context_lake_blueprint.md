# Context Lake Blueprint

## Executive Summary
The Context Lake is the append-only memory layer for the repository. It stores raw logs, semantic chunks, graph facts, execution traces, and project state outside the LLM context window.

## Why It Matters
Agents should not repeatedly read full files or dump giant prompt blocks. They should query a compact, structured context layer only when a task needs it.

## Mental Model
Use a three-layer memory system:
1. Working memory: short-lived task context
2. Context Lake: structured repository memory
3. Organizational memory: shared state and policies in .ai

## Architecture
- Ingest local files into semantic chunks
- Store metadata: path, tokens, language, entity tags, last modified, ownership
- Keep a graph of facts and relationships
- Retrieve only when explicitly triggered by task, tool, or policy

## Local File Ingestion Rules
- Parse by semantic unit: module, function, doc section, test case, config block
- Normalize path references and create stable IDs
- Store chunk hash and source path
- Track dependencies between files and modules
- Avoid storing duplicate content with different wrappers

## Retrieval Rules
- Retrieval is trigger-based, not automatic
- Each agent must check config/brain_state.json before tool use
- If a task needs context, retrieve the smallest relevant slice
- Favor dense, structured retrieval over long prompt dumps

## Modelmaxxing Guidelines
Tokenmaxxing is over. Modelmaxxing means using smaller, denser reasoning prompts combined with retrieval and structure.
- Give the model a crisp task, a small evidence set, and explicit constraints
- Use retrieval to provide facts rather than raw text blocks
- Prefer schema-first prompts and graph traversal over narrative context
- Keep prompts short, targeted, and tool-aware

## Control Plane Integration
- The Context Lake should be readable by a future central agent control layer
- It should expose retrieval summaries, entity references, and recent state updates
- This supports a Herdr-style registry without forcing all agents to share raw context

## Best Practices
- Store facts, not chat history, as the primary source
- Use idempotency keys for indexing and update operations
- Keep retrieval triggers explicit: search, inspect, compare, verify
- Separate reasoning from memory access

## Implementation Example
- Agent asks: "inspect the flow explorer architecture"
- System reads related graph nodes, relevant docs, and recent changelog entries
- System returns a compact evidence packet with file paths and notes
- Agent reasons over that packet instead of reading the whole repo

## Repository Integration
- Main state store: config/brain_state.json
- Indexing source: local repository files and docs
- Access path: .ai/mcp/setup.json and .ai/mcp/available_mcp_registry.md
