import unittest

from notification import *
from notification.factory import NotificationFactory
from notification.products import NotificationType, EmailNotification, SmsNotification, PushNotification


class TestNotification(unittest.TestCase):
    def setUp(self):
        self.notification = SmsNotification("1234567890", "0987654321", "Hello, World!")

    def test_inheritance(self):
        self.assertIsInstance(
            self.notification,
            SmsNotification,
            "If there is a common parent Notification class, the SmsNotification class should inherit from it",
        )

    def test_fields(self):
        self.assertTrue(
            hasattr(self.notification, "recipient"),
            "If there is a common parent Notification class, it should have a recipient field",
        )
        self.assertTrue(
            hasattr(self.notification, "sender"),
            "If there is a common parent Notification class, it should have a sender field",
        )
        self.assertTrue(
            hasattr(self.notification, "message"),
            "If there is a common parent Notification class, it should have a message field",
        )

    def test_methods(self):
        self.assertTrue(
            hasattr(self.notification, "send_notification"),
            "If there is a common parent Notification class, it should have a send_notification method",
        )
        self.assertTrue(
            hasattr(self.notification, "notification_type"),
            "If there is a common parent Notification class, it should have a notification_type method",
        )

    def test_type_check(self):
        self.assertIsInstance(
            self.notification.recipient,
            str,
            "If there is a common parent Notification class, the recipient field should be a string",
        )
        self.assertIsInstance(
            self.notification.sender,
            str,
            "If there is a common parent Notification class, the sender field should be a string",
        )
        self.assertIsInstance(
            self.notification.message,
            str,
            "If there is a common parent Notification class, the message field should be a string",
        )


class TestNotificationFactory(unittest.TestCase):
    def test_create_sms(self):
        sms_notification = NotificationFactory.create_notification(
            NotificationType.SMS, "1234567890", "0987654321", "Hello, World!"
        )
        self.assertIsInstance(
            sms_notification,
            SmsNotification,
            "If the requested format is SMS, the factory should return a SmsNotification",
        )

    def test_create_email(self):
        email_notification = NotificationFactory.create_notification(
            NotificationType.EMAIL, "1234567890", "0987654321", "Hello, World!"
        )
        self.assertIsInstance(
            email_notification,
            EmailNotification,
            "If the requested format is EMAIL, the factory should return a EmailNotification",
        )

    def test_create_push(self):
        push_notification = NotificationFactory.create_notification(
            NotificationType.PUSH, "1234567890", "0987654321", "Hello, World!"
        )
        self.assertIsInstance(
            push_notification,
            PushNotification,
            "If the requested format is PUSH, the factory should return a PushNotification",
        )


if __name__ == "__main__":
    unittest.main()
