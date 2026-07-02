---
source_url: https://arxiv.org/abs/2606.30660
pdf_url: https://arxiv.org/pdf/2606.30660
captured: 2026-07-02
title: Improving Survey Participation in Low-Literacy Populations Through Value-Sensitive Conversational AI
authors: [Raj Gaurav Maurya]
published: 2026-06-16
publisher: arXiv
venue_note: Accepted at IJCAI-ECAI 2026 AI and Social Good Track
raw_pdf: raw/files/arxiv-2606.30660-value-sensitive-conversational-ai.pdf
capture_method: Original PDF preserved; seven pages extracted with pdfplumber and page 1 rendered with Poppler
---

# Value-sensitive conversational AI for low-literacy surveys

## Capture status

- Original seven-page PDF preserved at `raw/files/arxiv-2606.30660-value-sensitive-conversational-ai.pdf`.
- Full text extracted page by page on 2026-07-02.
- Page 1 was rendered and visually inspected to verify title, author, abstract, and layout.
- This card is an AI-authored evidence summary; consult the PDF for exact wording and tables.

## Study design

- **Population:** 315 adult married women without undergraduate degrees in four rural Hindi-speaking districts of Uttar Pradesh and Bihar, India.
- **Deployment:** 21 local volunteers, each assigned one modality and 15 participants; data collected in November-December 2025.
- **Design:** non-randomized, quasi-experimental assignment at the volunteer level.
- **Instrument:** ten questions moving from demographics toward sensitive questions about mobility, money, work, menstruation, contraception, and reproductive decision-making.
- **Primary outcome:** normalized survey completion, not response validity or truthfulness.

## Six modalities

1. Paper interview with a volunteer reading and recording responses.
2. Mobile web form with text and optional audio.
3. Voice over web with standard Hindi and visual response selection.
4. Voice over phone with a neutral text-to-speech agent.
5. Value-sensitive phone convAI with respectful salutations, explicit consent reminders, slower pacing, permission to skip, and gentle clarification.
6. Layered value-sensitive convAI adding gender-matched voices, local dialect, familiar forms of address, and backchannel cues.

ASHA community health workers informed the voice, dialect, salutations, and interaction cues. GPT-4o-mini validated spoken answers against predefined options; ElevenLabs supplied regional female Hindi voices.

## Results

| Modality | Mean completion |
| --- | ---: |
| Paper | 0.46 |
| Web | 0.51 |
| Voice over web | 0.68 |
| Voice over phone | 0.74 |
| Value-sensitive convAI | 0.83 |
| Layered value-sensitive convAI | 0.89 |

- Between-modality differences were significant: H(5) = 174.78, p < 0.001, eta-squared = 0.55.
- The main gains appeared between text and voice, then between standard voice and value-sensitive conversational design.
- ConvAI versus layered convAI was not a significant pairwise difference after correction (p = 0.47).
- Across all participants, retention fell from 100% at question 1 to 27.3% at question 10 as burden and sensitivity increased.
- No modality showed significant volunteer-to-volunteer variation after correction, but this does not eliminate confounding.

## Design mechanisms

- Audio-first interaction reduces literacy and navigation demand.
- Permission to skip and discontinue supports autonomy.
- Slower pacing, respectful address, and non-judgmental clarification can reduce interaction anxiety.
- Local dialect and community-informed voices can reduce social distance.
- Backchannel cues may signal listening, but the study did not isolate their causal effect.

## Critical limitations and ethics

1. Modalities were not randomized at participant level; volunteer, region, and participant composition may confound results.
2. Completion is not data quality. The paper did not test response validity, satisficing, acquiescence, or truthfulness.
3. The layered design combines multiple cues, so individual mechanisms cannot be causally attributed.
4. Formal institutional review board approval was not obtained.
5. The AI identity was not disclosed to ASHA workers or participants. The authors acknowledge this as a limitation for informed consent and autonomy.
6. The sample and sensitive-topic context limit generalization beyond rural low-literacy women in the studied districts.

## Reuse boundary

Use this study as field evidence that modality and interaction design correlate with survey completion. Do not use it to claim that conversational AI produces more valid data, eliminates social-desirability bias, or is ethically sufficient without transparent consent and randomized follow-up evidence.
