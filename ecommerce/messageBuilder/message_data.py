from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import time

class MessageType(Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"

@dataclass(frozen=True)
class Message:
    message_type: MessageType
    content: str
    sender: str
    recipient: str
    is_delivered: bool
    timestamp: int

    @staticmethod
    def builder() -> MessageBuilder:
        return Message.MessageBuilder()

    class MessageBuilder:
        def __init__(self):
            self._message_type = None
            self._content = None
            self._sender = None
            self._recipient = None
            self._is_delivered = False
            self._timestamp = int(time.time())

        def with_type(self, message_type: MessageType) -> Message.MessageBuilder:
            self._message_type = message_type
            return self

        def with_content(self, content: str) -> Message.MessageBuilder:
            self._content = content
            return self

        def with_sender(self, sender: str) -> MessageBuilder:
            self._sender = sender
            return self

        def with_recipient(self, recipient: str) -> Message.MessageBuilder:
            self._recipient = recipient
            return self

        def with_delivery_status(self, is_delivered: bool) -> Message.MessageBuilder:
            self._is_delivered = is_delivered
            return self

        def with_timestamp(self, timestamp: int) -> Message.MessageBuilder:
            self._timestamp = timestamp
            return self

        def build(self) -> Message:
            if None in (self._message_type, self._content, self._sender, self._recipient):
                raise ValueError("Missing required fields for Message creation.")
            return Message(
                message_type=self._message_type,
                content=self._content,
                sender=self._sender,
                recipient=self._recipient,
                is_delivered=self._is_delivered,
                timestamp=self._timestamp
            )


if __name__ == '__main__':
    # Usage Example
    message = Message.builder() \
        .with_type(MessageType.TEXT) \
        .with_content("Hello, World!") \
        .with_sender("me@example.com") \
        .with_recipient("you@example.com") \
        .with_delivery_status(True) \
        .build()

    print(message)
