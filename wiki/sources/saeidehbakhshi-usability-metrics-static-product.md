---
type: source
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [ux-metrics, usability-testing, adaptive-systems, personalization, steerability, measurement-validity, longitudinal-research, engagement, saeideh-bakhshi]
source_path: raw/web/saeidehbakhshi-usability-metrics-static-product-2026-08-04.md
source_url: https://saeidehbakhshi.substack.com/p/we-are-no-longer-testing-the-same
authors: [Saeideh Bakhshi]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.72
---

# Bakhshi (2026): Usability Metrics Assume the Product Stays Still

## Citation

Saeideh Bakhshi, "Usability Metrics Assume the Product Stays Still" (subtitle: "Why adaptive systems make usability measures harder to interpret"), **Research Toolbox**, 2026-08-02.

**Source type:** Methodological critique essay by a practising quantitative UX researcher. Conceptual argument; no data.
**Raw capture:** [[raw/web/saeidehbakhshi-usability-metrics-static-product-2026-08-04|saeidehbakhshi-usability-metrics-static-product-2026-08-04]]
**Coverage note:** `coverage: full` — all six sections captured with their headings, the four-dimension framework, and every worked example.
**Note on the URL:** the slug is `we-are-no-longer-testing-the-same`, taken from the first section heading rather than the title. Cite by title.

## Summary

The cleanest statement this vault has of a problem it keeps running into sideways: **usability measurement presumes a stationary object of study, and personalised systems are not stationary.** The violation happens twice.

> "Different users are using different versions of the product."

> "The product changes as the same person uses it."

The consequence is not that metrics get noisier. It is that they stay precise while their referent moves:

> "The number may be precise while the underlying construct it is measuring is not the same thing."

Bakhshi's structural claim — the one that does the most work — is that every score on an adaptive product is conditional and the conditions are usually unreported:

> "The score is conditional on the user, their history, the state of the system, and the stage of use."

The essay's most consequential section is the circularity argument. An adaptive system infers a preference, acts on it, thereby manufactures more of the behaviour it inferred, and reads the repetition as confirmation:

> "The system shapes the behavior and it later uses that same behavior as evidence of what the user wants."

Which produces the finding that should worry anyone reporting engagement: *"Engagement may rise while the experience gets more limited and more repetitive."*

The proposed alternative is four dimensions — Goal, Interaction (usability **plus steerability**), Outcome, Trajectory — offered explicitly as a decomposition rather than a replacement north-star score.

## Key Claims

- **Task success stops being definable in open-ended adaptive products.** *"When a user opens a video recommendation feed, it is not clear what should count as success."* The task was never specified, so completion has no referent.

- **Low effort is ambiguous, not good.** *"Less effort can mean better support, and it can also mean the user had less room to compare, question, or change what happened."* One-click purchase is the case: frictionless, and it removes price comparison, alternatives, and awareness of the commitment. This inverts the default reading of the most-used metric in the field.

- **Every behavioural metric on a feed has two readings and the metric cannot distinguish them.** More scrolling = bad recommendations, or active exploration. Video watched = satisfying feed, or effective clickbait. Daily engagement = valued habit, or a narrowed loop.

- **Attitudinal measures do not collapse into one another.** *"Satisfaction, trust, control, and usefulness are not interchangeable summaries of quality."* Named divergences: useful but hard to control; enjoyable without being trusted; satisfying within a session but not across weeks; trusting a single recommendation but not the system.

- **Steerability is usability's missing partner for adaptive systems.** A static interface needs to be operable. A system that has learned a model of you additionally needs to be *redirectable* — and the test includes whether corrections **persist or revert**.

- **Trajectory is a dimension, not a longitudinal nice-to-have.** Direction of change across sustained use is the thing a snapshot structurally cannot see, and on an adaptive product the direction is the finding.

- **The operative discipline is disclosure of conditions:** *"Make the conditions of our measures explicit: whose goal, which product state, what outcome, and what stage of use?"*

## Useful Examples

**The four dimensions** — the reusable artifact:

| Dimension | The question | Why the standard toolkit misses it |
|---|---|---|
| **Goal** | Whose objective, under what conditions? | Assumed given by the task script |
| **Interaction** | Usable *and* steerable? Do corrections stick? | Steerability has no standard instrument |
| **Outcome** | Did completing it leave the user better off? | Conflated with completion |
| **Trajectory** | Which way is this going across weeks? | Invisible to a single session |

