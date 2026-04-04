---
name: find-empty-sections
description: Find markdown headings with no content below them
argument-hint: "[path]"
---

Find all headings in markdown files that have no content — i.e. a heading immediately followed by another heading, a `<!-- TODO -->` comment, or end of file, with no real content lines in between.

## Rules

- Search in `$ARGUMENTS` if provided; otherwise search in `wiki/`.
- Use a Bash script to detect empty sections. A section is empty if no non-blank, non-heading lines appear between its heading and the next heading (or EOF). A `<!-- TODO ... -->` comment alone does not count as content.
- Output results in the format `file.md:line: ## Section Name`, one per line.
- Group results by file.
- After the list, print a summary: total count and which files are most affected.
