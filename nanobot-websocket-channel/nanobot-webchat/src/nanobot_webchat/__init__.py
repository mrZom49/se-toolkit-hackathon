"""WebChat channel plugin for nanobot — exposes a WebSocket server for web clients."""

from .channel import WebChatChannel, WebChatConfig

__all__ = ["WebChatChannel", "WebChatConfig"]
