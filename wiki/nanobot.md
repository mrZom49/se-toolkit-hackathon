# `Nanobot`

<h2>Table of contents</h2>

- [About `Nanobot`](#about-nanobot)
- [Gateway](#gateway)
- [Webchat channel](#webchat-channel)
- [MCP server](#mcp-server)
- [How clients connect](#how-clients-connect)

## About `Nanobot`

`Nanobot` is an AI assistant gateway that uses an [LLM](./llm.md#what-is-an-llm) to answer questions about course data.
It connects to chat clients through a [webchat channel](#webchat-channel) and accesses the [LMS API](./lms-api.md#about-the-lms-api) through an [MCP server](#mcp-server).

`Nanobot` runs as a [`Docker Compose` service](./docker-compose.md#service) and is built on the `nanobot-ai` framework.

Docs:

- [nanobot-ai on PyPI](https://pypi.org/project/nanobot-ai/)

## Gateway

The [`Nanobot`](#about-nanobot) gateway is the internal process that coordinates the agent loop, message bus, and connected channels.

It [listens on](./computer-networks.md#listen-on-a-port) the [address](./computer-networks.md#ip-address) and [port](./computer-networks.md#port-number) configured by [`NANOBOT_GATEWAY_CONTAINER_ADDRESS`](./dotenv-docker-secret.md#nanobot_gateway_container_address) and [`NANOBOT_GATEWAY_CONTAINER_PORT`](./dotenv-docker-secret.md#nanobot_gateway_container_port) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

## Webchat channel

The webchat channel is a [`WebSocket`](./websocket.md#what-is-websocket) server that allows chat clients to communicate with the `Nanobot` agent.
Clients connect via `WebSocket` and exchange `JSON` messages to send questions and receive answers.

The webchat channel [listens on](./computer-networks.md#listen-on-a-port) the [address](./computer-networks.md#ip-address) and [port](./computer-networks.md#port-number) configured by [`NANOBOT_WEBCHAT_CONTAINER_ADDRESS`](./dotenv-docker-secret.md#nanobot_webchat_container_address) and [`NANOBOT_WEBCHAT_CONTAINER_PORT`](./dotenv-docker-secret.md#nanobot_webchat_container_port) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

[`Caddy`](./caddy.md#what-is-caddy) [forwards requests](./web-infrastructure.md#forward-request) from `/ws/chat` to the webchat channel.
The web client must also provide the [`NANOBOT_ACCESS_KEY`](./dotenv-docker-secret.md#nanobot_access_key) configured for that deployment.

## MCP server

The MCP (`Model Context Protocol`) server exposes the [LMS API](./lms-api.md#about-the-lms-api) as tools that the `Nanobot` agent can call during reasoning.
When a user asks a question, the agent may call these tools to fetch course data before composing a response.

The MCP server runs as a `stdio` process inside the `Nanobot` [container](./docker.md#container).
It authenticates to the LMS with the deployment's own `NANOBOT_LMS_API_KEY` / `LMS_API_KEY`, not with credentials from the web client.

## How clients connect

Both the [`Telegram` bot client](./client-telegram-bot.md#about-the-telegram-bot-client) and the `Flutter` web app connect to the same `Nanobot` instance over the [webchat channel](#webchat-channel).

- The [`Telegram` bot client](./client-telegram-bot.md#about-the-telegram-bot-client) forwards free-text messages to `Nanobot` via [`WebSocket`](./websocket.md#what-is-websocket).
  Local session commands such as `/start`, `/help`, `/login`, and `/logout` are handled directly by the bot.
- The `Flutter` web app connects to the webchat channel directly and authenticates with the deployment access key.

The [`WebSocket` URL](./websocket.md#websocket-url) is configured by [`NANOBOT_WS_URL`](./dotenv-docker-secret.md#nanobot_ws_url) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).
