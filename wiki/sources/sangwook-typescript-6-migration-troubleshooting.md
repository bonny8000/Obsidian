---
type: source
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [typescript, typescript-6, migration, tsconfig, monorepo, tsup, tsdown]
sources: []
source_path: raw/web/sangwook-typescript-6-migration-troubleshooting-2026-07-02.md
source_url: https://blog.sangwook.dev/posts/typescript-6-migration-troubleshooting/
authors: [Sangwook Han]
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# Sangwook Han: TypeScript 6 Migration Troubleshooting

> [!info] Metadata
> - **Author:** Sangwook Han
> - **Published:** 2026-07-02
> - **Type:** practitioner migration report
> - **Raw card:** [[raw/web/sangwook-typescript-6-migration-troubleshooting-2026-07-02]]
> - **URL:** [blog.sangwook.dev](https://blog.sangwook.dev/posts/typescript-6-migration-troubleshooting/)

## Citation

Han, S. (2026, July 2). *TypeScript 6 업그레이드인 줄 알았는데, 문제는 "설정"이었습니다.* Sangwook's Blog. Captured 2026-07-02.

## Summary

A monorepo migration report that treats TypeScript 6 as a configuration-hygiene exercise rather than a version-number exercise. Han traces `baseUrl`, `rootDir`, and `types` changes from release notes through TypeScript issues and implementation diffs, then demonstrates that a hidden declaration-bundler default can keep producing a deprecated compiler option after application configs are fixed.

## Key Claims

- `baseUrl` is deprecated because its bare-specifier lookup behavior can accept imports that do not match runtime resolution. Most `paths` users can remove it and make mappings explicit.
- `rootDir` should be declared when a project expects a specific emit layout; TypeScript 6 no longer infers it from the input set when a `tsconfig` exists.
- `types` now defaults to an empty list, so ambient packages should be named per package instead of being pulled in transitively from a flattened monorepo.
- The migration is incomplete until generated and tool-owned TypeScript options are inspected. The author's residual `TS5101` came from `tsup`'s declaration-build behavior.
- The durable rule is to replace implicit compiler and tool defaults with explicit, reviewable configuration.

## Useful Examples

- Remove `baseUrl: "."` while retaining explicit `paths` mappings.
- Add `rootDir: "./src"` to preserve `dist/index.js` rather than `dist/src/index.js` when that layout is intentional.
- Use `types: ["node", "vitest/globals"]` only in packages that require those globals.
- Search tool configuration when a compiler diagnostic names an option absent from every checked-in `tsconfig`.

## Constraints / Caveats

- The field report covers a Turborepo plus pnpm workspace and does not enumerate every TypeScript 6 breaking change.
- `tsup` to `tsdown` is a case-specific resolution, not a universal migration requirement.
- `ignoreDeprecations: "6.0"` is a temporary compatibility bridge; it does not make a TypeScript 7-incompatible option durable.
- Package `imports`, bundler aliases, and TypeScript `paths` must be evaluated against the actual runtime and test runner.

## Design Implications

- Add a configuration provenance step to migration checklists: for every compiler option in an error, identify whether it comes from source control, an extended config, a plugin, or generated state.
- Run type checking, declaration emit, application builds, and tests separately; each layer may load a different config path.
- In monorepos, prefer explicit per-package ambient types over a global base config that silently broadens every package.
- Treat compiler defaults as API surface: pin critical defaults when output layout or global types affect downstream consumers.

## Tensions

- Explicit config improves predictability but adds maintenance across many packages.
- `paths` aliases are convenient at author time but can diverge from runtime resolution unless the package manager, bundler, tests, and TypeScript share one mapping source.
- Suppressing deprecations can unblock a migration while obscuring the exact work required before TypeScript 7.

## Open Questions

- Which tools in the current project synthesize compiler options during declaration or test builds?
- Can package `imports` replace private aliases without breaking the project's bundler and editor workflow?
- Should a repository add a test that prints effective `tsconfig` values for every workspace package?

## Concepts Linked

- [[concepts/infrastructure-dev/typescript-configuration-hygiene|TypeScript Configuration Hygiene]]
- [[concepts/infrastructure-dev/modern-web-guidance|Modern Web Guidance]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]

## LLM Use

- **Use for:** diagnosing TypeScript 6 migration errors, reviewing monorepo `tsconfig` defaults, and identifying hidden tool configuration.
- **Do not use for:** claiming every TypeScript 6 change is covered or selecting a bundler without current project evidence.
- **Best prompt pattern:** provide the effective config, command, emitted path, and full diagnostic; ask the LLM to trace config provenance before proposing edits.

## Reliability Notes

> [!warning] Caveats
> Practitioner evidence is limited to one monorepo. The three compiler behaviors were cross-checked against official TypeScript 6.0 documentation; the bundler conclusion remains environment-specific.

## Backfill Status

- New standard ingest completed 2026-07-02.
