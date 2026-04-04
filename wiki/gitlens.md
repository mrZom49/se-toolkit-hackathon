# `GitLens`

<h2>Table of contents</h2>

- [What is `GitLens`](#what-is-gitlens)
- [`GitLens` features](#gitlens-features)
- [Open the `GITLENS` view](#open-the-gitlens-view)
- [See all branches](#see-all-branches)
  - [See all branches using the `Status Bar`](#see-all-branches-using-the-status-bar)
  - [See all branches using the `GITLENS` view](#see-all-branches-using-the-gitlens-view)
- [Open the commit graph](#open-the-commit-graph)
  - [Open the commit graph using the `Status Bar`](#open-the-commit-graph-using-the-status-bar)
  - [Open the commit graph using the `Command Palette`](#open-the-commit-graph-using-the-command-palette)
- [Look at the commit graph](#look-at-the-commit-graph)
- [Open commits on the current branch](#open-commits-on-the-current-branch)
- [View changes in a commit on the current branch](#view-changes-in-a-commit-on-the-current-branch)
- [Open a commit menu on the current branch](#open-a-commit-menu-on-the-current-branch)
- [Undo a commit on the current branch](#undo-a-commit-on-the-current-branch)
- [Inspect the current branch](#inspect-the-current-branch)
- [Inspect the remotes](#inspect-the-remotes)

## What is `GitLens`

`GitLens` is a [`VS Code`](vs-code.md) extension that simplifies the work with `Git` inside `VS Code`.

## `GitLens` features

See [`GitLens` features](https://help.gitkraken.com/gitlens/gitlens-features/).

## Open the `GITLENS` view

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Click `GITLENS` to uncollapse the view.

## See all branches

See all branches using any of the following methods:

<!-- no toc -->
- [See all branches using the `Status Bar`](#see-all-branches-using-the-status-bar)
- [See all branches using the `GITLENS` view](#see-all-branches-using-the-gitlens-view)

### See all branches using the `Status Bar`

1. Go to the [`Status Bar`](./vs-code.md#status-bar).
2. Look at the branch name.

   <img alt="Current branch" src="./images/gitlens/status-bar-current-branch.png" style="width:400px"></img>
3. Click it to see all available branches.
4. If you click a branch, you'll be able to switch to it.

### See all branches using the `GITLENS` view

1. [Open the `GITLENS` view](#open-the-gitlens-view).
2. Click the icon `Branches`.

   <img alt="View Branches" src="./images/gitlens/view-branches.png" style="width:400px"></img>

## Open the commit graph

Open the commit graph using any of the following methods:

<!-- no toc -->
- [Open the commit graph using the `Status Bar`](#open-the-commit-graph-using-the-status-bar)
- [Open the commit graph using the `Command Palette`](#open-the-commit-graph-using-the-command-palette)

### Open the commit graph using the `Status Bar`

1. Go to the [`Status Bar`](./vs-code.md#status-bar).
2. Click the icon `Visualize commits on the Commit Graph`.

   <img alt="Status Bar Commit Graph" src="./images/gitlens/status-bar-commit-graph.png" style="width:400px"></img>

### Open the commit graph using the `Command Palette`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Show Commit Graph`

## Look at the commit graph

See [Open the commit graph](#open-the-commit-graph).

## Open commits on the current branch

1. [Open the `GITLENS` view](#open-the-gitlens-view).
2. Click the icon `Commits`.

   <img alt="View Commits" src="./images/gitlens/view-commits.png" style="width:400px"></img>
3. Look at something like `- on <branch> fetched 1 minute ago`.
4. Below that text are the commits on the branch [`<branch>`](./git.md#branch-placeholder).
5. Here, the latest not pushed commit is highlighted:

   <img alt="Latest commit" src="./images/gitlens/view-commits-latest.png" style="width:400px"></img>

## View changes in a commit on the current branch

1. [Open commits on the current branch](#open-commits-on-the-current-branch).
2. Click a commit to open a list of files changed in that commit.
3. Click a file changed in that commit to see changes in that file.

## Open a commit menu on the current branch

1. [Open commits on the current branch](#open-commits-on-the-current-branch).
2. Right click a commit.
3. A menu will open that shows possible actions with the commit.

## Undo a commit on the current branch

1. [Open the commit menu on the current branch](#open-a-commit-menu-on-the-current-branch).
2. Click `Undo Commit` in the menu.
3. The commit will be undone.
4. Changes from the commit will be added to `Staged Changes`.

## Inspect the current branch

Inspect the current branch using these sections:

1. [Open commits on the current branch](#open-commits-on-the-current-branch).
2. [View changes in a commit on the current branch](#view-changes-in-a-commit-on-the-current-branch).

## Inspect the remotes

1. [Open the `GITLENS` view](#open-the-gitlens-view).
2. Hover over the `GITLENS` view name.
3. Click the icon `Remotes`.

    <img alt="View Remotes" src="./images/gitlens/view-remotes.png" style="width:400px"></img>
4. (Optional) Make sure [`origin`](./github.md#origin) points to [`<your-fork-url>`](./github.md#your-fork-url-placeholder):
   1. Hover over `origin`.
   2. Look at URLs for fetching and pushing changes.

      They should both be `<your-fork-url>`.
