"""Post-process lychee --format json output to add file:line locations."""

import json
import os
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from pydantic import BaseModel

# ANSI colours — only when writing to a real terminal
_TTY = sys.stdout.isatty()

_md = MarkdownIt()


def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _TTY else text


class _Status(BaseModel):
    text: str


class _LinkError(BaseModel):
    url: str
    status: _Status


class _LycheeOutput(BaseModel):
    error_map: dict[str, list[_LinkError]] = {}


def _display_url(url: str) -> str:
    """Convert file:// URLs to relative paths; leave other URLs unchanged."""
    if url.startswith("file://"):
        path_part = re.sub(r"^file://", "", url)
        file_path, _, fragment = path_part.partition("#")
        try:
            rel = Path(file_path).relative_to(Path.cwd())
            return f"{rel}#{fragment}" if fragment else str(rel)
        except ValueError:
            pass
    return url


def find_locations(filepath: str, url: str) -> list[tuple[int, int, str]]:
    """Find source locations of a broken link using markdown AST parsing.

    Parses the file with markdown-it-py to extract all links, resolves each
    href to an absolute path (mirroring lychee's resolution), and matches
    against the reported URL.  This avoids false positives from the previous
    basename-only regex approach.
    """
    if not url.startswith("file://"):
        # Non-file URLs: fall back to plain text search.
        pattern = re.compile(re.escape(url.rstrip("/")))
        results: list[tuple[int, int, str]] = []
        try:
            with open(filepath) as f:
                for i, line in enumerate(f, 1):
                    m = pattern.search(line)
                    if m:
                        results.append(
                            (i, m.start() + 1, line[m.start() : m.end()].rstrip())
                        )
        except (OSError, UnicodeDecodeError):
            pass
        return results

    # Decompose lychee's absolute file:// URL into path + fragment.
    url_path = re.sub(r"^file://", "", url)
    url_file, _, url_fragment = url_path.partition("#")
    url_file_norm = os.path.normpath(url_file)

    try:
        with open(filepath) as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return []

    lines = content.splitlines()
    source_dir = os.path.dirname(os.path.abspath(filepath))
    cwd = str(Path.cwd())
    tokens = _md.parse(content)

    results: list[tuple[int, int, str]] = []
    for token in tokens:
        if not token.children or not token.map:
            continue
        for child in token.children:
            if child.type == "link_open":
                href = dict(child.attrs or {}).get("href", "")
            elif child.type == "image":
                href = dict(child.attrs or {}).get("src", "")
            else:
                continue
            if not href:
                continue

            # Resolve the href to an absolute path the same way lychee does.
            href_path, _, href_fragment = href.partition("#")
            if href_path:
                if href_path.startswith("/"):
                    resolved = os.path.normpath(cwd + href_path)
                else:
                    resolved = os.path.normpath(os.path.join(source_dir, href_path))
            else:
                # Fragment-only link targets the source file itself.
                resolved = os.path.normpath(os.path.abspath(filepath))

            if resolved != url_file_norm or href_fragment != url_fragment:
                continue

            # Found a matching broken link — locate exact column.
            start_line, end_line = token.map
            for i in range(start_line, min(end_line, len(lines))):
                col = lines[i].find(href)
                if col >= 0:
                    results.append((i + 1, col + 1, href))
                    break

    # Deduplicate while preserving order.
    return list(dict.fromkeys(results))


raw = sys.stdin.read()
# lychee sometimes emits the JSON block twice; take the first complete object
raw_obj, _ = json.JSONDecoder().raw_decode(raw.lstrip())
data = _LycheeOutput.model_validate(raw_obj)

if not data.error_map:
    print("No broken links found.")
    sys.exit(0)

total = 0

for filepath, errors in data.error_map.items():
    try:
        relpath = Path(filepath).relative_to(Path.cwd())
    except ValueError:
        relpath = Path(filepath)
    for error in errors:
        locs = find_locations(filepath, error.url)
        display_link = _display_url(error.url)
        if locs:
            total += len(locs)
            for loc in locs:
                location = f"{relpath}:{loc[0]}:{loc[1]}"
                link = loc[2] if error.url.startswith("file://") else display_link
                print(f"{_c('1', location)}: {_c('1;31', '[ERROR]')} {_c('36', link)}")
                print(f"  {_c('2', error.status.text)}")
        else:
            total += 1
            print(
                f"{_c('1', str(relpath))}: {_c('1;31', '[ERROR]')} {_c('36', display_link)}"
            )
            print(f"  {_c('2', error.status.text)}")

print(
    f"\n{_c('1;31', f'Found {total} broken link(s) in {len(data.error_map)} file(s).')}"
)
sys.exit(1)
