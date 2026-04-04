# Virtual machine

<h2>Table of contents</h2>

- [What is a VM](#what-is-a-vm)
- [Your VM](#your-vm)
- [Your VM name](#your-vm-name)
  - [`<your-vm-name>` placeholder](#your-vm-name-placeholder)
- [Your VM IP address](#your-vm-ip-address)
  - [`<your-vm-ip-address>` placeholder](#your-vm-ip-address-placeholder)
- [Connect to the correct network](#connect-to-the-correct-network)
- [Go to the VMs site](#go-to-the-vms-site)
- [Create a VM](#create-a-vm)
  - [Create a subscription](#create-a-subscription)
  - [Delete the existing VM](#delete-the-existing-vm)
  - [Create a VM using the subscription](#create-a-vm-using-the-subscription)
  - [Go to the VM page](#go-to-the-vm-page)
  - [Check the VM is running](#check-the-vm-is-running)
  - [Get the IP address of the VM](#get-the-ip-address-of-the-vm)
- [Recreate the VM](#recreate-the-vm)
- [Set up the VM](#set-up-the-vm)

## What is a VM

A VM (virtual machine) is a software-emulated computer that runs on a physical [host machine](./computer-networks.md#host), with its own [operating system](./operating-system.md#what-is-an-operating-system) and isolated environment.

In this lab, you use a VM provided by the university to deploy and run the application remotely over [`SSH`](./ssh.md#what-is-ssh).

Docs:

- [What is a virtual machine?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-virtual-machine)

## Your VM

The university provides you a virtual machine (VM) for labs and home experiments for the duration of the `Software Engineering Toolkit` course.

You probably won't have access to the VMs after the course finishes.

See [VM image](./vm-info.md) for the information about your VM.

## Your VM name

The name you chose when [creating the VM](#create-a-vm-using-the-subscription).

### `<your-vm-name>` placeholder

[Your VM name](#your-vm-name) (without `<` and `>`).

## Your VM IP address

The [IP address](./computer-networks.md#ip-address) of [your VM](#your-vm) in the `UniversityStudent` [network](./computer-networks.md#what-is-a-network).

See [Get the IP address of your VM](#get-the-ip-address-of-the-vm).

### `<your-vm-ip-address>` placeholder

[Your VM IP address](#your-vm-ip-address) (without `<` and `>`).

Example: `192.0.2.1`.

See [Get the IP address of the VM](#get-the-ip-address-of-the-vm).

## Connect to the correct network

1. Disable `VPN`.

2. Connect your local machine (laptop) to the `Wi-Fi` network `UniversityStudent`.

## Go to the VMs site

1. [Connect to the correct network](#connect-to-the-correct-network).
2. Open the [https://vm.innopolis.university](https://vm.innopolis.university) site in a browser.

## Create a VM

Complete these steps:

<!-- no toc -->
1. [Connect to the correct network](#connect-to-the-correct-network).
2. [Create a subscription](#create-a-subscription) if you don't have one.
3. [Delete the existing VM](#delete-the-existing-vm) if you have one.
4. [Create a VM using the subscription](#create-a-vm-using-the-subscription).
5. [Go to the VM page](#go-to-the-vm-page).
6. [Check the VM is running](#check-the-vm-is-running).
7. [Get the IP address of the VM](#get-the-ip-address-of-the-vm).
8. [Check the VM is accessible (LOCAL)](./vm-access.md#check-the-vm-is-accessible-local).

### Create a subscription

1. [Go to the VMs site](#go-to-the-vms-site).
2. Click `+ NEW`.
3. Click `MY ACCOUNT`.
4. Click `ADD SUBSCRIPTION`.
5. Click `Software Engineering Toolkit`.
6. Click the checkmark.
7. Go to the [`SUBSCRIPTIONS`](https://vm.innopolis.university/#Workspaces/MyAccountExtension/subscriptions) tab.
8. Look at the `SUBSCRIPTION` column.

   You should see there `Software Engineering Toolkit`.

   The `Status` of this subscription can be `Syncing` or `Active`.

   It can be `Syncing` for a long time.

   Nevertheless, you'll be able to [create a VM using this subscription](#create-a-vm-using-the-subscription) in approximately 15 minutes.

   Don't just sit and wait. Complete other steps.

### Delete the existing VM

1. [Go to the VM page](#go-to-the-vm-page).
2. Click `DELETE`.

### Create a VM using the subscription

1. [Set up `SSH` (LOCAL)](./vm-access.md#set-up-ssh-local) if it's not yet set up.
2. [Go to the VMs site](#go-to-the-vms-site).
3. Click `+ NEW`.
4. Click `STANDALONE VIRTUAL MACHINE`.
5. Click `FROM GALLERY`.
6. Click `ALL`.
7. Click `Linux Ubuntu 24.04 Software Engineering Toolkit`.
8. Click `->` to go to the page 2.
9. Fill in the fields:
    - `NAME`: Write the name of your VM (we'll refer to it as [`<your-vm-name>`](#your-vm-name-placeholder) in the instructions).
    - `NEW PASSWORD`: Write the password.
    - `CONFIRM`: Write the same password.
    - `ADMINISTRATOR SSH KEY`:
       1. [Get the `SSH` public key (LOCAL)](./vm-access.md#get-the-ssh-public-key-local).
       2. Copy the **full content** of the public key file.
       3. Paste the content into the input field.
10. Note that the user's name on the VM is [`root`](./linux.md#the-user-root).
11. Click `->` to go to the page 3.
12. Go to `NETWORK ADAPTER 1`.
13. Click `Not Connected`.
14. In the drop-down list, click `StudentsCourses01;10.93.24.0/22`.
15. Click checkmark to complete the setup.
16. In approximately 20 minutes, [check the VM is accessible](./vm-access.md#check-the-vm-is-accessible-local).

### Go to the VM page

1. [Go to the VMs site](#go-to-the-vms-site).
2. Click `VIRTUALS MACHINES`.
3. Look at the `NAME` column.
4. Click [`<your-vm-name>`](#your-vm-name-placeholder).
5. Click `DASHBOARD`.
6. You should be on the VM page.

### Check the VM is running

1. [Go to the VM page](./vm.md#go-to-the-vm-page).
2. Go to the `quick glance` sidebar.
3. You should see:

   ```terminal
   Status
   Running
   ```

   > <h3>Troubleshooting</h3>
   >
   > **The VM isn't running in 20 minutes after creation**
   >
   > 1. Wait 10 more minutes.
   > 2. If the status doesn't change, [recreate the VM](#recreate-the-vm).

### Get the IP address of the VM

1. [Go to the VM page](#go-to-the-vm-page).
2. Go to the `quick glance` sidebar (on the right).
3. Go to `IP ADDRESS(ES)`.
4. You should see there:

   ```
   StudentsCourses01 - <your-vm-ip-address>
   ```

   See [`<your-vm-ip-address>`](#your-vm-ip-address-placeholder).

   Example: `StudentsCourses01` - `192.0.2.1`

## Recreate the VM

1. [Delete the existing VM](#delete-the-existing-vm).
2. [Create a new VM](#create-a-vm-using-the-subscription).

## Set up the VM

1. [Recreate the VM](#recreate-the-vm) if you want to set up a clean VM.
2. [Set up the `SSH` access to the VM as the user `admin`](./vm-access.md#set-up-the-ssh-access-to-the-vm).
3. [Provide the `Autochecker` agent with access to the VM as the user `admin`](./autochecker.md#provide-the-autochecker-agent-with-access-to-the-vm-remote).
4. [Configure `Git` as the user `admin`](./git.md#configure-git).
5. [Set up `Docker` as the user `admin`](./docker.md#set-up-docker-as-the-user-user-remote).
6. [Harden the VM as the user `admin`](./vm-hardening.md#harden-the-vm).
