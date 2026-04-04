# Operating system (OS)

<h2>Table of contents</h2>

- [What is an operating system](#what-is-an-operating-system)
- [Operating systems](#operating-systems)
  - [`Linux`](#linux)
  - [`macOS`](#macos)
  - [`iOS`](#ios)
  - [`Windows`](#windows)
    - [`WSL`](#wsl)
- [Process](#process)
  - [Background process](#background-process)
  - [PID](#pid)
- [Service](#service)
- [User](#user)
  - [Username](#username)
  - [`<user>` placeholder](#user-placeholder)
- [Group](#group)
  - [Group name](#group-name)
  - [`<user-group>` placeholder](#user-group-placeholder)
- [Permission](#permission)

## What is an operating system

An operating system (OS) is software that manages computer hardware and software resources, providing a layer between applications and the hardware.

It handles memory allocation, process scheduling, file systems, and device I/O, so that programs can run without directly interacting with hardware.

## Operating systems

- [`Linux`](#linux)
- [`macOS`](#macos)
- [`Windows`](#windows)

### `Linux`

`Linux` is an [open-source](./software-distribution.md#open-source-software) operating system commonly used for servers and [virtual machines](./vm.md).

See [`Linux`](./linux.md) for more details.

### `macOS`

`macOS` is `Apple`'s [proprietary](./software-distribution.md#proprietary-software) operating system for `Mac` computers.

It is based on `Unix`, so many command-line tools and workflows that work on `Linux` also work on `macOS`.

### `iOS`

`iOS` is `Apple`'s [proprietary](./software-distribution.md#proprietary-software) operating system for `iPhone`s and `iPad`s.

Like `macOS`, it is based on `Darwin` (a `Unix`-like core), but it is designed for mobile devices with touchscreens rather than desktop computers.

### `Windows`

`Windows` is Microsoft's proprietary operating system widely used on personal computers.

It uses a different file system structure and command-line environment from `Linux` and `macOS`.

Students on `Windows` can use [`WSL`](#wsl) to run a `Linux` environment.

#### `WSL`

`WSL` (Windows Subsystem for `Linux`) is a feature of `Windows` that lets you run a [`Linux`](#linux) environment directly on `Windows`, without a [virtual machine](./vm.md#what-is-a-vm).

Docs:

- [`WSL` documentation](https://learn.microsoft.com/en-us/windows/wsl/)

> [!TIP]
> To use `WSL` with `VS Code`, see [(`Windows` only) Set up running `VS Code` in `WSL`](./vs-code.md#windows-only-set-up-running-vs-code-in-wsl).

## Process

A process is an instance of a running [program](./software-types.md#program).

When you execute a program, the operating system creates a process that contains the program's code, memory space, variables, and system resources. Each process has a unique process ID (PID) and runs independently of other processes.

Processes can be created, managed, and terminated using various [shell commands](./shell.md#shell-command).

They form the basis of multitasking in the operating system.

### Background process

A background process is a [process](#process) that runs without holding the terminal — the shell prompt returns immediately and the process continues running while it is not attached to any terminal session.

You can start a background process in the [shell](./shell.md#what-is-a-shell) by appending `&` to a command:

```terminal
<command> &
```

### PID

A PID (Process ID) is a unique numerical identifier assigned by the operating system to each running process. PIDs help the operating system to track and manage individual processes.

PIDs are used by various system commands to interact with specific processes, such as terminating them, checking their status, or monitoring their resource usage.

PIDs let the operating system handle multitasking.

<!-- TODO command line -->

## Service

A service is a long-running [process](#process) that performs specific system functions or provides functionality to other processes and applications.

Services typically start automatically during system boot and run in the background without direct user interaction. They can be managed using system service managers like `systemd`, `init`, or service scripts.

Common examples include [web servers](./web-infrastructure.md#web-server), [database servers](./database.md#database-server) (`MySQL`/`PostgreSQL`), [`SSH` daemons](./ssh.md#sshd), and network services.

Services often [listen on specific ports](./computer-networks.md#listen-on-a-port) to handle incoming requests.

They form the backbone of system functionality and network communications.

## User

A user is an account on the operating system that can run [processes](#process) and own [files](./file-system.md#file).

Each user has a [username](#username) and a set of [permissions](#permission) that determine what resources they can access or modify.

### Username

A username is the unique name that identifies a [user](#user) account on the operating system. It is used when logging in to the system.

### `<user>` placeholder

The [username](#username) (without `<` and `>`).

Replace this placeholder with `admin`.

## Group

A group is a collection of [users](#user) that share the same [access permissions](#permission) to [files](./file-system.md#file) and [directories](./file-system.md#directory).

Groups allow an administrator to manage permissions for multiple users at once: adding a user to a group grants them all the group's permissions.

Each user has a primary group and can belong to additional supplementary groups.

### Group name

A group name is the unique name that identifies a [group](#group) on the operating system. It is used when managing group membership and [permissions](#permission).

### `<user-group>` placeholder

The [group name](#group-name) (without `<` and `>`) that coincides with the [`<user>`](#user-placeholder).

The user `<user>` is in the [group](#group) `<user-group>`.

## Permission

A permission is a rule that controls whether a [user](#user) or [group](#group) can read, modify, or execute a resource such as a [file](./file-system.md#file) or [directory](./file-system.md#directory).

Permissions determine what actions each user can perform on the system, preventing unauthorized access and protecting shared resources.

See [`Linux` permissions](./linux.md#permissions) for how permissions work on [`Linux`](./linux.md#what-is-linux).
