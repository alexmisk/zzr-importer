from uuid import uuid4
from pydantic.dataclasses import dataclass


@dataclass
class DrupalGenericNode:
    uuid: str = str(uuid4())
    title: str = "Page"
    node_type: str = "page"

    def json(self):
        return {
            "uuid": [{"value": self.uuid}],
            "type": [{"target_id": self.node_type}],
            "title": [{"value": self.title}],
        }
