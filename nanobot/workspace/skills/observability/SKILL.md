---
name: observability
description: Use observability MCP tools for logs and traces
always: true
---

# Observability Skill

When the user asks about errors, logs, or tracing information, use the observability MCP tools to investigate and provide concise summaries.

## When to use this skill

- User asks "any errors in the last hour?" or similar
- User asks "what went wrong?" after a failure
- User asks about logs, traces, or debugging information
- User asks about health status or debugging
- User asks "check system health"

## Available Tools

You have access to the following observability MCP tools:

- `mcp_mcp-obs_mcp_obs_logs_search` - Search logs in VictoriaLogs by keyword and/or time range. Useful fields: service.name, severity, event, trace_id.
- `mcp_mcp-obs_mcp_obs_logs_error_count` - Count error-level log entries per service over a time window.
- `mcp_mcp-obs_mcp_obs_traces_list` - List recent traces for a service from VictoriaTraces.
- `mcp_mcp-obs_mcp_obs_traces_get` - Fetch a specific trace by its trace ID from VictoriaTraces.

## Investigation workflow for "What went wrong?"

When the user asks "What went wrong?" or "Check system health", perform a complete investigation:

1. **Check for errors** — Use `mcp_mcp-obs_mcp_obs_logs_error_count` to quickly see if there are recent errors. Use a short time window (e.g., "10m" or "5m") and service name "Learning Management Service".

2. **Search logs** — If errors exist, use `mcp_mcp-obs_mcp_obs_logs_search` to inspect the relevant log entries with query like `_time:10m service.name:"Learning Management Service" severity:ERROR`. Look for:
   - `trace_id` field — useful for fetching the full trace
   - `error` field — the actual error message
   - `event` — what operation was happening (e.g., "db_query")

3. **Fetch trace** — If you find a `trace_id` in the logs, use `mcp_mcp-obs_mcp_obs_traces_get` to get the full trace and understand the request flow.

4. **Summarize** — Present a concise summary that explicitly mentions both log evidence AND trace evidence:
   - What happened (error type/message)
   - Where it occurred (service, operation)
   - Relevant trace ID if available
   - Don't dump raw JSON — extract the key information

## Example queries

- "Any LMS backend errors in the last 10 minutes?" → Use `mcp_mcp-obs_mcp_obs_logs_error_count` with service="Learning Management Service" and time_window="10m"
- "What went wrong?" → Run full investigation: logs_error_count → logs_search → traces_get → concise summary with both log and trace evidence
- "Check system health" → Run full investigation

## Important notes

- Always scope queries to a reasonable time window (10m, 5m) to avoid overwhelming results
- Include the service name when possible to filter out unrelated errors
- Extract and present the error message and key context, not raw JSON
- If no errors found, say so clearly
- For "What went wrong?" always chain the tools: error count → search → get trace → summarize