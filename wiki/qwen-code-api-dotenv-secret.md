# `qwen-code-api/.env.secret`

<h2>Table of contents</h2>

- [About `qwen-code-api/.env.secret`](#about-qwen-code-apienvsecret)
- [`QWEN_CODE_API_HOST_PORT`](#qwen_code_api_host_port)
- [`QWEN_CODE_API_KEY`](#qwen_code_api_key)

## About `qwen-code-api/.env.secret`

`qwen-code-api/.env.secret` is a [`.env` file](./environments.md#env-file) that stores [environment variables](./environments.md#environment-variable) for the [`Qwen Code` API](./qwen-code-api.md#what-is-qwen-code-api).

Default values: `qwen-code-api/.env.example` in the [`qwen-code-api` repository](./qwen-code-api.md#qwen-code-api-repository).

> [!NOTE]
> The file `qwen-code-api/.env.secret` was added to `qwen-code-api/.gitignore` because you may specify there
> [secrets](./environments.md#secrets) such as the [`QWEN_CODE_API_KEY`](#qwen_code_api_key).

## `QWEN_CODE_API_HOST_PORT`

The [`Qwen Code` API host port](./qwen-code-api.md#qwen-code-api-host-port).

Default: `42005`

## `QWEN_CODE_API_KEY`

The [`Qwen Code` API key](./qwen-code-api.md#qwen-code-api-key).

Default: `my-secret-qwen-key`
