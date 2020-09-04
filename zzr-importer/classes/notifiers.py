from classes.notification_channels import NotificationChannel


class Notifier:
    def __init__(self):
        super().__init__()
        self._notification_channels = set()

    def add_notification_channel(self, channel: NotificationChannel):
        self._notification_channels.add(channel)

    def notify(self):
        [channel.notify() for channel in self._notification_channels]
