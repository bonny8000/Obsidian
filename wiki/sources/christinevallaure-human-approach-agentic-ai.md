---
type: source
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [agentic-ai, multi-agent, claude-cowork, claudemd, markdown-orchestration, persona-agents, solo-builder, 1-person-vault, natural-language-prompting, agent-experience]
source_path: raw/web/christinevallaure-human-approach-agentic-ai-2026-06-29.md
source_url: https://substack.com/@christinevallaure/note/p-191484683
authors: [Christine Vallaure]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.72
---

# Christine Vallaure (2026): A Human Approach to Agentic AI — One Person, One Text File, Five Agents

**Christine Vallaure (moonlearning.io founder), Substack, 2026-03-26.**
**Raw capture:** [[raw/web/christinevallaure-human-approach-agentic-ai-2026-06-29|christinevallaure-human-approach-agentic-ai-2026-06-29]]
**URL:** [christinevallaure.substack.com](https://christinevallaure.substack.com/p/a-human-approach-to-agentic-ai-one)

> [!note] Practitioner narrative + book promotion
> This is a self-published first-person story (the Substack *note* redirects to a full article), not independent research. It is effectively a teaser for the author's upcoming book **CHORUS**. Claims about "emergent collaboration" and the productivity of human-named personas are her lived experience with a sample of one. Treat as a vivid pattern source, not evidence. Captured full via web_fetch and cross-checked against the UX Collective republication.

## Citation

Vallaure, C. (2026, March 26). *A Human Approach to Agentic AI. One person. One text file. Five agents.* Christine Vallaure (Substack). Also republished on UX Collective. Captured 2026-06-29 into `raw/web/christinevallaure-human-approach-agentic-ai-2026-06-29.md` (resolved from the note URL `substack.com/@christinevallaure/note/p-191484683`).

## Summary

A non-coder UX educator runs the editorial and commercial operations of her book SOLO (and an upcoming book, CHORUS) with a five-agent "team" defined entirely in plain markdown and driven through **Claude Cowork**. The entire team — roles, voice, and rules — lives in a single ~106-line `CLAUDE.md`, supported by a handful of folders (`context/`, `status/`, `output/`, `website-source/`); agents read files only when needed. Her thesis is that "the only skill you need is being able to have a human conversation": no programming, just markdown plus casual dialogue. The agents are given human names (after favourite female writers), which she argues compresses a 500-line specification into a single evocative word, and they began coordinating with each other without being instructed to. She emphasizes natural over formal prompting, the win from *simplifying* an over-engineered setup, and an explicit "Be honest, not helpful" stance. She is candid about limits: weak on heavy data and large documents, no persistence across days, occasional hallucination, "reason[ing] from patterns, not facts."

## Key Claims

- **A whole multi-agent system fits in one ~106-line markdown file.** `CLAUDE.md` holds five role/voice/rule definitions; supporting folders (`context/`, `status/`, `output/`, `website-source/`) are read on demand. "It is not code — it can be read and edited in any text editor." This is a maximally low-floor instance of a [[concepts/ai-agents/1-person-vault|one-person vault]] / [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md as context substrate]].
- **The only required skill is human conversation.** No coding, no orchestration framework, no infra. Operated through [[concepts/ai-agents/cowork|Claude Cowork]].
- **Human names do the work of long specs.** "A name does in one word what a detailed specification tries to do in five hundred." Naming agents after writers (Elke, Joan, Caitlin, Miranda, Rachel) leverages the model's existing associations. "Seven lines and one instruction. That is what separates a generic chatbot from five distinct people."
- **Inter-agent collaboration emerged unprogrammed.** Set up individually, the agents began discussing among themselves; the model inferred coordination from the role descriptions — an informal, name-driven [[concepts/ai-agents/multi-agent-coordination|multi-agent coordination]].
- **Division of labour: AI does grunt work; the human does the thinking and every decision.** She drafts roughly ("paste it in and say, 'Caitlin, clean this up'"); the AI shapes/structures; she supplies original thinking, stories, and judgment — a clear [[concepts/ai-agents/ai-as-thinking-partner|thinking-partner]] / [[concepts/product-management/domain-expert-as-builder|domain-expert-as-builder]] split.
- **Simplify, don't over-engineer.** Her first build was over-specified (backstories, complex reading instructions). She asked the AI to critique itself; stripping to essentials and removing unnecessary file reads improved speed significantly — an argument for [[concepts/ai-agents/context-engineering|lean context engineering]] over elaborate prompting.
- **Casual conversation beats formal prompting.** "hey Elke, what's the deal with Part 3?" outperforms structured requests.
- **"Be honest, not helpful."** A deliberate counter-sycophancy stance ([[concepts/agent-experience/ai-sycophancy|sycophancy]]); the Rachel agent challenged the author's affiliate-link practices and pushed for more vulnerable writing.
- **Stated limits.** Good for creative/editorial/focused work; weak on complex data processing and large documents; "reason[s] from patterns, not facts"; no cross-day persistence without intervention; occasional hallucination.

