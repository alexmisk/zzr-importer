from abc import ABC, abstractmethod
from classes.auth import RESTClient
from settings.notification_channels import SendPulseSMTPNotificationChannelSettings


class NotificationChannel(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class SendPulseSMTPNotificationChannel(NotificationChannel, RESTClient):
    def __init__(self, settings: SendPulseSMTPNotificationChannelSettings) -> None:
        super().__init__(settings)
        self._name = settings.name
        self.emails = settings.emails
        self.base_url = settings.base_url

    @property
    def name(self) -> str:
        return self._name

    def notify(self) -> None:
        url = self.base_url + "/smtp/emails"
        for email in self.emails:
            payload = {
                "email": {
                    "text": "Есть новости на модерацию https://zzr.ru/admin/moderation/news",
                    "subject": "На zzr.ru появились новости для модерации",
                    "from": {"name": "ZZR Robot", "email": "robot@zzr.ru"},
                    "to": [{"name": email, "email": email}],
                }
            }
            self.session.post(url, json=payload)
