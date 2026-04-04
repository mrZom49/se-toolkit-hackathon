"""Query the Qwen Code API (OpenAI-compatible endpoint).

Usage:
    python scripts/query-qwen-code-api.py [OPTIONS] PROMPT

Options:
    --base-url URL   API base URL   (default: $LLM_API_BASE_URL or http://localhost:42005/v1)
    --port PORT      Shorthand for http://localhost:<PORT>/v1 (overrides --base-url)
    --api-key KEY    API key        (default: $LLM_API_KEY)
    --model MODEL    Model name     (default: $LLM_API_MODEL or "coder-model")

Environment variables:
    LLM_API_BASE_URL   Default base URL
    LLM_API_KEY        Default API key
    LLM_API_MODEL      Default model name
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the Qwen Code API")
    parser.add_argument(
        "--base-url",
        default=os.environ.get("LLM_API_BASE_URL", "http://localhost:42005/v1"),
        help="API base URL (default: $LLM_API_BASE_URL or http://localhost:42005/v1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        help="Shorthand for http://localhost:<PORT>/v1 (overrides --base-url)",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("LLM_API_KEY", ""),
        help="API key (default: $LLM_API_KEY)",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("LLM_API_MODEL", "coder-model"),
        help="Model name (default: $LLM_API_MODEL or coder-model)",
    )
    parser.add_argument("prompt", nargs="+", help="The prompt to send")
    args = parser.parse_args()

    base_url: str = args.base_url
    if args.port is not None:
        base_url = f"http://localhost:{args.port}/v1"
    if not base_url.startswith(("http://", "https://")):
        base_url = f"http://{base_url}"
    if not base_url.endswith("/v1"):
        base_url = f"{base_url}/v1"

    api_key: str = args.api_key
    if not api_key:
        print("Error: API key is required (--api-key or LLM_API_KEY)", file=sys.stderr)
        sys.exit(1)

    prompt = " ".join(args.prompt)
    url = f"{base_url.rstrip('/')}/chat/completions"

    payload = json.dumps(
        {
            "model": args.model,
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
            print(json.dumps(data, indent=2))
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
