---
type: source
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [design-system, llm-safe-design-system, agentic-engineering, harness, design-tokens, eval, agent-memory, skills, claude-agent-sdk, mastra, case-study, karrot, korea]
source_path: raw/web/daangn-kraft-design-system-agent-2026-07-31.md
source_url: https://medium.com/daangn/%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%ED%99%94%EB%A9%B4%EC%9D%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EC%8B%9C%EB%8C%80-%EB%8B%B9%EA%B7%BC%EC%8A%A4%EB%9F%AC%EC%9A%B4-%ED%99%94%EB%A9%B4%EC%9D%84-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B2%95-0bc268f819c7
authors: [SeieunYoo]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Karrot (2026): Kraft — Automating the Decisions a Design System Demands

## Citation

SeieunYoo, 「프롬프트 한 줄로 화면이 나오는 시대, '당근스러운 화면'을 만드는 법」 *(In the era where one prompt line produces a screen: how to make a 'Karrot-like' screen)*, **당근 기술 블로그 (Karrot Tech Blog)**, Medium, 2026-04-30. 26 min read.

**Source type:** First-party engineering case study by a frontend engineer on Karrot's design system team, describing an internal tool through three architectural generations.
**Raw capture:** [[raw/web/daangn-kraft-design-system-agent-2026-07-31|daangn-kraft-design-system-agent-2026-07-31]]
**Coverage note:** `coverage: full` — the complete article was rendered in-browser (Medium blocks server-side fetch) and read end-to-end, including the architecture diagram, the DesignSpec JSON sample, the skill table, and the scorer lists. Nothing was skimmed. This does **not** mean Kraft's source or the SEED system itself was inspected.

## Summary

Karrot's design system team wanted screens generated from prompts that were actually shippable in the Karrot app. They tried Lovable/v0/Bolt and Figma Make, found both structurally unable to produce SEED-compliant code, and concluded the problem had been misstated. The reframing is the source's core contribution:

> "'AI로 화면을 그리게 할 것인가?'가 아니라 '어떤 결정을 AI에게 맡길 것인가?'였어요."
> *"The question was not 'shall we have AI draw the screen?' but 'which decisions do we delegate to AI?'"*

The resulting tool, **Kraft**, went through three forms — **admin → CLI → agent** — and each transition is documented with the specific wall that forced it. That progression, with its failures named, is what makes this an unusually good source: it is a record of three hypotheses being falsified in order.

It is also the vault's **second independent arrival** at [[wiki/concepts/infrastructure-dev/llm-safe-design-system|constraining the acceptance criteria rather than the generator]], after [[wiki/sources/polar-orbit-llm-safe-design-system|Polar Orbit]] — and it extends that idea in two directions Polar Orbit did not: the constraint is made **machine-scored** (11 scorers) and **cumulative** (cross-session memory that promotes repeated decisions into principles).

## Key Claims

- **The unit of automation is the decision, not the pixel.** A design system is dozens of decisions per screen — component choice, token application, layout structure, copy tone, state handling. *"결국 핵심은 픽셀을 그리는 게 아니라, 디자인 시스템이 요구하는 결정들을 자동화하는 것"* — the core is automating the decisions the design system demands, not drawing pixels. Recorded on [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] and [[wiki/concepts/infrastructure-dev/design-automation|Design Automation]].

- **Generic vibe-coding tools fail on three structural grounds, not on quality.** They build with their own component sets (shadcn/ui, Tailwind), so output is `<Button>` rather than SEED's `ActionButton`; they cannot be told that `@karrotmarket/icon` or the SEED token scale exists; and their output is one-shot, with no path to propagate a later design-system change into already-generated screens. Figma Make fails differently — output is Figma layers, so the developer bottleneck the project set out to remove survives intact, and templates do not sync back to projects built from them.

- **A general-purpose agent cannot carry domain context.** The admin version served every team the same agent: *"중고거래팀이 쓸 때랑 부동산팀이 쓸 때, 같은 결과가 나와요"* — the used-goods team and the real-estate team get the same result. Being web-based, it could not reach the user's project folder, policy docs, or conventions. Moving to a CLI was specifically a move to **acquire context**, not to acquire developer ergonomics.

- **Prompt → code is the wrong wiring, because design systems are mostly tacit.** Rules like "padding inside a card must be at least `x4`" and "no more than 4 type steps on one screen" are never stated by users in prompts. The agent has to already hold them. The stated structural answer is a **DesignSpec intermediate representation** plus a **skill system** — see [[wiki/concepts/ai-agents/design-spec-intermediate-representation|Design Spec as Intermediate Representation]].

