from models.drupal.nodes.generic import DrupalGenericNode
from pydantic.dataclasses import dataclass
from pydantic import AnyUrl


@dataclass
class ZZRNewsNode(DrupalGenericNode):
    body: str = None
    header_photo: str = None
    origin_url: AnyUrl = None
    parther: str = None
    news_type: str = "industry_news"

    def __post_init__(self):
        self.node_type = "news"

    def json(self):
        return {
            "uuid": [{"value": self.uuid}],
            "type": [{"target_id": self.node_type}],
            "title": [{"value": self.title}],
            "body": [{"value": self.body, "format": "full_html"}],
            "field_type": [{"value": self.news_type}],
            "field_origin_url": [{"value": self.origin_url}],
        }
