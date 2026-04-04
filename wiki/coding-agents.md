# Coding agents

<h2>Table of contents</h2>

- [What is a coding agent](#what-is-a-coding-agent)
- [Use a coding agent efficiently and effectively](#use-a-coding-agent-efficiently-and-effectively)
- [Choose and use a coding agent](#choose-and-use-a-coding-agent)
- [Skill](#skill)
  - [Skill name](#skill-name)
  - [Skill arguments](#skill-arguments)

## What is a coding agent

A coding agent lets you use LLMs to help you complete your tasks.

You can [choose and use](#choose-and-use-a-coding-agent) any coding agent for this course.

You should [use the coding agent efficiently and effectively](#use-a-coding-agent-efficiently-and-effectively).

Docs:

- [Coding agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/coding-agents.html)

## Use a coding agent efficiently and effectively

The goal is to pay as little as possible for [tokens](./llm.md#token) and [requests](./http.md#http-request) to the [LLM provider API](./llm.md#llm-provider-api) when using a [coding agent](#what-is-a-coding-agent).

Therefore:

- [choose a model](./llm.md#choose-a-model) that fits your [requirements](./requirements.md#what-are-requirements) and [constraints](./architecture.md).
- give focused and actionable [prompts](./llm.md#prompt) that explain well what you want to achieve so that the agent doesn't spend tokens on irrelevant changes;
- [set up the necessary context](./llm.md#context-engineering) that fits the [context window](./llm.md#context-window) of the underlying LLM.

## Choose and use a coding agent

You may use any [coding agent](#what-is-a-coding-agent) with almost any [model](./llm.md#model).

For this course, we recommend using free [coding agents](#what-is-a-coding-agent) and [free models](./llm.md#free-models) to save your money.

For example, you can [set up `Qwen Code`](./qwen-code.md#set-up-qwen-code-local).

## Skill

Docs:

- [Agent Skills](https://agentskills.io/home)

### Skill name

The skill name is an identifier that selects which [skill](#skill) to run. It matches the name of the skill directory (e.g., `commit`, `review-file`).

Example: `commit` in `commit @main.py`.

### Skill arguments

Skill arguments are the inputs passed to a [skill](#skill) after the [skill name](#skill-name). The expected format depends on the skill (e.g., a [file path](./file-system.md#file-path), a list of files, or no arguments at all).

Example: `@main.py` in `commit @main.py`.
