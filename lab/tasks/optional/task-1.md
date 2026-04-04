# Optional — Add a Telegram Bot Client

## Background

The Flutter web client connects to nanobot via the WebSocket channel. A Telegram bot is another client that connects the same way — demonstrating that **the agent is the interface, not any particular frontend**. Same agent, same tools, same answers — different client.

The Telegram bot code is in the `nanobot-websocket-channel` repo you added in Task 2 (at `nanobot-websocket-channel/client-telegram-bot/`). It connects to nanobot via WebSocket and relays messages between Telegram users and the agent. Unlike the web client, you can keep the Telegram bot LMS-specific if you want a `/login` flow there.

### Note on Telegram in Russia

The Telegram Bot API (`api.telegram.org`) is blocked from most Russian servers. Your university VM can't reach it. The bot connects to nanobot via WebSocket (local Docker network — no internet needed for that part), but Telegram polling requires a machine that *can* reach the Bot API. You can either run the bot locally or on a non-Russian server.

## What to do

1. Get a Telegram bot token from [@BotFather](https://t.me/BotFather).

2. Uncomment the scaffolded `client-telegram-bot` service in `docker-compose.yml`:
   - Build from `nanobot-websocket-channel/client-telegram-bot/`
   - Use the `additional_contexts` entry that exposes `./nanobot-websocket-channel` as the Docker build workspace, because the Dockerfile copies shared files from that repository root
   - Environment: `BOT_TOKEN`, `NANOBOT_ACCESS_KEY`, and `NANOBOT_WS_URL`
   - If the bot runs inside Docker Compose, use `NANOBOT_WS_URL=ws://nanobot:8765`
   - If the bot runs on your local machine or another host, use the public/proxied endpoint instead, for example `NANOBOT_WS_URL=ws://localhost:42002/ws/chat` with SSH port forwarding to the VM
   - `depends_on: nanobot`

   If you use the repository root `uv` workspace tooling, also uncomment the
   matching `nanobot-websocket-channel/client-telegram-bot` lines in the root
   `pyproject.toml` under:

   - `[tool.uv.workspace].members`
   - `[tool.uv.sources]`

   Do not append `?access_key=...` yourself — the bot adds that query parameter automatically.
   If you run the bot outside Docker Compose, use the same environment variables and start it from `nanobot-websocket-channel/client-telegram-bot/` by following that repo's README.

   If you want to keep Telegram LMS-specific, users can still provide a per-user LMS key with `/login <api_key>`.

3. Deploy and test. Open Telegram, find your bot, and ask it a question.

4. Ask the same question in the Flutter app and in Telegram. Compare — same agent, same answers.

## Acceptance criteria

- The Telegram bot runs as a Docker Compose service (or locally if VM can't reach Telegram API).
- Free-text messages are routed to the agent and responses appear in Telegram.
- The same queries work from both Telegram and the Flutter web app.
