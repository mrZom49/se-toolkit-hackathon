# AGENTS.md conventions

<h2>Table of contents</h2>

- [1. Purpose](#1-purpose)
- [2. Agent-neutral content](#2-agent-neutral-content)
- [3. Format and structure](#3-format-and-structure)

---

## 1. Purpose

`AGENTS.md` is the canonical instruction file for AI coding agents working in the repository.
It follows the [agents.md open specification](https://agents.md/), which defines a predictable,
agent-independent format recognised across all major AI coding platforms.

---

## 2. Agent-neutral content

`AGENTS.md` must not mention any specific AI agent by name (e.g., Claude, Copilot, Codex, Gemini).

- Write instructions that any capable coding agent can follow.
- Do not reference agent-specific configuration directories, file formats, or proprietary features.
- Use "the agent" when referring to the executor in third person.

Agent-specific instructions belong in the respective agent's configuration directory
(e.g., `.agents/` for Claude Code, `.github/copilot-instructions.md` for Copilot), not in `AGENTS.md`.

---

## 3. Format and structure

Follow the [agents.md specification](https://agents.md/):

- Use standard Markdown; no required headings or fields are mandated by the spec.
- Focus on what agents need to act: build steps, test commands, code style, and conventions.
- For monorepos, a nested `AGENTS.md` in a subdirectory takes precedence over the root file for that subtree.
- Agent-specific tools such as skill files are referenced via agent-neutral paths only; do not embed tool invocation syntax that is specific to one platform.
