# Conventions for writing conventions

<h2>Table of contents</h2>

- [1. Numbered sections](#1-numbered-sections)
- [2. Table of contents](#2-table-of-contents)
- [3. DRY](#3-dry)
- [4. Hyperlinks when mentioning sections](#4-hyperlinks-when-mentioning-sections)
- [5. No Markdown tables](#5-no-markdown-tables)
- [6. Section link text](#6-section-link-text)
- [7. Agent-neutral language](#7-agent-neutral-language)

---

## 1. Numbered sections

All top-level sections must be numbered starting from 1.
Nested subsections use the format `S.N.` where S is the parent section number (e.g., `2.1.`, `2.2.`).

---

## 2. Table of contents

Each convention file must include a table of contents immediately after the title.
Use an HTML heading (`<h2>Table of contents</h2>`) instead of a Markdown `##` heading so the TOC entry does not appear inside its own list.
Follow the HTML heading with a blank line, then the TOC list.
The TOC list must be in Markdown format (bullet list with `- [Link](#anchor)` syntax).

---

## 3. DRY

Don't duplicate content across convention files. If a rule already exists in one file, reference it from others using a hyperlink instead of repeating it.

---

## 4. Hyperlinks when mentioning sections

When mentioning a section by name, always link to it. For sections in another file, include the file path in the link.

Good: `See [Section name](#section-name).`

Good (cross-file): `See [Section name](other-file.md#section-name).`

Bad: `See the Section name section.`

---

## 5. No Markdown tables

Never use Markdown tables in convention files. Use bullet lists instead — they are easier to read, write, and maintain.

---

## 6. Section link text

Don't include the section number in the link text when linking inline. Use only the section name.

In a table of contents, you may include the section number in the link text.

Good (inline): `[Section name](#323-section-name)`

Good (TOC): `[3.2.3. Section name](#323-section-name)`

Bad (inline): `[3.2.3. Section name](#323-section-name)`

---

## 7. Agent-neutral language

Convention files must not mention any specific AI agent by name (e.g., Claude, GPT, Gemini). Write so that any capable agent can follow the conventions.

- Write instructions in imperative mood, addressed directly to the agent:
  - Good: `Read the target file.`
  - Bad: `Ask Claude to read the target file.`
- When referring to the executor in third person, write "the agent":
  - Good: `If the path is missing, the agent must stop and ask the user.`
  - Bad: `If the path is missing, Claude must stop and ask the user.`
- The rule applies to all occurrences — including identifiers, scope names, and directory paths, not just instructional text:
  - Good: `agent` scope, `.agents/` directory
  - Bad: `claude` scope, `.claude/` directory
