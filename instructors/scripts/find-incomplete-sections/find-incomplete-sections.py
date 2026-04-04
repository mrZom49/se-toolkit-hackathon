"""Find empty sections and TODO-only sections in markdown files."""

import argparse
import os
import re
from collections import defaultdict
from datetime import date
from pathlib import Path


def heading_anchor(text: str) -> str:
    text = re.sub(r"^#+\s*", "", text)
    text = text.lower()
    text = text.replace(" ", "-")
    text = re.sub(r"[^a-z0-9\-]", "", text)
    return text


def scan_file(filepath: Path) -> list[tuple[int, str, str, str]]:
    lines = filepath.read_text(encoding="utf-8", errors="replace").splitlines()
    results: list[tuple[int, str, str, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^#{1,6}\s+", line):
            heading_line = i + 1
            heading_text = line.rstrip()
            j = i + 1
            body_lines: list[str] = []
            while j < len(lines):
                if re.match(r"^#{1,6}\s+", lines[j]):
                    break
                body_lines.append(lines[j])
                j += 1
            non_blank = [bl.strip() for bl in body_lines if bl.strip()]
            if not non_blank:
                results.append((heading_line, heading_text, "empty", ""))
            else:
                todo_comments: list[str] = []
                all_todo = True
                for bl in non_blank:
                    m = re.match(r"^<!--\s*TODO\s*(.*?)\s*-->$", bl)
                    if m:
                        todo_comments.append(m.group(1).strip())
                    else:
                        all_todo = False
                        break
                if all_todo and todo_comments:
                    results.append(
                        (heading_line, heading_text, "TODO", " | ".join(todo_comments))
                    )
        i += 1
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="Directory to scan (default: lab/tasks/ and wiki/)",
    )
    parser.add_argument("--output", required=True, help="Path to write the report to")
    args = parser.parse_args()

    report_path = Path(args.output)
    search_paths = [Path(args.path)] if args.path else [Path("lab/tasks"), Path("wiki")]

    md_files: list[Path] = []
    for sp in search_paths:
        md_files.extend(sorted(sp.rglob("*.md")))

    file_results: dict[str, list[tuple[int, str, str, str]]] = {}
    empty_count = 0
    todo_count = 0

    for filepath in md_files:
        fres = scan_file(filepath)
        if fres:
            file_results[str(filepath)] = fres
            for _, _, kind, _ in fres:
                if kind == "empty":
                    empty_count += 1
                else:
                    todo_count += 1

    out: list[str] = []
    out.append("# Incomplete sections")
    out.append("")
    out.append(f"**Date:** {date.today().isoformat()}")
    out.append(f"**Paths scanned:** {', '.join(f'`{sp}`' for sp in search_paths)}")
    out.append("")

    if not file_results:
        out.append("---")
        out.append("")
        out.append("No incomplete sections found.")
    else:
        groups: dict[str, list[str]] = defaultdict(list)
        for filepath_str in sorted(file_results.keys()):
            top = Path(filepath_str).parts[0].capitalize()
            groups[top].append(filepath_str)
        sorted_groups = sorted(groups.items())

        out.append("<h2>Table of contents</h2>")
        out.append("")
        for group, files in sorted_groups:
            out.append(f"- [{group}](#{group.lower()})")
            for fp in files:
                anchor = heading_anchor(f"### `{fp}`")
                out.append(f"  - [`{fp}`](#{anchor})")
        out.append("")
        out.append("---")
        out.append("")

        for group, files in sorted_groups:
            out.append(f"## {group}")
            out.append("")
            for filepath_str in files:
                out.append(f"### `{filepath_str}`")
                out.append("")
                for lnum, heading, kind, comment in file_results[filepath_str]:
                    anchor = heading_anchor(heading)
                    rel = os.path.relpath(filepath_str, report_path.parent)
                    link_target = f"{rel}#{anchor}"
                    label = f"{filepath_str}:{lnum}"
                    if kind == "empty":
                        out.append(f"- [{label}]({link_target}) — {heading} (empty)")
                    else:
                        out.append(
                            f"- [{label}]({link_target}) — {heading} (TODO: {comment})"
                        )
                out.append("")

    out.append("---")
    out.append("")
    out.append(
        f"**Summary:** {empty_count + todo_count} incomplete sections total"
        f" — {empty_count} empty, {todo_count} TODO-only"
    )

    if file_results:
        by_count = sorted(file_results.items(), key=lambda x: len(x[1]), reverse=True)
        out.append("")
        out.append("Most affected files:")
        out.append("")
        for fp, fres in by_count[:5]:
            out.append(f"- `{fp}`: {len(fres)} section(s)")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Report written to {report_path}")


if __name__ == "__main__":
    main()
