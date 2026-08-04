---
type: concept
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [concept, ux-research, ux-context-design, ai-readable-documentation, context-engineering, research-artifacts, design-md, nngroup]
sources: [nngroup-ux-context-design, atlassian-design-md, yozm-obsidian-llm-wiki-secondbrain]
confidence: 0.66
---

# UX-Context Design

> [!abstract] Summary
> The practice of curating what an organisation knows about its users into the **context that steers its AI tools' output** — rather than into documents written to persuade humans. Named by [[wiki/sources/nngroup-ux-context-design|Alicea (NN/g, 2026)]]:
>
> *"The practice of discovering and curating what an organization knows and wants into the context that guides everything its AI tools generate."*

## Why It Matters

Two shifts make this a different job rather than a rename.

**The audience changed.** A persona is built to persuade a stakeholder — hence the stock photo, the name, the narrative. A model does not need persuading. *"The model does not need persuading, it needs the underlying reasoning."* Everything in the artifact that was doing rhetorical work is now dead weight, and the reasoning that was implicit becomes the payload.

**The success criterion changed.** *"Its success is measured by whether AI output improves, not by whether stakeholders are convinced."* This replaces the profession's traditional measure — buy-in — with an output test. It is the most consequential claim in the practice, and also the least verified.

The structural driver: when *"designers are no longer the only people producing designs,"* insight can no longer travel by review meeting. It has to be deposited somewhere the generator reads.

## Key Claims

- **Context biases, it does not instruct.** *"Context leans a model's output in a particular direction."* Without it, generation lands on the statistical middle. The house-builder analogy: a builder who never meets the family builds an average two-storey house and misses the wheelchair ramp.

- **An AI-ready deliverable has three properties** — machine-readable, curated by a skilled human, available across the organisation. The middle one is load-bearing: this is not "dump the research folder into the repo."

- **`DESIGN.md` is the existence proof.** Google Labs' April 2026 format holds machine-readable design-system values beside human-readable rationale. See [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]]. The format works; the question is what else goes in it.

- **The proposed five components of a `UX.md`:**

  | Component | Content | Why the generator needs it |
  |---|---|---|
  | Research synthesis | Insights as **actionable constraints** | A finding phrased as an observation cannot be obeyed |
  | Interaction standards | Behavioural guidelines | What it does, separate from how it looks |
  | Glossary | The users' own vocabulary | *"If your users say 'case' and are confused by 'ticket,' the AI should know that"* |
  | User models | Expertise, concerns, goals, pain points | The persona minus the persuasion |
  | World models | Circumstances of use | The component no traditional artifact carries |

- **World models are the usual omission.** Not who the user is but what is happening around them — a nurse interrupted mid-task on a hospital floor; a person filing a claim from the roadside. A persona carries neither.

- **The obeyability test is the practical filter.** "Users found the flow confusing" cannot be obeyed. "Never ask for a policy number before the incident date, because users file from the roadside without documents" can. This test is useful whether or not AI is involved.

- **There is no handoff and no done state.** *"Never finished. New research updates it, and so does watching what the AI gets wrong."* The generator's failures become a research queue — someone has already localised the gap for you.

- **Curation decisions have a shelf life.** *"A curation decision made for today's models may be wrong for next year's."*

## ⚖️ Conflicts & Caveats

> [!warning] The central claim has no evidence
> *"Our experiments suggest that curated UX context improves AI-generated UI"* is the entire empirical basis — no methodology, sample, baseline, or definition of "improves." From NN/g, whose authority is empirical, that absence should be named rather than excused. The practice is a reasonable way to organise work; it is not established that it pays.

> [!warning] The measurement proposal is circular as stated
> "Success is whether AI output improves" requires an independent judgment of improvement. If the same person writes the context and judges the output, the loop closes on itself. Alicea does not notice this.

