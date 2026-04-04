# Security

<h2>Table of contents</h2>

- [API key authentication](#api-key-authentication)
- [VM hardening](#vm-hardening)

## API key authentication

API key authentication is a simple mechanism to protect endpoints.

How it works:

1. The server has a secret key stored in an environment variable (e.g., `API_KEY`).
2. The client sends the key in the `Authorization` header: `Authorization: Bearer <key>`.
3. The server checks if the key matches. If not, it returns `401 Unauthorized`.

> [!NOTE]
> This is a simple shared key mechanism. It has no user accounts, roles, or permissions.
> It is sufficient for protecting a development API but not for production systems with many users.

## VM hardening

See [VM hardening](./vm-hardening.md).
