from typing import List

from pydantic import EmailStr, HttpUrl

from settings.adapters import RESTAdapterSettings


class SendPulseSMTPNotificationChannelSettings(RESTAdapterSettings):
    client_id: str
    client_secret: str
    base_url: HttpUrl
    token_url: HttpUrl
    emails: List[EmailStr]
    name: str = "SendPulse"