> [!warning] A context file is also a synthetic-user substrate
> The same curated user and world models that improve interface generation make a model a *more convincing and no more accurate* fake user. See [[wiki/concepts/ux-research/synthetic-user-bias|Synthetic User Bias]] and [[wiki/concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]]. The purposes differ; the file does not. Anyone who builds a `UX.md` has built both.

> [!warning] Curation failure is the unaddressed failure mode
> A wrong, stale, or contested constraint is obeyed silently by every subsequent generation. Where [[wiki/concepts/ux-research/democratization-of-insights|democratization of insights]] fails by human misinterpretation, this fails by **silent over-application at scale with no reviewer between the constraint and the artifact.** The article treats only the upside.

> [!warning] `UX.md` does not exist
> It is a proposal in an article. `DESIGN.md` exists and has adoption; `UX.md` has neither. Do not cite them as equivalent.

**Unresolved:** organisations hold contradictory beliefs about their users. A persuasion document tolerates that ambiguity; a constraint file cannot. Who arbitrates is unaddressed by the source and unknown here.

## This Vault Is an Instance

[[wiki/concepts/infrastructure-dev/llm-wiki|LLM-Wiki]], `CLAUDE.md`, `AGENTS.md`, and the `llm_ready` flag on every source page are UX-context design as described — built before the article named it. That gives a testable prediction: if the practice works, the pages the agent actually relies on should be the ones whose constraints are phrased most obeyably. **This has never been checked here**, and it is the cheapest available test of the whole idea.

## Practical Guidance

1. **Rewrite findings as constraints.** Apply the obeyability test as an editorial filter.
2. **Write the world model down explicitly** — it is the emptiest component and the one that most changes output.
3. **Capture the users' vocabulary, including the words that confuse them.** Cheap, unambiguous, immediately effective on generated copy.
4. **Treat wrong generations as a research queue** rather than as model failure.
5. **Version context with the product code.** Storing it elsewhere reintroduces the staleness that killed the wiki-as-handoff.
6. **Keep a human-readable rationale layer** beside the machine-readable values, per `DESIGN.md`. The reviewer needs to know why a value is what it is.
7. **Get an independent judge of output quality** — otherwise the measurement is circular.

## 🔗 Related Concepts

- [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]] — the working precedent.
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]] — the general form.
- [[wiki/concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]] — the same pattern for agent instructions.
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]] — the engineering discipline this is the UX branch of.
- [[wiki/concepts/infrastructure-dev/llm-wiki|LLM Wiki]] — this vault, as an instance.
- [[wiki/concepts/ux-research/evidence-engineering|Evidence Engineering]] — the adjacent argument about research output as durable artifact.
- [[wiki/concepts/ux-research/democratization-of-insights|Democratization of Insights]] — the predecessor practice, with a different failure mode.
- [[wiki/concepts/product-management/insight-to-execution-gap|Insight-to-Execution Gap]] — the problem this claims to close.
- [[wiki/concepts/ux-research/synthetic-user-bias|Synthetic User Bias]] — the risk the same artifact creates.
- [[wiki/concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] — the same move applied to the component layer.

## 📚 Sources

- [[wiki/sources/nngroup-ux-context-design|Alicea (2026): UX-Context Design]] — names the practice, proposes `UX.md`, supplies the five components and the obeyability framing. Sole source for the practice as such.
- [[wiki/sources/atlassian-design-md|Atlassian: DESIGN.md]] — the machine-readable-design-context precedent.
- [[wiki/sources/yozm-obsidian-llm-wiki-secondbrain|Yozm: Obsidian LLM Wiki]] — the vault-as-context-substrate pattern.

## ❓ Open Questions

- Which artifact types actually move generated output, and by how much? Answerable with a small controlled comparison; nobody has run one.
- Does a context file drift toward what the model handles well rather than what is true about users? That is the selection pressure the feedback loop creates, and it is unexamined.
- Is there a saturation point past which more context degrades rather than plateaus?
- What is the review process for a contested constraint, and who owns it?
- Does the practice survive an organisation that disagrees with itself about its users?
