# `client-web-react/.env.secret`

<h2>Table of contents</h2>

- [What is `client-web-react/.env.secret`](#what-is-client-web-reactenvsecret)
- [`VITE_API_TARGET`](#vite_api_target)

## What is `client-web-react/.env.secret`

`client-web-react/.env.secret` is an [`.env` file](./environments.md#env-file) that stores [environment variables](./environments.md#environment-variable) for the `Vite` dev server.

`Vite` loads the values when running `pnpm run dev`.

Docs:

- [Vite env and mode](https://vite.dev/guide/env-and-mode)

Default values: [`client-web-react/.env.example`](../client-web-react/.env.example)

> [!NOTE]
> The file `client-web-react/.env.secret` was added to [`client-web-react/.gitignore`](./git.md#gitignore) because you may specify there
> [secrets](./environments.md#secrets) such as the [address of your VM](./vm.md#your-vm-ip-address).

## `VITE_API_TARGET`

The [gateway base URL](./gateway.md#gateway-base-url) that the `Vite` dev server [proxies](./web-infrastructure.md#reverse-proxy) requests to.

Default: `http://127.0.0.1:42002`
