"""Export the OpenAPI schema from the FastAPI app to a JSON file."""

import argparse
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "backend" / "openapi.json"

# Seed the minimal backend settings required to import the app and export its
# schema in CI without depending on a real runtime environment.
_EXPORT_ENV_DEFAULTS = {
    "NAME": "Learning Management Service",
    "DEBUG": "false",
    "ADDRESS": "0.0.0.0",
    "PORT": "8000",
    "RELOAD": "false",
    "LMS_API_KEY": "dummy",
    "CORS_ORIGINS": "[]",
    "BACKEND_ENABLE_INTERACTIONS": "true",
    "BACKEND_ENABLE_LEARNERS": "true",
    "AUTOCHECKER_API_URL": "http://example.invalid",
    "AUTOCHECKER_API_LOGIN": "dummy",
    "AUTOCHECKER_API_PASSWORD": "dummy",
    "DB_HOST": "localhost",
    "DB_PORT": "5432",
    "DB_NAME": "dummy",
    "DB_USER": "dummy",
    "DB_PASSWORD": "dummy",
}

for name, value in _EXPORT_ENV_DEFAULTS.items():
    os.environ[name] = value

from lms_backend.main import app


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check that the file is up to date instead of writing it",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output file path (default: %(default)s)",
    )
    args = parser.parse_args()

    schema = app.openapi()
    new_content = json.dumps(schema, indent=2) + "\n"

    if args.check:
        if not args.output.exists():
            print(f"ERROR: {args.output} does not exist.", file=sys.stderr)
            print("Run `uv run poe export-openapi` to generate it.", file=sys.stderr)
            raise SystemExit(1)
        old_content = args.output.read_text()
        if old_content != new_content:
            print(f"ERROR: {args.output} is out of date.", file=sys.stderr)
            print(
                "Run `uv run poe export-openapi` and commit the result.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        print("openapi.json is up to date.")
        return

    args.output.write_text(new_content)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
