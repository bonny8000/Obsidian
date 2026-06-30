---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [synthetic-users, digital-twin, pipeline, validation, ai-uxr, system-prompt, engineering]
sources:
  - sources/voiceofuser-inhouse-digital-twins-blueprint
confidence: 0.82
---

# In-House Synthetic User Pipeline

## Summary

A reusable, tool-agnostic engineering recipe for building an individual-level synthetic-user / [[concepts/ux-research/digital-twin-respondents|digital-twin]] panel from a team's own data — distinct from the *what-is-it* [[concepts/ux-research/synthetic-user-taxonomy|taxonomy]]. The Voice of User blueprint specifies a six-component architecture and six build steps where the model is never trained, only prompted, and where validation is treated as the deliverable rather than an afterthought.

## Why It Matters

Most "synthetic users" discourse is either marketing or taxonomy. This concept captures the actual build: it makes the pattern auditable and repeatable, and — crucially — it bakes honesty about limits into the pipeline itself (a coverage rubric and a three-level validation ladder), so the output can't quietly masquerade as evidence.

## Key Claims

- **Six steps, prompting-only:** grounding data (interviews/surveys/behavioral telemetry) -> segment labels *held back* from the model -> plain-English profile with cohort-relative positioning -> behavioral system prompt -> a `ThreadPoolExecutor` scenario runner over the Anthropic `claude-sonnet-4-6` API (~50–100 twins in ~2 min) -> results table -> validation harness ([[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User, 2026]]).
- **A twin "is one thing: a system prompt"** — no fine-tuning; validated research found prompting beats fine-tuning for this task.
- **Coverage rubric (Green/Yellow/Red)** gates which questions are answerable: only Green questions yield evidence; Red questions are the model's prior in costume.
- **Three-level validation ladder:** internal consistency; MAE vs real humans (<~10 pt good / >~25 pt unusable); published-metric habits with a baseline ladder (Columbia: random 0.63 / empty 0.73 / demographics 0.75 / full twins 0.75).
- **Documented bias catalog:** under-dispersion (154/164), stereotyping, representation bias, ideological tilt, hyper-rationality (99.9% vs 52% human) — and concrete countermeasures: hold derived labels out of the prompt, add cohort-relative positioning.
- **Five deliberate simplifications and governance** (consent, pseudonymization, months-not-years refresh) are labeled rather than hidden.

## Related Concepts

- [[concepts/ux-research/digital-twin-respondents|Digital-Twin Respondents]] — what this pipeline produces.
- [[concepts/ux-research/synthetic-user-taxonomy|Synthetic User Taxonomy]] — where the pipeline's output sits (Type 4–5).
- [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]] — the validation ladder is this concept's quality bar.
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]] — Level-2 MAE validation extends its empirical evidence.
- [[concepts/ux-research/llm-user-proxy|LLM User Proxy]] — the coverage rubric is a usable gate for proxy studies.
- [[concepts/ux-research/algorithmic-monoculture|Algorithmic Monoculture]] — under-dispersion is the homogenization failure mode the pipeline fights.

## Conflicts & Caveats

> [!warning] Secondary reporting of untraced studies
> The embedded figures (Columbia baseline ladder, the under-dispersion and hyper-rationality counts, "Stanford"/mega-study references) are the author's secondary reporting of unnamed primaries not yet traced. The pipeline is a strong practitioner artifact, but its quantitative claims should be verified before being cited as evidence.

## Sources

- [[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User: In-House Digital-Twins Blueprint (Constantine Papas, 2026)]] — six-component architecture, six build steps, coverage rubric, validation ladder, bias catalog.

## Open Questions

- Which steps generalize beyond the Anthropic API stack the blueprint uses?
- What is the minimum grounding-data volume per person before a twin clears Level-2 MAE?
- Can the coverage rubric be automated, or does it require human judgment per question?
