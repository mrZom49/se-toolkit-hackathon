# `Swagger UI`

<h2>Table of contents</h2>

- [What is `Swagger UI`](#what-is-swagger-ui)
- [Open `Swagger UI`](#open-swagger-ui)
- [Authorize in `Swagger UI`](#authorize-in-swagger-ui)
- [Try an endpoint in `Swagger UI`](#try-an-endpoint-in-swagger-ui)

## What is `Swagger UI`

`Swagger UI` is an interactive web page that lets you explore and test a [REST API](./rest-api.md#what-is-a-rest-api).

`FastAPI` auto-generates `Swagger UI` at the `/docs` path.

Actions:

- [What is `Swagger UI`](#what-is-swagger-ui)
- [Open `Swagger UI`](#open-swagger-ui)
- [Authorize in `Swagger UI`](#authorize-in-swagger-ui)
- [Try an endpoint in `Swagger UI`](#try-an-endpoint-in-swagger-ui)

## Open `Swagger UI`

1. Open in a browser: `<gateway-base-url>/docs`.

   Replace the placeholder [`<gateway-base-url>`](./gateway.md#gateway-base-url-placeholder).

   You should see the `Swagger UI` with all endpoints listed.

## Authorize in `Swagger UI`

If the API requires authentication:

1. [Open `Swagger UI`](#open-swagger-ui).
2. Click the `Authorize` button (lock icon at the top right).
3. In the `Value` field, enter the [`<api-key>`](./web-api.md#api-key).
4. Click `Authorize`.
5. Click `Close`.

All subsequent requests will include the API key in the `Authorization` header.

## Try an endpoint in `Swagger UI`

1. [Open `Swagger UI`](#open-swagger-ui).
2. Click on an endpoint (e.g., `GET /items`).
3. Click `Try it out`.
4. Fill in parameters if needed.
5. Click `Execute`.
6. See the response below: status code, response body, headers.
