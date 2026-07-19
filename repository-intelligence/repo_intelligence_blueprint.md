# Repository Intelligence Blueprint

## Executive Summary
Repository intelligence is the structured map of a codebase that agents can query without reading everything.

## What It Should Contain
- architecture overview
- module boundaries
- dependency map
- ownership hints
- recent change summaries
- test and eval entry points
- risk hotspots

## Why It Matters
This reduces context waste and helps agents reason over the repository accurately.

## Recommended Sources
- docs/ folder
- README files
- package and requirements files
- tests
- architecture docs
- .ai state manifests

## Suggested Output Format
Each repository should expose a compact intelligence packet:
- repo_name
- purpose
- key modules
- current risks
- recommended next actions
- linked files

## Integration With Agents
Agents should read this packet before making changes. This shortens prompts and improves reliability.
