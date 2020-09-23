from abc import ABC, abstractmethod
from typing import Sequence, Set
from models.data.generic import Data
from models.drupal.nodes.generic import DrupalGenericNode
from models.drupal.nodes.zzr import ZZRNewsNode


class DataConverter(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def convert(data: Data) -> Sequence[DrupalGenericNode]:
        pass


class DataConverterFactory:
    def __init__(self) -> None:
        self._converters: Set[DataConverter] = set()

    def add_converter(self, converter: DataConverter) -> None:
        self._converters.add(converter)

    def convert(self, data: Data) -> Sequence[DrupalGenericNode]:
        for converter in self._converters:
            if converter.name == data.provider:
                return converter.convert(data)
        return []


class FeedlyConverter(DataConverter):
    name = "feedly"

    @staticmethod
    def convert(data: Data) -> Sequence[ZZRNewsNode]:
        nodes = []
        for post in data.payload:
            node = ZZRNewsNode()
            node.uuid = post["id"]
            node.title = post["title"]
            try:
                node.body = post["content"]["content"]
            except:
                node.body = post["summary"]["content"]
            node.origin_url = post["originId"]
            nodes.append(node)
        return nodes
