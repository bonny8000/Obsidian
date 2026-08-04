---
type: source
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [ux-context-design, ai-readable-documentation, design-md, context-engineering, research-artifacts, nngroup, democratization]
source_path: raw/web/nngroup-ux-context-design-2026-08-04.md
source_url: https://www.nngroup.com/articles/ux-context-design/
authors: [Tony Alicea]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.66
---

# Alicea (2026): UX-Context Design

## Citation

Tony Alicea, "UX-Context Design: Using UX Knowledge to Inform AI-Generated Design," **Nielsen Norman Group**, 2026-07-24.

**Source type:** Practitioner article from a high-authority UX institution, proposing and naming a practice. No study, no data.
**Raw capture:** [[raw/web/nngroup-ux-context-design-2026-08-04|nngroup-ux-context-design-2026-08-04]]
**Coverage note:** `coverage: full` — the article is short and was captured end to end, including the five `UX.md` components and all six of the author's own open questions.

## Summary

NN/g gives a name to something this vault has been doing without one. The claim: when AI generates the interface work, the deliverable of UX research and design stops being a document written to persuade humans and becomes **context curated to steer machines**.

> "The practice of discovering and curating what an organization knows and wants into the context that guides everything its AI tools generate: from who its users are and the world they live in, to how a product should look and behave."

The mechanism claim is modest and correct: context does not instruct, it biases. *"Context leans a model's output in a particular direction."* Without it a model produces the statistical middle — the article's house-builder analogy is that a builder who never meets the family builds an average two-storey house and misses the wheelchair ramp.

The structural argument is the more interesting one. Because *"designers are no longer the only people producing designs,"* research insight can no longer travel by review meeting. It has to be **deposited somewhere the generator reads**, which makes the artifact's audience a model and its success criterion mechanical:

> "Its success is measured by whether AI output improves, not by whether stakeholders are convinced."

That single sentence is the reason this source matters. It replaces the profession's traditional success measure — stakeholder buy-in — with an output test.

## Key Claims

- **A persona built to persuade is the wrong artifact.** *"A persona has a stock photo … the model does not need persuading, it needs the underlying reasoning."* The stock photo, the name, the narrative are all persuasion scaffolding. What survives translation to context is the reasoning: what this user knows, fears, is trying to do, and is prevented from doing.

- **An AI-ready deliverable has three properties:** machine-readable, curated by a skilled human, and available across the organisation. The middle one is the load-bearing constraint — the article does not propose dumping raw research into a folder.

- **`DESIGN.md` is the existence proof.** Google Labs' April 2026 open format holds machine-readable design-system values (colours, type sizes, spacing, radii) beside human-readable guidance on application and accessibility. It already works, so the format is not hypothetical.

- **`UX.md` is the proposed extension** — five components: research synthesis expressed as *actionable constraints*, interaction standards, a glossary of the users' own vocabulary, user models, and world models.

- **World models are the part usually missing.** Not who the user is but what is happening around them: a nurse interrupted mid-task on a hospital floor; a person filing a claim immediately after an accident. Neither is captured by a persona.

- **There is no handoff and no done state.** *"Never finished. New research updates it, and so does watching what the AI gets wrong."* The generator's failures become a research input — a feedback channel that did not exist when the deliverable's audience was human.

- **The curation decision has a shelf life.** *"A curation decision made for today's models may be wrong for next year's."*

## Useful Examples

**The five `UX.md` components** — the reusable artifact:

| Component | Content | Why the model needs it |
|---|---|---|
| Research synthesis | Insights as actionable constraints | A finding phrased as a constraint can be obeyed; phrased as an observation it cannot |
| Interaction standards | Behavioural guidelines | What the product does, separate from how it looks |
| Glossary | The users' own vocabulary | *"If your users say 'case' and are confused by 'ticket,' the AI should know that"* |
| User models | Expertise, concerns, goals, pain points | The persona minus the persuasion |
| World models | Circumstances of use | The part no traditional artifact carries |

**The `DESIGN.md` split** — machine-readable values plus human-readable guidance in one file. The pattern generalises: the numbers are for the generator, the prose is for the person deciding whether the generator got it right.

**The starting move the article prescribes:** extract a few user insights into plain markdown, make them visible to the team's AI tools, convert the design system to a machine-readable format, then watch whether generated output improves. Deliberately small — the point is that the entry cost is a text file.

## Constraints / Caveats

- **No evidence.** *"Our experiments suggest that curated UX context improves AI-generated UI"* is the whole empirical basis: no methodology, no sample, no baseline, no comparison, no definition of "improves." From NN/g, whose authority rests on empirical work, the absence is conspicuous and should be named rather than excused.
- **"Many teams are already practicing UX-context design"** is supported by a link to another article, not by a survey or count.
- **The six open questions are the article's own,** and they are the six that decide whether the practice is operable: which artifacts help, how much raw data, what metrics, how the answers move as models improve, whether context saturates, and how this is maintained at scale. None is answered.
- **Curation quality is assumed, not addressed.** The article requires a skilled human curator and never discusses what happens when the curation is wrong, stale, or contested — which is the failure mode that matters, because a bad constraint in context is obeyed silently by every generation thereafter.
- **No treatment of conflict.** Real organisations hold contradictory beliefs about their users. A persuasion document can survive that ambiguity; a constraint file cannot. Who resolves the conflict is unaddressed.
- **The measurement proposal is circular as stated.** "Success is whether AI output improves" needs an independent judgment of improvement, and if that judgment is itself made by whoever wrote the context, the loop closes on itself. The article does not notice this.
- **`UX.md` does not exist.** It is a proposal in an article, not a format, spec, or tool. Do not cite it as though `DESIGN.md`-style adoption exists for it.