**The short-video feed** — the anchor case. A new user scrolls past many irrelevant items before choosing, and the novelty is itself pleasurable despite the inefficiency. An experienced user selects faster. Faster is not better: the two are being measured on **different products at different stages**, and the metric reports one number.

**The circularity loop, step by step** — system observes a category preference → shows more of it → creates more opportunity for the same behaviour → reduces exposure to alternatives → user cannot demonstrate broader interest → repetition reads as confirmation. Note the mechanism: the evidence is not merely correlated with the system's action, it is *produced* by it.

**The separation that makes narrowing detectable:** track what the user was **shown** separately from what the user **did**, and measure exposure diversity. Without that split, narrowing and preference are indistinguishable in the data.

## Constraints / Caveats

- **No evidence of any kind.** No study, no data, no worked measurement, no example of the framework applied. This is argument, and it should be cited as argument.
- **Nothing is operationalised.** Steerability and trajectory are named and defended but given no instruments, items, or scoring. The essay's own stated position is that it is not trying to supply a replacement score — which is intellectually honest and leaves a practitioner with no next step.
- **Sampling cadence for trajectory is unaddressed.** How often you must measure to detect real directional change is the question that decides whether the dimension is affordable.
- **The distinguishing problem is stated, not solved.** Separating genuine preference change from system-induced narrowing is the hardest inference in the essay and it gets no method.
- **Feasibility at scale is not discussed** — the argument's own premise is that each user has an individualised product, and it does not say how conditions get recorded across millions of them.
- **The internal tension the essay half-acknowledges:** it rejects collapsing quality into a single score, then proposes four dimensions with no instruments, which in practice is either four scores or no measurement.
- **No engagement with the incentive problem.** The critique of engagement metrics assumes an organisation that wants to know. Where engagement is the business metric, "engagement may rise while the experience narrows" is not a measurement flaw to be fixed — see the tension below.

## Design Implications

- **Report conditions with every number.** Segment, product state, and stage of use, on the slide, next to the figure. This is the cheapest and most defensible thing in the essay and it requires no new instrument.
- **Stop treating reduced effort as an unqualified win.** For any friction removal, ask what comparison the friction was affording. Especially on purchase, consent, and irreversible actions.
- **Log exposure, not just behaviour.** If you cannot answer "what were they shown?", you cannot detect narrowing, and narrowing will look like satisfaction.
- **Add a steerability probe to adaptive-product studies:** can the user articulate how it personalises, redirect it, and does the redirect survive the next session? Three questions, and the third is the one products fail.
- **Design benchmarks around a declared product state** rather than pretending the product is one thing. A benchmark on a personalised surface without a stated state is not comparable to itself over time.
- **Do not composite satisfaction, trust, control, and usefulness.** Report them separately and expect them to disagree; the disagreement is the signal.

## Tensions

- **Directly against [[wiki/concepts/ux-research/ux-performance-benchmarking|UX performance benchmarking]] as practised.** Benchmarking's value proposition is comparability over time and against competitors. If the score is conditional on user, history, system state, and stage, comparability is not degraded — it is unwarranted unless the conditions are pinned. The vault's benchmarking material does not currently carry this caveat.
- **Sharpens [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX measurement constructs]] rather than contradicting it.** Sauro & Lewis propose an instrument for AI chat; Bakhshi's argument is that on an *adaptive* product the instrument's validity conditions move under it. The two are compatible and the pairing is unflattering to any attempt to benchmark AI products with either alone.
- **Against the vault's engagement-adjacent material, and against the industry's incentives.** [[wiki/concepts/product-management/ai-advertising|AI advertising]] records that non-verification is commercially valuable. Bakhshi's narrowing mechanism is, from that angle, not a defect — it is the product working. The essay never says this, and the conflict is the reason the recommendation "measure exposure diversity" will be resisted where it matters most.
- **Convergent with [[wiki/concepts/ux-research/algorithmic-self|algorithmic self]] and [[wiki/concepts/ux-research/algorithmic-monoculture|algorithmic monoculture]]** — the same feedback loop described at the individual level rather than the population level. Bakhshi's contribution is that she makes it a *measurement* problem rather than an ethics problem, which is what gives a researcher something to do about it.
- **Extends [[wiki/concepts/agent-experience/satisfaction-vs-benefit|satisfaction vs. benefit]] to behavioural metrics.** That concept records that a high self-reported score need not mean the user was helped. This says the same of effort, completion, and engagement — the metrics that were supposed to be the objective corrective to self-report.
- **Steerability against [[wiki/concepts/ux-research/progressive-user-control|progressive user control]].** Progressive control is about how much autonomy the user grants; steerability is about whether the user can change a model the system has already built of them. Adjacent, not the same, and the persistence question ("do corrections revert?") belongs only to the latter.

