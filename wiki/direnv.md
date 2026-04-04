# `direnv`

<h2>Table of contents</h2>

- [What is `direnv`](#what-is-direnv)
- [Set up `direnv`](#set-up-direnv)
  - [Install `direnv`](#install-direnv)
  - [Hook `direnv` into your shell](#hook-direnv-into-your-shell)
  - [(Optional) Set up `nix-direnv`](#optional-set-up-nix-direnv)
  - [Install the `VS Code` extension](#install-the-vs-code-extension)
  - [Run `direnv allow`](#run-direnv-allow)
  - [Reset and reload environment](#reset-and-reload-environment)
  - [Reload the `VS Code Terminal`](#reload-the-vs-code-terminal)
  - [Check tool versions](#check-tool-versions)

## What is `direnv`

`direnv` is a [shell](./shell.md#what-is-a-shell) extension that automatically loads and unloads [environment variables](./environments.md#environment-variable) when you enter or leave a [directory](./file-system.md#directory).

In this project, `direnv` reads the [`.envrc`](../.envrc) file and uses [`Nix`](./nix.md#what-is-nix) to set up the [development environment](./environments.md#development-environment) with the correct [tools](./software-types.md#tool) and [dependencies](./package-manager.md#dependency).

Docs:

- [direnv documentation](https://direnv.net/)

## Set up `direnv`

Complete these steps:

1. [Install `direnv`](#install-direnv).
2. [Hook `direnv` into your shell](#hook-direnv-into-your-shell).
3. [Set up `nix-direnv`](#optional-set-up-nix-direnv).
4. [Install the `VS Code` extension](#install-the-vs-code-extension).
5. [Run `direnv allow`](#run-direnv-allow).
6. [Reset and reload environment](#reset-and-reload-environment).
7. [Reload the `VS Code Terminal`](#reload-the-vs-code-terminal).
8. [Check tool versions](#check-tool-versions).

### Install `direnv`

1. To install `direnv`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nix profile add nixpkgs#direnv
   ```

2. To check the `direnv` version,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   direnv --version
   ```

   The output should be:

   ```terminal
   2.37.1
   ```

### Hook `direnv` into your shell

Follow the [instructions for your shell](https://direnv.net/docs/hook.html) to complete the `direnv` setup.

> [!TIP]
> [Open the file](./vs-code.md#open-the-file) mentioned in these instructions using `VS Code`.

### (Optional) Set up `nix-direnv`

> [!NOTE]
> See [`nix-direnv` repository](https://github.com/nix-community/nix-direnv).
>
> See [Installation](https://github.com/nix-community/nix-direnv?tab=readme-ov-file#installation).

If you use `bash` (see [Check the current shell](./vs-code.md#check-the-current-shell-in-the-vs-code-terminal)):

1. To install `nix-direnv`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nix profile add nixpkgs#nix-direnv
   ```

2. To create a directory for the `direnv` config,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   mkdir -p $HOME/.config/direnv
   ```

3. To create the `direnv` config file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   touch $HOME/.config/direnv/direnvrc
   ```

4. [Open the file using `VS Code`](./vs-code.md#open-the-file):
   `~/.config/direnv/direnvrc`.
5. Write there:

   ```terminal
   source $HOME/.nix-profile/share/nix-direnv/direnvrc
   ```

### Install the `VS Code` extension

[Install the extension](./vs-code.md#install-the-extension) with the identifier `mkhl.direnv`.

### Run `direnv allow`

1. To check that you are in the directory that contains a `.envrc` file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ls .envrc
   ```

   The output should be:

   ```terminal
   .envrc
   ```

2. To allow `direnv` to use the `.envrc` file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   direnv allow
   ```

3. Wait for `direnv` to download all dependencies.

### Reset and reload environment

Update the environment in which [`VS Code` extensions](./vs-code.md#extensions) run:

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `direnv: Reset and reload environment`.
2. Wait for `direnv` to finish.
   <img alt="Direnv loading" src="./images/direnv/direnv-loading.png" style="width:300px">
3. Click `Restart`.
   <img alt="Direnv restart extensions" src="./images/direnv/direnv-restart-extensions.png" style="width:300px">
4. Wait 1-2 minutes for extensions to reload.

### Reload the `VS Code Terminal`

1. To reload the `direnv` environment,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   direnv reload
   ```

   The output should be similar to this text:

   ```terminal
   [1-front-tools]
   ...
   [2-back-tools]
   ...
   [[general commands]]
   ...
   ```

### Check tool versions

1. To check the `uv` version,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   uv --version
   ```

   The output should be:

   ```terminal
   uv 0.10.4
   ```

2. To check the `node` version,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   node --version
   ```

   The output should be:

   ```terminal
   v22.22.0
   ```
