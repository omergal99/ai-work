# Hybrid Search

## Purpose
Combine lexical and semantic retrieval so agents can find both exact terms and conceptually relevant material.

## Recommended use
- repository searches
- policy and documentation lookup
- long-form knowledge retrieval
- tasks where exact wording and meaning both matter

## Pattern
1. Run a keyword-based retrieval pass.
2. Run a semantic retrieval pass.
3. Merge and re-rank the results.
4. Keep the best candidates for final reasoning.

## Benefits
- improves recall
- improves precision when used carefully
- reduces missed context

## Guardrails
- do not overload the context window
- keep ranking explicit
- require the final answer to reference the retrieved evidence
