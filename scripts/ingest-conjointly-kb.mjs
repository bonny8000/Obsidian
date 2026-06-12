import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Defuddle } from "file:///C:/Users/bonny_chen/AppData/Roaming/npm/node_modules/defuddle/dist/node.js";
import { parseLinkedomHTML } from "file:///C:/Users/bonny_chen/AppData/Roaming/npm/node_modules/defuddle/dist/utils/linkedom-compat.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, "..");
const retrieved = "2026-06-08";
const tocUrl = "https://conjointly.com/kb/table-of-contents/";
const rawDir = path.join(root, "raw", "web", "conjointly-research-methods-kb");
const wikiSourcePath = path.join(root, "wiki", "sources", "conjointly-research-methods-kb.md");
const wikiMapPath = path.join(root, "wiki", "maps", "research-methods-knowledge-base.md");
const wikiConceptPath = path.join(root, "wiki", "concepts", "ux-research", "research-methods-foundations.md");
const indexPath = path.join(root, "wiki", "index.md");
const aiUxMapPath = path.join(root, "wiki", "maps", "ai-ux-research-methods.md");
const changeLogPath = path.join(root, "wiki", "logs", "change-log.md");
const manifestPath = path.join(rawDir, "manifest.json");

process.env.ALL_PROXY = "";
process.env.HTTP_PROXY = "";
process.env.HTTPS_PROXY = "";
process.env.GIT_HTTP_PROXY = "";
process.env.GIT_HTTPS_PROXY = "";

function decodeEntities(text) {
  return text
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">");
}

function cleanText(text) {
  return decodeEntities(text.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim());
}

