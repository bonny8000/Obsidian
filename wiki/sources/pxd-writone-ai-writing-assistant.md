---
type: source
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [ux-writing, ai-writing-assistant, figma-plugin, rule-based-rag, transparency, explainability, automation-bias, workflow-placement, pxd, korea]
source_path: raw/web/pxd-writone-ai-writing-assistant-2026-07-31.md
source_url: https://pxdstory.tistory.com/m/1911
authors: [Yejin.lee]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.65
---

# pxd (2026): Writone — Where an AI Writing Assistant Has to Live

## Citation

Yejin.lee, 「AI 라이팅 어시스턴트, Writone 개선기」 *(AI Writing Assistant, Writone: An Improvement Log)*, **pxd story**, 2026-07-30. Category: pxd AI툴 이야기.

**Source type:** First-party product improvement log from a UX consultancy about its own tool, following on from a September 2024 experiment by the same team.
**Raw capture:** [[raw/web/pxd-writone-ai-writing-assistant-2026-07-31|pxd-writone-ai-writing-assistant-2026-07-31]]
**Coverage note:** `coverage: substantial` — the argument, the rule hierarchy, the architecture change, and the trust principles were all captured. No quantitative results exist in the source to capture.

Third pxd source in this vault, after [[wiki/sources/pxd-story-ai-insights|pxd AI insights]] and [[wiki/sources/pxd-color-token-design-2026|pxd color token design]].

## Summary

pxd's team had already asked, in 2024, whether AI could learn a company's UX Writing guidelines. The answer turned out to be the wrong question. The reframed one is:

> "AI Writing 어시스턴트가 실제로 쓰이려면, 사용자의 경험 중 어디에 있어야 하는가?"
> *"For an AI writing assistant to actually get used, where in the user's experience must it live?"*

The observation behind it is mundane and, for that reason, useful: companies spend heavily producing UX Writing guidelines that then sit as PDFs in cloud storage. Not because practitioners disagree with them, but because checking one means leaving Figma, opening a hundred-page document, finding the rule, and coming back. **The switching cost, not the rule quality, is what kills compliance.**

Everything else in the piece follows from placing the tool inside Figma: the plugin can read layer nodes for context, and can tell a button from a toast and apply the right rule to each.

## Key Claims

- **Placement determines adoption more than capability does.** *"UX Writing 검토의 필요성은 인지하지만, 그것을 위해 흐름을 끊는 전환 비용이 너무 크다"* — practitioners recognise the need but the cost of breaking flow is too high. The design conclusion: *"기술이 아닌 사람의 흐름에서 출발했기 때문에, 제품이 있어야 할 자리가 자연스럽게 결정되었다"* — starting from the human workflow rather than the technology decided the product's location naturally. See [[wiki/concepts/infrastructure-dev/in-workflow-ai-placement|In-Workflow AI Placement]].

- **A Figma plugin buys context a web app cannot.** Beyond removing the interruption, the plugin reads **layer node information**, so corrections are context-aware, and it can distinguish **UI element types** — applying button rules to buttons and toast rules to toasts. The same argument [[wiki/sources/karrot-kraft-design-system-agent|Kraft]] makes for moving from a hosted admin to a local CLI: the move is to acquire context, not convenience.

- **Rules should be hierarchical, not a flat list.** Aaron Walter's hierarchy-of-user-needs model was applied to structure the guideline so the AI can understand relations between rules and the practitioner can follow the logic of a correction. Four levels: **terminology → UI rules → grammar → principles/tone**.

- **Rule-based RAG over similarity search.** Rather than retrieving passages that look similar to the input, the system extracts abstract rules from the PDF (e.g. *"경로 표기는 '→'로 통일한다"* — unify path notation as '→') and matches them contextually. The stated payoff is that a correction becomes **justifiable** rather than merely plausible — retrieval that returns a rule can cite it; retrieval that returns similar text cannot.

- **Three principles for trust, with automation bias named as the target.** *Transparency* — show the guideline source and principle page for every correction. *Explainability* — give the reason in human language, not algorithmic terms (citing the McKinsey 2024 AI survey on explainability as an enterprise adoption risk). *Human control* — *"AI는 선택지를 제시하고, 판단은 사람이 합니다"* — AI presents options, the person judges.

- **Position the tool as an assistant, explicitly.** Writone is framed as "the smartest assistant," not an autonomous decision-maker, so that professional judgment stays with the practitioner and the guideline becomes *"살아 움직이는"* — living — rather than dormant.

## Useful Examples

**The four-level rule hierarchy** — the most reusable artifact here:

| Level | Scope | Example given |
|---|---|---|
| 1 | **Terminology** — banned term → recommended term | '익월' → '다음 달'; '당사' → 'OO증권' |
| 2 | **UI rules** — per component | buttons concise, noun-form ending; tooltips may explain at length |
| 3 | **Grammar** — structure, format, tone consistency | path notation unified as '→' |
| 4 | **Principles / tone** — brand philosophy | clarity, brevity, user-centricity |

The ordering matters for conflict resolution: a level-1 terminology substitution is mechanical and safe to apply; a level-4 tone judgment is not. The source does not say this explicitly, but the hierarchy makes it available.

