from notification.products import NotificationType, EmailNotification, Notification, SmsNotification, PushNotification


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: NotificationType, recipient: str, message: str, sender: str = None):
        if notification_type == NotificationType.EMAIL:
            if sender is None:
                raise ValueError("Sender is required for EmailNotification")
            return EmailNotification(recipient=recipient, message=message, sender=sender)
        elif notification_type == NotificationType.PUSH:
            return PushNotification(recipient=recipient, message=message)
        elif notification_type == NotificationType.SMS:
            return SmsNotification(recipient=recipient, message=message,sender=sender)
        else:
            raise ValueError(f"Unsupported notification type: {notification_type}")