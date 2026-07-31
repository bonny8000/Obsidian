---
source_url: https://medium.com/daangn/%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%ED%99%94%EB%A9%B4%EC%9D%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EC%8B%9C%EB%8C%80-%EB%8B%B9%EA%B7%BC%EC%8A%A4%EB%9F%AC%EC%9A%B4-%ED%99%94%EB%A9%B4%EC%9D%84-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B2%95-0bc268f819c7
captured: 2026-07-31
title: "프롬프트 한 줄로 화면이 나오는 시대, '당근스러운 화면'을 만드는 법"
title_en: "In the era where one prompt line produces a screen: how to make a 'Karrot-like' screen"
authors: [SeieunYoo]
published: 2026-04-30
publisher: 당근 기술 블로그 (Karrot Tech Blog, Medium)
language: ko
format: engineering case study
reading_time: 26 min
capture_method: rendered in-browser (Medium blocks server-side fetch); read end-to-end
---

# In the Era Where One Prompt Produces a Screen — Karrot Tech Blog

**Author:** SeieunYoo (self-introduced as "조이" / Joy), frontend engineer on **당근's design system team**.
**Published:** 2026-04-30 · **Captured:** 2026-07-31 · **Length:** 26 min read

AI-written extraction. No full-text reproduction; short quoted phrases only.

---

## Thesis

From the perspective of a team operating a design system, "a plausible screen" and "a screen that looks like our product" are entirely different problems. Karrot has a design system called **SEED** — components, tokens, layout rules, copy guidelines — such that building one screen involves dozens of decisions that must be respected. The conclusion drawn:

> "결국 핵심은 픽셀을 그리는 게 아니라, 디자인 시스템이 요구하는 결정들을 자동화하는 것이었어요."
> *"The core turned out to be not drawing pixels, but automating the decisions the design system demands."*

And the reframing that drove the project:

> "'AI로 화면을 그리게 할 것인가?'가 아니라 '어떤 결정을 AI에게 맡길 것인가?'였어요."
> *"The question was not 'shall we have AI draw the screen?' but 'which decisions do we delegate to AI?'"*

## Background

Normal flow at Karrot: planner writes requirements → designer draws in Figma → developer ports to code. Days at minimum, weeks at worst. Screen-building itself became the bottleneck for fast idea validation, so the team leaned on vibe-coding tools.

## What existing tools could not solve

**Lovable / v0 / Bolt (vibe-coding tools)** — reported as genuinely fast and low-barrier, but:

- **Cannot use SEED components.** These tools build with their own components (shadcn/ui, Tailwind-based). Output is generic `<Button>`, `<Modal>` rather than SEED's `ActionButton`, `AppBar`, `BottomSheet` — so however pretty, it cannot be dropped into the Karrot app.
- **Cannot inject package context.** Karrot has its own icon package (`@karrotmarket/icon`); color/spacing/radius are managed as SEED tokens. External tools do not know these packages exist.
- **Output is one-shot.** Once generated, done. If the design system updates or a component API changes, there is no way to propagate that into already-generated screens.

**Figma Make (Figma AI)**:

- **Trapped in the Figma canvas.** Output is Figma layers — a design file, not code. A developer still has to port it, so the original "developer bottleneck" problem remains intact.
- **Hard to inject context beyond components.** A SEED component library can be connected to Figma, but "code-level knowledge" — the icon package, context-specific spacing-token rules, form patterns — is difficult to inject.
- **No template sync.** Build a template in Figma, use it across projects, then update the original — the change does not reach projects already built from it. Each must be updated manually.

## Kraft: three forms

Kraft is described as a **decision-automation tool** for producing SEED-based screens from a prompt, not merely "AI draws a screen." It evolved through three forms, each setting a different scope of "user" and "extensibility."

### 1. Admin (web editor/dashboard)

Flow: prompt → preview → deploy → check in webview (QR / deep-link scheme). Initial hypothesis: "give a prompt to an AI that knows SEED components and a usable screen will come out."

