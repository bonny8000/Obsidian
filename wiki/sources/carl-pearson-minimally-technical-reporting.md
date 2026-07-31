---
type: source
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [ux-research, research-reporting, stakeholder-communication, quant-uxr, data-visualization, executive-communication, carl-pearson]
source_path: raw/web/carljpearson-minimally-technical-reporting-2026-07-31.md
source_url: https://carljpearson.com/minimally-technical-reporting/
authors: [Carl J. Pearson]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.7
---

# Pearson (2026): Minimally Technical Reporting — The Information Iceberg

## Citation

Carl J. Pearson, "Minimally Technical Reporting: The information iceberg," **carljpearson.com**, 2026-06-30. The term is credited to **Chapman and Rodden**: *"Good reports are short, focused on action, minimally technical, and unbiased."*

**Source type:** Practitioner essay by a PhD UX researcher (experience at Meta), built explicitly from personal successes and failures rather than from study.
**Raw capture:** [[raw/web/carljpearson-minimally-technical-reporting-2026-07-31|carljpearson-minimally-technical-reporting-2026-07-31]]
**Coverage note:** `coverage: substantial` — the iceberg model, all numeric rules, the production order, and the visualization guidance were captured in full. The source contains no data to have covered.

Second Pearson source, after [[wiki/sources/carl-pearson-quant-uxr-self-study-resources|the quant UXR self-study resource list]].

## Summary

An operational answer to a question this vault has repeatedly raised but not resolved: **how deep should a research readout go, and for whom.** Pearson's model is an iceberg with five levels — **workings → technical appendix → memo → briefing → headline** — where information density falls as audience seniority rises.

Its value is that it is *specific* where this genre is usually vague. It gives numbers (10–20 slides; three sentences per slide; one number per slide for executives), a production order (appendix first, memo written fresh rather than edited down, deck built from the memo), and testable prohibitions:

> "If you show a table to executives, you've gone too deep. If you show a dodged or stacked bar chart to executives, you've gone too far."

The framing claim that does the most work:

> "Most people don't care about how you got your answer. Some don't care about your answer, they just want to know what they should do next."

## Key Claims

- **Reporting depth is an audience variable, and career progression changes the audience.** Junior researchers report to peers who want the detail; senior researchers report to executives who cannot absorb it. The skill is knowing which level of the iceberg to surface, and it has to be relearned as the stakeholder mix shifts.

- **Write the appendix first, then write the memo from scratch.** Explicitly *not* by editing the appendix down. The appendix is exploratory and exhaustive; the memo is a new document with a different job, linked back to the appendix for depth. The deck is then built from the completed memo — never the reverse.

- **Format follows the reading mode, and mixing them fails twice.** Decks are for presenting, documents are for reading. A deep-dive memo formatted as a deck is *"trying to do two jobs at once while failing at both."*

- **The analysis chart and the communication chart are different charts.** *"The chart that helps you understand the data isn't necessarily the chart that will help your stakeholder understand what you learned."* Good communicative visuals named: a single-point bar chart with one bar highlighted; an annotated line chart describing the movement. Bad for executives: tables, dodged/stacked bars, driver-analysis charts with regression-coefficient axes.

- **Translate statistics into relative risk in plain language.** *"Users that do X are 3x more likely to be satisfied than users who do Y"* rather than coefficients or p-values. The technical machinery — generalized linear mixed effects models, non-response bias weights, sandwich estimators, top-2-box percentages — belongs in the appendix, not in the message.

- **Every visible number must come with a plain-language explanation prepared in advance.** Executives will question any detail that is on the slide, so the expectation of being questioned becomes the filter for what goes on the slide at all. *"You're not ready to talk to executives about your work until you can do it with one number per slide maximum."*

- **Run separate readouts per team** rather than combining insights for different audiences into one presentation.

## Useful Examples

**The iceberg, with its density rule:**

| Level | Audience | Density |
|---|---|---|
| Workings | you | everything; not shared |
| Technical appendix | research peers | exhaustive; written first |
| Memo | partner teams | written fresh, deep-linked to appendix |
| Briefing | leadership | 10–20 slides, ≤ 3 sentences/slide |
| Headline | executives | one number per slide maximum, or none |

**The two-line depth test** ("table → too deep, stacked bar → too far") is the most immediately usable thing in the piece: it converts a judgment call into an artifact check that anyone can apply to a deck before sending it.

## Constraints / Caveats

