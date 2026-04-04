---
name: get-meeting-report
description: Generate a meeting report for a given lab and iteration
argument-hint: "<lab-number> <iteration-number>"
---

Generate a meeting report for week N, meeting M.

## Steps

1. Parse `$ARGUMENTS` to extract N (week number) and M (meeting number). Both are required — if missing, ask the user.
2. Read [`contributing/conventions/meetings/meeting-report.md`](../../../contributing/conventions/meetings/meeting-report.md) for the report format, rules, and file locations.
3. Read the transcript at the path specified in the File locations section of the convention file (substituting actual N and M).
4. Following the convention file, write the meeting report to the path specified in the File locations section.

## Output

Confirm the file was written. Do not summarize, analyze, or comment on the report contents.
