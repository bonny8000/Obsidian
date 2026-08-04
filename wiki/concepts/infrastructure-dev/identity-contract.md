---
type: concept
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [concept, infrastructure-dev, identity, equality-semantics, value-objects, domain-modeling, agent-memory, data-modeling]
sources: [evan-moon-identity-in-programming]
confidence: 0.78
---

# Identity Contract

> [!abstract] Summary
> Identity is not a property you can read off data. It is a **contract declared in code** — usually implicitly, by choosing a comparison operator. Languages ship a default implementation of that contract, and the default hides that a decision was ever made.
>
> *"동일성은 데이터에 들어 있는 속성이 아니라 우리가 코드에 부여하는 계약에 가깝다"* — *identity is less a property contained in the data than a contract we assign in code.* — [[wiki/sources/evan-moon-identity-in-programming|Evan Moon (2026)]]

## Why It Matters

The failure mode is specific and worth memorising:

> "버그는 계약을 어겼을 때가 아니라 … 만나는 경계에서 터진다"
> — *Bugs go off not when a contract is broken, but at the boundary where contracts meet.*

Each side of a boundary is internally consistent. The defect appears only where two differently-declared notions of "same" are joined — API deserialisation, cache keys, ORM hydration, diffing algorithms, agent memory retrieval. None of those boundaries announces itself.

And the failures are silent. Hash structures and sort algorithms *assume* the equivalence axioms and do not check them: *"잘못된 동일성은 그 자리에서 터지지 않는다"* — *a wrong identity does not blow up on the spot.*

## Three Meanings of "Same"

The core taxonomy. Choosing among these **is** the design decision:

| Dimension | Term | Criterion | Typical code | Fails when |
|---|---|---|---|---|
| Memory location | Reference identity | Same address | `===` on objects | Two instances represent one thing |
| Contents | Structural equality | Identical structure | deep-equal | Two distinct things happen to match |
| Logical entity | Domain identity | Same persistent ID | `a.id === b.id` | No ID has been assigned |

## Value vs. Entity — Time Is the Test

> "값에는 시간이라는 개념이 없고 엔티티에는 있다"
> — *Values have no concept of time; entities do.*

A **value** is timeless and needs no identifier: money, a coordinate, a date. An **entity** changes state over time and therefore requires an identity that persists through the change: a user, an order.

The framing comes from **Rich Hickey's values / identity / state split** in Clojure, which the source names: a photograph is a value, the person photographed is an identity, the current photo is that identity's state. The philosophical anchor is the **Ship of Theseus** — identity without a persistent marker is undecidable, which is why entities need IDs *assigned* rather than derived.

**The practical rule:** ask whether time applies to this thing. If it does, it needs an assigned ID.

## The Equivalence Axioms

Equality must satisfy three laws — **reflexivity** (`a = a`), **symmetry** (`a = b` ⟹ `b = a`), and **transitivity** (`a = b`, `b = c` ⟹ `a = c`).

Epsilon comparison **cannot** satisfy transitivity, and this is a property of the approach rather than a fixable bug:

```js
const isEqual = (a, b) => Math.abs(a - b) < 0.1;
isEqual(1.00, 1.09); // true
isEqual(1.09, 1.18); // true
isEqual(1.00, 1.18); // false  ← transitivity broken
```

**How violations surface, all silently:** values unreachable after insertion into a hash structure; sorts returning wrong order with a broken comparator (Tim Sort named); cache hit/miss inconsistency. Nothing throws.

## Four Equality Algorithms in JavaScript

Spec-accurate, and worth keeping:

| Algorithm | Surfaces | `NaN` vs `NaN` | `+0` vs `-0` |
|---|---|---|---|
| Loose Equality | `==` | false | true |
| Strict Equality | `===`, `indexOf` | false | true |
| SameValueZero | `includes`, `Set`, `Map` keys | true | true |
| SameValue | `Object.is` | true | false |

Consequence: `[NaN].indexOf(NaN)` is `-1` while `[NaN].includes(NaN)` is `true`. Same array, same question, two answers — because the methods were specified against different algorithms. Neither is a bug.

## Making the Declaration Visible

The design principle the source argues for: **prefer mechanisms that force the identity choice into the source, where a reviewer can see it.**

- **React's `key`** — the programmer must state whether identity is positional or domain-based. Good design because the choice becomes reviewable.
- **Rust's trait split** — `Copy` for move semantics, `PartialEq` for equality that may be partial (floats, `NaN`), `Eq` as a marker asserting the axioms hold. Separating "can be compared" from "the axioms hold" is the most honest design in the source's survey.
- **Brand types** — lift domain identity into the type system so a `UserId` cannot be passed where an `OrderId` is expected. Cost, stated honestly: *"변환 함수가 우수수 늘어나고"* — conversion functions pile up.
- **Domain-keyed dedup** — the replacement for `new Set(objects)`:

