from pydantic.dataclasses import dataclass
from typing import Any


@dataclass
class Data:
    provider: str
    payload: Any
