---
type: source
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [input-modality, wearables, sensors, ai-hardware, privacy, data-trust, investment-thesis]
source_path: raw/web/kakao-vc-ai-input-modality-wearables-2026-06-25.md
source_url: https://www.kakao.vc/blog/ai-modality
authors: [Kakao Ventures]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Kakao Ventures (2026): How AI Reads the World — The Input-Modality Competition on Wearables

**Author:** Kakao Ventures (editor: Chloe) — kakao.vc blog, 2026-06-24.
**Raw capture:** [[raw/web/kakao-vc-ai-input-modality-wearables-2026-06-25|kakao-vc-ai-input-modality-wearables-2026-06-25]]
**URL:** [kakao.vc/blog/ai-modality](https://www.kakao.vc/blog/ai-modality)

## Citation

Kakao Ventures. (2026, June 24). *How AI Reads the World — The Input Modality Competition on Wearables.* kakao.vc blog. Captured 2026-06-25 into `raw/web/kakao-vc-ai-input-modality-wearables-2026-06-25.md`.

## Summary

A VC investment thesis: as AI takes on more decision-making, advantage shifts from **model performance → contextual understanding**, and **wearables** become critical because they capture signals smartphones can't (gaze, motion, biometrics). The arc is **explicit, user-initiated input → continuous, embodied collection**. The frontier that decides winners is *how* the tech enters the body and daily life — not raw sensor accuracy.

## Key Claims

- **Input modality** = the format through which AI receives information: text, image, voice, and sensor signals (gaze, movement, neural activity).
- **Two cross-cutting taxonomies:**
  - **By signal channel:** Auditory (mature, limited state), Visual (rich context + attention; battery/thermal/3rd-party-privacy hard), Motion (intuitive; must separate intent from everyday movement), Physiological/Neural (HR, temp, EMG, EEG, BCI; captures undisclosed states; hard to interpret).
  - **By collection mechanism:** Explicit (user-initiated; high control, low continuity), Standby (trigger-watching; less friction, consent ambiguity), Continuous (passive; temporal understanding, but control/trust concerns).
- **Three barriers to viability:** **Technical performance** (stable interpretation), **Physical adoption** (wearability: design/weight/battery/aesthetics), **Data trust** (consent for personal *and third-party* data).
- **Positioning rule:** winners behave as **fashion accessories** (Ray-Ban Meta, Oura Ring) *and* guarantee privacy (on-device processing, transparency indicators, user control over storage/retention).
- **Thesis quote:** "The winner will not be the technology that collects the most data, but the one that enables users to naturally adopt it while safely utilizing their information."

## Useful Examples

- **Google Glass** — failed on privacy + design unfamiliarity despite technical feasibility (the "third-party privacy / social acceptability" barrier).
- **Meta Ray-Ban** — AI sensing inside an established fashion brand (physical-adoption win).
- **Oura Ring** — biometrics in a familiar accessory form.
- **Apple Vision Pro** — mature eye-tracking as a visual-channel reference.

## Constraints / Caveats

- VC thesis, not empirical research — directional, no market sizing or named portfolio companies captured.
- Korean-market lens (Kakao Ventures); examples are global but framing is investor-side.
- Overlaps conceptually with this vault's [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]] but at the **hardware/sensor** layer rather than the **interaction-design** layer.

## Design Implications

- Anchors a new [[concepts/robotics-spatial/input-modality|Input Modality]] concept (sensor channels × collection mechanisms × the 3 adoption barriers) — a planning lens for any wearable/ambient AI product.
- For AX/UX: **standby and continuous** collection create the hardest *consent and awareness* design problems — connect to trust/transparency work and [[concepts/robotics-spatial/egocentric-human-data|egocentric human data]].
- "Fashion accessory + privacy guarantee" is the adoption gate, not sensor specs — a product-strategy implication for [[concepts/robotics-spatial/ai-hardware-boom|AI hardware]].

## Tensions

- **More signal vs. more trust** — continuous physiological/visual capture maximizes context but maximizes privacy/consent risk; the thesis says trust, not data volume, wins.
- **Intent vs. ambient** — motion/standby modes must distinguish deliberate commands from incidental signals.

## Open Questions

- Which signal channel reaches reliable, low-power, socially-acceptable use first?
- What consent UX actually earns "data trust" for **third-party** bystander data (the Glass failure mode)?

## Concepts Linked

- [[concepts/robotics-spatial/input-modality|Input Modality]]
- [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]]
- [[concepts/robotics-spatial/ar-glasses|AR Glasses]]
- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]
- [[concepts/robotics-spatial/ai-hardware-boom|AI Hardware Boom]]
- [[concepts/robotics-spatial/spatial-ai|Spatial AI]]

## LLM Use

- **Use for:** mapping a wearable/ambient-AI product's input modalities (channel × mechanism), stress-testing it against the 3 adoption barriers, and the "fashion + privacy" positioning argument.
- **Do not use for:** market sizing or specific investment claims; treat as a framing lens.
- **Best prompt pattern:** "Classify this wearable's inputs by signal channel and collection mechanism, then evaluate it against technical performance / physical adoption / data trust, and propose a consent UX."

## Reliability Notes

> [!warning] Caveats
> VC thesis, no empirical backing. Confidence 0.8 on the taxonomy/framing as a planning lens; lower on any predictive market claim.

## Backfill Status

- New ingest 2026-06-25 from full web_fetch. To reach `full`, capture the verbatim original and any named companies/market data.
