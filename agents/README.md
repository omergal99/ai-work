# Agent Architecture

## Purpose
This folder defines how agent roles, workflows, and shared state should be structured.

## Core Model
- orchestrator: coordinates work
- specialist agents: perform narrow tasks
- reviewer agents: verify results
- shared state: central source of truth

## Best Practices
- assign one clear responsibility per agent
- keep orchestration explicit
- use state manifests and idempotency keys
- prefer structured handoffs over long conversation history
- add evals for each critical workflow