## Useful Examples

- **The five named agents and their beats:** Elke (Editor-in-Chief / oversight), Joan (Sales & Growth / pricing & strategy), Caitlin (Voice / tone consistency), Miranda (Product / design & build), Rachel (Reader Advocate / reader impact, "human truth," uncomfortable questions).
- **Rachel's origin:** emerged from a "completely unproductive" late-night chat (reading Rachel Cusk in bed) and became the most transformative agent — evidence that low-stakes exploratory conversation can define a genuinely useful role.
- **"Caitlin, clean this up"** as the canonical request shape — a persona handle plus a plain-language instruction.
- **Self-critique loop:** asking the AI to review its own over-engineered setup and recommend cuts.
- **Concrete numbers:** SOLO ebook **€29**; **30+ samples** in the extended brand-voice guidelines; **~€90** initial setup cost.

## Constraints / Caveats

- **n = 1 practitioner story, and a book teaser.** No baseline, no comparison, no measurement; "emergent collaboration" is observed, not tested. Effectively promotion for the upcoming **CHORUS** book.
- **Self-reported productivity.** Claims that names "do the work of 500 lines" and that casual prompting "yields better results" are impressions, not benchmarks.
- **Tooling-specific.** Reflects Claude Cowork / Claude Opus behaviour as of early 2026; persona-from-name and emergent-coordination effects may not transfer to other models/harnesses.
- **Does NOT prove** that markdown-only multi-agent setups scale beyond a solo creative/editorial workload — the author herself flags weakness on data-heavy and large-document tasks and the lack of cross-day persistence.

## Design Implications

- **Lower the floor for agent orchestration.** A single human-readable `CLAUDE.md` plus on-demand folders is a viable starting harness for non-engineers — pair this with [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md context]] and [[concepts/ai-agents/1-person-vault|1-person-vault]] patterns when designing AX for solo builders.
- **Persona handles as an interaction primitive.** Naming agents (and addressing them by name) is a cheap, legible affordance for routing intent in a [[concepts/ai-agents/multi-agent-coordination|multi-agent]] setup; design [[concepts/agent-experience/mental-model-onboarding|mental models]] around named roles rather than opaque tool calls.
- **Engineer for honesty, not agreeableness.** Bake a "be honest, not helpful" instruction and an explicit "advocate/critic" role (Rachel) into agent teams to counter [[concepts/agent-experience/ai-sycophancy|sycophancy]] and surface uncomfortable truths.
- **Favour lean context.** Strip backstories and unnecessary file reads; let the model self-critique the setup ([[concepts/ai-agents/context-engineering|context engineering]], [[concepts/ai-agents/self-improving-agent-workflows|self-improving workflows]]).
- **Keep the human as the decision-maker.** Position the agents as research/grunt-work and the human as author of "every single decision" — a concrete [[concepts/ux-research/human-in-the-loop|human-in-the-loop]] / [[concepts/ai-agents/ai-as-thinking-partner|thinking-partner]] division for [[concepts/product-management/domain-expert-as-builder|domain-expert builders]].

## Tensions

