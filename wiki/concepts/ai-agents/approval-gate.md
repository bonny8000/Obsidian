---
type: concept
status: active
created: 2026-07-24
updated: 2026-07-31
tags: [concept, ai-agent, human-in-the-loop, safety, automation, approval-gate, capability-boundary]
sources: [openworker-andrew-ng, socar-self-healing-agents, naver-d2-ai-hackathon-nstake, socar-parking-brain-knowledge-graph, karrot-kraft-design-system-agent]
confidence: 0.85
---

# Approval Gate

> [!abstract] Summary
> A structural halt placed immediately before any **irreversible** action — send, write, execute, deploy — requiring human confirmation to proceed. The gate is positioned by *reversibility*, not by the agent's confidence: a highly confident agent about to send an email still stops.

> [!important] Why it Matters
> Two sources in this cluster arrived at the same pattern from **opposite motives** — OpenWorker from privacy and user control, SOCAR from production reliability. Independent convergence from unrelated pressures is the strongest signal available that a pattern is load-bearing rather than stylistic.

## 📝 Key Claims

- **Gate on reversibility, not confidence.** The question is "can this be undone?", never "how sure is the model?"
- **Autonomy is asymmetric.** SOCAR's formulation: auto-recovery acceptable, auto-deployment unacceptable. Agents repair failures automatically but open **Draft PRs only**.
- **The escalation inbox** accumulates approvals from unattended runs, so the gate does not force synchronous babysitting — it batches the human interrupt rather than eliminating it.
- **Read-then-write adoption:** start agents on read-only tasks (organize, summarize), widen to write and send only once behavior is understood.
- **Declare the gate in the prompt** — "show me the draft before sending" — so it is explicit in the brief, not only in the harness.
- **Place the gate at the tool boundary, not in the prompt alone.** [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] requires explicit user confirmation before any state-changing operation (create / update / delete), enforced by the tool executor outside the model. Their post-incident principle is blunter still: **require explicit approval for destructive operations**, after reset code intended for local test data ran against the shared development database and took over 20 minutes to recover.
- **Gates also belong at knowledge ingestion, not only at action.** [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR's parking-brain]] routes confidence-scored extractions below threshold (e.g. 77% against an 85% minimum) to a **human approval queue** rather than ingesting them — the same gate applied to what the system comes to believe, not just what it does.
- **Strongest form yet: enforce the gate by removing the capability.** [[wiki/sources/karrot-kraft-design-system-agent|Kraft's]] Plan mode does not decline to write code — `runCodingAgent` is **deliberately absent from that mode's tool list**. *"코드를 만들 수 없는 모드"* — a mode that cannot produce code. This outranks "declare the gate in the prompt": a mode without the tool cannot be talked past, regardless of how the user phrases the request. On approval the same session transitions to the execution mode and **skips the already-completed steps**, so the gate costs the user one decision rather than a restart.
- **Independent convergence is now five sources deep**, from privacy (OpenWorker), production reliability (SOCAR agents), financial correctness (NStake), knowledge quality (parking-brain), and design-system compliance (Kraft). Five unrelated motives, same structural answer.

## ⚖️ Conflicts & Caveats

> [!warning] The rubber-stamp failure mode
> No source in this cluster tests the gate under fatigue. A gate that fires constantly trains the human to approve reflexively, at which point it provides the *appearance* of oversight while providing none. This is the single largest unexamined risk in the pattern — and it is a UX problem, not an engineering one.
>
> **This got worse, not better, with the 2026-07-28 cluster.** NStake adds a gate on *every* state change plus per-request authorization; parking-brain adds an approval queue for borderline knowledge extractions. More gates, still no source measuring what happens when they fire constantly.

> [!warning] Throughput tax
> Every gate is a human interrupt. At volume this is the same bottleneck Holbrook calls **"the tyranny of reviewing"** — generation capacity outruns review capacity, and the gate is where that mismatch becomes visible.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/human-in-the-loop|Human in the Loop]] — the parent pattern
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]] — the gate as one of six authorization boundaries
- [[wiki/concepts/ai-agents/rule-statistical-external-validation|Rule / Statistical / eXternal Validation]] — where external-class findings terminate
- [[wiki/concepts/infrastructure-dev/domain-knowledge-graph|Domain Knowledge Graph]] — the ingestion-side approval queue
- [[wiki/concepts/ai-agents/local-first-agents|Local-First Agents]]
- [[wiki/concepts/ai-agents/jagged-frontier|Jagged Frontier]] — why gates cannot be retired on good performance

## 📚 Sources

- [[wiki/sources/openworker-andrew-ng|AX LABS (2026): OpenWorker]]
- [[wiki/sources/socar-self-healing-agents|SOCAR (2026): AI Agents That Self-Repair Failures]]
- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): What the Winning AI Hackathon Team Did *Not* Delegate to AI]] — gate at the tool boundary; destructive-operation approval after a shared-DB incident.
- [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR (2026): parking-brain]] — approval queue for confidence-gated knowledge ingestion.
- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — the gate as a capability boundary: a mode with the code tool removed from its tool list.

## ❓ Open Questions

- At what approval frequency does review quality collapse into rubber-stamping?
- Should gate placement adapt to demonstrated reliability, or does adaptive gating just reintroduce confidence-based gating through the back door?
- Is there a design that makes the *cost* of an irreversible action legible at the moment of approval?
- Does gating by **capability removal** (Kraft) reduce rubber-stamping relative to gating by prompt declaration, or does it just move the reflexive click to the mode switch?
