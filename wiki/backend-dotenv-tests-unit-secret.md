# `backend/.env.tests.unit.secret`

- [What is `backend/.env.tests.unit.secret`](#what-is-backendenvtestsunitsecret)
- [`NAME`](#name)
- [`DEBUG`](#debug)
- [`ADDRESS`](#address)
- [`PORT`](#port)
- [`RELOAD`](#reload)
- [`LMS_API_KEY`](#lms_api_key)
- [`BACKEND_ENABLE_INTERACTIONS`](#backend_enable_interactions)
- [`BACKEND_ENABLE_LEARNERS`](#backend_enable_learners)
- [`DB_HOST`](#db_host)
- [`DB_PORT`](#db_port)
- [`DB_NAME`](#db_name)
- [`DB_USER`](#db_user)
- [`DB_PASSWORD`](#db_password)

## What is `backend/.env.tests.unit.secret`

`backend/.env.tests.unit.secret` is an [`.env` file](./environments.md#env-file) that stores [environment variables](./environments.md#environment-variable) for running [unit tests](./quality-assurance.md#unit-test) for the [backend](../docs/design/architecture.md#51-fastapi-application).

<!-- TODO properly document backend -->

Default values: [`backend/.env.tests.unit.example`](../backend/.env.tests.unit.example)

> It was added to [`.gitignore`](./git.md#gitignore) because it may contain [secrets](./environments.md#secrets).

## `NAME`

See [`BACKEND_NAME`](./dotenv-docker-secret.md#backend_name) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

Default: `"Learning Management Service"`

## `DEBUG`

See [`BACKEND_DEBUG`](./dotenv-docker-secret.md#backend_debug) in `.env.docker.secret`.

Default: `false`

## `ADDRESS`

The [IP address](./computer-networks.md#ip-address) the backend [listens on](./computer-networks.md#listen-on-a-port) during tests. [`127.0.0.1`](./computer-networks.md#127001) restricts access to the local machine only.

Default: `127.0.0.1`

## `PORT`

The [port number](./computer-networks.md#port-number) the backend [listens on](./computer-networks.md#listen-on-a-port) during tests.

Default: `8000`

## `RELOAD`

See [`BACKEND_RELOAD`](./dotenv-docker-secret.md#backend_reload) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

Default: `false`

## `LMS_API_KEY`

See [`LMS_API_KEY`](./dotenv-docker-secret.md#lms_api_key) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

Default: `test`

## `BACKEND_ENABLE_INTERACTIONS`

See [`BACKEND_ENABLE_INTERACTIONS`](./dotenv-docker-secret.md#backend_enable_interactions) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

Default: `true`

## `BACKEND_ENABLE_LEARNERS`

See [`BACKEND_ENABLE_LEARNERS`](./dotenv-docker-secret.md#backend_enable_learners) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

Default: `true`

## `DB_HOST`

The hostname of the [database](./database.md#what-is-a-database) used during tests.

Default: `localhost`

## `DB_PORT`

See [`POSTGRES_HOST_PORT`](./dotenv-docker-secret.md#postgres_host_port) in `.env.docker.secret`.

Default: `5432`

## `DB_NAME`

See [`POSTGRES_DB`](./dotenv-docker-secret.md#postgres_db) in `.env.docker.secret`.

Default: `test`

## `DB_USER`

See [`POSTGRES_USER`](./dotenv-docker-secret.md#postgres_user) in `.env.docker.secret`.

Default: `test`

## `DB_PASSWORD`

See [`POSTGRES_PASSWORD`](./dotenv-docker-secret.md#postgres_password) in `.env.docker.secret`.

Default: `test`
