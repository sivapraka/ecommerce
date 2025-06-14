import unittest

from config import *

from notificationfactory.abstract_factory import *
from notificationfactory.notification import *
from notificationfactory.sender import *
from notificationfactory.template import *


class TestNotificationFactory(unittest.TestCase):

    def test_methods(self):
        email_factory = EmailNotificationFactory()
        push_factory = PushNotificationFactory()
        methods = ["create_notification", "create_sender", "create_template"]
        for method in methods:
            self.assertTrue(
                hasattr(email_factory, method),
                f"If the abstract factory is correctly implemented, DocumentFactory should have a method named {method}.",
            )
            self.assertTrue(
                hasattr(push_factory, method),
                f"If the abstract factory is correctly implemented, DocumentFactory should have a method named {method}.",
            )

    def test_email_notification_factory(self):
        email_factory = EmailNotificationFactory()

        # Create mock data
        recipient = "test-user"
        sender = "test-sender"
        template_name = "test-template"

        # Create objects using the factory
        try:
            template = email_factory.create_template(template_name)
        except AttributeError as e:
            self.fail(
                "If the abstract factory is correctly implemented, EmailNotificationFactory should have a create_template method."
            )

        try:
            notification = email_factory.create_notification(
                recipient, template
            )
        except AttributeError as e:
            self.fail(
                "If the abstract factory is correctly implemented, EmailNotificationFactory should have a create_notification method."
            )

        try:
            sender = email_factory.create_sender(notification)
        except AttributeError as e:
            self.fail(
                "If the abstract factory is correctly implemented, EmailNotificationFactory should have a create_sender method."
            )

        # Check types of created objects
        self.assertIsInstance(
            template,
            EmailNotificationTemplate,
            "If the create_template method is called, it should return an object of type EmailNotificationTemplate.",
        )
        self.assertIsInstance(
            notification,
            EmailNotification,
            "If the create_notification method is called, it should return an object of type EmailNotification.",
        )
        self.assertIsInstance(
            sender,
            EmailNotificationSender,
            "If the create_sender method is called, it should return an object of type EmailNotificationSender.",
        )

    def test_push_notification_factory(self):
        push_factory = PushNotificationFactory()

        # Create mock data
        recipient = "test-device"
        template_name = "test-template"
        sender = "test-sender"

        # Create objects using the factory
        try:
            template = push_factory.create_template(template_name)
        except AttributeError as e:
            self.fail(
                "If the abstract factory is correctly implemented, PushNotificationFactory should have a create_template method."
            )

        try:
            notification = push_factory.create_notification(recipient, template)
        except AttributeError as e:
            self.fail(
                "If the abstract factory is correctly implemented, PushNotificationFactory should have a create_notification method."
            )

        try:
            sender = push_factory.create_sender(notification)
        except AttributeError as e:
            self.fail(
                "If the abstract factory is correctly implemented, PushNotificationFactory should have a create_sender method."
            )

        # Check types of created objects
        self.assertIsInstance(
            template,
            PushNotificationTemplate,
            "If the create_template method is called, it should return an object of type PushNotificationTemplate.",
        )
        self.assertIsInstance(
            notification,
            PushNotification,
            "If the create_notification method is called, it should return an object of type PushNotification.",
        )
        self.assertIsInstance(
            sender,
            PushNotificationSender,
            "If the create_sender method is called, it should return an object of type PushNotificationSender.",
        )


if __name__ == "__main__":
    unittest.main()
