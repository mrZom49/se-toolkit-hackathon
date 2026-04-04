# Package manager

- [What is a package manager](#what-is-a-package-manager)
- [Package](#package)
- [Dependency](#dependency)
- [Package managers](#package-managers)
  - [`Nix`](#nix)
  - [`uv`](#uv)
  - [`pnpm`](#pnpm)

## What is a package manager

A package manager is a tool that automates the installation, upgrade, and removal of software [packages](#package).
It resolves [dependencies](#dependency) and ensures the correct versions of [tools](./software-types.md#tool) and [libraries](./software-types.md#library) are available in your environment.

## Package

A package is a bundle of software — code, configuration, and metadata — that a package manager can install and manage.
Packages are versioned, so you can install a specific version or upgrade to a newer one.

[Package managers](#what-is-a-package-manager) install packages alongside their required [dependencies](#dependency).

## Dependency

A dependency is a [package](#package) that your project or another package requires in order to run.
[Package managers](#what-is-a-package-manager) resolve and install the full dependency tree automatically.

## Package managers

### `Nix`

`Nix` is a cross-platform package manager that provides reproducible, isolated [environments](./environments.md#what-is-an-environment).

Docs:

- [`Nix` wiki](./nix.md#what-is-nix)
- [Nix documentation](https://nix.dev/)

### `uv`

`uv` is a modern package manager for [`Python`](./python.md#what-is-python).

Docs:

- [`uv` wiki](./python.md#uv)
- [`uv` documentation](https://docs.astral.sh/uv/)

### `pnpm`

`pnpm` is a fast, disk-efficient package manager for [`Node.js`](./nodejs.md#what-is-nodejs).
It stores packages in a shared content-addressable store and uses hard links to avoid duplicating files across projects.

Docs:

- [`pnpm` documentation](https://pnpm.io/)
