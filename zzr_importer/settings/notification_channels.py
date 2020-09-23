from settings.adapters import RESTAdapterSettings
from typing import List
from pydantic import HttpUrl, EmailStr


class SendPulseSMTPNotificationChannelSettings(RESTAdapterSettings):
    client_id: str
    client_secret: str
    base_url: HttpUrl
    token_url: HttpUrl
    emails: List[EmailStr]
    name: str = "SendPulse"
