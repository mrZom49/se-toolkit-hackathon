---
name: commit
description: Create a git commit following this project's conventions
disable-model-invocation: true
argument-hint: "[files...]"
---

Create a git commit following this project's commit conventions.

## Conventions

Read [`contributing/conventions/git/commits.md`](../../../contributing/conventions/git/commits.md) for the full reference
(types, scopes, subject line, body rules, examples).

## AI co-authorship

Always append this trailer:

```text
Co-Authored-By: <model name> <noreply email>
```

Use your actual model name and vendor no-reply email (e.g. `Claude Opus 4.6 <noreply@anthropic.com>`, `Qwen 2.5 <noreply@alibaba.com>`).

## Staging and committing

- If the user specifies files via $ARGUMENTS, stage only those files. If `$ARGUMENTS` is literally `staged`, skip staging and commit whatever is already in the index
- If no files are specified, stage only files that were read, edited, or created during this session (check conversation history). Do **not** blindly stage all modified files in the working tree
- If a file lives inside a **git submodule**, run `git add` / `git commit` from the submodule's root directory. Known submodule: `instructors/meetings` (remote: `inno-se-toolkit/meetings`). For unknown paths, detect by running `git rev-parse --show-toplevel` from the file's directory — if it differs from the parent repo root, the file is in a submodule. Before staging and committing, `cd` to the submodule root
- Make exactly **one commit** per invocation. If the user passes specific files, commit only those. If changes span unrelated areas, the user will invoke the skill multiple times
