# Skill conventions

Skills are agent-executable instruction files stored in `.agents/skills/`.
Each skill defines a repeatable task that any capable coding agent can follow.
The format follows the [Agent Skills specification](https://agentskills.io/specification).

## Directory structure

`.agents/` is the canonical directory. Agent-specific directories such as
`.claude/` and `.qwen/` are symlinks to `.agents/`; edit only files inside
`.agents/`.

A skill is a directory containing at minimum a `SKILL.md` file:

```
.agents/skills/<skill-name>/
├── SKILL.md          # Required
├── scripts/          # Optional — executable scripts the agent can run
├── references/       # Optional — additional documentation loaded on demand
└── assets/           # Optional — templates, images, data files
```

Keep `references/` files focused. The agent loads them on demand, so smaller
files consume less context.

## Frontmatter

Every `SKILL.md` begins with a YAML frontmatter block between `---` delimiters.

### Required fields

- `name` — must match the directory name; lowercase letters, digits, and
  hyphens only; no leading, trailing, or consecutive hyphens; max 64 characters
- `description` — describes what the skill does **and when to use it**;
  include specific keywords that help an agent identify relevant tasks;
  max 1024 characters

Good `description`:

```yaml
description: >
  Fix convention violations in a lab task or wiki file using the report
  produced by review-file. Use when a review report exists
  and you want to apply the fixes automatically.
```

Poor `description` (too vague, no trigger cues):

```yaml
description: Fixes files.
```

### Optional standard fields

- `license` — license name or reference to a bundled license file
- `compatibility` — environment requirements (intended tool, required system
  packages, network access); omit if the skill has no special requirements
- `metadata` — arbitrary key-value map for additional properties
- `allowed-tools` — space-delimited list of pre-approved tools (experimental)

### Optional implementation-specific fields

Some agent products extend the frontmatter with their own fields. These are
not part of the Agent Skills standard and are ignored by other agents:

- `argument-hint` — shows expected argument syntax (e.g., `<path>`)
- `disable-model-invocation` — `true` for skills that do not require
  model inference

## Body structure

The body follows the frontmatter in this order:

1. **Opening sentence** — one sentence stating what the skill does; not a
   restatement of the `description` field
2. **[Steps](#steps)** — always present; numbered list of actions to follow
3. **[Rules](#rules)** — optional; hard constraints that apply throughout
4. **[Output](#output)** — describes what the skill produces

Keep `SKILL.md` under 500 lines. Move detailed reference material to
`references/` and link to it from the body.

## Agent-neutral language

Skill files must not mention any specific AI agent by name (e.g., Claude,
GPT, Gemini). Write so that any capable agent can execute the skill.

- Write steps in imperative mood, addressed directly to the agent:
  - Good: `Read the target file.`
  - Bad: `Ask Claude to read the target file.`
- When referring to the executor in third person, write "the agent":
  - Good: `If the path is missing, the agent must stop and ask the user.`
  - Bad: `If the path is missing, Claude must stop and ask the user.`

## Steps

- Use a numbered list; each item is one clear, imperative action
- Reference files by their exact path from the repository root
- When referencing a convention file, use a markdown link rather than a
  bare path. Good: `[Read the conventions.](../../../contributing/conventions/writing/common.md)`.
  Bad: `Read contributing/conventions/writing/common.md.`
- Validate `$ARGUMENTS` in the **first step**; if input is invalid or
  missing, tell the user and stop

## Rules

Use the Rules section for constraints that do not fit naturally inside a
single step — for example, scope limits, prohibitions, or fallback behaviour.
Each rule is a separate bullet.

Omit the Rules section when all constraints fit naturally inside the
[Steps](#steps).

## Output

Specify:

- The exact path or path pattern of any files written, relative to the
  repository root
- What to print in the conversation after the skill completes (e.g., the
  written file path, a one-line summary count)
