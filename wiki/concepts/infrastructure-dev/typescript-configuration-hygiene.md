---
type: concept
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [typescript, configuration, migration, monorepo, determinism]
sources:
  - sources/sangwook-typescript-6-migration-troubleshooting
confidence: 0.88
---

# TypeScript Configuration Hygiene

> [!abstract] Summary
> Make module resolution, output layout, ambient globals, and tool-generated compiler options explicit so every build stage resolves the same project.

## Why It Matters

TypeScript errors often look local while originating in layered config, a declaration bundler, or a workspace default. Explicit configuration narrows that hidden state and makes migrations reproducible across editor, type-check, test, build, and declaration pipelines.

## Key Claims

- A compiler option is not understood until its provenance is known.
- Module aliases must match runtime resolution, not only editor resolution.
- Output layout is a contract; declare `rootDir` when consumers depend on it.
- Ambient types should be scoped to the packages that use them.
- Full migration verification includes generated configs and build-tool adapters.

## Migration Gate

1. Print or inspect the effective config for each workspace package.
2. Remove ambiguous `baseUrl` behavior and make mappings explicit.
3. Declare `rootDir` for emit-sensitive packages.
4. List required ambient `types` per environment.
5. Run type check, declaration emit, build, and tests independently.
6. Trace any unexpected option to the tool that generated it.

## Conflicts & Caveats

> [!warning] Tradeoff
> Repetition across package configs can create maintenance cost. Prefer shared presets only when they preserve environment-specific type and module boundaries.

## Related Concepts

- [[concepts/infrastructure-dev/modern-web-guidance|Modern Web Guidance]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]]

## Sources

- [[sources/sangwook-typescript-6-migration-troubleshooting|Sangwook Han: TypeScript 6 Migration Troubleshooting]]

## Open Questions

- Can the repo generate a machine-readable report of effective TypeScript config per package?
- Which aliases can move to standards-based package `imports`?
- What migration checks should become CI assertions before TypeScript 7?