- **Experience-based, not researched.** No study, no data, no citation beyond the Chapman & Rodden phrase. The author is candid that the model came from a personal failure — *"I stumbled and ultimately failed to give a decent answer"* — which means it is a post-hoc rationalization of experience rather than a tested framework.
- **The author disclaims the structure himself:** *"These levels are not strict, I can see arguments for fewer or more."* Treat five as a convenience, not a finding.
- **Organization-dependent by the author's own admission** — *"The way you implement the details of your UX research communication will be very organization dependent."*
- **Assumes a hierarchical org with executive leadership.** Flat organisations, agencies, and client work are not addressed.
- **Does not address stakeholders who demand a format** regardless of fit, which is the most common real obstacle to applying any of this.
- **Weighted to quantitative research.** Qualitative is mentioned (affinity mapping, familiarization, mental model mapping — the last noted as not yet used by the author), but the numeric rules are built around quant readouts.
- The numeric rules (10–20, three, one) are stated without derivation; exceptions are acknowledged in passing.

## Design Implications

- **Adopt the production order as a workflow rule, not advice.** "Memo written fresh, not edited down" is a specific, checkable practice, and it is the recommendation most likely to change output quality — editing down preserves the appendix's structure, which is organised around method rather than around the decision.
- **Use the depth test as a pre-send gate.** Table present → wrong altitude for this audience. This is cheap enough to actually run.
- **Prepare the plain-language gloss for every number before the meeting**, and use the fact that you cannot write one as evidence the number should be cut.
- **Split readouts by audience** rather than building one deck that serves none of them.

## Tensions

- **Against the vault's rigor-first material.** The pages this vault holds on [[wiki/concepts/ux-research/quant-uxr-rigor|quant UXR rigor]] and [[wiki/concepts/ux-research/decision-contract|decision contracts]] push toward stating methodological limits explicitly. Pearson pushes methodology out of the message entirely. These are compatible only if the appendix is genuinely maintained and genuinely read — and Pearson's own claim that executives don't care about method suggests it usually is not. **The honest reading is that this is a trade, not a free optimisation: legibility is bought with reviewability.**
- **Against [[wiki/sources/nngroup-accelerating-research-with-ai|NN/g on interpretation locality]].** If interpretation cannot be separated from the person who observed the research, then compressing five levels down to a headline moves the decision further from the interpretation each time. Pearson's model manages that risk with deep links back to the appendix; whether anyone follows them is untested here.
- **Sits oddly beside AI-accelerated reporting.** Every level of this iceberg is a plausible generation target, and the level most easily generated — the polished headline — is the one furthest from the evidence. This source predates that concern and does not address it, but the iceberg is a useful map of exactly where generated summarisation is most dangerous.

## Open Questions

- Does the "write the memo fresh" rule actually produce better memos than editing down, or is it a discipline that works because it forces re-reading? Testable, and nobody appears to have tested it.
- Do deep links from memo to appendix get followed? If not, the appendix is a compliance artifact and the model's safety valve is decorative.
- Do the numeric rules transfer outside large hierarchical tech companies?
- What is the equivalent depth test for qualitative readouts? The table/stacked-bar test is quant-specific.

## Concepts Linked from This Source

- [[wiki/concepts/ux-research/minimally-technical-reporting|Minimally Technical Reporting]] *(new)*
- [[wiki/concepts/ux-research/decision-contract|Decision Contract]]
- [[wiki/concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[wiki/concepts/ux-research/interpretation-locality|Interpretation Locality]]
- [[wiki/concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]

## LLM Use Guidance

- **Strong, directly usable guidance** for structuring a research readout, and one of the few sources in this vault that gives checkable numbers for it.
- Use the depth test and the production order as **operational rules**; use the five-level count as a **convenience**, since the author disclaims it.
- **Do not cite as evidence about what executives actually absorb.** No measurement is offered; this is one practitioner's model of his audience.
- When advising on AI-assisted reporting, use this as the **map of altitudes** and flag that generation quality is inversely related to distance from the raw evidence.

## Reliability Notes

- **Confidence 0.70.** High for the practical guidance, which is specific, internally coherent, and matches how research communication is widely taught; capped because it is entirely experience-based, explicitly organisation-dependent, self-disclaimed on its central structure, and offers no evidence that following it changes stakeholder decisions.
- Second Pearson source; the first was a resource list rather than an argument, so this is the first opportunity to assess his reasoning directly. It holds up — the caveats are volunteered rather than extracted, which is a credibility signal.
- **Highest-value follow-up:** the Chapman & Rodden original, which is cited for the framing phrase and is the only external anchor in the piece. Ingesting it would give this cluster a primary source.
