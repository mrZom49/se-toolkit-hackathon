---
name: find-incomplete-sections
description: Find empty sections and sections containing TODO markers in task and wiki files
argument-hint: "[path]"
---

Find all incomplete sections in markdown files — either empty headings (no content below them) or sections that contain only a `<!-- TODO ... -->` comment. Writes the report to `instructors/file-reviews/incomplete-sections.md`.

## Steps

1. Run the helper script from the repo root. If `$ARGUMENTS` is provided, pass it as the path argument; otherwise omit it to use the default paths (`lab/tasks/` and `wiki/`):
   ```
   python3 instructors/scripts/find-incomplete-sections/find-incomplete-sections.py $ARGUMENTS --output instructors/file-reviews/incomplete-sections.md
   ```
2. Display the contents of `instructors/file-reviews/incomplete-sections.md` to the user.
