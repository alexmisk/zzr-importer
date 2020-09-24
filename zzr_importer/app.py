from typing import Any, Optional

from classes.adapters import DrupalRESTAdapter
from classes.converters import DataConverterFactory, FeedlyConverter
from classes.grabbers import FeedlyGrabber
from classes.notification_channels import SendPulseNotificationChannel
from settings.general import feedly_settings, sendpulse_settings, zzr_settings


def main(*args: Optional[Any], **kwargs: Optional[Any]) -> None:

    feedly_grabber = FeedlyGrabber(settings=feedly_settings)
    sendpulse = SendPulseNotificationChannel(settings=sendpulse_settings)
    converters = DataConverterFactory()
    drupal_importer = DrupalRESTAdapter(
        settings=zzr_settings, converter_factory=converters
    )

    drupal_importer.add_notification_channel(sendpulse)
    converters.add_converter(FeedlyConverter())

    posts = feedly_grabber.get_saved_posts()
    drupal_importer.import_nodes(posts)


if __name__ == "__main__":
    main()
