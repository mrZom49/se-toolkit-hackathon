# Writing conventions — applies to both tasks and wiki

- [4.1. Instructions wording](#41-instructions-wording)
- [4.2. Terminal commands](#42-terminal-commands)
- [4.3. Command Palette commands](#43-command-palette-commands)
- [4.4. Options vs steps](#44-options-vs-steps)
- [4.5. Ordered lists](#45-ordered-lists)
- [4.6. Mini-ToC](#46-mini-toc)
- [4.7. Table of contents](#47-table-of-contents)
- [4.8. Links and cross-references](#48-links-and-cross-references)
- [4.9. Notes, tips, warnings](#49-notes-tips-warnings)
- [4.10. Images](#410-images)
- [4.11. Collapsible hints and solutions](#411-collapsible-hints-and-solutions)
- [4.12. Commit message format](#412-commit-message-format)
- [4.13. Diagrams](#413-diagrams)
- [4.14. `<!-- TODO -->` comments](#414----todo----comments)
- [4.15. `<!-- no toc -->` comments](#415----no-toc----comments)
- [4.16. Code snippets in explanations](#416-code-snippets-in-explanations)
- [4.17. Heading levels in section titles](#417-heading-levels-in-section-titles)
- [4.18. Inline formatting of technical terms](#418-inline-formatting-of-technical-terms)
- [4.19. Steps with sub-steps](#419-steps-with-sub-steps)
- [4.20. Placeholders in docs](#420-placeholders-in-docs)
- [4.21. `docker compose up` commands](#421-docker-compose-up-commands)
- [4.22. Environment variable references](#422-environment-variable-references)
- [4.23. Horizontal rules](#423-horizontal-rules)
- [4.24. Inline paths](#424-inline-paths)
- [4.25. Branch-on-remote references](#425-branch-on-remote-references)
- [4.26. Example IP address](#426-example-ip-address)
- [4.27. Troubleshooting](#427-troubleshooting)
  - [Inline troubleshooting](#inline-troubleshooting)
  - [Troubleshooting section](#troubleshooting-section)
  - [Cross-references](#cross-references)
- [4.28. JSON command output](#428-json-command-output)
- [4.29. Referring to users of a machine](#429-referring-to-users-of-a-machine)
- [4.30. Section titles with execution context](#430-section-titles-with-execution-context)
- [4.31. Path placeholder references](#431-path-placeholder-references)
- [4.32. Standalone `<branch>` placeholder references](#432-standalone-branch-placeholder-references)

## 4.1. Instructions wording

- **Navigate somewhere** — `Go to X.`
- **Click something** — `Click X.`
- **Type something in a shell or chat** — `Type X.`
- **Choose an option** — `Method N:` prefix (see [4.6](#46-mini-toc))
- **Complete all steps** — `Complete these steps:`
- **Conditional steps** — `If <condition>, complete these steps:`

- **Split compound instructions.** Never write "Do A and do B." Instead, split into two numbered steps.
- **Finish complete sentences with a `.`**
- **Write each sentence on its own line.** This makes diffs cleaner and lets individual sentences be referenced by line number.

## 4.2. Terminal commands

Write each command for the `VS Code Terminal` in a multi-line code block with the type `terminal`. Always precede with a link to the wiki.

- **Use the "To…" intention pattern.** Start with "To \<intention\>," (ending with a comma), then a blank line for visual separation, then the run instruction. This forms one grammatical sentence — the blank line is only for readability. The "run" is lowercase because it continues the sentence. Never present a bare command without context.

From a task file:

~~~markdown
1. To <intention>,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   <command>
   ```
~~~

From a wiki file:

~~~markdown
1. To <intention>,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   <command>
   ```
~~~

Commands that run on a VM (after an SSH connection) use the same pattern — students type them in the `VS Code Terminal` via the SSH session.

Exception: `vs-code.md` itself is exempt because the link would be self-referential.

## 4.3. Command Palette commands

From a task file:

~~~markdown
1. [Run using the `Command Palette`](../../../wiki/vs-code.md#run-a-command-using-the-command-palette):
   `<command>`
~~~

From a wiki file:

~~~markdown
1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `<command>`
~~~

Exception: `vs-code.md` itself is exempt because the link would be self-referential.

## 4.4. Options vs steps

Clearly differentiate:

- **Options:** List with `Method N:` prefix (see [4.6](#46-mini-toc)).
- **Steps:** "Complete these steps:" (then list steps in order).

## 4.5. Ordered lists

Each ordered list must use `1. 2. 3.`, **not** `1. 1. 1.`.

## 4.6. Mini-ToC

Provide a little table of contents when the list of options or steps is long. Use `Method N:` prefixes with full heading text as the link:

```markdown
<!-- no toc -->
- Method 1: [Do X using the `VS Code Terminal`](#do-x-using-the-vs-code-terminal)
- Method 2: [Do X using `GitLens`](#do-x-using-gitlens)

### Do X using the `VS Code Terminal`

### Do X using `GitLens`
```

Place `<!-- no toc -->` on the line immediately before the list (not before any introductory sentence). Use a numbered list when the items are sequential steps. Use a bulleted list when the items are unordered options.

Don't provide a mini-ToC when all lists of items are short.

## 4.7. Table of contents

- Insert a ToC right after the document title.
- **Edit body sections first, then update the ToC.** When modifying a document, make all heading and content changes in the body before touching the ToC. This avoids stale or mismatched entries and keeps diffs easier to review.
- `Markdown All in One` generates and updates the ToC automatically from your headings. Write sections first, then let the extension generate the ToC. Fix any anchor indices (e.g., step numbers) in the ToC afterwards if needed.
- To skip a section from the ToC, use HTML tags for the title: `<h2>Heading</h2>`.
- To control which heading levels appear in the ToC, edit `"markdown.extension.toc.levels"` in `.vscode/settings.json`.

## 4.8. Links and cross-references

- Link to wiki sections whenever a concept or tool is mentioned for the first time in a section. Don't link when it's mentioned second time. This applies to both task docs and wiki docs. This ensures readers who jump to a specific section can still find relevant references.
- Wiki files can and should cross-reference other wiki files: `[concept name](./other-wiki.md#<section>)`.
- Use relative paths for all links.
- Provide a link to each file that exists in the repo.
- Link format for wiki references from tasks: `[concept name](../../../wiki/<file>.md#<section>)`.
- Tasks can reference steps in other tasks: `[Run the web server](./task-1.md#8-run-the-web-server)`.
- **Forward references for rationale:** When the reason for a step's placement or structure depends on a future step, link forward to that step. This tells readers *why* the step appears here rather than elsewhere. Example: a "Start creating a VM" step that is intentionally placed early (because provisioning takes time) should link to the later "Continue creating a VM" step where the workflow resumes.
- **Don't link to the top-level heading** (the `#` title) of a file. Link to a specific subsection instead. The top-level heading is just the document title — linking to it is the same as linking to the file with no anchor. Good: `[Linux](./linux.md#what-is-linux)`. Bad: `[Linux](./linux.md#linux)`.
- **Compound phrases:** When a tool name and a concept naturally form a single phrase (e.g., `` `GitHub` pull request ``, `` `VS Code` Terminal ``), link the whole phrase to the concept's section rather than creating two adjacent links. Good: `` [`GitHub` pull request](./github.md#pull-request) ``. Bad: `` [`GitHub`](./github.md) [pull request](./github.md#pull-request) ``.
- **No consecutive links:** Two links next to each other with no plain text between them look like a single link in the rendered preview — the reader can't tell where one ends and the next begins. Reword the sentence so at least one plain-text word separates them. Good: `a [process](…) that [listens on a port](…)`. Bad: `a [process](…) [listens on a port](…)`.

## 4.9. Notes, tips, warnings

Use GitHub-flavored Markdown alerts:

```markdown
> [!NOTE]
> Explanatory information.

> [!TIP]
> Helpful suggestion.

> [!IMPORTANT]
> Critical information.

> [!WARNING]
> Urgent information.

> [!CAUTION]
> Negative consequences.
```

- **Do not indent alerts.** GitHub-flavored Markdown alerts (`> [!NOTE]`, etc.) do not render correctly when indented (e.g., inside a list item). If you need an alert inside a list, restructure the content to place the alert at the top indentation level, or use a blockquote with a bold label as a fallback:

  ```markdown
  1. Step text.

     > 🟦 **Note**
     >
     > Note text.

     > 🟩 **Tip**
     >
     > Tip text.

     > 🟪 **Important**
     >
     > Important text.

     > 🟨 **Warning**
     >
     > Warning text.

     > 🟥 **Caution**
     >
     > Caution text.
  ```

## 4.10. Images

Use HTML `<img>` tags with a `style` attribute for width control:

```markdown
<img alt="Description" src="../../images/wiki/vs-code/example.png" style="width:400px"></img>
```

## 4.11. Collapsible hints and solutions

Use `<details>` and `<summary>` for hints and solutions:

```markdown
1. <details><summary>Click to open a hint</summary>

   The hint text here.

   </details>

2. <details><summary>Click to open the solution</summary>

   The solution text here.

   </details>
```

## 4.12. Commit message format

Use [conventional commits](https://www.conventionalcommits.org/):

```text
<type>: <short description>

- <detail 1>
- <detail 2>
```

Common types:

- `fix:` — bug fixes
- `feat:` — new features or additions
- `docs:` — documentation changes

When a task specifies a commit message, provide it in a code block:

```markdown
   Use a multi-line message:

   \`\`\`text
   <type>: <short description>

   - <detail 1>
   - <detail 2>
   \`\`\`
```

## 4.13. Diagrams

- Use `.drawio.svg` format for editable diagrams (created with [draw.io](https://app.diagrams.net/)).
- Store diagrams used in `wiki/` in `wiki/images/`; store diagrams used in `lab/` in `lab/images/`.
- Docs in `lab/` may also reference images stored in `wiki/images/`.
- Reference them with standard Markdown image syntax: `![Alt text](../images/diagram.drawio.svg)`.

## 4.14. `<!-- TODO -->` comments

Use `<!-- TODO description -->` HTML comments for work-in-progress sections. These are invisible to students but trackable by authors using the `Todo Tree` VS Code extension.

## 4.15. `<!-- no toc -->` comments

Use `<!-- no toc -->` before a list to prevent `Markdown All in One` from including it in the auto-generated ToC:

```markdown
<!-- no toc -->
- [Method 1](#method-1)
- [Method 2](#method-2)
```

## 4.16. Code snippets in explanations

When walking students through code (e.g., debugging a bug), show the relevant code snippet in a fenced code block with the language specified:

~~~markdown
1. Look at the line where the `result` variable gets a value:

   ```<language>
   result = find_by_id(item_id, collection=data)
   ```

   The function `find_by_id` searches for an item in a given collection.
~~~

## 4.17. Heading levels in section titles

When asking to write particular sections in a file, provide file section headings in section titles:

```markdown

Create the file `docs.md` with the following sections:

1. [## Section 1](#-section-1)
2. [## Section 2](#-section-2)

## ## Section 1

## ## Section 2
```

## 4.18. Inline formatting of technical terms

Wrap names of tools, languages, formats, and protocols in backticks: `` `VS Code` ``, `` `Git` ``, `` `Docker` ``, `` `Python` ``, `` `SQL` ``, `` `JSON` ``, `` `CSV` ``, `` `SSH` ``, `` `WSL` ``, `` `Autochecker` ``.

Don't backtick acronyms that aren't names: VM, API, URL, ERD.

Use these exact spellings and capitalizations for recurring terms in the lab:

- backend — the back-end service; write as plain text, not inline code (not "back-end" or "back end")
- frontend — the front-end service; write as plain text, not inline code (not "front-end" or "front end")

## 4.19. Steps with sub-steps

When multiple actions serve a single logical goal, group them under one step. Write the step as a complete sentence followed by "Complete the following steps:", then list the sub-steps as a nested ordered list:

```markdown
1. Configure the environment. Complete the following steps:
   1. Open `.env.example`.
   2. Copy it to `.env.secret`.
   3. Fill in the values.
```

When sub-items describe the behavior of an artifact being created (a workflow, config file, script, etc.) rather than actions the student performs, use "does the following:" instead. Write sub-items in third person to reflect what the artifact does:

```markdown
1. Add a workflow that does the following on every push to `main`:
   1. Checks out the repository.
   2. Runs all back-end unit tests.
   3. Runs all end-to-end tests.
```

When actions don't share a logical goal, flatten them into separate top-level steps (see [4.1. Instructions wording](#41-instructions-wording)).

## 4.20. Placeholders in docs

**Parameterize generic instructions; bind concrete values at the surface.**
Wiki pages and reusable how-tos (e.g., `git-vscode.md`) must be written with placeholders (`<branch>`, `<remote>`, `<user>`, `<path>`, etc.).
Surface files that students actually follow (e.g., `git-workflow.md`, `lab.md`, task files) bind those placeholders to concrete values for the current lab.

Example — generic wiki instruction:

```markdown
[Switch to the branch `<branch>`](./git-vscode.md#switch-to-the-branch-branch)
```

Surface file binds the placeholder:

```markdown
Switch to the `main` branch.
```

This separation keeps wiki content reusable across labs while letting each lab supply its own values.

Use placeholders instead of hardcoded environment-specific values (e.g., URLs, ports from `.env`). This keeps docs accurate when students change their configuration.

Bad: `` Open <http://127.0.0.1:5050> in a browser. ``

Good: `` Open <pgadmin-url> in a browser. ``

When defining a placeholder, clarify that the value does not include `<` and `>` wherever it may not be obvious to the reader. Use the format: ``(without `<` and `>`)`` at the end of the description sentence.

When asking students to replace a single placeholder, include the word "placeholder" explicitly after the placeholder name. Don't repeat inline what the placeholder means if it already links to a section that explains it — the link is enough.

**Multiple placeholders — bullet list:**

~~~markdown
Replace the placeholders:

- [`<placeholder-1>`](link-to-explanation)
- [`<placeholder-2>`](link-to-explanation)
~~~

**Single placeholder (linked):**

~~~markdown
Replace the placeholder [`<placeholder>`](link-to-explanation).
~~~

**Single placeholder (not linked):**

~~~markdown
Replace the placeholder `<placeholder>` with <explanation>.
~~~

## 4.21. `docker compose up` commands

Always include the `--build` flag when writing `docker compose up` commands in instructions. This ensures containers are rebuilt from the latest source, preventing students from running stale images.

Good: `docker compose up --build`

Bad: `docker compose up`

## 4.22. Environment variable references

When referencing an environment variable from a `.env.*.secret` file in prose, link it to its section in the wiki and link the file name to indicate the source.

**`.env.docker.secret`**

From a wiki file:

```markdown
[`VARIABLE_NAME`](./dotenv-docker-secret.md#variable_name) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret)
```

From a task file:

```markdown
[`VARIABLE_NAME`](../../../wiki/dotenv-docker-secret.md#variable_name) in [`.env.docker.secret`](../../../wiki/dotenv-docker-secret.md#what-is-envdockersecret)
```

**`backend/.env.tests.unit.secret`**

From a wiki file:

```markdown
[`VARIABLE_NAME`](./backend-dotenv-tests-unit-secret.md#variable_name) in [`backend/.env.tests.unit.secret`](./backend-dotenv-tests-unit-secret.md#what-is-backendenvtestsunitsecret)
```

From a task file:

```markdown
[`VARIABLE_NAME`](../../../wiki/backend-dotenv-tests-unit-secret.md#variable_name) in [`backend/.env.tests.unit.secret`](../../../wiki/backend-dotenv-tests-unit-secret.md#what-is-backendenvtestsunitsecret)
```

**`backend/.env.tests.e2e.secret`**

From a wiki file:

```markdown
[`VARIABLE_NAME`](./backend-dotenv-tests-e2e-secret.md#variable_name) in [`backend/.env.tests.e2e.secret`](./backend-dotenv-tests-e2e-secret.md#what-is-backendenvtestse2esecret)
```

From a task file:

```markdown
[`VARIABLE_NAME`](../../../wiki/backend-dotenv-tests-e2e-secret.md#variable_name) in [`backend/.env.tests.e2e.secret`](../../../wiki/backend-dotenv-tests-e2e-secret.md#what-is-backendenvtestse2esecret)
```

Following [4.8](#48-links-and-cross-references), the file link only needs to appear once per section when multiple variables from the same file are referenced together.

Exception: variables inside fenced code blocks cannot use markdown links — use plain text there.

## 4.23. Horizontal rules

Use exactly three dashes (`---`) for horizontal rules.

Good: `---`

Bad: `----`, `-----`, `***`, `___`

## 4.24. Inline paths

Use a trailing `/` for directory paths: `` `lab/tasks/` ``, `` `client-web-react/` ``.

Exception: `..` references do not get a trailing `/`: `` `lab/tasks/..` ``.

## 4.25. Branch-on-remote references

When referring to a branch on a remote in prose, use `` branch `<branch>` on `<remote>` ``:

```markdown
Pull changes from the branch `<branch>` on `<remote>`.
```

When the placeholder pair first appears in a section, link each part to its definition:

From a wiki file:

```markdown
See [`<branch>`](./git.md#branch-placeholder), [`<remote>`](./git.md#remote-placeholder).
```

From a task file:

```markdown
See [`<branch>`](../../../wiki/git.md#branch-placeholder), [`<remote>`](../../../wiki/git.md#remote-placeholder).
```

## 4.26. Example IP address

Use `192.0.2.1` as the example IP address in all documentation.

Good: `192.0.2.1`

Bad: `192.168.1.1`, `10.0.0.1`

## 4.27. Troubleshooting

Use a blockquote for all troubleshooting content. Do **not** use `<details>` blocks.

Start with an `<h3>Troubleshooting</h3>` label. Each issue is a bold sentence followed by its resolution:

```markdown
> <h3>Troubleshooting</h3>
>
> **Issue title.**
>
> Resolution text.
>
> **Another issue.**
>
> Resolution text.
```

### Inline troubleshooting

Place a troubleshooting blockquote directly after the step or section it relates to. This is the preferred form when only one or two issues apply to a specific step.

~~~markdown
1. To connect to the VM,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh <user>@<vm-ip>
   ```

> <h3>Troubleshooting</h3>
>
> **Connection refused.**
>
> Resolution text.
~~~

### Troubleshooting section

When troubleshooting applies to the document as a whole — or when there are many issues — place a `## Troubleshooting` section at the **end of the document**. Add it to the table of contents.

```markdown
## Troubleshooting

> <h3>Troubleshooting</h3>
>
> **Issue title**
>
> Resolution text.
```

### Cross-references

When a step's troubleshooting is already covered in a dedicated section of the same file or another file, use a blockquote with one linked bold title per problem instead of duplicating content:

```markdown
> <h3>Troubleshooting</h3>
>
> [**Issue title**](#issue-title)
>
> [**Another issue**](#another-issue)
```

## 4.28. JSON command output

Always pipe commands that produce `JSON` output to `jq` for readable formatting.

Good: `curl http://localhost:3000/api/items | jq`

Bad: `curl http://localhost:3000/api/items`

## 4.29. Referring to users of a machine

When referring to a user of a machine in prose, use the pattern "the user `<username>`":

- The administrator user: `the user \`root\``
- A non-root user placeholder: `the user \`<user>\``

Link on first mention in a section (see [Links and cross-references](#48-links-and-cross-references)):

From a wiki file:

```markdown
[the user `root`](./linux.md#the-user-root)
[the user `<user>`](./operating-system.md#user-placeholder)
```

From a task file:

```markdown
[the user `root`](../../../wiki/linux.md#the-user-root)
[the user `<user>`](../../../wiki/operating-system.md#user-placeholder)
```

## 4.30. Section titles with execution context

When a section contains commands that run on a specific machine, append `(REMOTE)` or `(LOCAL)` to the section title to indicate where the commands should be run:

- `(REMOTE)` — commands run on a remote machine (e.g., a VM accessed via `SSH`).
- `(LOCAL)` — commands run on the local machine (e.g., the student's own computer).

```markdown
## Connect to the VM (LOCAL)

## Configure the firewall (REMOTE)
```

Omit the suffix when the section contains no commands, or when the execution context is unambiguous from the surrounding content (e.g., a file that exclusively covers remote or local operations).

## 4.31. Path placeholder references

When referring to a path placeholder in prose, link it to the matching section in `file-system.md`.

From a wiki file:

```markdown
[`<path>`](./file-system.md#path-placeholder)
[`<file-path>`](./file-system.md#file-path-placeholder)
[`<directory-path>`](./file-system.md#directory-path-placeholder)
```

From a task file:

```markdown
[`<path>`](../../../wiki/file-system.md#path-placeholder)
[`<file-path>`](../../../wiki/file-system.md#file-path-placeholder)
[`<directory-path>`](../../../wiki/file-system.md#directory-path-placeholder)
```

## 4.32. Standalone `<branch>` placeholder references

When asking the reader to replace a `<branch>` placeholder outside of a branch-on-remote pair (see [4.25](#425-branch-on-remote-references)), link to the placeholder section:

From a wiki file:

```markdown
Replace the placeholder [`<branch>`](./git.md#branch-placeholder).
```

From a task file:

```markdown
Replace the placeholder [`<branch>`](../../../wiki/git.md#branch-placeholder).
```
