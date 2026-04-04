# Repo index

<h2>Table of contents</h2>

- [Lab tasks](#lab-tasks)
  - [Full setup](#full-setup)
  - [Git workflow](#git-workflow)
- [Application source](#application-source)
- [Infrastructure](#infrastructure)
- [Wiki](#wiki)
  - [Architectural views](#architectural-views)
  - [`Caddy`](#caddy)
  - [Coding agents](#coding-agents)
  - [Networks](#networks)
  - [Database](#database)
  - [`Docker`](#docker)
  - [`Docker Compose`](#docker-compose)
  - [Environments](#environments)
  - [File formats](#file-formats)
  - [File system](#file-system)
  - [`Git`](#git)
  - [`Git` in `VS Code`](#git-in-vs-code)
  - [`GitHub`](#github)
  - [`GitLens`](#gitlens)
  - [`HTTP`](#http)
  - [`Linux`](#linux)
  - [Operating system (OS)](#operating-system-os)
  - [`pgAdmin`](#pgadmin)
  - [`Python`](#python)
  - [Security](#security)
  - [Shell](#shell)
  - [`SSH`](#ssh)
  - [Swagger](#swagger)
  - [Quality assurance](#quality-assurance)
  - [Useful programs](#useful-programs)
  - [Visualize the architecture](#visualize-the-architecture)
  - [VM](#vm)
  - [Your VM image](#your-vm-image)
  - [`VS Code`](#vs-code)

## Lab tasks

### [Full setup](./lab/setup/setup-full.md)

Required and optional steps to get the environment ready: fork, clone, install tools, start services.

### [Git workflow](./wiki/git-workflow.md)

Branching, committing, opening PRs, and the review process used throughout the lab.

## Application source

Entry point and configuration:

- [`backend/src/lms_backend/main.py`](backend/src/lms_backend/main.py) — FastAPI app creation and router registration.
- [`backend/src/lms_backend/settings.py`](backend/src/lms_backend/settings.py) — environment-based configuration.
- [`backend/src/lms_backend/auth.py`](backend/src/lms_backend/auth.py) — API key authentication dependency.
- [`backend/src/lms_backend/database.py`](backend/src/lms_backend/database.py) — database session setup.
- [`backend/src/lms_backend/run.py`](backend/src/lms_backend/run.py) — entry point for running the server.

Routers (HTTP endpoints):

- [`backend/src/lms_backend/routers/items.py`](backend/src/lms_backend/routers/items.py)
- [`backend/src/lms_backend/routers/interactions.py`](backend/src/lms_backend/routers/interactions.py)
- [`backend/src/lms_backend/routers/learners.py`](backend/src/lms_backend/routers/learners.py)

Models (Pydantic schemas):

- [`backend/src/lms_backend/models/item.py`](backend/src/lms_backend/models/item.py)
- [`backend/src/lms_backend/models/interaction.py`](backend/src/lms_backend/models/interaction.py)
- [`backend/src/lms_backend/models/learner.py`](backend/src/lms_backend/models/learner.py)

Database queries:

- [`backend/src/lms_backend/db/items.py`](backend/src/lms_backend/db/items.py)
- [`backend/src/lms_backend/db/interactions.py`](backend/src/lms_backend/db/interactions.py)
- [`backend/src/lms_backend/db/learners.py`](backend/src/lms_backend/db/learners.py)

Database seed:

- [`backend/src/lms_backend/data/init.sql`](backend/src/lms_backend/data/init.sql) — initial schema and data loaded on first `PostgreSQL` start.

## Infrastructure

- [`docker-compose.yml`](docker-compose.yml) — defines the `backend`, `postgres`, `pgadmin`, and `caddy` services.
- [`backend/Dockerfile`](backend/Dockerfile) — builds the application container image.
- [`caddy/Caddyfile`](caddy/Caddyfile) — reverse proxy configuration.
- [`.env.docker.example`](.env.docker.example) — template for container environment variables.
- [`pyproject.toml`](pyproject.toml) — Python project metadata and dependencies.

## Wiki

### [Architectural views](./wiki/architectural-views.md)

Component, sequence, and deployment diagram types used to document the system architecture.

### [`Caddy`](./wiki/caddy.md)

A web server and reverse proxy configured via a `Caddyfile`.

### [Coding agents](./wiki/coding-agents.md)

Using LLMs to help complete development tasks inside `VS Code`.

### [Networks](./wiki/computer-networks.md)

IP addresses, hosts, `localhost`, and basic networking concepts.

### [Database](./wiki/database.md)

`PostgreSQL`, SQL basics (`SELECT`, `INSERT`, `WHERE`), and database schema concepts.

### [`Docker`](./wiki/docker.md)

Container images, running containers, volumes, and health checks.

### [`Docker Compose`](./wiki/docker-compose.md)

Running multi-container applications from a `docker-compose.yml` file.

### [Environments](./wiki/environments.md)

Environment variables, `.env` files, secrets, and deployment environments.

### [File formats](./wiki/file-formats.md)

`Markdown` and `JSON` file formats.

### [File system](./wiki/file-system.md)

Files, directories, absolute and relative paths, and filesystem concepts.

### [`Git`](./wiki/git.md)

Version control basics, `GitHub flow`, merge conflicts, and `Conventional Commits`.

### [`Git` in `VS Code`](./wiki/git-vscode.md)

Cloning repos, switching branches, staging, and committing via the `VS Code` UI.

### [`GitHub`](./wiki/github.md)

Repositories, forks, issues, and `GitHub`-specific concepts and placeholders.

### [`GitLens`](./wiki/gitlens.md)

`VS Code` extension for exploring Git history, branches, and commits visually.

### [`HTTP`](./wiki/http.md)

Requests, responses, status codes, and the `HTTP` protocol.

### [`Linux`](./wiki/linux.md)

Distributions, users, permissions, processes, and `Linux` fundamentals.

### [Operating system (OS)](./wiki/operating-system.md)

Overview of `Linux`, `macOS`, and `Windows`.

### [`pgAdmin`](./wiki/pgadmin.md)

Web-based GUI for browsing tables, running SQL queries, and managing `PostgreSQL` databases.

### [`Python`](./wiki/python.md)

Syntax, package management with `uv`, testing with `pytest`, and static analysis.

### [Security](./wiki/security.md)

API key authentication and VM hardening (firewall, `fail2ban`, SSH configuration).

### [Shell](./wiki/shell.md)

Shell variants (`bash`, `zsh`), commands, scripting basics, and directory navigation.

### [`SSH`](./wiki/ssh.md)

Key setup, connecting to a VM, and common errors.

### [Swagger](./wiki/swagger.md)

`Swagger UI` for exploring and testing API endpoints.

### [Quality assurance](./wiki/quality-assurance.md)

What testing is, assertions, and links to language-specific testing guides.

### [Useful programs](./wiki/useful-programs.md)

Reference for common CLI tools: `git`, `jq`, `find`, `ripgrep`, and others.

### [Visualize the architecture](./wiki/visualize-architecture.md)

Tools for creating architecture diagrams: `Draw.io`, `PlantUML`, and `Mermaid`.

### [VM](./wiki/vm.md)

Creating, connecting to, and managing a virtual machine.

### [Your VM image](./wiki/vm-info.md)

Programs pre-installed on the lab VM image (`docker`, `uv`, `python`, `nix`, etc.).

### [`VS Code`](./wiki/vs-code.md)

IDE layout, panels, the `Command Palette`, and editor features.
