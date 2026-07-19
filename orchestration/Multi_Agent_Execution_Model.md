DOC_ID: ORCH_MULTI_01
Keywords: orchestrator, state, handoff, idempotency, async

ROLE
Master orchestrator owns plan and state.
Specialists execute narrow tasks.

STATE
Use state_manifest.json.
Fields:
- project_id
- task_id
- status
- artifacts
- handoff_trigger
- last_updated
- version
- idempotency_key

HANDOFF
Pass artifact refs.
Do not pass long chat.
When a condition is true, trigger the next agent.

IDEMPOTENCY
Each task has an idempotency_key.
Write status before and after.
Retries must not duplicate output.

EXECUTION
- Simple tasks: direct sync
- Long tasks: async queue or webhook
- Large loops: coordinator + specialist pattern

OUTPUT
Every agent returns:
{
  "task_id": "...",
  "status": "ok|failed|blocked",
  "artifacts": [],
  "notes": "...",
  "next_action": "..."
}
