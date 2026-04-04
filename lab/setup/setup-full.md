# Lab setup

- [1. Required steps](#1-required-steps)
  - [1.1. (UPD) Find a partner](#11-upd-find-a-partner)
  - [1.2. Start creating a VM](#12-start-creating-a-vm)
  - [1.3. Set up your fork (LOCAL)](#13-set-up-your-fork-local)
    - [1.3.1. Sign in on `GitHub`](#131-sign-in-on-github)
    - [1.3.2. (UPD) Fork the course instructors' repo](#132-upd-fork-the-course-instructors-repo)
    - [1.3.3. (UPD) Go to your fork](#133-upd-go-to-your-fork)
    - [1.3.4. (UPD) Enable issues](#134-upd-enable-issues)
    - [1.3.5. (UPD) Add a classmate as a collaborator](#135-upd-add-a-classmate-as-a-collaborator)
    - [1.3.6. (UPD) Protect your `main` branch](#136-upd-protect-your-main-branch)
  - [1.4. Set up tools (LOCAL)](#14-set-up-tools-local)
    - [1.4.1. (UPD) Set up `VS Code`](#141-upd-set-up-vs-code)
    - [1.4.2. (UPD) Set up `Docker`](#142-upd-set-up-docker)
    - [1.4.3. (UPD) (`Windows` only) Switch to the `Linux` shell for the `VS Code Terminal`](#143-upd-windows-only-switch-to-the-linux-shell-for-the-vs-code-terminal)
    - [1.4.4. (UPD) Clean up `Docker`](#144-upd-clean-up-docker)
    - [1.4.5. Set up `Git`](#145-set-up-git)
  - [1.5. (UPD) Open in `VS Code` the `software-engineering-toolkit` directory (LOCAL)](#15-upd-open-in-vs-code-the-software-engineering-toolkit-directory-local)
  - [1.6. Clone your fork](#16-clone-your-fork)
    - [1.6.1. (UPD) Copy your fork URL](#161-upd-copy-your-fork-url)
    - [1.6.2. (UPD) Clone your fork (LOCAL)](#162-upd-clone-your-fork-local)
  - [1.7. (UPD) Set up `VS Code` in the lab repository directory (LOCAL)](#17-upd-set-up-vs-code-in-the-lab-repository-directory-local)
  - [1.8. Create a new VM](#18-create-a-new-vm)
  - [1.9. Set up `Python`](#19-set-up-python)
    - [1.9.1. Install `uv` (LOCAL)](#191-install-uv-local)
    - [1.9.2. (UPD) Set up `Python` in `VS Code` (LOCAL)](#192-upd-set-up-python-in-vs-code-local)
  - [1.10. Set up `Node.js`](#110-set-up-nodejs)
    - [1.10.1. Install `Node.js` (LOCAL)](#1101-install-nodejs-local)
    - [1.10.2. (UPD) Install `pnpm` (LOCAL)](#1102-upd-install-pnpm-local)
  - [1.11. (UPD) Set up `Qwen Code` (LOCAL)](#111-upd-set-up-qwen-code-local)
  - [1.12. Set up the VM](#112-set-up-the-vm)
  - [1.13. (UPD) Clone your fork on the VM (REMOTE)](#113-upd-clone-your-fork-on-the-vm-remote)
  - [1.14. (UPD) Deploy the LMS API (REMOTE)](#114-upd-deploy-the-lms-api-remote)
  - [1.15. (UPD) Set up the `Qwen Code` API (REMOTE)](#115-upd-set-up-the-qwen-code-api-remote)
  - [1.16. Optional: create a `Telegram` bot token](#116-optional-create-a-telegram-bot-token)
  - [1.17. Set up the `Autochecker` bot](#117-set-up-the-autochecker-bot)
  - [1.18. Check the setup using the `Autochecker` bot](#118-check-the-setup-using-the-autochecker-bot)
- [2. Optional steps](#2-optional-steps)
  - [2.1. (UPD) Set up `gh` (LOCAL)](#21-upd-set-up-gh-local)
  - [2.2. Set up `Nix` (LOCAL)](#22-set-up-nix-local)
  - [2.3. Set up `direnv` (LOCAL)](#23-set-up-direnv-local)
  - [2.4. Learn to go back after clicking a link (LOCAL)](#24-learn-to-go-back-after-clicking-a-link-local)
  - [2.5. Set up the shell prompt (LOCAL)](#25-set-up-the-shell-prompt-local)
  - [2.6. Customize the `Source Control` (LOCAL)](#26-customize-the-source-control-local)
  - [2.7. Get familiar with `GitLens` (LOCAL)](#27-get-familiar-with-gitlens-local)
  - [2.8. Create a label for tasks (`GitHub`)](#28-create-a-label-for-tasks-github)
  - [2.9. View `Markdown` files in `VS Code` (LOCAL)](#29-view-markdown-files-in-vs-code-local)

## 1. Required steps

> [!IMPORTANT]
> Complete all steps if you haven't completed the full setup in previous labs.
>
> Otherwise, complete just the steps with the `(UPD)` label to get the right setup for this lab.

> [!IMPORTANT]
> Complete the steps with the label:
>
> - `(LOCAL)` - on your local machine (laptop).
>
> - `(REMOTE)` - on your VM.

> [!NOTE]
> We provide the hardest setup steps before all other tasks
> so that TAs can help you resolve issues during the lab.
>
> Tasks are doable when you have the right setup.

### 1.1. (UPD) Find a partner

1. Find a partner for this lab.
2. Sit next to them.

> [!IMPORTANT]
> You work on tasks independently from your partner.
>
> You and your partner work together when reviewing each other's work.

### 1.2. Start creating a VM

> [!TIP]
> Skip this step if you can [connect to your VM as the user `admin`](../../wiki/vm-access.md#connect-to-the-vm-as-the-user-user-local).

1. [Create a subscription](../../wiki/vm.md#create-a-subscription) to be able to create a VM.

> [!TIP]
> Subscription approval may take time.
> Continue with the next steps while you wait — you will
> [set up the VM](#112-set-up-the-vm) later.

### 1.3. Set up your fork (LOCAL)

#### 1.3.1. Sign in on `GitHub`

1. Sign in on [`GitHub`](https://github.com/).
2. [Find `<your-github-username>`](../../wiki/github.md#find-your-github-username).

#### 1.3.2. (UPD) Fork the course instructors' repo

1. [Fork the course instructors' repo](../../wiki/github.md#fork-a-repo).

   The course instructors' repo [URL](../../wiki/computer-networks.md#url) is <https://github.com/inno-se-toolkit/se-toolkit-lab-8>.

#### 1.3.3. (UPD) Go to your fork

1. [Go to your fork](../../wiki/github.md#go-to-your-fork).

   The [URL](../../wiki/computer-networks.md#url) of your fork should look like `https://github.com/<your-github-username>/se-toolkit-lab-8`.

   See [`<your-github-username>`](../../wiki/github.md#your-github-username-placeholder).

#### 1.3.4. (UPD) Enable issues

1. [Enable issues](../../wiki/github.md#enable-issues).

#### 1.3.5. (UPD) Add a classmate as a collaborator

1. [Add a collaborator](../../wiki/github.md#add-a-collaborator) — your partner.
2. Your partner should add you as a collaborator in their repo.

> [!NOTE]
> It's OK if your collaborator can't change `Settings` in your repo.

#### 1.3.6. (UPD) Protect your `main` branch

> [!NOTE]
> Branch protection prevents accidental pushes directly to `main`.
> This enforces the PR workflow and ensures all changes are reviewed.

1. [Protect the `main` branch](../../wiki/github.md#protect-a-branch).

### 1.4. Set up tools (LOCAL)

See [tools](../../wiki/software-types.md#tool).

#### 1.4.1. (UPD) Set up `VS Code`

1. (Optional) [Read about `VS Code`](../../wiki/vs-code.md#what-is-vs-code).
2. [Set up `VS Code`](../../wiki/vs-code.md#set-up-vs-code).

#### 1.4.2. (UPD) Set up `Docker`

1. (Optional) [Read about `Docker`](../../wiki/docker.md#what-is-docker).
2. [Install `Docker`](../../wiki/docker.md#install-docker) if it's not installed.
3. [Start `Docker`](../../wiki/docker.md#start-docker).

#### 1.4.3. (UPD) (`Windows` only) Switch to the `Linux` shell for the `VS Code Terminal`

1. [Check the current shell in the `VS Code Terminal`](../../wiki/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. If it's not `bash` or `zsh`, [switch to the `Linux` shell for the `VS Code Terminal`](../../wiki/vs-code.md#windows-only-switch-to-the-linux-shell-for-the-vs-code-terminal).
3. [Check the current shell](../../wiki/vs-code.md#check-the-current-shell-in-the-vs-code-terminal) again.

#### 1.4.4. (UPD) Clean up `Docker`

> [!NOTE]
> Old containers and volumes from a previous lab version may conflict with the updated services.
>
> Stop running containers, remove stopped containers, and delete unused volumes and networks so you start with a clean state.

1. [Clean up `Docker`](../../wiki/docker.md#clean-up-docker).

#### 1.4.5. Set up `Git`

1. (Optional) [Read about `Git`](../../wiki/git.md#what-is-git).
2. [Install `Git`](https://git-scm.com/install/) if it's not installed.
3. [Configure `Git`](../../wiki/git.md#configure-git).

### 1.5. (UPD) Open in `VS Code` the `software-engineering-toolkit` directory (LOCAL)

1. Inside the [`Desktop` directory](../../wiki/file-system.md#desktop-directory),
   create the directory `software-engineering-toolkit`.

   Skip this step if this directory exists.

2. [Open in `VS Code` the directory](../../wiki/vs-code.md#open-the-directory):
   `software-engineering-toolkit`.

3. (`Windows` only) [Reopen the directory in `WSL`](../../wiki/vs-code.md#windows-only-reopen-the-directory-in-wsl).

### 1.6. Clone your fork

#### 1.6.1. (UPD) Copy your fork URL

1. [Go to your lab repository fork](#133-upd-go-to-your-fork).

2. Copy [`<your-fork-url>`](../../wiki/github.md#your-fork-url-placeholder).

   It should look like `https://github.com/<your-github-username>/se-toolkit-lab-8`.

   See [`<your-github-username>`](../../wiki/github.md#your-github-username-placeholder).

#### 1.6.2. (UPD) Clone your fork (LOCAL)

1. [Clone your lab repository fork](../../wiki/lab.md#clone-your-lab-repository-fork).

### 1.7. (UPD) Set up `VS Code` in the lab repository directory (LOCAL)

> [!IMPORTANT]
> Go by the links in the steps below and complete the checks ("You should see ...").
> Otherwise, your setup will be broken.

1. [Open in `VS Code` the cloned lab repository directory](../../wiki/vs-code.md#open-the-directory):
   `se-toolkit-lab-8`.
2. [Check the current shell in the `VS Code Terminal`](../../wiki/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
3. [Install the recommended `VS Code` extensions](../../wiki/vs-code.md#install-the-recommended-vs-code-extensions).

> <h3>Troubleshooting</h3>
>
> **The terminal shell is not `bash` or `zsh`.**
>
> 1. [(`Windows` only) Switch to the `Linux` shell for the `VS Code Terminal`](#143-upd-windows-only-switch-to-the-linux-shell-for-the-vs-code-terminal).
>
> **Recommended extensions did not install.**
>
> 1. [Run using the `Command Palette`](../../wiki/vs-code.md#run-a-command-using-the-command-palette):
>    `Reload Window`

### 1.8. Create a new VM

> [!TIP]
> You don't need to create a new [`SSH` key pair](../../wiki/ssh.md#ssh-key-pair) if the old one exists.
>
> You can use the key pair that you created before for the new VM.

1. If you can't [connect to your VM as the user `admin`](../../wiki/vm-access.md#connect-to-the-vm-as-the-user-user-local),
   [recreate the VM](../../wiki/vm.md#recreate-the-vm).

### 1.9. Set up `Python`

> [!NOTE]
> See [What is `Python`](../../wiki/python.md#what-is-python).

#### 1.9.1. Install `uv` (LOCAL)

> [!NOTE]
> See [`uv`](../../wiki/python.md#uv).

1. [Install `uv`](../../wiki/python.md#install-uv).

#### 1.9.2. (UPD) Set up `Python` in `VS Code` (LOCAL)

> [!NOTE]
> The dependencies have been updated in this project version.

1. [Set up `Python` in `VS Code`](../../wiki/vscode-python.md#set-up-python-in-vs-code).

### 1.10. Set up `Node.js`

#### 1.10.1. Install `Node.js` (LOCAL)

1. [Install `Node.js`](../../wiki/nodejs.md#install-nodejs).

#### 1.10.2. (UPD) Install `pnpm` (LOCAL)

1. [Install `pnpm`](../../wiki/nodejs.md#install-pnpm).

### 1.11. (UPD) Set up `Qwen Code` (LOCAL)

[`Qwen Code`](../../wiki/qwen-code.md#what-is-qwen-code) is a [coding agent](../../wiki/coding-agents.md#what-is-a-coding-agent) that can answer questions about the repository and help you complete the lab tasks.

<div style="display:flex;flex-wrap:wrap;gap:10px">
  <img alt="Qwen request" src="../images/tasks/setup/qwen-request.png" style="width:300px"></img>
  <img alt="Qwen response" src="../images/tasks/setup/qwen-response.png" style="width:300px"></img>
</div>

1. [Set up `Qwen Code`](../../wiki/qwen-code.md#set-up-qwen-code-local).

### 1.12. Set up the VM

1. [Set up the VM](../../wiki/vm.md#set-up-the-vm).

### 1.13. (UPD) Clone your fork on the VM (REMOTE)

1. [Set up the lab repository directory (REMOTE)](../../wiki/lab.md#set-up-the-lab-repository-directory).

### 1.14. (UPD) Deploy the LMS API (REMOTE)

1. [Deploy the LMS API on your VM](../../wiki/lms-api-deployment.md#deploy-the-lms-api-on-the-vm).

### 1.15. (UPD) Set up the `Qwen Code` API (REMOTE)

1. [Set up the `Qwen Code` API on your VM](../../wiki/qwen-code-api-deployment.md#deploy-the-qwen-code-api-remote).
2. [Check that the `Qwen Code` API is accessible on your local machine (LOCAL)](../../wiki/qwen-code-api.md#check-that-the-qwen-code-api-is-accessible).

### 1.16. Optional: create a `Telegram` bot token

1. [Create a `Telegram` bot](../../wiki/bot.md#create-a-telegram-bot).
2. You do not need to deploy the bot during setup.
3. If you later do Lab 8 Optional Task 1, follow the task instructions there and the README in the external `nanobot-websocket-channel/client-telegram-bot/` repo.

### 1.17. Set up the `Autochecker` bot

1. [Set up the `Autochecker` bot](../../wiki/autochecker.md#set-up-the-autochecker-bot)

### 1.18. Check the setup using the `Autochecker` bot

1. [Check the `Setup` task](../../wiki/autochecker.md#check-the-task-using-the-autochecker-bot).

---

## 2. Optional steps

These enhancements can make your life easier:

<!-- no toc -->
- [Set up `gh`](#21-upd-set-up-gh-local)
- [Set up `Nix`](#22-set-up-nix-local)
- [Set up `direnv`](#23-set-up-direnv-local)
- [Learn to go back after clicking a link](#24-learn-to-go-back-after-clicking-a-link-local)
- [Set up the shell prompt](#25-set-up-the-shell-prompt-local)
- [Customize the `Source Control`](#26-customize-the-source-control-local)
- [Get familiar with `GitLens`](#27-get-familiar-with-gitlens-local)
- [Create a label for tasks](#28-create-a-label-for-tasks-github)
- [View `Markdown` files in `VS Code`](#29-view-markdown-files-in-vs-code-local)

### 2.1. (UPD) Set up `gh` (LOCAL)

1. [Set up `gh`](../../wiki/github.md#set-up-gh)

### 2.2. Set up `Nix` (LOCAL)

1. (Optional) [Read about `Nix`](../../wiki/nix.md#what-is-nix).
2. [Set up `Nix`](../../wiki/nix.md#set-up-nix).

### 2.3. Set up `direnv` (LOCAL)

1. (Optional) [Read about `direnv`](../../wiki/direnv.md#what-is-direnv).
2. [Set up `Nix`](#22-set-up-nix-local).
3. [Set up `direnv`](../../wiki/direnv.md#set-up-direnv).

### 2.4. Learn to go back after clicking a link (LOCAL)

> [!NOTE]
> Shortcuts for going back after clicking a link:

- `VS Code` — see the [shortcut](../../wiki/vs-code.md#shortcut-go-back).
- `Firefox` — `Alt+ArrowLeft`.
- Other browsers — google.

### 2.5. Set up the shell prompt (LOCAL)

`Starship` shows your current `Git` branch, status, and other useful info directly in your [shell prompt](../../wiki/shell.md#shell-prompt) in almost any terminal, including the [`VS Code Terminal`](../../wiki/vs-code.md#vs-code-terminal).

Complete these steps:

1. [Install `Starship`](https://github.com/starship/starship#-installation).
2. [Open the `VS Code Terminal`](../../wiki/vs-code.md#open-the-vs-code-terminal).

   You should see something similar to this:

   <img alt="Starship in the VS Code Terminal" src="../../wiki/images/starship/terminal-prompt.png" style="width:400px"></img>

### 2.6. Customize the `Source Control` (LOCAL)

1. [Open the `Source Control`](../../wiki/vs-code.md#open-the-source-control).
2. Click three dots to the right of `SOURCE CONTROL`.
3. Put checkmarks only near `Changes` and `GitLens` to see only these views.

   <img alt="Changes and GitLens" src="../../wiki/images/vs-code/source-control-allowed-views.png" style="width:400px"></img>

### 2.7. Get familiar with `GitLens` (LOCAL)

[`GitLens`](../../wiki/gitlens.md#what-is-gitlens) helps you work with `Git` in `VS Code`.

Complete these steps:

1. [See all branches](../../wiki/gitlens.md#see-all-branches).
2. [Look at the commit graph](../../wiki/gitlens.md#look-at-the-commit-graph).
3. [Inspect the current branch](../../wiki/gitlens.md#inspect-the-current-branch).
4. [Inspect the remotes](../../wiki/gitlens.md#inspect-the-remotes).

### 2.8. Create a label for tasks (`GitHub`)

[Labels](../../wiki/github.md#label) help you filter and organize issues.

With a `task` label, you can see in one view all issues created for lab tasks.

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../../.github/ISSUE_TEMPLATE/01-task.yml).

Complete these steps:

1. [Create](../../wiki/github.md#create-a-label) the `task` label.
2. [Add the label to issues](../../wiki/github.md#add-a-label-to-issues).
3. [See all issues with the label](../../wiki/github.md#see-all-issues-with-a-label).

### 2.9. View `Markdown` files in `VS Code` (LOCAL)

If you want to view [`README.md`](../../README.md) and other `Markdown` files in `VS Code` instead of on `GitHub`:

1. [Install the recommended `VS Code` extensions](../../wiki/vs-code.md#install-the-recommended-vs-code-extensions).
2. [Open a `Markdown` file](../../wiki/vs-code.md#open-the-file),
   e.g. [`README.md`](../../README.md).
3. [Open the `Markdown` preview](../../wiki/vs-code.md#open-the-markdown-preview).
