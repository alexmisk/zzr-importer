from settings.adapters import DrupalRESTAdapterSettings
from classes.auth import RESTClient
from classes.notifiers import Notifier
from classes.converters import DataConverter
from models.data.generic import Data


class DrupalRESTAdapter(RESTClient, Notifier):
    def __init__(self, settings: DrupalRESTAdapterSettings):
        super().__init__(settings)
        self._base_url = settings.base_url

    def _create_node(self, payload):
        url = self._base_url + "/node?_format=json"
        response = self.session.post(url=url, json=payload)
        return response.status_code

    def import_nodes(self, data: Data):
        nodes = DataConverter.convert(data)
        updated = False
        for node in nodes:
            response = self._create_node(node)
            if response == 201:
                updated = True
        if updated:
            self.notify()