```ts
const dedupeBy = <T, K>(items: T[], toKey: (item: T) => K) =>
  Array.from(new Map(items.map(item => [toKey(item), item])).values());
```

- **ORM Identity Map** — a session-scoped instance cache so one row yields one object. The ORM two-instances problem is not an ORM defect; it is a boundary between database domain identity and language reference identity.

**Language-level difficulty, with a receipt:** Java's Project Valhalla has run since 2014 toward JEP 401 Value Objects — twelve years. Haskell expresses the contract in type classes and does not enforce the laws. Content addressing (Git, Docker) makes identity *be* the content hash, which is exactly why it cannot represent mutable state.

## The Agent-Memory Connection

> [!important] The most valuable unexplored link in this area
> An agent that remembers "the user" across sessions is asserting a **domain identity across state changes** — with no declared contract, no assigned ID, and no boundary check. The silent-failure analysis above predicts precisely the observed failure mode in [[wiki/concepts/ai-agents/memory-contamination|memory contamination]]: nothing throws, the wrong entity is retrieved, and the system proceeds confidently.
>
> Neither the source nor any agent-memory source in this vault has made this connection. The value/entity test looks like it should give a usable rule — store values (immutable, safe); key entities (needing declared IDs) — and **that is a hypothesis, not a finding.**

## ⚖️ Conflicts & Caveats

> [!warning] Single-author essay
> Every specification-level claim is independently verifiable (ECMAScript comparison algorithms, IEEE 754, Rust trait semantics, JEP 401, React reconciliation) and the ones checked hold. The *framing* — three sameness dimensions, the boundary thesis — is the author's own construction, drawn from named established sources.

> [!warning] No empirical claim about frequency
> The four opening bugs are presented as recognisable, not as measured. Whether identity confusion is a leading cause of real defects is unaddressed and measurable in any bug tracker.

> [!warning] Frontend-weighted examples
> React, TypeScript, and ORM cases dominate. The taxonomy is language-independent; the illustrations are not.

> [!warning] `useMemo` is not an identity-stability guarantee
> React may discard the cache. The source notes this and does not follow the consequence — memoisation is not a reliable way to hold reference identity stable.

## This Vault's Own Identity Contract

Source pages are identified by **filename**, so wiki links are reference identity (a path) standing in for domain identity (a source). This is why `AGENTS.md` says *"keep filenames stable once linked"* — the vault chose reference identity and therefore has to freeze it. [[wiki/decisions/2026-07-20-link-path-convention|The link-path convention decision]] is, in this concept's vocabulary, an identity-contract decision. Worth knowing that is what the rule is doing, and what it costs.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/agent-memory|Agent Memory]] — an undeclared identity contract over time.
- [[wiki/concepts/ai-agents/memory-contamination|Memory Contamination]] — the predicted failure mode.
- [[wiki/concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]] — reframed: a boundary between two identity contracts.
- [[wiki/concepts/infrastructure-dev/object-backend|Object Backend]]
- [[wiki/concepts/infrastructure-dev/deterministic-ui|Deterministic UI]] — requires stable identity for its inputs; an index-based `key` is the instability.
- [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]] — the same argument about hidden defaults and explicit declaration.
- [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]] — domain identity at organisational scale.
- [[wiki/concepts/infrastructure-dev/domain-knowledge-graph|Domain Knowledge Graph]] — entity resolution is this problem with a different name.
- [[wiki/concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]] — broken-link detection is an identity-contract check.

## 📚 Sources

- [[wiki/sources/evan-moon-identity-in-programming|Evan Moon (2026): Why Identity Is the Hardest Problem in Programming]] — sole source. The contract framing, the three-sameness taxonomy, the boundary thesis, the axioms, the language survey, and every code pattern.

## ❓ Open Questions

- Does the value/entity distinction give a usable rule for agent memory — values stored, entities keyed? The mapping looks clean and is untested.
- Is there a language mechanism that could *enforce* the equivalence axioms rather than assert them? Rust's `Eq` is a promise; Haskell does not enforce laws; twelve years of Valhalla suggests the answer is hard.
- What is the identity contract at an LLM boundary — when an entity is described in text, retrieved, and re-serialised, what preserves its identity?
- How often do real defects trace to identity confusion? Unmeasured and measurable.
