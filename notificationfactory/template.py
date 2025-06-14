from abc import ABC, abstractmethod
from dataclasses import dataclass

from .model import NotificationType


@dataclass
class NotificationTemplate(ABC):
    message: str

    @abstractmethod
    def apply_template(self) -> str:
        pass

    @abstractmethod
    def notification_type(self) -> NotificationType:
        pass


@dataclass
class PushNotificationTemplate(NotificationTemplate):
    def apply_template(self) -> str:
        print("Applying Push notification template")
        return self.message

    def notification_type(self) -> NotificationType:
        return NotificationType.PUSH


@dataclass
class EmailNotificationTemplate(NotificationTemplate):
    def apply_template(self) -> str:
        print("Applying Email notification template")
        return self.message

    def notification_type(self) -> NotificationType:
        return NotificationType.EMAIL
