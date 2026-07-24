---
type: concept
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [concept, ai-agent, local-first, privacy, openworker, mcp-integration, automation]
sources: [openworker-andrew-ng]
confidence: 0.7
---

# Local-First Agents

> [!abstract] Summary
> An architectural posture in which **data, credentials, API keys and model inference all remain on the user's machine**. Only authentication signals (OAuth) cross the network boundary. The agent reaches into the user's real tools without the user's real data leaving the device.

> [!important] Why it Matters
> It removes a whole category of objection that otherwise blocks agent adoption in knowledge work — "I can't let this read my inbox." For research and design work touching participant data, consent-sensitive material or client confidences, the local-first posture is what makes tool-connected agents discussable at all.

## 📝 Key Claims

- **Only OAuth signals leave the device**; everything else — inference included — stays local.
- **Model-agnostic by design:** hosted providers (OpenAI, Anthropic, Gemini, DeepSeek) or fully local models via Ollama; users supply their own keys.
- **Bring-your-own-key changes the cost model:** the harness is free and open-source, but model usage bills directly to the user's provider account. "Free" describes the tool, not the running cost.
- **Pairs structurally with the [[wiki/concepts/ai-agents/approval-gate|approval gate]]** — local data handling plus a halt before irreversible action are the two commitments that make unattended operation defensible.
- Built on `aisuite` for multi-model abstraction and **MCP-standard** tool connectivity.

## ⚖️ Conflicts & Caveats

> [!warning] Privacy trades against capability
> On-device inference constrains model choice. The privacy posture and the quality ceiling pull in opposite directions, and no source in this cluster measures the gap between local Ollama models and hosted frontier models on these tasks.

> [!warning] Integration surface is a maintenance liability
> 25+ connected platforms means 25+ APIs that drift. Compare [[wiki/sources/socar-self-healing-agents|SOCAR's]] baseline-schema burden across 50 operators — the same problem, and they consider it unsolved.

> [!note] Vendor-adjacent source
> Confidence 0.7. The architecture is described specifically and plausibly, but every claim comes from a third-party guide with no independent evaluation and no adversarial testing.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
- [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]]
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]
- [[wiki/concepts/ux-research/human-in-the-loop|Human in the Loop]]

## 📚 Sources

- [[wiki/sources/openworker-andrew-ng|AX LABS (2026): OpenWorker — AI That Finishes Work, Not Just Chats]]

## ❓ Open Questions

- What is the real quality gap between local and hosted models on aggregation and drafting tasks?
- Does local-first survive team use, where the data being reasoned over is shared rather than personal?
- Is a 25+ integration surface maintainable by an open-source project as those APIs drift?
