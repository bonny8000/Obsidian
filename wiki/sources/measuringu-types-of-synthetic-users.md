---
type: source
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [synthetic-users, ai-uxr, taxonomy, personas, digital-twin, research-grounding]
source_path: raw/web/measuringu-types-of-synthetic-users-2026-06-25.md
source_url: https://measuringu.com/what-are-the-different-types-of-synthetic-users/
authors: [Jim Lewis, Jeff Sauro]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# MeasuringU (2026): What Are the Different Types of Synthetic Users?

**Authors:** Jim Lewis, PhD & Jeff Sauro, PhD — MeasuringU, 2026-06-23.
**Raw capture:** [[raw/web/measuringu-types-of-synthetic-users-2026-06-25|measuringu-types-of-synthetic-users-2026-06-25]]
**URL:** [measuringu.com/what-are-the-different-types-of-synthetic-users](https://measuringu.com/what-are-the-different-types-of-synthetic-users/)

## Citation

Lewis, J., & Sauro, J. (2026, June 23). *What Are the Different Types of Synthetic Users?* MeasuringU. Captured 2026-06-25 into `raw/web/measuringu-types-of-synthetic-users-2026-06-25.md`.

## Summary

A preliminary **taxonomy** of "synthetic users" — AI-generated respondents that simulate human attitudes/behaviors. The authors treat synthetic users as an umbrella **genus** (not one species) and sort five types along a single axis: **how grounded each is in real human data**, from ungrounded role-play up to individual-level digital twins. The companion to their empirical [[sources/measuringu-synthetic-users-review|12-paper review]]: that piece asked *do they work?*; this one asks *what kinds are there?*

## Key Claims

- **Five types, weakest → strongest grounding:**
  1. **AI Proto Persona** — generated from a bare role-play prompt; preliminary, assumption-based, no research backing.
  2. **Demographic Based** — age/gender/occupation/region specs to approximate group tendencies.
  3. **Persona Based** — richer persona descriptions (traits, behaviors); more detail but still weak grounding.
  4. **Research Grounded** — references real research artifacts (interviews, surveys, analytics, support logs) with traceable sources, without modeling individuals.
  5. **Digital Twins** — models individual-level data to replicate specific persons; strongest grounding; real-world accuracy still an open question.
- **Grounding ≠ richness.** A vivid persona is not "grounded"; the distinguishing variable is traceability to real human data, not descriptive detail.
- **Generative agents are a different category** — agents that model behavior *over time* sit outside this static taxonomy.
- **Hybrids are real** — practice blends types; cites **Bisbee et al. (2024)** mixing demographic + persona-based methods.
- **The taxonomy is provisional** and expected to change as the field matures.

## Useful Examples

- The proto-persona prompt "You are a world-class Python programmer" as the canonical Type-1 (ungrounded) instance.
- **Bisbee et al. (2024)** as a hybrid (demographic + persona) data point.
- The genus/species (biological taxonomy) analogy for why "synthetic user" needs subtypes.

## Constraints / Caveats

- Practitioner blog post proposing a **provisional** scheme — a vocabulary, not validated measurement.
- Says nothing new about *accuracy*; for that, pair with the [[sources/measuringu-synthetic-users-review|empirical review]] (only ~21% of classic psych studies replicated; variance/subgroups/regressions fail).
- The "Digital Twins" type here means a **twin of a research participant** — distinct from the spatial/industrial [[concepts/robotics-spatial/digital-twin|digital twin]] concept in this vault.

## Design Implications

- Use the taxonomy to **state which type you're using and how grounded it is** before trusting any synthetic-user output — it makes the grounding claim explicit and auditable.
- Treat Types 1–3 (proto/demographic/persona) as ideation-only "vibe checks"; reserve Types 4–5 (research-grounded / digital twin) for anything closer to evidence, and still validate against humans.
- Maps onto [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]] (Type 4–5 territory) and the [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]].

## Tensions

- **Detail vs. grounding** — richer personas *feel* more valid but can be just as ungrounded (model-collapse toward the mean).
- **Useful-for-ideation vs. mistaken-for-evidence** — the same artifact can be a fine brainstorm prompt and a dangerous decision input.

## Open Questions

- Exact decision guidance: which type for which research goal? (deferred — capture from verbatim text)
- How do "Digital Twins" of real participants perform empirically, given the review's poor replication for the lower types?
- Where do "generative agents" fit once behavior-over-time is in scope?

## Concepts Linked

- [[concepts/ux-research/synthetic-user-taxonomy|Synthetic User Taxonomy]]
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]]
- [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]]
- [[concepts/ux-research/ai-persona-replication|AI Persona Replication]]

## LLM Use

- **Use for:** classifying/labeling a synthetic-user approach by grounding type; arguing for grounded over proto personas; structuring a "which type, how grounded" check before using synthetic respondents.
- **Do not use for:** accuracy claims (see the empirical review); treating any type as a replacement for human data.
- **Best prompt pattern:** "Given this synthetic-user setup, classify it into the 5-type MeasuringU taxonomy, state its grounding level, and list what it can/can't be used for."

## Reliability Notes

> [!warning] Caveats
> Practitioner taxonomy, explicitly provisional. Confidence 0.85 that the five types are a useful current vocabulary; lower on any specific type's empirical accuracy (defer to the review).

## Backfill Status

- New ingest 2026-06-25 from full web_fetch. To reach `full`, capture verbatim type definitions and any per-type decision guidance.
