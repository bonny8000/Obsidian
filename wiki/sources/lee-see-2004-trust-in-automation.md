---
type: source
status: active
created: 2026-06-12
tags: [source, paper, trust, automation, agent-experience]
sources: []
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# Lee & See (2004): Trust in Automation — Designing for Appropriate Reliance

> [!info] Metadata
> - **Author:** John D. Lee, Katrina A. See
> - **Date:** 2004, Human Factors 46(1), 50-80
> - **Type:** paper (peer-reviewed review, ~4,000+ citations)
> - **Raw File:** [[raw/web/lee-see-2004-trust-in-automation]]

## Citation

Lee, J. D., & See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. Human Factors, 46(1), 50-80. DOI 10.1518/hfes.46.1.50_30392. Captured 2026-06-12 from publisher abstract and secondary literature; full text paywalled, so coverage is partial.

## Summary

The foundational review of human-automation trust. Frames automation failure as a reliance problem: people misuse (over-rely on) or disuse (under-rely on) systems, and trust is the mechanism governing which. Integrates trust research across multiple disciplines into a conceptual model and argues the design target is appropriate reliance, not maximum trust.

## Key Claims

- Reliance failures split into misuse (trusting beyond capability) and disuse (rejecting capable automation); both destroy system value.
- Good trust has three properties: calibration (level matches capability), resolution (trust differentiates contexts where capability differs), and specificity (trust attaches to the right function, not the whole system).
- Users form trust from three information dimensions: purpose, process, and performance of the automation.
- Trust forms through analytic, analogical, and affective routes; emotional response is a first-class factor, not noise.
- Interface and display characteristics materially shape trust dynamics, making trust a designable property.

## Useful Examples

- The misuse/disuse taxonomy maps directly onto agent products: unreviewed agent output shipping into work (misuse) versus users redoing everything the agent did (disuse).
- Purpose/process/performance gives a checklist for trust surfaces: explain intent, expose reasoning, show track record.

## Constraints / Caveats

- Written for 2004-era automation (alarms, autopilots, decision aids); generative agents differ in output open-endedness and failure legibility. Transfer is plausible but each claim should be re-validated for LLM agents.
- This ingest is from abstract plus secondary sources, not full text; resolution/specificity details are summarized at framework level only.

## Design Implications

- Optimize for appropriate reliance: add friction or verification where over-trust is likely, reduce it where under-trust wastes agent value.
- Build trust surfaces per function, not globally — support resolution by letting users trust retrieval while verifying judgment.
- Show purpose, process, and performance at the moments reliance decisions happen.

## Tensions

- Tension with engagement metrics: maximizing trust boosts short-term usage but invites misuse; this source says calibrate instead.

## Open Questions

- Which of calibration, resolution, specificity degrades fastest with memory-bearing agents whose capability shifts over time?

## Concepts Linked

- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/error-recovery|Error Recovery]]
- [[concepts/agent-experience/agent-evaluation-ux|Agent Evaluation UX]]

## LLM Use

- **Use for:** grounding trust-calibration claims, framing reliance metrics, vocabulary for trust research design.
- **Do not use for:** quantitative effect sizes or verbatim model details (full text not ingested).
- **Best prompt pattern:** Ask the LLM to apply the misuse/disuse and purpose/process/performance frames to a specific agent feature before proposing trust surfaces.

## Reliability Notes

> [!warning] Caveats
> Peer-reviewed and foundational, but pre-LLM. Coverage partial (abstract-level ingest).

## Backfill Status

- Promote to coverage: full if the PDF is obtained and ingested into raw/.
