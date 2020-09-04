def main(*args, **kwargs):
    from classes.grabbers import FeedlyGrabber
    from classes.adapters import DrupalRESTAdapter
    from classes.notification_channels import SendPulseSMTPNotificationChannel
    from settings.general import zzr_settings, feedly_settings, sendpulse_settings

    feedly_grabber = FeedlyGrabber(settings=feedly_settings)
    drupal_importer = DrupalRESTAdapter(settings=zzr_settings)
    sendpulse = SendPulseSMTPNotificationChannel(settings=sendpulse_settings)

    drupal_importer.add_notification_channel(sendpulse)
    posts = feedly_grabber.get_saved_posts()
    drupal_importer.import_nodes(posts)


if __name__ == "__main__":
    main()
