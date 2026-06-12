#!/usr/bin/env python3
"""Backfill source pages with LLM-ready metadata and sections.

Run from the vault root or directly from scripts/. The script is conservative:
it standardizes source records and marks coverage honestly, but it does not
pretend a thin source note has been deeply re-read.
"""
from __future__ import annotations

import datetime as _dt
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "wiki" / "sources"
MAP_PATH = ROOT / "wiki" / "maps" / "llm-ready-source-index.md"
TODAY = _dt.date.today().isoformat()

REQUIRED_HEADINGS = [
    "Citation",
    "Summary",
    "Key Claims",
    "Useful Examples",
    "Constraints / Caveats",
    "Design Implications",
    "Tensions",
    "Open Questions",
    "Concepts Linked",
    "LLM Use",
    "Reliability Notes",
    "Backfill Status",
]


def split_frontmatter(text: str) -> tuple[list[str], str]:
    if not text.startswith("---\n"):
        return [], text
    end = text.find("\n---", 4)
    if end == -1:
        return [], text
    fm = text[4:end].splitlines()
    body = text[end + len("\n---") :].lstrip("\n")
    return fm, body


def join_frontmatter(fm: list[str], body: str) -> str:
    return "---\n" + "\n".join(fm).rstrip() + "\n---\n\n" + body.lstrip("\n").rstrip() + "\n"


def get_prop(fm: list[str], name: str) -> str | None:
    prefix = f"{name}:"
    for line in fm:
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return None


def set_prop(fm: list[str], name: str, value: str) -> list[str]:
    prefix = f"{name}:"
    out = []
    for line in fm:
        if not line.startswith(prefix):
            out.append(line)

    insert_at = None
    for i, line in enumerate(out):
        if line.startswith("confidence:"):
            insert_at = i
            break
    if insert_at is None:
        out.append(f"{name}: {value}")
    else:
        out.insert(insert_at, f"{name}: {value}")
    return out


def normalize_heading(title: str) -> str:
    plain = title.strip().strip("#").strip()
    plain_no_emoji = re.sub(r"^[^\w\[\]가-힣一-龥]+", "", plain).strip()
    lower = plain_no_emoji.lower()

    if "citation" in lower:
        return "Citation"
    if "summary" in lower or plain_no_emoji in {"요약", "摘要"}:
        return "Summary"
    if "claim" in lower or "성공 비결" in plain_no_emoji or "핵심" in plain_no_emoji:
        return "Key Claims"
    if "useful example" in lower or lower == "examples":
        return "Useful Examples"
    if "constraint" in lower or "caveat" in lower:
        return "Constraints / Caveats"
    if "design implication" in lower:
        return "Design Implications"
    if "tension" in lower:
        return "Tensions"
    if "open question" in lower:
        return "Open Questions"
    if "concept" in lower or "관련 링크" in plain_no_emoji:
        return "Concepts Linked"
    if "llm use" in lower:
        return "LLM Use"
    if "reliability" in lower:
        return "Reliability Notes"
    if "backfill status" in lower:
        return "Backfill Status"
    if "비즈니스 시사점" in plain_no_emoji:
        return "Design Implications"
    return plain_no_emoji


def normalize_headings(body: str) -> str:
    lines = []
    for line in body.splitlines():
        match = re.match(r"^(##+)\s+(.+?)\s*$", line)
        if match and match.group(1) == "##":
            lines.append("## " + normalize_heading(match.group(2)))
        else:
            lines.append(line)
    return "\n".join(lines).rstrip() + "\n"


def headings(body: str) -> set[str]:
    found = set()
    for match in re.finditer(r"^##\s+(.+?)\s*$", body, re.M):
        found.add(match.group(1).strip())
    return found


def dedupe_lines(text: str) -> str:
    lines = []
    seen = set()
    for line in text.splitlines():
        marker = line.strip()
        if marker and marker in seen:
            continue
        if marker:
            seen.add(marker)
        lines.append(line)
    return "\n".join(lines).strip()


