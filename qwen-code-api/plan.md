# Implementation Plan: High-Priority Parity Features

## Goal
Bring Python implementation to feature parity with Node.js version for high-priority features.

---

## High-Priority Features

### 1. Token Counting
**Status**: Pending

**Implementation**:
- Add `tiktoken` dependency to `pyproject.toml`
- Create `app/utils/token_counter.py`
  - `count_tokens(input)` function using `cl100k_base` encoding
  - Handle string, array, and object inputs
  - Fallback to character-based estimation on error

**Usage**: Count tokens in incoming requests for logging

---

### 2. Request/Response Logging (liveLogger)
**Status**: Pending

**Implementation**:
- Create `app/utils/live_logger.py`
  - Colored console output using ANSI codes
  - Account-specific colors (for future multi-account support)
  - Methods:
    - `proxy_request()` - Log incoming requests with model, tokens, streaming status
    - `proxy_response()` - Log responses with status, latency, token usage
    - `proxy_error()` - Log errors with status and message
    - `server_started()` - Startup message
    - `shutdown()` - Shutdown message

**Format** (matching Node.js):
```
→ [account] req_id | model {streaming} | N tokens
← [account] req_id 200 | 150ms | 100+50 tok | qwen: abc123
✗ [account] 500 | Error message
```

---

### 3. System Prompt Injection
**Status**: Pending

**Implementation**:
- Create `app/utils/system_prompt_transformer.py`
  - Read `sys-prompt.txt` from project root on startup
  - `SystemPromptTransformer` class:
    - `should_apply_to_model(model)` - Check model filter
    - `add_cache_control(message)` - Add Anthropic-style cache markers
    - `transform(messages, model)` - Inject system prompt
  - Support prepend/append mode via config
  - Support model filtering

**Config Options** (add to `config.py`):
- `SYSTEM_PROMPT_ENABLED` (default: `true`)
- `SYSTEM_PROMPT_FILE` (optional, default: `sys-prompt.txt`)
- `SYSTEM_PROMPT_MODE` (`prepend` or `append`, default: `prepend`)
- `SYSTEM_PROMPT_MODELS` (comma-separated, default: all models)

---

## Configuration Changes

### Add to `config.py`:
```python
# Token counting
USE_TOKEN_COUNTING = os.getenv("USE_TOKEN_COUNTING", "true").lower() != "false"

# System prompt
SYSTEM_PROMPT_ENABLED = os.getenv("SYSTEM_PROMPT_ENABLED", "true").lower() != "false"
SYSTEM_PROMPT_FILE = os.getenv("SYSTEM_PROMPT_FILE")
SYSTEM_PROMPT_MODE = os.getenv("SYSTEM_PROMPT_MODE", "prepend")
SYSTEM_PROMPT_MODELS = os.getenv("SYSTEM_PROMPT_MODELS")

# Logging
LOG_REQUESTS = os.getenv("LOG_REQUESTS", "true").lower() != "false"
```

### Add to `.env.example`:
```bash
# System Prompt Configuration
SYSTEM_PROMPT_ENABLED=true
SYSTEM_PROMPT_FILE=sys-prompt.txt
SYSTEM_PROMPT_MODE=prepend
SYSTEM_PROMPT_MODELS=coder-model,qwen3-coder-plus

# Logging
LOG_REQUESTS=true
USE_TOKEN_COUNTING=true
```

---

## File Changes

### New Files:
1. `app/utils/__init__.py` - Empty package initializer
2. `app/utils/token_counter.py` - Token counting utility
3. `app/utils/live_logger.py` - Colored console logging
4. `app/utils/system_prompt_transformer.py` - System prompt injection
5. `sys-prompt.txt` - Default system prompt (can be empty placeholder)

### Modified Files:
1. `pyproject.toml` - Add `tiktoken` dependency
2. `app/config.py` - Add new config options
3. `app/main.py` - Initialize logger in lifespan
4. `app/routes/chat.py` - Integrate all three features
5. `.env.example` - Document new config options

---

## Integration in chat.py

### Request Flow:
```python
@router.post("/v1/chat/completions")
async def chat_completions(request: Request, ...):
    # 1. Parse body
    body = await request.json()
    
    # 2. Count tokens
    token_count = count_tokens(body.get("messages", []))
    
    # 3. Log request
    live_logger.proxy_request(request_id, model, "default", token_count, is_streaming)
    
    # 4. Transform messages (system prompt)
    transformed_messages = system_prompt_transformer.transform(
        body.get("messages", []), model
    )
    
    # 5. Make API call with transformed messages
    ...
    
    # 6. Log response
    latency = time.time() - start_time
    live_logger.proxy_response(request_id, 200, "default", latency, input_tokens, output_tokens)
```

---

## Testing Checklist

- [ ] Token counting works for simple messages
- [ ] Token counting handles arrays of messages
- [ ] Token counting falls back gracefully on error
- [ ] Request logging shows correct format
- [ ] Response logging shows latency and tokens
- [ ] System prompt injected when enabled
- [ ] System prompt respects model filter
- [ ] System prompt respects prepend/append mode
- [ ] All features can be disabled via config
- [ ] No breaking changes to existing functionality

---

## Implementation Order

1. ✅ Add `tiktoken` to `pyproject.toml`
2. ✅ Create `token_counter.py`
3. ✅ Create `live_logger.py`
4. ✅ Create `system_prompt_transformer.py`
5. ✅ Update `config.py`
6. ✅ Update `chat.py` integration
7. ✅ Update `main.py` lifespan
8. ✅ Update `.env.example`
9. ✅ Run linting and type checking
10. ✅ Test all features

---

## Notes

- Keep features optional via environment variables
- Maintain backward compatibility
- Match Node.js output format where possible
- Use proper type annotations throughout
- Follow existing code style conventions
