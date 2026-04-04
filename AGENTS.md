# AGENTS.md

This file provides instructions for AI coding agents working in this repository.

---

## Build, Lint, and Test Commands

Run all commands from the repository root (`/root/se-toolkit-lab-8`) using `uv run poe <task>`.

### Static Analysis

```sh
# Run all checks (format + lint + typecheck)
uv run poe check

# Format code with Ruff
uv run poe format

# Lint with Ruff
uv run poe lint

# Typecheck (Pyright + ty)
uv run poe typecheck
```

### Testing

```sh
# Run all tests (unit + e2e)
uv run poe test

# Run unit tests only
uv run poe test-unit

# Run e2e tests only (against deployed API)
uv run poe test-e2e

# Run a single test file
uv run pytest backend/tests/unit/test_interactions.py

# Run a single test function
uv run pytest backend/tests/unit/test_interactions.py::test_filters_by_item_id -v

# Run tests matching a pattern
uv run pytest backend/tests/unit/ -k "interaction" -v
```

### Development

```sh
# Run server with static analysis
uv run poe dev

# Run server without checks
uv run poe dev-unsafe

# Export OpenAPI schema
uv run poe export-openapi

# Check OpenAPI schema is up to date
uv run poe check-openapi
```

### Flutter (client-web-react)

Flutter CLI is not installed locally. Run via Docker:

```sh
uv run poe flutter <args>
# Example: uv run poe flutter analyze lib/chat_screen.dart
```

---

## Code Style Guidelines

### Python (backend/, mcp/, qwen-code-api/)

**Naming conventions:**
- Files/modules: `snake_case` (e.g., `interaction_logs.py`)
- Functions/variables: `snake_case` (e.g., `read_learners`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `DEFAULT_PAGE_SIZE`)
- Classes: `PascalCase` (e.g., `LearnerCreate`)
- SQLModel table: `__tablename__ = "learner"` (singular, snake_case)
- Test files: `test_<module>.py` (e.g., `test_interactions.py`)
- Test functions: `test_<behaviour>` (e.g., `test_filters_by_item_id`)

**Type annotations:**
- All function signatures must have **full type annotations** (params and return type)
- Use `X | None` union syntax, not `Optional[X]`
- Pyright runs in **strict** mode — zero errors allowed

**Imports:**
- Standard library first, then third-party, then local
- Use explicit relative imports for intra-package imports

**Comments:**
- Every module starts with a one-line docstring
- Every public class and function has a docstring
- Use inline comments only when logic is non-obvious

### TypeScript / React (client-web-react/)

**Naming conventions:**
- Component files: `PascalCase.tsx` (e.g., `App.tsx`)
- Utility files: `camelCase.ts` (e.g., `apiClient.ts`)
- Functions/variables: `camelCase` (e.g., `setItems`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `API_URL`)
- Components: `PascalCase` (e.g., `function App()`)
- CSS files: matches component (e.g., `App.css`)

**Types:**
- All component props and API response shapes must have **explicit interfaces**
- Prefer `interface` over `type` for object shapes
- Use `strict` compiler option — zero errors allowed

### Environment Variables

- Backend: no prefix (e.g., `DATABASE_URL`)
- Frontend (Vite): `VITE_` prefix (e.g., `VITE_API_URL`)

### Markdown / Config Files

- Markdown files: `kebab-case.md`
- Directories: `kebab-case`
- Docker/Compose: lowercase (e.g., `docker-compose.yml`)

---

## Error Handling

- Never swallow exceptions silently — log and re-raise or return meaningful error responses
- API clients should handle HTTP errors with appropriate status code checks
- Use `httpx` for async HTTP calls; check response status before accessing body

---

## Security

- Store secrets in `.env` files — never hardcode API keys or passwords
- Use `.env.docker.example` as a template for required environment variables
- Never commit `.env.docker.secret` or `*.secret` files

---

## Docker

Always use the env file flag when running docker compose:

```sh
docker compose --env-file .env.docker.secret <command>
```

---

## Key Conventions Files

- **Code conventions:** `contributing/conventions/implementation/code.md`
- **Git conventions:** `contributing/conventions/git/`
- **Lab authoring:** `contributing/conventions/writing/`
- **Agent skills:** `.agents/skills/`
- **Project structure:** `contributing/configuration.md`