def merge_duplicate_sections(body: str) -> str:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", body, re.M))
    if not matches:
        return body.rstrip() + "\n"

    preamble = body[: matches[0].start()].rstrip()
    sections: list[tuple[str, str]] = []
    by_heading: dict[str, int] = {}

    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        content = body[start:end].strip()
        if heading in by_heading:
            section_index = by_heading[heading]
            old_heading, old_content = sections[section_index]
            merged = dedupe_lines((old_content + "\n\n" + content).strip())
            sections[section_index] = (old_heading, merged)
        else:
            by_heading[heading] = len(sections)
            sections.append((heading, content))

    parts = [preamble] if preamble else []
    for heading, content in sections:
        parts.append(f"## {heading}\n\n{content}" if content else f"## {heading}")
    return "\n\n".join(parts).rstrip() + "\n"


def first_h1(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    return match.group(1).strip() if match else fallback


def section_text(body: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.M)
    match = pattern.search(body)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^##\s+", body[start:], re.M)
    end = start + next_match.start() if next_match else len(body)
    return body[start:end].strip()


def strip_generated_sections(body: str) -> str:
    generated = {
        "Useful Examples",
        "Constraints / Caveats",
        "Design Implications",
        "Tensions",
        "Open Questions",
        "LLM Use",
        "Backfill Status",
    }
    parts: list[str] = []
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", body, re.M))
    if not matches:
        return body
    first = matches[0]
    parts.append(body[: first.start()])
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        if heading not in generated:
            parts.append(body[match.start() : end])
    return "\n".join(part.rstrip() for part in parts if part.strip()) + "\n"


def wiki_concepts(body: str) -> list[str]:
    seen = []
    for match in re.finditer(r"\[\[(concepts/[^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", body):
        target = match.group(1)
        if target not in seen:
            seen.append(target)
    return seen


def raw_refs(text: str) -> list[str]:
    refs = []
    for match in re.finditer(r"(raw/[A-Za-z0-9_\-./%()]+)", text):
        ref = match.group(1).rstrip(").,`")
        if ref not in refs:
            refs.append(ref)
    return refs


def infer_metadata(path: Path, fm: list[str], body: str, original_body: str) -> dict[str, object]:
    title = first_h1(body, path.stem)
    classification_body = strip_generated_sections(body)
    source_text = "\n".join(fm) + "\n" + classification_body
    concept_links = wiki_concepts(body)
    raw = raw_refs(source_text)
    has_summary = "Summary" in headings(body) and len(section_text(body, "Summary")) > 40
    has_claims = "Key Claims" in headings(body) and "-" in section_text(body, "Key Claims")
    has_concepts = bool(concept_links)
    has_reliability = "Reliability Notes" in headings(body)
    raw_preserved = bool(raw) or bool(re.search(r"^\s+-\s+raw/", "\n".join(fm), re.M))

    lower = source_text.lower()
    deep_signals = [
        "deep ingest",
        "deep-ingested",
        "page count captured",
        "chapter structure",
        "transcript",
        "pdf",
        "book",
        "source family",
        "knowledge base",
        "captured pages",
    ]
    if any(signal in lower for signal in deep_signals) or len(classification_body) > 3500:
        ingest_level = "deep"
    elif has_summary and has_claims and (has_concepts or raw_preserved):
        ingest_level = "standard"
    else:
        ingest_level = "light"

    if ingest_level == "deep" and raw_preserved and ("captured pages" in lower or "page count captured" in lower):
        coverage = "full"
    elif ingest_level in {"deep", "standard"} and raw_preserved and len(classification_body) > 1200:
        coverage = "substantial"
    else:
        coverage = "partial"

    llm_ready = bool(has_summary and has_claims and has_concepts and has_reliability and coverage != "partial")

    return {
        "title": title,
        "concepts": concept_links,
        "raw_refs": raw,
        "has_summary": has_summary,
        "has_claims": has_claims,
        "has_concepts": has_concepts,
        "has_reliability": has_reliability,
        "raw_preserved": raw_preserved,
        "ingest_level": ingest_level,
        "coverage": coverage,
        "llm_ready": llm_ready,
        "deepening_focus": deepening_focus(coverage, raw_preserved, has_claims, has_concepts, has_reliability),
    }


def deepening_focus(
    coverage: str,
    raw_preserved: bool,
    has_claims: bool,
    has_concepts: bool,
    has_reliability: bool,
) -> str:
    focus = []
    if not raw_preserved:
        focus.append("raw provenance")
    if coverage == "partial":
        focus.append("raw-based expansion")
    if not has_claims:
        focus.append("claims")
    if not has_concepts:
        focus.append("concept links")
    if not has_reliability:
        focus.append("reliability")
    if not focus:
        return "ready for grounded ideation"
    return ", ".join(focus)


def source_domain_hint(fm: list[str], body: str) -> str:
    haystack = ("\n".join(fm) + "\n" + body).lower()
    if "ux-research" in haystack or "research" in haystack or "usability" in haystack:
        return "research design, UX evidence, method selection, and evaluation prompts"
    if "product-management" in haystack or "roadmap" in haystack or "pm" in haystack:
        return "product strategy, roadmap framing, operating model, and prioritization prompts"
    if "robot" in haystack or "hardware" in haystack or "spatial" in haystack:
        return "hardware, robotics, spatial computing, and embodied-AI product prompts"
    if "agent" in haystack or "claude" in haystack or "gemini" in haystack or "codex" in haystack:
        return "AI-agent workflow, toolchain, and automation prompts"
    if "design" in haystack or "figma" in haystack or "typography" in haystack:
        return "design-system, design automation, and UI-quality prompts"
    return "idea generation, source-grounded comparison, and follow-up research prompts"


def insert_before_reliability(body: str, block: str) -> str:
    match = re.search(r"^##\s+Reliability Notes\s*$", body, re.M)
    if not match:
        return body.rstrip() + "\n\n" + block.strip() + "\n"
    return body[: match.start()].rstrip() + "\n\n" + block.strip() + "\n\n" + body[match.start() :].lstrip()


def missing_section_block(heading: str, meta: dict[str, object], fm: list[str], body: str) -> str:
    concepts = meta["concepts"]  # type: ignore[index]
    raw = meta["raw_refs"]  # type: ignore[index]
    concept_sample = ", ".join(f"[[{c}]]" for c in concepts[:4]) if concepts else "linked concepts"
    raw_sample = ", ".join(f"`{r}`" for r in raw[:3]) if raw else "`raw/` evidence"
    domain = source_domain_hint(fm, body)

    if heading == "Citation":
        return (
            "## Citation\n\n"
            f"- Source record: `{meta['title']}`.\n"
            f"- Raw evidence: {raw_sample}."
        )
    if heading == "Summary":
        return "## Summary\n\n- Backfill note: no standalone summary was present before the LLM-ready upgrade. Re-read the raw source before using this as decision evidence."
    if heading == "Key Claims":
        return "## Key Claims\n\n- Backfill note: no explicit claims were extracted before this upgrade. Promote claims from the raw source during a standard or deep ingest pass."
    if heading == "Useful Examples":
        return f"## Useful Examples\n\n- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to {raw_sample} before asking an LLM for concrete examples."
    if heading == "Constraints / Caveats":
        return f"## Constraints / Caveats\n\n- Coverage is `{meta['coverage']}` and ingest level is `{meta['ingest_level']}`; do not treat this source as fully digested unless `coverage: full`.\n- Claims should be checked against {raw_sample} when used for recommendations, metrics, or external-facing work."
    if heading == "Design Implications":
        return f"## Design Implications\n\n- Use this source to shape {domain}.\n- Connect it with {concept_sample} before turning it into a project recommendation."
    if heading == "Tensions":
        return "## Tensions\n\n- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled."
    if heading == "Open Questions":
        return "## Open Questions\n\n- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?\n- Which linked concept would change most if this source were contradicted?"
    if heading == "Concepts Linked":
        return "## Concepts Linked\n\n- Backfill note: no concept links were present before this upgrade. Add links during the next standard or deep ingest pass."
    if heading == "LLM Use":
        return (
            "## LLM Use\n\n"
            f"- **Use for:** {domain}.\n"
            f"- **Do not use for:** unsupported exact claims beyond the source note's `{meta['coverage']}` coverage.\n"
            "- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use."
        )
    if heading == "Reliability Notes":
        return "## Reliability Notes\n\n> [!warning] Caveats\n> Reliability was not assessed in the earlier note. Treat this source as a prompt for exploration until raw evidence is checked."
    if heading == "Backfill Status":
        return (
            "## Backfill Status\n\n"
            f"- Retrofitted on {TODAY} by `scripts/backfill_llm_ready.py` from the existing source note.\n"
            "- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read."
        )
    raise ValueError(heading)


def ensure_sections(fm: list[str], body: str, meta: dict[str, object]) -> str:
    body = merge_duplicate_sections(body)
    current = headings(body)
    additions = []
    for heading in REQUIRED_HEADINGS:
        if heading not in current:
            additions.append(missing_section_block(heading, meta, fm, body))
    if not additions:
        if "Backfill Status" in current:
            return body
        additions.append(missing_section_block("Backfill Status", meta, fm, body))
    return insert_before_reliability(body, "\n\n".join(additions))


def update_source(path: Path) -> dict[str, object]:
    original = path.read_text(encoding="utf-8-sig")
    fm, body = split_frontmatter(original)
    if not fm:
        fm = [
            "type: source",
            "status: active",
            f"created: {TODAY}",
            f"updated: {TODAY}",
            "tags: [source]",
            "sources: []",
            "confidence: 0.6",
        ]
    normalized_body = normalize_headings(body)
    meta = infer_metadata(path, fm, normalized_body, normalize_headings(body))

    fm = set_prop(fm, "updated", TODAY)
    fm = set_prop(fm, "ingest_level", str(meta["ingest_level"]))
    fm = set_prop(fm, "coverage", str(meta["coverage"]))
    fm = set_prop(fm, "llm_ready", "true" if meta["llm_ready"] else "false")
    fm = set_prop(fm, "raw_preserved", "true" if meta["raw_preserved"] else "false")

    new_body = ensure_sections(fm, normalized_body, meta)
    new_text = join_frontmatter(fm, new_body)
    if new_text != original:
        path.write_text(new_text, encoding="utf-8", newline="\n")

    return {
        "file": path.name,
        "stem": path.stem,
        "title": meta["title"],
        "ingest_level": meta["ingest_level"],
        "coverage": meta["coverage"],
        "llm_ready": meta["llm_ready"],
        "raw_preserved": meta["raw_preserved"],
        "deepening_focus": meta["deepening_focus"],
    }


def generate_index(rows: list[dict[str, object]]) -> None:
    ready = sum(1 for r in rows if r["llm_ready"])
    deep = sum(1 for r in rows if r["ingest_level"] == "deep")
    standard = sum(1 for r in rows if r["ingest_level"] == "standard")
    light = sum(1 for r in rows if r["ingest_level"] == "light")
    partial = sum(1 for r in rows if r["coverage"] == "partial")

    lines = [
        "---",
        "type: map",
        "status: active",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "tags: [map, llm-ready, source-index]",
        "sources: []",
        "confidence: 1.0",
        "---",
        "",
        "# LLM-Ready Source Index",
        "",
        "This map tracks whether source pages are ready to support LLM-assisted ideation, synthesis, and decision drafting.",
        "",
        "## Status Summary",
        "",
        f"- Total source pages: {len(rows)}",
        f"- LLM-ready source pages: {ready}",
        f"- Deep / standard / light: {deep} / {standard} / {light}",
        f"- Partial coverage sources needing deeper ingest: {partial}",
        "",
        "## How to Use",
        "",
        "- Prefer `llm_ready: true` and `coverage: substantial` or `coverage: full` when asking an LLM for grounded ideation.",
        "- Use `light` or `partial` sources for exploration only, then return to raw evidence before making decisions.",
        "- Promote sources by filling examples, caveats, tensions, open questions, and concept links from the raw material.",
        "",
        "## Source Readiness Table",
        "",
        "| Source | Level | Coverage | LLM ready | Raw preserved | Deepening focus |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(rows, key=lambda r: (str(r["ingest_level"]), str(r["file"]))):
        link = f"[[sources/{row['stem']}|{row['title']}]]"
        lines.append(
            f"| {link} | `{row['ingest_level']}` | `{row['coverage']}` | `{str(row['llm_ready']).lower()}` | `{str(row['raw_preserved']).lower()}` | {row['deepening_focus']} |"
        )

    MAP_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    rows = []
    for path in sorted(SOURCE_DIR.glob("*.md")):
        rows.append(update_source(path))
    generate_index(rows)
    print(f"sources: {len(rows)}")
    print(f"llm_ready: {sum(1 for r in rows if r['llm_ready'])}")
    print(f"index: {MAP_PATH.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
