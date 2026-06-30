---
type: concept
status: active
created: 2026-06-25
updated: 2026-06-29
tags: [synthetic-users, taxonomy, ai-uxr, personas, digital-twin, research-grounding]
sources:
  - sources/measuringu-types-of-synthetic-users
  - sources/brox-digital-twins-market-research
  - sources/voiceofuser-inhouse-digital-twins-blueprint
confidence: 0.8
---

# Synthetic User Taxonomy

## Summary

A preliminary five-type classification of "synthetic users" (AI-generated research respondents), ordered along a single axis: **how grounded each is in real human data**. From Lewis & Sauro (MeasuringU, 2026).

## Why It Matters

"Synthetic user" is an umbrella term covering very different things, from a one-line role-play prompt to an individual-level digital twin. Naming the type forces an explicit, auditable claim about grounding — which is exactly the variable that determines whether the output is safe to use as evidence or only as ideation.

## Key Claims

- **Five types, weakest → strongest grounding:**
  1. **AI Proto Persona** — bare role-play prompt; ungrounded, assumption-based.
  2. **Demographic Based** — age/gender/occupation/region specs approximating group tendencies.
  3. **Persona Based** — rich persona descriptions; more detail, still weak grounding.
  4. **Research Grounded** — references real research artifacts (interviews, surveys, analytics, logs) with traceable sources; no individual modeling.
  5. **Digital Twins** — models individual-level data to replicate specific persons; strongest grounding, accuracy still open.
- **Grounding ≠ richness** — a vivid persona is not "grounded"; the distinguishing variable is traceability to real human data.
- **Generative agents** (modeling behavior over time) are a *separate* category, outside this static taxonomy.
- **Hybrids occur** (e.g., Bisbee et al., 2024: demographic + persona). The scheme is explicitly **provisional**.
- Grounding type ≠ accuracy: even grounded types must be validated against humans (only ~21% of classic psych studies replicated with synthetic users — see [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]]).
- **Type 5 in the wild — productized and home-built.** Brox sells ~60,000 standing "[[concepts/ux-research/digital-twin-respondents|digital-twin respondents]]" of real people as the commercial Type-5 instance ([[sources/brox-digital-twins-market-research|Brox, 2026]]), while an in-house blueprint shows teams can build the same Type 4–5 panel themselves via prompting ([[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User, 2026]]). Critically, the blueprint's baseline ladder (random 0.63 / empty 0.73 / demographics 0.75 / full twins 0.75) suggests **Type 5 may not beat Type 2 on individual accuracy** — concrete evidence that grounding richness ≠ accuracy.

## Related Concepts

- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]] — the empirical "do they work?" evidence.
- [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]] — the Type 4–5 (grounded) end of the spectrum.
- [[concepts/ux-research/digital-twin-respondents|Digital-Twin Respondents]] — the Type-5 (individual-replica) instance, productized and home-built.
- [[concepts/ux-research/in-house-synthetic-user-pipeline|In-House Synthetic User Pipeline]] — how to build a Type 4–5 panel yourself.
- [[concepts/ux-research/ai-persona-replication|AI Persona Replication]]
- [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]]

## Conflicts & Caveats

> [!warning] Provisional
> The authors expect the scheme to change. It is a vocabulary for *grounding*, not a measure of *accuracy* — pair it with empirical evidence before trusting any type as decision input.

## Sources

- [[sources/measuringu-types-of-synthetic-users|MeasuringU: What Are the Different Types of Synthetic Users? (Lewis & Sauro, 2026)]]
- [[sources/brox-digital-twins-market-research|Brox: 60,000 "digital twins" of real people (VentureBeat, 2026)]] — the productized Type-5 instance.
- [[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User: In-House Digital-Twins Blueprint (2026)]] — Type 4–5 build + baseline-ladder evidence.

## Open Questions

- Decision guidance: which type fits which research goal?
- How do Type-5 digital twins of real participants perform empirically?
- Where do generative (over-time) agents slot in once behavior is modeled?
