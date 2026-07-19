DOC_ID: PROTO_EVAL_01
Keywords: evals, regression, capability, grader, trace

EVAL_01: PURPOSE
Measure agent quality before deployment.

EVAL_02: TASK
Each task has:
- id
- prompt
- inputs
- expected_outcome
- success_criteria

EVAL_03: GRADERS
Use deterministic checks first.
Use rubric checks for subjective quality.
Use human review for calibration.

EVAL_04: SUITE
Keep two suites:
- capability: hard tasks
- regression: known good tasks

EVAL_05: HARNESS
Clean env.
Record transcript.
Isolate state.
Run multiple trials.

EVAL_06: METRICS
Pass/fail.
Latency.
Token usage.
Tool call quality.
Error rate.

EVAL_07: LOOP
Create task -> run eval -> inspect transcript -> improve -> repeat.
