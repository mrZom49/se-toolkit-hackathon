# `.env.docker.secret`

<h2>Table of contents</h2>

- [What is `.env.docker.secret`](#what-is-envdockersecret)
- [Registry prefixes](#registry-prefixes)
  - [`REGISTRY_PREFIX_DOCKER_HUB`](#registry_prefix_docker_hub)
  - [`REGISTRY_PREFIX_GHCR`](#registry_prefix_ghcr)
- [`backend`](#backend)
  - [`BACKEND_NAME`](#backend_name)
  - [`BACKEND_DEBUG`](#backend_debug)
  - [`BACKEND_RELOAD`](#backend_reload)
  - [`BACKEND_CONTAINER_ADDRESS`](#backend_container_address)
  - [`BACKEND_CONTAINER_PORT`](#backend_container_port)
  - [`BACKEND_HOST_ADDRESS`](#backend_host_address)
  - [`BACKEND_HOST_PORT`](#backend_host_port)
  - [`BACKEND_ENABLE_INTERACTIONS`](#backend_enable_interactions)
  - [`BACKEND_ENABLE_LEARNERS`](#backend_enable_learners)
- [`postgres`](#postgres)
  - [`POSTGRES_DB`](#postgres_db)
  - [`POSTGRES_USER`](#postgres_user)
  - [`POSTGRES_PASSWORD`](#postgres_password)
  - [`POSTGRES_HOST_ADDRESS`](#postgres_host_address)
  - [`POSTGRES_HOST_PORT`](#postgres_host_port)
- [`pgadmin`](#pgadmin)
  - [`PGADMIN_EMAIL`](#pgadmin_email)
  - [`PGADMIN_PASSWORD`](#pgadmin_password)
  - [`PGADMIN_HOST_ADDRESS`](#pgadmin_host_address)
  - [`PGADMIN_HOST_PORT`](#pgadmin_host_port)
- [`caddy`](#caddy)
  - [`CADDY_CONTAINER_PORT`](#caddy_container_port)
- [Gateway](#gateway)
  - [`GATEWAY_HOST_ADDRESS`](#gateway_host_address)
  - [`GATEWAY_HOST_PORT`](#gateway_host_port)
  - [`LMS_API_KEY`](#lms_api_key)
  - [`GATEWAY_BASE_URL`](#gateway_base_url)
- [`Autochecker` API](#autochecker-api)
  - [`AUTOCHECKER_API_URL`](#autochecker_api_url)
  - [`AUTOCHECKER_API_LOGIN`](#autochecker_api_login)
  - [`AUTOCHECKER_API_PASSWORD`](#autochecker_api_password)
- [Telegram bot](#telegram-bot)
  - [`BOT_TOKEN`](#bot_token)
- [LLM API](#llm-api)
  - [`LLM_API_KEY`](#llm_api_key)
  - [`LLM_API_BASE_URL`](#llm_api_base_url)
  - [`LLM_API_MODEL`](#llm_api_model)
- [`Nanobot`](#nanobot)
  - [`NANOBOT_GATEWAY_CONTAINER_ADDRESS`](#nanobot_gateway_container_address)
  - [`NANOBOT_GATEWAY_CONTAINER_PORT`](#nanobot_gateway_container_port)
  - [`NANOBOT_WEBCHAT_CONTAINER_ADDRESS`](#nanobot_webchat_container_address)
  - [`NANOBOT_WEBCHAT_CONTAINER_PORT`](#nanobot_webchat_container_port)
  - [`NANOBOT_ACCESS_KEY`](#nanobot_access_key)
  - [`NANOBOT_WS_URL`](#nanobot_ws_url)
- [Constants](#constants)
  - [`CONST_POSTGRESQL_SERVICE_NAME`](#const_postgresql_service_name)
  - [`CONST_POSTGRESQL_SERVER_NAME`](#const_postgresql_server_name)
  - [`CONST_POSTGRESQL_DEFAULT_PORT`](#const_postgresql_default_port)
  - [`CONST_PGADMIN_CONTAINER_PORT`](#const_pgadmin_container_port)

## What is `.env.docker.secret`

`.env.docker.secret` is a [`.env` file](./environments.md#env-file) that stores [environment variables](./environments.md#environment-variable) for [`Docker Compose`](./docker-compose.md#what-is-docker-compose).

The values are substituted into [`docker-compose.yml`](../docker-compose.yml) when running commands with the `--env-file` flag (e.g., `docker compose --env-file .env.docker.secret up --build`).

Therefore, use the values from the `.env.docker.secret` file stored on the [machine](./computer-networks.md#machine) where you deployed via `Docker Compose`.

The default values are in [`.env.docker.example`](../.env.docker.example).

> [!NOTE]
> `.env.docker.secret` was added to [`.gitignore`](./git.md#gitignore) because you may specify there
> [secrets](./environments.md#secrets) such as the [LMS API key](./lms-api.md#lms-api-key) or the [address of your VM](./vm.md#your-vm-ip-address).

## Registry prefixes

Prefixes prepended to [Docker image](./docker.md#image) names when pulling base images.
By default, they point to [`Harbor`](https://goharbor.io/) cache proxies on the university network to avoid rate limits.
Outside the university network, set them to empty strings to pull directly from the source registries.

### `REGISTRY_PREFIX_DOCKER_HUB`

A [registry prefix](#registry-prefixes) for [Docker Hub](./docker.md#dockerhub) images.

Used as a build argument in [`docker-compose.yml`](../wiki/docker-compose-yml.md#what-is-docker-composeyml).

Default: `harbor.pg.innopolis.university/docker-hub-cache/`

### `REGISTRY_PREFIX_GHCR`

A [registry prefix](#registry-prefixes) for [GitHub Container Registry](https://ghcr.io) images.

Used as a build argument in [`docker-compose.yml`](../wiki/docker-compose-yml.md).

Default: `harbor.pg.innopolis.university/ghcr-proxy/`

## `backend`

Variables for the [`backend` service](./docker-compose-yml.md#backend-service).

### `BACKEND_NAME`

The display name of the application.

Default: `"Learning Management Service"`

### `BACKEND_DEBUG`

Enables debug mode in the [web server](./web-infrastructure.md#web-server). When `true`, the server returns detailed error messages.

Default: `false`

### `BACKEND_RELOAD`

Enables auto-reload. When `true`, the [web server](./web-infrastructure.md#web-server) restarts automatically when source files change.

Default: `false`

### `BACKEND_CONTAINER_ADDRESS`

The [IP address](./computer-networks.md#ip-address) the backend [listens on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: [`0.0.0.0`](./computer-networks.md#0000)

### `BACKEND_CONTAINER_PORT`

The [port number](./computer-networks.md#port-number) the backend [listens on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: `8000`

### `BACKEND_HOST_ADDRESS`

The [IP address](./computer-networks.md#ip-address) exposed on the [host](./computer-networks.md#host). [`127.0.0.1`](./computer-networks.md#127001) restricts access to the local machine only.

Default: `127.0.0.1`

### `BACKEND_HOST_PORT`

The [port number](./computer-networks.md#port-number) exposed on the [host](./computer-networks.md#host) for accessing the backend.

Default: `42001`

### `BACKEND_ENABLE_INTERACTIONS`

A [feature flag](./environments.md#feature-flag) for enabling the `/interactions` endpoint.

Default: `true`

### `BACKEND_ENABLE_LEARNERS`

A [feature flag](./environments.md#feature-flag) for enabling the `/learners` endpoint.

Default: `true`

## `postgres`

Variables for the [`postgres` service](./docker-compose-yml.md#postgres-service).

### `POSTGRES_DB`

The name of the [database](./database.md#what-is-a-database) created on the first startup.

Default: `db-lab-7`

### `POSTGRES_USER`

The username for the [`PostgreSQL`](./database.md#postgresql) database.

Default: `postgres`

### `POSTGRES_PASSWORD`

The password for the [`PostgreSQL`](./database.md#postgresql) database.

Default: `postgres`

### `POSTGRES_HOST_ADDRESS`

The [IP address](./computer-networks.md#ip-address) exposed on the [host](./computer-networks.md#host). [`127.0.0.1`](./computer-networks.md#127001) restricts access to the local machine only.

Default: `127.0.0.1`

### `POSTGRES_HOST_PORT`

The [port number](./computer-networks.md#port-number) exposed on the [host](./computer-networks.md#host) for accessing [`PostgreSQL`](./database.md#postgresql).

Default: `42004`

## `pgadmin`

Variables for the [`pgadmin` service](./docker-compose-yml.md#pgadmin-service).

### `PGADMIN_EMAIL`

The email used to log in to [`pgAdmin`](./pgadmin.md#what-is-pgadmin).

Default: `admin@example.com`

### `PGADMIN_PASSWORD`

The password used to log in to [`pgAdmin`](./pgadmin.md#what-is-pgadmin).

Default: `admin`

### `PGADMIN_HOST_ADDRESS`

The [IP address](./computer-networks.md#ip-address) exposed on the [host](./computer-networks.md#host).

[`127.0.0.1`](./computer-networks.md#127001) restricts access to the local machine only.

Default: `127.0.0.1`

### `PGADMIN_HOST_PORT`

The [port number](./computer-networks.md#port-number) exposed on the [host](./computer-networks.md#host) for accessing [`pgAdmin`](./pgadmin.md#what-is-pgadmin).

Default: `42003`

## `caddy`

Variables for the [`caddy` service](./docker-compose-yml.md#caddy-service).

### `CADDY_CONTAINER_PORT`

The [port number](./computer-networks.md#port-number) that [`Caddy`](./caddy.md#what-is-caddy) [listens on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: `80`

## Gateway

Variables for the [gateway](./gateway.md#about-the-gateway).

### `GATEWAY_HOST_ADDRESS`

The [IP address](./computer-networks.md#ip-address) of the [gateway](./gateway.md#about-the-gateway) exposed on the [host](./computer-networks.md#host).

Default: [`0.0.0.0`](./computer-networks.md#0000)

### `GATEWAY_HOST_PORT`

The [gateway host port](./gateway.md#gateway-host-port).

Default: `42002`

### `LMS_API_KEY`

The [LMS API key](./lms-api.md#lms-api-key).

Default: `<lms-api-key>`

<!-- TODO everywhere
don't mention [`.env.docker.secret`](#what-is-envdockersecret) inline?
-->

Set in [`.env.docker.secret`](#what-is-envdockersecret).

### `GATEWAY_BASE_URL`

The [gateway base URL](./gateway.md#gateway-base-url).

Default: `<gateway-base-url>`

## `Autochecker` API

Variables for the [autochecker](./autochecker.md#what-is-the-autochecker) ETL pipeline.

### `AUTOCHECKER_API_URL`

The [`Autochecker` API base URL](./autochecker-api.md)

Default: `https://auche.namaz.live`

### `AUTOCHECKER_API_LOGIN`

The [`Autochecker` API login](./autochecker-api.md#autochecker-api-login).

Default: `<autochecker-api-login>`

### `AUTOCHECKER_API_PASSWORD`

The [`Autochecker` API password](./autochecker-api.md#autochecker-api-password).

Default: `<autochecker-api-password>`.

## Telegram bot

Variables for the [`Telegram` bot client](./client-telegram-bot.md#about-the-telegram-bot-client).

### `BOT_TOKEN`

The Telegram bot token obtained from [`@BotFather`](https://core.telegram.org/bots#botfather).

Default: `<bot-token>`

## LLM API

Variables for the [LLM API](./llm-api.md#about-llm-api) used by the deployed `Nanobot` agent and related tooling.

### `LLM_API_KEY`

The [LLM API key](./llm-api.md#llm-api-key).

Default: `<llm-api-key>`

### `LLM_API_BASE_URL`

The [LLM API base URL](./llm-api.md#llm-api-base-url).

Default: `<llm-api-base-url>`

### `LLM_API_MODEL`

The [LLM API model](./llm-api.md#llm-api-model).

Default: `<llm-api-model>`

## `Nanobot`

Variables for the [`Nanobot`](./nanobot.md) gateway and webchat channel.

### `NANOBOT_GATEWAY_CONTAINER_ADDRESS`

The [IP address](./computer-networks.md#ip-address) the [`Nanobot` gateway](./nanobot.md#gateway) is [listening on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: [`0.0.0.0`](./computer-networks.md#0000)

### `NANOBOT_GATEWAY_CONTAINER_PORT`

The [port number](./computer-networks.md#port-number) the [`Nanobot` gateway](./nanobot.md#gateway) [listens on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: `18790`

### `NANOBOT_WEBCHAT_CONTAINER_ADDRESS`

The [IP address](./computer-networks.md#ip-address) the [`Nanobot` webchat channel](./nanobot.md#webchat-channel) [`WebSocket`](./websocket.md#what-is-websocket) server [listens on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: [`0.0.0.0`](./computer-networks.md#0000)

### `NANOBOT_WEBCHAT_CONTAINER_PORT`

The [port number](./computer-networks.md#port-number) the [`Nanobot` webchat channel](./nanobot.md#webchat-channel) [`WebSocket`](./websocket.md#what-is-websocket) server [listens on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: `8765`

### `NANOBOT_ACCESS_KEY`

The password that protects access to the [`Nanobot` web client](./nanobot.md#webchat-channel).

Set this yourself in `.env.docker.secret`.
There is no default value on purpose.

### `NANOBOT_WS_URL`

The full [`WebSocket`](./websocket.md#what-is-websocket) URL that the [`Telegram` bot client](./client-telegram-bot.md#about-the-telegram-bot-client) uses to connect to the [`Nanobot` webchat channel](./nanobot.md#webchat-channel).

Default: `ws://nanobot:8765`

## Constants

Values that should not be changed.
They are defined here for convenient referencing in [`docker-compose.yml`](../docker-compose.yml).

### `CONST_POSTGRESQL_SERVICE_NAME`

The [`Docker Compose` service name](./docker-compose.md#service-name) for [`PostgreSQL`](./database.md#postgresql).
Other [services](./docker-compose.md#service) use this name to connect to the database via [`Docker Compose` networking](./docker-compose.md#docker-compose-networking).

Default: `postgres`

### `CONST_POSTGRESQL_SERVER_NAME`

The display name for the [`PostgreSQL`](./database.md#postgresql) server in [`pgAdmin`](./pgadmin.md#what-is-pgadmin).

Default: `postgres-lab-7`

### `CONST_POSTGRESQL_DEFAULT_PORT`

The default [port number](./computer-networks.md#port-number) [`PostgreSQL`](./database.md#postgresql) [listens on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: `5432`

### `CONST_PGADMIN_CONTAINER_PORT`

The [port number](./computer-networks.md#port-number) that [`pgAdmin`](./pgadmin.md#what-is-pgadmin) is [listening on](./computer-networks.md#listen-on-a-port) inside the [container](./docker.md#container).

Default: `80`