**The workflow that was actually observed:** planning → Figma → insert text → review → revise. The guideline check is not a stage in this flow; it is an interruption of it. That framing — audit where the work already happens before deciding where the tool goes — is the transferable method.

## Constraints / Caveats

- **No quantitative results whatsoever.** No adoption figures, no correction-accuracy measurement, no before/after guideline-compliance rate, no time saved. For a piece whose thesis is that placement drives adoption, no adoption data is offered.
- **No failure cases.** The source states no scope limits and reports nothing that did not work — unusual for an "improvement log" and a reason to discount its confidence.
- **Rule-extraction fidelity is asserted, not evidenced.** How reliably abstract rules are pulled out of a PDF is the load-bearing technical claim, and it is unexamined. A wrong rule extracted confidently is worse than no tool.
- **First-party**: Writone is pxd's own product, described on pxd's own blog.
- **The Aaron Walter transfer is by analogy.** His model describes user needs, not rule precedence. Applying it as a rule hierarchy is a reasonable metaphor, not a validated mapping.
- **The McKinsey citation is second-hand** — year only, no sample, question wording, or page.
- Korean-language context throughout; no discussion of whether the hierarchy or extraction survives other languages.

## Design Implications

- **Audit the workflow before designing the interface.** The finding that reframed this product came from watching where the check actually happens, not from asking whether AI could do it.
- **Make retrieval return rules, not passages,** when the output has to be defensible. This is the difference between "here is something similar" and "here is the rule, and here is where it lives."
- **Give the correction a citation.** Transparency here is not a disclosure banner — it is a pointer to the specific guideline page. That is a materially stronger form than the labels [[wiki/concepts/agent-experience/checkbox-transparency|checkbox transparency]] warns about, because it is checkable.
- **Order rules by how safely they can be automated.** Terminology substitution can be near-automatic; tone cannot. A flat rule list forfeits this distinction.

## Tensions

- **Transparency's track record cuts against the optimism here.** Writone's first two principles are transparency and explainability, and this vault now holds two independent results ([[wiki/sources/kakao-vc-ai-agent-advertising|the Princeton figures]] and [[wiki/sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan's willful blindness]]) where disclosure under-performed. The reconciliation is plausible but untested: those cases involved a counterparty with an interest in over-trust, while a guideline citation invites a comparison the user can actually make — which is precisely the mechanism [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the trust memo]] identifies as what makes disclosure work. **Writone is the favourable case for disclosure, not a refutation of the unfavourable ones.**
- **"Human control" is asserted, not designed for.** Naming automation bias as the risk and answering it with "the human decides" is the answer [[wiki/concepts/agent-experience/willful-blindness|willful blindness]] shows to be insufficient — people accept AI suggestions without asking why, especially under the deadline pressure this source identifies as the original problem. The source does not measure acceptance rates, so it cannot know whether its own principle holds.
- **Converges with [[wiki/sources/karrot-kraft-design-system-agent|Kraft]] independently** on tools joining the existing workflow rather than replacing it — one from UX writing, one from screen generation, neither citing the other.

## Open Questions

- What fraction of Writone's suggestions are accepted, and does that fraction differ between level-1 terminology fixes and level-4 tone rewrites? That single measurement would test the automation-bias concern directly.
- How accurate is rule extraction from an arbitrary guideline PDF, and what happens when the document contradicts itself — as hundred-page guidelines usually do?
- Does citing the source page actually change practitioner behaviour, or is it read as reassurance and skipped?
- Does the four-level hierarchy survive a guideline written without it in mind?

## Concepts Linked from This Source

- [[wiki/concepts/infrastructure-dev/in-workflow-ai-placement|In-Workflow AI Placement]] *(new)*
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[wiki/concepts/agent-experience/checkbox-transparency|Checkbox Transparency]]
- [[wiki/concepts/agent-experience/willful-blindness|Willful Blindness]]
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]]
- [[wiki/concepts/ai-agents/agentic-rag|Agentic RAG]]
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]

## LLM Use Guidance

- Use for the **workflow-placement argument** and the **four-level rule hierarchy** — both are clean, transferable, and the strongest things here.
- Use the **rule-based RAG vs. similarity search** distinction when designing any retrieval that must justify an output rather than merely produce one.
- **Do not cite for efficacy or for adoption.** There is no evidence in this source that Writone works, only an account of why it is shaped as it is.
- Treat the trust-principles section as a **design stance**, not as a validated mitigation of automation bias.

## Reliability Notes

- **Confidence 0.65.** The workflow observation and the design reasoning are coherent and consistent with other sources in this vault; the score is held down by zero measurement, zero failure cases, first-party authorship about a first-party product, and one load-bearing technical claim (rule extraction fidelity) left entirely unexamined.
- Third pxd source, and the publisher's analytical quality has been consistent. Note that all three are first-party accounts by a consultancy with a commercial interest in AI-tooling expertise.
- **Highest-value verification step:** a suggestion-acceptance rate broken down by rule level. It would test both the adoption thesis and the automation-bias concern with one number.
