---
type: source
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [identity, equality-semantics, value-objects, domain-modeling, javascript, rust, java, react, orm, korean-source, infrastructure-dev]
source_path: raw/web/evan-moon-identity-in-programming-2026-08-04.md
source_url: https://evan-moon.github.io/2026/08/02/why-identity-is-hard-in-programming/
authors: [Evan Moon]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.78
---

# Evan Moon (2026): Why Identity Is the Hardest Problem in Programming

## Citation

Evan Moon (evan), "동일성은 왜 프로그래밍에서 가장 어려운 문제인가" (*Why Identity Is the Hardest Problem in Programming*), personal blog, 2026-08-02. Korean, with an English translation route in the URL structure.

**Source type:** Long-form engineering essay by a practising frontend engineer. Technical claims are verifiable against language specifications; the framing is the author's own.
**Raw capture:** [[raw/web/evan-moon-identity-in-programming-2026-08-04|evan-moon-identity-in-programming-2026-08-04]]
**Coverage note:** `coverage: full` — the full argument arc, all four equality algorithms, the three-sameness taxonomy, the axioms, the language survey, and every code pattern were captured with original-language quotes.

## Summary

The best-argued piece of engineering writing this vault has ingested, and its thesis is portable well beyond code.

> "동일성은 데이터에 들어 있는 속성이 아니라 우리가 코드에 부여하는 계약에 가깝다"
> — *Identity is less a property contained in the data than a contract we assign in code.*

The essay opens with four unrelated-looking bugs — React `key` set to array index, `Set` failing to dedupe objects, `useEffect` re-firing on an object literal, an ORM returning two instances for one row — and shows they are one bug: a mismatch between what the programmer means by "same" and what the language means.

The second move is the one that makes this durable. Languages ship a default identity contract, and the default **hides that a decision was made**:

> "선언이 언어 안으로 숨어버리고, 우리는 자기가 계약을 맺었다는 사실조차 잊어버린다"
> — *The declaration hides inside the language, and we forget we even made a contract.*

And therefore:

> "버그는 계약을 어겼을 때가 아니라 … 만나는 경계에서 터진다"
> — *Bugs go off not when a contract is broken, but at the boundary where contracts meet.*

The essay's third move is to show why these failures are quiet: hash structures and sort algorithms *assume* the equivalence axioms and do not check them. *"잘못된 동일성은 그 자리에서 터지지 않는다"* — *a wrong identity does not blow up on the spot.* Nothing throws. Values become unreachable, sorts return wrong order, caches disagree with themselves.

## Key Claims

- **Three distinct meanings of "same," and choosing between them is the design decision:**

  | Dimension | Term | Criterion | Typical code |
  |---|---|---|---|
  | Memory location | 참조 동일성 (reference identity) | same address | `===` on objects |
  | Contents | 구조적 동등성 (structural equality) | identical structure | deep-equal |
  | Logical entity | 도메인 동일성 (domain identity) | same persistent ID | `a.id === b.id` |

- **JavaScript ships four equality algorithms simultaneously,** and they disagree on edge cases. `[NaN].indexOf(NaN)` is `-1`; `[NaN].includes(NaN)` is `true` — same array, same question, two answers, because the two methods were specified against different algorithms (`===` vs. SameValueZero). Neither is a bug; both are the spec.

- **Time is what separates a value from an entity.** *"값에는 시간이라는 개념이 없고 엔티티에는 있다"* — *values have no concept of time; entities do.* Money and coordinates are timeless and need no ID; a user or an order changes state and therefore requires an identity that persists through the change. Cited framing: **Rich Hickey's values / identity / state split** from Clojure — a photograph is a value, the person is an identity, the current photo is that identity's state.

- **Equality must satisfy three axioms** — reflexivity, symmetry, transitivity — and epsilon comparison **cannot** satisfy transitivity. `|a−b| < 0.1` makes 1.00 ≈ 1.09 ≈ 1.18 but not 1.00 ≈ 1.18. The author is explicit that this is not a fixable bug but a property of the approach.

- **Axiom violations fail silently, in three named ways:** values unreachable after insertion into a hash structure; sorts (Tim Sort is named) producing wrong order with a broken comparator; cache hit/miss inconsistency.

