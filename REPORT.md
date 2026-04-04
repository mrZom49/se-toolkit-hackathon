# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Checkpoint 1 - "What is the agentic loop?":**
> The agentic loop is the fundamental cycle that an AI agent follows to accomplish tasks autonomously. It's the core reasoning and action pattern that distinguishes an agent from a simple chatbot.
> 
> 1. **Perceive** — Gather information about the current state
> 2. **Reason** — Analyze the situation and plan next steps
> 3. **Act** — Execute the chosen action
> 4. **Observe** — Receive feedback from the action
> 5. **Repeat** — Continue until the task is complete

**Checkpoint 2 - "What labs are available in our LMS?":**
> The agent searched the repository and database directly. Labs found:
> - Lab 01 – Products, Architecture & Roles
> - Lab 02 — Run, Fix, and Deploy a Backend Service
> - Lab 03 — Backend API: Explore, Debug, Implement, Deploy
> - Lab 04 — Testing, Front-end, and AI Agents
> - Lab 05 — Data Pipeline and Analytics Dashboard
> - Lab 06 — Build Your Own Agent
> - Lab 07 — Build a Client with an AI Coding Agent
> - lab-08

## Task 1B — Agent with LMS tools

**Checkpoint 1 - "What labs are available?":**
> Here are the available labs:
> 1. **Lab 01** – Products, Architecture & Roles
> 2. **Lab 02** — Run, Fix, and Deploy a Backend Service
> 3. **Lab 03** — Backend API: Explore, Debug, Implement, Deploy
> 4. **Lab 04** — Testing, Front-end, and AI Agents
> 5. **Lab 05** — Data Pipeline and Analytics Dashboard
> 6. **Lab 06** — Build Your Own Agent
> 7. **Lab 07** — Build a Client with an AI Coding Agent
> 8. **Lab 08** — lab-08

**Checkpoint 2 - "Is the LMS backend healthy?":**
> Yes, the LMS backend is healthy! It's currently tracking 56 items.

## Task 1C — Skill prompt

**Checkpoint - "Show me the scores":**
> I'll help you check the scores. First, let me see which labs are available in the LMS.
> 
> There are 8 labs available. Which lab would you like to see the scores for?
> 
> 1. Lab 01 – Products, Architecture & Roles
> 2. Lab 02 — Run, Fix, and Deploy a Backend Service
> 3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
> 4. Lab 04 — Testing, Front-end, and AI Agents
> 5. Lab 05 — Data Pipeline and Analytics Dashboard
> 6. Lab 06 — Build Your Own Agent
> 7. Lab 07 — Build a Client with an AI Coding Agent
> 8. lab-08
> 
> Please let me know which lab you're interested in, or I can show you scores for all of them.

## Task 2A — Deployed agent

**Nanobot startup log excerpt:**

```
nanobot-1  | Using config: /app/nanobot/config.resolved.json
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
nanobot-1  | 2026-04-02 13:27:31.693 | INFO     | nanobot.channels.manager:_init_channels:58 - WebChat channel enabled
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | ✓ Heartbeat: every 1800s
nanobot-1  | 2026-04-02 13:27:34.607 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'webchat': connected, 1 tools registered
nanobot-1  | 2026-04-02 13:27:34.607 | INFO     | nanobot.agent.loop:run:280 - Agent loop started
```

**Service status:**

```
NAME                                STATUS
se-toolkit-lab-8-nanobot-1          Up 19 minutes
```

The nanobot gateway is running as a Docker Compose service with:
- WebChat channel enabled on port 8765
- MCP server 'webchat' connected (provides `mcp_webchat_ui_message` tool)
- Agent loop started and processing messages

---

## Task 2B — Web client

**WebSocket endpoint test:**

The WebSocket endpoint at `ws://localhost:42002/ws/chat?access_key=1234` is accessible through Caddy's reverse proxy.

**Flutter web client:**

- Accessible at `http://<vm-ip>:42002/flutter`
- Protected by `NANOBOT_ACCESS_KEY` authentication
- Build output mounted in Caddy at `/srv/flutter`

**Recent agent activity (from logs):**

```
nanobot-1  | 2026-04-02 14:05:09.851 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: exec({"command": "ps aux | grep -i mcp | head -10"})
nanobot-1  | 2026-04-02 14:05:32.799 | INFO     | nanobot.agent.subagent:_run_subagent:91 - Subagent [4bb4e8d8] starting task: Get LMS labs list
nanobot-1  | 2026-04-02 14:05:39.219 | INFO     | nanobot.agent.loop:_process_message:479 - Response to webchat:ff4ea0e2-214f-4640-ac73-de7f22333368: I've started a background task to query the LMS backend for available labs...
```

**Architecture implemented:**

```
browser -> caddy (port 42002) -> nanobot webchat channel (port 8765) -> nanobot gateway (port 18790) -> mcp_lms -> backend
nanobot gateway -> qwen-code-api -> Qwen
nanobot gateway -> mcp_webchat -> nanobot webchat UI relay -> browser
```

