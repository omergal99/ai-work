# .ai Index

## Purpose
This index is the canonical entry point for the local AI operating system.

## Mandatory Rules
- Keep this file updated whenever .ai changes.
- Preserve the folder structure and avoid adding loose files at the root unless they are globally relevant.
- New documents must follow the conventions in .ai/README.md and the protocols under .ai/protocols/.
- Every major addition should include a short summary here.
- Any contributor editing .ai must update this index.

## Top-Level Structure
- .ai/README.md — overview and operating principles
- .ai/INDEX.md — this index
- .ai/brain_state.json — shared state manifest
- .ai/context_lake_blueprint.md — context lake and modelmaxxing rules
- .ai/jcode_swarm_rules.md — jcode swarm and local execution rules
- .ai/adoption_playbook.md — adoption maturity roadmap
- .ai/genai-flow/ — GenAI Flow product guidance and drift strategy
- .ai/knowledge/ — curated knowledge packs
- .ai/mcp/ — MCP config and registry
- .ai/ops/ — operational discipline and session history
- .ai/personas/ — role definitions
- .ai/prompts/ — reusable prompts
- .ai/protocols/ — operating contracts and Pydantic models
- .ai/repository-intelligence/ — repository intelligence blueprint
- .ai/skills/ — reusable skill instructions
- .ai/templates/ — templates for new artifacts
- .ai/evals/ — evaluation suite and cases
- .ai/control-plane/ — multi-agent control plane concept
- .ai/context/ — context engineering guidance
- .ai/agents/ — agent roles and handoff conventions
- .ai/observability/ — tracing, metrics, and drift signals
- .ai/deployment/ — deployment and runtime guidance
- .ai/tokens/ — token and cost notes
- .ai/z_temp_context/ — temporary session context

## Core Knowledge Packs
- .ai/knowledge/agentic-design/agentic_design_patterns.md
- .ai/knowledge/agentic-design/herdr_central_agent_control.md
- .ai/knowledge/ai-engineering-roadmap/ai_engineering_roadmap.md
- .ai/knowledge/token-economics/token_economics.md
- .ai/knowledge/adoption/adoption_framework.md

## GenAI Flow Layer
- .ai/genai-flow/README.md
- .ai/genai-flow/hallucination_and_drift_strategy.md

## Operational Files
- .ai/ops/README.md
- .ai/ops/history/README.md
- .ai/ops/standards/ai_documentation_standards.md

## Templates
- .ai/templates/agent_task_template.md
- .ai/templates/eval_case_template.json
- .ai/templates/state_manifest_template.json
- .ai/templates/decision_record_template.md

## Maintenance Rule
Any future change to .ai must update this index and preserve the repository-wide operating rules.
