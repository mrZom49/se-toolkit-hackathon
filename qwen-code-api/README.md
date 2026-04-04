# Qwen Code API (Python) - OpenAI-Compatible Proxy Server

A Python proxy server that exposes Qwen models through an OpenAI-compatible API endpoint. Supports tool calling, streaming, and automatic token refresh.

This is a Python port of the original [qwen-code-api](https://github.com/aptdnfapt/qwen-code-api) (Node.js/TypeScript).

## Features

- **OpenAI-Compatible API** - Works with opencode, crush, claude code router, roo code, cline, and other OpenAI-compatible clients
- **Tool Calling Support** - Full support for function/tool calling
- **Streaming Responses** - Server-sent events (SSE) streaming support
- **Automatic Token Refresh** - OAuth token management with automatic refresh
- **Retry Logic** - Automatic retry on 500/429 errors with exponential backoff
- **API Key Authentication** - Secure your proxy with API keys
- **coder-model** - Qwen3.5-Plus (free via OAuth)

## Quick Start

### Option 1: Using Docker (Recommended)

1. **Authenticate**:

    You need to authenticate with Qwen to generate the required credentials file. Use the official `qwen-code` CLI:

    ```bash
    qwen login
    ```

    This creates the `~/.qwen/oauth_creds.json` file that will be mounted into the container.

2. **Configure Environment**:

    ```bash
    cp .env.example .env.secret
    # Edit .env.secret file with your desired configuration
    ```

3. **Build and Run with Docker Compose**:

    ```bash
    docker compose --env-file .env.secret up -d
    ```

4. **Use the Proxy**: Point your OpenAI-compatible client to `http://localhost:8080/v1`

### Option 2: Local Development

1. **Install Dependencies** (using uv):

    ```bash
    uv sync
    ```

2. **Authenticate**: You need to authenticate with Qwen to generate the required credentials file.

    ```bash
    qwen login
    ```

    This will create the `~/.qwen/oauth_creds.json` file needed by the proxy server.

3. **Start the Server**:

    ```bash
    uv run python -m qwen_code_api.main
    ```

    Or with uvicorn directly:

    ```bash
    uv run uvicorn qwen_code_api.main:app --host 0.0.0.0 --port 8080
    ```

4. **Use the Proxy**: Point your OpenAI-compatible client to `http://localhost:8080/v1`.

**Note**: API key can be any random string if not configured - it doesn't matter for this proxy.

## API Key Authentication

The proxy can be secured with API keys to prevent unauthorized access.

### Setting up API Keys

1. **Single API Key:**

   ```bash
   QWEN_CODE_API_KEY=your-secret-key-here
   ```

2. **Multiple API Keys:**

   ```bash
   QWEN_CODE_API_KEY=key1,key2,key3
   ```

If no API key is configured, the proxy will not require authentication.

## Configuration

The proxy server can be configured using environment variables. Create a `.env.secret` file in the project root (copy from `.env.example`).

| Variable             | Description                                              | Default            |
| -------------------- | -------------------------------------------------------- | ------------------ |
| `PORT`               | Server port                                              | `8080`             |
| `HOST`               | Server host                                              | `0.0.0.0`          |
| `LOG_LEVEL`          | Logging level (`error`, `debug`)                         | `error`            |
| `MAX_RETRIES`        | Maximum retry attempts for failed requests               | `5`                |
| `RETRY_DELAY_MS`     | Base retry delay in milliseconds                         | `1000`             |
| `QWEN_CODE_AUTH_USE` | Use OAuth authentication from `~/.qwen/oauth_creds.json` | `true`             |
| `QWEN_CODE_API_KEY`  | API key(s) for authentication (comma-separated)          | (none)             |
| `DEFAULT_MODEL`      | Default model to use when not specified                  | `coder-model`      |

## Example Usage

### Health Check

Monitor the proxy status:

```bash
curl http://localhost:8080/health
```

### Using Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="fake-key",
    base_url="http://localhost:8080/v1"
)

response = client.chat.completions.create(
    model="coder-model",
    messages=[
        {"role": "user", "content": "2+2=?"}
    ]
)

print(response.choices[0].message.content)
```

## Supported Models

The proxy supports Qwen models available through your Qwen Code OAuth account:

| Model ID      | Description                   | Max Tokens | Notes                             |
| ------------- | ----------------------------- | ---------- | --------------------------------- |
| `coder-model` | Qwen3.5-Plus (via OAuth free) | 65536      | **Only model available for free** |
  
**Note**: With free OAuth authentication, only `coder-model` is available. The proxy passes through whatever models your Qwen account has access to. Use `/model` in Qwen Code CLI to see available models for your account.

## Supported Endpoints

- `POST /v1/chat/completions` - Chat completions (streaming and non-streaming)
- `GET /v1/models` - List available models
- `GET /health` - Health check and status

## Development

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager

### Setup

```bash
# Install dependencies
uv sync

# Run type checking
uv run poe typecheck

# Run linting
uv run poe lint

# Run formatting
uv run poe format

# Run all checks
uv run poe check

# Run tests
uv run pytest
```

## Important Notes

- **Token Limits**: Users might face errors or 504 Gateway Timeout issues when using contexts with 130,000 to 150,000 tokens or more. This appears to be a practical limit for Qwen models.
- **Authentication**: The proxy uses OAuth credentials from `~/.qwen/oauth_creds.json`. Make sure to authenticate with the Qwen CLI before starting the proxy.
- **Token Refresh**: The proxy automatically refreshes OAuth tokens when they expire.

## Differences from Node.js Version

This Python implementation maintains feature parity with the original Node.js version while leveraging Python's async capabilities:

- Built with **FastAPI** and **uvicorn**
- Uses **httpx** for async HTTP requests
- OAuth token management with automatic refresh
- Same Docker deployment workflow
- Compatible with all the same AI agents and tools

## License

MIT
