# SE Toolkit Bot

Telegram bot for interacting with an LMS-aware Nanobot deployment.

## Quick Start

### 1. Setup environment

Set these environment variables before starting the bot:

- `BOT_TOKEN` — Telegram bot token from @BotFather
- `NANOBOT_WS_URL` — WebSocket endpoint exposed by the Nanobot channel
- `NANOBOT_ACCESS_KEY` — deployment access key for the Nanobot WebSocket channel

If your agent setup expects per-user LMS credentials, users can provide them at runtime with `/login <api_key>`. The bot will send that key separately from the deployment access key.

### 2. Run the bot

```bash
uv run python -m client_telegram_bot
```

## Available Commands

| Command         | Description               |
| --------------- | ------------------------- |
| `/start`        | Welcome message           |
| `/help`         | List all commands         |
| `/health`       | Check backend status      |
| `/labs`         | List available labs       |
| `/scores <lab>` | View pass rates for a lab |

## Natural Language Queries

You can also ask questions in plain language:

- "What labs are available?"
- "Show me the scores for lab-04"
- "Is the backend working?"
- "Who are the top learners in lab-01?"

## Docker Deployment

Add to `.env.docker.secret`:

```bash
BOT_TOKEN=your-telegram-bot-token
NANOBOT_WS_URL=ws://host.docker.internal:8765
NANOBOT_ACCESS_KEY=your-private-access-key
```

Then run:

```bash
docker compose --env-file .env.docker.secret up -d bot
```

## Architecture

- **Package** (`src/client_telegram_bot/`) — Telegram bot application code
- **Handlers** (`src/client_telegram_bot/handlers/`) — Command and message flow
- **Services** (`src/client_telegram_bot/services/`) — WebSocket client for the Nanobot channel
- **Entry point** (`python -m client_telegram_bot`) — package module startup
