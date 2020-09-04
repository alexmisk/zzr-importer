from pydantic.dataclasses import dataclass
from pydantic import HttpUrl


@dataclass
class DrupalRESTAdapterSettings:
    client_id: str
    client_secret: str
    token_url: HttpUrl
    base_url: HttpUrl
    authorization_url: HttpUrl
