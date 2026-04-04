# `pyproject.toml`

<h2>Table of contents</h2>

- [What is `pyproject.toml`](#what-is-pyprojecttoml)
- [`[tool.uv.workspace]`](#tooluvworkspace)
- [`[dependency-groups]`](#dependency-groups)
- [`[tool.poe.tasks]`](#toolpoetasks)
  - [Run server](#run-server)
    - [`poe dev`](#poe-dev)
    - [`poe dev-unsafe`](#poe-dev-unsafe)
  - [Static analysis](#static-analysis)
    - [`poe check`](#poe-check)
    - [`poe format`](#poe-format)
    - [`poe lint`](#poe-lint)
    - [`poe typecheck`](#poe-typecheck)
  - [Dynamic analysis](#dynamic-analysis)
    - [`poe test`](#poe-test)
    - [`poe test-unit`](#poe-test-unit)
    - [`poe test-e2e`](#poe-test-e2e)
- [`[tool.ruff.lint]`](#toolrufflint)
- [`[tool.pyright]`](#toolpyright)
- [`[tool.pytest.ini_options]`](#toolpytestini_options)
- [`[tool.ty.src]`](#tooltysrc)

## What is `pyproject.toml`

[`pyproject.toml`](../pyproject.toml) is the central configuration file for a [`Python`](./python.md#what-is-python) project.
It defines project metadata, dependencies, and tool settings in [`TOML`](./file-formats.md#toml) format.

This project uses a [`uv` workspace](#tooluvworkspace) layout with a root `pyproject.toml` and multiple member packages:

- [`pyproject.toml`](../pyproject.toml) (root) — configures the workspace, shared development tools, a [task runner](#toolpoetasks), and [static analysis](./quality-assurance.md#static-analysis) tools.
- Member `pyproject.toml` files, such as [`backend/pyproject.toml`](./backend-pyproject-toml.md#what-is-backendpyprojecttoml), define package metadata and runtime dependencies for their own workspace members.

Docs:

- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)

## `[tool.uv.workspace]`

Declares a [`uv`](./python.md#uv) workspace and lists its member packages.

```toml
[tool.uv.workspace]
members = [
  "backend",
  "qwen-code-api",
  "mcp/mcp-lms",
  "mcp/mcp-obs",
  "nanobot-websocket-channel/nanobot-webchat",
  "nanobot-websocket-channel/client-telegram-bot",
]
```

- **`members`** — directories that contain their own `pyproject.toml` files.
  [`uv`](./python.md#uv) treats each member as a separate package while sharing a single [virtual environment](./vscode-python.md#install-python-and-dependencies) and lock file at the workspace root.

Docs:

- [uv workspaces](https://docs.astral.sh/uv/concepts/workspaces/)

## `[dependency-groups]`

Defines groups of additional dependencies.
The `dev` group contains tools used during development but not required to run the application.

- **`poethepoet`** — the [task runner](#toolpoetasks) used to run predefined commands.
- **`pyright`** — a [static analysis](./quality-assurance.md#static-analysis) type checker for `Python`.
- **`pytest`** — the [testing framework](./python.md#pytest).
- **`pytest-asyncio`** — a `pytest` plugin that enables running `async` test functions.
- **`ruff`** — a fast [linter](#toolrufflint) and [formatter](#poe-format) for `Python`.
- **`ty`** — a type checker for `Python`.

## `[tool.poe.tasks]`

Defines tasks for `Poe the Poet`, a task runner that lets you run predefined commands using `poe <task-name>`.

Docs:

- [Poe the Poet documentation](https://poethepoet.natn.io/)

### Run server

#### `poe dev`

```toml
[tool.poe.tasks.dev]
sequence = ["check", "dev-unsafe"]
```

Runs [`poe check`](#poe-check) followed by [`poe dev-unsafe`](#poe-dev-unsafe).
This ensures the code passes all [static analysis](./quality-assurance.md#static-analysis) checks before starting the server.

#### `poe dev-unsafe`

```toml
[tool.poe.tasks.dev-unsafe]
cmd = "python -m lms_backend.run"
```

Starts the backend server without running [static analysis](./quality-assurance.md#static-analysis) first.

### Static analysis

See [Static analysis](./quality-assurance.md#static-analysis).

#### `poe check`

```toml
[tool.poe.tasks.check]
sequence = ["format", "lint", "typecheck"]
```

Runs all [static analysis](./quality-assurance.md#static-analysis) tools in sequence: [`poe format`](#poe-format), [`poe lint`](#poe-lint), [`poe typecheck`](#poe-typecheck).

#### `poe format`

```toml
[tool.poe.tasks.format]
cmd = "ruff format"
```

Formats all [`Python`](./python.md#what-is-python) files using `ruff`.

#### `poe lint`

```toml
[tool.poe.tasks.lint]
cmd = "ruff check"
```

Checks [`Python`](./python.md#what-is-python) code for lint errors using `ruff`.
See [`[tool.ruff.lint]`](#toolrufflint) for the configured rules.

#### `poe typecheck`

```toml
[tool.poe.tasks.typecheck]
sequence = ["ty-check", "pyright-check"]
```

Runs both type checkers (`ty` and `pyright`) in sequence.

### Dynamic analysis

See [Dynamic analysis](./quality-assurance.md#dynamic-analysis).

#### `poe test`

```toml
[tool.poe.tasks.test]
sequence = ["test-unit", "test-e2e"]
```

Runs [`poe test-unit`](#poe-test-unit), then [`poe test-e2e`](#poe-test-e2e).

Running unit tests is cheaper than running the full test suite.

If there's a problem in unit tests, there's no need to run the full test suite.

Therefore, unit tests run first.

#### `poe test-unit`

```toml
[tool.poe.tasks.test-unit]
cmd = "pytest backend/tests/unit"
envfile = "backend/.env.tests.unit.secret"
```

Runs [unit tests](./quality-assurance.md#unit-test) in `backend/tests/unit/` using [`pytest`](./python.md#pytest).

Uses [environment variables](./environments.md#environment-variable) from [`backend/.env.tests.unit.secret`](./backend-dotenv-tests-unit-secret.md#what-is-backendenvtestsunitsecret).

#### `poe test-e2e`

```toml
[tool.poe.tasks.test-e2e]
cmd = "pytest backend/tests/e2e"
envfile = "backend/.env.tests.e2e.secret"
```

Runs [end-to-end tests](./quality-assurance.md#end-to-end-test) in `backend/tests/e2e/` against the deployed API using [`pytest`](./python.md#pytest).

Uses [environment variables](./environments.md#environment-variable) from [`backend/.env.tests.e2e.secret`](./backend-dotenv-tests-e2e-secret.md#what-is-backendenvtestse2esecret).

## `[tool.ruff.lint]`

Configures lint rules for `ruff`.

```toml
[tool.ruff.lint]
select = ["RET503"]
```

- **`RET503`** — flags functions with an explicit `return` on some paths but an implicit `return None` on others.

Docs:

- [Ruff rule RET503](https://docs.astral.sh/ruff/rules/implicit-return/)

## `[tool.pyright]`

Configures the `pyright` type checker.

```toml
[tool.pyright]
include = ["backend"]
exclude = ["**/__pycache__", "**/node_modules", "**/.*", ".venv", ".direnv"]
typeCheckingMode = "strict"
reportAssignmentType = "none"
reportIncompatibleVariableOverride = "none"
```

- **`include`** — only checks files in the `backend/` directory.
- **`exclude`** — skips generated and tool-managed directories.
- **`typeCheckingMode`** — uses `strict` mode for maximum type safety.
- **`reportAssignmentType`** — disables errors for assignment type mismatches.
- **`reportIncompatibleVariableOverride`** — disables errors for variable override type mismatches.

Docs:

- [Pyright configuration](https://microsoft.github.io/pyright/#/configuration)

## `[tool.pytest.ini_options]`

Configures [`pytest`](./python.md#pytest).

```toml
[tool.pytest.ini_options]
testpaths = ["backend/tests"]
pythonpath = ["backend/src"]
asyncio_mode = "auto"
```

- **`testpaths`** — directories where `pytest` discovers tests.
- **`pythonpath`** — directories added to `Python`'s import path so test files can import application modules.
- **`asyncio_mode`** — set to `"auto"` so `async` test functions run automatically without requiring a per-function decorator.

Docs:

- [pytest configuration](https://docs.pytest.org/en/stable/reference/customize.html)

## `[tool.ty.src]`

Configures the `ty` type checker.

```toml
[tool.ty.src]
include = ["backend"]
```

- **`include`** — only checks files in the `backend/` directory.

Docs:

- [ty documentation](https://docs.astral.sh/ty/)