Strengths: no install, open a URL; easy sharing by QR/deep-link; the whole chain in one place; designer/PM/engineer alike could go "from idea to screen in 10 seconds."

**Wall hit:**

> "중고거래팀이 쓸 때랑 부동산팀이 쓸 때, 같은 결과가 나와요."
> *"When the used-goods team uses it and when the real-estate team uses it, the same result comes out."*

Admin served every user the same agent. Being web-based, it could not reach the user's local environment (project folder, existing code), so there was no way to inject a domain's policies or its particular screen patterns. Described as the innate limit of a general-purpose tool.

Meanwhile Claude Code and similar AI coding tools were spreading across job functions — PMs and designers running local AI tooling stopped being unusual — which undermined the admin's premise that web access was the accessibility win.

### 2. CLI (local, session-based)

`kraft` one-liner brings up a local editor with the agent alongside. The package bundles editor frontend + agent backend together so `npx` starts the whole environment; build-time bundling includes editor static files, agent server code, design skill files, and prompt templates.

What changed most was **context injection**: the agent can read the local project folder — existing screen code, per-domain policy documents, team convention files. Work separates per project/session, so "the used-goods team's screens" and "the real-estate team's screens" can naturally diverge. Entry points widened: blank screen, template, Figma URL, existing-code ZIP.

**Walls hit:**

- **"프롬프트를 잘 써야 좋은 결과가 나와요."** — *"You have to write a good prompt to get a good result."* Asked only for "make a trade-review screen," the agent must decide much on its own: what UI shows the star rating, how error states are handled, when the CTA activates. Without answers it just builds something "plausible."
- **Quality was erratic.** The same prompt twice gave different screens — first run uses SEED tokens, second hardcodes hex; first handles error states, second implements only the happy path. This raises "can I trust this tool?"
- **Corrections did not survive the session.** Telling it "in used-goods, always make the CTA `brandSolid`" applied within that session; a new session started from blank. Repeating the same correction every time is work for a person, not a tool.

The common thread: **there was nothing before or after generation** — no requirement-sharpening before, no quality verification after, no learning across sessions. Only a single jump from prompt to code.

### 3. Agent (the loop)

Structured loop: **Clarify → Memory Read → Cases → Generate → Verify → Memory Write**.

- **Clarify** — the agent asks back first: "How should the error state show on this screen?", "Is star-rating input tap-based or slide-based?" Rather than the user writing a better prompt, the agent fills the missing decisions.
- **Verify** — automatically scores SEED-guideline compliance, token-usage accuracy, required-state handling. The machine filters before a human reviews.
- **Memory** — previous decisions and corrections are referenced automatically; "last time in this domain we decided this way" carries into the next session.

## Agent architecture

### Harness pattern + external delegation

The team first considered a **multi-agent structure** — separate design agent, coding agent, and conductor agent collaborating freely. Building it revealed problems: **large communication overhead between agents, and context lost in transfer** — subtle nuance dropped when "the intent the design agent decided" was handed to the coding agent.

So they chose **harness pattern + external delegation**: design and decision-making live inside a harness built with **Mastra** tools, in two modes (**Plan / Orchestra**); work like actual code-writing, where a strong tool already exists, is delegated to **Claude Code (Claude Agent SDK)**.

