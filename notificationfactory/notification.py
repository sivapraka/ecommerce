from abc import ABC, abstractmethod
from dataclasses import dataclass

from .template import NotificationTemplate
from .model import NotificationType


@dataclass
class Notification(ABC):
    recipient: str
    template: NotificationTemplate

    @abstractmethod
    def notification_type(self) -> NotificationType:
        pass

    @abstractmethod
    def send_notification(self):
        pass


@dataclass
class EmailNotification(Notification):
    sender: str

    def notification_type(self) -> NotificationType:
        return NotificationType.EMAIL

    def send_notification(self):
        # Logic to send an email
        print(f"Email sent to {self.recipient} from {self.sender}")
        print("Message:", self.template.message)


@dataclass
class PushNotification(Notification):
    sender: str
    def notification_type(self) -> NotificationType:
        return NotificationType.PUSH

    def send_notification(self):
        # Logic to send a push notification
        print(f"Push notification sent to device {self.recipient}")
        print("Message:", self.template.message)
