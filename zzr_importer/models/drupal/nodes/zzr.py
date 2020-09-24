from typing import Any, Dict, Optional

from pydantic import AnyUrl, validator

from models.drupal.nodes.generic import DrupalGenericNode


class ZZRNewsNode(DrupalGenericNode):
    body: Optional[str] = None
    header_photo: Optional[str] = None
    origin_url: Optional[AnyUrl] = None
    partner: Optional[str] = None
    news_type: str = "industry_news"

    @validator("node_type", pre=True, always=True)
    def set_node_type(cls, v: str) -> str:
        return "news"

    def to_json(self) -> Dict[Any, Any]:
        return {
            "uuid": [{"value": self.uuid}],
            "type": [{"target_id": self.node_type}],
            "title": [{"value": self.title}],
            "body": [{"value": self.body, "format": "full_html"}],
            "field_type": [{"value": self.news_type}],
            "field_origin_url": [{"value": self.origin_url}],
        }
