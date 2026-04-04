# nanobot-websocket-channel

A WebSocket channel plugin for [nanobot-ai](https://github.com/HKUDS/nanobot), plus web and Telegram clients that connect through it.

See [architecture.md](architecture.md) for the workspace structure, shared
protocol, and build model.

## What's inside

| Directory              | What it is                                                       |
| ---------------------- | ---------------------------------------------------------------- |
| `nanobot-webchat/`     | Python project for the WebSocket channel plugin                  |
| `client-web-flutter/`  | Flutter web chat UI — connects to the agent via WebSocket        |
| `client-telegram-bot/` | Telegram bot — bridges Telegram users to the agent via WebSocket |

## Why WebSocket?

Nanobot has built-in Telegram support, but the Telegram Bot API is blocked from some networks (e.g., Russian university servers). The WebSocket channel is a transport-agnostic alternative — any web app can connect to it.

## Installation

Install the webchat channel plugin into your nanobot environment:

```bash
uv add nanobot-webchat --path /path/to/nanobot-websocket-channel/nanobot-webchat
```

Then enable it in your nanobot `config.json`:

```json
{
  "channels": {
    "webchat": {
      "enabled": true,
      "allow_from": ["*"]
    }
  }
}
```

The gateway will start a WebSocket server. Clients connect at `ws://<host>:<port>`.

## Protocol

```
Client → Server: {"content": "user message"}
Server → Client: {"type": "text", "content": "response", "format": "markdown"}
```

Structured response types: `text`, `choice` (buttons), `confirm` (yes/no), `composite` (text + interaction).

Required deployment key: pass `?access_key=...` on WebSocket connect. The channel validates it against `NANOBOT_ACCESS_KEY` and refuses to start if that env var is missing.

Optional LMS key: LMS-aware clients may also pass `?api_key=...`. The channel forwards it to the agent as a legacy `[LMS_API_KEY=...]` prompt prefix so per-user LMS flows keep working without reusing that key as deployment auth.
