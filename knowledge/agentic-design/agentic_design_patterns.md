# Agentic Design Patterns

## Executive Summary
Agentic systems are moving from prompt wrappers to structured execution loops. The core idea is to combine reasoning, tools, memory, and verification in a deterministic control structure.

## Core Patterns
1. React Agent
   - Alternates reasoning and action
   - Uses tools and state updates
   - Best for narrow, stepwise tasks

2. CodeAct Agent
   - Executes code as an action primitive
   - Allows stronger autonomy and tool use
   - Useful for data processing, scripting, and testing

3. Modern Tool Use
   - MCP exposes tools to agents in a structured way
   - Enables integration with local and remote systems
   - Prevents each agent from reinventing basic capabilities

4. Self-Reflection
   - The agent critiques its own output
   - Supports iterative improvement and error recovery
   - Should be bounded and auditable

5. Multi-Agent Workflow
   - Specialized agents collaborate through a coordinator
   - Good for decomposition, review, and synthesis

6. Agentic RAG
   - Retrieval is active and iterative
   - Uses memory, tools, graph connections, and reranking
   - Reduces token waste by raising retrieval precision

## Why It Matters
These patterns define the engineering vocabulary for building real agent systems instead of simple chat wrappers.

## Best Practices
- Separate planning, execution, and verification
- Keep state explicit and centralized
- Use structured outputs and tool contracts
- Add evals for each critical workflow
- Use graph or hybrid retrieval rather than long prompt dumping
