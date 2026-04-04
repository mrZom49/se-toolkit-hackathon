# `Bash`

<h2>Table of contents</h2>

- [What is `Bash`](#what-is-bash)
- [`Bash` syntax basics](#bash-syntax-basics)
  - [Run a command](#run-a-command)
    - [Run a command - example](#run-a-command---example)
  - [Pipe the `stdout`](#pipe-the-stdout)
    - [Pipe the `stdout` - example](#pipe-the-stdout---example)

## What is `Bash`

`Bash` is a command-line [shell](./shell.md#what-is-a-shell) and scripting language used to interact with the [operating system](./operating-system.md#what-is-an-operating-system).

Docs:

- [Bash reference manual](https://www.gnu.org/software/bash/manual/bash.html)
- [Learn Bash in Y minutes](https://learnxinyminutes.com/bash/)

## `Bash` syntax basics

### Run a command

Type a command name followed by its arguments to execute it.

To run a command with arguments,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
<command> <arguments>
```

#### Run a command - example

To list files in the current directory,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
ls .
```

### Pipe the `stdout`

The pipe operator `|` sends the [standard output](./shell.md#what-is-a-shell) of one command as input to another.

To pipe the output of one command into another,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
<command-1> | <command-2>
```

#### Pipe the `stdout` - example

To list files and show only the first 5 lines,

[run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

```terminal
ls . | head -5
```
