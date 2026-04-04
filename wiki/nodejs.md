# `Node.js`

<h2>Table of contents</h2>

- [What is `Node.js`](#what-is-nodejs)
- [Install `Node.js`](#install-nodejs)
  - [Install `Node.js` using `nvm`](#install-nodejs-using-nvm)
  - [Install `Node.js` using the commands from the official site](#install-nodejs-using-the-commands-from-the-official-site)
  - [Install `Node.js` using `Nix`](#install-nodejs-using-nix)
- [Check that `Node.js` works](#check-that-nodejs-works)
- [`nvm`](#nvm)
  - [Install `nvm`](#install-nvm)
- [`package.json`](#packagejson)
- [`node_modules`](#node_modules)
- [Package managers for `Node.js`](#package-managers-for-nodejs)
- [`npm`](#npm)
- [`pnpm`](#pnpm)
  - [Install `pnpm`](#install-pnpm)
    - [Install `pnpm` via the official installer script](#install-pnpm-via-the-official-installer-script)
    - [Install `pnpm` via `Nix`](#install-pnpm-via-nix)
  - [Common `pnpm` commands](#common-pnpm-commands)
    - [`pnpm install`](#pnpm-install)
  - [Common `pnpm` actions](#common-pnpm-actions)
    - [Install `Node.js` dependencies in the directory](#install-nodejs-dependencies-in-the-directory)

## What is `Node.js`

`Node.js` is a runtime environment that executes `JavaScript` outside of a browser. In this project, it is used to run the frontend development server and build tools.

Docs:

- [Node.js documentation](https://nodejs.org/en/docs)

## Install `Node.js`

- Method 1: [Install `Node.js` using `nvm`](#install-nodejs-using-nvm)
- Method 2: [Install `Node.js` using the commands from the official site](#install-nodejs-using-the-commands-from-the-official-site)
- Method 3: [Install `Node.js` using `Nix`](#install-nodejs-using-nix)

> [!NOTE]
> Probably only the [`Nix`](./nix.md#what-is-nix) method will work on your VM
> because a [library](./software-types.md#library) is missing there.
>
> See <https://github.com/nodejs/node/issues/60790>
>
> `Nix` will fetch this library and other necessary dependencies for you.

### Install `Node.js` using `nvm`

1. [Install `nvm`](#install-nvm) if not yet installed.

2. To install [`Node.js`](#what-is-nodejs) using [`nvm`](#nvm),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nvm install 25.8.1
   ```

3. The output should be similar to this:

   ```terminal
   Downloading and installing node v25.8.1...
   Now using node v25.8.1 (npm v11.10.1)
   ```

4. To set this version as the default,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nvm alias default node
   ```

5. [Check that `Node.js` works](#check-that-nodejs-works).

### Install `Node.js` using the commands from the official site

1. Go to the [`Download Node.js` page](https://nodejs.org/en/download)

2. Configure the instructions for a [terminal](./terminal.md). If you use:

   - `Linux`: Get `v25.x.x` for `Linux` using `<tool>` with `<package-manager>`
   - `macOS`: Get `v25.x.x` for `macOS` using `<tool>` with `<package-manager>`
   - `Windows`: Get `v25.x.x` for `Linux` using `<tool>` with `<package-manager>`

   Choose `<tool>` and `<package-manager>` that you like.
  
   Replace the placeholders:

   - `<tool>` with `nvm` (recommended)
   - `<package-manager>` with `npm` (recommended)

3. To copy the instructions to clipboard,

   Click `Copy to clipboard`.

4. [Run the copied commands in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal).

### Install `Node.js` using `Nix`

1. [Install `Nix`](./nix.md#install-nix) if it's not yet installed.

2. To install `Node.js` from [`nixpkgs`](./nix.md#nixpkgs),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nix profile add nixpkgs#nodejs_25
   ```

3. [Check that `Node.js` works](#check-that-nodejs-works).

## Check that `Node.js` works

1. To check the [`Node.js`](#nodejs) version,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   node --version
   ```

2. The output should be similar to this:

   ```terminal
   v25.8.1
   ```

<!-- TODO install npm with nix because when installing on the VM using nvm libatomic is missing -->

## `nvm`

`nvm` (Node Version Manager) is a tool for installing and switching between multiple versions of [`Node.js`](#what-is-nodejs).

See [Install `nvm`](#install-nvm).

Docs:

- [`nvm` repository](https://github.com/nvm-sh/nvm)

### Install `nvm`

1. Copy the single-line script from the [installation instructions](https://github.com/nvm-sh/nvm#installing-and-updating).

2. [Run the copied script in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal).

3. To check that [`nvm`](#nvm) is installed,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nvm --version
   ```

   The output should be similar to this:

   ```terminal
   0.40.3
   ```

## `package.json`

`package.json` is a configuration [file](./file-system.md#file) in a [`Node.js`](#what-is-nodejs) project that declares the project's [dependencies](./package-manager.md#dependency), scripts, and metadata.

[`pnpm`](#pnpm) and other [package managers for `Node.js`](#package-managers-for-nodejs) read it to know which packages to install and which commands to run.

## `node_modules`

`node_modules` stores all [`Node.js`](#nodejs) modules installed using [`pnpm`](#pnpm) or another [package manager for `Node.js`](#package-managers-for-nodejs).

This [directory](./file-system.md#directory) is [`.gitignore`](./git.md#gitignore)-d.

## Package managers for `Node.js`

> [!NOTE]
> See [Package manager](./package-manager.md#what-is-a-package-manager).

- [`npm`](#npm)
- [`pnpm`](#pnpm)

## `npm`

`npm` is the default [package manager](./package-manager.md#what-is-a-package-manager) for [`Node.js`](#what-is-nodejs).

It is installed automatically when you install [`Node.js`](#install-nodejs).

Docs:

- [`npm` documentation](https://docs.npmjs.com/)

## `pnpm`

`pnpm` is a fast, disk-efficient [package manager](./package-manager.md#what-is-a-package-manager) for [`Node.js`](#what-is-nodejs).
It installs and manages project dependencies declared in [`package.json`](#packagejson).

Docs:

- [`pnpm` documentation](https://pnpm.io/)

### Install `pnpm`

- Method 1: [Install `pnpm` via the official installer script](#install-pnpm-via-the-official-installer-script)
- Method 2: [Install `pnpm` via `Nix`](#install-pnpm-via-nix)

#### Install `pnpm` via the official installer script

```terminal
curl -fsSL https://get.pnpm.io/install.sh | sh -
```

#### Install `pnpm` via `Nix`

1. [Install `Nix`](./nix.md#install-nix).

2. To install [`pnpm`](#pnpm) from [`nixpkgs`](./nix.md#nixpkgs),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nix profile add nixpkgs#pnpm
   ```

3. To set up `pnpm`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   pnpm setup
   ```

4. To update the current shell environment with `pnpm` variables set in the [shell profile](./shell.md#shell-profile),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   source ~/.bashrc
   ```

5. To check that [`pnpm`](#pnpm) is available,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   pnpm --version
   ```

   The output should be similar to this:

   ```terminal
   10.32.1
   ```

### Common `pnpm` commands

- [`pnpm install`](#pnpm-install)

#### `pnpm install`

This command [installs packages in the specified directory](#install-nodejs-dependencies-in-the-directory).

Executes postinstall hooks.

### Common `pnpm` actions

- [Install `Node.js` dependencies in the directory](#install-nodejs-dependencies-in-the-directory)

#### Install `Node.js` dependencies in the directory

> [!NOTE]
> See [`pnpm install`](#pnpm-install), [`package.json`](#packagejson), [directory](./file-system.md#directory).

1. [Open in `VS Code` the project directory](./vs-code.md#open-the-directory).

2. Navigate to the directory that contains `package.json`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cd frontend
   ```

3. [Run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   pnpm install
   ```

4. Verify that the output is similar to this:

   ```terminal
   Packages: +184
   Done in 4.6s using pnpm v10.28.0
   ```

5. [Open the `VS Code Explorer`](./vs-code.md#vs-code-explorer).

6. Verify that there is the `node_modules` directory in the directory where you wanted to install the dependencies.
