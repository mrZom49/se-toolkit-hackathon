# `backend/pyproject.toml`

<h2>Table of contents</h2>

- [What is `backend/pyproject.toml`](#what-is-backendpyprojecttoml)
- [`[project]`](#project)
- [`[dependency-groups]`](#dependency-groups)

## What is `backend/pyproject.toml`

[`backend/pyproject.toml`](../backend/pyproject.toml) defines the backend application metadata and runtime dependencies.
It is a workspace member of the root [`pyproject.toml`](./pyproject-toml.md#tooluvworkspace), which means [`uv`](./python.md#uv) manages its dependencies together with the shared development tools defined at the workspace level.

Docs:

- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [uv workspaces](https://docs.astral.sh/uv/concepts/workspaces/)

## `[project]`

Defines the backend application metadata and runtime dependencies.

- **`name`** — the package name.
- **`version`** — the current version of the backend.
- **`description`** — a short description of the package.
- **`requires-python`** — the exact [`Python`](./python.md#what-is-python) version required.
  [`uv sync`](./vscode-python.md#install-python-and-dependencies) automatically downloads and uses this version.
- **`dependencies`** — the list of packages required to run the application.
  [`uv`](./python.md#uv) installs them into the [virtual environment](./vscode-python.md#install-python-and-dependencies).

Runtime dependencies:

- **`asyncpg`** — an asynchronous [`PostgreSQL`](./postgresql.md#what-is-postgresql) driver.
- **`fastapi`** — the web framework used to build the [REST API](./rest-api.md#what-is-a-rest-api).
- **`httpx`** — an asynchronous [HTTP](./http.md#what-is-http) client used for making outbound requests.
- **`pydantic`** — a data validation library that `FastAPI` uses for request and response models.
- **`pydantic-settings`** — extends `pydantic` to load configuration from [environment variables](./environments.md#environment-variable).
- **`sqlmodel`** — an ORM that combines `pydantic` models with [`SQL`](./sql.md#what-is-sql) database tables.
- **`uvicorn`** — an ASGI server that runs the `FastAPI` application.

## `[dependency-groups]`

Defines groups of additional dependencies specific to the backend.
The `dev` group contains packages needed only during development.

```toml
[dependency-groups]
dev = [
  "aiosqlite>=0.21.0",
  "greenlet>=3.2.0",
]
```

- **`aiosqlite`** — an asynchronous `SQLite` driver used as an in-memory database for [unit tests](./quality-assurance.md#unit-test).
- **`greenlet`** — a concurrency library required by `sqlmodel` when running with `aiosqlite`.
