# Nix flake

<h2>Table of contents</h2>

- [What is a flake](#what-is-a-flake)
  - [`flake.lock`](#flakelock)
  - [Common flake commands](#common-flake-commands)
    - [`nix flake update`](#nix-flake-update)
- [Flake registry](#flake-registry)
  - [`nix registry pin`](#nix-registry-pin)

## What is a flake

A flake is a [`Nix`](./nix.md#what-is-nix) project that declares its [dependencies](./package-manager.md#dependency) and outputs in a `flake.nix` file.
It provides a standardized way to define reproducible [environments](./environments.md#what-is-an-environment), [packages](./package-manager.md#package), and [devshells](./nix-devshell.md#what-is-a-devshell).

In this project, the flake is defined in [`flake.nix`](../flake.nix).

Docs:

- [Flakes on NixOS wiki](https://wiki.nixos.org/wiki/Flakes)
- [Flakes on nix.dev](https://nix.dev/concepts/flakes.html)

### `flake.lock`

Docs:

- [Lock files](https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-flake.html#lock-files)

Example: [`flake.lock`](../flake.lock).

### Common flake commands

#### `nix flake update`

Update the revision of inputs used in this project using the [`nix flake update`](https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-flake-update.html) command.

## Flake registry

Docs:

- [`nix registry`](https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-registry.html)

### `nix registry pin`

<https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-registry-pin.html>
