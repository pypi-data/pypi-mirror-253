from contextvars import ContextVar
from contextlib import asynccontextmanager
from typing import Any

context_data = ContextVar("context_data", default={})

@asynccontextmanager
async def load_context(data: dict[str, Any]):
    token = context_data.set(data)
    try:
        yield
    finally:
        context_data.reset(token)