- **Generation without verification is worthless, and inconsistency is what destroys trust.** Making a plausible screen is easy; making a compliant one is not. The same prompt twice produced different screens — one using SEED tokens, the next hardcoding hex; one handling error states, the next only the happy path. *"두 번째로 생성한 화면이 첫 번째와 전혀 다른 스타일이면, 도구로서의 신뢰가 깨져요."* The 11-scorer eval exists so the machine filters before a human reviews. See [[wiki/concepts/ai-agents/generated-output-scoring|Generated-Output Scoring]].

- **Multi-agent was tried and abandoned.** The team first designed separate design/coding/conductor agents collaborating freely. In practice, **inter-agent communication overhead was large and context was lost in transfer** — subtle nuance dropped when the design agent's decided intent was handed to the coding agent. They replaced it with a **harness holding two modes plus external delegation**. This is a rare recorded negative result on multi-agent architecture from a production team; see [[wiki/concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]].

- **Delegate the solved part outward, keep the contextual part inward.** Design and decision-making live in a Mastra harness; code-writing is delegated to **Claude Code via `@anthropic-ai/claude-agent-sdk`**, spawning the local `claude` binary with only `Edit/Write/Read/Bash/Glob/Grep` plus a SEED-docs MCP whitelisted. Described as *"Claude Code를 도구처럼 임베드하는 어댑터"* — an adapter that embeds Claude Code as a tool. The stated benefit: control the design context yourself, borrow the mature tool ecosystem for the rest.

- **Ambiguity must produce a question, never a guess and never a refusal.** Of the four intents the Orchestra mode routes, the one the author calls the core is #4: an ambiguous request must go to `ask_user` to establish intent before proceeding.

- **Approval is enforced by tool-list exclusion, not by instruction.** Plan mode does not merely decline to write code — `runCodingAgent` is deliberately absent from its tool list. *"코드를 만들 수 없는 모드"* — a mode that cannot produce code. This is [[wiki/concepts/ai-agents/approval-gate|approval-gate]] implemented as a capability boundary rather than a prompt rule, matching [[wiki/concepts/ai-agents/permission-boundary-guardrails|permission-boundary guardrails]].

- **Corrections must outlive the session or they are the human's job, not the tool's.** Telling the CLI "in used-goods, always use `brandSolid` for CTAs" held for that session and vanished. The fix accumulates `designDecisions` into `.design-memory/decision-log.jsonl`, auto-promotes patterns repeating **above a threshold** into per-domain principles in `.design-memory/principles.json`, and reads them back at the next session's Memory Read step. See [[wiki/concepts/ai-agents/agent-memory|Agent Memory]].

## Useful Examples

**The agent loop:** Clarify → Memory Read → Cases → Generate → Verify → Memory Write. Each step maps to a failure observed in the CLI generation: vague prompts, erratic quality, lost corrections.

**The two modes:**

| Mode | Does | `runCodingAgent` | Use when |
|---|---|---|---|
| **Plan** (review) | sharpens intent, saves DesignSpec, `ask_user` → stops | **excluded from tool list** | agree structure/components first; break before expensive work |
| **Orchestra** (execution, default) | intent → spec → verify → code → spec update, end-to-end | available | quick screens; simple edits needing no agreement |

Arriving in Orchestra via Plan approval **skips Clarify and Cases** and resumes at verification.

**The DesignSpec JSON** — fields observed: `title`, `screenType`, `serviceDomain`, `structure` (description + component `tree`), `components` (with `importFrom: "@seed-design/react"` and `props`), `designTokens` (`colors` / `typography` / `spacing`), and `designDecisions` (topic / decision / rationale). The rationale field is what makes the intermediate representation earn its place: *"코드만 보면 알 수 없는 맥락이 남아요"* — context invisible from code alone survives.

The sample records the star-rating decision as: tap five star icons, chosen because *"슬라이더보다 직관적이고, 모바일에서 오탭 가능성이 낮음"* — more intuitive than a slider, lower mis-tap probability on mobile.

**Semantic-token enforcement by schema:** `designTokens` accepts only names like `bg.layerDefault`, never `#FF6F0F`. The author's claim — *"이것만으로도 '당근스러운 색상'이 자동으로 보장돼요"* — is that this alone guarantees brand-correct color. This is the same move as Polar Orbit's typed tokens, executed one layer up, in the spec rather than the type system.

**The seven skills** (markdown modules, lazily loaded):

