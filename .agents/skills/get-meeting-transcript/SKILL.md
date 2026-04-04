---
name: get-meeting-transcript
description: Process a meeting transcript for a given lab and iteration
argument-hint: "<lab-number> <iteration-number> [--merge X=Y ...]"
---

Process the meeting transcript for lab N, iteration M.

## Steps

1. Parse `$ARGUMENTS` to extract N (lab number), M (iteration number), and any optional `--merge X=Y` flags. N and M are required — if missing, ask the user.
2. Read [`contributing/conventions/meetings/meeting-report.md`](../../../contributing/conventions/meetings/meeting-report.md) and locate the **Transcript** path in the File locations section. Substitute actual N and M values, then strip the filename to get the transcripts directory.
3. Run `nix develop --command process-meeting-transcript <transcripts-dir>` using the directory from step 2. Pass through any `--merge` flags as-is.
4. Do NOT summarize, analyze, or comment on the output. Just confirm the command ran successfully.
