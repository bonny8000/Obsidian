---
type: concept
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [input-modality, wearables, sensors, ai-hardware, privacy, data-trust, multimodal]
sources:
  - sources/kakao-vc-ai-input-modality
confidence: 0.78
---

# Input Modality

## Summary

The **format through which an AI system receives information** — text, image, voice, and (on wearables) sensor signals like gaze, motion, and biometrics. Kakao Ventures (2026) frames the wearable input-modality race as the next platform battle, where advantage shifts from model performance to *contextual understanding* captured at the body.

## Why It Matters

As AI takes on more decision-making, the constraint becomes the quality and continuity of input context — not just the model. Wearables capture signals smartphones can't, but each modality trades richer context against harder privacy, consent, and interpretation problems. This is the hardware/sensor layer beneath the interaction-design [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]].

## Key Claims

- **Two cross-cutting taxonomies:**
  - **By signal channel:** Auditory (mature, limited state) · Visual (rich context + attention; battery/thermal/3rd-party privacy) · Motion (intuitive; intent vs. incidental movement) · Physiological/Neural (HR, temp, EMG, EEG, BCI; undisclosed states, hard to interpret).
  - **By collection mechanism:** Explicit (user-initiated; high control, low continuity) · Standby (trigger-watching; less friction, consent ambiguity) · Continuous (passive; temporal understanding, control/trust concerns).
- **Three barriers to viability:** technical performance, physical adoption (wearability/aesthetics), and **data trust** (consent for personal *and third-party* data).
- **Adoption gate = "fashion accessory + privacy guarantee,"** not sensor specs (Ray-Ban Meta, Oura Ring succeed; Google Glass failed on privacy + social acceptability).
- Thesis: the winner is not who collects the most data, but who makes adoption natural and information use safe.

## Related Concepts

- [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]] — the interaction-design counterpart (input/interaction/output modalities).
- [[concepts/robotics-spatial/ar-glasses|AR Glasses]]
- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]
- [[concepts/robotics-spatial/ai-hardware-boom|AI Hardware Boom]]
- [[concepts/robotics-spatial/spatial-ai|Spatial AI]]

## Conflicts & Caveats

> [!warning] VC thesis, not research
> Directional framing with no empirical backing or market sizing. Useful as a planning lens, not a prediction.

## Sources

- [[sources/kakao-vc-ai-input-modality|Kakao Ventures: How AI Reads the World — Input Modality on Wearables (2026)]]

## Open Questions

- Which channel reaches reliable, low-power, socially-acceptable use first?
- What consent UX actually earns "data trust" for third-party bystander data?