| Skill | Governs | Example rule |
|---|---|---|
| `spacing-constraint` | x0.5–x16 tokens | card inner padding ≥ x4; list-item gap x3 |
| `radius-constraint` | r0.5–rFull | buttons rFull, cards r3, inputs r2 |
| `typography-constraint` | t1–t10 | ≤ 4 type steps per screen |
| `screen-patterns` | layout rules | 8 patterns for form-screen error display |
| `small-writing-guide` | UI copy | CTA starts with a verb, ≤ 12 characters |
| `design-principles` | SEED's 7 principles | connected experience, improvement for users, intuitive experience… |
| `eval-self-check` | post-write check | 7 areas: color token / component / spacing / typography / icon / layout / animation |

Lazy-loading example given: a review form loads `screen-patterns` and `spacing-constraint`; `small-writing-guide` loads only once copy is being decided. Claimed benefit — a design-system rule change edits one skill file, never the system prompt.

**The 11 scorers, split by determinism:**

| Code-based (7) — deterministic, fast | LLM-based (4) — qualitative |
|---|---|
| `color-tokens` (semantic vs. hardcoded hex) | `ux-patterns` (pattern fits screen type) |
| `typography` (logical size steps) | `interaction-quality` (flow feels natural) |
| `layout-structure` (VStack/HStack/Flex vs. SEED patterns) | `flow-patterns` (inter-screen flow matches intent) |
| `spacing-rules` (context-appropriate tokens) | `form-patterns` (error/loading/empty handled) |
| `component-compliance` (correct props) | |
| `icon-usage` | |
| `animation-stability` | |

The split is the reusable idea: **check mechanically whatever can be checked mechanically, and spend model calls only on judgment.**

**Self-correction budget:** `validateDesignSpec` failures trigger at most **2** self-corrections before re-verification — a bounded repair loop rather than an open one.

## Constraints / Caveats

- **Zero quantitative outcomes.** This is the source's single largest weakness. No adoption count, no before/after cycle-time measurement, no eval-score distribution, no defect rate, no rework rate. The "days to weeks" baseline and "idea to screen in 10 seconds" are stated, never measured. A tool whose entire justification is consistency reports no consistency metric.
- **No cost side.** Seven skill files, eleven scorers (four of them LLM calls), a memory store, and a harness all carry standing maintenance. Neither build cost nor running cost nor break-even volume is given.
- **Early stage.** The article describes an internal announcement and the inquiries that followed — not an org-wide rollout with results.
- **First-party, by the builder,** on the company engineering blog. No independent evaluation and no dissenting internal view is recorded.
- **The multi-agent rejection is qualitative.** "Communication overhead" and "context loss" are asserted without measurement, configuration detail, or the model/framework used in the failed attempt. Useful as a directional signal; not as evidence about multi-agent architectures in general.
- **The principle-promotion threshold is unspecified**, which is exactly the parameter that decides whether the memory system generalizes usefully or ossifies one team's habits.
- **Article is 2026-04-30**, captured three months later; the "next problems" list may have moved.

## Design Implications

