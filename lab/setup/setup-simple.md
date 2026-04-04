# Lab setup

- [1. Required steps](#1-required-steps)
  - [1.1. Set up your fork](#11-set-up-your-fork)
    - [1.1.1. Fork the course instructors' repo](#111-fork-the-course-instructors-repo)
    - [1.1.2. Go to your fork](#112-go-to-your-fork)
    - [1.1.3. Enable issues](#113-enable-issues)
    - [1.1.4. Add a classmate as a collaborator](#114-add-a-classmate-as-a-collaborator)
    - [1.1.5. Protect your `main` branch](#115-protect-your-main-branch)
    - [1.1.6. Sync your fork with upstream](#116-sync-your-fork-with-upstream)
  - [1.2. SSH into your VM and set up the environment there](#12-ssh-into-your-vm-and-set-up-the-environment-there)
  - [1.3. Stop Lab 7 services on your VM to free the ports](#13-stop-lab-7-services-on-your-vm-to-free-the-ports)
  - [1.4. Start the services on your VM](#14-start-the-services-on-your-vm)
  - [1.5. Populate the database](#15-populate-the-database)
  - [1.6. Verify the deployment on your VM](#16-verify-the-deployment-on-your-vm)
  - [1.7. Keep the deployment on your VM](#17-keep-the-deployment-on-your-vm)
  - [1.8. Set up SSH for the autochecker](#18-set-up-ssh-for-the-autochecker)
  - [1.9. Set up LLM access (Qwen Code API)](#19-set-up-llm-access-qwen-code-api)
  - [1.10. Coding agent](#110-coding-agent)

## 1. Required steps

> [!IMPORTANT]
> Do the whole lab on your **VM**. You can work through a plain SSH shell or through `VS Code` Remote-SSH. When this guide says `localhost`, it means the VM itself or a forwarded port from that VM. Do not install or run `nanobot` on your main machine.

### 1.1. Set up your fork

#### 1.1.1. Fork the course instructors' repo

1. Fork the [lab's repo](https://github.com/inno-se-toolkit/se-toolkit-lab-8).

We refer to your fork as `fork` and to the original repo as `upstream`.

#### 1.1.2. Go to your fork

1. Go to your fork: `https://github.com/`**`YOUR_GITHUB_USERNAME`**`/se-toolkit-lab-8`.

#### 1.1.3. Enable issues

1. [Enable issues](../../wiki/github.md#enable-issues).

#### 1.1.4. Add a classmate as a collaborator

1. [Add a collaborator](../../wiki/github.md#add-a-collaborator) — your partner.
2. Your partner should add you as a collaborator in their repo.

#### 1.1.5. Protect your `main` branch

1. [Protect a branch](../../wiki/github.md#protect-a-branch).

#### 1.1.6. Sync your fork with upstream

1. [Sync your fork](../../wiki/git-workflow.md#pull-changes-from-the-branch-main-on-the-remote-upstream) so you have the latest changes from the course repository.

   Do this **before cloning** to the VM, and again whenever the instructors push updates.

### 1.2. SSH into your VM and set up the environment there

1. [Connect to your VM](../../wiki/vm-access.md#connect-to-the-vm-as-the-user-user-local).

   You will do the whole lab on VM. All the steps below and the tasks will be done on VM.

2. Clone your fork there:

   ```terminal
   git clone --recurse-submodules https://github.com/YOUR_GITHUB_USERNAME/se-toolkit-lab-8
   ```

   Replace **`YOUR_GITHUB_USERNAME`** with your GitHub username.

   > [!NOTE]
   > The `--recurse-submodules` flag clones the Qwen Code API [submodule](../../wiki/git.md#submodule) included in the repository.

   > [!TIP]
   > If you already cloned the repo earlier without `--recurse-submodules`, the `qwen-code-api/` directory may be empty and Docker builds will fail later.
   > From the repo root, run:
   >
   > ```terminal
   > git submodule update --init --recursive
   > ```

   > [!IMPORTANT]
   > You will need to **push code from the VM** to GitHub. Set this up now so it works later.
   >
   > **If you use VS Code Remote-SSH** — git credentials are forwarded automatically. No extra setup needed.
   >
   > **If you use a plain SSH terminal** — pick one of these:
   >
   > **Option A — SSH key** (recommended, one-time setup):
   > 1. On the VM, generate a key (skip if `~/.ssh/id_ed25519.pub` already exists):
   >
   >    ```
   >    ssh-keygen -t ed25519 -C "your-email@example.com"
   >    ```
   >
   >    Press Enter three times to accept defaults (no passphrase is fine).
   > 2. Print the public key:
   >
   >    ```
   >    cat ~/.ssh/id_ed25519.pub
   >    ```
   >
   > 3. Copy the output. In your browser, go to <https://github.com/settings/keys> → **New SSH key** → paste → **Add SSH key**.
   > 4. Clone with the SSH URL instead of HTTPS:
   >
   >    ```
   >    git clone --recurse-submodules git@github.com:YOUR_GITHUB_USERNAME/se-toolkit-lab-8.git
   >    ```
   >
   >    Or, if you already cloned via HTTPS, switch the remote:
   >
   >    ```
   >    git remote set-url origin git@github.com:YOUR_GITHUB_USERNAME/se-toolkit-lab-8.git
   >    ```
   >
   > **Option B — Personal access token** (quick, less secure):
   > 1. In your browser, go to <https://github.com/settings/tokens> → **Generate new token (classic)** → select **`repo`** scope → **Generate token**.
   > 2. Copy the token. On the VM, run:
   >
   >    ```
   >    git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_GITHUB_USERNAME/se-toolkit-lab-8.git
   >    ```
   >
   > **Verify** — after either option, run: `git push origin main`. It should succeed with no password prompt.

3. Go into the repository and install `Python` dependencies:

   ```terminal
   cd se-toolkit-lab-8
   uv sync --dev
   ```

   You will add `nanobot-ai` later in Task 1 inside a repo-local `nanobot/` project.

4. Create the environment file:

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

5. Configure the autochecker API credentials.

   The ETL pipeline fetches data from the autochecker dashboard API.
   Open `.env.docker.secret` and set:

   ```text
   AUTOCHECKER_API_LOGIN=YOUR_EMAIL@innopolis.university
   AUTOCHECKER_API_PASSWORD=YOUR_GITHUB_USERNAMEYOUR_TELEGRAM_ALIAS
   ```

   Replace **`YOUR_EMAIL`**, **`YOUR_GITHUB_USERNAME`**, and **`YOUR_TELEGRAM_ALIAS`** with your actual values. Example: if your GitHub username is `johndoe` and your Telegram alias is `jdoe`, the password is `johndoejdoe`.

   > [!IMPORTANT]
   > The credentials must match your autochecker bot registration.
   >
   > If you haven't registered in the autochecker bot yet, do it now at <https://t.me/auchebot>.
   > If you need to change existing data, ask your TA or try `/reset` in the bot.

6. Set `LMS_API_KEY` — this is the **backend API key** that protects your LMS endpoints (used for `Authorization: Bearer` in Swagger and the React dashboard). It is **not** the Nanobot login password and it is **not** the LLM key.

   ```text
   LMS_API_KEY=set-it-to-something-and-remember-it
   ```

7. Set `QWEN_CODE_API_KEY` — the Qwen Code API is included as a Docker Compose service. You just need to set your API key:

   ```text
   QWEN_CODE_API_KEY=your-qwen-api-key
   ```

   If you don't have a Qwen API key yet, see [step 1.9](#19-set-up-llm-access-qwen-code-api).

8. Set `NANOBOT_ACCESS_KEY` — this is the password that will protect the Nanobot web client in Task 2. There is **no default**. Choose your own value and remember it.

   ```text
   NANOBOT_ACCESS_KEY=set-your-own-private-password
   ```

### 1.3. Stop Lab 7 services on your VM to free the ports

> [!IMPORTANT]
> Labs 7 and 8 use the same ports (42001–42005). You **must** stop Lab 7 containers before starting Lab 8.

```terminal
cd ~/se-toolkit-lab-7
docker compose --env-file .env.docker.secret down
```

> [!NOTE]
> You must use `--env-file .env.docker.secret` — without it, `docker compose down` will fail because the compose file references required variables.

### 1.4. Start the services on your VM

1. Start the services in the background:

   ```terminal
   docker compose --env-file .env.docker.secret up --build -d
   ```

2. Check that the containers are running:

   ```terminal
   docker compose --env-file .env.docker.secret ps --format "table {{.Service}}\t{{.Status}}"
   ```

   You should see the foundation services listed below:

   ```terminal
   SERVICE           STATUS
   backend           Up 50 seconds
   caddy             Up 49 seconds
   client-web-react  Up 49 seconds (exited)
   otel-collector    Up 50 seconds
   pgadmin           Up 50 seconds
   postgres          Up 55 seconds (healthy)
   qwen-code-api     Up 50 seconds (healthy)
   victorialogs      Up 50 seconds
   victoriatraces    Up 50 seconds
   ```

   > [!NOTE]
   > `client-web-react` exits after copying its build output — that's normal. Caddy serves the static files.
   >
   > The observability services (VictoriaLogs, VictoriaTraces, OTel Collector) are part of the base system. You'll use them in Task 3.

   > [!TIP]
   > If you use `VS Code` Remote-SSH, forward port `42002` so `http://localhost:42002` opens in your local browser while the services keep running on the VM.

> <h3>Troubleshooting</h3>
>
> **Port conflict (`port is already allocated`).**
>
> First, check what's using the port:
>
> ```terminal
> docker ps
> ```
>
> This shows all running containers and their ports. Look for containers using ports 42001–42005 — they're likely leftover from a previous lab. Stop them:
>
> ```terminal
> docker stop <container-name>
> ```
>
> If that doesn't help, make sure you stopped Lab 7 services (step 1.3), or [clean up `Docker`](../../wiki/docker.md#clean-up-docker) and try again.
>
> **Containers exit immediately.**
>
> Rebuild all containers from scratch:
>
> ```terminal
> docker compose --env-file .env.docker.secret down -v
> docker compose --env-file .env.docker.secret up --build -d
> ```
>
> **DNS resolution errors (`getaddrinfo EAI_AGAIN`).**
>
> If you see DNS errors like `getaddrinfo EAI_AGAIN registry.npmjs.org`, `Docker` can't resolve domain names. This is a university network DNS issue. Add Google DNS to `Docker`:
>
> ```terminal
> echo '{"dns": ["8.8.8.8", "8.8.4.4", "1.1.1.1"]}' \
>   | jq \
>   | sudo tee /etc/docker/daemon.json
>
> sudo systemctl restart docker
> ```
>
> Then run the `docker compose up` command again.
>
> **Docker Hub rate limits (`Too many requests`).**
>
> If you're building outside the university network and hit Docker Hub rate limits, set the registry prefix to empty in `.env.docker.secret`:
>
> ```text
> REGISTRY_PREFIX_DOCKER_HUB=
> ```
>
> This is only needed outside the university. On campus, the default harbor cache avoids rate limits.

### 1.5. Populate the database

The database starts empty. You need to run the ETL pipeline to populate it with data from the autochecker API.

1. Open `http://<your-vm-ip-address>:42002/docs` in your browser (or `localhost:42002` if you forwarded the port via VS Code).

   You should see the Swagger UI page.

2. [Authorize in Swagger](../../wiki/swagger.md#authorize-in-swagger-ui) with the `LMS_API_KEY` you set in `.env.docker.secret`.

3. Run the ETL sync by calling `POST /pipeline/sync` in Swagger UI.

   You should get a response showing the number of items and logs loaded:

   ```json
   {
     "new_records": 120,
     "total_records": 9502
   }
   ```

   > [!NOTE]
   > The exact numbers depend on how much data the autochecker API has.
   > As long as both numbers are greater than 0, the sync worked.

4. Verify data by calling `GET /items/`.

   You should get a non-empty array of items.

> [!IMPORTANT]
> Without this step, all analytics endpoints return empty results and the agent will have no data to work with.

### 1.6. Verify the deployment on your VM

1. Open `http://<your-vm-ip-address>:42002/docs` in your browser.

   You should see the Swagger UI with all endpoints.

2. Open `http://<your-vm-ip-address>:42002/` in your browser.

   You should see the React dashboard. Enter your `LMS_API_KEY` to connect.

3. Switch to the **Dashboard** tab.

   You should see charts with analytics data (submissions timeline, score distribution, group performance, task pass rates).

4. Verify the Qwen Code API is working:

   ```terminal
   curl -s http://localhost:42005/v1/models -H "Authorization: Bearer YOUR_QWEN_CODE_API_KEY" | head -c 100
   ```

   You should see a JSON response with model information.

   > [!TIP]
   > If you get `Internal Server Error`, your Qwen token may have expired.
   > Check: `curl -s -H "X-API-Key: YOUR_KEY" http://localhost:42005/health` — if `default_account.status` is `"expired"`, you need to refresh.
   > See [Qwen Code credentials file](../../wiki/qwen-code.md#qwen-code-credentials-file) for how to re-copy the credentials from your local machine to the VM.

> [!IMPORTANT]
> If the dashboard shows no data or errors, make sure:
>
> - The ETL sync completed successfully (step 1.5)
> - You entered the correct `LMS_API_KEY` in the React dashboard
> - Try selecting a different lab in the dropdown

### 1.7. Keep the deployment on your VM

Keep the services running on your VM after setup. The autochecker will query that deployment during evaluation.

If you rebuild the stack later, use the same `.env.docker.secret` values, including your `NANOBOT_ACCESS_KEY`.

### 1.8. Set up SSH for the autochecker

The autochecker needs to SSH into your VM as **your main user** to run checks.

> [!NOTE]
> If you completed Lab 6 Task 3, this is already done. Verify by checking with the autochecker bot — if the setup check passes, skip this step.

1. On your VM, add the autochecker's SSH public key:

   ```terminal
   mkdir -p ~/.ssh
   echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker' >> ~/.ssh/authorized_keys
   chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
   ```

2. Register your VM username with the autochecker bot if you haven't already.

   In the Telegram bot, when prompted for your VM username, run `whoami` on your VM and reply with the output.

### 1.9. Set up LLM access (Qwen Code API)

The Qwen Code API is included as a Docker Compose service in this lab. You just need an API key.

[Qwen Code](../../wiki/qwen-code.md#what-is-qwen-code) provides **1000 free requests per day** and works from Russia — no VPN or credit card needed.

> [!NOTE]
> If you already have a Qwen Code API key from a previous lab, use the same one. Set it as `QWEN_CODE_API_KEY` in `.env.docker.secret` (step 1.2).

If you need a new key, follow the [Qwen Code API setup guide](../../wiki/qwen-code-api.md#qwen-code-api-key).

Verify the API works:

```terminal
curl -s http://localhost:42005/v1/models -H "Authorization: Bearer YOUR_QWEN_CODE_API_KEY" | head -c 100
```

You should see a JSON response with model information.

<details><summary><b>Alternative: OpenRouter (click to open)</b></summary>

If you prefer [OpenRouter](https://openrouter.ai), register and get an API key. Then in `.env.docker.secret`:

```text
LLM_API_KEY=your-openrouter-key
LLM_API_BASE_URL=https://openrouter.ai/api/v1
LLM_API_MODEL=meta-llama/llama-3.3-70b-instruct:free
```

</details>

### 1.10. Coding agent

> [!NOTE]
> You should already have a coding agent from previous labs.
> If not, [set one up](../../wiki/coding-agents.md#choose-and-use-a-coding-agent).

> [!TIP]
> When stuck, ask your coding agent first, then ask the TA.

In this lab, you will use the coding agent (Qwen Code) to help implement tasks. The agent is your development partner — but **make sure you understand what it builds**. Each task has checkpoints where you must verify the results manually.

----

You're all set. Now go to the [tasks](../../README.md#tasks).