**Files modified:**

| File | Purpose |
|------|---------|
| `nanobot/entrypoint.py` | Resolves env vars into config, launches `nanobot gateway` |
| `nanobot/Dockerfile` | Multi-stage uv build, runs as non-root user |
| `nanobot/config.json` | Configures webchat channel and MCP servers |
| `docker-compose.yml` | nanobot, client-web-flutter, caddy services |
| `caddy/Caddyfile` | `/ws/chat` reverse proxy, `/flutter` static files |
| `nanobot-websocket-channel/` | Git submodule with webchat channel, mcp-webchat, Flutter client |

## Task 3A — Structured logging

**Happy-path log excerpt (request_started → request_completed with status 200):**
```
2026-04-02 15:58:35,504 INFO [lms_backend.main] [main.py:62] [trace_id=f75835f24b92615c805f1cfd5b730d22 span_id=d2dbe9dfeda8c95c resource.service.name=Learning Management Service trace_sampled=True] - request_started
2026-04-02 15:58:35,506 INFO [lms_backend.auth] [auth.py:30] [trace_id=f75835f24b92615c805f1cfd5b730d22 span_id=d2dbe9dfeda8c95c resource.service.name=Learning Management Service trace_sampled=True] - auth_success
2026-04-02 15:58:35,507 INFO [lms_backend.db.items] [items.py:16] [trace_id=f75835f24b92615c805f1cfd5b730d22 span_id=d2dbe9dfeda8c95c resource.service.name=Learning Management Service trace_sampled=True] - db_query
2026-04-02 15:58:35,705 INFO [lms_backend.main] [main.py:74] [trace_id=f75835f24b92615c805f1cfd5b730d22 span_id=d2dbe9dfeda8c95c resource.service.name=Learning Management Service trace_sampled=True] - request_completed
```

**Error-path log excerpt (db_query with error):**
```
2026-04-02 15:58:10,785 INFO [lms_backend.main] [main.py:62] [trace_id=36dcee934fd5269b17136bbb9c8a2811 span_id=7c84490a3ae6df18 resource.service.name=Learning Management Service trace_sampled=True] - request_started
2026-04-02 15:58:10,787 INFO [lms_backend.auth] [auth.py:30] [trace_id=36dcee934fd5269b17136bbb9c8a2811 span_id=7c84490a3ae6df18 resource.service.name=Learning Management Service trace_sampled=True] - auth_success
2026-04-02 15:58:10,787 INFO [lms_backend.db.items] [items.py:16] [trace_id=36dcee934fd5269b17136bbb9c8a2811 span_id=7c84490a3ae6df18 resource.service.name=Learning Management Service trace_sampled=True] - db_query
2026-04-02 15:58:10,823 ERROR [lms_backend.db.items] [items.py:23] [trace_id=36dcee934fd5269b17136bbb9c8a2811 span_id=7c84490a3ae6df18 resource.service.name=Learning Management Service trace_sampled=True] - db_query
2026-04-02 15:58:10,825 INFO [lms_backend.main] [main.py:74] [trace_id=36dcee934fd5269b17136bbb9c8a2811 span_id=7c84490a3ae6df18 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
```

**VictoriaLogs UI query result:**
- Query: `_time:10m service.name:"Learning Management Service" severity:ERROR`
- Error details from VictoriaLogs:
  - `error`: "(sqlalchemy.dialects.postgresql.asyncpg.InterfaceError) <class 'asyncpg.exceptions._base.InterfaceError'>: connection is closed"
  - `trace_id`: 36dcee934fd5269b17136bbb9c8a2811
  - `event`: db_query
  - `severity`: ERROR

![VictoriaLogs query screenshot](docs/task-3-victorialogs.png)

## Task 3B — Traces

**Healthy trace (Trace ID: f75835f24b92615c805f1cfd5b730d22):**
- 8 spans showing:
  - connect (duration: 174074μs)
  - SELECT db-lab-8 (duration: 16531μs)
  - GET /items/ http send (multiple spans for response handling)
- All spans completed successfully with status 200

**Error trace (Trace ID: 36dcee934fd5269b17136bbb9c8a2811):**
- Spans show the database error:
  - SELECT db-lab-8 span has `error: true` tag
  - `otel_status_description`: "connection is closed"
  - HTTP response shows status 404 (Items not found)
- The failure occurs in the db_query span (SQLAlchemy asyncpg)

![Healthy trace screenshot](docs/task-3-trace-healthy.png)
![Error trace screenshot](docs/task-3-trace-error.png)

## Task 3C — Observability MCP tools

**Normal condition (no errors):**
> Good news! There are **no errors** in the LMS backend (Learning Management Service) in the last 10 minutes. The system appears to be running smoothly.

