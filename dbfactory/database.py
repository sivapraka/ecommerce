from abc import ABC, abstractmethod


class Database(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def supports_type(self) -> str:
        pass

    def connect(self):
        print(f"Connecting to {self.supports_type()} database: {self.name}")
