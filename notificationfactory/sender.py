from abc import ABC, abstractmethod
from .model import NotificationType
from .notification import Notification


class NotificationSender(ABC):
    def __init__(self, notification: Notification):
        self.notification = notification

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def notification_type(self):
        pass


class EmailNotificationSender(NotificationSender):
    def __init__(self, notification: Notification):
        super().__init__(notification)

    def send(self):
        print(f"Sending Email notification to {self.notification.recipient}")

    def notification_type(self):
        return NotificationType.EMAIL


class PushNotificationSender(NotificationSender):
    def __init__(self, notification: Notification):
        super().__init__(notification)

    def send(self):
        print(f"Sending Push notification to {self.notification.recipient}")

    def notification_type(self):
        return NotificationType.PUSH
