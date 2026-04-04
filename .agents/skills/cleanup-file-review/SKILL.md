---
name: cleanup-file-review
description: Clean up a file-review report by removing addressed problems and writing "No issues found." for empty sections
argument-hint: "<path>"
---

Remove addressed (strikethrough-marked) problem entries from a file-review report and replace emptied sections with the appropriate "no issues" placeholder.

## Steps

1. Parse `$ARGUMENTS` to get the file path. Accept:
   - Paths under `lab/tasks/` (e.g., `lab/setup/setup-full.md`, `lab/tasks/required/task-2.md`)
   - Paths under `wiki/` (e.g., `wiki/api.md`)
   - Paths under `contributing/conventions/` (e.g., `contributing/conventions/writing/common.md`)
   - The repository root `AGENTS.md` file
   - Meeting report files matching the pattern `instructors/meetings/week-N/meeting-M/report.md`

   If the path is missing or does not match one of these patterns, ask the user.

2. Derive the review file path:
   - **For `instructors/meetings/` files:** `report-review.md` in the same directory as the source file (e.g., `instructors/meetings/week-2/meeting-1/report-review.md` for `instructors/meetings/week-2/meeting-1/report.md`).
   - **For all other files:** `instructors/file-reviews/<repo-root-path>`, where `<repo-root-path>` is the target file's path from the repository root (e.g., `instructors/file-reviews/lab/tasks/required/task-1.md`).

   If the review file does not exist, tell the user to run `/review-file <path>` first and stop.

3. Read the review file.
4. **Identify addressed items.** An item is addressed if its opening line is a numbered list entry where the content is wrapped in strikethrough: `1. ~~…~~`. Multi-line items have their continuation lines (indented paragraphs and their blank separator lines) also wrapped in strikethrough.
5. **Remove each addressed item** — the numbered list line, any blank lines that follow it within the same item, and any indented continuation paragraphs (lines starting with three or more spaces that belong to the same item). Re-number the remaining items in each section sequentially starting from 1.
6. **Replace emptied sections.** After removal, if a section heading (e.g., `### D3. Student navigation` or `### 4.2. Terminal commands`) has no remaining numbered items beneath it, replace the empty body with a single line matching the original placeholder style:
   - Use `No issues found.` for Conceptual findings sections, Convention findings sections, and Meeting report findings sections.
   - Use `Not applicable.` only if the original section already said "Not applicable." and no items were removed from it (i.e., it was already not applicable — do not change it).
   - Use `No TODOs found.` for the **TODOs** section.
   - Use `No empty sections found.` for the **Empty sections** section.
7. **Update the Summary table.** Recount all remaining items in the report (excluding strikethrough lines) and update the counts in the summary table. Recalculate the **Total** row. Rewrite the **Overall assessment** paragraph to reflect the current state of the file (remaining issues only).

## Rules

- Only remove items explicitly marked with `~~` strikethrough. Never remove items that are not marked.
- Do not change any section heading, horizontal rule, report header, or the structure of the report.
- Do not alter the wording of any remaining (non-strikethrough) problem item.
- When re-numbering, use plain integers starting at 1 (`1.`, `2.`, `3.`, …).
- If no addressed items are found in the report, tell the user and stop — do not modify the file.

## Output

After editing the report, print a one-line summary: how many items were removed and how many remain.
