from typing import Optional, Any


def main(*args: Optional[Any], **kwargs: Optional[Any]) -> None:
    from classes.grabbers import FeedlyGrabber
    from classes.adapters import DrupalRESTAdapter
    from classes.notification_channels import SendPulseSMTPNotificationChannel
    from classes.converters import DataConverterFactory, FeedlyConverter
    from settings.general import zzr_settings, feedly_settings, sendpulse_settings

    feedly_grabber = FeedlyGrabber(settings=feedly_settings)
    sendpulse = SendPulseSMTPNotificationChannel(settings=sendpulse_settings)
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
