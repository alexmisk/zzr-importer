from models.data.generic import Data
from models.drupal.nodes.zzr import ZZRNewsNode


class DataConverter:
    @staticmethod
    def convert(data: Data):
        if data.provider == "feedly":
            return FeedlyConverter.convert(data)
        else:
            return None


class FeedlyConverter:
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
