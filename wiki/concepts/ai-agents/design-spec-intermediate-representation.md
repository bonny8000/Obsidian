---
type: concept
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [concept, ai-agents, intermediate-representation, spec-driven-development, design-system, traceability, semantic-tokens, constraint-by-construction]
sources: [karrot-kraft-design-system-agent, polar-orbit-llm-safe-design-system]
confidence: 0.72
---

# Design Spec as Intermediate Representation

> [!abstract] Summary
> Instead of wiring **prompt → code** directly, place a structured, machine-validated **spec document** between them: the agent first decides *what to build* and writes it as data, that data is validated against system rules, and only then is code generated from it. The spec — not the code, and not the prompt — becomes the artifact that is edited, versioned, validated, and remembered.

> [!important] Why it Matters
> A prompt cannot carry the tacit rules of a mature system, and generated code cannot explain why it looks the way it does. An intermediate representation solves both at once: it is a **schema**, so it can refuse to represent an off-system choice, and it is a **record**, so the reasoning behind a choice survives into the next session. It converts "the model remembered the rules this time" into "the rules are structurally present."

## 📝 Key Claims

- **The schema is the enforcement point.** In [[wiki/sources/karrot-kraft-design-system-agent|Kraft's]] `DesignSpec`, the `designTokens` field accepts only SEED semantic token names (`bg.layerDefault`) and cannot hold a raw hex value like `#FF6F0F`. Brand-correct color is not something the model is asked to remember — it is the only thing the field can hold. This is [[wiki/concepts/infrastructure-dev/llm-safe-design-system|constraining the acceptance criteria, not the generator]], moved up from the type system into the spec.

- **Rationale is a first-class field.** Kraft's `designDecisions` records `topic` / `decision` / `rationale` — e.g. star rating as five tappable icons, chosen because it is more intuitive than a slider and less mis-tap-prone on mobile. *"코드만 보면 알 수 없는 맥락이 남아요"* — context invisible from the code alone survives. This is what makes the layer worth its cost; a spec that only restated the code would not be.

- **Edits go to the spec, then regenerate.** "Change the rating to a slider" modifies the spec — including its recorded rationale — and the code is re-derived. Editing generated code directly desynchronises the two and discards the reasoning.

- **The representation should be reversible.** Kraft's `reverseDesignFromCode` regenerates a spec from existing code, which is what lets pre-existing screens enter the agent's modification loop at all. A one-way pipeline can only ever handle greenfield work.

- **Validation happens on the spec, before generation.** Checking a structured document against system rules is cheaper and more deterministic than checking generated code, and it fails before any code is written. Kraft bounds the repair loop at **two** self-corrections before re-verification.

- **The spec is the memory unit.** Because decisions are already structured data, they can be appended to a log, counted, and promoted into standing principles — see [[wiki/concepts/ai-agents/agent-memory|agent memory]]. Free-text prompts and generated code are both poor substrates for that.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]] — the same instinct with a different owner. In SDD a **human** writes the spec as the source of truth; here the **agent** writes it as a checkable intermediate. The distinction matters: SDD treats code as disposable, whereas this pattern treats the spec as *derived and re-derivable* from code.
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] — the same principle enforced in the type system and CI rather than in a spec schema.
- [[wiki/concepts/ai-agents/interactive-specs|Interactive Specs]]
- [[wiki/concepts/ai-agents/agent-memory|Agent Memory]]
- [[wiki/concepts/ai-agents/generated-output-scoring|Generated-Output Scoring]] — validation *after* generation; the spec is validation *before* it.
- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[wiki/comparisons/where-to-put-the-constraint|Where to Put the Constraint]]

## ⚖️ Conflicts & Caveats

- **The layer can become the drift.** Two artifacts describing one screen is a synchronisation problem. Kraft ships `reverseDesignFromCode`, which is a tell — the drift was anticipated before it was solved.
- **No evidence it pays for itself.** The only detailed source reports no measurement of quality, speed, or rework, so the pattern is currently justified by argument rather than result.
- **Schema rigidity cuts both ways.** A field that cannot hold a hex value also cannot express a deliberate exception, and no source describes the escape hatch.
- **Single-source pattern.** Only Kraft implements this concretely in this vault. Polar Orbit supports the *principle* from the type-system side but does not use an intermediate spec.

## 📚 Sources

- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — the `DesignSpec` implementation, in detail
- [[wiki/sources/polar-orbit-llm-safe-design-system|Polar Orbit]] — the same principle enforced one layer down

## ❓ Open Questions

- At what system size does the spec layer pay back? For a small component set, typed props alone may be sufficient and cheaper.
- How is a deliberate exception represented, and who approves it?
- Does spec-mediated editing actually produce better revisions than direct code editing, or does it just produce more traceable ones?
- Can the spec schema itself be generated from the design system's source of truth, so the two cannot diverge?
