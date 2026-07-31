---
type: concept
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [concept, ux-research, research-reporting, stakeholder-communication, executive-communication, data-visualization, quant-uxr, research-ops]
sources: [carl-pearson-minimally-technical-reporting]
confidence: 0.7
---

# Minimally Technical Reporting

> [!abstract] Summary
> Calibrating a research readout's depth to its audience, on the principle — credited to **Chapman and Rodden** — that *"Good reports are short, focused on action, minimally technical, and unbiased."* Structured as an **iceberg** with five levels, where information density falls as audience seniority rises, and the researcher's skill is knowing which level to surface.

> [!important] Why it Matters
> This is the operational answer to a question this vault has raised repeatedly without resolving: how deep should a readout go, and for whom. Most advice on it is vague; this is specific enough to check against an actual deck before sending it. The governing observation: *"Most people don't care about how you got your answer. Some don't care about your answer, they just want to know what they should do next."*

## 📝 Key Claims

**The iceberg:**

| Level | Audience | Density |
|---|---|---|
| Workings | you | everything; never shared |
| Technical appendix | research peers | exhaustive; **written first** |
| Memo | partner teams | written fresh, deep-linked back to appendix |
| Briefing | leadership | 10–20 slides, ≤ 3 sentences per slide |
| Headline | executives | one number per slide maximum, or none |

- **Write the appendix first, then write the memo from scratch — not by editing the appendix down.** This is the recommendation most likely to change output quality, because editing down preserves the appendix's structure, which is organised around *method* rather than around the *decision*. The deck is then built from the finished memo, never the reverse.

- **The depth test is a checkable artifact rule:** *"If you show a table to executives, you've gone too deep. If you show a dodged or stacked bar chart to executives, you've gone too far."* Cheap enough to actually run as a pre-send gate.

- **The analysis chart and the communication chart are different charts.** *"The chart that helps you understand the data isn't necessarily the chart that will help your stakeholder understand what you learned."* Communicative: single-bar charts with one bar highlighted; annotated line charts. Not communicative: tables, stacked bars, regression-coefficient axes.

- **Translate statistics to relative risk in plain language** — *"Users that do X are 3x more likely to be satisfied than users who do Y"* — and keep the machinery (mixed effects models, non-response weights, sandwich estimators, top-2-box) in the appendix.

- **Prepare a plain-language gloss for every visible number in advance.** Executives question any detail on the slide, so inability to write the gloss is evidence the number should be cut.

- **Format follows reading mode.** Decks present, documents are read; a deep-dive memo built as a deck is *"trying to do two jobs at once while failing at both."* Run separate readouts per team rather than one combined deck.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/decision-contract|Decision Contract]] — agrees the readout serves a decision; disagrees on how much method survives the trip.
- [[wiki/concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]] — the direct tension; see caveats.
- [[wiki/concepts/ux-research/interpretation-locality|Interpretation Locality]] — each level of compression moves the decision further from whoever did the interpreting.
- [[wiki/concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the same shape applied to interfaces.
- [[wiki/concepts/agent-experience/modality-intent-matching|Modality–Intent Matching]] — the same instinct in interface design: shape the artifact to the receiver's capacity, not the producer's convenience.
- [[wiki/methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]]

## ⚖️ Conflicts & Caveats

- **Legibility is bought with reviewability — this is a trade, not a free optimisation.** This vault's rigor material pushes toward stating methodological limits explicitly; this pushes method out of the message entirely. The two reconcile only if the appendix is genuinely maintained *and* genuinely read, and the source's own premise (executives don't care about method) suggests it usually is not.
- **Experience-based, not researched.** No study, no data, no citation beyond the Chapman & Rodden phrase, and the author is candid that the model originated in a personal failure.
- **The author disclaims the structure:** *"These levels are not strict, I can see arguments for fewer or more."* Five is a convenience.
- **Organisation-dependent by the author's own statement**; assumes a hierarchical org with executives. Flat orgs, agencies, and client work are unaddressed, as are stakeholders who demand a format regardless of fit.
- **Quant-weighted.** The depth test is quant-specific; there is no stated qualitative equivalent.
- **Uncomfortable next to AI-generated reporting.** Every level here is a plausible generation target, and the level most easily generated — the polished headline — is the one furthest from the evidence. The iceberg doubles as a map of where generated summarisation is most dangerous, though the source predates and does not address this.

## 📚 Sources

- [[wiki/sources/carl-pearson-minimally-technical-reporting|Pearson (2026): Minimally Technical Reporting]]

## ❓ Open Questions

- Does "write the memo fresh" beat editing down, or does it just force a re-read? Testable, untested.
- Do deep links from memo to appendix get followed? If not, the model's safety valve is decorative and the rigor trade-off is worse than it looks.
- Do the numeric rules (10–20, three, one) transfer outside large hierarchical tech companies?
- What is the depth test for a qualitative readout?
