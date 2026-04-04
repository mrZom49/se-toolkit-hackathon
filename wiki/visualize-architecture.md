# Visualize the architecture

<h2>Table of contents</h2>

- [`Draw.io`](#drawio)
- [`PlantUML`](#plantuml)
- [`Mermaid`](#mermaid)
- [Other tools](#other-tools)

> [!WARNING]
> System architecture diagrams represent the system architecture but they are not the [system architecture](https://github.com/inno-se/the-guide?tab=readme-ov-file#architecture).

## `Draw.io`

You can *prototype* diagrams in [`docs/diagrams/prototype`](./lab-1/docs/diagrams/prototype/example.drawio.svg) via the [`hediet.vscode-drawio`](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) extension ([example](./lab-1/docs/diagrams/prototype/example.drawio.svg)).

However, it's not a good idea to version control images because you can't conveniently visualize their diffs and therefore can't track changes well.

Therefore, you must use the [`diagrams as code`](https://simmering.dev/blog/diagrams/) approach and eventually switch to one of the following tools:

<!-- no toc -->
- [`PlantUML`](#plantuml)
- [`Mermaid`](#mermaid)
- [Other tools](#other-tools)

## `PlantUML`

[`PlantUML`](https://plantuml.com/) supports all the necessary types of diagrams. Therefore, we recommend using it to visualize the architecture.

If you want to preview the `PlantUML` diagrams in `VS Code`, follow these steps:

- Install the [`jebbs.plantuml`](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml) `VS Code` extension.
- Install [`Docker`](https://docs.docker.com/get-started/get-docker/).
- Run in the terminal `docker run --name plantuml-server -d -p 48080:8080 plantuml/plantuml-server:jetty` to start a `PlantUML` server.
- Open the `PlantUML` server in the browser at `http://localhost:48080` to make sure it works.
- In `VS Code`, in the [`docs/diagrams/src/`](./lab-1/docs/diagrams/src/) directory, open a `PlantUML` file with the `.puml` extension.
- Click the `Preview Current Diagram` icon.

    The extension should connect to the `PlantUML` server and render the diagram.

    The `48080` port is already set in [`.vscode/settings.json`](../.vscode/settings.json).

- Write the `PlantUML` code in [`docs/diagrams/src/`](./lab-1/docs/diagrams/src/) and render the diagrams to `SVG` in [`docs/diagrams/out/`](./lab-1/docs/diagrams/out/) using the `jebbs.plantuml` extension. These directories are already set in [`.vscode/settings.json`](../.vscode/settings.json).
- To render diagrams to SVG, open the [`Command Palette`](./vs-code.md#command-palette), write `PlantUML: Export Workspace Diagrams`, and choose `svg`.
- [Embed](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) the rendered images into your `Markdown` file.

## `Mermaid`

You can write [`Mermaid`](https://mermaid.js.org/) code in `Markdown` files in code blocks with the `mermaid` language tag (see [docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams)).

## Other tools

Other tools that implement the `diagrams as code` approach include:

- [`Structurizr`](https://structurizr.com/)
- [`D2`](https://d2lang.com/)
- [`LikeC4`](https://github.com/likec4/likec4)
- [`IcePanel`](https://icepanel.io/)
