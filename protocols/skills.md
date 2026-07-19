DOC_ID: PROTO_SKILL_01  
Keywords: skill, determinism, predictability, hierarchy, pruning, invocation

(טלגרפי, מינימלי, תואם efficiency.md)

SKILL_01: PURPOSE
Create predictable behaviour.
Deterministic process.
Consistent execution.

SKILL_02: INVOCATION
Two modes:

Model‑invoked:  
Has description.
Adds context load.
Use only when autonomous reach is required.

User‑invoked:  
No description.
Zero context load.
User must remember it.
Use router skill when many exist.

SKILL_03: DESCRIPTION (model‑invoked only)
Leading word first

One trigger per branch

No duplication

No identity repeated from body

Minimal tokens

SKILL_04: INFORMATION_HIERARCHY
Three layers:

Steps:  
Ordered actions.
Each ends with completion criterion.
Criterion must be checkable + exhaustive.

In‑skill reference:  
Rules, definitions, facts.
Flat peer set allowed.

External reference:  
Disclosed via context pointer.
Only when some branches need it.

SKILL_05: BRANCHING
Each distinct path = branch.
Inline shared material.
Disclose branch‑specific material.

SKILL_06: CO‑LOCATION
Keep definition + rules + caveats together.
No scattering.

SKILL_07: SPLITTING
Split only when:

Invocation requires independent reach

Steps ahead cause premature completion

SKILL_08: PRUNING
Single source of truth

Remove irrelevant lines

Remove no‑ops

Remove duplication

Prefer positive phrasing

Aggressive deletion

SKILL_09: LEADING_WORDS
Use pretrained compact concepts.
Anchor behaviour.
Reduce tokens.
Sharpen invocation.

SKILL_10: FAILURE_MODES
Premature completion → sharpen criterion → split if needed

Duplication → collapse

Sediment → prune

Sprawl → disclose

No‑op → replace with stronger leading word

Negation → rewrite positive

SKILL_11: META
All skills must follow skill.md.
All protocols may reference skill.md.
Coordinator enforces consistency.