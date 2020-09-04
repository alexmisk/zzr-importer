from classes.notification_channels import NotificationChannel


class Notifier:
    def __init__(self):
        super().__init__()
        self._notification_channels = []

    def add_notification_channel(self, channel: NotificationChannel):
        if not (channel in self._notification_channels):
            self._notification_channels.append(channel)

    def notify(self):
        [channel.notify() for channel in self._notification_channels]