**Plan mode (review mode, Plan Agent)** — analyzes the request, sharpens intent, saves a `DesignSpec`, then requests approval via the `ask_user` tool and stops. Access to `runCodingAgent` is **structurally blocked** (deliberately excluded from this mode's tool list) — "a mode that cannot produce code." On approval the same session shifts to Orchestra mode.

**Orchestra mode (execution mode, default)** — intent sharpening → save DesignSpec → verify → generate code → update spec, end-to-end alone. Has every design tool the Plan mode has, plus `runCodingAgent`. When arriving via Plan-mode approval it skips Clarify and Cases and resumes at verification.

**Coding agent** — not a separate Mastra agent. It calls `query()` from `@anthropic-ai/claude-agent-sdk`, spawning the locally installed `claude` binary. Only `Edit / Write / Read / Bash / Glob / Grep` plus the SEED-docs MCP are whitelisted; results (file changes, tool-call events, session ID) flow back to Mastra. Described as "an adapter that embeds Claude Code as a tool."

> "설계의 맥락은 우리가 직접 통제하면서도, 코드 작성처럼 이미 강력한 도구가 있는 영역은 그걸 그대로 활용할 수 있다"
> *"We control the design context ourselves, while areas like code-writing — where a powerful tool already exists — can be used as-is."*

### Tool groups

**Design tools** (write no code; decide *what* to build): `clarifyScreenIntent`, `fetchSeedGuideline` (live lookup of SEED component API docs), `lookupScreenCases`, `saveDesignSpec` / `readDesignSpec`, `validateDesignSpec`, `reverseDesignFromCode` (regenerate a DesignSpec from existing code).

**Coding tools** (execute *how*): `runCodingAgent`.

The system prompt densely carries design knowledge — SEED's 7 design principles, screen patterns, spacing/radius/typography rules — and each tool is "the hands and feet that execute that knowledge."

### Request routing (Orchestra classifies into 4 intents)

1. File read/inspect/explore → straight to coding-agent, bypassing design tools
2. Screen design/modify/implement → design Phase, DesignSpec validation, then coding-agent
3. Conversation/question about SEED → answer directly as Kraft
4. **Ambiguous request → do not refuse and do not guess; must ask back via `ask_user`**

Item 4 is called the core.

### Execution-mode phase pipeline

Clarify → Memory Read → Cases → Initial Spec (`saveDesignSpec`) → **Validate** (`validateDesignSpec`; on error, **up to 2 self-corrections** then re-verify) → Code Generation (`runCodingAgent`) → DesignSpec update (changes recorded in `designDecisions`, becoming next session's context).

### DesignSpec: an intermediate representation

Most AI UI generators wire prompt → code directly. Kraft places a **`DesignSpec` JSON** between them. Fields observed: `title`, `screenType`, `serviceDomain`, `structure` (description + component `tree`), `components` (component, `importFrom: "@seed-design/react"`, usage, props), `designTokens` (`colors`, `typography`, `spacing`), `designDecisions` (topic / decision / rationale).

Stated benefits:

- **Traceability of design intent** — *why* a component was chosen is recorded in `designDecisions`; context invisible from code alone survives.
- **Precision of modification** — to change a screen you edit the relevant part of the DesignSpec and regenerate, rather than editing code. "Change the rating to a slider" also updates the rationale in `designDecisions`.
- **Semantic tokens enforced** — `designTokens` accepts only SEED semantic token names like `bg.layerDefault`, never hardcoded values like `#FF6F0F`. "This alone automatically guarantees Karrot-like color."
- **Reverse-engineerable** — `reverseDesignFromCode` regenerates a DesignSpec from existing code, letting existing screens enter the agent's modification loop.

### Skill system

Putting all design-system rules in the system prompt wastes tokens and makes context-irrelevant rules into noise. So design knowledge is split into **Skills** — markdown modules loaded only when needed. Seven implemented:

| Skill | Role | Example given |
| --- | --- | --- |
| `spacing-constraint` | spacing rules (x0.5–x16 tokens) | "card inner padding at least x4, list-item gap x3" |
| `radius-constraint` | corner rules (r0.5–rFull) | "buttons rFull, cards r3, input fields r2" |
| `typography-constraint` | type rules (t1–t10) | "no more than 4 type steps within one screen" |
| `screen-patterns` | screen layout rules | "8 patterns for error display on form screens" |
| `small-writing-guide` | UI copy rules | "CTA buttons start with a verb, within 12 characters" |
| `design-principles` | SEED's 7 design principles | "connected experience, improvement for users, intuitive experience…" |
| `eval-self-check` | post-write self-check rules | "self-check across 7 areas: color token / component / spacing / typography / icon / layout / animation" |

Example of lazy loading: building a "review-writing form screen" loads `screen-patterns` and `spacing-constraint` but not `small-writing-guide`, which loads only when copy is being decided. Advantage claimed: when a design-system rule updates, only the skill file changes — the whole system prompt is untouched.

### Eval: 11 automatic scorers

Human review every time does not scale, so generated code is scored. **7 code-based** (deterministic, fast) and **4 LLM-based** (qualitative).

Code-based: `color-tokens` (semantic tokens vs. hardcoded hex), `typography` (logical size steps), `layout-structure` (VStack/HStack/Flex against SEED patterns), `spacing-rules` (context-appropriate spacing tokens), `component-compliance` (correct SEED component props), `icon-usage` (SEED icon library rules), `animation-stability`.

LLM-based: `ux-patterns` (pattern appropriate to screen type), `interaction-quality`, `flow-patterns` (flow matches user intent), `form-patterns` (error/loading/empty state handling on form screens).

Runs at the Verify step; a low score feeds back so the agent can self-correct.

### Cross-session design memory

- **Decision-log accumulation** — every generation appends `designDecisions` to `.design-memory/decision-log.jsonl` per session.
- **Automatic principle extraction** — when the same pattern repeats **above a threshold** in the accumulated log, it is auto-promoted to a "per-domain design principle" and stored in `.design-memory/principles.json`.
- **Injection into the next session** — a new session's Memory Read step consults accumulated principles via `readDesignPrinciples`.
- Conversation context survives server restarts via a **LibSQL** memory store (`orchestra-memory.db`).

## Lessons stated

**The trap of wiring prompt → code directly.** The team initially believed a good prompt yields good code. In practice, design systems carry too many tacit rules that are hard to put in a prompt — "padding inside a card must be at least x4," "no more than 4 type steps on one screen." Users do not state these; the agent must already know them. The DesignSpec intermediate representation and the skill system are called the structural answer.

**Generation without verification is meaningless.** Making a "plausible" screen is not hard; making one that *complies with the design system* is. If the second screen differs in style from the first, trust in the tool breaks. The 11-scorer eval system exists to guarantee consistent quality — the machine filters before a human reviews.

## Next problems named

- **Feature expansion driven by user requests.** After an internal announcement, inquiries showed different people wanting different things (fast prototyping vs. learning the design system). The team says it tries to understand *which workflow* a request belongs to rather than treating it as a feature add: "if a similar request arrives several times, that's a gap the tool left open."
- **Multi-canvas view.** Currently focused on one screen; practitioners work by looking at *flows* (trade complete → write review → done) to keep consistency and spot missing steps.
- **Integration with real workflows.** Paths from Figma into Kraft, from Kraft results back to the team library, and automatic SEED-compliance checks at PR review. *"도구는 워크플로우를 바꾸려 하기보다, 워크플로우에 스며들어야 한다고 생각해요."* — *"I think a tool should seep into the workflow rather than try to change it."*
- **Design-decision DB and a learning agent.** Memory currently accumulates per session; the goal is a DB of users' design decisions — which pattern in which domain, and why — so the agent learns dynamically, one person's correction automatically applies for the next person, and "the resolution of Karrot-like judgment" rises over time.

## Limitations and caveats (as observed in the text)

- **No quantitative outcome is reported anywhere.** No adoption count, no before/after time measurement, no error-rate or eval-score figures. The "days to weeks" baseline and "idea to screen in 10 seconds" are stated without measurement. The 11 scorers produce scores, but no score distribution is given.
- **No break-even or maintenance cost stated** for building and running the skill files, scorers, memory store, and harness.
- **Threshold for principle promotion is unspecified** ("above a threshold").
- **Status is early.** The article describes an internal announcement and subsequent inquiries — not an org-wide rollout with measured results.
- **First-party account** by the tool's own builder, on the company engineering blog. No independent evaluation, no dissenting internal view recorded.
- **Multi-agent was rejected on qualitative grounds** ("communication overhead," "context loss") with no measurement or configuration detail given.
- **The `coverage: full` claim** applies to the article, which was read end-to-end; it does not mean Kraft's source code or SEED itself was inspected.
