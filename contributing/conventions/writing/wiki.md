# Wiki conventions — applies to `wiki/` only

- [1. Wiki documents (`wiki/`)](#1-wiki-documents-wiki)
  - [1.1. Purpose](#11-purpose)
  - [1.2. Naming](#12-naming)
  - [1.3. Structure of a wiki file](#13-structure-of-a-wiki-file)
  - [1.4. Key rules](#14-key-rules)
  - [1.5. Standard wiki topics to include](#15-standard-wiki-topics-to-include)
- [2. `vs-code.md` section structure pattern](#2-vs-codemd-section-structure-pattern)
- [3. Checklist before publishing](#3-checklist-before-publishing)

## 1. Wiki documents (`wiki/`)

### 1.1. Purpose

Wiki files are **reference documents** — one file per tool or concept. They are linked from task docs whenever a concept or operation is first mentioned.

### 1.2. Naming

- One file per tool/concept: `vs-code.md`, `git.md`, `docker.md`, `python.md`, `shell.md`, etc.
- Use lowercase with hyphens.

### 1.3. Structure of a wiki file

```markdown
# <Tool or Concept Name>

<h2>Table of contents</h2>

- [About `<tool or concept name>`](#about-tool-or-concept-name)
- [Section 2](#section-2)
- ...

## About `<tool or concept name>`

<1–3 sentences explaining what this tool or concept is and how it is used in this project.>

Docs:

- [Official docs](https://...)

## Section 2

<Explanation and/or step-by-step instructions.>

...
```

### 1.4. Key rules

- Each section is self-contained and linkable (task docs link to `wiki/<file>.md#<section>`).
- Start every wiki file with a `## About <tool, concept, procedure>` section that defines the tool/concept in 1–3 sentences and includes a link to official docs. The heading may use natural phrasing (articles, singular/plural) that differs from the H1 title — e.g., `# Computer Networks` → `## About computer networks`.
- Provide both explanation and how-to instructions.
- Link to other wiki sections whenever a concept appears for the first time in a section (see [Links and cross-references](./common.md#48-links-and-cross-references)).
- **Connect the dots.** Wiki files are often read in isolation — readers jump in from a task link. Don't just define a concept; situate it. Use cross-links and connecting wording (e.g., `` `X` works together with `Y` to… ``, `` When using `Z`, you will also need… ``) to help readers understand how concepts relate to each other and to the broader system.
- Use `<h2>Table of contents</h2>` (HTML) so the ToC heading itself doesn't appear in the auto-generated ToC.
- When a section has many sub-sections or steps, add a mini-ToC (see [Mini-ToC](./common.md#46-mini-toc)).
- When an operation can be done multiple ways, list them as options: "Use any of the following methods:"
- These wiki files must stay in sync with their corresponding source files — variable names, default values, and grouping must match:
  - `wiki/dotenv-docker-secret.md` ↔ `.env.docker.example`
  - `wiki/backend-dotenv-tests-unit-secret.md` ↔ `backend/.env.tests.unit.example`
  - `wiki/backend-dotenv-tests-e2e-secret.md` ↔ `backend/.env.tests.e2e.example`
  - `wiki/pyproject-toml.md` ↔ `pyproject.toml`
- Vendor instructions that aren't good enough anywhere else (e.g., rewrite unclear official docs).
- Provide fallback methods when one method may not work for all students.
- **Avoid sub-steps; use sections instead.** When a wiki step would need nested sub-steps, extract them into a separate subsection with its own flat step list. This keeps each section independently linkable and easier to follow.
- **Placeholder section titles** must use the format `` `<placeholder>` placeholder `` to avoid collision with the concept section of the same name. Example: a wiki file may have both `### Username` (explaining what a username is) and `` ### `<username>` placeholder `` (defining the placeholder). Without the word "placeholder" in the title, the two sections would collide.

### 1.5. Standard wiki topics to include

Depending on the lab, consider creating wiki files for:

- `vs-code.md` — VS Code basics: terminal, Command Palette, editor, extensions, layout.
- `git.md` — Git concepts: commits, branches, merging, rebasing.
- `git-vscode.md` — Git operations in VS Code: clone, commit, push, pull, switch branches.
- `git-workflow.md` — GitHub Flow-based git workflow for tasks and pull requests.
- `github.md` — GitHub: forks, issues, PRs, GitHub flow.
- `gitlens.md` — GitLens extension usage.
- `shell.md` — Shell basics: commands, arguments, environment variables.
- `bash.md` — Bash shell syntax basics and command execution patterns.
- `linux.md` — Linux basics: ports, processes, package management.
- `docker.md` — Docker concepts and container management.
- `docker-compose.md` — Docker Compose commands for multi-container orchestration.
- `docker-postgres.md` — PostgreSQL Docker container management and database reset.
- `environments.md` — Environment variables, `.env` files, secrets.
- `direnv.md` — Direnv setup for automatic environment variable loading per directory.
- `nix.md` — Nix package manager, nixpkgs, devshell, and flake configuration.
- `package-manager.md` — Package managers, tools, and dependencies overview.
- `ssh.md` — SSH setup and usage.
- `python.md` — Python, virtual environments, package managers (`uv`).
- `quality-assurance.md` — Quality assurance concepts, `pytest`, assertions.
- `http.md` — HTTP protocol, requests, responses, and status codes.
- `http-auth.md` — HTTP authentication via API keys and authorization.
- `database.md` — Database concepts, PostgreSQL, pgAdmin, SQL, and schema management.
- `sql.md` — SQL basics: SELECT, INSERT, WHERE statements.
- `pgadmin.md` — pgAdmin web interface for PostgreSQL database management.
- `swagger.md` — Swagger UI for interactive REST API exploration and testing.
- `caddy.md` — Caddy reverse proxy configuration and Caddyfile setup.
- `security.md` — API key authentication and security hardening.
- `file-system.md` — Files, directories, paths.
- `file-formats.md` — JSON, YAML, TOML, Markdown.
- `vm.md` — Virtual machines: creation, access, IP addresses.
- `vm-info.md` — VM base image information and preinstalled programs.
- `vm-hardening.md` — VM security hardening: firewall, fail2ban, SSH configuration.
- `operating-system.md` — OS concepts.
- `computer-networks.md` — Networking basics.
- `architectural-views.md` — PlantUML component, sequence, and deployment diagrams.
- `visualize-architecture.md` — Draw.io, PlantUML, and Mermaid for architecture diagrams.
- `coding-agents.md` — LLM-based coding agents setup and configuration.
- `useful-programs.md` — Command-line tools: curl, jq, find, ripgrep.

----

## 2. `vs-code.md` section structure pattern

Each section in `vs-code.md` should follow this pattern (other wiki files use the simpler "About" + "Docs:" structure described above):

```markdown
## <Feature Name>

<1-2 sentence explanation.>

Location: see [`Basic Layout`](#basic-layout).

Docs:

- [Official docs link](https://...)

Actions:

- [Action 1](#action-1)
- [Action 2](#action-2)

### Action 1

<Step-by-step instructions.>
```

This provides: what it is, where to find it, official docs, and how to use it.

----

## 3. Checklist before publishing

**Always required:**

- [ ] `README.md` has: story, learning advice, learning outcomes, task list.
- [ ] Every task file has: Time, Purpose, Context, ToC, Steps, Acceptance criteria.
- [ ] Every terminal command uses the "To…" intention pattern with a `` [run in the `VS Code Terminal`] `` link.
- [ ] Every Command Palette command has a `` [Run using the `Command Palette`] `` link prefix.
- [ ] All cross-references use relative paths and are valid.
- [ ] Wiki docs exist for every tool/concept linked from tasks.
- [ ] Issue templates (`01-task.yml`, `02-bug-report.yml`) are configured.
- [ ] PR template has a checklist.
- [ ] `.vscode/settings.json` and `.vscode/extensions.json` are configured.
- [ ] `.gitignore` excludes generated files and secrets for the lab's ecosystem.
- [ ] Ordered lists use `1. 2. 3.` (not `1. 1. 1.`).
- [ ] Compound instructions are split into separate steps.
- [ ] All sentences end with `.`.
- [ ] Each sentence is on its own line.
- [ ] Options and steps are clearly differentiated.
- [ ] Tool/concept names are wrapped in backticks: `` `VS Code` ``, `` `Git` ``, `` `Docker` ``.
- [ ] `Git workflow` is referenced from tasks that produce code changes.
- [ ] Acceptance criteria are concrete and verifiable.
- [ ] Commit message format is documented (conventional commits).
- [ ] Setup instructions cover: fork, clone, install tools, configure environment.
- [ ] Branch protection rules are documented.
- [ ] Partner/collaborator setup is documented.
- [ ] Diagrams use `.drawio.svg` format.
- [ ] `<!-- TODO -->` markers exist for unfinished sections.

**Conditional (include when applicable):**

- [ ] `.env.example` files are provided; `.env.secret` files are gitignored (if the lab uses environment variables).
- [ ] Wiki files are in sync with their corresponding source files — variable names, defaults, and grouping match (if the lab has dotenv or pyproject-toml wiki pages):
  - `wiki/dotenv-docker-secret.md` ↔ `.env.docker.example`
  - `wiki/backend-dotenv-tests-unit-secret.md` ↔ `backend/.env.tests.unit.example`
  - `wiki/backend-dotenv-tests-e2e-secret.md` ↔ `backend/.env.tests.e2e.example`
  - `wiki/pyproject-toml.md` ↔ `pyproject.toml`
- [ ] `.dockerignore` excludes tests, docs, `.git/`, build caches, markdown files (if the lab uses Docker).
- [ ] At least one test intentionally fails for the debugging task (if the lab has a testing/debugging task).
- [ ] Task runner commands are documented in the config file (if the lab uses a task runner).
- [ ] Seed project has three tiers: reference (working), debug (commented out with bugs), implement (placeholder templates) (if the lab uses the seed project pattern).
- [ ] Placeholder templates include `# Reference:` comments mapping new resources to reference counterparts (if the lab uses placeholder-based implementation).
- [ ] All tasks are completable without LLMs.
- [ ] Docker images use an institutional container registry (if the lab uses Docker in an institutional setting).
- [ ] API key or auth mechanism is set via environment variable and encountered naturally during exploration (if the lab includes security).
