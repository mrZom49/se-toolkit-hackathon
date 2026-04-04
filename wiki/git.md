# `Git`

<h2>Table of contents</h2>

- [What is `Git`](#what-is-git)
- [Repository](#repository)
- [Remote](#remote)
  - [`<remote>` placeholder](#remote-placeholder)
- [Root directory of the repository](#root-directory-of-the-repository)
- [Commit](#commit)
  - [Commit hash](#commit-hash)
  - [`<git-commit-hash>`](#git-commit-hash)
  - [Commit message](#commit-message)
  - [`Conventional Commits`](#conventional-commits)
    - [Common commit message prefixes in `Conventional Commits`](#common-commit-message-prefixes-in-conventional-commits)
- [Branch](#branch)
  - [`main` branch](#main-branch)
  - [`<branch>` placeholder](#branch-placeholder)
- [Revision](#revision)
- [How `Git` works - text](#how-git-works---text)
- [How `Git` works - videos](#how-git-works---videos)
- [Merge conflict](#merge-conflict)
- [Practice `Git`](#practice-git)
- [`.gitignore`](#gitignore)
- [Submodule](#submodule)
- [`GitHub flow`](#github-flow)
- [Check your `Git` config](#check-your-git-config)
- [Configure `Git`](#configure-git)
  - [Configure `user.name`](#configure-username)
  - [Configure `user.email`](#configure-useremail)

<!-- TODO improve docs -->

## What is `Git`

`Git` is a distributed version control system that tracks changes in your files and lets multiple people collaborate on the same codebase. It records a history of every change, so you can revert mistakes, compare versions, and work on features in parallel using branches.

Docs:

- [Git Reference](https://git-scm.com/doc)
- [Git Cheat Sheet](https://git-scm.com/cheat-sheet)

## Repository

A repository (or "repo") is a storage location for files that are version-controlled using [`Git`](./git.md#what-is-git).

Example: [`GitHub` repository](./github.md#github-repository)

## Remote

A remote (remote repository) is a version of your [repository](./git.md#repository) hosted on a [remote host](./computer-networks.md#remote-host), e.g. [`GitHub`](./github.md#what-is-github).

Remotes let you push and pull changes between your local repository and the remote host.

You can [inspect remotes in `VS Code`](./gitlens.md#inspect-the-remotes).

Docs:

- [Git Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)

See also [`upstream`](./github.md#upstream) and [`origin`](./github.md#origin).

### `<remote>` placeholder

A [remote](#remote) name (without `<` and `>`).

Common remote names:

- [`origin`](./github.md#origin) — your fork on `GitHub`.
- [`upstream`](./github.md#upstream) — the original repository that was forked.

## Root directory of the repository

<!-- TODO -->

## Commit

A commit is a snapshot of your project at a specific point in time. Each commit records what changed since the previous commit, who made the change, and a [commit message](#commit-message) describing why. Commits form a history that you can browse, revert, or branch from.

### Commit hash

A hash of a commit in `Git`.

Example: `4aeacb54f898125560c545e5e0477762094027a7`

Docs:

- [Git Has Integrity](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#_git_has_integrity)
- [Revision Selection - Short SHA-1](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#_short_sha_1)

### `<git-commit-hash>`

A [commit hash](#commit-hash) (without `<` and `>`).

### Commit message

A commit message is a short description attached to each commit. It explains **what** was changed and **why**. Good commit messages make the project history readable and help teammates understand changes without reading the code.

Guidelines:

- Keep the first line short (under 72 characters).
- Use the imperative mood ("add feature", not "added feature").
- Focus on why the change was made, not just what changed.
- (Optional) follow the [`Conventional Commits`](#conventional-commits) specification.

### `Conventional Commits`

Rules for creating human- and machine-readable commit history.

Docs:

- [`Conventional Commits`](https://www.conventionalcommits.org/en/v1.0.0/).

#### Common commit message prefixes in `Conventional Commits`

- `feat:` for new functionality.
- `fix:` for bug fixes.
- `docs:` for documentation changes.
- `refactor:` for code changes without behavior changes.

## Branch

A branch is an independent line of development. It lets you work on a feature or fix in isolation without affecting the [`main` branch](#main-branch). Under the hood, a branch is a movable pointer to a [commit](#commit) — as you add new commits, the pointer advances.

Branches are central to the [`GitHub flow`](#github-flow): you create a branch, commit changes to it, open a pull request, and merge it back into `main` when ready.

Docs:

- [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

### `main` branch

`main` is typically the default branch of a [repository](./git.md#repository).

It represents the stable, up-to-date state of the project.

### `<branch>` placeholder

A [`Git` branch](#branch) name (without `<` and `>`).

Examples:

- `main`
- `dev`
- `upstream/dev`

## Revision

Typically a [commit hash](#commit-hash) or the branch name.

Docs:

- [Revision selection](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection).

## How `Git` works - text

- Read this [tutorial](https://hackmd.io/@aabounegm/SWP-git) to learn about `Git`, `Github`, and other `Git` workflows.

Quick mental model:

- `Working tree`: your local files.
- `Staging area`: selected changes for the next commit (`git add`).
- `Commit`: a save point of your progress since the previous save point (`git commit`).
- `Commit history`: a timeline of these save points.

Simple view:

```text
working tree changes -> git add -> git commit
                         (stage)     (save progress)
```

Useful commands:

```terminal
git status
git add <file-path>
git commit -m "docs: update wiki"
git log --oneline --decorate --graph -n 15
```

See [`<file-path>`](./file-system.md#file-path-placeholder).

When confused, start with `git status` and read it carefully before running the next command.

## How `Git` works - videos

- Watch videos to build your mental model of how `Git` works:
  - [Git Explained in 100 Seconds](https://www.youtube.com/watch?v=hwP7WQkmECE)
  - [What is Git? Explained in 2 Minutes!](https://www.youtube.com/watch?v=2ReR1YJrNOM)
  - [A brief introduction to Git for beginners](https://www.youtube.com/watch?v=r8jQ9hVA2qs)
  - [How Git Works: Explained in 4 Minutes](https://www.youtube.com/watch?v=e9lnsKot_SQ)
  - [Git MERGE vs REBASE: Everything You Need to Know](https://www.youtube.com/watch?v=0chZFIZLR_0)

## Merge conflict

A merge conflict occurs when two branches modify the same lines in a file and `Git` cannot automatically decide which version to keep.
Conflicts happen during `git merge` or `git pull`.

`Git` marks conflicting sections with conflict markers:

```text
<<<<<<< HEAD
Your changes on the current branch.
=======
Changes from the other branch.
>>>>>>> other-branch
```

To resolve a conflict: choose which version to keep (or combine them), then remove all conflict markers, and commit the result.

See [Resolve a merge conflict](./git-vscode.md#resolve-a-merge-conflict).

## Practice `Git`

- Practice on [Learn Git Branching](https://learngitbranching.js.org/) (focus on merge/rebase and conflicts).

## `.gitignore`

The `.gitignore` file allows you to specify which files shouldn't be added to the repo.

Examples:

- [`.gitignore`](../.gitignore)
- [`client-web-react/.gitignore`](../client-web-react/.gitignore)

Common ignored files:

- Secrets (`.env` files, keys, tokens).
- Build artifacts (`dist/`, `build/`).
- Local caches and temporary files.

## Submodule

A submodule is a [`Git` repository](#repository) embedded inside another `Git` repository.

It lets you include external projects (e.g., a shared library or service) as a subdirectory while keeping their history separate.

The parent repository tracks a specific [commit](#commit) of the submodule — not its full contents.

Docs:

- [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

## `GitHub flow`

- Read about the [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow).

Typical sequence:

1. Create an issue.
2. Create a branch from `main`.
3. Commit changes to the branch.
4. Push branch.
5. Open a PR.
6. Get review.
7. Merge the branch to `main`.

## Check your `Git` config

1. To find out which name and email are used in [commits](#commit),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git config --global --list
   ```

   The output should look like this (but with your values):

   ```terminal
   user.name=Inno SE Toolkit
   user.email=inno-se-toolkit@gmail.com
   ```

## Configure `Git`

> [!NOTE]
> See [docs](https://git-scm.com/docs/git-config#Documentation/git-config.txt-username) about `user.name` and `user.email`.

Complete the following steps:

1. [Check your `Git` config](#check-your-git-config).
2. [Configure `user.name`](#configure-username).
3. [Configure `user.email`](#configure-useremail).

### Configure `user.name`

1. To set the name that will be used in [commits](#commit),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git config --global user.name '<your-name>'
   ```

   Example: `git config --global user.name 'Inno SE Toolkit'`

### Configure `user.email`

1. To set the email that will be used in [commits](#commit),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git config --global user.email '<your-email>'
   ```

   Example: `git config --global user.email 'inno-se-toolkit@gmail.com'`
