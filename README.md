# LLM-Wiki Vault

This is a local Obsidian vault set up for an LLM Wiki workflow.

Everything for this vault lives on the D: drive. Open this folder in Obsidian:

```text
D:\Obsidian\LLM-Wiki
```

All raw sources, wiki pages, scripts, and logs are kept under `D:\Obsidian\LLM-Wiki`. Do not create or sync a copy under `C:\Users\bonny_chen` — work directly against the D: drive path.

Basic use:

1. Put source files, web clippings, PDFs, transcripts, or notes into `raw/`.
2. Ask Codex or Claude Code to ingest the new source.
3. Read the compiled wiki in `wiki/` through Obsidian.
4. Use Obsidian graph view to inspect links between concepts.

Useful agent prompts:

```text
Ingest everything new in raw/ into the wiki.
```

```text
Query the wiki: what are the main design implications of LLM Wiki?
```

```text
Lint the wiki and fix low-risk issues.
```

```text
Create a topic map for the current wiki.
```

