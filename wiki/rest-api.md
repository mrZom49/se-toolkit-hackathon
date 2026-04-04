# `REST` API

<h2>Table of contents</h2>

- [What is a `REST` API](#what-is-a-rest-api)
- [Key principles](#key-principles)
- [Example](#example)

## What is a `REST` API

A `REST` API (`Representational State Transfer`) is a style of [API](./api.md#what-is-an-api) design that uses [`HTTP`](./http.md#what-is-http) methods and noun-based resource paths to expose resources.

It is not a [protocol](./computer-networks.md#protocol) — it is a set of conventions for structuring an API on top of `HTTP`.

Docs:

- [What is REST](https://restfulapi.net/)

## Key principles

- **[Resources](./web-api.md#resource)** are identified by paths: `/items`, `/learners`, `/interactions`.
- **[`HTTP` methods](./http.md#http-request-method)** define the action: `GET` (read), `POST` (create), `PUT` (update), `DELETE` (remove).
- **[Status codes](./http.md#http-response-status-code)** indicate the result: `200`, `201`, `404`, etc.

## Example

| Action               | Method | Path           | Status code |
| -------------------- | ------ | -------------- | ----------- |
| List all items       | `GET`  | `/items`       | `200`       |
| Get one item         | `GET`  | `/items/{id}`  | `200`/`404` |
| Create an item       | `POST` | `/items`       | `201`       |
| Update an item       | `PUT`  | `/items/{id}`  | `200`/`404` |
