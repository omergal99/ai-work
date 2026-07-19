# Agent Architecture

## Purpose
This folder defines the expected roles, responsibilities, and collaboration patterns for agents operating in this workspace.

## Core model
- orchestrator: coordinates the flow and keeps progress aligned
- specialist agents: handle focused work such as coding, analysis, or retrieval
- reviewer agents: validate correctness, quality, and policy compliance
- shared state: the common source of truth for progress, memory, and handoffs

## Best practices
- assign one clear responsibility per agent
- keep orchestration explicit and visible
- use structured state manifests and idempotency keys
- prefer short, structured handoffs over long chat-only context
- add evals for critical workflows and high-risk decisions

## How to work with this folder
Use this folder when you need to understand how an agent should behave in a multi-agent setup, not just how a single prompt should be written.
