# nanobot-websocket-channel Architecture

## Overview

`nanobot-websocket-channel` is a small workspace for transport adapters that
talk to a deployed Nanobot gateway over WebSocket.

It has three user-facing pieces:

- `nanobot-webchat/` — the Nanobot channel plugin that exposes a WebSocket
  server
- `client-web-flutter/` — the Flutter web UI that connects to that server
- `client-telegram-bot/` — the Telegram bridge that renders the same structured
  protocol in Telegram

It also has one shared internal package:

- `nanobot-channel-protocol/` — typed message schemas shared by the channel and
  Telegram client

## Workspace Layout

```text
nanobot-websocket-channel/
├── architecture.md
├── pyproject.toml
├── nanobot-channel-protocol/
│   └── src/nanobot_channel_protocol/
├── nanobot-webchat/
│   └── src/nanobot_webchat/
├── client-telegram-bot/
│   └── src/client_telegram_bot/
└── client-web-flutter/
```

The workspace root owns the lockfile and shared `uv` workspace membership.

## Message Flow

The common request flow is:

1. A client sends a WebSocket message like `{"content": "Is the backend healthy?"}`.
2. `nanobot-webchat` forwards that request into the Nanobot gateway.
3. Nanobot produces text or structured output.
4. `nanobot-webchat` converts the output into typed protocol messages.
5. The client renders the result in its own UI.

## Shared Protocol

`nanobot-channel-protocol` is the single source of truth for structured
messages.

Current outbound message types:

- `text`
- `choice`
- `confirm`
- `composite`

The protocol package exists so:

- the channel and Telegram client validate the same payload shapes
- rendering logic does not depend on handwritten dictionaries
- protocol changes happen in one place

## Channel Plugin

`nanobot-webchat` is an installable Nanobot channel package. It is responsible
for:

- accepting WebSocket connections
- checking the deployment access key
- forwarding messages into Nanobot
- converting Nanobot output into protocol messages

The channel is the protocol boundary between Nanobot and external clients.

## Telegram Client

`client-telegram-bot` is a standalone Python package under
`src/client_telegram_bot/`.

Its internal split is:

- `bot.py` — process startup and dispatcher wiring
- `settings.py` — environment-backed configuration
- `logging_config.py` — structured JSON logging
- `handlers/` — Telegram command, callback, and message flow
- `services/nanobot_client.py` — WebSocket bridge to Nanobot

The Telegram client does not implement a separate business protocol. It renders
the shared `nanobot-channel-protocol` message types into Telegram-native output.

## Build and Packaging

The Python workspace uses `uv`.

Important packaging rules:

- shared packages live in the workspace root lockfile
- `nanobot-webchat` and `client-telegram-bot` both depend on
  `nanobot-channel-protocol`
- the Telegram Docker image is built from the workspace root, not from the
  subproject directory alone, so workspace dependencies resolve correctly

That is why Compose uses:

- build context: `./nanobot-websocket-channel`
- Dockerfile: `client-telegram-bot/Dockerfile`

## Observability

The Telegram client and channel both emit structured logs.

For Docker deployment, the Telegram client runs under
`opentelemetry-instrument`, which allows:

- container stdout with structured JSON records
- OTEL log export
- OTEL trace export for the client service

## Design Notes

This workspace exists because Nanobot's default Telegram path is not always
usable in every network environment. WebSocket gives us one transport that can
be reused by:

- a browser client
- a Telegram bridge
- future clients with different UIs

The key design choice is to keep the transport protocol shared and typed, while
letting each client own its own rendering and UX.
