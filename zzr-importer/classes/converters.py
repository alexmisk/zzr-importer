from abc import ABC, abstractmethod
from models.data.generic import Data
from models.drupal.nodes.zzr import ZZRNewsNode


class DataConverter(ABC):
    @property
    @abstractmethod
    def name():
        pass

    @staticmethod
    @abstractmethod
    def convert(data: Data):
        pass


class DataConverterFactory:
    def __init__(self):
        self._converters = set()

    def add_converter(self, converter: DataConverter):
        self._converters.add(converter)

    def convert(self, data: Data):
        for converter in self._converters:
            if converter.name == data.provider:
                return converter.convert(data)
        return False


class FeedlyConverter(DataConverter):
    name = "feedly"

    @staticmethod
    def convert(data: Data):
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
            nodes.append(node.json())
        return nodes
