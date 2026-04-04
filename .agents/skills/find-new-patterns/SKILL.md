---
name: find-new-patterns
description: Identify recurring patterns in tasks and wiki files that could become conventions
argument-hint: "[tasks|wiki|<path>]"
---

Scan `lab/tasks/` and/or `wiki/` files for recurring structural, formatting, or writing patterns that appear consistently across files but are not yet documented as conventions.

## Steps

1. Parse `$ARGUMENTS` to determine scope:
   - No argument → scan both `lab/tasks/` and `wiki/`
   - `tasks` → scan only `lab/tasks/`
   - `wiki` → scan only `wiki/`
   - A specific file path under `lab/tasks/` or `wiki/` → use that file's directory as the scope
   - If the argument is unrecognisable, ask the user.

2. List all `.md` files in the scope directories (recursively for `lab/tasks/`).

3. Read all convention files that apply to the scope:
   - Always read [`contributing/conventions/writing/common.md`](../../../contributing/conventions/writing/common.md)
   - If scope includes `lab/tasks/`: read [`contributing/conventions/writing/tasks.md`](../../../contributing/conventions/writing/tasks.md)
   - If scope includes `wiki/`: read [`contributing/conventions/writing/wiki.md`](../../../contributing/conventions/writing/wiki.md)

4. Read every `.md` file in the scope. For each file, note recurring elements:
   - **Structural patterns** — how sections, headings, or sub-sections are organised
   - **Formatting patterns** — how a particular element (command, note, image, link) is presented
   - **Writing patterns** — a fixed phrase, sentence starter, or wording template used consistently
   - **Content patterns** — a piece of information that is always included in a particular position (e.g., a "You should see…" line after a command)

5. Group identical or near-identical patterns across files. A pattern qualifies as a candidate if:
   - It appears in **2 or more files** (or 2 or more places in the same file if the scope is a single file), and
   - It is **not already covered** by any rule in the convention files read in step 3.

6. For each candidate pattern record:
   - **Name** — a short, descriptive label (e.g., "Post-step state check phrase", "Inline mini-ToC for methods")
   - **Occurrences** — file paths and approximate line numbers where the pattern appears
   - **Example** — one concrete excerpt showing the pattern as it appears in the files
   - **Gap** — which convention file and section is closest to this pattern, and what rule is missing
   - **Proposal** — one or two sentences describing what the convention rule would say if formalised

## Rules

- Do not flag patterns that are already described (even partially) in the convention files. Only flag genuine gaps.
- Do not flag patterns that appear only once across all scanned files — a single occurrence is not a pattern.
- Do not invent patterns. Only report what is actually present in the files.
- Be specific: quote a short excerpt (1–5 lines) to illustrate each candidate.
- Distinguish between patterns that are **consistent** (all occurrences look the same → strong candidate) and **near-consistent** (most occurrences look similar with minor variation → weaker candidate, note the variation).

## Output format

Write the report to `tmp/find-new-patterns/report.md`. Create intermediate directories if they do not exist.

Structure:

1. **Header** — scope scanned, date, convention files consulted, total files read.
2. **Candidate patterns** — one subsection per candidate, in descending order of occurrence count. Each subsection contains:
   - Occurrence count and file list
   - Example excerpt (fenced code block)
   - Gap: nearest existing convention and what it does not cover
   - Proposal: draft rule text
3. **Weak candidates** (near-consistent patterns) — same format, clearly labelled as requiring author judgement.
4. **Summary** — total strong candidates, total weak candidates, and a suggested priority order for formalising them.

After writing the file, print its path in the conversation so the user can find it.
