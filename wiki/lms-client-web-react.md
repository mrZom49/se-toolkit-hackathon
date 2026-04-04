# LMS frontend

<!-- TODO it's about the system explorer -->
<!-- TODO client-web-flutter is a chatbot -->

<h2>Table of contents</h2>

- [About the LMS frontend](#about-the-lms-frontend)
- [Pages](#pages)
  - [Items page](#items-page)
  - [Dashboard page](#dashboard-page)
- [Authentication](#authentication)
- [Set up the LMS frontend development server](#set-up-the-lms-frontend-development-server)
- [Production build](#production-build)

## About the LMS frontend

The LMS frontend is a single-page [frontend](./frontend.md#what-is-frontend) application built with `React` and `TypeScript` that provides a web interface for the [LMS API](./lms-api.md#about-the-lms-api).

After you [authenticate](#authentication), you can see [items](#items-page) and [analytics dashboards](#dashboard-page) loaded from the LMS API.

The source code is in the [`client-web-react/`](../client-web-react/) directory.

Docs:

- [React documentation](https://react.dev/learn)
- [Vite documentation](https://vite.dev/guide/)

## Pages

The frontend has two pages:

<!-- no toc -->
- [Items page](#items-page)
- [Dashboard page](#dashboard-page)

You can switch between pages using the navigation bar at the top.

### Items page

The Items page displays a table of items fetched from the `GET /items/` [endpoint](./web-api.md#endpoint).
Each row shows the item ID, type, title, and creation date.

### Dashboard page

The Dashboard page displays analytics charts for a selected lab.
It fetches data from the `/analytics/*` [endpoints](./web-api.md#endpoint).

Charts:

- **Submissions Timeline** — a line chart showing the number of submissions per day.
- **Score Distribution** — a bar chart showing how many students fall into each score bucket.
- **Group Performance** — a bar chart showing the average score per group.
- **Task Pass Rates** — a doughnut chart showing the average score per task.

A lab selector dropdown lets you filter the data by lab.

## Authentication

The frontend requires the [LMS API key](./lms-api.md#lms-api-key) to access the [LMS API](./lms-api.md#about-the-lms-api).
When you open the frontend, you see a form asking for the API key.

After you enter the key, the frontend stores it in the browser's `localStorage` and sends it as a `Bearer` token in the `Authorization` [header](./http.md#http-request-header) with every request.

Click **Disconnect** in the navigation bar to clear the stored key and return to the login form.

## Set up the LMS frontend development server

[`Vite`](https://vite.dev/) runs a development server that serves the frontend locally and [proxies](./web-infrastructure.md#reverse-proxy) API requests to the backend.

The proxy target is configured by [`VITE_API_TARGET`](./client-web-react-dotenv-secret.md#vite_api_target) in [`client-web-react/.env.secret`](./client-web-react-dotenv-secret.md#what-is-client-web-reactenvsecret).

1. To navigate to the `client-web-react/` directory,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cd client-web-react
   ```

2. To create the [environment file](./client-web-react-dotenv-secret.md#what-is-client-web-reactenvsecret),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cp .env.example .env.secret
   ```

   Then set [`VITE_API_TARGET`](./client-web-react-dotenv-secret.md#vite_api_target) to your [gateway base URL](./gateway.md#gateway-base-url).

3. To install [`Node.js`](./nodejs.md#what-is-nodejs) dependencies,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   pnpm install
   ```

4. To start the development server,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   pnpm run dev
   ```

## Production build

In production, the frontend is built into static files by [`Vite`](https://vite.dev/) and served by [`Caddy`](./caddy.md#what-is-caddy).

The [`caddy` service](./docker-compose-yml.md#caddy-service) builds the frontend using [`client-web-react/Dockerfile`](../client-web-react/Dockerfile) and [serves the output files](./gateway.md#serve-frontend-files) from `/srv`.
