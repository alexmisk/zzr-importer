from classes.auth import RESTClient
from classes.converters import DataConverterFactory
from classes.notifiers import Notifier
from models.data.generic import Data
from models.drupal.nodes.generic import DrupalGenericNode
from settings.adapters import RESTAdapterSettings


class DrupalRESTAdapter(RESTClient, Notifier):
    def __init__(
        self,
        settings: RESTAdapterSettings,
        converter_factory: DataConverterFactory = DataConverterFactory(),
    ) -> None:
        super().__init__(settings)
        self._base_url = settings.base_url
        self._converter_factory = converter_factory

    def _create_node(self, payload: DrupalGenericNode) -> int:
        url = str(self._base_url) + "/node?_format=json"
        response = self.session.post(url=url, json=payload.to_json())
        return int(response.status_code)

    def import_nodes(self, data: Data) -> None:
        nodes = self._converter_factory.convert(data)
        updated = False
        for node in nodes:
            response = self._create_node(node)
            if response == 201:
                updated = True
        if updated:
            self.notify()
