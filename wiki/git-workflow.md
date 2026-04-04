# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](./github.md#github-flow).

```text
Issue ➜ Branch ➜ Commits ➜ PR ➜ Review ➜ Merge
```

The following diagram shows this workflow in the context of repositories:

<img alt="Git workflow" src="./images/git-workflow/git-workflow.drawio.svg" style="width:100%"></img>

Outline:

- [Create a `Lab Task` issue](#create-a-lab-task-issue)
- [Switch to the branch `main`](#switch-to-the-branch-main)
- [Pull changes from the branch `main` on the remote `origin`](#pull-changes-from-the-branch-main-on-the-remote-origin)
- [Pull changes from the branch `main` on the remote `upstream`](#pull-changes-from-the-branch-main-on-the-remote-upstream)
- [Switch to the `<task-branch>`](#switch-to-the-task-branch)
  - [`<task-branch>` placeholder](#task-branch-placeholder)
- [Edit files](#edit-files)
- [Commit changes](#commit-changes)
- [(Optional) Undo commits](#optional-undo-commits)
- [Push commits](#push-commits)
- [Create a PR to the branch `main` in your fork](#create-a-pr-to-the-branch-main-in-your-fork)
- [Get a PR review](#get-a-pr-review)
  - [PR review rules](#pr-review-rules)
    - [PR review rules for the reviewer](#pr-review-rules-for-the-reviewer)
    - [PR review rules for the author](#pr-review-rules-for-the-author)
- [Merge the PR](#merge-the-pr)
- [Clean up](#clean-up)

## Create a `Lab Task` issue

[Create an issue](./github.md#create-an-issue) using the `Lab Task` [issue form](./github.md#issue-form).

## Switch to the branch `main`

[Switch to the branch `main`](./git-vscode.md#switch-to-the-branch-branch) in `VS Code`.

## Pull changes from the branch `main` on the remote `origin`

[Pull changes](./git-vscode.md#pull-changes-from-the-branch-branch-on-remote) from the branch `main` on the remote [`origin`](./github.md#origin) to get the latest changes from your repository.

## Pull changes from the branch `main` on the remote `upstream`

[Pull changes](./git-vscode.md#pull-changes-from-the-branch-branch-on-remote) from the branch `main` on the remote [`upstream`](./github.md#upstream) to get the latest changes from the instructors' repository.

## Switch to the `<task-branch>`

[Create a new branch `<task-branch>` from the branch `main` and switch to it](./git-vscode.md#switch-to-a-new-branch).

### `<task-branch>` placeholder

The [new branch for the task](#switch-to-the-task-branch).

Alternatively, the name of that branch (without `<` and `>`).

## Edit files

[Edit files](./vs-code.md#editor) using `VS Code` to produce changes.

## Commit changes

[Commit changes](./git-vscode.md#commit-changes) to the [`<task-branch>`](#task-branch-placeholder) to complete the task.

## (Optional) Undo commits

[Undo commits](./git-vscode.md#undo-commits) if necessary.

## Push commits

1. [Publish the branch](./git-vscode.md#publish-the-branch) with your changes if it's not yet published.
2. [Push more commits](./git-vscode.md#push-more-commits) to the published branch if necessary.

## Create a PR to the branch `main` in your fork

[Create a PR](./github.md#create-a-pull-request-in-your-fork) from the branch [`<task-branch>`](#task-branch-placeholder) to `main`.

Replace the placeholders:

- [`<repo-name>`](./github.md#repo-name-placeholder) with [`<lab-repo-name>`](./lab.md#lab-repo-name)
- [`<branch>`](./git.md#branch-placeholder) with [`<task-branch>`](./git-workflow.md#task-branch-placeholder)
- [`<your-github-username>`](./github.md#your-github-username-placeholder)

> [!WARNING]
> By default, `GitHub` sets the base repository to the upstream (`inno-se-toolkit`).
>
> You must **change the base repository to your own fork** (`<your-github-username>/<lab-repo-name>`) before creating the PR. Do **not** create PRs to the upstream repo.

## Get a PR review

1. [Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review#requesting-reviews-from-collaborators-and-organization-members) a review of the PR from the collaborator.

2. Conduct the PR review together following the [PR review rules](#pr-review-rules).

3. Get the collaborator to approve the PR.

### PR review rules

- [PR review rules for the reviewer](#pr-review-rules-for-the-reviewer)
- [PR review rules for the author](#pr-review-rules-for-the-author)

#### PR review rules for the reviewer

As a reviewer:

- Check the task's **Acceptance criteria**.
- Leave at least one [comment](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-comments-to-a-pull-request) — point out problems or confirm that items look good.
- [Approve](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#submitting-your-review) the PR when all relevant acceptance criteria are met.

#### PR review rules for the author

As a PR author:

- Address reviewer comments (fix issues or explain your reasoning).
- Reply to comments, e.g., "Fixed in d0d5aeb".

## Merge the PR

Click `Merge pull request`.

## Clean up

1. Close the issue.

2. Delete the PR branch ([`<task-branch>`](#task-branch-placeholder)).
