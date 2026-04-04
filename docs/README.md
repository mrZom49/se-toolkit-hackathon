# Learning Management Service — Documentation

<!-- TODO rewrite so that docs can be published via GitHub pages 

this will probably be the first page that visitors will see
-->

This directory contains architecture and requirements documentation for the **Learning Management Service (LMS)** — the system students work with in the Software Engineering Toolkit course.

The LMS is grounded in the **OBER** (Outcome-Based Educational Recommender) [^OBER] data model, which extends the classic user–item schema with learning outcomes and assessment items.

## Structure

```tree
docs/
├── README.md                    # This file
├── design/
│   └── architecture.md          # C4 architecture: context, containers, components, flows
└── requirements/
    └── vision.md                # Project vision, features, and actors
```

## Getting Started

1. Start with [requirements/vision.md](requirements/vision.md) to understand what the system does and who uses it.
2. Then read [design/architecture.md](design/architecture.md) for how it is built and how the components interact.

To view Mermaid diagrams, open the files in a Markdown viewer with Mermaid support (e.g., VS Code with the Markdown Preview Mermaid Support extension, or GitHub).

## References

[^OBER]: <https://arxiv.org/abs/2509.18186>
