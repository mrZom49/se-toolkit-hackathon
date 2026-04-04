---
name: fix-broken-links
description: >
  Find and fix broken markdown links in the repository. Use when links return
  "Cannot find file" or "Cannot find fragment" errors. Runs find-broken-links
  to detect problems, then repairs each broken link by locating the correct
  target or updating the fragment anchor.
compatibility: requires find-broken-links on PATH (available via nix develop)
---

Find all broken markdown links in the repository and fix each one.

## Steps

1. Run `nix develop -c find-broken-links` from the repository root. Capture the output.
   If the command fails (e.g., nix is not available), stop and tell the user.
2. Parse the output. Each broken link is reported as:
   ```
   file:line:col: [ERROR] link-target
     Reason
   ```
   where `Reason` is either `Cannot find file` or `Cannot find fragment`.
   Group errors by source file. Deduplicate entries that appear more than once
   (the tool may report the same link under multiple reasons).
3. If the output contains `Found 0 broken link(s)`, print "No broken links found." and stop.
4. For each source file with broken links:
   a. Read the source file.
   b. For each broken link in the file (use the reported line number as a starting guide,
      then verify against the actual file content):
      - **Cannot find file**: the linked file has moved or been deleted.
        Search the repository for a file whose name matches the last path segment
        of the broken link. If exactly one match exists, update the link to use
        the correct relative path from the source file's location. If no match or
        multiple matches exist, note the link as unresolvable and skip it.
      - **Cannot find fragment**: the linked file exists but the anchor is wrong.
        Read the target file. List all headings and derive their anchors
        (lowercase, spaces replaced with hyphens, special characters removed).
        Find the anchor that most closely matches the broken one. If a clear
        match exists, update the fragment. Otherwise, note it as unresolvable
        and skip it.
   c. Apply all fixes to the source file.
5. After all fixes, re-run `nix develop -c find-broken-links`. Verify that fixed
   links no longer appear in the output.

## Rules

- Fix only links that appear in the `find-broken-links` output. Do not modify
  any other links or file content.
- If a broken link cannot be resolved with confidence, skip it and report it as
  unresolvable rather than guessing.
- Never delete a link just because it is broken — only remove it if the link
  target no longer exists anywhere in the repository and there is no reasonable
  replacement.

## Output

After all fixes, print a summary with three sections:

**Fixed** — one line per link fixed, in the format `file:line: old-target → new-target`.

**Unresolvable** — one line per link that could not be fixed, with the reason.

**Counts** — totals for fixed, unresolvable, and total broken links found.
