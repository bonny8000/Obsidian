---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [ux-research, screening, data-cleaning, survey-quality, panel-fraud, ai-fraud, methodological-integrity]
sources:
  - sources/measuringu-tac10-screening
confidence: 0.88
---

# Survey Data Quality Screening

> [!abstract] Summary
> The stacked set of signals UX researchers use to identify problematic respondents in survey data — speeders, attention checks, straightlining, open-ended review, internal consistency checks, duplicate / bot detection, session-recording review, and instrument-specific pattern checks like [[concepts/ux-research/tac-10-tech-savviness|TAC-10]] Guttman patterns. Approximately **10% of paid-panel respondents engage in cheating** (range 3–20%), so screening is not optional; it is operational hygiene.

> [!important] Why it Matters
> A survey dataset that hasn't been screened is not data — it's noise dressed as data. With AI now able to convincingly mimic both low- and high-skill respondents, single-signal screens are not enough. The defense is **layered**: multiple signals, each of which an adversary would have to defeat separately, plus a baseline assumption that "verified human" status comes from customer lists or panel-level checks rather than from any one in-survey question.

## 📝 Key Claims

- **~10% of paid-panel respondents engage in cheating** (range 3–20%). The base rate is high enough that screening must be a default step, not a special case.
- **Standard screening / cleaning checklist:**
  1. **Speeders** — flag respondents in the bottom decile of completion time.
  2. **Disqualifying questions** — filter respondents who do not match the target population.
  3. **Attention checks** — explicit "select strongly disagree" items.
  4. **Open-ended response review** — does the prose actually answer the question?
  5. **Internal consistency checks** — cross-item logic (e.g. age vs job tenure).
  6. **Straightlining detection** — same answer for every Likert item.
  7. **Session recording review** — for high-stakes studies, observe actual behavior.
  8. **Duplicate and bot detection** — IP, fingerprint, behavioral fingerprinting.
  9. **Instrument-specific pattern checks** — e.g. [[concepts/ux-research/tac-10-tech-savviness|TAC-10]] Guttman plausibility (87% plausible / <0.5% implausible in the reference dataset).
- **AI complicates these methods.** Sophisticated LLMs can mimic plausible respondents. Panel operators have implemented safeguards, but they are not foolproof.
- **The most reliable defense is "verified human" status** from the population frame itself — customer lists, recruited cohorts, panel-level fraud screening already applied — rather than any single in-survey signal.
- **Layering matters.** Each signal has false positives and false negatives; in combination they cover more of the fraud surface than any one in isolation.

## How to apply

- **Make screening a pipeline stage, not a post-hoc cleanup.** Every survey ingest should produce a "screened / flagged / removed" log.
- **Stack at least 3–4 signals.** For paid-panel work, fewer than three is undercooked.
- **Encode automatic discards.** Inverse-Guttman patterns, straightlining across every Likert block, completion time < 30% of median — these can be deterministic rules.
- **Reserve human review for the ambiguous middle.** Flagged-but-not-obvious responses go to a manual queue; clean and clearly-fraudulent both auto-route.
- **Document the screening pipeline in the report.** Stakeholders should know that *n = 324 survey responses → 287 retained after screening* is what they're looking at.
- **For AI-fraud-resistant survey design**, prefer signals that require *behavior* (timing variance, response trajectory, session-recording behavior) over signals that depend only on *content* (an LLM can produce plausible content).

## 🔗 Related Concepts

- [[concepts/ux-research/tac-10-tech-savviness|TAC-10 Tech Savviness]] — specific pattern-check instrument.
- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]] — the in-house version of "what panel fraud could look like at scale."
- [[concepts/ai-agents/agent-skills|Agent Skills]] — a screening pipeline is a strong Skill candidate.

## ⚖️ Conflicts & Caveats

> [!warning] Screening rigor vs participant friction
> Stacked screens lower fraud but annoy legitimate participants. The trade is real; the article doesn't quantify it.

> [!warning] No single signal is sufficient
> Treat the eight-item checklist as a *menu*. Use most of it, not all of it. Choose based on study stakes, population, and tooling.

## 📚 Sources

- [[sources/measuringu-tac10-screening|MeasuringU: Using the TAC-10 for Screening and Data Cleaning]] (Lewis & Sauro, 2026) — primary source for the checklist and AI-fraud framing.

## ❓ Open Questions

- What is the right screening stack for Bonny's bilingual (zh-TW / en) survey work — same eight signals, or locale-specific tuning?
- Can an agent-driven Skill auto-apply the checklist (compute speeder threshold, parse open-ended for plausibility, run pattern checks, score straightlining), with human review only for the ambiguous middle?
- For verified-human customer-list populations, which screening signals add the least vs most value — i.e. where is the screening budget best spent?
