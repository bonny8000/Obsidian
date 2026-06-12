---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, concept-testing, evaluative]
sources: []
confidence: 0.6
method_family: evaluative
best_for: early comprehension and appeal signal on a value proposition before building
avoid_when: the question is about usability of an existing flow, or stimuli are too unequal to compare
outputs: comprehension evidence, appeal and uniqueness ratings, objection inventory, concept ranking
---

# Method: Concept Testing

## Purpose

Test whether people understand a proposed value proposition, find it relevant, and would plausibly act on it — before engineering investment, using stimuli as cheap as a paragraph or a mock landing page.

## Use When

- Multiple directions compete for the same roadmap slot.
- The risk is "nobody wants this," not "nobody can use this."
- Positioning and message comprehension need evidence.

## Avoid When

- The concept's value only emerges through interaction over time (agents and recommender systems often fail flat concept tests yet succeed in use).
- Stimuli quality differs so much between concepts that the test measures polish, not appeal.
- Stated intent would be mistaken for behavior — treat results as directional.

## Inputs

- Concept stimuli at matched fidelity (statement, storyboard, or fake-door page).
- Comprehension questions written before fielding.
- A decision rule: what result kills, changes, or advances each concept.

## Procedure

1. Fix the decision and the kill/advance threshold first.
2. Build matched-fidelity stimuli; pilot for comprehension of the stimuli themselves.
3. Test comprehension before appeal ("explain this back to me"), then relevance, uniqueness, objections.
4. Rotate concept order; use monadic or sequential-monadic design when comparing.
5. Report comprehension failures as loudly as appeal scores — a loved-but-misunderstood concept is a mirage.

## Outputs

- Comprehension evidence per concept.
- Appeal, relevance, and uniqueness ratings with verbatim reasoning.
- Objection and confusion inventory.
- A recommendation against the pre-set decision rule.

## Quality Bar

- Stated intent never reported as demand prediction.
- Stimuli differences documented as a validity caveat.
- Sample matched to the decision's target segment.

## LLM Assistance

- **Safe uses:** drafting stimulus variants, clustering open-ended objections.
- **Risky uses:** simulating respondent reactions as evidence — see [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]].
- **Verification required:** clusters checked against verbatims.

## Related

- [[methods/maxdiff-prioritization|MaxDiff Prioritization]]
- [[methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]]
