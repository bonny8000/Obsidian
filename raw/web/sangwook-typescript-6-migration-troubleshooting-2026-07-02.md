---
source_url: https://blog.sangwook.dev/posts/typescript-6-migration-troubleshooting/
captured: 2026-07-02
title: 'TypeScript 6 업그레이드인 줄 알았는데, 문제는 "설정"이었습니다'
authors: [Sangwook Han]
published: 2026-07-02
publisher: Sangwook's Blog
capture_method: Defuddle Markdown extraction plus official TypeScript 6.0 release-note verification
---

# TypeScript 6 migration troubleshooting

## Capture status

- Full article extracted with Defuddle on 2026-07-02.
- Korean body was read as UTF-8; earlier console mojibake was a PowerShell decoding issue, not source corruption.
- Core compiler claims were checked against the official TypeScript 6.0 release notes.
- This card is an AI-authored evidence summary, not a verbatim copy of the article.

## Context

Sangwook Han documents a Turborepo and pnpm workspace migration from TypeScript 5.8.3 to 6.0.3. The article follows three configuration changes from release notes into TypeScript issues and implementation pull requests, then traces one remaining build failure to a declaration-bundler default rather than to the application's own `tsconfig`.

## Key evidence preserved

1. **`baseUrl` deprecation (`TS5101`).** `baseUrl` has a hidden module-resolution role: it can treat a directory as a lookup root for bare specifiers, allowing imports that the runtime or bundler would not resolve. TypeScript 6 deprecates that behavior in preparation for TypeScript 7. `paths` has not required `baseUrl` since TypeScript 4.1.
2. **`rootDir` default and `TS5011`.** TypeScript 6 defaults `rootDir` to the directory containing `tsconfig.json` instead of inferring it from input files. Projects emitting from a deeper `src/` directory should declare `"rootDir": "./src"` when they need the prior output layout.
3. **`types` now defaults to `[]`.** TypeScript no longer enumerates every package under `node_modules/@types` into the global scope. Projects should explicitly name ambient packages such as `node`, `jest`, or test-runner globals. `"types": ["*"]` restores the old behavior but gives up the predictability and performance benefit.
4. **Hidden tool configuration.** The author's remaining `TS5101` came from `tsup` injecting a declaration-build `baseUrl`, even after project configs were cleaned. The field fix was to migrate the declaration build to `tsdown`, not suppress the warning indefinitely.
5. **Underlying principle.** The three compiler changes remove implicit, expensive, or ambiguous defaults. The practical migration method is to expose each dependency explicitly and test the entire toolchain, not only application code.

## Practitioner checklist

- Remove `baseUrl` where it only prefixes `paths`; make mappings explicit or consider package `imports` when runtime support matches.
- Set `rootDir` wherever declaration or JavaScript output layout matters.
- List ambient type packages per workspace package.
- Search build tools and declaration bundlers for generated compiler options.
- Use `ignoreDeprecations` only as a temporary bridge; TypeScript 7 removes unsupported options.

## Caveats

- The migration is one monorepo case; its `tsup` to `tsdown` decision is not automatically required for every project.
- TypeScript 6 contains more breaking/default changes than the three examined here.
- Tool versions are time-sensitive. Re-check the current TypeScript and bundler documentation before applying the recipe.

## Verification links

- [TypeScript 6.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)
- [`baseUrl` deprecation issue](https://github.com/microsoft/TypeScript/issues/62207)
- [`rootDir` default issue](https://github.com/microsoft/TypeScript/issues/62194)
- [`types` default issue](https://github.com/microsoft/TypeScript/issues/62195)
- [tsup repository](https://github.com/egoist/tsup)
- [tsdown migration guide](https://tsdown.dev/guide/migrate-from-tsup)
