from abc import ABC, abstractmethod
from notificationfactory.notification import *
from notificationfactory.sender import *
from notificationfactory.template import *


class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self)->Notification:
        pass
    @abstractmethod
    def create_template(self)->NotificationTemplate:
        pass
    @abstractmethod
    def create_sender(self)->NotificationSender:
        pass

class EmailNotificationFactory(NotificationFactory):

        def create_notification(self,recipient:str, template:NotificationTemplate,sender:str=None)->Notification:
            return EmailNotification(recipient=recipient, template=template,sender=sender)
        def create_template(self,template:str)->NotificationTemplate:
            return EmailNotificationTemplate(template)
        def create_sender(self,sender:Notification)->NotificationSender:
            return EmailNotificationSender(sender)

class PushNotificationFactory(NotificationFactory):
    def create_notification(self, recipient: str, template: NotificationTemplate, sender: str = None) -> Notification:
        return PushNotification(recipient=recipient, template=template, sender=sender)

    def create_template(self, template: str) -> NotificationTemplate:
        return PushNotificationTemplate(template)

    def create_sender(self, sender: Notification) -> NotificationSender:
        return PushNotificationSender(sender)
