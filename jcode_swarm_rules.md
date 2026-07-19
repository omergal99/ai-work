# jcode Swarm Rules

## Executive Summary
jcode is treated as a local-first, high-efficiency coding swarm runtime. It is optimized for parallel sessions and low resource use.

## Runtime Assumptions
- Baseline single-session footprint: ~27MB RAM
- Additional session overhead: ~9.9MB per extra session
- Performance advantage: often 20x-100x faster than heavier runtimes in local coding loops
- Use lightweight execution when memory is constrained

## Swarm Architecture
- One orchestrator manages tasks and state
- Multiple specialists run in parallel on the same repository
- Each agent owns a narrow scope and only writes to allowed paths
- Shared state lives in .ai/brain_state.json and is read before every write

## Control Plane Principles
- Maintain a central registry of active agents and tasks
- Use file locks and state manifest updates to prevent clobbering
- Keep conflict review lightweight and automatic
- Route status updates through a shared state source rather than chat history

## Conflict Handling
- If Agent A changes code under Agent B's path, the runtime should notify Agent B to inspect the diff
- Use git status and diffs before merging
- Keep a small reconciliation step for overlapping edits

## Headless Browser & Ambient Mode
- Use browser bridge tools for snapshot, interactables, and form filling
- Run headless checks without crashing local web servers
- Keep browser automation deterministic and isolated from the main coding loop

## Voice and Hands-Free Work
- Expose STT/TTS as tool endpoints for agents
- Support commands such as `jcode dictate` or audio-pipe workflows for planning and review
- Keep voice commands short and structured

## J Language Note
The J language is a terse array-oriented programming language with ASCII-based operators, but the environment here targets the jcode agent runtime, not general-purpose J development.

## Operational Rules
- Prefer local execution first
- Do not allow blind writes without reading state
- Keep the system deterministic, inspectable, and auditable
- Treat every run as an event in the organizational memory trail
