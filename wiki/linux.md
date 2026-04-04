# `Linux`

<h2>Table of contents</h2>

- [What is `Linux`](#what-is-linux)
- [User](#user)
  - [The user `root`](#the-user-root)
  - [A non-root user](#a-non-root-user)
- [Group](#group)
  - [The group `sudo`](#the-group-sudo)
- [Permissions](#permissions)
  - [Owner](#owner)
  - [Mode](#mode)
    - [Mode digit](#mode-digit)
    - [Mode `700`](#mode-700)
    - [Mode `600`](#mode-600)
    - [Mode `644`](#mode-644)

## What is `Linux`

`Linux` is a family of [operating systems](./operating-system.md) commonly used for servers and [virtual machines](./vm.md).

See:

- [`Linux` distros](./linux-distros.md#what-is-a-linux-distro).
- [`Linux` administration](./linux-administration.md#what-is-linux-administration).

## User

See [User](./operating-system.md#user).

### The user `root`

`root` is the administrator [user](#user).

### A non-root user

A non-root user is a regular [user](#user) account without administrator privileges.

Non-root users can only access [files](./file-system.md#file) and run [programs](./software-types.md#program) that their [permissions](#permissions) allow.
To perform administrative actions, a non-root user must use the [`sudo` command](./linux-administration.md#the-sudo-command).

## Group

See [Group](./operating-system.md#group).

### The group `sudo`

The [group](#group) `sudo` is a special group on `Ubuntu`/`Debian` systems whose members are allowed to run commands with elevated [permissions](#permissions) using the [`sudo` command](./linux-administration.md#the-sudo-command).

Adding a [user](#user) to the group `sudo` grants them administrator access without using [the user `root`](#the-user-root) directly.

## Permissions

On [`Linux`](#what-is-linux), each [file](./file-system.md#file) and [directory](./file-system.md#directory) has [permissions](./operating-system.md#permission) that control access for three categories:

- the [owner](#owner) user
- the owner [group](#group)
- everyone else

Each category can have three types of access:

- **Read (`r`)** — view the contents of a file or list the contents of a directory.
- **Write (`w`)** — modify a file or add/remove files in a directory.
- **Execute (`x`)** — run a file as a program or enter a directory.

See:

- [Change permissions](./linux-administration.md#change-permissions).

### Owner

Every [file](./file-system.md#file) and [directory](./file-system.md#directory) has an owning [user](./operating-system.md#user) and an owning [group](./operating-system.md#group). The owner determines which category of the [mode](#mode) applies to a given user.

See:

- [`chown`](./linux-administration.md#chown) — change the owner and group.

### Mode

A mode is a three-digit number (e.g., `755`, `600`) that encodes the read, write, and execute [permissions](#permissions) for the [owner](#owner) user, the owner group, and everyone else respectively.

#### Mode digit

Each mode digit is a 3-bit binary number — one bit per permission:

| Bit | Permission | Value |
|-----|------------|-------|
| `1` | read       | `4`   |
| `1` | write      | `2`   |
| `1` | execute    | `1`   |

The digit is the sum of the values of the enabled bits.
Examples:

- `7` = `4+2+1` (all enabled)
- `6` = `4+2` (read and write only)

#### Mode `700`

| Category | Digit | `r` | `w` | `x` |
|----------|-------|-----|-----|-----|
| Owner    | `7`   | ✓   | ✓   | ✓   |
| Group    | `0`   |     |     |     |
| Others   | `0`   |     |     |     |

Owner can read, write, and execute; no access for group or others.

#### Mode `600`

| Category | Digit | `r` | `w` | `x` |
|----------|-------|-----|-----|-----|
| Owner    | `6`   | ✓   | ✓   |     |
| Group    | `0`   |     |     |     |
| Others   | `0`   |     |     |     |

Owner can read and write; no access for group or others.

#### Mode `644`

| Category | Digit | `r` | `w` | `x` |
|----------|-------|-----|-----|-----|
| Owner    | `6`   | ✓   | ✓   |     |
| Group    | `4`   | ✓   |     |     |
| Others   | `4`   | ✓   |     |     |

Owner can read and write; group and others can read.
