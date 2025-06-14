import unittest

from messageBuilder.message_data import Message, MessageType


class TestMessageBuilder(unittest.TestCase):

    def test_build_without_setting_fields(self):
        builder = Message.builder()
        message = builder.build()
        self.assertIsNotNone(
            message, "If the build method is called, it should return a non-None value"
        )
        self.assertIsInstance(
            message,
            Message,
            "If the build method is called, it should return an instance of Message",
        )

    def test_build_no_fields_set(self):
        builder = Message.builder()
        message = builder.build()

        self.assertIsNotNone(
            message, "If the build method is called, it should return a non-None value"
        )
        self.assertIsInstance(
            message,
            Message,
            "If the build method is called, it should return an instance of Message",
        )

        # Assert that all fields are None
        self.assertIsNone(
            message.message_type, "If no value is set, message_type should be None"
        )
        self.assertIsNone(message.content, "If no value is set, content should be None")
        self.assertIsNone(message.sender, "If no value is set, sender should be None")
        self.assertIsNone(
            message.recipient, "If no value is set, recipient should be None"
        )
        self.assertIsNone(
            message.is_delivered, "If no value is set, is_delivered should be None"
        )
        self.assertIsNone(
            message.timestamp, "If no value is set, timestamp should be None"
        )

    def test_build_with_updated_instance(self):
        builder = Message.builder()
        builder._instance.message_type = MessageType.TEXT
        builder._instance.content = "Hello World"
        builder._instance.sender = "sender@example.com"
        builder._instance.recipient = "recipient@example.com"
        builder._instance.is_delivered = False
        builder._instance.timestamp = 123456789

        message = builder.build()

        self.assertEqual(
            message.message_type,
            MessageType.TEXT,
            "If the message_type is set, it should be returned",
        )
        self.assertEqual(
            message.content,
            "Hello World",
            "If the content is set, it should be returned",
        )
        self.assertEqual(
            message.sender,
            "sender@example.com",
            "If the sender is set, it should be returned",
        )
        self.assertEqual(
            message.recipient,
            "recipient@example.com",
            "If the recipient is set, it should be returned",
        )
        self.assertFalse(
            message.is_delivered,
            "If the is_delivered is set to False, it should be returned",
        )
        self.assertEqual(
            message.timestamp,
            123456789,
            "If the timestamp is set, it should be returned",
        )


if __name__ == "__main__":
    unittest.main()
