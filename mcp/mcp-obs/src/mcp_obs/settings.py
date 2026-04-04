"""MCP server for observability — VictoriaLogs and VictoriaTraces."""

import logging
import os

from pydantic import Field
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    victorialogs_url: str = Field(
        default=os.environ.get("NANOBOT_VICTORIALOGS_URL", "http://victorialogs:9428"),
        alias="NANOBOT_VICTORIALOGS_URL",
    )
    victoriatraces_url: str = Field(
        default=os.environ.get(
            "NANOBOT_VICTORIATRACES_URL", "http://victoriatraces:10428"
        ),
        alias="NANOBOT_VICTORIATRACES_URL",
    )


settings = Settings.model_validate({})