**Failure condition (PostgreSQL down):**
> Yes, there are **3 errors** in the LMS backend in the last 10 minutes. All are database connectivity issues:
> 
> **Error Type**: `asyncpg.exceptions._base.InterfaceError` - connection is closed
> 
> This indicates the database became unavailable during the request, causing the backend to fail when trying to query items. The LMS was unable to connect to PostgreSQL, resulting in failed requests with 404 "Items not found" responses.

## Task 4A — Multi-step investigation

**Agent response to "What went wrong?" (triggered after asking "What labs are available?" with PostgreSQL down):**

> The LMS backend is currently **unhealthy** and unable to serve lab data.
>
> **Issue:** Database connection failure
> - Error: `[Errno -2] Name or service not known` - the backend cannot reach the PostgreSQL database
> - Service: Learning Management Service
> - Trace ID: 3250d9275fee7a22ecb0eb8e924de086
>
> The logs show a db_query error where the backend tried to connect to the database but failed. The traces confirm this is a connection failure to the database service.

**Investigation flow observed in nanobot logs:**
1. `mcp_lms_lms_labs({})` - tried to get labs
2. `mcp_lms_lms_health({})` - checked health
3. `mcp_mcp-obs_mcp_obs_logs_error_count(...)` - found errors
4. `mcp_mcp-obs_mcp_obs_logs_search(...)` - searched logs
5. `mcp_mcp-obs_mcp_obs_traces_get(...)` - fetched trace

**Key discrepancy noticed:** The backend returns `404 Items not found` even though the real issue is a database connection failure (PostgreSQL is down).

## Task 4B — Proactive health check

**Health check job created:**
- Job ID: 4818e617
- Interval: Every 2 minutes (120 seconds)
- Command: "Check for backend errors in the last 2 minutes using observability tools, inspect traces if errors found, and post a summary"

**Initial health check response (first run):**
```
mcp_mcp-obs_mcp_obs_logs_error_count({"service": "Learning Management Service", "time_window": "2m"})
-> Found 5 errors

mcp_mcp-obs_mcp_obs_logs_search(...)
-> Retrieved error details with trace_id

mcp_mcp-obs_mcp_obs_traces_get({"trace_id": "a8d8472a4422adb47f0805eb80f8027a"})
-> Fetched trace for investigation
```

**Proactive report from scheduled cron (second cycle at 16:39 UTC):**
The cron job executed and found:
- "Errors (last 2 min): 1" (fresh error from our latest test)
- Used logs_error_count → logs_search → traces_get chain
- Attempted to post via mcp_webchat_ui_message

Note: The WebChat channel shows "no connection for chat_id" warnings because the test was run from Python script rather than the Flutter UI. In a real Flutter chat session, the proactive report would appear directly in the chat.

**Screenshot/transcript:**
```
## 🐾 LMS Health Check Report
**Status:** ⚠️ Error detected in last 2 minutes
### Error Summary
- Count: 1 error
- Details: Database connection issue
- Service: Learning Management Service
- Trace ID: 29950a56048aa07b68a6646a11aea591
```

## Task 4C — Bug fix and recovery

### 1. Root cause - What was the planted bug?

**Location:** `backend/src/lms_backend/routers/items.py` lines 17-30

The bug was in the `get_items` exception handler. When the database query failed (e.g., PostgreSQL down), the code was catching ALL exceptions and returning a misleading `404 Items not found` response:

```python
# BEFORE (buggy):
except Exception as exc:
    logger.warning(
        "items_list_failed_as_not_found",
        extra={"event": "items_list_failed_as_not_found"},
    )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Items not found",  # <-- WRONG! This hides the real error
    ) from exc
```

This made it appear as if there were no items in the database, when in reality the database was unreachable.

### 2. Fix - What was changed?

```python
# AFTER (fixed):
except Exception as exc:
    logger.warning(
        "items_list_failed",
        extra={"event": "items_list_failed", "error": str(exc)},
    )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Backend error: {exc}",  # <-- Reports the real error
    ) from exc
```

Changes:
- Changed HTTP status from `404` to `500 Internal Server Error`
- Changed detail message from `"Items not found"` to the actual error message
- Added the error string to the logger for better observability

### 3. Post-fix failure check - "What went wrong?" after redeploy

With PostgreSQL still down, the agent now correctly reports:
- **Before fix:** "404 Items not found" (misleading)
- **After fix:** "503 Backend error: [Errno -2] Name or service not known" (accurate)

```
HTTP Status: 503
{"detail":"Backend error: [Errno -2] Name or service not known"}
```

The agent's observability investigation now shows the real underlying database connection failure instead of a fake "not found" error.

### 4. Healthy follow-up - System recovery

After restarting PostgreSQL:
```bash
curl -H "Authorization: Bearer 1234" http://127.0.0.1:42001/items/
# Returns: [] (normal empty response, no error)
```

The backend now correctly returns:
- HTTP 200 OK when database is accessible
- HTTP 503 with real error message when database is unavailable (PostgreSQL down)
