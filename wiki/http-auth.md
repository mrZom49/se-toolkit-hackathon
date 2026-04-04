# `HTTP` authentication and authorization

<h2>Table of contents</h2>

- [`HTTP` authentication](#http-authentication)
- [`HTTP` authorization](#http-authorization)

## `HTTP` authentication

Authentication is the process of verifying the identity of a client making a request to an [API](./api.md#what-is-an-api).

In `HTTP` APIs, a common authentication mechanism is an [API key](./web-api.md#api-key).

The API key is sent in the `Authorization` header of every request:

```http
Authorization: Bearer <api-key>
```

The server rejects requests with a missing or invalid key with [`401 Unauthorized`](./http.md#401-unauthorized).

Docs:

- [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)

## `HTTP` authorization

Authorization is the process of determining whether an authenticated [client](./web-infrastructure.md#web-client) has permission to access a specific [endpoint](./web-api.md#endpoint) or [resource](./web-api.md#resource).

A client can be [authenticated](#http-authentication) but still lack permission for certain resources.

Common `HTTP` status codes related to auth:

- [`401` (Unauthorized)](./http.md#401-unauthorized) — the client is not authenticated (missing or invalid [API key](./web-api.md#api-key)).
- [`403` (Forbidden)](./http.md#403-forbidden) — the client is authenticated but not allowed to access this resource.

Docs:

- [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)
- [Authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Authorization)
