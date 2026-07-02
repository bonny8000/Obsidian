---
type: concept
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [ux-research, survey, conversational-ai, value-sensitive-design, inclusion, ethics]
sources:
  - sources/arxiv-2606.30660-value-sensitive-conversational-ai
confidence: 0.8
---

# Value-Sensitive Conversational Surveys

> [!abstract] Summary
> Design voice surveys around literacy, autonomy, local communication norms, and explicit consent while measuring participation separately from response validity.

## Why It Matters

Text-first survey interfaces systematically exclude some participants. Voice and conversational pacing can reduce burden, but human-like interaction also changes authority, disclosure, privacy, and trust. The modality is part of the research method.

## Key Claims

- Audio-first delivery can reduce reading and navigation barriers.
- Community co-design should shape dialect, voice, address, pacing, and clarification.
- Permission to skip and stop must remain visible throughout the interaction.
- Completion, comprehension, validity, truthfulness, and consent quality are separate outcomes.
- AI disclosure is part of informed consent, especially when the system uses human-like cues.
- Layered cues require factorial or randomized follow-up before causal attribution.

## Research Design Gate

| Question | Required evidence |
| --- | --- |
| Can participants access the modality? | device, phone, audio, privacy, language, disability checks |
| Do they understand the instrument? | comprehension pilot and teach-back |
| Do they feel free to decline? | explicit skip/stop controls and consent comprehension |
| Is completion meaningful? | response consistency, validity, satisficing, and missingness analysis |
| Does adaptation help? | randomized or factorial comparison of individual cues |
| Is the agent legible? | clear AI disclosure and context-appropriate explanation |

## Conflicts & Caveats

> [!warning] Ethical tension
> Human-like voices and backchannels may lower anxiety while increasing perceived social obligation. Do not optimize completion without measuring autonomy and understanding.

## Related Concepts

- [[concepts/ux-research/ai-moderated-interviews|AI-Moderated Interviews]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/survey-data-quality-screening|Survey Data Quality Screening]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]

## Sources

- [[sources/arxiv-2606.30660-value-sensitive-conversational-ai|Maurya (2026): Value-Sensitive Conversational AI for Low-Literacy Surveys]]

## Open Questions

- How should AI disclosure be explained where prior exposure to AI is low?
- Which completion gains survive participant-level randomization?
- How can voice surveys protect privacy when devices and rooms are shared?