## Design Implications

- **Rewrite findings as constraints.** The practical test for a research output is whether a generator could obey it. "Users found the flow confusing" cannot be obeyed. "Never ask for a policy number before the incident date, because users file claims from the roadside without documents" can.
- **Write the world model down explicitly.** It is the component with no traditional home and the one that most changes generated output, because it is what the model cannot infer from the product.
- **Capture the users' vocabulary as a glossary,** including the words that confuse them. This is cheap, unambiguous, and immediately effective on generated copy.
- **Treat the generator's mistakes as a research queue.** Every wrong generation is a gap in the context, and it is a gap someone has already localised for you.
- **Version context with the product code.** Storing it elsewhere reintroduces the staleness problem that killed the wiki-as-handoff.
- **Keep a human-readable layer beside the machine-readable one,** per `DESIGN.md`. The reviewer needs to know why a value is what it is.

## Tensions

- **This vault is an instance of the thing being named.** [[wiki/concepts/infrastructure-dev/llm-wiki|LLM-Wiki]], `CLAUDE.md`, `AGENTS.md`, and the `llm_ready` flag on every source page are UX-context design as described — built before the article named it. The useful consequence is a testable prediction: if the practice works, the pages the agent reads most should be the ones whose constraints are phrased most obeyably. That has never been checked here.
- **Against the vault's own accumulated caution about synthetic users.** [[wiki/concepts/ux-research/grounded-synthetic-personas|Grounded synthetic personas]] and [[wiki/concepts/ux-research/synthetic-user-bias|synthetic user bias]] record that a model given user context will confidently generate user-shaped output that is wrong. This article proposes feeding models exactly that context, for a different purpose (generating interfaces, not generating research findings). The distinction holds, but it is thin, and the same file serves both uses. Anyone who builds a `UX.md` has built a synthetic-user substrate whether they meant to or not.
- **Against [[wiki/concepts/ux-research/democratization-of-insights|democratization of insights]].** Democratization moved insight to more humans and its known failure is misinterpretation by non-researchers. This moves insight into a generator, which does not misinterpret so much as *over-apply* — silently, at scale, with no reviewer between the constraint and the artifact. Different failure mode, and the article treats only the upside.
- **Convergent with [[wiki/sources/carl-pearson-minimally-technical-reporting|Pearson]] and [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco]]:** all three argue the artifact must be shaped to its receiver rather than to its producer. Alicea's receiver is a model. None of the three cites the others; the pairing is this vault's.
- **The measurement gap is the vault's standing complaint again.** [[wiki/analyses/2026-07-31-constraint-architectures-converge|The 2026-07-31 memo]] found that eight sources converge on what good constraint architecture looks like and one has measured it. This is a ninth source proposing constraints with no measurement, from the institution best equipped to supply it.

## Open Questions

- Which artifact types actually move generated output, and by how much? The article asks this and it is answerable with a small controlled comparison that NN/g could run.
- Does a context file drift toward what the model handles well rather than what is true about users? That is the selection pressure the feedback loop creates and nobody has looked for it.
- What is the review process for a contested constraint, and who owns it?
- Is there a saturation point, and does context past it degrade output rather than plateau?
- Does `UX.md` survive contact with an organisation that disagrees with itself?

## Concepts Linked from This Source

- [[wiki/concepts/ux-research/ux-context-design|UX-Context Design]] *(new)*
- [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]]
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]]
- [[wiki/concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]]
- [[wiki/concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]
- [[wiki/concepts/ux-research/democratization-of-insights|Democratization of Insights]]
- [[wiki/concepts/ux-research/evidence-engineering|Evidence Engineering]]
- [[wiki/concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]
- [[wiki/concepts/product-management/insight-to-execution-gap|Insight-to-Execution Gap]]

## LLM Use Guidance

- **Use the five `UX.md` components as a checklist** when assembling context for any generation task. The world-model row is the one most likely to be empty and most likely to matter.
- **Use the obeyability test** on research findings: could a generator act on this sentence? It is a good editorial filter regardless of whether AI is involved.
- **Do not cite the "our experiments suggest" claim as evidence.** It has no methodology attached and is the article's only empirical assertion.
- **Do not present `UX.md` as an existing standard.** `DESIGN.md` exists; `UX.md` is a proposal.
- When applying this to research artifacts, pair with [[wiki/concepts/ux-research/synthetic-user-bias|synthetic user bias]] — the same curated context that improves interface generation will also make a model a more convincing and no more accurate fake user.

## Reliability Notes

- **Confidence 0.66.** High for the framing and the naming: the practice is real, the mechanism (context biases rather than instructs) is correctly stated, `DESIGN.md` is a genuine precedent, and the article is unusually honest in listing what it does not know. Held down by a complete absence of evidence for its central claim, a circular measurement proposal, and no treatment of curation failure — from a publisher whose authority is empirical.
- The **framework** is usable now; the **effect size** is unestablished. Use it as a way to organise work, not as a warrant that the work pays off.
- **Highest-value verification step:** a controlled comparison of generated UI with and without each `UX.md` component. It is cheap, it is the article's own first open question, and it would convert this source from a naming exercise into evidence.
