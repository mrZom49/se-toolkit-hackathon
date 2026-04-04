---
name: pr
description: Create or update a pull request using this project's PR template
disable-model-invocation: true
argument-hint: "[issue-number]"
---

Create or update a pull request following the project's PR template at `.github/pull_request_template.md`.

## Rules

- Run `git fetch origin main` to update the remote ref, then run `git log origin/main..HEAD` to get the commit messages for all commits between the local current branch and the remote main branch.
- Check if an open (unmerged) PR already exists for the current branch by running `gh pr view --json state,url,title 2>/dev/null`. If a PR exists and its state is `OPEN`, follow the **Updating an existing PR** flow below. Otherwise, follow the **Creating a new PR** flow.

### Creating a new PR

- Write a concise PR title summarizing the changes (under 72 characters). Base it on the commit messages.
- Fill in the Summary section with a bullet list of the key changes in the PR, written in imperative voice (e.g. "Rename appendix to wiki"). Derive each bullet point from the commit messages — do not invent or assume changes not described in them.
- If `$ARGUMENTS` contains an issue number, include `- Closes #<issue-number>` in the Summary section; otherwise omit that line entirely.
- Use `gh pr create` with `--title` and `--body` to open the PR.
- Target the `main` branch (`--base main`).
- Do not mark any checklist items. Leave all checkboxes unchecked (`[ ]`) for the user to review and check manually.
- Do not push or create the PR without showing the user the complete `gh pr create` command first (using a heredoc for the body) and asking for confirmation. The user can edit the command before approving it.

### Updating an existing PR

- Regenerate the PR title and body using the same rules as for a new PR (concise title, imperative bullet list derived from all commits, checklist unchecked).
- Show the user the complete `gh pr edit` command (using a heredoc for the body) and ask for confirmation. The user can edit the command before approving it.
