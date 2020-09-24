from typing import Any

from pydantic import BaseModel


class Data(BaseModel):
    provider: str = ""
    payload: Any = None