- **Anthropomorphism as a feature vs. a trap.** Human names boost legibility and steer the model usefully, but invite [[concepts/agent-experience/parasocial-relationship|parasocial]] over-trust in an n=1 setup with no persistence and acknowledged hallucination.
- **"Emergent collaboration" vs. controllability.** Unprogrammed inter-agent discussion is presented as delightful, but unspecified coordination is also unaudited coordination — at odds with [[concepts/ai-agents/multi-agent-coordination|deliberate orchestration]].
- **Simplicity vs. capability.** The lean markdown setup is its strength and its ceiling: it explicitly fails on data-heavy and large-document tasks.

## Open Questions

- What exactly is in the 106-line `CLAUDE.md` (verbatim structure of the five roles, the "seven lines" per persona)?
- How far does the markdown-only pattern scale before it needs real orchestration / persistence tooling?
- Is the persona-from-name effect model-specific (Claude Opus) or general across frontier models/harnesses?
- How does "be honest, not helpful" hold up — does the critic role stay critical, or drift back to agreeableness over a long session?

## Concepts Linked

- [[concepts/ai-agents/cowork|Claude Cowork]]
- [[concepts/ai-agents/1-person-vault|1-Person Vault]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]]
- [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]]
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
- [[concepts/ai-agents/context-engineering|Context Engineering]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]
- [[concepts/ai-agents/ai-as-thinking-partner|AI as Thinking Partner]]
- [[concepts/agent-experience/ai-sycophancy|AI Sycophancy]]
- [[concepts/agent-experience/parasocial-relationship|Parasocial Relationship]]
- [[concepts/agent-experience/relationship-architecture|Relationship Architecture]]
- [[concepts/agent-experience/mental-model-onboarding|Mental-Model Onboarding]]
- [[concepts/product-management/domain-expert-as-builder|Domain-Expert-as-Builder]]
- [[concepts/product-management/10-person-unicorn|10-Person Unicorn]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- Proposed new: [[concepts/ai-agents/markdown-agent-orchestration|Markdown Agent Orchestration]]
- Proposed new: [[concepts/ai-agents/persona-agent|Persona Agent (named-role agents)]]
- Related sources: [[sources/hai-cooperbench-agent-teamwork|CooperBench: Agent Teamwork]], [[sources/datarize-intelligence-to-autonomy|Datarize: Intelligence to Autonomy]]

## LLM Use

- **Use for:** illustrating the lowest-floor pattern for multi-agent orchestration (one markdown file + Claude Cowork, no code); persona/named-role agent design; the "be honest, not helpful" anti-sycophancy stance; the lean-context "simplify the setup" argument; a vivid solo-builder workflow narrative.
- **Do not use for:** any quantitative or generalizable claim about multi-agent productivity, "emergent collaboration," or scalability — it is an n=1 self-report and a book teaser; do not cite €/line/sample figures as benchmarks.
- **Best prompt pattern:** "Design a markdown-only multi-agent setup for a solo [creator/PM]: define 4–5 named persona roles in a single CLAUDE.md (≤7 lines each), one of them an honest 'reader/critic advocate', operated by plain conversation; keep context lean and let the model critique its own setup."

## Reliability Notes

> [!warning] Caveats
> Self-published practitioner narrative and promotion for the author's upcoming book CHORUS; sample of one, no measurement, no comparison. Captured full via web_fetch and cross-checked against the UX Collective republication, so the *content* is faithfully recorded (confidence 0.72 on the descriptive facts: the file, the five agents, the quotes). Confidence on the *causal/general* claims ("names beat specs," "collaboration emerges," "casual beats formal") is low — they are impressions, model- and task-specific.

## Backfill Status

- **Captured 2026-06-29:** full article text via web_fetch (note URL resolved to the article), cross-checked against the UX Collective republication; both raw and source pages written; slug renamed to `christinevallaure-human-approach-agentic-ai`.
- **To reach coverage: full** — obtain the verbatim 106-line `CLAUDE.md` and the exact per-role wording if the author publishes them; capture the CHORUS book material when released; pair with an independent multi-agent orchestration source for any generalization.
