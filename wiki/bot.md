# `Telegram` bot

<h2>Table of contents</h2>

- [About `Telegram` bots](#about-telegram-bots)
- [Bot username](#bot-username)
- [Your bot username](#your-bot-username)
  - [`<your-bot-username>` placeholder](#your-bot-username-placeholder)
- [Create a `Telegram` bot](#create-a-telegram-bot)

## About `Telegram` bots

A [`Telegram` bot](https://core.telegram.org/bots) is an automated program that runs inside the [`Telegram`](https://telegram.org/) messaging app.
Bots can respond to messages, answer queries, and interact with external services.

In this project, you build a `Telegram` bot that connects to the [LMS API](./lms-api.md#about-the-lms-api) to provide analytics and answer questions about the course data.

Docs:

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [BotFather](https://core.telegram.org/bots#botfather)

## Bot username

A unique name of the bot on `Telegram`.

Example: `@BotFather`

## Your bot username

The [username](#bot-username) of your bot.

### `<your-bot-username>` placeholder

[Your bot username](#your-bot-username) (without `<` and `>`).

## Create a `Telegram` bot

> [!NOTE]
> You need a [`Telegram`](https://telegram.org/) account to create a bot.

1. Open `Telegram` and search for [`@BotFather`](https://t.me/BotFather).

2. Send `/newbot`.

3. Choose a **name** for your bot (e.g., `My LMS Bot`).

4. Choose a [username for your bot](#your-bot-username).

   The username must end in `bot` (e.g., `my_lms_bot`).

5. `BotFather` will reply with a token like:

   ```text
   123456789:ABCdefGhIJKlmNoPQRsTUVwxyz
   ```

6. Save this token — you will need it for the [`BOT_TOKEN`](./dotenv-docker-secret.md#bot_token) variable.
