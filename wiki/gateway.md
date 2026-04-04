# Gateway

<h2>Table of contents</h2>

- [About the gateway](#about-the-gateway)
- [Gateway host port](#gateway-host-port)
  - [`<gateway-host-port>` placeholder](#gateway-host-port-placeholder)
- [Gateway base URL](#gateway-base-url)
  - [`<gateway-base-url>` placeholder](#gateway-base-url-placeholder)
- [`Caddy`](#caddy)
  - [`Caddyfile`](#caddyfile)
- [`Caddy` duties](#caddy-duties)
  - [Listen on the specific port](#listen-on-the-specific-port)
  - [Forward requests to the backend](#forward-requests-to-the-backend)
  - [Forward requests to `pgAdmin`](#forward-requests-to-pgadmin)
  - [Serve frontend files](#serve-frontend-files)

## About the gateway

The gateway is the single entry point to the LMS system, implemented using [`Caddy`](#caddy).
It listens on a single [host port](#gateway-host-port) and routes requests to the appropriate backend services.

## Gateway host port

The [port number](./computer-networks.md#port-number) (without `<` and `>`) which the gateway is available at on the [host](./computer-networks.md#host).

The port number is the value of [`GATEWAY_HOST_PORT`](./dotenv-docker-secret.md#gateway_host_port) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

### `<gateway-host-port>` placeholder

The [gateway host port](#gateway-host-port) (without `<` and `>`).

## Gateway base URL

> [!NOTE]
>
> See [URL](./computer-networks.md#url).

- (REMOTE or LOCAL) When running the request on the [host](./computer-networks.md#host) where the [LMS API is deployed](./lms-api-deployment.md#about-the-lms-api-deployment):

  `http://localhost:<gateway-host-port>`

- (LOCAL) When running the request on the local machine and the LMS API is deployed on the VM:

  `http://<your-vm-ip-address>:<gateway-host-port>`

Replace the placeholders:

- [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address-placeholder)
- [`<gateway-host-port>`](./gateway.md#gateway-host-port-placeholder)

### `<gateway-base-url>` placeholder

The [gateway base URL](#gateway-base-url) (without `<` and `>`).

## `Caddy`

In this project, `Caddy` [is configured using the `Caddyfile`](#caddyfile).

### `Caddyfile`

The [`Caddyfile`](./caddy.md#caddyfile) at [`caddy/Caddyfile`](../caddy/Caddyfile) specifies the [`Caddy` duties](#caddy-duties).

## `Caddy` duties

<!-- no toc -->
- [Listen on the specific port](./computer-networks.md#listen-on-a-port) inside a [`Docker` container](./docker.md#container).
- [Forward requests to the backend](#forward-requests-to-the-backend)
- [Forward requests to `pgAdmin`](#forward-requests-to-pgadmin)
- [Serve the frontend files](#serve-frontend-files)

### Listen on the specific port

`Caddy` listens on the port whose port number is the value of [`GATEWAY_HOST_PORT`](./dotenv-docker-secret.md#gateway_host_port) from [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

### Forward requests to the backend

`Caddy` routes to the [`backend` service](./docker-compose-yml.md#backend-service) these [API endpoints](./web-api.md#endpoint):

- `/items*`
- `/learners*`
- `/interactions*`
- `/pipeline*`
- `/analytics*`
- `/docs*`
- `/openapi.json`

### Forward requests to `pgAdmin`

`Caddy` routes to [`pgAdmin`](./pgadmin.md#what-is-pgadmin) these [API endpoints](./web-api.md#endpoint):

- `/utils/pgadmin*`

### Serve frontend files

`Caddy` serves static front-end files from `/srv` for all other paths.

The `try_files` directive falls back to `index.html` for client-side routing.
