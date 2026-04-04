# LLM

<h2>Table of contents</h2>

- [What is an LLM](#what-is-an-llm)
- [Model](#model)
  - [Choose a model](#choose-a-model)
- [Inference](#inference)
  - [Local inference](#local-inference)
- [LLM provider API](#llm-provider-api)
  - [LLM provider APIs](#llm-provider-apis)
  - [`OpenAI`-compatible API](#openai-compatible-api)
    - [`OpenAI` API](#openai-api)
    - [`OpenRouter` API](#openrouter-api)
  - [Request to LLM provider API](#request-to-llm-provider-api)
  - [Free models](#free-models)
- [Token](#token)
- [Context](#context)
  - [Context window](#context-window)
  - [Context engineering](#context-engineering)
- [Prompt](#prompt)
  - [Prompt engineering](#prompt-engineering)
- [Response](#response)
- [Modality](#modality)
  - [Multimodal model](#multimodal-model)

## What is an LLM

An LLM (Large Language Model) is a type of AI model trained on large amounts of text data that can understand and generate human-readable text, including code.

LLMs power [coding agents](./coding-agents.md#what-is-a-coding-agent) that help you complete tasks in this course.

Docs:

- [What is a large language model?](https://aws.amazon.com/what-is/large-language-model/)

## Model

A model is a specific trained version of an [LLM](#llm), identified by a name (e.g., `Qwen3-Coder`, `claude-sonnet-4-6`).

Different models vary in [modality](#modality), capability, speed, and cost.

### Choose a model

Choose a [model](#model) for the task at hand.

Check which [modalities](#modality) it supports to make sure it can handle the inputs your task requires.

## Inference

Inference is the process of generating output from a trained [model](#model) — for example, producing a text [response](#response) from a [prompt](#prompt).

### Local inference

Docs:

- [What Can I Run?](https://apxml.com/models)

## LLM provider API

An LLM provider API allows [applications](./software-types.md#application) to:

- send [prompts](#prompt) to the provider's [LLMs](#what-is-an-llm)

- receive generated [responses](#response)

### LLM provider APIs

- [OpenAI API reference](https://developers.openai.com/api/reference/overview)
- [OpenRouter API reference](https://openrouter.ai/docs/api-reference/overview)
- [Anthropic Claude API reference](https://platform.claude.com/docs/en/api/overview)

### `OpenAI`-compatible API

An `OpenAI`-compatible API is an [LLM provider API](#llm-provider-api) that follows the same [request](./http.md#http-request) and [response](./http.md#http-response) format as the [`OpenAI` API](#openai-api).

The same [client](./web-infrastructure.md#web-client) code can work with different `OpenAI`-compatible [LLM provider APIs](#llm-provider-api) by changing only the [base URL](./web-api.md#base-url) and the [API key](./web-api.md#api-key).

Most [coding agents](./coding-agents.md#what-is-a-coding-agent) support `OpenAI`-compatible APIs.

#### `OpenAI` API

An [`HTTP` API](./web-api.md#http-api) that provides access to `OpenAI` [models](#model).

Docs:

- [`OpenAI` API](https://openai.com/api/)
- [OpenAI API reference](https://developers.openai.com/api/reference/overview)

#### `OpenRouter` API

Docs:

- <https://openrouter.ai/>
- [OpenRouter: OpenAI compatibility](https://openrouter.ai/docs/community/frameworks)

### Request to LLM provider API

A request to an LLM provider API is an [`HTTP` POST request](./http.md#http-request) that includes the [model](#model) name and a list of messages, each with a role and text content.

The three message roles are:

- `system` — instructions that set the behavior of the LLM (e.g., "You are a helpful assistant.").
- `user` — the input from the user.
- `assistant` — a previous response from the LLM, included to provide conversation history.

The request is authenticated using an API key in the [`Authorization` header](./http-auth.md#http-authentication).

Example request body:

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "What is an LLM?" }
  ]
}
```

Docs:

- [OpenAI: Chat completions](https://platform.openai.com/docs/guides/chat-completions)

### Free models

- [`OpenRouter` API](#openrouter-api) provides [free models](https://openrouter.ai/collections/free-models).

## Token

A token is a unit of text that an [LLM](#llm) processes — roughly a word or a few characters.

LLMs read and generate text token by token. The number of tokens in a message affects how much of the [context window](#context-window) it uses.

## Context

The context is the information available to the [LLM](#llm) during an interaction — your messages, the conversation history, and any files or instructions you provide.

### Context window

The context window is the maximum amount of text (measured in [tokens](#token)) that an [LLM](#llm) can process in a single interaction — including the conversation history, files, and the current message.

When the context window is full, earlier parts of the conversation are dropped. To avoid this, keep conversations focused and start a new conversation when switching tasks.

### Context engineering

Context engineering is the practice of deliberately choosing what information to include in the context to get better results from an LLM.

When using a [coding agent](./coding-agents.md#what-is-a-coding-agent), you control the [context](#context) by referencing specific files, pasting error messages, and providing acceptance criteria. The more relevant the context, the more useful the response.

## Prompt

A prompt is the input text you send to an LLM to guide its response. The quality of the prompt directly affects the quality of the output.

See [Prompt engineering](#prompt-engineering).

### Prompt engineering

Prompt engineering is the practice of writing prompts that produce accurate, relevant, and useful responses.

## Response

A response is the output that an [LLM](#what-is-an-llm) generates from a [prompt](#prompt) during [inference](#inference).

The response is generated token by token — the [model](#model) predicts one [token](#token) at a time until it produces a complete answer.

## Modality

Modality is the type of input or output that a [model](#model) can process or generate:

- text
- image
- audio
- video

### Multimodal model

A multimodal model is a [model](#model) that supports multiple [modalities](#modality) (e.g., text and image).
