import os

from pydantic import EmailStr, HttpUrl
from pydantic.tools import parse_obj_as

from settings.adapters import RESTAdapterSettings
from settings.grabbers import FeedlyGrabberSettings
from settings.notification_channels import \
    SendPulseSMTPNotificationChannelSettings

zzr_settings = RESTAdapterSettings(
    client_id=os.environ["ZZR_CLIENT_ID"],
    client_secret=os.environ["ZZR_CLIENT_SECRET"],
    token_url=parse_obj_as(HttpUrl, os.environ["ZZR_TOKEN_URL"]),
    base_url=parse_obj_as(HttpUrl, os.environ["ZZR_BASE_URL"]),
    authorization_url=parse_obj_as(HttpUrl, os.environ["ZZR_AUTHORIZATION_URL"]),
)

feedly_settings = FeedlyGrabberSettings(
    refresh_token=str(os.environ.get("FEEDLY_REFRESH_TOKEN")),
    returned_posts_count=int(os.environ["FEEDLY_RETURNED_POSTS_COUNT"]),
)

emails = [
    EmailStr(email) for email in os.environ["SENDPULSE_NOTIFICATION_EMAILS"].split(",")
]

sendpulse_settings = SendPulseSMTPNotificationChannelSettings(
    emails=emails,
    client_id=os.environ["SENDPULSE_CLIENT_ID"],
    client_secret=os.environ["SENDPULSE_CLIENT_SECRET"],
    token_url=parse_obj_as(HttpUrl, os.environ["SENDPULSE_TOKEN_URL"]),
    base_url=parse_obj_as(HttpUrl, os.environ["SENDPULSE_BASE_URL"]),
)
