# Web infrastructure

<h2>Table of contents</h2>

- [What is web infrastructure](#what-is-web-infrastructure)
- [Web server](#web-server)
- [Web client](#web-client)
- [Reverse proxy](#reverse-proxy)
  - [Forward request](#forward-request)
- [`CDN`](#cdn)

## What is web infrastructure

Web infrastructure refers to the software components that enable web communication: [web servers](#web-server), [web clients](#web-client), [reverse proxies](#reverse-proxy), and [`CDNs`](#cdn).

## Web server

A web server is software that delivers content or services to [web clients](#web-client) over a [network](./computer-networks.md#what-is-a-network) (e.g., [Internet](./computer-networks.md#internet)) using a [protocol](./computer-networks.md#protocol).

> [!NOTE]
> We refer to a web server as software only.
>
> Other sources may refer to it as hardware too.
>
> Example: [What is a web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server).

## Web client

A web client is software that requests content from a [web server](#web-server) and displays the received content.

Web clients include [browsers](./useful-programs.md#browser) ([`Chrome`](./useful-programs.md#chrome), [`Firefox`](./useful-programs.md#firefox)) and command-line tools ([`curl`](./useful-programs.md#curl)).

## Reverse proxy

A reverse proxy is a server that sits in front of a backend [service](./backend.md#service) and [forwards](#forward-request) incoming [client](#web-client) requests to it.

The client communicates only with the reverse proxy — it does not connect to the backend directly. The reverse proxy passes the request to the backend, receives the response, and returns it to the client.

Common uses:

- **Routing:** direct requests to the appropriate backend service based on the request path.
- **Serving static files:** serve front-end assets directly without involving the backend.
- **Port management:** expose a single [port](./computer-networks.md#port) to clients while backend services run on separate internal ports.

Example: [`Caddy`](./caddy.md#what-is-caddy) is the reverse proxy in this project.

### Forward request

To forward a request, a [reverse proxy](#reverse-proxy) takes an incoming [`HTTP`](./http.md#what-is-http) request from a [client](#web-client), sends it to a backend [service](./backend.md#service), and returns the backend's response to the client.

Example: in this project, [`Caddy`](./caddy.md#what-is-caddy) is configured to [forward API requests to the backend service](./gateway.md#forward-requests-to-the-backend) ([`backend` service](./docker-compose-yml.md#backend-service)).

## `CDN`

A `CDN` (`Content Delivery Network`) is a network of distributed servers that delivers static files (such as `HTML`, `CSS`, and `JavaScript`) to users from a location close to them. Serving files from a `CDN` reduces load on the origin server and improves response time.
