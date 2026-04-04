# File review: AGENTS.md

**File reviewed:** `AGENTS.md`
**Date:** 2026-03-09
**Convention files used:**
- `contributing/conventions/agents/agents.md`

---

## Convention findings

### Section 2. Agent-neutral content

1. ~~**Line 32** — Section heading `## When editing \`.claude/skills/\`` names `.claude/`, which is Claude Code's proprietary configuration directory. The convention states: "Do not reference agent-specific configuration directories, file formats, or proprietary features." The heading should use an agent-neutral description (e.g., `## When editing agent skill files`).~~

### Section 3. Format and structure

1. ~~**Line 32** — Same heading `## When editing \`.claude/skills/\`` uses a Claude-specific path as its label. The convention states: "Agent-specific tools such as skill files are referenced via agent-neutral paths only." The path `.claude/skills/` is platform-specific and must not appear in the heading.~~

---

## TODOs

No TODOs found.

---

## Empty sections

No empty sections found.

---

## Summary

**Total findings: 2** (both on line 32, overlapping — one violation, two convention rules broken by the same heading).

The file is otherwise well-formed and agent-neutral. The only problem is the section heading `## When editing \`.claude/skills/\``, which names a Claude-specific directory in an agent-neutral file. Replacing it with a generic label (e.g., `## When editing agent skill files`) and keeping the agent-neutral path in the bullet body would resolve both findings.