- If a generator must produce house-style output, **put the house style in a schema the generator fills, not in a prompt it reads.** The DesignSpec makes semantic tokens the only representable option; compliance stops depending on the model remembering.
- **Separate the deterministic checks from the judgment checks explicitly** and staff them differently. Seven of Karrot's eleven checks need no model at all.
- **Enforce approval by removing the capability,** not by instructing restraint. A mode without the code tool cannot write code regardless of what the prompt says or how the user phrases the request.
- **Make ambiguity route to a question.** Karrot treats "guess" and "refuse" as equally wrong; both destroy the interaction. This is a concrete, implementable stance on a problem [[wiki/concepts/agent-experience/initiative-and-interruption|initiative and interruption]] raises abstractly.
- **Budget the self-repair loop.** Two attempts, then escalate — an unbounded retry loop on a failing validator burns tokens and hides the failure.
- **Tools should join the workflow rather than replace it:** *"도구는 워크플로우를 바꾸려 하기보다, 워크플로우에 스며들어야 한다"* — converges with [[wiki/sources/pxd-writone-ai-writing-assistant|Writone's]] Figma-plugin decision from an entirely different problem domain. See [[wiki/concepts/infrastructure-dev/in-workflow-ai-placement|In-Workflow AI Placement]].

## Tensions

- **Against generic AI-UI tooling's premise.** Lovable/v0/Bolt/Figma Make are not described as low-quality — they are described as *structurally* unable to hold institutional context. If that is right, the entire category is a prototyping instrument rather than a production one, which is a stronger claim than the article makes explicitly.
- **Against [[wiki/sources/designer-builder-collapse|the designer-builder thesis]].** That source treats fast generated prototypes as the win and the design act as review. Karrot agrees the design act becomes review — but only after building a spec layer, a skill system, a scorer suite, and a memory store first. The optimism about "AI collapses the boundary" survives; the implied cheapness does not.
- **With [[wiki/concepts/ai-agents/multi-agent-architecture|multi-agent architecture]].** That page's guidance ("start single-agent; graduate only at clear limits") is supported here by a team that graduated early and reverted.
- **Corroborates [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] on workflow completeness** — Karrot's "multi-canvas view" gap is the same observation from the other direction: practitioners work in flows, and a tool that produces one correct screen at a time still leaves the flow-level judgment unautomated.
- **Unresolved against [[wiki/concepts/ai-agents/context-rot|context rot]]:** Kraft's answer to too-much-context is lazy skill loading, while its answer to too-little-context is accumulating memory. The article does not say what happens when accumulated principles grow large enough to become noise themselves.

## Open Questions

- What is the principle-promotion threshold, and what stops a wrong early decision from being promoted into a domain principle and then propagating to every later user?
- What do the 11 scorers actually score in practice? A distribution would convert this from an architecture description into evidence.
- Does the DesignSpec layer pay for itself, or does it become a second artifact to keep in sync with the code it generates? `reverseDesignFromCode` exists, which suggests drift was already anticipated.
- Is the multi-agent failure a property of multi-agent architectures, of Mastra, or of this team's first attempt at one?
- Karrot and Polar Orbit converged on the same principle from different layers (spec schema vs. type system + CI). Is there a reason to prefer one, or do mature systems need both? Recorded in [[wiki/comparisons/where-to-put-the-constraint|Where to Put the Constraint]].

## Concepts Linked from This Source

- [[wiki/concepts/ai-agents/design-spec-intermediate-representation|Design Spec as Intermediate Representation]] *(new)*
- [[wiki/concepts/ai-agents/generated-output-scoring|Generated-Output Scoring]] *(new)*
- [[wiki/concepts/infrastructure-dev/in-workflow-ai-placement|In-Workflow AI Placement]] *(new)*
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] *(second instance)*
- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[wiki/concepts/infrastructure-dev/design-automation|Design Automation]]
- [[wiki/concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[wiki/concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]]
- [[wiki/concepts/ai-agents/agent-memory|Agent Memory]]
- [[wiki/concepts/ai-agents/skill-system|Skill System]]
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]]
- [[wiki/concepts/agent-experience/designing-generative-systems|Designing Generative Systems]]
- [[wiki/concepts/ai-agents/claude-code|Claude Code]]

## LLM Use Guidance

- **Strong grounding** for questions about architecting a design-system-aware generation tool: the tool inventory, mode split, spec schema, skill decomposition, and scorer taxonomy are all concretely specified and directly reusable.
- **Do not cite this source for efficacy.** It reports no outcome measurement of any kind. Any claim that this architecture *works better* is unsupported here — cite it for design, not for results.
- Use the three-generation progression (admin → CLI → agent) when a reader asks why a local/contextual tool beats a hosted one: the reason given is context access, not developer preference.
- The multi-agent negative result is worth surfacing whenever multi-agent designs are proposed, **flagged as one team's qualitative experience.**

## Reliability Notes

- **Confidence 0.80.** The architectural facts are high-confidence — they are specific, internally consistent, named down to file paths and tool names, and would be costly to fabricate. The score is capped by the complete absence of outcome data, first-party authorship with no independent check, early deployment stage, and the qualitative-only basis for the multi-agent rejection.
- Read end-to-end in-browser; `coverage: full` is honest for the article. Medium's server-side block means the raw capture is a browser-rendered extraction, not an API retrieval.
- **Fifth Korean-industry engineering source in the constraint cluster**, alongside [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]], [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR]], [[wiki/sources/polar-orbit-llm-safe-design-system|Polar Orbit]], and [[wiki/sources/pxd-writone-ai-writing-assistant|pxd Writone]]. The cluster's consistency is a genuine signal; its shared blind spot — **none of them measures anything** — is now a pattern rather than a coincidence, and is the load-bearing finding of [[wiki/analyses/2026-07-31-constraint-architectures-converge|the batch analysis]].
- **Highest-value verification step:** any published eval-score distribution, adoption figure, or cycle-time comparison from Karrot would move several claims here from 0.80 toward 0.9.
