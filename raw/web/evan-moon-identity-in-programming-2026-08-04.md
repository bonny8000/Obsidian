---
source_url: https://evan-moon.github.io/2026/08/02/why-identity-is-hard-in-programming/
captured: 2026-08-04
title: "동일성은 왜 프로그래밍에서 가장 어려운 문제인가 (Why Identity Is the Hardest Problem in Programming)"
authors: [Evan Moon]
published: 2026-08-02
publisher: evan-moon.github.io (personal engineering blog)
language: ko
format: long-form engineering essay
---

# Why Identity Is the Hardest Problem in Programming — Evan Moon

**Author:** Evan Moon (evan), Korean frontend engineer, personal blog.
**Published:** 2026-08-02 · **Captured:** 2026-08-04

AI-written extraction. No full-text reproduction; short quoted phrases only, with translation.

---

## Thesis

Identity is not a property you can read off data. It is a **contract the programmer declares** — usually implicitly, by choosing a comparison operator. Languages ship default implementations of that contract, which hides the fact that a decision was ever made. Bugs then appear not where the contract is written but where two differently-declared contracts meet.

> "동일성은 데이터에 들어 있는 속성이 아니라 우리가 코드에 부여하는 계약에 가깝다"
> — *Identity is less a property contained in the data than a contract we assign in code.*

> "선언이 언어 안으로 숨어버리고, 우리는 자기가 계약을 맺었다는 사실조차 잊어버린다"
> — *The declaration hides inside the language, and we forget we even made a contract.*

> "버그는 계약을 어겼을 때가 아니라 … 만나는 경계에서 터진다"
> — *Bugs go off not when a contract is broken, but at the boundary where contracts meet.*

## Opening move — four bugs, one root cause

1. React list `key` set to the array index.
2. `Set` / `Map` failing to deduplicate objects.
3. `useEffect` re-firing because an object literal is a new reference each render.
4. ORM returning two distinct instances for one database row.

All four are the same mismatch: programmer intent about sameness versus the language's comparison semantics.

## Four equality algorithms coexist in JavaScript

| Algorithm | Surfaces | `NaN` vs `NaN` | `+0` vs `-0` |
| --- | --- | --- | --- |
| Loose Equality | `==` | false | true |
| Strict Equality | `===`, `indexOf` | false | true |
| SameValueZero | `includes`, `Set`, `Map` keys | true | true |
| SameValue | `Object.is` | true | false |

The consequence the author highlights: `[NaN].indexOf(NaN)` is `-1` while `[NaN].includes(NaN)` is `true`. Same array, same question, two answers, because the two methods were specified against different algorithms.

## Three meanings of "same"

The author's central taxonomy, given with a detective metaphor (place / appearance / ID number):

| Dimension | Korean term | Criterion | Typical code |
| --- | --- | --- | --- |
| Memory location | 참조 동일성 (reference identity) | same address | `===` on objects |
| Contents | 구조적 동등성 (structural equality) | identical structure | deep-equal, `JSON.stringify` |
| Logical entity | 도메인 동일성 (domain identity) | same persistent ID | `a.id === b.id` |

## Value vs. entity — the role of time

> "값에는 시간이라는 개념이 없고 엔티티에는 있다"
> — *Values have no concept of time; entities do.*

Values (money, coordinates, a date) are timeless and need no ID. Entities (a user, an order) change state over time and therefore require an identity that persists across those changes. The album/photograph metaphor: a photo is a value, the person photographed is an identity, the current photo is that identity's state.

Cited framing: **Rich Hickey / Clojure's values–identity–state split.** Values are unchanging; identity is a stable logical thread through time; state is the value an identity holds at a moment.

Philosophical anchor: **Ship of Theseus** — identity without a persistent marker is undecidable.

## Equivalence axioms (동치관계 공리)

Equality must satisfy three laws:

- **Reflexivity** — `a = a` always.
- **Symmetry** — `a = b` implies `b = a`.
- **Transitivity** — `a = b` and `b = c` implies `a = c`.

Epsilon comparison breaks transitivity and cannot be repaired algorithmically:

```js
const isEqual = (a, b) => Math.abs(a - b) < 0.1;
isEqual(1.00, 1.09); // true
isEqual(1.09, 1.18); // true
isEqual(1.00, 1.18); // false  ← transitivity broken
```

## Silent failure — why axiom violations are dangerous

> "잘못된 동일성은 그 자리에서 터지지 않는다"
> — *A wrong identity does not blow up on the spot.*

Hash-based structures (`Set`, `Map`) assume reflexivity and hash/equality consistency. Violations produce: values that become unreachable after insertion, sorts that silently return wrong order (Tim Sort with a broken comparator), and caches whose hit/miss behaviour is inconsistent. Nothing throws.

## How languages have handled it

- **JavaScript** — hard split between primitives and objects; no user-defined value types.
- **Java** — originally required overriding `equals`/`hashCode` in pairs; now `record`, and **JEP 401 Value Objects** from **Project Valhalla, running since 2014**. The author's aside: *"무려 12년이나 붙들고 있는"* — *held onto for a full twelve years* — as evidence of how hard the problem is at the language level.
- **Rust** — decomposes the concern into traits: `Copy` for move semantics, `PartialEq` for equality that may be partial (floats, `NaN`), `Eq` as a marker asserting the full equivalence relation holds.
- **Haskell** — type classes express the contract but the laws are not enforced by the compiler.
- **Git / Docker** — content addressing (SHA-1/SHA-256): identity *is* the content hash, which is why mutable state cannot be represented that way.

The author's read: Rust's split is the most honest design because it separates "can be compared" from "the axioms hold."

## Practical patterns given

**Domain-keyed dedup** — do not rely on `Set` for objects:

```ts
const dedupeBy = <T, K>(items: T[], toKey: (item: T) => K) =>
  Array.from(new Map(items.map(item => [toKey(item), item])).values());

dedupeBy(users, user => user.id);
```

**Brand types** — lift domain identity into the type system so IDs of different entities cannot be swapped:

```ts
type UserId = Brand<string, 'UserId'>;
type OrderId = Brand<string, 'OrderId'>;
findUser(toOrderId('order-1')); // compile error
```

**React `key` as an explicit identity declaration** — the framework forces the programmer to state whether identity is positional or domain-based, which the author treats as good design precisely because the choice becomes visible in the source.

**ORM Identity Map pattern** — session-scoped instance cache so one row yields one object. Named ORMs: Prisma, Sequelize, Hibernate, Entity Framework Core.

## Caveats the author states

- Language runtimes do not detect axiom violations, and the edge cases are not documented where the programmer would look.
- Epsilon comparison is *fundamentally* incompatible with transitivity — not a fixable bug.
- Brand types carry real maintenance cost: *"변환 함수가 우수수 늘어나고"* — *conversion functions pile up.*
- `useMemo` is not a caching guarantee; React may discard the cache.
- Content addressing cannot represent mutable state, so it is not a general answer.
- On whether to throw versus degrade, the author marks the position as preference (*"필자는 … 낫다고 본다"* — *I think … is better*) rather than assertion.

## References named in the piece

JEP 401 (Value Objects) · Project Valhalla (2014–) · Java `record` · Tim Sort · ECMAScript comparison algorithms · Rust trait system, `derive(Eq)` · Haskell type classes · IEEE 754 · Git/Docker content addressing · React reconciliation and `key` semantics · Rich Hickey, *Values and Change* (Clojure design rationale) · Identity Map pattern · Ship of Theseus.

## Structure of the argument

Four runtime bugs (symptoms) → multiple equality algorithms → language design choices → mathematical axioms → silent data-structure failure → the value/entity philosophical boundary → practical code organisation.
