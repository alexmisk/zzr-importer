from pydantic.dataclasses import dataclass
from typing import List
from pydantic import HttpUrl, EmailStr


@dataclass
class SendPulseSMTPNotificationChannelSettings:
    client_id: str
    client_secret: str
    token_url: HttpUrl
    base_url: HttpUrl
    emails: List[EmailStr]
    name: str = "SendPulse"
