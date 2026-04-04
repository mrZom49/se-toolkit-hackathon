# Program lifecycle

<h2>Table of contents</h2>

- [About the program lifecycle](#about-the-program-lifecycle)
- [Compile time](#compile-time)
- [Runtime](#runtime)

## About the program lifecycle

The program lifecycle describes the phases [source code](./software-types.md#source-code) of a [program](./software-types.md#program) goes through from creation to execution.

Two key phases are:

- [compile time](#compile-time) — when source code is translated into an [executable](./software-types.md#executable)
- [runtime](#runtime) — when the [program](./software-types.md#program) is actively running

Docs:

- [Execution (computing)](https://en.wikipedia.org/wiki/Execution_(computing))

## Compile time

Compile time is the phase when [source code](./software-types.md#source-code) is translated into an [executable](./software-types.md#executable) before the program can run.

Errors detected during this phase (e.g., syntax errors, type mismatches) are called compile-time errors, as opposed to [runtime](#runtime) errors that occur during execution.

## Runtime

Runtime is the phase when a [program](./software-types.md#program) is actively executing.
Errors that occur during this phase (e.g., dividing by zero, accessing a missing file) are called runtime errors.

The term is also used to mean a runtime environment — [software](./software-types.md#what-is-software) that provides services a program needs while running.
For example, [`Node.js`](./nodejs.md#what-is-nodejs) is a `JavaScript` runtime that executes `JavaScript` outside of a browser.

[Shared libraries](./software-types.md#shared-library) are loaded at runtime.
