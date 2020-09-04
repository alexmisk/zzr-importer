from models.data.generic import Data
from classes.auth import RESTClient
from settings.grabbers import FeedlyGrabberSettings


class FeedlyGrabber(RESTClient):
    def __init__(self, settings: FeedlyGrabberSettings):
        super(FeedlyGrabber, self).__init__(settings)
        self._feed_url = settings.feed_url
        self._profile_url = settings.profile_url
        self._user_id = self._get_user_id()
        self.returned_posts_count = settings.returned_posts_count

    def _get_user_id(self):
        url = self._profile_url
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()["id"]
        return False

    def get_saved_posts(self, count=None):
        count = count or self.returned_posts_count
        url = self._feed_url
        payload = {
            "streamId": "user/" + self._user_id + "/tag/global.saved",
            "count": count,
        }
        response = self.session.get(url=url, params=payload)
        if response.status_code == 200:
            data = Data(provider="feedly", payload=response.json()["items"])
            return data
        return False