function slugFromUrl(url) {
  const parsed = new URL(url);
  let parts = parsed.pathname.split("/").filter(Boolean);
  if (parts.length === 0) return "home";
  if (parts.length === 1 && parts[0] === "kb") return "kb-home";
  return parts.join("-").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function parseToc(html) {
  const start = html.indexOf("<div class=table-of-content-page>");
  const end = html.indexOf("</article>", start);
  if (start === -1 || end === -1) {
    throw new Error("Could not locate table-of-content-page in TOC HTML");
  }
  const tocHtml = html.slice(start, end);
  const tokenRe = /<ul\b[^>]*>|<\/ul>|<a\b([^>]*)>([\s\S]*?)<\/a>/gi;
  const items = [];
  let depth = -1;
  let match;
  while ((match = tokenRe.exec(tocHtml))) {
    const token = match[0].toLowerCase();
    if (token.startsWith("<ul")) {
      depth += 1;
      continue;
    }
    if (token.startsWith("</ul")) {
      depth -= 1;
      continue;
    }
    const attrs = match[1] || "";
    const hrefMatch = attrs.match(/href=(?:"([^"]*)"|'([^']*)'|([^\s>]+))/i);
    if (!hrefMatch) continue;
    let href = hrefMatch[1] || hrefMatch[2] || hrefMatch[3] || "";
    if (href.startsWith("/")) href = new URL(href, tocUrl).href;
    if (!href.startsWith("https://conjointly.com/kb/") && href !== "https://conjointly.com/legal/terms-and-conditions/") {
      continue;
    }
    const url = href.split("#")[0];
    const title = cleanText(match[2] || "");
    if (!title) continue;
    items.push({ title, url, depth: Math.max(0, depth) });
  }
  const seen = new Set();
  return items.filter((item) => {
    if (seen.has(item.url)) return false;
    seen.add(item.url);
    return true;
  }).map((item, index) => ({
    ...item,
    order: index + 1,
    slug: slugFromUrl(item.url),
    rawFile: `${String(index + 1).padStart(3, "0")}-${slugFromUrl(item.url)}.md`,
  }));
}

async function fetchText(url) {
  const response = await fetch(url, {
    headers: {
      "user-agent": "Mozilla/5.0 (compatible; LLM-Wiki local knowledge import)",
      "accept": "text/html,application/xhtml+xml",
    },
  });
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
  return response.text();
}

async function parsePage(item) {
  const html = await fetchText(item.url);
  const result = await Defuddle(parseLinkedomHTML(html), item.url, {
    markdown: true,
    separateMarkdown: true,
  });
  const content = (result.content || "").trim();
  if (!content) throw new Error("Defuddle returned empty content");
  return {
    ...item,
    extractedTitle: result.title || item.title,
    description: result.description || "",
    author: result.author || "Conjointly",
    site: result.site || "Conjointly",
    published: result.published || "",
    wordCount: result.wordCount || 0,
    parseTime: result.parseTime || 0,
    content,
  };
}

function rawMarkdown(page) {
  return `# Source Capture: ${page.extractedTitle}

URL: ${page.url}

Retrieved: ${retrieved}

Source collection: Conjointly Research Methods Knowledge Base

TOC title: ${page.title}

TOC order: ${page.order}

TOC depth: ${page.depth}

Author/site: ${page.author} / ${page.site}

Published: ${page.published || "Not stated"}

Word count: ${page.wordCount}

---

${page.content}
`;
}

function yamlList(items) {
  return items.map((item) => `  - ${item}`).join("\n");
}

function sourcePage(pages) {
  const pageRows = pages.map((page) => {
    const indent = "&nbsp;".repeat(page.depth * 2);
    const raw = `../../raw/web/conjointly-research-methods-kb/${page.rawFile}`;
    return `| ${page.order} | ${indent}${page.title.replace(/\|/g, "\\|")} | [raw](${raw}) | ${page.url} |`;
  }).join("\n");

  return `---
type: source
status: active
created: ${retrieved}
updated: ${retrieved}
tags: [research-methods, ux-research, methods, conjointly, trochim]
sources:
${yamlList(["raw/web/conjointly-research-methods-kb/manifest.json"])}
confidence: 0.9
---

# Conjointly Research Methods Knowledge Base

## Citation

Trochim, William M.K. The Research Methods Knowledge Base. Hosted by Conjointly. Captured from ${tocUrl} on ${retrieved}.

## Source Type

Hosted web knowledge base / book-style research methods reference.

## Location

- Raw captures: \`raw/web/conjointly-research-methods-kb/\`
- Manifest: \`raw/web/conjointly-research-methods-kb/manifest.json\`
- Page count captured: ${pages.length}

## Summary

This source collection is a broad research-methods reference covering foundations of research, sampling, measurement, validity, reliability, survey research, scaling, qualitative measures, unobtrusive measures, research design, experimental and quasi-experimental design, data analysis, and research write-up.

## Extracted Claims

- Research quality depends on matching the question, unit of analysis, design, measurement strategy, sampling frame, and analysis method.
- Validity is not one check; the KB separates construct, internal, external, and conclusion validity as different risk areas.
- Measurement requires attention to reliability, error, scale level, response format, wording, placement, and qualitative versus quantitative evidence.
- Experimental and quasi-experimental designs should be judged through causal inference risks, group equivalence, assignment, threats, and analysis fit.
- Research write-up is part of method quality because claims must be formatted, evidenced, and communicated clearly.

## Concepts Linked From This Source

- [[concepts/ux-research/research-methods-foundations|Research Methods Foundations]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/research-ethics|Research Ethics]]
- [[concepts/ux-research/ux-research-matrix|UX Research Matrix]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/maxdiff-prioritization|MaxDiff Prioritization]]

## Captured Pages

| # | TOC title | Raw capture | URL |
| --- | --- | --- | --- |
${pageRows}

## Reliability Notes

- Conjointly identifies the KB as Professor William M.K. Trochim's Research Methods Knowledge Base hosted by Conjointly.
- This capture used the TOC page as the link authority and Defuddle extraction for readable Markdown.
- The final TOC item is Conjointly's legal terms page; it was captured because it appears in the TOC appendix, but it is not treated as research-method evidence.
`;
}

function mapPage(pages) {
  const tocLines = pages.map((page) => {
    const indent = "  ".repeat(page.depth);
    const raw = `../../raw/web/conjointly-research-methods-kb/${page.rawFile}`;
    return `${indent}- ${page.title} - [raw](${raw})`;
  }).join("\n");
  const top = pages.filter((page) => page.depth === 0).map((page) => `| ${page.title} | ${page.url} |`).join("\n");

  return `---
type: map
status: active
created: ${retrieved}
updated: ${retrieved}
tags: [map, research-methods, ux-research, methodology]
sources:
  - sources/conjointly-research-methods-kb
confidence: 0.9
---

# Research Methods Knowledge Base

This map indexes the Conjointly-hosted Research Methods Knowledge Base capture and connects it to the LLM Wiki's UX research methodology layer.

## Source

- [[sources/conjointly-research-methods-kb|Conjointly Research Methods Knowledge Base]]
- Raw capture folder: \`raw/web/conjointly-research-methods-kb/\`
- Captured pages: ${pages.length}

## Top-Level Structure

| Section | URL |
| --- | --- |
${top}

## How To Use This Map

- Use Foundations, Sampling, Measurement, Design, Analysis, and Write-Up as the method backbone for evaluating AI-assisted research outputs.
- Use the validity pages as a checklist for whether a research claim is about measurement, causality, generalizability, or statistical conclusion risk.
- Use the survey, scaling, and qualitative-measures pages when designing or reviewing UX research instruments.
- Use the experimental and quasi-experimental design pages when judging whether a product experiment can support causal claims.

## Related Wiki Concepts

- [[concepts/ux-research/research-methods-foundations|Research Methods Foundations]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/ux-research-matrix|UX Research Matrix]]
- [[concepts/ux-research/research-ethics|Research Ethics]]

## Captured TOC

${tocLines}
`;
}

function conceptPage() {
  return `---
type: concept
status: active
created: ${retrieved}
updated: ${retrieved}
tags: [ux-research, research-methods, methodology, validity, measurement]
sources:
  - sources/conjointly-research-methods-kb
confidence: 0.85
---

# Research Methods Foundations

## Summary

Research methods foundations are the shared rules for turning questions into evidence: define the problem, choose a design, identify the unit of analysis, sample appropriately, measure constructs carefully, analyze with the right assumptions, and report claims with their limits.

## Why It Matters

AI-assisted UX research can accelerate drafting, synthesis, and analysis, but method quality still depends on validity, reliability, sampling, measurement, causal design, and clear write-up. The Conjointly/Trochim KB is useful as a baseline method reference for checking whether an AI-generated research output is making a claim it can actually support.

## Key Claims

- Research questions, hypotheses, variables, data types, and units of analysis need to be aligned before collection starts.
- Validity has multiple dimensions: construct validity for measurement, internal validity for causal inference, external validity for generalization, and conclusion validity for statistical inference.
- Reliability and measurement error matter because stable measurement is a prerequisite for strong interpretation, but reliability alone does not guarantee validity.
- Sampling choices determine who the evidence can reasonably represent.
- Survey design depends on question content, response format, wording, placement, and method selection.
- Experimental and quasi-experimental designs require explicit checks for assignment, equivalence, threats, and appropriate analysis.

## Related Concepts

- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/research-ethics|Research Ethics]]
- [[concepts/ux-research/ux-research-matrix|UX Research Matrix]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/ai-evals|AI Evals in Research]]

## Sources

- [[sources/conjointly-research-methods-kb|Conjointly Research Methods Knowledge Base]]
- [[maps/research-methods-knowledge-base|Research Methods Knowledge Base]]

## Open Questions

- Which parts of this methods baseline should become explicit evaluation rubrics for AI-generated UX research plans?
- Which Conjointly KB pages should be promoted into standalone concept notes after deeper reading?
`;
}

async function ensureDir(filePath) {
  await fs.mkdir(path.dirname(filePath), { recursive: true });
}

async function writeFile(filePath, content) {
  await ensureDir(filePath);
  await fs.writeFile(filePath, content, "utf8");
}

async function updateTextFile(filePath, transform) {
  const original = await fs.readFile(filePath, "utf8");
  const next = transform(original);
  if (next !== original) await fs.writeFile(filePath, next, "utf8");
}

function insertOnce(text, needle, insertion, fallbackAppend = false) {
  if (text.includes(insertion.trim())) return text;
  if (text.includes(needle)) return text.replace(needle, `${needle}${insertion}`);
  return fallbackAppend ? `${text}\n${insertion.trim()}\n` : text;
}

async function wireWiki() {
  await updateTextFile(indexPath, (text) => {
    let next = insertOnce(
      text,
      "> - [[maps/ai-ux-research-methods|AI UX Research Methods]]",
      "\n> - [[maps/research-methods-knowledge-base|Research Methods Knowledge Base]]",
    );
    next = insertOnce(
      next,
      "- [[concepts/ux-research/ux-research-matrix|UX Research Matrix]]",
      "\n- [[concepts/ux-research/research-methods-foundations|Research Methods Foundations]]",
    );
    return next;
  });

  await updateTextFile(aiUxMapPath, (text) => {
    let next = text;
    if (!next.includes("sources/conjointly-research-methods-kb")) {
      next = next.replace(
        "  - sources/cooper-about-face-4-2014\nconfidence:",
        "  - sources/cooper-about-face-4-2014\n  - sources/conjointly-research-methods-kb\nconfidence:",
      );
    }
    next = insertOnce(
      next,
      "- [[concepts/ux-research/ai-uxr-maturity-matrix|AI UXR Maturity Matrix]]",
      "\n- [[concepts/ux-research/research-methods-foundations|Research Methods Foundations]]",
    );
    next = insertOnce(
      next,
      "- [[sources/how-to-ai-uxr-2026|How To AI UXR: The ResearchOps Review (2026)]]",
      "\n- [[sources/conjointly-research-methods-kb|Conjointly Research Methods Knowledge Base]]",
    );
    next = insertOnce(
      next,
      "### Frameworks & Process Models\n",
      "- [[concepts/ux-research/research-methods-foundations|Research Methods Foundations]] *(Trochim / Conjointly KB)*\n",
    );
    return next;
  });

  await updateTextFile(changeLogPath, (text) => {
    const entry = `## ${retrieved} - Ingest: Conjointly Research Methods Knowledge Base

Source: \`raw/web/conjointly-research-methods-kb/\`

- Captured the Conjointly table-of-contents collection into raw Markdown files.
- Created \`wiki/sources/conjointly-research-methods-kb.md\` as the collection source page.
- Created \`wiki/maps/research-methods-knowledge-base.md\` as the navigable method map.
- Created \`wiki/concepts/ux-research/research-methods-foundations.md\` as the umbrella methodology concept.
- Updated \`wiki/maps/ai-ux-research-methods.md\` and \`wiki/index.md\` to link the new source and map.

    `;
    if (text.includes("Ingest: Conjointly Research Methods Knowledge Base")) return text;
    return text.replace(/# Change Log\r?\n\r?\n/, `# Change Log\n\n${entry}`);
  });
}

async function main() {
  await fs.mkdir(rawDir, { recursive: true });
  const tocHtml = await fetchText(tocUrl);
  const tocItems = parseToc(tocHtml);
  console.log(`Found ${tocItems.length} TOC links`);

  const pages = [];
  const failures = [];
  for (const item of tocItems) {
    const target = path.join(rawDir, item.rawFile);
    try {
      const page = await parsePage(item);
      await fs.writeFile(target, rawMarkdown(page), "utf8");
      pages.push({ ...page, content: undefined });
      console.log(`OK ${String(item.order).padStart(3, "0")} ${item.title}`);
    } catch (error) {
      failures.push({ ...item, error: error instanceof Error ? error.message : String(error) });
      console.error(`FAIL ${String(item.order).padStart(3, "0")} ${item.title}: ${failures.at(-1).error}`);
    }
  }

  const manifest = {
    source: "Conjointly Research Methods Knowledge Base",
    tocUrl,
    retrieved,
    pageCount: pages.length,
    failureCount: failures.length,
    pages: pages.map(({ order, depth, title, url, slug, rawFile, extractedTitle, description, wordCount, author, site, published }) => ({
      order,
      depth,
      title,
      url,
      slug,
      rawFile,
      extractedTitle,
      description,
      wordCount,
      author,
      site,
      published,
    })),
    failures,
  };
  await fs.writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");

  if (failures.length > 0) {
    console.error(`Import completed with ${failures.length} failures. Wiki pages were not written.`);
    process.exitCode = 1;
    return;
  }

  await writeFile(wikiSourcePath, sourcePage(pages));
  await writeFile(wikiMapPath, mapPage(pages));
  await writeFile(wikiConceptPath, conceptPage());
  await wireWiki();
  console.log(`Imported ${pages.length} pages and updated wiki source/map/concept files.`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
