DOC_ID: AI_CONFIG_01
Keywords: agent-config, orchestration, evals, skills, prompts

OVERVIEW
This folder is the local AI operating system for the workspace.

PURPOSE
Make agent work predictable, scalable, evaluable, and maintainable.

PRIMARY LAYERS
- core state: .ai/brain_state.json
- memory and retrieval: .ai/context_lake_blueprint.md
- local swarm execution: .ai/jcode_swarm_rules.md
- adoption roadmap: .ai/adoption_playbook.md
- GenAI Flow product layer: .ai/genai-flow/
- repository intelligence: .ai/repository-intelligence/
- evals and drift detection: .ai/evals/
- multi-agent control plane: .ai/control-plane/
- operational discipline: .ai/ops/
- knowledge packs: .ai/knowledge/
- reusable templates: .ai/templates/

STRUCTURE
- personas: role definitions
- protocols: contracts and rules
- orchestration: execution model and state handoffs
- prompts: reusable prompts
- skills: reusable instructions
- mcp: tool exposure and server config
- ops: history, standards, and maintenance
- knowledge: curated design and roadmap content

OPERATING RULES
- Read the shared state before using tools.
- Keep state explicit, not implicit in chat history.
- Prefer retrieval and structured context over large prompt dumping.
- Update the index when structure or purpose changes.
- Preserve session history in .ai/ops/history.

USE
1. Start with .ai/README.md
2. Read .ai/INDEX.md
3. Load the relevant persona, prompt, and skill
4. Use the shared state manifest
5. Run evals before shipping
