"""Structured message parsing for the WebChat channel.

LLM responses may contain structured JSON (choice, confirm, composite) that
clients render as interactive widgets.  This module validates untrusted LLM
output against Pydantic schemas and normalises it into typed models.
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from nanobot_channel_protocol.schemas import (
    CompositeMessage,
    OutboundPayload,
    StructuredMessage,
    TextPart,
)
from pydantic import TypeAdapter, ValidationError

_structured_adapter: TypeAdapter[StructuredMessage] = TypeAdapter(StructuredMessage)
logger = logging.getLogger(__name__)

_CODE_FENCE_RE = re.compile(r"^\s*```(?:json)?\s*\n(.*?)\n\s*```\s*$", re.DOTALL)


def _strip_code_fence(text: str) -> str:
    """Remove a markdown code fence wrapper if present."""
    m = _CODE_FENCE_RE.match(text)
    return m.group(1).strip() if m else text


def _parse_structured(data: Any) -> OutboundPayload | None:
    """Validate untrusted data against the structured message schema.

    This is the trust boundary: *data* comes from ``json.loads`` (``Any``)
    and a validated Pydantic model comes out.

    If validation fails but *data* looks like a malformed structured message
    (has a ``content`` string), returns a ``TextPart`` so the user sees the
    text instead of raw JSON.  Returns ``None`` only when there is nothing
    useful to extract.
    """
    try:
        return _structured_adapter.validate_python(data)
    except ValidationError:
        # The LLM tried to produce structured JSON but got the shape wrong.
        # Salvage the "content" field as plain text.
        try:
            content = data.get("content")
            if isinstance(content, str) and content:
                logger.warning(
                    "WebChat: invalid structured message (type=%s), "
                    "falling back to text",
                    data.get("type"),
                )
                return TextPart(content=content)
        except AttributeError:
            pass
        return None


def _extract_embedded(content: str) -> OutboundPayload | None:
    """Extract a structured JSON block embedded in plain text.

    When the LLM returns text like::

        Here are the labs.
        {"type": "choice", "content": "Pick one", "options": [...]}

    this function splits it into a composite message with a text part and
    the structured part.  Returns ``None`` if no embedded JSON is found.
    """
    idx = content.find('{"type"')
    if idx <= 0:
        return None
    try:
        candidate = json.loads(content[idx:].strip())
    except (json.JSONDecodeError, TypeError):
        return None
    parsed = _parse_structured(candidate)
    if parsed is None:
        return None
    prefix = content[:idx].strip()
    if not prefix:
        return parsed
    text_part = TextPart(content=prefix)
    # If the embedded block is already composite, prepend the text to its parts.
    if isinstance(parsed, CompositeMessage):
        return CompositeMessage(parts=[text_part, *parsed.parts])
    return CompositeMessage(parts=[text_part, parsed])


def parse_outbound(content: str) -> OutboundPayload:
    """Parse an LLM response into a typed outbound payload.

    Tries, in order: pure JSON, embedded JSON in text, plain text fallback.
    Handles markdown code fences around JSON.
    """
    stripped = _strip_code_fence(content)

    # 1. Pure JSON
    try:
        result = _parse_structured(json.loads(stripped))
        if result is not None:
            return result
    except (json.JSONDecodeError, TypeError):
        pass

    # 2. Text with embedded JSON block
    embedded = _extract_embedded(stripped)
    if embedded is not None:
        return embedded

    # 3. Plain text
    return TextPart(content=content)
