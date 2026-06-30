---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [agentic-ai, multi-agent, claudemd, markdown-orchestration, solo-builder, natural-language, low-code]
sources:
  - sources/christinevallaure-human-approach-agentic-ai
confidence: 0.65
---

# Markdown Agent Orchestration

## Summary

Markdown agent orchestration is the lowest-floor pattern for running a multi-agent system: the entire "team" — roles, voice, and rules — is defined in a single plain-markdown file (e.g. a ~106-line `CLAUDE.md`), supported by a few on-demand folders read only when needed, and operated through natural conversation in a tool like Claude Cowork. There is no code, no orchestration framework, and no infrastructure. It is distinct from [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md context]] (which is the context *substrate*) and from [[concepts/ai-agents/orchestrator-of-agents|programmatic orchestration]] (which routes agents in code): here the markdown file *is* the orchestration.

## Why It Matters

It demonstrates that a non-coder can stand up and run a functioning multi-agent workflow with "the only skill you need being able to have a human conversation." That lowers the floor for agent adoption dramatically and is the natural starting harness for solo builders and [[concepts/ai-agents/1-person-vault|1-person vaults]]. It also surfaces a lean-context lesson: stripping an over-engineered setup (backstories, unnecessary file reads) measurably improved speed — an argument for [[concepts/ai-agents/context-engineering|lean context engineering]] over elaborate prompting.

## Key Claims

- A whole multi-agent system can fit in one ~106-line markdown file, editable in any text editor, with supporting folders read on demand ([[sources/christinevallaure-human-approach-agentic-ai|Vallaure, 2026]]).
- The only required skill is human conversation — no coding, framework, or infra; operated through [[concepts/ai-agents/cowork|Claude Cowork]].
- Inter-agent collaboration emerged unprogrammed: agents set up individually began coordinating, inferred from their role descriptions.
- Simplifying an over-specified setup (and letting the model self-critique it) improved speed — lean context beats elaborate prompting.
- The pattern is bounded: it is good for creative/editorial work but weak on heavy data and large documents, with no cross-day persistence.

## Related Concepts

- [[concepts/ai-agents/persona-agent|Persona Agent]] — named roles are the unit this pattern orchestrates.
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]] — the context substrate the file relies on.
- [[concepts/ai-agents/1-person-vault|1-Person Vault]] — the solo-operator setting this instantiates.
- [[concepts/ai-agents/cowork|Cowork]] — the operating environment.
- [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]] — emergent, unaudited version of it.
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]] — the programmatic contrast.
- [[concepts/ai-agents/context-engineering|Context Engineering]] · [[concepts/product-management/domain-expert-as-builder|Domain-Expert-as-Builder]]

## Conflicts & Caveats

> [!warning] n=1 narrative, model-specific
> The source is a single practitioner story and a book teaser (CHORUS), not research — no baseline, comparison, or measurement. "Emergent collaboration" is observed, not tested, and unprogrammed coordination is also *unaudited* coordination, at odds with deliberate orchestration. The persona-from-name and emergent-coordination effects may be specific to Claude Cowork / Claude Opus as of early 2026 and may not transfer.

## Sources

- [[sources/christinevallaure-human-approach-agentic-ai|Christine Vallaure (2026): A Human Approach to Agentic AI — One Person, One Text File, Five Agents]]

## Open Questions

- How far does the markdown-only pattern scale before it needs real orchestration / persistence tooling?
- Is the emergent-coordination effect model-specific or general across frontier models/harnesses?
