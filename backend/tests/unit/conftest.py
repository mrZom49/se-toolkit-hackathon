"""Unit-test configuration — runs before any test module is imported."""

import os

# The import chain (routers → database → settings) requires LMS_API_KEY.
# Unit tests never call the real API, so a dummy value is sufficient.
os.environ.setdefault("LMS_API_KEY", "test")