## Open Questions

- What instrument measures steerability? Nothing in the vault does, and correction-persistence is directly observable, so this is buildable.
- How often must trajectory be sampled to detect direction rather than noise?
- Can exposure diversity plus behaviour separate real preference change from induced narrowing, or is the inference unavailable without an intervention that removes the system's constraint?
- Bakhshi's fourth author-adjacent question, unasked here: if conditions must be reported for a score to mean anything, what is the minimum reportable condition set that keeps benchmarking honest without making it unaffordable?
- Does the four-dimension frame survive an organisation whose business metric is the engagement number it distrusts?

## Concepts Linked from This Source

- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]] *(new)*
- [[wiki/concepts/ux-research/steerability|Steerability]] *(new)*
- [[wiki/concepts/ux-research/ux-metrics|UX Metrics]]
- [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]]
- [[wiki/concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[wiki/concepts/ux-research/reliability-vs-validity|Reliability vs. Validity]]
- [[wiki/concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[wiki/concepts/ux-research/algorithmic-self|Algorithmic Self]]
- [[wiki/concepts/ux-research/algorithmic-monoculture|Algorithmic Monoculture]]
- [[wiki/concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs. Benefit]]
- [[wiki/concepts/ux-research/progressive-user-control|Progressive User Control]]
- [[wiki/methods/usability-testing|Usability Testing]]
- [[wiki/methods/longitudinal-research|Longitudinal Research]]
- [[wiki/methods/benchmark-studies|Benchmark Studies]]

## LLM Use Guidance

- **Use the four dimensions to structure any evaluation plan for a personalised or adaptive product.** They are a good decomposition even though they come with no instruments.
- **Use the conditions sentence verbatim as a reporting standard** — whose goal, which product state, what outcome, what stage of use. It is the most portable thing in the source.
- **Use the two-readings test on every behavioural metric** before reporting it: what is the other explanation for this number moving?
- **Do not cite this as evidence about adaptive products.** There is none. It is a well-argued conceptual critique, and stating it that way is what keeps it usable.
- **Do not treat the four dimensions as a validated framework or compute a composite from them.** The author explicitly declines to offer a replacement score.
- Pair with [[wiki/concepts/product-management/ai-advertising|AI advertising]] whenever recommending exposure-diversity measurement to a business that monetises attention — the recommendation is sound and the resistance is structural.

## Reliability Notes

- **Confidence 0.72.** Higher than the vault's usual score for an evidence-free essay, for three reasons: the central argument is a *validity* argument that does not require data to be sound; the effort-ambiguity and circularity claims are individually checkable against any recommender product; and the author is a practising quantitative researcher writing within her competence, with four prior sources in this vault ([[wiki/sources/saeidehbakhshi-ai-in-quantitative-research|AI in quantitative research]], [[wiki/sources/saeidehbakhshi-long-accommodation|long accommodation]], [[wiki/sources/saeidehbakhshi-wicked-work-ai-unbundles-research|wicked work]], [[wiki/sources/saeidehbakhshi-the-fallacy-of-depth-at-scale|the fallacy of depth at scale]]) and no accuracy problems recorded against them.
- Held below 0.80 by the absence of any operationalisation, any worked example of the framework in use, and any empirical demonstration that the four dimensions capture something the standard toolkit misses.
- **Do not upgrade this on rhetorical strength.** The argument is persuasive precisely because it is internally coherent, which is not the same as being right about effect sizes.
- **Highest-value verification step:** run one adaptive-product study that reports conditions per Bakhshi and measures correction-persistence. Either the reported conditions change the conclusion or they do not, and that is a cheap, decisive test of the essay's core claim.
