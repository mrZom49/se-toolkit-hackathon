# `docker-compose.yml`

<h2>Table of contents</h2>

- [What is `docker-compose.yml`](#what-is-docker-composeyml)
- [Services](#services)
  - [`backend` service](#backend-service)
  - [`postgres` service](#postgres-service)
  - [`pgadmin` service](#pgadmin-service)
  - [`caddy` service](#caddy-service)
- [Volumes](#volumes)
  - [`postgres_data`](#postgres_data)

## What is `docker-compose.yml`

[`docker-compose.yml`](../docker-compose.yml) is the [`Docker Compose`](./docker-compose.md#what-is-docker-compose) configuration file for this project. It defines the local deployment stack, including the LMS [`backend`](#backend-service), [`postgres`](#postgres-service), [`pgadmin`](#pgadmin-service), [`caddy`](#caddy-service), AI-related services such as `nanobot` and `qwen-code-api`, and observability services such as `victorialogs`, `victoriatraces`, and `otel-collector`.

In this project, the services read their configuration from [environment variables](./environments.md#environment-variable) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

Docs:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)

## Services

<!-- no toc -->
- [`backend` service](#backend-service)
- [`postgres` service](#postgres-service)
- [`pgadmin` service](#pgadmin-service)
- [`caddy` service](#caddy-service)

This page focuses on the core LMS web stack services.
Other services from [`docker-compose.yml`](../docker-compose.yml), such as `client-web-react`, `client-web-flutter`, `nanobot`, `qwen-code-api`, `client-telegram-bot`, `victorialogs`, `victoriatraces`, and `otel-collector`, are documented in their own pages or in task instructions.

### `backend` service

The `backend` service runs the [backend web server](./web-infrastructure.md#web-server).

It builds from the root [`backend/Dockerfile`](../backend/Dockerfile), which uses a multi-stage build: the first stage installs [`Python`](./python.md#what-is-python) dependencies with [`uv`](./python.md#uv), and the second stage runs the application.

Configuration in [`docker-compose.yml`](../docker-compose.yml):

- **`build.context: ./backend`** — builds the [image](./docker.md#image) from the [`backend/`](../backend/) project directory.
- **`build.additional_contexts.workspace: .`** — exposes the repository root to the Docker build so the backend image can copy shared workspace files.
- **`restart: unless-stopped`** — restarts the [container](./docker.md#container) automatically unless it is explicitly stopped.
- **`ports`** — maps [`BACKEND_HOST_ADDRESS`](./dotenv-docker-secret.md#backend_host_address):[`BACKEND_HOST_PORT`](./dotenv-docker-secret.md#backend_host_port) on the [host](./computer-networks.md#host) to [`BACKEND_CONTAINER_PORT`](./dotenv-docker-secret.md#backend_container_port) inside the container.
- **`environment`** — passes [environment variables](./environments.md#environment-variable) into the container. The values come from [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).
- **`depends_on`** — waits for the [`postgres` service](#postgres-service) to pass its [health check](./docker-compose.md#health-checks) and for `otel-collector` to start before starting.

### `postgres` service

The `postgres` service runs a [`PostgreSQL`](./database.md#postgresql) [database server](./database.md#database-server).

Configuration in [`docker-compose.yml`](../docker-compose.yml):

- **`image`** — uses the `postgres:18.3-alpine` [image](./docker.md#image).
- **`restart: unless-stopped`** — restarts the [container](./docker.md#container) automatically unless it is explicitly stopped.
- **`environment`** — sets the database name ([`POSTGRES_DB`](./dotenv-docker-secret.md#postgres_db)), user ([`POSTGRES_USER`](./dotenv-docker-secret.md#postgres_user)), and password ([`POSTGRES_PASSWORD`](./dotenv-docker-secret.md#postgres_password)) from [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).
- **`ports`** — maps [`POSTGRES_HOST_ADDRESS`](./dotenv-docker-secret.md#postgres_host_address):[`POSTGRES_HOST_PORT`](./dotenv-docker-secret.md#postgres_host_port) on the [host](./computer-networks.md#host) to [`CONST_POSTGRESQL_DEFAULT_PORT`](./dotenv-docker-secret.md#const_postgresql_default_port) inside the container.
- **`volumes`** — mounts [`postgres_data`](#postgres_data) for persistent data storage and [`backend/src/lms_backend/data/init.sql`](../backend/src/lms_backend/data/init.sql) as the database initialization script. Scripts in `/docker-entrypoint-initdb.d/` run on the first startup of the container.
- **`healthcheck`** — runs `pg_isready` every 5 seconds to verify the database is ready to accept connections. Other services use this [health check](./docker-compose.md#health-checks) to wait before starting.

### `pgadmin` service

The `pgadmin` service runs [`pgAdmin`](./pgadmin.md#what-is-pgadmin), a web interface for managing [`PostgreSQL`](./database.md#postgresql) databases.

Configuration in [`docker-compose.yml`](../docker-compose.yml):

- **`image`** — uses the `dpage/pgadmin4:latest` [image](./docker.md#image).
- **`restart: unless-stopped`** — restarts the [container](./docker.md#container) automatically unless it is explicitly stopped.
- **`environment`** — sets the login email ([`PGADMIN_EMAIL`](./dotenv-docker-secret.md#pgadmin_email)) and password ([`PGADMIN_PASSWORD`](./dotenv-docker-secret.md#pgadmin_password)) from [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).
- **`ports`** — maps [`PGADMIN_HOST_ADDRESS`](./dotenv-docker-secret.md#pgadmin_host_address):[`PGADMIN_HOST_PORT`](./dotenv-docker-secret.md#pgadmin_host_port) on the [host](./computer-networks.md#host) to port `80` inside the container.
- **`depends_on`** — waits for the [`postgres` service](#postgres-service) to pass its [health check](./docker-compose.md#health-checks) before starting.

### `caddy` service

The `caddy` service runs [`Caddy`](./caddy.md#what-is-caddy), a [reverse proxy](./web-infrastructure.md#reverse-proxy) that serves frontend files and forwards [API](./api.md#what-is-an-api) requests to the [`backend` service](#backend-service) and other internal services.

Configuration in [`docker-compose.yml`](../docker-compose.yml):

- **`image`** — uses the `caddy:2.11-alpine` [image](./docker.md#image).
- **`depends_on`** — waits for the backend, frontend build, nanobot, AI, and observability services to start before starting.
- **`environment`** — passes [`CADDY_CONTAINER_PORT`](./dotenv-docker-secret.md#caddy_container_port), [`BACKEND_CONTAINER_PORT`](./dotenv-docker-secret.md#backend_container_port), and related port variables from [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).
- **`ports`** — maps [`GATEWAY_HOST_ADDRESS`](./dotenv-docker-secret.md#gateway_host_address):[`GATEWAY_HOST_PORT`](./dotenv-docker-secret.md#gateway_host_port) on the [host](./computer-networks.md#host) to `CADDY_CONTAINER_PORT` inside the [container](./docker.md#container).
- **`volumes`** — mounts [`caddy/Caddyfile`](../caddy/Caddyfile) as the [`Caddy` configuration](./caddy.md#caddyfile) and mounts the built React and Flutter static files from named volumes.

See [`Caddy` duties](./gateway.md#caddy-duties) for how the `Caddyfile` routes requests.

## Volumes

[Volumes](./docker-compose.md#volume) are defined under the `volumes:` key at the top level of [`docker-compose.yml`](../docker-compose.yml).

### `postgres_data`

A named [volume](./docker-compose.md#volume) that stores [`PostgreSQL`](./database.md#postgresql) data. Data in this volume persists across container restarts.

The [`postgres` service](#postgres-service) mounts this volume at `/var/lib/postgresql/data`.

See [Resetting the database](./docker-postgres.md#resetting-the-database) to remove this volume and reinitialize the database.
