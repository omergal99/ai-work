# Context Engineering

## Purpose
This layer defines how agents receive the smallest useful context for each task.

## Core Principles
- curate, do not dump
- use a context stack with clear components
- retrieve facts on demand
- compress long history
- isolate subagents

## Context Stack
1. Instructions
2. User Input
3. Retrieved Facts
4. Tools
5. Short-Term Notes
6. Long-Term Memory
7. Output Format

## Best Practices
- avoid stale history
- avoid irrelevant details
- avoid contradictory sources
- keep prompts dense and task-specific
- use structured retrieval and state manifests
