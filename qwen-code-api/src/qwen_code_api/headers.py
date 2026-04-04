"""DashScope request headers that mimic the Qwen Code client."""


def build_headers(access_token: str, *, streaming: bool = False) -> dict[str, str]:
    return {
        "connection": "keep-alive",
        "accept": "text/event-stream" if streaming else "application/json",
        "authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "user-agent": "QwenCode/0.12.2 (linux; x64)",
        "x-dashscope-authtype": "qwen-oauth",
        "x-dashscope-cachecontrol": "enable",
        "x-dashscope-useragent": "QwenCode/0.12.2 (linux; x64)",
        "x-stainless-arch": "x64",
        "x-stainless-lang": "js",
        "x-stainless-os": "Linux",
        "x-stainless-package-version": "5.11.0",
        "x-stainless-retry-count": "1",
        "x-stainless-runtime": "node",
        "x-stainless-runtime-version": "v18.19.1",
        "accept-language": "*",
        "sec-fetch-mode": "cors",
    }
