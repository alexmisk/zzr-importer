from requests_oauthlib import OAuth2Session  # type: ignore
from oauthlib.oauth2 import BackendApplicationClient, MissingTokenError  # type: ignore
from settings.adapters import RESTAdapterSettings


class RESTClient:
    def __init__(self, settings: RESTAdapterSettings) -> None:
        super().__init__()
        self.client = BackendApplicationClient(client_id=settings.client_id)
        self.session = OAuth2Session(client=self.client)
        try:
            self.session.fetch_token(
                token_url=settings.token_url,
                client_id=settings.client_id,
                client_secret=settings.client_secret,
            )
        except MissingTokenError:
            self.session.refresh_token(
                refresh_token=settings.refresh_token,
                token_url=settings.token_url,
                client_id=settings.client_id,
                client_secret=settings.client_secret,
                params={"grant_type": "refresh_token"},
            )