- **Rust's trait decomposition is the most honest language design** on the author's reading: `Copy` for move semantics, `PartialEq` for equality that may be partial (floats, `NaN`), `Eq` as a marker asserting the full equivalence relation holds. Separating "can be compared" from "the axioms hold" makes the contract explicit rather than default.

- **The problem is hard at language level, with a receipt.** Java's Project Valhalla has been running since 2014 toward JEP 401 Value Objects — *"무려 12년이나 붙들고 있는"* (*held onto for a full twelve years*). Haskell expresses the contract in type classes but does not enforce the laws.

- **React's `key` is good design because it forces the declaration into the source.** The programmer must state whether identity is positional or domain-based. The choice becomes visible and reviewable.

- **Content addressing is identity-as-hash** (Git, Docker digests), which is exactly why it cannot represent mutable state.

## Useful Examples

**The four-algorithm table** — worth keeping verbatim:

| Algorithm | Surfaces | `NaN` vs `NaN` | `+0` vs `-0` |
|---|---|---|---|
| Loose Equality | `==` | false | true |
| Strict Equality | `===`, `indexOf` | false | true |
| SameValueZero | `includes`, `Set`, `Map` keys | true | true |
| SameValue | `Object.is` | true | false |

**Domain-keyed dedup** — the practical replacement for `new Set(objects)`:

```ts
const dedupeBy = <T, K>(items: T[], toKey: (item: T) => K) =>
  Array.from(new Map(items.map(item => [toKey(item), item])).values());

dedupeBy(users, user => user.id);
```

**Brand types** — lifting domain identity into the type system so a `UserId` cannot be passed where an `OrderId` is expected. The author gives the cost honestly: *"변환 함수가 우수수 늘어나고"* — *conversion functions pile up.*

**The ORM Identity Map pattern** — a session-scoped instance cache so one row yields one object. Named implementations: Prisma, Sequelize, Hibernate, Entity Framework Core.

**The Ship of Theseus** is used properly rather than decoratively: identity without a persistent marker is genuinely undecidable, which is why entities need IDs assigned rather than derived.

## Constraints / Caveats

- **Single-author essay, no peer review.** Every specification-level claim (the four algorithms, `NaN`/`±0` behaviour, Rust trait semantics, JEP 401) is independently verifiable and, on inspection, correct — which is what carries the confidence here. The *framing* is the author's own construction.
- **The headline claim is unfalsifiable.** "The hardest problem in programming" is rhetoric. Nothing establishes ranking against concurrency, naming, or distributed consensus, and nothing needs to.
- **Frontend-weighted.** React, TypeScript, and ORM examples dominate. The three-sameness taxonomy is language-independent, but the illustrations are not, and readers outside that stack get less.
- **The author marks his own preferences as preferences.** On whether to throw versus degrade on identity violations: *"필자는 … 낫다고 본다"* (*I think … is better*). Correctly hedged and worth respecting as a hedge.
- **No empirical claim about bug frequency.** The four opening bugs are presented as recognisable, not as measured. Whether identity confusion is a leading cause of defects is not addressed.
- **`useMemo` caveat is real and underexplored** — the essay notes React may discard the cache, which undercuts memoisation as an identity-stability strategy without fully following the consequence.

## Design Implications

- **State the identity contract explicitly wherever two systems meet.** The boundary claim is the actionable one: API deserialisation, cache keys, ORM hydration, and diffing algorithms are all places two identity contracts meet, and none of them announces it.
- **Choose the sameness dimension before choosing the comparison.** Reference, structural, or domain — the question is which one this code means, and the answer should be written down.
- **Never use `Set`/`Map` for object identity without a domain key.** Use the `dedupeBy` shape. This alone eliminates a common class of silent duplication.
- **Treat epsilon comparison as intransitive by construction.** Do not sort with it, do not use it as a hash key, and do not chain it.
- **Prefer designs that force the declaration into the source** — React's `key`, Rust's `Eq`, brand types. The measure of a good identity API is whether a reviewer can see the choice.
- **Assign IDs to entities; derive nothing from content for anything mutable.** Content addressing is for values.

## Tensions

