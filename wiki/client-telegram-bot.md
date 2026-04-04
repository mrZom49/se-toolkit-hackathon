# Client: `Telegram` bot

<h2>Table of contents</h2>

- [About the `Telegram` bot client](#about-the-telegram-bot-client)
- [Where the code lives](#where-the-code-lives)
- [Environment variables](#environment-variables)
- [How it fits into Lab 8](#how-it-fits-into-lab-8)

## About the `Telegram` bot client

The `Telegram` bot client is a standalone [Python](./python.md#what-is-python) service built with `aiogram` that connects the [`Telegram`](./bot.md#about-telegram-bots) messaging interface to the [`Nanobot`](./nanobot.md#about-nanobot) AI agent over the webchat `WebSocket` channel.

Docs:

- [aiogram documentation](https://docs.aiogram.dev/en/latest/)

## Where the code lives

The bot source code is not stored in this lab repository anymore.
It lives in the standalone `nanobot-websocket-channel` repository:

<https://github.com/inno-se-toolkit/nanobot-websocket-channel/tree/main/client-telegram-bot>

That repo also contains the current Dockerfile, README, and local run instructions for the bot.

## Environment variables

The current bot expects these variables:

- [`BOT_TOKEN`](./dotenv-docker-secret.md#bot_token) — Telegram bot token from `@BotFather`
- [`NANOBOT_WS_URL`](./dotenv-docker-secret.md#nanobot_ws_url) — `WebSocket` URL for the deployed `Nanobot` channel
- [`NANOBOT_ACCESS_KEY`](./dotenv-docker-secret.md#nanobot_access_key) — deployment access key required by the webchat channel

If you want the Telegram client to remain LMS-specific, users can still provide a per-user LMS key with `/login <api_key>`.

## How it fits into Lab 8

In Lab 8 this bot is optional.
The required path uses the Flutter web client, while the Telegram bot demonstrates that the same agent can serve multiple frontends.

For the lab workflow, follow [Optional Task 1](../lab/tasks/optional/task-1.md).

> [!NOTE]
> The Telegram Bot API is blocked from many Russian servers. The bot may need to run locally or on a non-Russian host even though it talks to `Nanobot` over the local Docker network.
