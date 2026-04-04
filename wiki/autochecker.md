# Autochecker

<h2>Table of contents</h2>

- [What is the `Autochecker`](#what-is-the-autochecker)
- [The `Autochecker` bot](#the-autochecker-bot)
  - [Set up the `Autochecker` bot](#set-up-the-autochecker-bot)
  - [Check the task using the `Autochecker` bot](#check-the-task-using-the-autochecker-bot)
- [The `Autochecker` agent](#the-autochecker-agent)
  - [Provide the `Autochecker` agent with access to the VM (REMOTE)](#provide-the-autochecker-agent-with-access-to-the-vm-remote)

## What is the `Autochecker`

The `Autochecker` is a system that you can ask to [check](#check-the-task-using-the-autochecker-bot) your repository and your VM when you work on a task.

It has three main components:

<!-- no toc -->
- [The `Autochecker` bot](#the-autochecker-bot)
- [The `Autochecker` agent](#the-autochecker-agent)
- [The `Autochecker` API](./autochecker-api.md#about-the-autochecker-api)

## The `Autochecker` bot

The `Autochecker` bot in Telegram.

<https://t.me/auchebot>

### Set up the `Autochecker` bot

1. Open in `Telegram` the [`Autochecker` bot](#the-autochecker-bot).
2. Send `/start`.
3. Provide the info:

   - [Your VM IP address](./vm.md#your-vm-ip-address)
   - etc.

### Check the task using the `Autochecker` bot

1. Open in `Telegram` the [`Autochecker` bot](#the-autochecker-bot).
2. Click the lab.
3. Click the task.

## The `Autochecker` agent

An agent that can check the setup on [your VM](./vm.md#your-vm) and send requests to it.

### Provide the `Autochecker` agent with access to the VM (REMOTE)

> [!NOTE]
> Replace the placeholder [`<user>`](./operating-system.md#user-placeholder).

> Add the [`SSH` public key](./ssh.md#ssh-public-key) for [the `Autochecker` agent](#the-autochecker-agent) so that it can access the VM as the user `<user>`.

1. [Connect to the VM as the user `<user>`](./vm-access.md#connect-to-the-vm-as-the-user-user-local).

2. To check whether the `SSH` public key is already present,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   grep se-toolkit-autochecker ~/.ssh/authorized_keys
   ```

   Skip the following steps in this section if you see:

   ```terminal
   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker
   ```

3. To add the `SSH` public key,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker" >> ~/.ssh/authorized_keys
   ```

4. To verify the `SSH` public key was added,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   grep se-toolkit-autochecker ~/.ssh/authorized_keys
   ```

   You should see:

   ```terminal
   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker
   ```
