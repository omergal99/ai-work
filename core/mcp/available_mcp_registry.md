# Available MCP Registry

## Filesystem MCP
- Capability: read, write, inspect repository files
- Value: stable local context access for 100-agent workflows
- Prevents: redundant custom file readers

## Memory MCP
- Capability: persistent project state and memory graph access
- Value: shared memory without repeated prompt stuffing
- Prevents: duplicated state tracking logic

## Git MCP
- Capability: branch, diff, status, patch operations
- Value: deterministic change tracking and conflict handling
- Prevents: manual git wrappers in each agent

## Browser Bridge MCP
- Capability: snapshots, interactables, form fill, headless testing
- Value: local UI verification and browser-based automation
- Prevents: bespoke browser automation in each agent

## Shell MCP
- Capability: terminal execution and command orchestration
- Value: local task execution with guardrails
- Prevents: custom shell wrappers

## Search MCP
- Capability: semantic and keyword search over docs and code
- Value: precise retrieval for agentic RAG
- Prevents: each agent building its own search layer

## Observability MCP
- Capability: logs, traces, metrics, eval results
- Value: full audit trail for debugging and performance tuning
- Prevents: hidden failures and untracked regressions

## Activation Policy
Activate only the MCPs that solve a repeated need. Do not build custom tools when a shared MCP can satisfy the behavior.
