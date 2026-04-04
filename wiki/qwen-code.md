# `Qwen Code`

<h2>Table of contents</h2>

- [What is `Qwen Code`](#what-is-qwen-code)
- [`Qwen` API](#qwen-api)
- [`Qwen Code` credentials file](#qwen-code-credentials-file)
- [Set up `Qwen Code` (LOCAL)](#set-up-qwen-code-local)
  - [Set up the `Qwen Code` CLI](#set-up-the-qwen-code-cli)
  - [Set up the `Qwen Code Companion` extension for `VS Code`](#set-up-the-qwen-code-companion-extension-for-vs-code)
  - [Set up the `GitHub Copilot Chat` extension for `VS Code`](#set-up-the-github-copilot-chat-extension-for-vs-code)
- [Set up the `Qwen Code` CLI (REMOTE)](#set-up-the-qwen-code-cli-remote)
- [Check the `Qwen Code` credentials file](#check-the-qwen-code-credentials-file)
- [Copy the `Qwen Code` credentials file to the VM (LOCAL)](#copy-the-qwen-code-credentials-file-to-the-vm-local)
- [Open a chat with `Qwen Code`](#open-a-chat-with-qwen-code)
  - [Open a chat with `Qwen Code` using the CLI](#open-a-chat-with-qwen-code-using-the-cli)
  - [Open a chat with `Qwen Code` using the `Qwen Code Companion` extension for `VS Code`](#open-a-chat-with-qwen-code-using-the-qwen-code-companion-extension-for-vs-code)
  - [Open a chat with `Qwen Code` using the `GitHub Copilot Chat` extension for `VS Code`](#open-a-chat-with-qwen-code-using-the-github-copilot-chat-extension-for-vs-code)
- [Chat with `Qwen Code`](#chat-with-qwen-code)
  - [Refer to a file](#refer-to-a-file)
  - [Use a skill](#use-a-skill)
  - [View available models](#view-available-models)
  - [Quit the chat with `Qwen Code`](#quit-the-chat-with-qwen-code)
- [Lab instructions for `Qwen Code`](#lab-instructions-for-qwen-code)

## What is `Qwen Code`

[`Qwen Code`](https://github.com/QwenLM/qwen-code) is a [coding agent](./coding-agents.md#what-is-a-coding-agent) that:

- [provides 1000 free requests per day](https://github.com/QwenLM/qwen-code#why-qwen-code) to `Qwen` [models](./llm.md#model) (see [View available models](#view-available-models)).

- is available in Russia.

See:

- [Set up `Qwen Code` (LOCAL)](#set-up-qwen-code-local).
- [Set up the `Qwen Code` CLI (REMOTE)](./qwen-code.md#set-up-the-qwen-code-cli-remote).
- [Set up the `Qwen Code` API (REMOTE)](./qwen-code-api.md).

## `Qwen` API

An [`OpenAI`-compatible API](./llm.md#openai-compatible-api) that provides access to the `Qwen` family of [LLMs](./llm.md#model).

Docs:

- [`Qwen` API](https://qwen.ai/apiplatform).

## `Qwen Code` credentials file

A file where `Qwen Code` stores credentials for the [user](./operating-system.md#user) to authenticate in the [`Qwen` API](#qwen-api).

Path: `~/.qwen/oauth_creds.json`.

## Set up `Qwen Code` (LOCAL)

> [!NOTE]
> See [`Qwen Code`](#what-is-qwen-code).

<!-- no toc -->
- Method 1: [Set up the `Qwen Code` CLI (LOCAL)](#set-up-the-qwen-code-cli).
- Method 2: [Set up the `Qwen Code Companion` extension for `VS Code`](#set-up-the-qwen-code-companion-extension-for-vs-code).
- Method 3: [Set up the `GitHub Copilot Chat` extension for `VS Code`](#set-up-the-github-copilot-chat-extension-for-vs-code).

### Set up the `Qwen Code` CLI

> [!NOTE]
> See [CLI](./cli.md#what-is-a-cli)

> [!NOTE]
> These instructions should work:
>
> - on your VM (REMOTE)
> - on your local machine (LOCAL)

1. [Install `Node.js`](./nodejs.md#install-nodejs).

2. [Install `pnpm`](./nodejs.md#install-pnpm).

3. To install [`Qwen Code`](./qwen-code.md#what-is-qwen-code),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   pnpm add -g @qwen-code/qwen-code
   ```

4. [Open a chat with `Qwen Code` using the CLI](./qwen-code.md#open-a-chat-with-qwen-code-using-the-cli).

5. Type `/auth` in the chat.

6. Select `Qwen Oauth` using the keyboard (`UpArrow` and `DownArrow`).

7. Press `Enter` to [authenticate via Qwen OAuth](https://github.com/QwenLM/qwen-code?tab=readme-ov-file#authentication).

8. Open the link in a browser to complete the authentication procedure.

9. [Quit the chat with `Qwen Code`](./qwen-code.md#quit-the-chat-with-qwen-code).

10. [Check the `Qwen Code` credentials file](#check-the-qwen-code-credentials-file).

### Set up the `Qwen Code Companion` extension for `VS Code`

1. [Install the `VS Code` extension](./vs-code.md#install-the-vs-code-extension):
   `qwenlm.qwen-code-vscode-ide-companion`.

2. [Open a chat with `Qwen Code` using the `Qwen Code Companion` extension for `VS Code`](#open-a-chat-with-qwen-code-using-the-qwen-code-companion-extension-for-vs-code).

3. Type `/login` in the chat to [authenticate via Qwen OAuth](https://github.com/QwenLM/qwen-code?tab=readme-ov-file#authentication).

4. Complete the authentication procedure.

5. [Check the `Qwen Code` credentials file](#check-the-qwen-code-credentials-file).

### Set up the `GitHub Copilot Chat` extension for `VS Code`

> [!NOTE]
> `Copilot Chat` is not officially available for users in Russia (see [this discussion](https://github.com/orgs/community/discussions/182386)).

1. [Install](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace#_browse-for-extensions) the `github.copilot-chat` and `denizhandaklr.vscode-qwen-copilot` extensions.

2. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Qwen Copilot: Authenticate` to [authenticate via Qwen OAuth](https://github.com/QwenLM/qwen-code?tab=readme-ov-file#authentication).

3. [Check the `Qwen Code` credentials file](#check-the-qwen-code-credentials-file).

4. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Chat: Manage Language Models`.

5. Click `Add Models`.

6. Click `Qwen Code`.

7. Double click `Qwen 3 Coder Plus` to make the model visible.

8. [Open a chat with `Qwen Code` using the `GitHub Copilot Chat` extension for `VS Code`](#open-a-chat-with-qwen-code-using-the-github-copilot-chat-extension-for-vs-code).

## Set up the `Qwen Code` CLI (REMOTE)

1. [Set up the `Qwen Code` CLI (LOCAL)](#set-up-the-qwen-code-cli).
2. [Copy the `Qwen Code` credentials file to the VM](#copy-the-qwen-code-credentials-file-to-the-vm-local).
3. [Connect to the VM as the user `admin`](./vm-access.md#connect-to-the-vm-as-the-user-user-local).
4. [Set up the `Qwen Code` CLI (REMOTE)](#set-up-the-qwen-code-cli).

## Check the `Qwen Code` credentials file

> [!NOTE]
> See [`Qwen Code` credentials file](#qwen-code-credentials-file).

1. To print the content of the credentials file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cat ~/.qwen/oauth_creds.json | jq
   ```

   The output should look like this:

   ```json
   {
     "access_token": "...",
     "token_type": "Bearer",
     "refresh_token": "...",
     "resource_url": "portal.qwen.ai",
     "expiry_date": 1773502586930
   }
   ```

## Copy the `Qwen Code` credentials file to the VM (LOCAL)

1. [Set up the `Qwen Code` CLI (LOCAL)](#set-up-the-qwen-code-cli).

2. To copy the [`Qwen Code` credentials file](#qwen-code-credentials-file) to the VM,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   scp ~/.qwen/oauth_creds.json se-toolkit-vm:~/.qwen/oauth_creds.json
   ```

   The output should look similar to this:

   ```terminal
   oauth_creds.json             100%  313   201.4KB/s   00:00    
   ```

## Open a chat with `Qwen Code`

<!-- no toc -->
- Method 1: [Open a chat with `Qwen Code` using the CLI](#open-a-chat-with-qwen-code-using-the-cli)
- Method 2: [Open a chat with `Qwen Code` using the `Qwen Code Companion` extension for `VS Code`](#open-a-chat-with-qwen-code-using-the-qwen-code-companion-extension-for-vs-code)
- Method 3: [Open a chat with `Qwen Code` using the `GitHub Copilot Chat` extension for `VS Code`](#open-a-chat-with-qwen-code-using-the-github-copilot-chat-extension-for-vs-code)

### Open a chat with `Qwen Code` using the CLI

> [!NOTE]
> See [CLI](./cli.md#what-is-a-cli).

1. [Run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   qwen
   ```

   See [Quit the chat with `Qwen Code`](#quit-the-chat-with-qwen-code).

### Open a chat with `Qwen Code` using the `Qwen Code Companion` extension for `VS Code`

Method 1:

1. Go to the [`Editor Toolbar`](./vs-code.md#editor-toolbar).
2. Click the `Qwen Code: Open` icon.

   <img alt="Icon Qwen Code: Open" src="./images/qwen-code/qwen-code-open.png" style="width:300px"></img>

Method 2:

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Qwen Code: Open`.

### Open a chat with `Qwen Code` using the `GitHub Copilot Chat` extension for `VS Code`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Chat: Open Chat`
2. The `CHAT` panel will open.
3. Go to `CHAT`.
4. Click `Auto` (`Pick Model`).
5. Click `Qwen 3 Coder Plus`.

## Chat with `Qwen Code`

Actions:

<!-- no toc -->
- [Refer to a file](#refer-to-a-file)
- [Use a skill](#use-a-skill)

### Refer to a file

Write `@<file-path>` (without `<` and `>`) to refer to the file at the [`<file-path>`](./file-system.md#file-path-placeholder).

Example: `@main.py`.

### Use a skill

1. [Open a chat with `Qwen Code`](#open-a-chat-with-qwen-code).
2. Write `skills`.
3. Press `Enter`.
4. To use the skill, write the [skill name](./coding-agents.md#skill-name) and the [skill arguments](./coding-agents.md#skill-arguments).

   Example: `commit @main.py`.

   See [Refer to a file](#refer-to-a-file).
5. Press `Enter`.

### View available models

1. [Open a chat with `Qwen Code`](#open-a-chat-with-qwen-code).
2. Type `/model`.
3. Press `Enter`.

   In the `Select Model` dialogue, you should see the available [models](./llm.md#model).

   At the time of writing there is:

   - `coder-model` - `Qwen 3.5 Plus` — efficient hybrid model with leading coding performance.
      - [Modality](./llm.md#modality): text · image · video
      - [Context Window](./llm.md#context-window): 1,000,000 tokens

### Quit the chat with `Qwen Code`

1. Type `/quit`.
2. Press `Enter`.

## Lab instructions for `Qwen Code`

[`Qwen Code`](#what-is-qwen-code) automatically reads [`AGENTS.md`](../AGENTS.md) in the project root. This file contains instructions that guide the agent to help you learn — not just generate code. The agent will ask you questions, help you plan, and encourage you to write code yourself.
