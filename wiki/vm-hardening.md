# VM hardening

<h2>Table of contents</h2>

- [About the VM hardening](#about-the-vm-hardening)
- [Hardening tools](#hardening-tools)
  - [`ufw`](#ufw)
  - [`fail2ban`](#fail2ban)
- [Harden the VM](#harden-the-vm)
  - [Set up `ufw` (REMOTE)](#set-up-ufw-remote)
  - [Set up `fail2ban` (REMOTE)](#set-up-fail2ban-remote)
- [Disable VM hardening services](#disable-vm-hardening-services)
  - [Disable `ufw`](#disable-ufw)
  - [Disable `fail2ban`](#disable-fail2ban)

## About the VM hardening

VM hardening is the process of securing a [virtual machine](./vm.md#what-is-a-vm) by reducing its attack surface.

Docs:

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

## Hardening tools

- [`ufw`](#ufw)
- [`fail2ban`](#fail2ban)

### `ufw`

`ufw` (`Uncomplicated Firewall`) is a simple firewall for [`Linux`](./linux.md#what-is-linux).

By default, `ufw` denies all incoming traffic on all ports except the specified ones.

### `fail2ban`

`fail2ban` blocks [IP addresses](./computer-networks.md#ip-address) that make too many failed login attempts.

Even if password authentication is disabled, `fail2ban` remains useful:

- It rate-limits repeated [`SSH`](./ssh.md#what-is-ssh) connection attempts.
- It can be extended to protect other services.

## Harden the VM

> [!NOTE]
> Replace the placeholder [`<user>`](./operating-system.md#user-placeholder).

Complete these steps:

<!-- no toc -->
1. [Connect to the VM as the user `<user>` (LOCAL)](./vm-access.md#connect-to-the-vm-as-the-user-user-local).
2. [Set up `ufw` (REMOTE)](#set-up-ufw-remote).
3. [Set up `fail2ban` (REMOTE)](#set-up-fail2ban-remote).

### Set up `ufw` (REMOTE)

> [!NOTE]
> See [`ufw`](#ufw).

1. To allow [`SSH`](./ssh.md#what-is-ssh),

   1. [Run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

      ```terminal
      sudo ufw allow 22
      ```

   2. [Type the password for the user `<user>`](./shell.md#type-the-password-for-the-user).

   The output should look like this:

   ```terminal
   Rules updated
   Rules updated (v6)
   ```

   > 🟪 **Important**
   >
   > Always allow `SSH` (port 22) before enabling `ufw`.
   > Otherwise, you will lock yourself out of your VM.

2. To allow the [gateway host port](./gateway.md#gateway-host-port),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo ufw allow <gateway-host-port>
   ```

   Replace the placeholder [`<gateway-host-port>`](./gateway.md#gateway-host-port-placeholder).

   The output should look like this:

   ```terminal
   Rules updated
   Rules updated (v6)
   ```

3. To enable the [firewall](./computer-networks.md#firewall),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo ufw enable
   ```

4. When prompted `Command may disrupt existing ssh connections. Proceed with operation (y|n)?`:
  
   1. Type `y`.

   2. Press `Enter`.

   The output should look like this:

   ```terminal
   Firewall is active and enabled on system startup
   ```

5. To check the status,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo ufw status
   ```

   The output should look like this:

   ```terminal
   Status: active

   To                         Action      From
   --                         ------      ----
   22                         ALLOW       Anywhere                  
   42002                      ALLOW       Anywhere                  
   22 (v6)                    ALLOW       Anywhere (v6)             
   42002 (v6)                 ALLOW       Anywhere (v6) 
   ```

### Set up `fail2ban` (REMOTE)

> [!NOTE]
> See [`fail2ban`](#fail2ban)

1. To update the package list,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo apt update
   ```

   The output should look like this:

   ```terminal
   ...
   Reading package lists... Done
   Building dependency tree... Done
   Reading state information... Done
   16 packages can be upgraded. Run 'apt list --upgradable' to see them.
   ```

2. To install `fail2ban`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo apt install -y fail2ban
   ```

   The output should look like this:

   ```terminal
   ...
   
   No user sessions are running outdated binaries.

   No VM guests are running outdated hypervisor (qemu) binaries on this host.
   ```

3. To enable the service,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl enable fail2ban
   ```

   The output should look like this:

   ```terminal
   Synchronizing state of fail2ban.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
   Executing: /usr/lib/systemd/systemd-sysv-install enable fail2ban
   ```

4. To start the service,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl start fail2ban
   ```

   The output should be empty.

5. To check the status,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl status fail2ban
   ```

   The output should look like this:

   ```terminal
   ● fail2ban.service - Fail2Ban Service
        Loaded: loaded (/usr/lib/systemd/system/fail2ban.service; enabled; preset: enabled)
        Active: active (running) since Wed 2026-03-18 21:53:57 MSK; 1min 48s ago
   ...
   ```

## Disable VM hardening services

- [Disable `ufw`](#disable-ufw)
- [Disable `fail2ban`](#disable-fail2ban)

### Disable `ufw`

1. To disable the firewall:

   1. [Run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

      ```terminal
      sudo ufw disable
      ```

   2. [Type the password for the user `<user>`](./shell.md#type-the-password-for-the-user).
  
   The output should look like this:

   ```terminal
   Firewall is active and enabled on system startup
   ```

### Disable `fail2ban`

1. (Optional) To stop the service,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl stop fail2ban
   ```

   The output should be empty.
