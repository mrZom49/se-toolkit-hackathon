---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

## Available LMS Tools

You have access to the following LMS MCP tools:

- `lms_health` - Check if the LMS backend is healthy and report the item count.
- `lms_labs` - List all labs available in the LMS.
- `lms_learners` - List all learners registered in the LMS.
- `lms_pass_rates` - Get pass rates (avg score and attempt count per task) for a lab. **Requires `lab` parameter.**
- `lms_timeline` - Get submission timeline (date + submission count) for a lab. **Requires `lab` parameter.**
- `lms_groups` - Get group performance (avg score + student count per group) for a lab. **Requires `lab` parameter.**
- `lms_top_learners` - Get top learners by average score for a lab. **Requires `lab` and optional `limit` parameter.**
- `lms_completion_rate` - Get completion rate (passed / total) for a lab. **Requires `lab` parameter.**
- `lms_sync_pipeline` - Trigger the LMS sync pipeline. May take a moment.

## Strategy Rules

1. **Lab selection required**: When a user asks for scores, pass rates, completion, groups, timeline, or top learners without naming a specific lab, call `lms_labs` first to get available labs, then ask the user which lab they want.

2. **Multiple labs available**: If multiple labs are available, ask the user to choose one before proceeding with data queries.

3. **Lab labels**: Use each lab title/identifier as the default user-facing label. Let the shared `structured-ui` skill decide how to present lab choices on supported channels.

4. **Formatting**: Format numeric results nicely:
   - Percentages: "85%" not "0.85"
   - Counts: "42 students" not just "42"
   - Scores: "92.5/100" for clarity

5. **Conciseness**: Keep responses concise. Don't list every data point - summarize the key information.

6. **Self-description**: When asked "what can you do?", explain your current tools and limits clearly: you can check backend health, list labs, and query scores/pass rates/completion for any lab.

7. **Backend health**: The `lms_health` tool reports whether the LMS backend is accessible and includes item counts. Use this to verify connectivity when troubleshooting.

8. **Sync pipeline**: If data seems outdated or missing, suggest triggering `lms_sync_pipeline` to refresh the data.
