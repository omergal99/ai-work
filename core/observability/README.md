# Observability

## Purpose
This layer makes agent behavior inspectable, debuggable, and measurable.

## What to Track
- task start/end
- tool calls
- state transitions
- latency and failures
- eval outcomes
- drift signals

## Recommended Signals
- structured logs
- event traces
- summaries per task
- human review queue
- policy violation warnings

## Design Goals
- make every agent action auditable
- make failures easy to replay
- make success measurable
- make state transitions visible
