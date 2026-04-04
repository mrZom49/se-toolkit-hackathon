# VM access

<h2>Table of contents</h2>

- [About the VM access](#about-the-vm-access)
- [Set up the `SSH` access to the VM](#set-up-the-ssh-access-to-the-vm)
- [Set up `SSH` (LOCAL)](#set-up-ssh-local)
  - [Create a new `SSH` key (LOCAL)](#create-a-new-ssh-key-local)
  - [Find the `SSH` key files (LOCAL)](#find-the-ssh-key-files-local)
  - [Get the `SSH` public key (LOCAL)](#get-the-ssh-public-key-local)
  - [Add the `SSH` key to the `ssh-agent` (LOCAL)](#add-the-ssh-key-to-the-ssh-agent-local)
  - [Check the VM is accessible (LOCAL)](#check-the-vm-is-accessible-local)
- [Set up the `SSH` access to the VM as the user `root`](#set-up-the-ssh-access-to-the-vm-as-the-user-root)
  - [Update the `SSH` config to connect to the VM as the user `root` (LOCAL)](#update-the-ssh-config-to-connect-to-the-vm-as-the-user-root-local)
  - [Connect to the VM as the user `root` (LOCAL)](#connect-to-the-vm-as-the-user-root-local)
- [Set up the `SSH` access to the VM as the user `<user>`](#set-up-the-ssh-access-to-the-vm-as-the-user-user)
  - [Create the non-root user `<user>` (REMOTE)](#create-the-non-root-user-user-remote)
    - [Add the non-root user `<user>` (REMOTE)](#add-the-non-root-user-user-remote)
    - [Set the password for the user `<user>` (REMOTE)](#set-the-password-for-the-user-user-remote)
    - [Provide other information about the user `<user>` (REMOTE)](#provide-other-information-about-the-user-user-remote)
    - [Add the user `<user>` to the group `sudo` (REMOTE)](#add-the-user-user-to-the-group-sudo-remote)
  - [Set up the `SSH` key authentication for the user `<user>` (REMOTE)](#set-up-the-ssh-key-authentication-for-the-user-user-remote)
  - [Update the `SSH` config to connect to the VM as the user `<user>` (LOCAL)](#update-the-ssh-config-to-connect-to-the-vm-as-the-user-user-local)
  - [Connect to the VM as the user `<user>` (LOCAL)](#connect-to-the-vm-as-the-user-user-local)
- [Restrict the `SSH` connection](#restrict-the-ssh-connection)
  - [Restrict the `SSH` config for the user `<user>` (LOCAL)](#restrict-the-ssh-config-for-the-user-user-local)
  - [Restrict the `sshd` config for the user `<user>` (REMOTE)](#restrict-the-sshd-config-for-the-user-user-remote)
  - [Restart `sshd` (REMOTE)](#restart-sshd-remote)
  - [Verify that you can't connect to the VM as the user `root` (LOCAL)](#verify-that-you-cant-connect-to-the-vm-as-the-user-root-local)

## About the VM access

VM access is the process of connecting to a [virtual machine](./vm.md#what-is-a-vm) over a network using [`SSH`](./ssh.md#what-is-ssh).

The initial connection uses [the user `root`](./linux.md#the-user-root) because a fresh VM has no other [users](./operating-system.md#user).
After that, you create [a non-root user](./linux.md#a-non-root-user) and switch to it for all further work.

Working as [the user `root`](./linux.md#the-user-root) is risky because every command runs with full [permissions](./linux.md#permissions) — a mistake or a compromised session can modify or delete any [file](./file-system.md#file), change system configuration, or break the [operating system](./operating-system.md#what-is-an-operating-system).
A non-root user operates with limited permissions by default, so accidental damage is contained.
When an administrative action is genuinely needed, the user can escalate temporarily with the [`sudo` command](./linux-administration.md#the-sudo-command).

After switching to the non-root user, you [restrict the `SSH` connection](#restrict-the-ssh-connection) so that [the user `root`](./linux.md#the-user-root) can no longer log in remotely.
This reduces the attack surface of the VM: even if an attacker knows the IP address, the most powerful account is unreachable over the network.

## Set up the `SSH` access to the VM

> [!NOTE]
> Replace the placeholder [`<user>`](./operating-system.md#user-placeholder).

Complete these steps:

<!-- no toc -->
1. [Set up `SSH` (LOCAL)](#set-up-ssh-local).
2. [Create a VM](./vm.md#create-a-vm).
3. [Check that the VM is accessible (LOCAL)](./vm-access.md#check-the-vm-is-accessible-local).
4. [Set up the `SSH` access to the VM as the user `root`](#set-up-the-ssh-access-to-the-vm-as-the-user-root).
5. [Set up the `SSH` access to the VM as the user `<user>`](#set-up-the-ssh-access-to-the-vm-as-the-user-user).
6. [Restrict the `SSH` connection](#restrict-the-ssh-connection).

## Set up `SSH` (LOCAL)

Set up [`SSH`](./ssh.md#what-is-ssh) to connect to a [remote host](./computer-networks.md#remote-host).

Complete these steps:

<!-- no toc -->
1. [Check your current shell](./vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. [Create a new `SSH` key (LOCAL)](#create-a-new-ssh-key-local).
3. [Find the `SSH` key files (LOCAL)](#find-the-ssh-key-files-local).
4. [Get the `SSH` public key (LOCAL)](#get-the-ssh-public-key-local).
5. [Add the `SSH` key to the `ssh-agent` (LOCAL)](#add-the-ssh-key-to-the-ssh-agent-local).

### Create a new `SSH` key (LOCAL)

1. To generate a new key,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh-keygen -t ed25519 -C "se-toolkit-student" -f ~/.ssh/se_toolkit_key
   ```

   *Note:* You can replace `"se-toolkit-student"` with your email or another label.

   *Note:* `-f ~/.ssh/se_toolkit_key` sets a custom file path and name.

   > Note
   > We'll use the `ed25519` algorithm, which is the modern standard for security and performance.
   > We chose this algorithm because it's used in the [`GitHub` docs on generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key).

   > Note
   > Actually, you generate a key pair: a **private key** (secret) and a **public key** (safe to share).

2. **Passphrase:** When prompted `Enter passphrase`, you may type a secure password or press `Enter` for no passphrase.

   *Note:* If you set a passphrase, use `ssh-agent` to avoid retyping it on every connection.

### Find the `SSH` key files (LOCAL)

1. To verify the keys were created,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ls ~/.ssh/se_toolkit_key*
   ```

2. You should see two files listed.

   The file ending in `.pub` contains the [public key](./ssh.md#ssh-public-key).

   Another file contains the [private key](./ssh.md#ssh-private-key).

> [!CAUTION]
>
> Never share the private key.

### Get the `SSH` public key (LOCAL)

1. To view the content of the public key file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cat ~/.ssh/se_toolkit_key.pub
   ```

   The output should be similar to this:

   ```terminal
   ssh-ed25519 AKdk38D3faWJnlFfalFJSKEFGG/vmLQ62Z+vpWCe5e/c2n37cnNc39N3c8qb7cBS+e3d se-toolkit-student
   ```

### Add the `SSH` key to the `ssh-agent` (LOCAL)

1. To start the agent,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   eval "$(ssh-agent -s)"
   ```

2. To add the key to the `ssh-agent`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh-add ~/.ssh/se_toolkit_key
   ```

3. To list the loaded keys,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh-add -l
   ```

   You should see your key fingerprint in the output.

> <h3>Troubleshooting</h3>
>
> **`The agent has no identities`.**
>
> [Add the `SSH` key to the `ssh-agent` (LOCAL)](#add-the-ssh-key-to-the-ssh-agent-local) again.

### Check the VM is accessible (LOCAL)

1. [Connect to the correct network](./vm.md#connect-to-the-correct-network).

2. [Get the IP address of the VM](./vm.md#get-the-ip-address-of-the-vm).

3. To check that the VM is accessible,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ping <your-vm-ip-address>
   ```

   See [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address).

   You should see the output like this:

   ```terminal
   PING <your-vm-ip-address> (<your-vm-ip-address>) 56(84) bytes of data.
   64 bytes from <your-vm-ip-address>: icmp_seq=1 ttl=62 time=4.40 ms
   64 bytes from <your-vm-ip-address>: icmp_seq=2 ttl=62 time=5.34 ms
   64 bytes from <your-vm-ip-address>: icmp_seq=3 ttl=62 time=3.04 ms
   ...
   ```

   The lines should continue being printed.

   > <h3>Troubleshooting</h3>
   >
   > **`Connection timed out`**
   >
   > 1. [Recreate the VM](./vm.md#recreate-the-vm).

## Set up the `SSH` access to the VM as the user `root`

Complete these steps:

1. [Update the `SSH` config to connect to the VM as the user `root` (LOCAL)](#update-the-ssh-config-to-connect-to-the-vm-as-the-user-root-local).
2. [Connect to the VM as the user `root` (LOCAL)](#connect-to-the-vm-as-the-user-root-local).

### Update the `SSH` config to connect to the VM as the user `root` (LOCAL)

1. [Open the file using `code`](./vs-code.md#open-the-file-or-the-directory-using-code):
   `~/.ssh/config`.

2. Add this text at the end of the opened file:

   - `Linux`, `Windows` (`WSL`):

     ```text
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User root
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
     ```

   - `macOS`:

     ```text
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User root
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
        UseKeychain yes
     ```

   Replace the placeholder [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address-placeholder).

   > 🟩 **Tip**
   >
   > If `~/.ssh/config` already contains a `Host se-toolkit-vm` entry, skip this step.

### Connect to the VM as the user `root` (LOCAL)

1. [Connect to the correct network](./vm.md#connect-to-the-correct-network).

2. To connect to the VM,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh se-toolkit-vm
   ```

3. If this is your first time connecting:

   1. You will see a message:
      `The authenticity of host ... can't be established.`

   2. Type `yes` and press `Enter`.

4. After a successful login, you should see this [`SSH` shell prompt](./ssh.md#ssh-shell-prompt):

   ```terminal
   root@<your-vm-name><vm-index>:~#
   ```

   > 🟦 **Note**
   >
   > [`<your-vm-name>`](./vm.md#your-vm-name-placeholder) is the same as you specified when [creating the VM](./vm.md#create-a-vm).

## Set up the `SSH` access to the VM as the user `<user>`

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

Complete these steps:

1. [Create the non-root user `<user>` (REMOTE)](#create-the-non-root-user-user-remote).
2. [Set up the `SSH` key authentication for the user `<user>` (REMOTE)](#set-up-the-ssh-key-authentication-for-the-user-user-remote).
3. [Update the `SSH` config to connect to the VM as the user `<user>` (LOCAL)](#update-the-ssh-config-to-connect-to-the-vm-as-the-user-user-local).
4. [Connect to the VM as the user `<user>` (LOCAL)](#connect-to-the-vm-as-the-user-user-local).

### Create the non-root user `<user>` (REMOTE)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

Complete these steps:

<!-- no toc -->
1. [Set the password for the user `<user>` (REMOTE)](#set-the-password-for-the-user-user-remote).
2. [Provide other information about the user `<user>` (REMOTE)](#provide-other-information-about-the-user-user-remote).
3. [Add the user `<user>` to the group `sudo` (REMOTE)](#add-the-user-user-to-the-group-sudo-remote).

#### Add the non-root user `<user>` (REMOTE)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

1. To create the user `<user>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   adduser <user>
   ```

   > 🟦 **Note**
   >
   > This will create a [group](./operating-system.md#group) with the same name as `<user>`.
   >
   > We'll refer to this group as [`<user-group>`](./operating-system.md#user-group-placeholder).

   The output should be similar to this:

   ```
   info: Adding user `<user>' ...
   info: Selecting UID/GID from range 1000 to 59999 ...
   info: Adding new group `<user-group>' (1002) ...
   info: Adding new user `<user>' (1002) with group `<user-group> (1002)' ...
   info: Creating home directory `/home/<user>' ...
   info: Copying files from `/etc/skel' ...
   New password:
   ```

#### Set the password for the user `<user>` (REMOTE)

1. When prompted for a password (`New password`):

   1. Save it in a password manager to not lose it.

   2. Type it in the [shell](./shell.md#what-is-a-shell) where you were prompted.

   > 🟦 **Note**
   >
   > The shell won't show what you type for security reasons.

#### Provide other information about the user `<user>` (REMOTE)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

1. Keep the default values for these (press `Enter` when prompted):

   ```terminal
   Full Name []:     
   Room Number []: 
   Work Phone []: 
   Home Phone []: 
   Other []: 
   ```

2. When prompted `Is the information correct? [Y/n]`:

   1. Type `y`.

   2. Press `Enter`.

   The output should be similar to this:

   ```terminal
   info: Adding new user `<user>' to supplemental / extra groups `users' ...
   info: Adding user `<user>' to group `users' ...
   ```

#### Add the user `<user>` to the group `sudo` (REMOTE)

> [!NOTE]
> Replace the placeholder [`<user>`](./operating-system.md#user-placeholder).

1. To add the user `<user>` to the [group `sudo`](./linux.md#the-group-sudo),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   usermod -aG sudo <user>
   ```

   There should be no output.

2. To check that the user `<user>` was added to the group `sudo`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   groups <user>
   ```

   The output should be similar to this:

   ```terminal
   <user> : <user-group> sudo users
   ```

   > 🟦 **Note**
   >
   > See [`<user-group>`](./operating-system.md#user-group-placeholder).

### Set up the `SSH` key authentication for the user `<user>` (REMOTE)

> [!NOTE]
> Replace the placeholder [`<user>`](./operating-system.md#user-placeholder).

1. To create the `.ssh/` directory for the [user](./operating-system.md#user) `<user>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   mkdir -p /home/<user>/.ssh
   ```

2. To copy the authorized keys from [the user `root`](./linux.md#the-user-root),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cp /root/.ssh/authorized_keys /home/<user>/.ssh/
   ```

3. To set the correct ownership on the `.ssh/` directory,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   chown -R <user>:<user-group> /home/<user>/.ssh
   ```

   > 🟦 **Note**
   >
   > See [`<user-group>`](./operating-system.md#user-group-placeholder).
   >
   > See [Change the owner and group (recursive)](./linux-administration.md#change-the-owner-and-group-recursive).

4. To set the correct permissions on the `.ssh/` directory,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   chmod 700 /home/<user>/.ssh
   ```

   > 🟦 **Note**
   >
   > See [Set the permissions](./linux-administration.md#set-the-permissions).

   > 🟦 **Note**
   >
   > `SSH` refuses to use keys if the `.ssh/` directory is accessible by other users.
   >
   > See [Mode `700`](./linux.md#mode-700).

5. To set the correct permissions on the `authorized_keys` file,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   chmod 600 /home/<user>/.ssh/authorized_keys
   ```

   > 🟦 **Note**
   >
   > `SSH` ignores `authorized_keys` if it is readable or writable by other users.
   >
   > See [Mode `600`](./linux.md#mode-600).

### Update the `SSH` config to connect to the VM as the user `<user>` (LOCAL)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

1. [Open the file](./vs-code.md#open-the-file-or-the-directory-using-code):
   `~/.ssh/config`.

2. Find the `se-toolkit-vm` entry.

3. Change `User root` to `User <user>`:

   - `Linux`, `Windows`:

     ```text
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User <user>
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
     ```

   - `macOS`:

     ```text
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User <user>
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
        UseKeychain yes
     ```

   Replace the placeholder [`<user>`](./operating-system.md#user-placeholder).

### Connect to the VM as the user `<user>` (LOCAL)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

1. [Connect to the correct network](./vm.md#connect-to-the-correct-network).

2. [Open a new `VS Code Terminal`](./vs-code.md#vs-code-terminal).

3. To connect to the VM as the user `<user>`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh se-toolkit-vm
   ```

   Replace the placeholder [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address-placeholder).

4. To confirm you are logged in as the user `<user>`,
   not [the user `root`](./linux.md#the-user-root),
   look at the [shell prompt](./ssh.md#ssh-shell-prompt).

   You should see:

   ```terminal
   <user>@<your-vm-name><vm-index>:~$
   ```

   > 🟦 **Note**
   >
   > The [current working directory](./shell.md#current-working-directory) is the [home directory (`~`)](./file-system.md#home-directory-).
   >
   > [`<user>`](./operating-system.md#user-placeholder) is the same as you specified when [updating the `SSH` config to connect to the VM as the user `<user>` (LOCAL)](#update-the-ssh-config-to-connect-to-the-vm-as-the-user-user-local).
   >
   > [`<your-vm-name>`](./vm.md#your-vm-name-placeholder) is the same as you specified when [creating the VM](./vm.md#create-a-vm).
   >
   > `<vm-index>` is some number.

## Restrict the `SSH` connection

Complete these steps:

<!-- no toc -->
1. [Restrict the `SSH` config for the user `<user>` (LOCAL)](#restrict-the-ssh-config-for-the-user-user-local).
2. [Restrict the `sshd` config for the user `<user>` (REMOTE)](#restrict-the-sshd-config-for-the-user-user-remote).
3. [Restart `sshd` (REMOTE)](#restart-sshd-remote).
4. [Connect to the VM as the user `<user>` (LOCAL)](#connect-to-the-vm-as-the-user-user-local).
5. [Verify that you can't connect to the VM as the user `root` (LOCAL)](#verify-that-you-cant-connect-to-the-vm-as-the-user-root-local).
6. [Verify that you can still connect to the VM as the user `<user>` (LOCAL)](#connect-to-the-vm-as-the-user-user-local).

### Restrict the `SSH` config for the user `<user>` (LOCAL)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

1. [Open the file](./vs-code.md#open-the-file-or-the-directory-using-code):
   `~/.ssh/config`.

2. Add `PasswordAuthentication no` there:

   - `Linux`, `Windows`:

     ```text
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User <user>
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
        PasswordAuthentication no
     ```

   - `macOS`:

     ```text
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User <user>
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
        UseKeychain yes
        PasswordAuthentication no
     ```

   Replace the placeholder [`<user>`](./operating-system.md#user-placeholder).

3. [Connect to the VM as the user `<user>` (LOCAL)](#connect-to-the-vm-as-the-user-user-local) to verify you can connect as the user `<user>` without a password.

### Restrict the `sshd` config for the user `<user>` (REMOTE)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

1. [Connect to the VM as the user `<user>` (LOCAL)](#connect-to-the-vm-as-the-user-user-local) if not yet connected.

2. To open the [`sshd`](./ssh.md#sshd) config:

   1. [Run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

      ```terminal
      sudo nano /etc/ssh/sshd_config
      ```

   2. [Type the password for the user `<user>`](./shell.md#type-the-password-for-the-user).

3. Find the line `PermitRootLogin yes` and set it to:

   ```text
   PermitRootLogin no
   ```

4. Find the line `#PasswordAuthentication yes` and set it to:

   ```text
   PasswordAuthentication no
   ```

5. To write the changes:

   1. Press `Ctrl+O`.
   2. Press `Enter`.

6. To close the editor, press `Ctrl+X`.

### Restart `sshd` (REMOTE)

> [!NOTE]
> See [`<user>`](./operating-system.md#user-placeholder).

1. To validate the [`sshd`](./ssh.md#sshd) config:

   1. [Run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

      ```terminal
      sudo sshd -t
      ```

   2. [Type the password for the user `<user>`](./shell.md#type-the-password-for-the-user).

2. If the command prints no output, the config is valid.

   If it prints errors, fix them in `/etc/ssh/sshd_config` before continuing.

3. To restart `sshd`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl restart sshd
   ```

   The output should be empty.

### Verify that you can't connect to the VM as the user `root` (LOCAL)

1. [Open a new `VS Code Terminal`](./vs-code.md#open-a-new-vs-code-terminal).

2. To try to connect to the VM as the user `root`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh root@<your-vm-ip-address>
   ```

   Replace the placeholder [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address-placeholder).

   The output should be similar to this:

   ```terminal
   Received disconnect from <your-vm-ip-address> port 22:2: Too many authentication failures
   Disconnected from <your-vm-ip-address> port 22
   ```

<!-- 7. If you use the `ms-vscode-remote.remote-ssh` extension in `VS Code`, the status bar should show that you are connected to a remote host.
   TODO explain how to use -->
