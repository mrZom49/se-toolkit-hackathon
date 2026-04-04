# `Git` in `VS Code`

<h2>Table of contents</h2>

- [What is `Git` in `VS Code`](#what-is-git-in-vs-code)
- [Clone the repository](#clone-the-repository)
  - [Clone the repository using the `VS Code Terminal`](#clone-the-repository-using-the-vs-code-terminal)
  - [Clone the repository using the `Command Palette`](#clone-the-repository-using-the-command-palette)
- [Update submodules using the `VS Code Terminal`](#update-submodules-using-the-vs-code-terminal)
- [Switch to the branch `<branch>`](#switch-to-the-branch-branch)
  - [Switch to the branch `<branch>` using the `VS Code Terminal`](#switch-to-the-branch-branch-using-the-vs-code-terminal)
  - [Switch to the branch `<branch>` using `GitLens`](#switch-to-the-branch-branch-using-gitlens)
- [Switch to a new branch](#switch-to-a-new-branch)
  - [Switch to a new branch using `GitHub`](#switch-to-a-new-branch-using-github)
  - [Switch to a new branch using the `VS Code Terminal`](#switch-to-a-new-branch-using-the-vs-code-terminal)
  - [Switch to a new branch using `GitLens`](#switch-to-a-new-branch-using-gitlens)
- [Fetch the branch `<branch>` using the `VS Code Terminal`](#fetch-the-branch-branch-using-the-vs-code-terminal)
- [Detect conflicts](#detect-conflicts)
  - [Detect conflicts using the `VS Code Terminal`](#detect-conflicts-using-the-vs-code-terminal)
  - [Detect conflicts using `GitLens`](#detect-conflicts-using-gitlens)
- [Hard reset the branch `<branch>`](#hard-reset-the-branch-branch)
- [Resolve a merge conflict](#resolve-a-merge-conflict)
  - [Resolve a merge conflict using `VS Code`](#resolve-a-merge-conflict-using-vs-code)
  - [Resolve a merge conflict using `GitLens`](#resolve-a-merge-conflict-using-gitlens)
  - [Resolve a merge conflict using the `VS Code Terminal`](#resolve-a-merge-conflict-using-the-vs-code-terminal)
- [Pull changes from the branch `<branch>` on `<remote>`](#pull-changes-from-the-branch-branch-on-remote)
  - [Pull changes from the branch `<branch>` on `<remote>` using the `VS Code Terminal`](#pull-changes-from-the-branch-branch-on-remote-using-the-vs-code-terminal)
  - [Pull changes from the branch `<branch>` on `<remote>` using `GitLens`](#pull-changes-from-the-branch-branch-on-remote-using-gitlens)
- [Pull changes from the branch `<branch>` on `<remote>` and rebase](#pull-changes-from-the-branch-branch-on-remote-and-rebase)
  - [Pull and rebase using the `VS Code Terminal`](#pull-and-rebase-using-the-vs-code-terminal)
  - [Pull and rebase using `GitLens`](#pull-and-rebase-using-gitlens)
- [Stage changes using the `Source Control`](#stage-changes-using-the-source-control)
  - [Stage all changes in a specific file](#stage-all-changes-in-a-specific-file)
  - [Stage all changes in specific files](#stage-all-changes-in-specific-files)
  - [Stage specific changes in a specific file](#stage-specific-changes-in-a-specific-file)
- [Unstage specific changes](#unstage-specific-changes)
- [Commit changes](#commit-changes)
  - [Commit using the `VS Code Terminal`](#commit-using-the-vs-code-terminal)
  - [Commit using `Source Control`](#commit-using-source-control)
    - [Commit staged changes](#commit-staged-changes)
- [Undo commits](#undo-commits)
  - [Undo commits using the `VS Code Terminal`](#undo-commits-using-the-vs-code-terminal)
  - [Undo commits using `GitLens`](#undo-commits-using-gitlens)
- [Publish the branch](#publish-the-branch)
  - [Publish using the `VS Code Terminal`](#publish-using-the-vs-code-terminal)
  - [Publish using `GitLens`](#publish-using-gitlens)
- [Push more commits](#push-more-commits)
  - [Push using the `VS Code Terminal`](#push-using-the-vs-code-terminal)
  - [Push using `GitLens`](#push-using-gitlens)

## What is `Git` in `VS Code`

`VS Code` has built-in [`Git`](./git.md#what-is-git) support and can be extended with [`GitLens`](./gitlens.md#what-is-gitlens) for advanced operations. This page covers common `Git` workflows in `VS Code`, including cloning, branching, committing, and pushing.

Docs:

- [`Git` support in `VS Code`](https://code.visualstudio.com/docs/sourcecontrol/overview)

## Clone the repository

> [!NOTE]
> See [`<repo-url>`](./github.md#repo-url-placeholder), [`<repo-name>`](./github.md#repo-name-placeholder).

<!-- no toc -->
- Method 1: [Clone the repository using the `VS Code Terminal`](#clone-the-repository-using-the-vs-code-terminal)
- Method 2: [Clone the repository using the `Command Palette`](#clone-the-repository-using-the-command-palette)

### Clone the repository using the `VS Code Terminal`

1. To clone the repository,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   - Case 1: You want to specify the `<path>`:

     ```terminal
     git clone <repo-url> <path>
     ```

   - Case 2: You want to clone in the [current working directory](./shell.md#current-working-directory) and use the `<repo-name>` as `<path>`:

     ```terminal
     git clone <repo-url>
     ```

   - Case 3: You want to clone a repository with submodules and specify the `<path>`:

     ```terminal
     git clone --recurse-submodules <repo-url> <path>
     ```

   Replace the placeholders:

   - [`<repo-url>`](./github.md#repo-url-placeholder)
   - [`<path>`](./file-system.md#path-placeholder) with the desired path of the repository directory

   Example:

   ```terminal
   git clone https://github.com/microsoft/vscode ~/vscode
   ```

   See [Home directory (`~`)](./file-system.md#home-directory-).

   > <h3>Troubleshooting</h3>
   >
   > [**`git` asks for a password**](./github.md#git-asks-for-a-password)
   >
   > [**`fatal: destination path <path> already exists and is not an empty directory.`**](./github.md#fatal-destination-path-directory-path-already-exists-and-is-not-an-empty-directory)

2. To verify that the repository isn't empty,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ls <path>
   ```

   The output should be the list of names of files in the repository.

   Example:

   ```terminal
   ls ~/vscode
   ```

### Clone the repository using the `Command Palette`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Git: Clone`.
2. Click `Clone from GitHub`.
3. Allow the extension to sign in.
4. Paste the [`<repo-url>`](./github.md#repo-url-placeholder).
5. [Select](./vs-code.md#select-an-option-from-a-list) the repo.
6. Choose a directory where to clone the repository.
7. Confirm the choice.

## Update submodules using the `VS Code Terminal`

1. To check out missing submodules and update all submodules,
  
   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git submodule update --init
   ```

## Switch to the branch `<branch>`

<!-- no toc -->
- Method 1: [Switch to the branch `<branch>` using the `VS Code Terminal`](#switch-to-the-branch-branch-using-the-vs-code-terminal)
- Method 2: [Switch to the branch `<branch>` using `GitLens`](#switch-to-the-branch-branch-using-gitlens)

### Switch to the branch `<branch>` using the `VS Code Terminal`

1. To switch to the branch `<branch>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git switch <branch>
   ```

   Replace the placeholder [`<branch>`](./git.md#branch-placeholder).

   Example:

   ```terminal
   git switch main
   ```

### Switch to the branch `<branch>` using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Git Switch to..`.
2. [Select](./vs-code.md#select-an-option-from-a-list) the branch `<branch>`.

## Switch to a new branch

<!-- no toc -->
- Method 1: [Switch to a new branch using `GitHub`](#switch-to-a-new-branch-using-github)
- Method 2: [Switch to a new branch using the `VS Code Terminal`](#switch-to-a-new-branch-using-the-vs-code-terminal)
- Method 3: [Switch to a new branch using `GitLens`](#switch-to-a-new-branch-using-gitlens)

### Switch to a new branch using `GitHub`

1. [Go to the repo](./github.md#go-to-your-fork).
2. [Create a branch](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue).
3. Copy the command provided by `GitHub`.

   It looks like this:

   ```terminal
   git fetch origin
   git checkout <branch>
   ```

   Replace the placeholder [`<branch>`](./git.md#branch-placeholder).

4. [Run the copied command using the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal).

### Switch to a new branch using the `VS Code Terminal`

1. To create and switch to a new branch,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git checkout -b <branch>
   ```

   Replace the placeholder [`<branch>`](./git.md#branch-placeholder).

### Switch to a new branch using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Git Create Branch...`.
2. [Select](./vs-code.md#select-an-option-from-a-list)
   `main` as the base branch.
3. Write the new branch name (we refer to this name as [`<branch>`](./git.md#branch-placeholder)).
4. Press `Enter` to confirm.
5. [Select](./vs-code.md#select-an-option-from-a-list)
   `Create & Switch to Branch`.

## Fetch the branch `<branch>` using the `VS Code Terminal`

1. To fetch the latest changes from the branch `<branch>` on `<remote>` to the local branch `<branch>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git fetch <remote> <branch>
   ```

   Replace the placeholders:

   - [`<remote>`](./git.md#remote-placeholder)
   - [`<branch>`](./git.md#branch-placeholder) with the branch that you want to fetch changes for.

   Example:

   ```terminal
   git fetch origin main
   ```

## Detect conflicts

It can happen that commits on the branch [`<branch>`](./git.md#branch-placeholder) on the remote [`<remote>`](./git.md#remote-placeholder) are different from commits on the local branch `<branch>` in the cloned repo on your computer.

- Method 1: [Detect conflicts using `GitLens`](#detect-conflicts-using-gitlens)
- Method 2: [Detect conflicts using the `VS Code Terminal`](#detect-conflicts-using-the-vs-code-terminal)

### Detect conflicts using the `VS Code Terminal`

1. [Fetch the branch `<branch>` using the `VS Code Terminal`](#fetch-the-branch-branch-using-the-vs-code-terminal).

2. To compare the local branch [`<branch>`](./git.md#branch-placeholder) with the branch `<branch>` on the remote `<remote>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git status
   ```

   If the output contains `Your branch is behind`, `Your branch is ahead`, or `have diverged`, there are differences between the local and remote branches.

### Detect conflicts using `GitLens`

1. Look at the [`Status Bar`](./vs-code.md#status-bar).

   <img alt="Commit Conflict" src="./images/vs-code/status-bar-commit-conflict.png" style="width:400px"></img>

   You should see that there is a non-zero number of commits to pull from the branch `<branch>` on `<remote>`.

## Hard reset the branch `<branch>`

> [!NOTE]
>
> This operation will make the local branch `<branch>` match the branch `<branch>` on `<remote>`.

> [!CAUTION]
> This operation discards all uncommitted changes and local commits that are not on the [`<remote>`](./git.md#remote-placeholder).

1. [Fetch the branch `<branch>`](#fetch-the-branch-branch-using-the-vs-code-terminal).

2. To hard reset the local branch `<branch>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git reset --hard <remote>/<branch>
   ```

   Replace the placeholders:

   - [`<remote>`](./git.md#remote-placeholder)
   - [`<branch>`](./git.md#branch-placeholder)

   Example:

   ```terminal
   git reset --hard origin/main
   ```

## Resolve a merge conflict

Resolve a [merge conflict](./git.md#merge-conflict).

<!-- no toc -->
- Method 1: [Resolve a merge conflict using `VS Code`](#resolve-a-merge-conflict-using-vs-code)
- Method 2: [Resolve a merge conflict using `GitLens`](#resolve-a-merge-conflict-using-gitlens)
- Method 3: [Resolve a merge conflict using the `VS Code Terminal`](#resolve-a-merge-conflict-using-the-vs-code-terminal)

### Resolve a merge conflict using `VS Code`

`VS Code` has a built-in merge conflict editor.

1. Open a file with conflicts.
2. Use the inline options that appear above the conflict markers:
   - `Accept Current Change` — keep your branch's version.
   - `Accept Incoming Change` — keep the other branch's version.
   - `Accept Both Changes` — keep both versions.
3. Save the file.
4. To stage the resolved file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git add <file-path>
   ```

5. To continue the merge,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git merge --continue
   ```

Docs:

- [Merge conflicts in `VS Code`](https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts)

### Resolve a merge conflict using `GitLens`

If you see a pull error like the one below, resolve the conflicts:

<img alt="Pull Error" src="./images/gitlens/pull-error.png" style="width:400px"></img>

For each conflicting file, complete the following steps:

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Merge Changes`.
3. Click a conflicting file.
4. Click `Resolve in Merge Editor`.
5. Accept the changes that you want to keep.
6. Click `Complete Merge`.
7. [Open the `Source Control`](./vs-code.md#open-the-source-control).
8. Click `Continue`.

> [!NOTE]
> If there are more conflicts, `VS Code` shows `Merging (1/3)` or `Rebasing (1/3)` (or similar).
> Repeat the steps above for each remaining conflict.

### Resolve a merge conflict using the `VS Code Terminal`

1. To see which files have conflicts,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git status
   ```

   Files with conflicts are listed under `Unmerged paths`.

2. Open each conflicted file.
3. Find the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Edit the file to keep the correct content.
5. Remove all conflict markers from the file.
6. To stage the resolved file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git add <file-path>
   ```

7. To continue the merge,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git merge --continue
   ```

## Pull changes from the branch `<branch>` on `<remote>`

> [!NOTE]
> See [`<branch>`](./git.md#branch-placeholder), [`<remote>`](./git.md#remote-placeholder).

<!-- no toc -->
- Method 1: [Pull changes from the branch `<branch>` on `<remote>` using the `VS Code Terminal`](#pull-changes-from-the-branch-branch-on-remote-using-the-vs-code-terminal)
- Method 2: [Pull changes from the branch `<branch>` on `<remote>` using `GitLens`](#pull-changes-from-the-branch-branch-on-remote-using-gitlens)

### Pull changes from the branch `<branch>` on `<remote>` using the `VS Code Terminal`

1. To pull changes from the branch `<branch>` on `<remote>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git pull <remote> <branch>
   ```

   Example:

   ```terminal
   git pull origin main
   ```

### Pull changes from the branch `<branch>` on `<remote>` using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Pull`.

## Pull changes from the branch `<branch>` on `<remote>` and rebase

<!-- no toc -->
- Method 1: [Pull and rebase using the `VS Code Terminal`](#pull-and-rebase-using-the-vs-code-terminal)
- Method 2: [Pull and rebase using `GitLens`](#pull-and-rebase-using-gitlens)

### Pull and rebase using the `VS Code Terminal`

1. To pull changes from the branch `<branch>` on `<remote>` and rebase onto it,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git pull --rebase <remote> <branch>
   ```

   Example:

   ```terminal
   git pull --rebase origin main
   ```

   > <h3>Troubleshooting</h3>
   >
   > [**`git` asks for a password**](./github.md#git-asks-for-a-password)

### Pull and rebase using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Pull`.
2. [Select](./vs-code.md#select-an-option-from-a-list)
   `Pull with Rebase`.
3. If `GitLens` does not show any error, the rebase is complete.

## Stage changes using the `Source Control`

<!-- no toc -->
- Method 1: [Stage all changes in a specific file](#stage-all-changes-in-a-specific-file)
- Method 2: [Stage all changes in specific files](#stage-all-changes-in-specific-files)
- Method 3: [Stage specific changes in a specific file](#stage-specific-changes-in-a-specific-file)

### Stage all changes in a specific file

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Changes`.
3. Hover over the file name.
4. Click the `+` icon next to the file name.

### Stage all changes in specific files

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Changes`.
3. Select multiple files by holding `Ctrl` and clicking each file.
4. Right mouse click the selected files.
5. Click `Stage Changes`.

### Stage specific changes in a specific file

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Changes`.
3. Click a file to open it.
4. Select changed lines in the editor (red-green).
5. Right mouse click the selected lines.
6. Click `Stage Selected Ranges`.

## Unstage specific changes

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Staged Changes`.
3. Click a file.
4. Select changed lines in the editor (red-green).
5. Right mouse click the selected lines.
6. Click `Unstage Selected Ranges`.

## Commit changes

> [!NOTE]
> Commit message format is: `type: short description`
>
> Common types:
>
> - `fix:` — bug fixes
> - `feat:` — additions (e.g., new feature)
> - `docs:` — documentation changes

<!-- no toc -->
- Method 1: [Commit using the `VS Code Terminal`](#commit-using-the-vs-code-terminal)
- Method 2: [Commit using `Source Control`](#commit-using-source-control)
  - [Commit staged changes](#commit-staged-changes)

### Commit using the `VS Code Terminal`

1. Open the [`VS Code Terminal`](./vs-code.md#open-the-vs-code-terminal).

2. To stage your changes,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git add <file-path>
   ```

   See [`<file-path>`](./file-system.md#file-path-placeholder).

   Example:

   ```terminal
   git add README.md
   ```

   Example (path with spaces):

   ```terminal
   git add 'path/some image.svg'
   ```

3. To commit your changes,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git commit -m '<type>: <short description>'
   ```

   Example:

   ```terminal
   git commit -m 'docs: add architecture diagram'
   ```

### Commit using `Source Control`

1. [Stage changes using the `Source Control`](#stage-changes-using-the-source-control).
2. [Commit staged changes](#commit-staged-changes).

#### Commit staged changes

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Write a [commit message](./git.md#commit-message).
3. Click `Commit`.

## Undo commits

> [!NOTE]
> There can appear a merge [conflict](./git.md#merge-conflict) when you try to undo.

<!-- no toc -->
- Method 1: [Undo commits using the `VS Code Terminal`](#undo-commits-using-the-vs-code-terminal)
- Method 2: [Undo commits using `GitLens`](#undo-commits-using-gitlens)

### Undo commits using the `VS Code Terminal`

1. To undo the last commit and keep the changes staged,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git reset --soft HEAD~1
   ```

   Your changes are staged now.

2. To stage more changes,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git add some-file
   ```

3. To commit using the previous message,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git commit -C ORIG_HEAD
   ```

### Undo commits using `GitLens`

See [Undo commit on the current branch](./gitlens.md#undo-a-commit-on-the-current-branch).

## Publish the branch

<!-- no toc -->
- Method 1: [Publish using the `VS Code Terminal`](#publish-using-the-vs-code-terminal)
- Method 2: [Publish using `GitLens`](#publish-using-gitlens)

### Publish using the `VS Code Terminal`

1. To publish the branch to `origin`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git push -u origin <branch>
   ```

### Publish using `GitLens`

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Click `GITLENS` to open the `GitLens` panel.
3. Click the `Commits` icon.
4. Click the `Publish Branch` icon to the right of `Publish <branch> to GitHub`.
5. Press `Enter` to confirm.

## Push more commits

<!-- no toc -->
- Method 1: [Push using the `VS Code Terminal`](#push-using-the-vs-code-terminal)
- Method 2: [Push using `GitLens`](#push-using-gitlens)

### Push using the `VS Code Terminal`

1. To push commits to the remote,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git push
   ```

### Push using `GitLens`

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Click `GITLENS`.
3. Click the `Commits` icon.
4. Click the `Push` icon to the right of `COMMITS`.
