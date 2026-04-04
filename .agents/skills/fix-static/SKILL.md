---
name: fix-static
description: Fix Python static analysis errors (lint, type checking, formatting). Use when the user wants to resolve type errors, lint violations, or formatting issues found by `uv run poe check`.
argument-hint: "[files...]"
---

Fix Python static analysis errors by running the project's full check pipeline and resolving each reported diagnostic using Pydantic validation, protocols, and strict type-safe patterns.

## Steps

1. Run `uv run poe check` and capture the full output. This runs formatting, linting, and type checking in sequence.
2. Parse the diagnostics. Each diagnostic includes a rule name, file path, line number, and explanation. Diagnostics may come from the formatter (ruff format), linter (ruff check), or type checkers (ty, pyright).
3. If `$ARGUMENTS` specifies one or more file paths, filter the diagnostics to only those files. Otherwise, fix all reported errors.
4. Group diagnostics by file. Process one file at a time, reading the file before applying fixes.
5. For each diagnostic, apply the minimal code change that resolves it. Follow the [type error resolution hierarchy](#type-error-resolution-hierarchy) for type errors. Common fixes include:
   - **Formatting**: apply the formatting change the formatter expects.
   - **Lint**: fix the code pattern flagged by the rule (e.g., missing return, unused import).
   - **Type errors**: resolve using the approaches in the hierarchy below, in order of preference.
6. After all fixes are applied, run `uv run poe check` again to verify the errors are resolved.
7. If new errors were introduced by the fixes, resolve them. Repeat until the fixed files are clean or only pre-existing errors in other files remain.

## Type error resolution hierarchy

When fixing a type error, try approaches in this order. Use the first one that works. Every approach below produces real type safety — none of them silence the checker.

### 1. Pydantic model validation (preferred for external data)

When the value comes from an external source (HTTP response, JSON payload, database row, config file), validate it through a Pydantic model. This gives both a type annotation and runtime validation.

```python
# BAD — bare annotation, no runtime guarantee
data: list[dict[str, str]] = response.json()

# GOOD — Pydantic validates structure and types at runtime
items = [Item.model_validate(i) for i in response.json()]
```

If no suitable model exists, create one. A two-field `BaseModel` is better than a bare `dict[str, Any]` annotation:

```python
class HealthResult(BaseModel):
    status: str
    version: str

result = HealthResult.model_validate(response.json())
```

For validating a type that is not a model (e.g., a list of strings), use `TypeAdapter`:

```python
from pydantic import TypeAdapter

adapter = TypeAdapter(list[str])
tags = adapter.validate_python(response.json())
```

### 2. Protocol classes (preferred for structural typing)

When the error involves incompatible interfaces, duck typing, or dependency injection, define or extend a `Protocol` class. Protocols declare the shape a type must satisfy without requiring inheritance.

```python
from typing import Protocol

class LMSClientProtocol(Protocol):
    async def get_items(self) -> list[Item]: ...
    async def get_learners(self) -> list[Learner]: ...
```

Use protocols when:
- A function accepts multiple concrete types that share a common interface.
- A third-party type does not implement your interface but structurally satisfies it.
- You need to decouple a handler or service from a concrete implementation for testability.

### 3. isinstance / assert narrowing (preferred for unions and optionals)

When the checker cannot determine which branch of a union applies, narrow with `isinstance` or `assert`:

```python
# Narrow Optional
if user is None:
    raise ValueError("user required")
# checker now knows: user is User

# Narrow union
if isinstance(value, str):
    process_string(value)
elif isinstance(value, int):
    process_int(value)
```

Use `assert` only when the condition is an invariant that must hold for the program to be correct:

```python
session = get_session()
assert session is not None  # session is always set after init
```

### 4. Explicit type annotations (preferred for local variables)

When the checker cannot infer a local variable's type from context, add an explicit annotation:

```python
rows: list[InteractionLog] = list((await session.exec(stmt)).all())
```

Use the most specific concrete type possible. Never annotate with `Any`, `object`, or an overly broad type when a narrower one is known.

### 5. TypeVar and Generic (preferred for reusable generic code)

When writing a function that operates on multiple types while preserving the input type in the output, use `TypeVar`:

```python
from typing import TypeVar

T = TypeVar("T", bound=BaseModel)

def first_or_raise(items: list[T]) -> T:
    if not items:
        raise ValueError("empty list")
    return items[0]
```

### 6. cast() (last resort — only when the type is provably correct)

Use `cast()` only when you can prove the type is correct but the checker cannot follow the proof. This is the weakest approach because it provides zero runtime checking.

```python
from typing import cast

# Acceptable: SQLAlchemy aggregate return type is too broad for the checker
avg_score = cast(float, row[0])
```

Before reaching for `cast()`, verify that none of the above approaches apply. If you use `cast()`, add a brief inline comment explaining why the cast is safe.

## Rules

- **Never use suppression comments.** Do not add `# type: ignore[...]`, `# pyright: ignore[...]`, `# noqa`, or any similar comment that silences a diagnostic. Every error must be resolved by fixing the actual code.
- **Never introduce `Any`.** Do not import `Any` from `typing` or annotate anything as `Any` to silence an error. `Any` disables type checking entirely for that value. Use a concrete type, a union, a `TypeVar`, a protocol, or a Pydantic model instead.
- **Never annotate with bare `dict` or `list`.** Always parameterize: `dict[str, int]`, `list[Item]`. If the value type is truly heterogeneous, validate it through a Pydantic model rather than using `dict[str, Any]`.
- **Prefer Pydantic validation over bare type annotations for external data.** When a value crosses a trust boundary (HTTP response, file read, environment variable, deserialized JSON), validate it through `model_validate`, `TypeAdapter`, or `BaseSettings` rather than just annotating the variable. A bare annotation asserts the type only to the checker; Pydantic enforces it at runtime.
- **Prefer protocols over `Union` for polymorphism.** When multiple concrete types need to satisfy the same interface, define a `Protocol` rather than enumerating types in a `Union`. Protocols are open for extension and do not require modifying existing code when a new implementation is added.
- **Use `X | None` syntax, not `Optional[X]`.** This project uses modern Python union syntax.
- Do not change runtime behavior beyond adding Pydantic validation, type narrowing, or type annotations.
- Do not add unnecessary imports. Only import typing constructs or Pydantic classes when needed by a fix.
- When a diagnostic stems from a third-party library's incomplete stubs or decorator patterns the checker cannot follow (e.g., framework-registered handlers reported as unused, or `add_middleware` type mismatches), fix it by restructuring the call, introducing a protocol that matches the expected shape, or — as a last resort — using `cast()` with a justification comment.

## Output

Print a summary listing each fixed diagnostic: file path, line number, rule name, and a one-line description of the fix applied. End with the final check result.
