from __future__ import annotations

import threading
from typing import Type, Any

from ecommerce.ConfigManager import FileBasedConfigurationManager


class FileBasedConfigurationManagerImpl(FileBasedConfigurationManager):
    _instance: FileBasedConfigurationManagerImpl | None = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_instance() -> FileBasedConfigurationManager:
        with FileBasedConfigurationManagerImpl._lock:
            if FileBasedConfigurationManagerImpl._instance is None:
                FileBasedConfigurationManagerImpl._instance = FileBasedConfigurationManagerImpl()
            return FileBasedConfigurationManagerImpl._instance

    @staticmethod
    def reset_instance() -> None:
        with FileBasedConfigurationManagerImpl._lock:
            FileBasedConfigurationManagerImpl._instance = None
        #pass

    def get_configuration(self, key: str) -> str:
        return self.properties.get(key, None)

    def get_configuration_with_type(self, key: str, type_: Type) -> Any:
        value = self.get_configuration(key)
        if value is None:
            return None  # Prevent TypeError by returning None
        return self.convert(value, type_)
        #raise NotImplementedError("Unimplemented method 'get_configuration_with_type'")

    def set_configuration(self, key: str, value: str) -> None:
        self.properties[key] = value
        #raise NotImplementedError("Unimplemented method 'set_configuration'")

    def remove_configuration(self, key: str) -> None:
        self.properties.pop(key, None)
        #raise NotImplementedError("Unimplemented method 'remove_configuration'")

    def clear(self) -> None:
        self.properties.clear()
        #raise NotImplementedError("Unimplemented method 'clear'")
