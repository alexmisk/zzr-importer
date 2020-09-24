from pydantic import HttpUrl
from pydantic.tools import parse_obj_as

from settings.adapters import RESTAdapterSettings


class FeedlyGrabberSettings(RESTAdapterSettings):
    client_id = "feedlydev"
    client_secret = "feedlydev"
    token_url = parse_obj_as(HttpUrl, "https://cloud.feedly.com/v3/auth/token")
    profile_url: HttpUrl = "https://cloud.feedly.com/v3/profile"  # type: ignore
    feed_url: HttpUrl = "https://cloud.feedly.com/v3/streams/contents"  # type: ignore
    returned_posts_count: int = 20
