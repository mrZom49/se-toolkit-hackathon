#!/usr/bin/env python3
"""Query LMS backend for available labs."""

import asyncio
from mcp_lms import LMSClient


async def main():
    async with LMSClient(base_url="http://backend:8000", api_key="1234") as client:
        labs = await client.get_labs()
        for lab in labs:
            print(f"{lab.id}: {lab.title}")


if __name__ == "__main__":
    asyncio.run(main())
