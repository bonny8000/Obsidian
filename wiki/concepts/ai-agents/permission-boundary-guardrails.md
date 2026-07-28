---
type: concept
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [concept, ai-agent, guardrails, authorization, zero-trust, mcp, audit-log, human-in-the-loop, safety]
sources: [naver-d2-ai-hackathon-nstake, socar-self-healing-agents]
confidence: 0.84
---

# Permission-Boundary Guardrails

> [!abstract] Summary
> Guardrails placed at the **authorization layer before the model**, not as a filter on its output. The agent is provisioned only the data the current user may see and only the tools that user may run — decided outside the model, re-checked on every request. Letting an agent read everything and then masking part of the final answer is not a boundary; it is a redaction with a full copy behind it.

> [!important] Why it Matters
> "Guardrails" for a data-handling agent are usually imagined as filters on dangerous questions or inappropriate answers. [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] found the real risk elsewhere: not what the model *says*, but what it can *reach* and *execute*. Their strongest evidence is an incident — reset code written for local test data ran against the **shared development database**, taking **over 20 minutes** to recover out of a six-hour event. The model did nothing wrong; it wrote code for the environment it was told about. The environment changed, and the tooling had more privilege than it needed.

## The core claim

> A safety policy does not end with writing *"don't show unauthorized data"* in the prompt. Rather than hoping the model follows rules, the authentication/authorization layer and the tool executor **outside** the model must structurally block disallowed actions.

This is the same principle as [[wiki/sources/socar-self-healing-agents|SOCAR's]] "hallucination is a code problem, not a prompt problem" — extended from *output validation* to *access provisioning*. If a safeguard depends on the model behaving, it is not a safeguard.

## 📝 Key Claims

- **Scope context at authorization time, not answer time.** The model receives only the entities the logged-in user may see, from the first token.
- **Re-verify per request, in the source of truth.** Trust neither the token nor the model's judgment: re-check the user's role and entity scope **in the database on every request**.
- **Separate tool classes by policy.** Read, LLM-query, write, and admin functions get different policies — not one "the agent has tools" permission.
- **Short-lived, minimal-identity tokens.** After SSO, issue a separate short-lived token for AI/MCP carrying minimal identifying information.
- **Explicit confirmation before state change.** Create / update / delete require user confirmation before execution — the [[wiki/concepts/ai-agents/approval-gate|approval gate]], placed at the tool boundary.
- **Append-only audit log.** Who read, created, updated, or deleted what, and when. Non-negotiable and non-editable.
- **Information protection at the edges too:** sensitive-data masking, input length limits, and no credentials in logs or error messages.
- **Privilege and execution control outrank hallucination as a practical risk** wherever an agent can access real systems and run code.

## The six boundaries

| Boundary | Principle |
|---|---|
| Authentication | Short-lived AI/MCP token after SSO, minimal identity |
| Data authorization | Re-check role and entity scope in the DB on **every** request |
| Tool authorization | Distinct policies for read / LLM-query / write / admin |
| Change approval | Explicit user confirmation before any state change |
| Information protection | Masking, input limits, no credentials in logs or errors |
| Traceability | Append-only audit log of all reads and mutations |

## Environment-separation principles

Derived from the shared-database incident, and the part most likely to be skipped in a prototype:

- **No admin privileges by default** for AI tooling.
- **Clearly separate local / dev / production** environments.
- **Re-confirm the target environment** before deletion or large-scale change.
- **Require explicit approval for destructive operations.**
- **Confirm backup and recoverability before feature development**, not after.
- **Verify AI-generated code by actual execution results, not by its explanation.**

## ⚖️ Conflicts & Caveats

> [!warning] Per-request DB authorization has a cost
> Re-checking role and scope on every request is the strongest form of the pattern and the most expensive. Neither anchor source reports the latency or load impact, and neither discusses caching strategies that would weaken the guarantee.

> [!warning] Evidence is a prototype plus a production analogue
> The six boundaries come from a **six-hour hackathon prototype**, and the authors are explicit that production-grade MCP authentication remains unbuilt. The general principle is corroborated by SOCAR's production credential isolation, but this specific boundary set has not run in production.

> [!warning] The rubber-stamp problem is inherited
> Change approval is an [[wiki/concepts/ai-agents/approval-gate|approval gate]], and it carries that concept's largest unexamined risk: a gate that fires constantly trains reflexive approval. Placing gates on every state change maximizes both safety and fatigue, and no source tests the trade-off.

> [!warning] Says nothing about who authorizes the agent itself
> These boundaries derive the agent's permissions from the logged-in user. They do not address an agent acting autonomously, on a schedule, or on behalf of many users — where "the current user's scope" has no referent. See [[wiki/concepts/ai-agents/agent-identity|Agent Identity]].

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]] — the parent security posture.
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]] — layered defense; this concept is the *access* layer specifically.
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] — the change-approval boundary, and the source of the fatigue caveat.
- [[wiki/concepts/ai-agents/agent-authorization|Agent Authorization]]
- [[wiki/concepts/ai-agents/agent-identity|Agent Identity]] — the unresolved question of autonomous-agent scope.
- [[wiki/concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]] — where tool-class policies are enforced in practice.
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] — the same structural-over-instructed logic in the front-end layer.
- [[wiki/concepts/ai-agents/membership-inference-attack|Membership Inference Attack]] — the complement: constraining what a model *is*, not what it can reach.
- [[wiki/concepts/ux-research/human-in-the-loop|Human in the Loop]]

## 📚 Sources

- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): What the Winning AI Hackathon Team Did *Not* Delegate to AI]] — primary source: the six boundaries, the shared-DB incident, the environment-separation principles.
- [[wiki/sources/socar-self-healing-agents|SOCAR (2026): AI Agents That Self-Repair Failures]] — production corroboration: credential isolation via closure so passwords never enter prompts or logs; retry blocked for write operations.

## ❓ Open Questions

- What is the latency and load cost of per-request DB authorization at scale, and what caching preserves the guarantee?
- How should permissions be scoped for an agent that runs unattended or acts across many users' data?
- Where should approval gates be placed to stay effective without inducing reflexive approval? Unanswered across this entire cluster.
- What is the base rate of destructive-execution incidents in normal agentic development? Four experienced engineers hit one in six hours.
- Does an append-only audit log of agent actions actually get read, and by whom?
