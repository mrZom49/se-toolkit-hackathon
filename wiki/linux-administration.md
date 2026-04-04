# `Linux` administration

<h2>Table of contents</h2>

- [What is `Linux` administration](#what-is-linux-administration)
- [Change permissions](#change-permissions)
  - [`chmod`](#chmod)
    - [Set the permissions](#set-the-permissions)
  - [`chown`](#chown)
    - [Change the owner and group (non-recursive)](#change-the-owner-and-group-non-recursive)
    - [Change the owner and group (recursive)](#change-the-owner-and-group-recursive)
- [Get my current user](#get-my-current-user)
- [The `sudo` command](#the-sudo-command)
- [Inspect ports](#inspect-ports)
  - [See listening TCP ports](#see-listening-tcp-ports)
  - [Inspect a specific port](#inspect-a-specific-port)

## What is `Linux` administration

`Linux` administration involves managing [users](./linux.md#user), [groups](./linux.md#group), [permissions](./linux.md#permissions), and system resources on a [`Linux`](./linux.md#what-is-linux) system.

## Change permissions

Changing [permissions](./linux.md#permissions) controls who can read, write, or execute a file or directory, and who owns it.

Commands for changing permissions:

- [`chmod`](#chmod)
- [`chown`](#chown)

### `chmod`

`chmod` changes the permissions of a file or directory.

#### Set the permissions

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
chmod <mode> <path>
```

Replace the placeholders:

- `<mode>` placeholder with the necessary [mode](./linux.md#mode)
- [`<path>` placeholder](./file-system.md#path-placeholder)

### `chown`

`chown` changes the owner and group of a file or directory.

#### Change the owner and group (non-recursive)

To change the owner and group of a file or a directory,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
chown <user>:<group> <path>
```

Replace the placeholders:

- [`<user>`](./operating-system.md#user-placeholder)

#### Change the owner and group (recursive)

To change the owner and group recursively for a directory and its contents,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
chown -R <user>:<group> <path>
```

Replace the placeholder [`<path>`](./file-system.md#path-placeholder).

## Get my current user

1. To get the current user,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   whoami
   ```

## The `sudo` command

`sudo` runs a command with elevated permissions.

To run a command with elevated permissions,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
sudo <command>
```

## Inspect ports

Use the following commands to inspect [ports](./computer-networks.md#port) on a [host](./computer-networks.md#host).

- [See listening TCP ports](#see-listening-tcp-ports)
- [Inspect a specific port](#inspect-a-specific-port)

### See listening TCP ports

To see all listening TCP ports,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
ss -ltn
```

### Inspect a specific port

To inspect a specific port,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
ss -ltn 'sport = :42000'
```
