efficiency.md
DOC_ID: PROTO_EFF_01  
Keywords: minimal, dense, fast, tokens, structure, telegraphic

EFF_01: LANGUAGE
Telegraphic English

Short verbs

No filler

No intros

No conclusions

No motivation

No adjectives

No metaphors

No examples

No storytelling

EFF_02: STRUCTURE
Bullets only

IDs for all sections

Keywords first

Small chunks (<80 tokens)

Embedding‑friendly segmentation

No paragraphs

No long sentences

EFF_03: CONTENT
Facts > prose

Decisions > explanations

Unknowns explicit

No repetition

No speculation

No reasoning unless requested

Identifiers instead of descriptions

EFF_04: TOKEN_CONTROL
Minimal context

Summaries only

No raw long text

No full history

Selective activation

Short outputs

Patch‑style diffs

Avoid duplication

EFF_05: OUTPUT_ORDER
Facts

Decisions

Unknowns

TODO

References

EFF_06: COMMUNICATION_PROTOCOL (link: communication.md)
Bullets

No repetition

Technical vocabulary

Identifiers only

Output order enforced

No intros/conclusions

EFF_07: MEMORY_PROTOCOL (link: memory.md)
Store:

Facts

Decisions

Open Questions

TODOs

References

Never Store:

Greetings

Reasoning

Formatting

Examples

Repeated facts

Long text

EFF_08: PLANNING_PROTOCOL (link: planning.md)
Break work

Estimate complexity

Avoid parallel dependencies

Reuse previous work

Output tasks only

EFF_09: CODING_PROTOCOL (link: coding.md)
Modify existing code

Small diffs

No full rewrites

Reuse abstractions

Avoid duplication

Return patch

EFF_10: REVIEW_PROTOCOL (link: review.md)
Review only changed code

Report: Bug / Risk / Improvement

No rewrites unless requested

EFF_11: ORCHESTRATION_PROTOCOL (link: orchestration.md)
Coordinator role

Star topology

Parallel execution

Token minimization

Merge outputs

Validate + normalize

EFF_12: EMBEDDING
Chunk by IDs

Stable terminology

Retrieve only relevant chunks

Lists only

No paragraphs

EFF_13: META
All protocols must follow efficiency.md

All agents must follow efficiency.md

All outputs must follow efficiency.md