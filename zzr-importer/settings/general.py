import os
from settings.adapters import DrupalRESTAdapterSettings
from settings.grabbers import FeedlyGrabberSettings
from settings.notification_channels import SendPulseSMTPNotificationChannelSettings

zzr_settings = DrupalRESTAdapterSettings(
    client_id=os.environ.get("ZZR_CLIENT_ID"),
    client_secret=os.environ.get("ZZR_CLIENT_SECRET"),
    token_url=os.environ.get("ZZR_TOKEN_URL"),
    base_url=os.environ.get("ZZR_BASE_URL"),
    authorization_url=os.environ.get("ZZR_AUTHORIZATION_URL"),
)

feedly_settings = FeedlyGrabberSettings(
    refresh_token=os.environ.get("FEEDLY_REFRESH_TOKEN"),
    returned_posts_count=os.environ.get("FEEDLY_RETURNED_POSTS_COUNT"),
)

sendpulse_settings = SendPulseSMTPNotificationChannelSettings(
    emails=os.environ.get("SENDPULSE_NOTIFICATION_EMAILS").split(","),
    client_id=os.environ.get("SENDPULSE_CLIENT_ID"),
    client_secret=os.environ.get("SENDPULSE_CLIENT_SECRET"),
    token_url=os.environ.get("SENDPULSE_TOKEN_URL"),
    base_url=os.environ.get("SENDPULSE_BASE_URL"),
)
