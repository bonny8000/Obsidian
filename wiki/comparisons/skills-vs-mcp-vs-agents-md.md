---
type: comparison
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [agent-skills, mcp, agents-md, design-md, routing, context-engineering]
sources:
  - sources/agent-skills-day-3
  - sources/agent-tools-interoperability-day-2
  - sources/the-new-sdlc-with-vibe-coding-day-1
  - sources/atlassian-design-md
confidence: 0.88
---

# Comparison: Agent Skills vs MCP vs AGENTS.md vs DESIGN.md

## Decision Question

When I want to make an agent reliably good at X, do I write a **Skill**, expose an **MCP server**, extend **AGENTS.md / CLAUDE.md**, or ship a **DESIGN.md**?

## Criteria

- **What it teaches the agent** — know-how, reach, or always-on context.
- **When it loads** — every turn, on demand, or via external call.
- **Token cost shape** — static, dynamic, or out-of-process.
- **Who owns it** — domain expert, infra/integrations team, or project lead.
- **Right when…** — workflow-specific, system-access, or project-wide.
- **Wrong when…** — boundary mis-applications.

## Matrix

| Primitive | What it teaches | When it loads | Token cost shape | Who owns it | Right when… | Wrong when… |
| --- | --- | --- | --- | --- | --- | --- |
| **Agent Skill** ([[concepts/ai-agents/agent-skills|↗]]) | *Know-how* — a procedure for a narrow class of work | On demand, when the description matches; body loads only on trigger | Dynamic — small metadata cost always; body + resources only when used | Domain expert / team that owns the workflow | The work is narrow, action-specific, repeatable, and has strong activation cues | Used as a dumping ground for global rules ("always do X") or for facts that belong in RAG / references |
| **MCP Server** ([[concepts/ai-agents/mcp-integration|↗]]) | *Reach* — a standardized way to call an external system (Drive, Salesforce, BigQuery, internal API) | When the agent invokes a tool | Per-call cost (request/response); negligible static cost | Infra / integrations team owning the external system | The agent needs to read or mutate state in a system the model can't reach itself | Used to encode workflow logic (that belongs in a Skill) or business rules (that belong in references / docs) |
| **AGENTS.md / CLAUDE.md** ([[concepts/infrastructure-dev/claudemd-context|↗]]) | *Project-wide always-on context* — conventions, stack, build/test commands, file layout | Always loaded for the project | Static — every turn pays the full cost | Project / repo lead | Information must be present on every turn (project conventions, repo map, "use pnpm not npm", a Skills catalog) | Used for action-specific workflows or long detailed procedures — those should be Skills |
| **DESIGN.md** ([[concepts/infrastructure-dev/design-md|↗]]) | *Portable design intent* — design tokens + rationale for color, spacing, layout, elevation, components | Always loaded when attached to the prompt | Static and large — Atlassian's ADS file is ~80 KB (~19,800 tokens) every turn | Design-system team (or customer, in white-label scenarios) | One-shot prototyping without MCP, cross-tool interoperability, customer theming for adaptive UIs, high-level artistic-direction documentation | Production codebase with an existing component library — Atlassian found agents re-implement components instead of importing them; ~92% more tokens, ~2.7× variance vs ADS MCP |

## Recommendation Pattern

- **Default to AGENTS.md for project context.** Keep it tight: conventions, stack, build commands, a short Skills catalog. Vercel's analysis: a passive AGENTS.md index achieved 100% pass rate against a 53% baseline — global context belongs in always-on documentation.
- **Default to a Skill for repeatable workflows.** One job, one folder, a description with 3 positive + 3 negative triggers, an eval suite, a Read/Draft/Act tier. A poorly-designed Skill *subtracts* capability (Vercel: −5pp); the discipline is in the description and the evals.
- **Default to an MCP server for external reach.** If the agent needs to talk to a system it cannot reach via the local filesystem or model API, that's an MCP. A Skill that *needs data* should call a tool typically provided by an MCP server.
- **Default to DESIGN.md for portable brand context.** When the consumer is a one-shot tool (Figma Make, V0), a different team's environment, or a customer who wants their own brand respected by AI-generated UI. Inside a production codebase with a real component library, prefer MCP + Skills + lint rules — Atlassian found DESIGN.md alone burns ~92% more tokens *and* steers agents toward re-implementing components instead of importing them.
- **Compose, don't compete.** A real workflow often uses several at once: AGENTS.md tells the agent "we ship Stripe-billed SaaS, here's the repo map"; the `refund-handling` Skill knows the policy and trajectory; the Stripe MCP server makes the actual API calls; a slim DESIGN.md guarantees marketing emails generated for customer A use customer A's brand kit.

## One-line mental model (from Day-3 Appendix A)

> System prompt = instinct. AGENTS.md = project README. Tools / MCP = hands. RAG = library. **Skills = the runbook the experienced colleague hands you on day one, and that the AI never forgets.**

## Routing heuristics

- If you cannot describe the thing as a *workflow*, it is not a Skill.
- If it must be in front of the model *every turn*, it is AGENTS.md.
- If it accesses *external state* the model can't reach, you need an MCP (the Skill can call it).
- If a Skill description starts with "always…" or "never…", it probably belongs in AGENTS.md.
- If AGENTS.md starts containing "when the user asks X, do Y, Z", those steps probably belong in a Skill.
- If the consumer is a *one-shot UI tool* or a *customer in a different environment*, ship a DESIGN.md instead of (or alongside) an MCP.
- If your agent *re-implements* an existing component instead of importing it, your design context is a DESIGN.md where it should be an MCP/Skill anchored on the actual component library.
- If your agent *reads component implementations* to recover usage guidance, your DESIGN.md is missing something the agent needs — fix the file or move that knowledge into an MCP/Skill.

## Source Evidence

- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — Section 2 (Skill vs MCP, Skill vs AGENTS.md) and Appendix A (one-line mental model).
- [[sources/agent-tools-interoperability-day-2|Patlolla et al. (2026): Agent Tools & Interoperability (Day 2)]] — MCP and the broader interoperability stack (A2A, A2UI, AP2, UCP).
- [[sources/the-new-sdlc-with-vibe-coding-day-1|Osmani et al. (2026): The New SDLC With Vibe Coding (Day 1)]] — static vs dynamic context framing.
- [[sources/atlassian-design-md|Hall & Campbell (2026): Atlassian's DESIGN.md is here]] — production comparison of DESIGN.md vs ADS MCP vs ADS skill vs no context on a log-in-screen task; "re-implementation vs importation" framing.
- Vercel production analysis: `vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` (cited via Day-3).
