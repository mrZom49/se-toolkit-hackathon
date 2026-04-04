import json
import os


def main() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as f:
        config = json.load(f)

    llm_api_key = os.environ.get("LLM_API_KEY")
    llm_api_base_url = os.environ.get("LLM_API_BASE_URL")
    llm_api_model = os.environ.get("LLM_API_MODEL")
    gateway_host = os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS")
    gateway_port = os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT")
    lms_backend_url = os.environ.get("NANOBOT_LMS_BACKEND_URL")
    lms_api_key = os.environ.get("NANOBOT_LMS_API_KEY")
    victorialogs_url = os.environ.get("NANOBOT_VICTORIALOGS_URL")
    victoriatraces_url = os.environ.get("NANOBOT_VICTORIATRACES_URL")
    webchat_host = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS")
    webchat_port = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT")
    access_key = os.environ.get("NANOBOT_ACCESS_KEY")

    if "providers" not in config:
        config["providers"] = {}
    if "custom" not in config["providers"]:
        config["providers"]["custom"] = {}
    if llm_api_key:
        config["providers"]["custom"]["apiKey"] = llm_api_key
    if llm_api_base_url:
        config["providers"]["custom"]["apiBase"] = llm_api_base_url

    if "agents" not in config:
        config["agents"] = {}
    if "defaults" not in config["agents"]:
        config["agents"]["defaults"] = {}
    if llm_api_model:
        config["agents"]["defaults"]["model"] = llm_api_model

    if "gateway" not in config:
        config["gateway"] = {}
    if gateway_host:
        config["gateway"]["host"] = gateway_host
    if gateway_port:
        config["gateway"]["port"] = int(gateway_port)

    if "tools" not in config:
        config["tools"] = {}
    if "mcpServers" not in config["tools"]:
        config["tools"]["mcpServers"] = {}

    if "lms" in config["tools"]["mcpServers"]:
        if "command" not in config["tools"]["mcpServers"]["lms"]:
            config["tools"]["mcpServers"]["lms"]["command"] = "/app/.venv/bin/python"
        else:
            config["tools"]["mcpServers"]["lms"]["command"] = "/app/.venv/bin/python"
        if "args" not in config["tools"]["mcpServers"]["lms"]:
            config["tools"]["mcpServers"]["lms"]["args"] = ["-m", "mcp_lms"]
        if "env" not in config["tools"]["mcpServers"]["lms"]:
            config["tools"]["mcpServers"]["lms"]["env"] = {}
        if lms_backend_url:
            config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_BACKEND_URL"] = (
                lms_backend_url
            )
        if lms_api_key:
            config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_API_KEY"] = (
                lms_api_key
            )
    else:
        config["tools"]["mcpServers"]["lms"] = {
            "command": "/app/.venv/bin/python",
            "args": ["-m", "mcp_lms"],
            "env": {
                "NANOBOT_LMS_BACKEND_URL": lms_backend_url or "",
                "NANOBOT_LMS_API_KEY": lms_api_key or "",
            },
        }

    if "mcp-obs" in config["tools"]["mcpServers"]:
        if "command" not in config["tools"]["mcpServers"]["mcp-obs"]:
            config["tools"]["mcpServers"]["mcp-obs"]["command"] = (
                "/app/.venv/bin/python"
            )
        if "args" not in config["tools"]["mcpServers"]["mcp-obs"]:
            config["tools"]["mcpServers"]["mcp-obs"]["args"] = ["-m", "mcp_obs"]
        if "env" not in config["tools"]["mcpServers"]["mcp-obs"]:
            config["tools"]["mcpServers"]["mcp-obs"]["env"] = {}
        if victorialogs_url:
            config["tools"]["mcpServers"]["mcp-obs"]["env"][
                "NANOBOT_VICTORIALOGS_URL"
            ] = victorialogs_url
        if victoriatraces_url:
            config["tools"]["mcpServers"]["mcp-obs"]["env"][
                "NANOBOT_VICTORIATRACES_URL"
            ] = victoriatraces_url
    else:
        config["tools"]["mcpServers"]["mcp-obs"] = {
            "command": "/app/.venv/bin/python",
            "args": ["-m", "mcp_obs"],
            "env": {
                "NANOBOT_VICTORIALOGS_URL": victorialogs_url or "",
                "NANOBOT_VICTORIATRACES_URL": victoriatraces_url or "",
            },
        }

    config["channels"] = {
        "webchat": {
            "enabled": True,
            "host": webchat_host or "0.0.0.0",
            "port": int(webchat_port) if webchat_port else 8765,
            "accessKey": access_key or "",
            "allowFrom": ["*"],
        }
    }

    config["tools"]["mcpServers"]["webchat"] = {
        "command": "/app/.venv/bin/python",
        "args": ["-m", "mcp_webchat"],
        "env": {
            "NANOBOT_WEBCHAT_UI_RELAY_URL": f"http://localhost:{webchat_port}"
            if webchat_port
            else "http://localhost:8765",
            "NANOBOT_WEBCHAT_UI_RELAY_TOKEN": access_key or "",
        },
    }

    resolved_path = os.path.join(os.path.dirname(__file__), "config.resolved.json")
    with open(resolved_path, "w") as f:
        json.dump(config, f, indent=2)

    workspace = (
        config.get("agents", {}).get("defaults", {}).get("workspace", "./workspace")
    )
    os.execvp(
        "nanobot",
        ["nanobot", "gateway", "--config", resolved_path, "--workspace", workspace],
    )


if __name__ == "__main__":
    main()
