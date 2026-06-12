---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, tree-testing, information-architecture]
sources: []
confidence: 0.6
method_family: evaluative
best_for: validating findability of a proposed IA without visual design noise
avoid_when: no candidate structure exists yet (use card sorting first)
outputs: task success per item, directness, first-click paths, problem branches
---

# Method: Tree Testing

## Purpose

Test whether people can find things in a proposed hierarchy presented as bare text — isolating IA quality from visual design, search, and page layout.

## Use When

- A candidate IA exists (often from [[methods/card-sorting|Card Sorting]]) and needs validation before build.
- Comparing two structures or measuring a redesign against the current tree.
- Findability complaints need diagnosis at the structure level.

## Avoid When

- Findability depends mainly on search or visual cues the tree test strips away.
- The structure is trivially shallow.

## Inputs

- The tree: full hierarchy as labels only.
- 8–12 findability tasks phrased without using the tree's own label words.
- Correct-destination definitions agreed before fielding.
- 30+ participants per tree for stable rates.

## Procedure

1. Write tasks from user goals; scrub label leakage from task wording.
2. Randomize task order; cap session length to avoid fatigue effects.
3. Measure success, directness (no backtracking), time, and first clicks.
4. Diagnose failures by path: wrong first branch vs. lost in depth vs. plausible-but-wrong destination.
5. Iterate the tree and retest the failing branches.

## Outputs

- Per-task success and directness rates.
- First-click distribution and failure-path diagnosis.
- Problem-branch list with proposed label or structure fixes.

## Quality Bar

- Task wording leakage checked in pilot.
- Success criteria fixed before data collection.
- Results compared against a baseline (current IA or alternative tree) where possible.

## LLM Assistance

- **Safe uses:** generating task wording variants, summarizing failure paths.
- **Risky uses:** predicting findability without participants.
- **Verification required:** diagnosis grounded in actual click paths.

## Related

- [[methods/card-sorting|Card Sorting]]
- [[methods/usability-testing|Usability Testing]]
