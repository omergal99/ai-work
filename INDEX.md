# AI Working Config Index

## Purpose
This index is the canonical entry point for the repository and should stay aligned with the current structure.

## Mandatory rules
- Keep this file updated whenever the repository structure changes.
- Keep the root clean and avoid adding loose files unless they are genuinely global.
- New documents should follow the conventions in the README and the protocols under protocols/.
- Every major addition should include a short summary here.
- Any contributor editing this repository should update this index when the structure or purpose changes.

## Top-level structure
- README.md — overview and purpose for human and agent readers
- INDEX.md — this index
- config/ — shared state, memory, execution rules, and adoption guidance
- core/ — consolidated operating layer for agents, protocols, prompts, skills, templates, ops, and related standards
- genai-flow/ — LLM, RAG, drift, and evaluation guidance
- knowledge/ — curated design, roadmap, efficiency, and adoption content
- docs/ — roadmap and next-step notes

## Core configuration files
- config/brain_state.json
- config/context_lake_blueprint.md
- config/jcode_swarm_rules.md
- config/adoption_playbook.md

## Core knowledge packs
- knowledge/agentic-design/agentic_design_patterns.md
- knowledge/agentic-design/herdr_central_agent_control.md
- knowledge/ai-engineering-roadmap/ai_engineering_roadmap.md
- knowledge/token-economics/token_economics.md
- knowledge/token-economics/token_optimization.md
- knowledge/adoption/adoption_framework.md

## GenAI Flow areas
- genai-flow/README.md
- genai-flow/hallucination_and_drift_strategy.md
- genai-flow/llm/README.md
- genai-flow/rag/README.md

## Operational files
- ops/README.md
- ops/history/README.md
- ops/standards/ai_documentation_standards.md

## Templates
- templates/agent_task_template.md
- templates/eval_case_template.json
- templates/state_manifest_template.json
- templates/decision_record_template.md

## Maintenance rule
Any future change to this repository should preserve the shared operating model and keep the structure easy to navigate for both humans and agents.
