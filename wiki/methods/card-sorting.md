---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, card-sorting, information-architecture]
sources: []
confidence: 0.6
method_family: generative
best_for: discovering how users group and label content, IA category hypotheses
avoid_when: a proposed IA needs validation against findability tasks (use tree testing)
outputs: similarity matrix, cluster analysis, user-generated labels, IA hypotheses
---

# Method: Card Sorting

## Purpose

Reveal users' mental categories by having them group content items and (in open sorts) name the groups — generating information-architecture hypotheses from user logic instead of org-chart logic.

## Use When

- Designing or restructuring navigation, menus, or content taxonomies.
- Internal teams disagree about category structure and need external evidence.
- Labels need to come from user vocabulary.

## Avoid When

- The question is whether a specific proposed structure works (use [[methods/tree-testing|Tree Testing]]).
- Items are too few (<15) or too abstract for meaningful grouping.
- The real challenge is cross-linking, not hierarchy.

## Inputs

- 30–60 cards written in user language, one concept each, no compound items.
- Sort type decision: open (generate categories) vs. closed (validate candidate categories).
- Remote tool or physical setup; 15–30 participants for stable patterns.

## Procedure

1. Pilot the card set: ambiguous or unknown cards corrupt every sort.
2. Run open sorts to generate structure, closed sorts to test candidate structures.
3. Ask participants to think aloud on hard-to-place cards; those are the design insight.
4. Analyze with similarity matrices and clustering; read agreement strength, not just clusters.
5. Translate to IA hypotheses, then validate with tree testing.

## Outputs

- Similarity matrix and dendrograms.
- Standardization of user-generated labels.
- "Homeless card" inventory — items with no stable category.
- Candidate IA structures.

## Quality Bar

- Low-agreement areas reported as genuinely ambiguous, not forced into clean categories.
- Card wording bias checked in the pilot.
- Card sorting output treated as hypothesis, not validated IA.

## LLM Assistance

- **Safe uses:** drafting card sets from content inventories, normalizing label variants.
- **Risky uses:** letting an LLM "sort like a user" and reporting it as user data.
- **Verification required:** clusters reflect participant matrices, not model priors.

## Related

- [[methods/tree-testing|Tree Testing]]
