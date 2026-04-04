"""MCP Observability server entry point."""

from mcp_obs.server import main

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
