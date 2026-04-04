# `Qwen Code` API deployment

<h2>Table of contents</h2>

- [About the `Qwen Code` API deployment](#about-the-qwen-code-api-deployment)
- [Deploy the `Qwen Code` API (REMOTE)](#deploy-the-qwen-code-api-remote)
  - [Initialize the `Qwen Code` API submodule (REMOTE)](#initialize-the-qwen-code-api-submodule-remote)
  - [Update the `Qwen Code` API submodule (REMOTE)](#update-the-qwen-code-api-submodule-remote)
  - [Enter the `Qwen Code` API directory (REMOTE)](#enter-the-qwen-code-api-directory-remote)
  - [Prepare the environment in the `Qwen Code` API directory (REMOTE)](#prepare-the-environment-in-the-qwen-code-api-directory-remote)
  - [Start the `Qwen Code` API (REMOTE)](#start-the-qwen-code-api-remote)

## About the `Qwen Code` API deployment

This page describes how to deploy the [`Qwen Code` API](./qwen-code-api.md#what-is-qwen-code-api) on [your VM](./vm.md#your-vm) using [`Docker Compose`](./docker-compose.md#what-is-docker-compose).

## Deploy the `Qwen Code` API (REMOTE)

Complete these steps:

1. [Connect to the VM as the user `admin`](./vm-access.md#connect-to-the-vm-as-the-user-user-local).
2. [Set up the `Qwen Code` CLI (REMOTE)](./qwen-code.md#set-up-the-qwen-code-cli-remote).
3. [Enter the lab repository directory (REMOTE)](./lab.md#enter-the-lab-repository-directory).
4. [Initialize the `Qwen Code` API submodule (REMOTE)](#initialize-the-qwen-code-api-submodule-remote).
5. [Update the `Qwen Code` API submodule (REMOTE)](#update-the-qwen-code-api-submodule-remote).
6. [Enter the `Qwen Code` API directory (REMOTE)](#enter-the-qwen-code-api-directory-remote).
7. [Prepare the environment in the `Qwen Code` API directory (REMOTE)](#prepare-the-environment-in-the-qwen-code-api-directory-remote).
8. [Start the `Qwen Code` API (REMOTE)](#start-the-qwen-code-api-remote).
9. [Check that the `Qwen Code` API is accessible](./qwen-code-api.md#check-that-the-qwen-code-api-is-accessible) on the VM (REMOTE).

### Initialize the `Qwen Code` API submodule (REMOTE)

> [!NOTE]
> The `Qwen Code` API is included as a [`Git` submodule](./git.md#submodule) in the lab repository.
>
> If you cloned the repository with `--recurse-submodules`, the submodule is already initialized.
> Skip to [Enter the `Qwen Code` API directory](#enter-the-qwen-code-api-directory-remote).

1. To initialize the [submodule](./git.md#submodule),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git submodule update --init qwen-code-api
   ```

### Update the `Qwen Code` API submodule (REMOTE)

1. To update the [submodule](./git.md#submodule) to the latest version,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git submodule update qwen-code-api
   ```

### Enter the `Qwen Code` API directory (REMOTE)

1. To enter the submodule directory,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cd qwen-code-api
   ```

### Prepare the environment in the `Qwen Code` API directory (REMOTE)

1. To create [`qwen-code-api/.env.secret`](./qwen-code-api-dotenv-secret.md),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cp .env.example .env.secret
   ```

2. [Set the variable in `.env.secret`](./environments.md#set-the-variable-to-value-in-the-env-file-at-file-path):

   - [`QWEN_CODE_API_KEY`](./qwen-code-api-dotenv-secret.md#qwen_code_api_key)

### Start the `Qwen Code` API (REMOTE)

1. To start the `Qwen Code` API via [`Docker Compose`](./docker-compose.md#what-is-docker-compose),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.secret up --build -d
   ```

   > <h3>Troubleshooting</h3>
   >
   > [**Port conflict (`port is already allocated`)**](./docker.md#port-conflict-port-is-already-allocated)
   >
   > **`network lms-network was found but has incorrect label com.docker.compose.network set to "default" (expected: "lms-network")`**
   >
   > 1. [Clean up `Docker`](./docker.md#clean-up-docker).
