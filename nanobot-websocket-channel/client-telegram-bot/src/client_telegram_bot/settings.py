"""Configuration for the bot."""

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str = Field(..., alias="BOT_TOKEN")
    nanobot_ws_url: str = Field(..., alias="NANOBOT_WS_URL")
    nanobot_access_key: str = Field(..., alias="NANOBOT_ACCESS_KEY")


settings = Settings.model_validate({})
