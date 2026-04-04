# Nix devshell

<h2>Table of contents</h2>

- [What is a devshell](#what-is-a-devshell)
- [Enter the devshell](#enter-the-devshell)
  - [Enter the devshell using `direnv`](#enter-the-devshell-using-direnv)
- [Print the devshell menu](#print-the-devshell-menu)

## What is a devshell

A devshell (`Nix` devshell) is a [development environment](./environments.md#development-environment) defined in a [`Nix` flake](./nix-flake.md#what-is-a-flake).
It provides a set of [tools](./software-types.md#tool) and [environment variables](./environments.md#environment-variable) that are available only inside the [shell](./shell.md#what-is-a-shell) session.

In this project, the devshell is defined in [`flake.nix`](../flake.nix) and provides tools grouped by purpose (e.g., frontend tools, backend tools, lint scripts).

Docs:

- [`numtide/devshell`](https://github.com/numtide/devshell)

## Enter the devshell

1. To enter the devshell,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nix develop
   ```

   The output should list the available tools and commands:

   ```terminal
   [1-front-tools]
   ...
   [2-back-tools]
   ...
   [[general commands]]
   ...
   ```

### Enter the devshell using `direnv`

To enter the devshell automatically when you open the project directory, use [`direnv`](./direnv.md#what-is-direnv).

## Print the devshell menu

1. To print the list of available commands inside the devshell,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   menu
   ```
