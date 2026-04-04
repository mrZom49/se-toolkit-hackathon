# LLM API

<h2>Table of contents</h2>

- [About LLM API](#about-llm-api)
- [LLM API key](#llm-api-key)
  - [`<llm-api-key>` placeholder](#llm-api-key-placeholder)
- [LLM API base URL](#llm-api-base-url)
  - [`<llm-api-base-url>` placeholder](#llm-api-base-url-placeholder)
- [LLM API model](#llm-api-model)
  - [`<llm-api-model>` placeholder](#llm-api-model-placeholder)

## About LLM API

The LLM API is the [OpenAI-compatible API](./llm.md#openai-compatible-api) that [clients](./web-infrastructure.md#web-client) use to generate responses from an [LLM](./llm.md#what-is-an-llm).

You choose which [LLM provider API](./llm.md#llm-provider-api) to use:

- the [`Qwen Code` API](./qwen-code-api.md#what-is-qwen-code-api) on your VM
- the [`OpenRouter` API](./llm.md#openrouter-api)

## LLM API key

The [API key](./web-api.md#api-key) for your [LLM provider API](./llm.md#llm-provider-api).

- For the [`Qwen Code` API](./qwen-code-api.md#what-is-qwen-code-api):

  the value of [`QWEN_CODE_API_KEY`](./qwen-code-api-dotenv-secret.md#qwen_code_api_key) from [`qwen-code-api/.env.secret`](./qwen-code-api-dotenv-secret.md#about-qwen-code-apienvsecret).

- For the [`OpenRouter` API](./llm.md#openrouter-api):

  your `OpenRouter` API key.

### `<llm-api-key>` placeholder

The [LLM API key](#llm-api-key) (without `<` and `>`).

## LLM API base URL

The base URL of the [OpenAI-compatible API](./llm.md#openai-compatible-api) endpoint.

- For the [`Qwen Code` API](./qwen-code-api.md#what-is-qwen-code-api) on your VM:

  `http://localhost:<qwen-code-api-host-port>/v1`.

  See [`<qwen-code-api-host-port>`](./qwen-code-api.md#qwen-code-api-host-port-placeholder).

- For the [`OpenRouter` API](./llm.md#openrouter-api):

  `https://openrouter.ai/api/v1`.

### `<llm-api-base-url>` placeholder

The [LLM API base URL](#llm-api-base-url) (without `<` and `>`).

## LLM API model

The name of the [LLM model](./llm.md#model) to use via the [LLM provider API](./llm.md#llm-provider-api).

- For the [`Qwen Code` API](./qwen-code-api.md#what-is-qwen-code-api):

  `coder-model`.

  See [View available models](./qwen-code.md#view-available-models).

- For the [`OpenRouter` API](./llm.md#openrouter-api):

  `meta-llama/llama-3.3-70b-instruct:free`.

### `<llm-api-model>` placeholder

The [LLM API model](#llm-api-model) (without `<` and `>`).
