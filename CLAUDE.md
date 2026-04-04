# Lab authoring conventions

See [`contributing/conventions/agents/authoring.md`](contributing/conventions/agents/authoring.md) for full instructions on editing tasks, wiki, code, and conventions.

## Docker

Always use the env file flag when running docker compose:

```sh
docker compose --env-file .env.docker.secret <command>
```

## Flutter

Run Flutter CLI commands via the poe task (uses Docker):

```sh
uv run poe flutter <args>
```

For example, to analyze: `uv run poe flutter analyze lib/chat_screen.dart`