- **Directly relevant to [[wiki/concepts/ai-agents/agent-memory|agent memory]], and neither this source nor the vault has connected them.** An agent that remembers "the user" across sessions is asserting a domain identity across state changes — with no declared contract, no ID, and no boundary check. The essay's silent-failure analysis predicts exactly the observed failure mode in [[wiki/concepts/ai-agents/memory-contamination|memory contamination]]: nothing throws, the wrong entity is retrieved, and the system proceeds confidently. **This is the most valuable unexplored link in this ingest.**
- **Reframes [[wiki/concepts/infrastructure-dev/object-graph-mapping|object-graph mapping]] and [[wiki/concepts/infrastructure-dev/object-backend|object backend]].** The ORM instance problem is not an ORM defect; it is a boundary between database domain identity and language reference identity, and Identity Map is the pattern that reconciles them.
- **A precise counterpart to [[wiki/concepts/infrastructure-dev/deterministic-ui|deterministic UI]].** Deterministic rendering requires stable identity for its inputs; an index-based `key` is precisely the identity instability that makes rendering non-deterministic under reordering.
- **Supports [[wiki/concepts/ai-agents/spec-driven-development|spec-driven development]] from an unexpected direction.** The essay's thesis is that hidden defaults cause failures at boundaries, and its recommended fix is making the declaration explicit and reviewable — the same argument spec-driven development makes about intent generally.
- **Against how this vault handles its own entities.** Source pages are identified by filename, and the vault has renamed and re-slugged pages before. Wiki links are reference identity (path) standing in for domain identity (the source). [[wiki/decisions/2026-07-20-link-path-convention|The link-path convention decision]] is, in this essay's vocabulary, an identity-contract decision — and the "keep filenames stable once linked" rule in `AGENTS.md` exists because the vault chose reference identity and has to freeze it. Worth knowing that is what the rule is doing.

## Open Questions

- Does the value/entity distinction give a usable rule for what an agent should store as memory (values, immutable and safe) versus what it should key (entities, needing declared IDs)? The essay does not consider agents at all and the mapping looks clean.
- Is there a language-level mechanism that could enforce the equivalence axioms rather than assert them? Rust's `Eq` is a promise, not a proof; Haskell does not enforce laws either. Twelve years of Valhalla suggests the answer is hard.
- How often do real defects trace to identity confusion? Unmeasured here and measurable in any bug tracker.
- What is the identity contract at an LLM boundary — when the same entity is described in text, retrieved, and re-serialised, what preserves its identity?

## Concepts Linked from This Source

- [[wiki/concepts/infrastructure-dev/identity-contract|Identity Contract]] *(new)*
- [[wiki/concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]]
- [[wiki/concepts/infrastructure-dev/object-backend|Object Backend]]
- [[wiki/concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]
- [[wiki/concepts/infrastructure-dev/typescript-configuration-hygiene|TypeScript Configuration Hygiene]]
- [[wiki/concepts/ai-agents/agent-memory|Agent Memory]]
- [[wiki/concepts/ai-agents/memory-contamination|Memory Contamination]]
- [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]]
- [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]]

## LLM Use Guidance

- **Use the three-sameness taxonomy** (reference / structural / domain) as the first question in any deduplication, caching, diffing, memory, or data-merge problem. It is the highest-leverage content in the source and it is domain-independent.
- **Use the four-algorithm table** as a factual reference for JavaScript equality; it is spec-accurate.
- **Use the boundary heuristic** — look for bugs where two identity contracts meet, not where one is written — when debugging silent duplication or phantom re-renders.
- **Use the value/entity test** ("does time apply to this thing?") to decide whether something needs an assigned ID.
- **Do not repeat "the hardest problem in programming"** as a claim; it is a title.
- Treat the code patterns as idiomatic starting points rather than as validated library code.

## Reliability Notes

- **Confidence 0.78 — the highest in this ingest batch,** and the reason is structural rather than reputational. Every technical claim is checkable against a specification (ECMAScript comparison algorithms, IEEE 754, Rust trait definitions, JEP 401, React reconciliation) and the ones checked hold. The conceptual framing is drawn from established sources the author names — Rich Hickey's values/identity/state, DDD's value-object/entity split, the Identity Map pattern — rather than invented.
- Held below 0.85 by: no peer review, an unfalsifiable headline, a frontend-weighted example set, and no empirical claim about how often this actually causes defects.
- **The taxonomy and the boundary thesis are the durable parts.** The specific code patterns are competent and ordinary.
- **Highest-value verification step:** none needed for the technical content. The valuable next step is not verification but *extension* — testing whether the value/entity distinction gives a usable design rule for agent memory, which is a question this source raises without knowing it.
