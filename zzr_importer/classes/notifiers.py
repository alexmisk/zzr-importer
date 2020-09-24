from typing import Set

from classes.notification_channels import NotificationChannel


class Notifier:
    def __init__(self) -> None:
        super().__init__()
        self._notification_channels: Set[NotificationChannel] = set()

    def add_notification_channel(self, channel: NotificationChannel) -> None:
        self._notification_channels.add(channel)

    def notify(self) -> None:
        [channel.notify() for channel in self._notification_channels]
