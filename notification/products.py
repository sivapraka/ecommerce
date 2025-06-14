from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

# COMPLETE THIS CLASS
@dataclass
class Notification(ABC):
    recipient: str
    message: str

    @abstractmethod
    def send_notification(self):
        pass

    @abstractmethod
    def notification_type(self):
        pass

class NotificationType(Enum):
    EMAIL = "Email"
    PUSH = "Push"
    SMS = "SMS"

@dataclass
class EmailNotification(Notification):
    recipient: str
    sender: str
    message: str

    def send_notification(self):
        print(f"Email sent to {self.recipient} from {self.sender}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.EMAIL


@dataclass
class PushNotification(Notification):
    recipient: str
    message: str

    def send_notification(self):
        print(f"Push notification sent to device {self.recipient}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.PUSH


@dataclass
class SmsNotification(Notification):
    recipient: str
    message: str
    sender: str

    def send_notification(self):
        print(f"SMS sent to {self.recipient}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.SMS
