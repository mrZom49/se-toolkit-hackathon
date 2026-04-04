# Useful programs

<h2>Table of contents</h2>

- [Browser](#browser)
  - [`Chrome`](#chrome)
  - [`Firefox`](#firefox)
  - [`Safari`](#safari)
- [`curl`](#curl)
  - [Send a `GET` request with `curl`](#send-a-get-request-with-curl)
  - [Common `curl` flags](#common-curl-flags)
- [`git`](#git)
  - [Common `git` commands](#common-git-commands)
- [`source`](#source)
- [`bash`](#bash)
- [`jq`](#jq)
  - [Format `JSON` output with `jq`](#format-json-output-with-jq)
  - [Common `jq` filters](#common-jq-filters)
- [`find`](#find)
  - [Find files with `find`](#find-files-with-find)
  - [Common `find` flags](#common-find-flags)
- [`ripgrep`](#ripgrep)
  - [Search text with `rg`](#search-text-with-rg)
  - [Common `rg` flags](#common-rg-flags)

<!-- TODO mention supported platforms -->

## Browser

Browsers:

- [`Chrome`](#chrome)
- [`Firefox`](#firefox)
- [`Safari`](#safari)

### `Chrome`

`Chrome` is a web browser developed by `Google`.

It is available on:

- [`Windows`](./operating-system.md#windows)
- [`macOS`](./operating-system.md#macos)
- [`Linux`](./operating-system.md#linux)

Docs:

- [Download `Chrome`](https://www.google.com/chrome/)

### `Firefox`

`Firefox` is a web browser developed by `Mozilla`.

It is available on

- [`Windows`](./operating-system.md#windows)
- [`macOS`](./operating-system.md#macos)
- [`Linux`](./operating-system.md#linux)

Docs:

- [Download `Firefox`](https://www.mozilla.org/firefox/)

### `Safari`

`Safari` is a web browser developed by `Apple`.

It is available on:

- [`macOS`](./operating-system.md#macos)
- [`iOS`](./operating-system.md#ios)

Docs:

- [About `Safari`](https://www.apple.com/safari/)

## `curl`

`curl` is a command-line tool for transferring data with URLs, commonly used to send `HTTP` requests.

### Send a `GET` request with `curl`

```terminal
curl <url>
```

Example:

```terminal
curl http://127.0.0.1:8080/status
```

### Common `curl` flags

| Flag | Description |
| ---- | ----------- |
| `-s` | Silent — suppresses progress output. Useful when piping to [`jq`](#jq). |
| `-X <method>` | Set the `HTTP` method (e.g., `-X POST`). |
| `-H <header>` | Add a request header (e.g., `-H "Authorization: Bearer <token>"`). |
| `-d <data>` | Send a request body (e.g., `-d '{"key": "value"}'`). |

## `git`

`git` is a version control system for tracking changes in files and coordinating work across a team.
See the [`git` wiki](./git.md) for detailed documentation.

### Common `git` commands

| Command | Description |
| ------- | ----------- |
| `git status` | Show the current state of the working tree. |
| `git add <file>` | Stage a file for the next commit. |
| `git commit -m "<message>"` | Create a commit with a message. |
| `git push` | Push commits to the remote repository. |
| `git pull` | Fetch and merge changes from the remote. |
| `git log` | Show the commit history. |

## `source`

`source` is a shell builtin that executes a file in the **current shell session**, not a subprocess.

It is commonly used to activate a `Python` virtual environment. Example:

```terminal
source .venv/bin/activate
```

> [!NOTE]
> Unlike running a script with `bash script.sh`, `source` applies changes (such as environment variable updates) directly to the current shell.

## `bash`

`bash` runs a shell script file.

```terminal
bash <script.sh>
```

Example:

```terminal
bash setup.sh
```

## `jq`

`jq` is a command-line `JSON` processor.
It is commonly used to format and filter `JSON` output from commands like [`curl`](#curl).

### Format `JSON` output with `jq`

Pipe the output of any command that returns `JSON` to `jq` to pretty-print it:

```terminal
curl -s <url> | jq
```

### Common `jq` filters

| Filter | Description |
| ------ | ----------- |
| `.` | Output the full `JSON` with pretty formatting. |
| `.<key>` | Extract a top-level field (e.g., `.name`). |
| `.[<index>]` | Extract an element from an array (e.g., `.[0]`). |
| `.[]` | Iterate over all elements in an array or object. |
| `.[].key` | Extract a field from each element of an array. |

## `find`

`find` searches for files and directories within a directory tree.

### Find files with `find`

```terminal
find <directory> -name "<pattern>"
```

Example — find all `Python` files in the current directory:

```terminal
find . -name "*.py"
```

### Common `find` flags

| Flag | Description |
| ---- | ----------- |
| `-name "<pattern>"` | Match by filename (supports wildcards, e.g., `"*.py"`). |
| `-type f` | Match regular files only. |
| `-type d` | Match directories only. |
| `-not -path "<pattern>"` | Exclude paths matching the pattern. |

## `ripgrep`

`ripgrep` (`rg`) searches file contents recursively for a text pattern.
It is faster than `grep` and respects `.gitignore` by default.

### Search text with `rg`

```terminal
rg "<pattern>"
```

Example — find all occurrences of `TODO` in the current directory:

```terminal
rg "TODO"
```

### Common `rg` flags

| Flag | Description |
| ---- | ----------- |
| `-i` | Case-insensitive search. |
| `-l` | List only file names with matches, not the matching lines. |
| `-n` | Show line numbers (enabled by default). |
| `-t <type>` | Limit to a file type (e.g., `-t py` for `Python`). |
| `--no-ignore` | Don't respect `.gitignore` rules. |
