from pydantic.dataclasses import dataclass
from pydantic import HttpUrl


@dataclass
class FeedlyGrabberSettings:
    refresh_token: str
    client_id: str = "feedlydev"
    client_secret: str = "feedlydev"
    token_url: HttpUrl = "https://cloud.feedly.com/v3/auth/token"
    feed_url: HttpUrl = "https://cloud.feedly.com/v3/streams/contents"
    profile_url: HttpUrl = "https://cloud.feedly.com/v3/profile"
    returned_posts_count: int = 20
