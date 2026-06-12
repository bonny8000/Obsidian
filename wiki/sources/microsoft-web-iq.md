---
source: https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ
author: Knut Risvik (Distinguished Engineer, Search & AI)
title: "Announcing Microsoft Web IQ: AI-Native Grounding APIs"
date: 2026-06-03
tags: [AI-Native, Microsoft, Web-IQ, Grounding, Agentic-Era, Search-API, RAG, Token-Efficiency]
updated: 2026-06-12
ingest_level: light
coverage: partial
llm_ready: false
raw_preserved: false
---

# Microsoft Web IQ: AI-Native Grounding APIs

## Summary

마이크로소프트가 에이전트 시대를 위해 설계된 AI 네이티브 그라운딩 API 모음인 'Web IQ'를 출시했다. Web IQ는 단순한 검색 엔진을 넘어, AI 에이전트가 실시간 웹 데이터를 바탕으로 추론하고 근거(Evidence)를 찾을 수 있도록 돕는 인프라다. 기존 빙(Bing)의 글로벌 인덱스를 기반으로 하되, 추론 시점의 그라운딩 요구 사항에 맞춰 아키텍처를 완전히 재설계했다.

## Key Claims

### 1. 에이전틱 워크플로를 위한 재설계
- 기존 검색이 단발성인 것과 달리, 에이전트는 반복적으로 검색하고 추론함.
- **레이턴시(Latency):** p95 기준 165ms 이하의 빠른 응답 속도 (기존 대비 약 2.5배 빠름).
- **지연 시간 예산(Latency Budget):** 다단계 추론(Multi-step reasoning)이 가능하도록 레이턴시를 극도로 압축.

### 2. 패시지(Passage) 단위의 정보 제공
- 문서(Document) 전체가 아닌, 정보 밀도가 높은 **패시지(Passage) 또는 구조화된 객체**를 반환.
- **토큰 효율성:** "Fewer tokens in, better answers out" 원칙. 모델에 전달하는 토큰 수를 줄이면서도 답변 품질을 높여 비용과 정밀도를 동시에 개선.

### 3. 기술적 기반
- **Bing Global Index:** 수십 년간 구축된 신뢰할 수 있고 신선한 글로벌 웹 인덱스 활용.
- **DiskANN:** 디스크 기반의 대규모 벡터 검색 기술을 통해 고성능 시맨틱 검색 수행.
- **임베딩 모델:** 마이크로소프트의 업계 선도적인 임베딩 모델을 통해 정보 공간의 정밀한 Neighborhood 검색 수행.

### 4. GDSAT (Grounding Satisfaction) 메트릭
- 단순 관련성 점수가 아닌, **완전성, 신선도, 권위성**을 종합적으로 측정하여 AI 그라운딩에 최적화된 품질 관리.

## 비즈니스 및 아키텍처 시사점

- **시스템 정합성:** 모델 단독 능력이 아닌, 모델과 세계(데이터)를 연결하는 전체 시스템의 효율성이 중요해짐.
- **에이전틱 웹(Agentic Web):** 미래의 웹 인프라는 인간의 검색뿐만 아니라 에이전트의 추론 환경을 지원하는 방향으로 진화할 것임.

## Concepts Linked

- [[microsoft-web-iq-announcement|원본 소스 (microsoft_web_iq_announcement.md)]]
- [Microsoft Web IQ 공식 페이지](https://aka.ms/WebIQ)

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/` evidence before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `partial` and ingest level is `light`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/` evidence when used for recommendations, metrics, or external-facing work.

## Citation

- Source record: `Microsoft Web IQ: AI-Native Grounding APIs`.
- Raw evidence: `raw/` evidence.

## Reliability Notes

- Coverage is `partial` and ingest level is `light`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/` evidence when used for recommendations, metrics, or external-facing work.

> [!warning] Caveats
> Reliability was not assessed in the earlier note. Treat this source as a prompt for exploration until raw evidence is checked.

## Design Implications

- Use this source to shape AI-agent workflow, toolchain, and automation prompts.
- Connect it with linked concepts before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** AI-agent workflow, toolchain, and automation prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `partial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
