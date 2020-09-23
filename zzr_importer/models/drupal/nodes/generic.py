from typing import Dict, Any
from uuid import uuid4
from pydantic import BaseModel


class DrupalGenericNode(BaseModel):
    uuid: str = str(uuid4())
    title: str = "Page"
    node_type: str = "page"

    def to_json(self) -> Dict[Any, Any]:
        return {
            "uuid": [{"value": self.uuid}],
            "type": [{"target_id": self.node_type}],
            "title": [{"value": self.title}],
        }
